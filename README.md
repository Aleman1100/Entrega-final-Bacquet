Entrega Final - Alejandro Bacquet
<br>
<br>
#Base de datos para cada clase no se encuentran creadas, por lo que debe ejecutarse en comando necesario para crearlas antes de usar las funcionalidades.#  
<br>
<br>
1. La vista general de cada pagina se crea a partir de templates/base, y la vista personalizada se encuentra en inicio/templates/inicio
<br>   
2. Los modelos orientados a funciones que definen el tipo de informacion que se puede guardar en la BBDD se encuentran disponibles en inicio/models.py.
<br>   
3. Los formularios donde se ingresaran los datos que usará cada modelo a funciones se encuentran disponibles en inicio/forms.py.
<br>   
4. En inicio/urls.py se encuentra el codigo que revisará los datos ingresados por el usuario para validarlos y si fuera posible, guardarlos en la BBDD.
<br>   
5. Las rutas para acceder a cada sitio que necesitemos para crear, mostrar y/o buscar datos se encuentran en inicio/urls.py.
<br>
6. La vista html general de cada pagina a partir de modelos CBV se encuentran en mangas/templates/manga y animes/templates/anime, teniendo como base inicio/templates/base.
<br>
7. Los modelos CBV que definen el tipo de informacion que se puede guardar en la BBDD se encuentran disponibles en mangas/models.py y animes/models.py.
<br>
8. mangas/views.py y animes/views.py contienen cada vista y uso para los modelos CBV creados anteriormente.
<br>
9. mangas/urls.py y animes/urls.py usara las vista para guardar o mostrar los datos en BBDD, usando las vistas de sus respectivas views.py como base.
<br>
10. Para la creacion de usuario y login, el html general de cada pagina se crea a partir de inicio/templates/base, y los htmls personalizadas se encuentra en usuarios/templates/usuario.
<br>
11. Los modelos CBV que definen el tipo de informacion que se puede guardar en la BBDD se encuentran disponibles en usuarios/models.py, donde User es importado y DatosExtra se definido. 
<br>
12. usuarios/views.py contiene cada vista y uso para el modelo CBV creado anteriormente, con la funcionalidades de registro, login, logut, detalle, edicion y alcance de acceso para los elementos del sitio.
<br>
12. usuarios/urls.py usara las vista para guardar o mostrar los datos en BBDD, usando las vistas de usuarios/views.py como base.
<br>
13. Seccion About disponible con html en inicio/templates/about_me.
