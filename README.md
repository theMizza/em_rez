# em_rez
legacy version of website

pages:
- index (static_page)
- about_us (static_page)
- contacts (static_page)

db:
- sqlite

# How to run
- clone repo
- create and activate venv
- install libs ```pip install -r requirements.txt``` in dir with requirements.txt
- cd in dir with manage.py
- ```python manage.py runserver```
- website will start on localhost

# Add
- admin login ```root```
- admin pwd ```dontstopme```

# TODO
- add more pages (by example: catalog via catalog app creating)
- add models and views
- refactoring
- postgre instead of sqlite
- dockerizing
- etc