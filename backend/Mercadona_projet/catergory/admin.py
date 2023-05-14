from django.contrib import admin

from catergory.models import Catergory


# Register your models here.
@admin.register(Catergory)
class CatergoryAdmin(admin.ModelAdmin):

    list_display = ('wording',)

    # Dans ce cas, nous avons spécifié list_display wording pour dire à Django de nafficher 
    # que le champ wording lorsque lutilisateur regarde la liste des instances de notre modèle dans linterface dadministration. 
    # En dautres termes, lorsque lutilisateur navigue vers la page de liste des catégories, il ne verra que la colonne contenant le libellé de chaque catégorie.


