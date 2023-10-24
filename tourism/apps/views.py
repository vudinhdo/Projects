from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import Tour, Blogs, BookTour, City, Comments, User
from django.contrib.auth.decorators import login_required


def index(req):
    return render(req, "Pages/index.html")


def destination(req):
    destination = Tour.objects.all()
    return render(req, "Pages/tour/destination.html", {"destination": destination})


def dSingle(req, id):
    dSingle = Tour.objects.get(id=id)
    return render(req, "Pages/tour/destination_single.html", {"dSingle": dSingle})


def blogs(req):
    tus = Blogs.objects.all()
    return render(req, "Pages/Blogs/blog.html", {"tus": tus})


def blog_single(req, blog_id):
    blog = Blogs.objects.get(id=blog_id)

    return render(req, "Pages/Blogs/blog_single.html", {"blog": blog})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session["username"] = username
            return redirect('index')
        else:
            return render(request, 'Pages/login/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'Pages/login/login.html')


def logout_view(request):
    logout(request)
    return redirect("/")


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login_view')
        return redirect("index")

    else:
        return render(request, 'Pages/login/register.html')


# def add_Author(request):
#     if request.method == 'POST':

@login_required
def profile(request):
    if request.session.get("is_logged_in", True):
        return render(request, "Pages/profile/profile.html")
    else:
        return redirect("login_view")


def add_Comment(request, blog_id, user_id):
    blog = Blogs.objects.get(id=blog_id)
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        body_comment = request.POST["body_comment"]
        comment = Comments(blog=blog, user_comment=user, body_comment=body_comment)
        comment.save()
        return render(request, "Pages/Blogs/blog_single.html", {"blog": blog})
    else:
        return render(request, "Pages/Blogs/blog.html")


def search(request):
    if request.method == "GET":
        diemden = request.GET["diemden"]
        destination = Tour.objects.filter(name__contains=diemden)
        return render(request, "Pages/tour/destination.html", {"destination": destination})


def search_blog(request):
    if request.method == "GET":
        baiviet = request.GET["baiviet"]
        tus = Blogs.objects.filter(name__contains=baiviet)
        return render(request, "Pages/Blogs/blog.html", {"tus": tus})


@login_required
def get_edit_username(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "Pages/edit_profile/edit_username.html", {"user": user})


def edit_username(request, user_id):
    user = User.objects.get(id=user_id)
    username = request.POST["username"]
    user.username = username
    user.save()
    return redirect("profile")


@login_required
def get_edit_email(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "Pages/edit_profile/edit_email.html", {"user": user})


def edit_email(request, user_id):
    user = User.objects.get(id=user_id)
    email_edit = request.POST["email"]
    user.email = email_edit
    user.save()
    return redirect("profile")


@login_required
def get_edit_password(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "Pages/edit_profile/edit_password.html", {"user": user})


def edit_password(request, user_id):
    user = User.objects.get(id=user_id)
    password = request.POST["password"]
    user.password = password
    user.save()
    return redirect("profile")


@login_required
def check_out_tour(request, user_id, tour_id):
    user = User.objects.get(id=user_id)
    tour = Tour.objects.get(id=tour_id)
    if request.method == "POST":
        booking = BookTour(user=user, tour=tour)
        booking.save()
        return render(request, "Pages/index.html")


@login_required
def show_book_tour(request, user_id):
    user = User.objects.get(id=user_id)
    tours = BookTour.objects.get(user=user)
    return render(request, "Pages/tour/check_out.html", {"tours": tours})
