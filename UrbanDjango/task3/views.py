from django.shortcuts import render

def platform_view(request):
    return render(request, 'third_task/platform.html')

def games_view(request):
    items = {
        'Metal Gear Rising: Revengeance': ' ',
        'Silent Hill 2': ' ',
        'BioShock Infinite': '',
    }
    return render(request, 'third_task/games.html', {'items': items})

def cart_view(request):
    return render(request, 'third_task/cart.html')

