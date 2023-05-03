from django.shortcuts import redirect


def return_redirect_home(request):
    if not request.user.is_authenticated:
        return redirect('home')
