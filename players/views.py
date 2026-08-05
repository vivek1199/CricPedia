from django.shortcuts import redirect, render
from .models import Player, Favorite
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q, Sum
from django.http import HttpResponseForbidden 
from django.core.paginator import Paginator
from .forms import ContactForm
from django.contrib import messages

def home(request):

    featured_players = Player.objects.filter(
        featured=True
    ).order_by("featured_order")[:3]

    total_players = Player.objects.count()

    total_countries = Player.objects.values(
        "country"
    ).distinct().count()

    total_runs = Player.objects.aggregate(
        Sum("runs")
    )["runs__sum"] or 0

    total_wickets = Player.objects.aggregate(
        Sum("wickets")
    )["wickets__sum"] or 0

    latest_players = Player.objects.order_by("-id")[:3]
    
    top_run_scorers = Player.objects.order_by("-runs")[:5]
    
    top_wicket_takers = Player.objects.order_by("-wickets")[:5]

    return render(
        request,
        "players/home.html",
        {
            "featured_players": featured_players,
            "latest_players": latest_players,
            "total_players": total_players,
            "total_countries": total_countries,
            "total_runs": total_runs,
            "total_wickets": total_wickets,
            "top_run_scorers": top_run_scorers,
            "top_wicket_takers": top_wicket_takers,
        }
    )

def player_list(request):

    search = request.GET.get("search")
    country = request.GET.get("country")

    players = Player.objects.all()

    if search:

        players = players.filter(

            Q(name__icontains=search) |
            Q(country__icontains=search) |
            Q(role__icontains=search)

        )

    if country:

        players = players.filter(country=country)

    countries = Player.objects.values_list(
        "country",
        flat=True
    ).distinct().order_by("country")
    
    total_players = Player.objects.count()

    total_countries = Player.objects.values(
        "country"
    ).distinct().count()

    total_runs = Player.objects.aggregate(
        Sum("runs")
    )["runs__sum"] or 0

    total_wickets = Player.objects.aggregate(
        Sum("wickets")
    )["wickets__sum"] or 0

    paginator = Paginator(players, 6)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "players/player_list.html",
        {
            "page_obj": page_obj,

            "countries": countries,

            "search": search,

            "selected_country": country,

            "total_players": total_players,

            "total_countries": total_countries,

            "total_runs": total_runs,

            "total_wickets": total_wickets,
        }
    )
    
def player_detail(request, id):
    player = Player.objects.get(id=id)

    is_favorite = False

    if request.user.is_authenticated:

        is_favorite = Favorite.objects.filter(
            user=request.user,
            player=player
        ).exists()

    return render(
        request,
        "players/player_detail.html",
        {
            "player": player,
            "is_favorite": is_favorite,
        }
    )
    
    
@login_required
def add_player(request):

    if request.method == "POST":

        form = PlayerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Player added successfully!"
            )

            return redirect("player_list")

    else:

        form = PlayerForm()

    return render(
        request,
        "players/add_player.html",
        {"form": form}
    )
    
@staff_member_required
def edit_player(request, id):

    player = Player.objects.get(id=id)

    if request.method == "POST":

        form = PlayerForm(
            request.POST,
            request.FILES,
            instance=player
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Player updated successfully!"
            )

            return redirect("player_detail", id=player.id)

    else:

        form = PlayerForm(instance=player)

    return render(
        request,
        "players/edit_player.html",
        {
            "form": form,
            "player": player
        }
    )
    
@staff_member_required
def delete_player(request, id):

    player = Player.objects.get(id=id)

    if request.method == "POST":
        player.delete()
        messages.success(
            request,
            "Player deleted successfully!"
        )
        return redirect("player_list")

    return render(
        request,
        "players/delete_player.html",
        {"player": player}
    )
    
def about(request):

    return render(

        request,

        "players/about.html"

    )
    
def compare_players(request):

    players = Player.objects.all().order_by("name")

    player1 = None
    player2 = None

    player1_id = request.GET.get("player1")
    player2_id = request.GET.get("player2")

    if player1_id and player2_id:

        player1 = Player.objects.get(id=player1_id)
        player2 = Player.objects.get(id=player2_id)

    return render(
        request,
        "players/compare_players.html",
        {
            "players": players,
            "player1": player1,
            "player2": player2,
        }
    )
    
@login_required
def add_favorite(request, player_id):

    player = Player.objects.get(id=player_id)

    Favorite.objects.get_or_create(
        user=request.user,
        player=player
    )
    messages.success(
        request,
        "Added to Favorites ❤️"
    )

    return redirect("player_detail", id=player.id)

@login_required
def favorite_players(request):

    favorites = Favorite.objects.filter(
        user=request.user
    )

    return render(
        request,
        "players/favorite_players.html",
        {
            "favorites": favorites,
        }
    )
    
@login_required
def remove_favorite(request, player_id):

    Favorite.objects.filter(
        user=request.user,
        player_id=player_id
    ).delete()
    
    messages.success(
        request,
        "Removed from Favorites."
    )

    return redirect("favorite_players")

def contact(request):

    form = ContactForm()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(
                request,
                "Thank you! Your message has been sent."
            )

            return redirect("contact")

    return render(
        request,
        "players/contact.html",
        {
            "form": form,
        }
    )