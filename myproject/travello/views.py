from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    """
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.price=400
    dest1.desc='the city will never sleep'
    dest1.img='destination_1.jpg'

    dest2=Destination()
    dest2.name='Hyderabad'
    dest2.price=500
    dest2.desc='Special: chicken biryani'
    dest2.img='destination_2.jpg'

    dest3=Destination()
    dest3.name='Bangalore'
    dest3.price=600
    dest3.desc='Royal challengers bangalore'
    dest3.img='destination_3.jpg'

    dest4=Destination()
    dest4.name='Medak'
    dest4.price=1000
    dest4.desc='methuku gadda'
    dest4.img='destination_4.jpg'

    dest5=Destination()
    dest5.name='Muddapur'
    dest5.price=5000
    dest5.desc='such a beautyfull village'
    dest5.img='destination_5.jpg'
    dests=[dest1,dest2,dest3,dest4,dest5]"""
    dests=Destination.objects.all()

    return render(request, 'index.html',{'dests':dests})

