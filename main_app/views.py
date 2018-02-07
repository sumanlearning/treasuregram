from django.shortcuts import render
from .models import Treasure
from .models import User
from .forms import TreasureForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# def index(request):
# 	return HttpResponse('<h1>Hallo... suman explorers!</h1>')

def index(request):
	# name = 'Gold Nugget'
	# value = 1000.00
	# context = {'treasure_name': name,
	# 			'treasure_val': value}
	treasures = Treasure.objects.all()
	# menambahkan tampilan form di halaman index
	form = TreasureForm()
	return render(request, 'index.html', {'treasures':treasures, 'form':form})

def detail(request, treasure_id):
	treasure = Treasure.objects.get(id=treasure_id)
	return render(request,'detail.html',{'treasure':treasure})

def post_treasure(request):
	form = TreasureForm(request.POST, request.FILES)
	if form.is_valid():
		treasure = form.save(commit = False)
		treasure.user = request.user
		treasure.save()
		# form.save(commit = True)
		# treasure = Treasure(name = form.cleaned_data['name'],
		# 					value = form.cleaned_data['value'],
		# 					material = form.cleaned_data['material'],
		# 					location = form.cleaned_data['location'],
		# 					img_url = form.cleaned_data['img_url'])
		# treasure.save()
		"""code yang diatas merupakan code lama yang menggunakan class di form, dibawah merupakan code baru dimana form inherited denagn ModelForm"""
		# form.save()
		"""kecek badai, satu syntax diatas itu membaca data dari form + save ke database"""
	return HttpResponseRedirect('/')

def profile(request, username):
	user = User.objects.get(username=username)
	treasures = Treasure.objects.filter(user=user)
	return render(request, 'profile.html', {'username': username, 'treasures': treasures})

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					print('The account has been disabled')
			else:
				print('The username and password were incorrect')
				return HttpResponse('password salah')
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form':form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def like_treasure(request):
	treasure_id = request.POST.get('treasure_id', None)
	likes = 0
	if (treasure_id):
		treasure = Treasure.objects.get(id=int(treasure_id))
		if treasure is not None:
			likes = treasure.likes + 1
			treasure.likes = likes
			treasure.save()
	return HttpResponse(likes)	


# class Treasure:
# 	def __init__(self,name,value,material,location, img_url):
# 		self.name = name
# 		self.value = value
# 		self.material = material
# 		self.location = location
# 		self.img_url = img_url
# treasures = [
# 	Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM","static/images/goldrose.png"),
# 	Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO","static/images/goldrose.png"),
# 	Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA',"static/images/goldrose.png")
# ]