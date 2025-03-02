# Rozwiązania zadań lab 5

## zadanie 1
Uruchom Django shell tak jak w przykładach zaprezentowanych w tym labie i dodaj po 3 nowe obiekty typu Category, Topic oraz Post. Dla minimum jednego posta nie zdefiniuj użytkownika (powinniśmy już mieć w definicji modelu Post atrybut null=True).

```python
python manage.py shell
from posts.models import Post, Topic, Category
from django.contrib.auth.models import User

cat1 = Category.objects.create(name="Kategoria1")
cat2 = Category.objects.create(name="Kategoria2")
cat3 = Category.objects.create(name="Kategoria3")

topic1 = Topic.objects.create(name="Temat1", category=cat1)
topic2 = Topic.objects.create(name="Temat2", category=cat2)
topic3 = Topic.objects.create(name="Temat3", category=cat3)

user = User.objects.first()  # Pobiera pierwszego użytkownika z bazy

post1 = Post.objects.create(content="Trele morele", topic=topic1, created_by=user)
post2 = Post.objects.create(content="Kot ma ale", topic=topic2, created_by=user)
post3 = Post.objects.create(content="Yeti to zwierze", topic=topic3)  # Brak użytkownika (null=True)

#Weryfikacja czy obiekty są w bazie:
Category.objects.all()
Topic.objects.all()
Post.objects.all()
```

## Zadanie 2
Wykonaj zapytanie filtrujące obiekty typu Topic, których nazwa rozpoczyna się od wybranej przez Ciebie litery, tak aby zwrócone były niepuste wyniki.

```python
Topic.objects.filter(name__startswith="T")
```

## Zadanie 3
Dla danych zwróconych w zadaniu 2 wyświetl listę wszystkich wartości tych obiektów (funkcja values()).

```python
Topic.objects.filter(name__startswith="T").values()
```

## Zadanie 4
Wykonaj pobranie wszystkich obiektów typu Post i zapisz je do zmiennej posts.

```python
posts = Post.objects.all()
posts
```

## Zadanie 5
Z listy stworzonej w zadaniu 4 za pomocą cięcia (slicing) wyświetl:

    pierwszy element
    ostatni element
    wszystkie elementy w odwróconej kolejności (od ostatniego do pierwszego)
    co drugi element


```python
#pierwszy element
posts[0]
#ostatni element
posts[posts.count() - 1]
#wszystkie elementy w odwróconej kolejności (od ostatniego do pierwszego)
posts[::-1]
#co drugi element
```

## Zadanie 6
Wyświetl liczbę obiektów typu Post, które nie mają przypisanego użytkownika.
```python
Post.objects.filter(created_by__isnull=True)
```
## Zadanie 7
Wyświetl wszystkie obiekty Topic sortując po nazwie w porządku alfabetycznym od Z do A.
```python
Topic.objects.all().order_by('-name').values('name')
```
## Zadanie 8
Wyświetl wszystkie obiekty Category, których id jest mniejsze niż 2 używając metody exclude().
```python
Category.objects.exclude(id__gte=2)
```
## Zadanie 9
Usuń jeden wybrany topic, który ma przypisany obiekt Post i sprawdź czy ten post również zostal usunięty.
```python
Post.objects.all()
Topic.objects.get(id=2).delete()
```