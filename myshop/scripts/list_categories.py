import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
django.setup()
from shop.models import Category

cats = Category.objects.all()
print('Total categories:', cats.count())
for c in cats:
    print(c.slug, '-', c.name)