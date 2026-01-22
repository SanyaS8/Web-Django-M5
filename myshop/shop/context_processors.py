from .models import Category
from django.templatetags.static import static


# External icon mapping (CDN icons). These are fallbacks when no local svg is present.
EXTERNAL_CATEGORY_ICONS = {
    'electronics': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/cpu.svg',
    'accessories': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/watch.svg',
    'home': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/house.svg',
    'noutbuki': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/laptop.svg',
    'telefony': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/phone.svg',
    'kompyutry': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/pc-display-horizontal.svg',
    'sports': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/activity.svg',
    'books': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/book.svg',
    'auto': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/car-front.svg',
    'gaming': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/controller.svg',
    'office': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/briefcase.svg',
}

CATEGORY_SUBS = {
    'noutbuki': ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'MSI'],
    'telefony': ['Apple', 'Samsung', 'Xiaomi', 'OnePlus', 'Google'],
    'accessories': ['Сумки', 'Часы', 'Наушники', 'Чехлы'],  
    'home': ['Мебель', 'Товары для дома', 'Кухня'],          
    'sports': ['Экипировка', 'Обувь', 'Аксессуары'],
    'books': ['Художественная', 'Нон-фикшн', 'Детская'],
    'electronics': ['Телевизоры', 'Фото', 'Аудио', 'Гаджеты'],
    'kompyutry': ['Сборные ПК', 'Мониторы', 'Материнские платы', 'Видеокарты'],
    'auto': ['Шины', 'Масла', 'Аксессуары'],
    'gaming': ['Консоли', 'Игры', 'Аксессуары'],
    'office': ['Принтеры', 'Канцелярия', 'Мебель'],
}



def categories(request):
    """Добавляет в контекст все категории, карту внешних иконок и подкатегорий для динамических меню.

    Также собираем `category_menu` — упорядоченный список словарей с
    параметрами для рендера верхнего меню (name, slug, url, icon, subs).
    Это упрощает шаблон и даёт один источник правды для иконок.
    """
    cats = Category.objects.all()
    category_menu = []
    for c in cats:
        # Сначала пробуем внешнюю иконку по слугу, иначе используем локальный svg в статике
        icon = EXTERNAL_CATEGORY_ICONS.get(c.slug) or static(f'img/categories/{c.slug}.svg')
        category_menu.append({
            'name': c.name,
            'slug': c.slug,
            'url': c.get_absolute_url(),
            'icon': icon,
            'subs': CATEGORY_SUBS.get(c.slug, [])
        })

    POPULAR_SLUGS = ['noutbuki', 'office', 'electronics']

    popular_categories = [
        c for c in category_menu
        if c['slug'] in POPULAR_SLUGS
    ]

    return {
        'categories': cats,
        'category_icons': EXTERNAL_CATEGORY_ICONS,
        'category_subs': CATEGORY_SUBS,
        'category_menu': category_menu,
        'popular_categories': popular_categories,
    }
