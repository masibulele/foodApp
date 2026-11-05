from django.forms import ModelForm
from .models import Item
from django.utils.translation import gettext_lazy as _


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["item_name","item_desc","item_price","item_image"]
        labels ={
            "item_desc": _("Item Description"),
        }
