# Creando api con django
Creamos entorno  >>>>> python -m venv venv
ejecuto entorno   >>>>>> source venv/Scripts/activate
instalamos django  >>>>>> pip install django
creamos proyecto   >>>>> django admin startproyect NOMBRRE_DEL_PROYECTO
    ingresamos  A la carpeta del proyecto  >>>> cd NOMBRRE_DEL_PROYECTO
creamos migracion   >>>>>> python manage.py migrate "se migra por que ya tiene una base por defecto"
corremos servidor >>>>>>> python manage.py runserver
creamos super usuario  >>>>>> python manage.py createsuperuser  "admin admin@hotmail.com"
creamos una aplicacion (APP)  >>>>>>>  python manage.py startapp sistema
creamos la tabla 
registramos la Aplicacion creada 

creamos la migracion   >>>>>>>>>> python mange.py makemigrations
verificamos migraciones creadas  >>>>>> $ python manage.py showmigrations