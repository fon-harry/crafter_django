from django.contrib import admin
from recipes.models import Recipe, RecipeProduction, RecipeIngredient


class ProductionInline(admin.TabularInline):
    model = RecipeProduction


class IngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [ProductionInline, IngredientInline]


admin.site.register(Recipe, RecipeAdmin)


