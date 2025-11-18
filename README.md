# Django Tree Menu App

## Установка и запуск

1. Клонировать репозиторий:

```bash
git clone https://github.com/monkeprogrammer01/UptraderTest.git
cd UptraderTest
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata initial_data.json
```
Также не забудьте создать .env файл и добавить туда DJANGO_SECRET_KEY=your_secrey_key