import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
django.setup()

from shop.models import Category

cats = [
    ('accessories', 'Аксессуары'),
    ('gaming', 'Гейминг'),
    ('home', 'Дом'),
    ('books', 'Книги'),
    ('kompyutry', 'Компьютры'),
    ('noutbuki', 'Ноутбуки'),
    ('office', 'Офис'),
    ('sports', 'Спорт'),
    ('telefony', 'Телефоны'),
    ('electronics', 'Электроника'),
]

created = 0
for slug, name in cats:
    obj, ok = Category.objects.get_or_create(
        slug=slug,
        defaults={'name': name}
    )
    if ok:
        created += 1
        print('Created:', slug)
    else:
        print('Exists:', slug)

print('Done. Created', created, 'categories.')