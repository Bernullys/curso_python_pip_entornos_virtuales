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
    Every time we add a new library we have to update the requirements.txt file.
    The use is when starting a project with these file, we can automatized the installation of the dependencies:
        pip3 install -r requirements.txt
        But first we need to create an enviroment as we did it before.

Pandas is a library to manipulate csv (and much more).

FastAPI is a library to create APIs.
    pip3 install fastapi                #is a api maker
    pip3 install "uvicorn[standard]"    #is a webserver launcher

    To lunch it: in the terminal: uvicorn file_name:app --reload
    Now is running in localhost:8000
    If I want to change the port: uvicorn file_name:app --reload --port 5000 (example)
    To acces from the LAN: uvicorn file_name:app --reload --port 5000 --host 0.0.0.0

    It can renderize html


Docker is make to isolated enviroments.
    The difference with virtual enviromens is that docker can also isolated the python version using containers.
    One of its uses it to deploy applications to a cloud
    

Dockerizar aplicaciones:
    Solo scripts
    Webservers

    Solo scripts:

    Create Dockerfile:
    ##############################################################################################################################

    #from which version should start
    FROM python:3.10    

    #work space
    WORKDIR /app    
    #good practice: left is local and right is container    
    COPY requirements.txt /app/requirements.txt  

    #install the dependencies from the file in the work directory
    RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt  

    #copy everthing and put it in the app work space we are  defining in or container
    COPY . /app

    #now we need to make another file: docker-compose.yml

    #to turn on the container:
    CMD bash -c "while true; do sleep 1; done"

    #now go to the terminal and execute the command: docker-compose build
    #To do this, docker should be on (its engine)

    #Now we need to launch it using this command: docker-compose up -d
    #Now it should be created an started
    #To see the status use this command: docker-compose ps

    #Now to conect to the container we execute this command: docker-compose exec app-csv bash
    #the last command will execute the container of the application app-csv and will be conected to a terminal type bash
    #and then we will be connected
    #its like we will be inside a unix server (a cloud server)
    #we will be inside the directory we specified with WORKDIR
    #now we can navigate to the app and then use the app we create in this file. It will be runing in a docker container

    #To exit the container we execute: exit

    #It something went grwon we must rebuild using: docker-compose build
    #but the container willbe up still, so we must put it down with: docker-compose down
    #and now we up it again with: docker-compose up -d


    #Now we are running or app using the docker container :)
    #This isolate from everything so it can be develop using differents lenguages (mmm)


    In parallel creacte docker-compose.yml file
    #############################################################################################################################################

    #this file will declarate how and from where is going to be initialized this container

    #define services and its name
    #build this context from this directory using dockerfile. So it can build the container
    services:
    app-csv:
        build:
            context: .
            dockerfile: Dockerfile
        volumes:
            - .:/app
    #now to connecto to the container we needed to be on. To do that we execute a CMD command in Dockerfile
    #Its like a virtual machine but is faster and better


    #app-csv is the name we used here



Automatizando la vinculación de archivos
    This is done by adding volumes and the next line as we add in this commit.

Dockerizando web services
    It only changes:
    Dockerfile:
        CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

        and
    docker-compose.yml:
        ports:
            - '80:80'