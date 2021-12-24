from django.shortcuts import render
from django.http import HttpResponse
from . import lotin_kril

# Create your views here.
def index(request):
	return render(request, 'home.html')

	
def tocyrillic(request):
	if request.method == 'POST':
		latin = request.POST.get('latin', '')
		print(latin)
		kril = lotin_kril.ToCyrilic(latin)
		print(kril)
		return render(request, 'ToCyrillic.html', {'cyrillic':kril, 'latin':latin})

		# def ToLatin(word):
		# 	for x in range(len(latin)):
		# 		word = word.replace(cyrilic[x], latin[x])
		# 	return word

		# latin_word = ToLatin(word)


		# print(lotin_kril.ToCyrilic(latin))
	else:
		return render(request, 'ToCyrillic.html')

def tolatin(request):
	if request.method == 'POST':
		cyril = request.POST.get('cyril', '')
		print(cyril)
		latin = lotin_kril.ToLatin(cyril)
		print(latin)
		return render(request, 'ToLatin.html', {'latin':latin, 'cyril':cyril})

		# def ToLatin(word):
		# 	for x in range(len(latin)):
		# 		word = word.replace(cyrilic[x], latin[x])
		# 	return word

		# latin_word = ToLatin(word)


		# print(lotin_kril.ToCyrilic(latin))
	else:
		return render(request, 'ToLatin.html')