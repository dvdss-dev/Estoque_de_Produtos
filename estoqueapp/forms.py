from django.forms import ModelForm
from estoqueapp.models import Itens

# Create the form class.
class ItensForm(ModelForm):
     class Meta:
         model = Itens
         fields = ['nome', 'tipo', 'qnt']