import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
django.setup()

from shop.models import Product, Category
from django.core.files import File


def create_product(name, slug, image_path, description, price, stock):
    try:
        category = Category.objects.get(slug='electronics')
    except Category.DoesNotExist:
        print("Категория 'electronics' не найдена.")
        return

    if Product.objects.filter(slug=slug).exists():
        print(f"Товар уже существует: {name}")
        return

    product = Product(
        category=category,
        name=name,
        slug=slug,
        description=description,
        price=Decimal(price),
        stock=stock,
        available=True
    )

    with open(image_path, "rb") as img_file:
        product.image.save(os.path.basename(image_path), File(img_file), save=True)

    print(f"Создан товар: {name}")


BASE_PATH = r"C:\Users\Alex\Pictures\картинки сайт\электро"


create_product(
    name="Веб-камера Epos Expand Vision 1",
    slug="epos-expand-vision-1",
    image_path=rf"{BASE_PATH}\electro1.jpg",
    description=(
        "разрешение: 3840x2160 (4K)\n"
        "60 кадр/сек\n"
        "встроенный микрофон\n"
        "интерфейс USB Type-A\n"
        "кабель 1.2 м"
    ),
    price="499.00",
    stock=10
)

create_product(
    name="Игровой монитор Xiaomi Redmi G Pro 27\"",
    slug="xiaomi-redmi-g-pro-27",
    image_path=rf"{BASE_PATH}\electro2.jpg",
    description=(
        "диагональ 27\"\n"
        "разрешение 2560x1440\n"
        "матрица IPS\n"
        "частота 180 Гц\n"
        "время отклика 1 мс\n"
        "HDMI, DisplayPort"
    ),
    price="1299.00",
    stock=7
)

create_product(
    name="Коммутатор TP-Link TL-SL1218P",
    slug="tp-link-tl-sl1218p",
    image_path=rf"{BASE_PATH}\electro3.jpg",
    description=(
        "тип: неуправляемый\n"
        "16 портов Gigabit\n"
        "2 порта 100 Мбит\n"
        "1 порт SFP\n"
        "PoE поддержка\n"
        "пропускная способность 7.2 Гбит/с"
    ),
    price="539.00",
    stock=5
)

print("Электроника добавлена.")