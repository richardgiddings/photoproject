from django.template import RequestContext
from .models import Photo, Category
from .forms import CategorySelectionForm
from django.shortcuts import render_to_response
from django.db.models import Q

def index(request):

    photo_list = Photo.objects.order_by('-photo_date')[:5]

    return render_to_response("photosite/index.html", { 
            "category_list": CategorySelectionForm(), 
            "photo_list": photo_list,
            })

def cat_filter(request):
    
    category_id = request.GET.get('category_list')
    if category_id == '':
    	photo_list = Photo.objects.order_by('-photo_date')[:5]
    else:
    	photo_list = Photo.objects.order_by('-photo_date').filter(category=category_id)[:5]

    category_list = CategorySelectionForm(request.GET)	

    return render_to_response("photosite/index.html", { 
            "category_list": category_list, 
            "photo_list": photo_list,
            })

def photo_search(request):
    
    photo_search = request.GET.get('search_term')

    photo_list = Photo.objects.filter(Q(photo_title__icontains=photo_search) | Q(photo_description__icontains=photo_search))
    photo_list = photo_list.order_by('-photo_date')[:5]

    return render_to_response("photosite/index.html", {
            "searched_for": photo_search, 
            "category_list": CategorySelectionForm(), 
            "photo_list": photo_list,
            })