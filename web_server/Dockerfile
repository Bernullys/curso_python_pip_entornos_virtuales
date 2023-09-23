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

#to turn severals commands: This is the only line that will change in this file
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

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

