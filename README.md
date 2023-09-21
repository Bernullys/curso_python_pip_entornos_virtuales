# curso_python_pip_entornos_virtuales
Curso de python para iniciar como backend developer

Conamdos:

pip3 freeze                                     #Show the currents libraries 
which python3                                   #Shows the version of the program or package
sudo apt install -y python3-venv                #To enable virtual enviroments in wsl
python3 -m venv nombre_del_ambiente             #To create a virtual enviromente (inside the folder of the project)
source nombre_del_ambiente/bin/activate         #To activate the enviroment
deactivate                                      #To deactivate the enviroment


Que es un ambiente virtual?
Lo que hace un ambiente virtual es encapsular los modulos (pip) y lo atan a cada proyecto por separado. Para evitar conflictos por versiones.

Como se aislan? Crear virtual enviroments
    Verificar de donde se esta ejecutando.
    En wsl se debe instalar el enviroment.
    Crear ambiente por proyecto. Entrar en carpeta del proyecto y ejecutar python3 -m venv nombre_del_ambiente.
    Ahora hay que activar el ambiente: source nombre_del_ambiente/bin/activate.
    Para salir del ambiente virtual: deactivate.
    Dentro del ambiente se puede ver desde donde se corre python o los paquetes.
    Inicialmente es este ambiente no hay nada instalado (aparte de python y pip).
    Las que se instalen, quedaran solo en este ambiente.

Requirements.txt: is a file that admins all dependencies and versions.
    To create a file with all the dependencies of an enviroment: pip3 freeze > requirements.txt
    The use is when starting a project with these file, we can automatized the installation of the dependencies:
        pip3 install -r requirements.txt
        But first we need to create an enviroment as we did it before.

