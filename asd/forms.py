#from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Album

class registrarAlbumForm(ModelForm):

    class Meta:
        model = Album
        fields = '__all__'