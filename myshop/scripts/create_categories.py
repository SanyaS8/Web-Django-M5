import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
django.setup()
from shop.models import Category

cats = [
    ('electronics', 'Электроника'),
    ('noutbuki', 'Ноутбуки'),
    ('telefony', 'Телефоны'),
    ('kompyutry', 'Компьютеры'),
    ('accessories', 'Аксессуары'),
    ('clothing', 'Одежда'),
    ('shoes', 'Обувь'),
    ('home', 'Дом'),
    ('kitchen', 'Кухня'),
    ('beauty', 'Красота'),
    ('sports', 'Спорт'),
    ('toys', 'Игрушки'),
    ('books', 'Книги'),
    ('auto', 'Автотовары'),
    ('baby', 'Детям'),
    ('garden', 'Сад'),
    ('gaming', 'Гейминг'),
    ('office', 'Офис'),
    ('health', 'Здоровье'),
    ('pets', 'Животные'),
    ('photo', 'Фото')
]

created = 0
for slug, name in cats:
    obj, ok = Category.objects.get_or_create(slug=slug, defaults={'name': name})
    if ok:
        created += 1
        print('Created:', slug)
    else:
        print('Exists:', slug)

print('Done. Created', created, 'categories.')
