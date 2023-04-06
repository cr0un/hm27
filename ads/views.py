from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Ad
from django.http import Http404
import json


# Create your views here.
def index(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": float(ad.price),
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
                "category": {
                    "id": ad.category.id,
                    "name": ad.category.name
                },
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ad()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.description = ad_data["description"]
        ad.address = ad_data["address"]
        ad.is_published = ad_data["is_published"]

        # Получаем категорию по id и присваиваем ее объявлению
        category_id = ad_data["category_id"]
        category = Category.objects.get(id=category_id)
        ad.category = category

        ad.save()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": float(ad.price),
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
            "category": {
                "id": ad.category.id,
                "name": ad.category.name
            },
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({"message": "Данного товара не существует"}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": float(ad.price),
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
            "category": {
                "id": ad.category.id,
                "name": ad.category.name
            },
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        categories_data = json.loads(request.body)

        category = Category()
        category.name = categories_data["name"]

        category.save()

        return JsonResponse({
            "id": category.pk,
            "name": category.name,
        }, status=200)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Http404:
            return JsonResponse({"error": "Данной категории не существует"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })

