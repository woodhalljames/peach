from .models import Category

def menu_links(request):
	links = Category.objects.all()
	return dict(links=links)


def clothing_categories(request):
    men_clothing = Clothing.objects.filter(category='men')
    women_clothing = Clothing.objects.filter(category='woman')
    kids_clothing = Clothing.objects.filter(category='kids')
    babies_clothing = Clothing.objects.filter(category='babies')

    context = {
        'men_clothing': men_clothing,
        'women_clothing': women_clothing,
        'kids_clothing': kids_clothing,
        'babies_clothing': babies_clothing,
    }

    return context