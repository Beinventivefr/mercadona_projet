from django.test import TestCase

from catergory.models import Catergory

# Create your tests here.
class CatergoryTestCase(TestCase):

    def test_create_category(self):

        # Voir combien d'élément sont présent dans la db
        nbr_of_catergory_before_add = Catergory.objects.count()

        # Ajouter un objet dans la db
        new_catergory = Catergory()
        new_catergory.wording = "Mur"
        new_catergory.save()

        nbr_of_catergory_after_add = Catergory.objects.count()

        # valider que le nombre d'objet dans la db a été incrémenté de 1
        self.assertTrue(nbr_of_catergory_after_add == nbr_of_catergory_before_add + 1)

