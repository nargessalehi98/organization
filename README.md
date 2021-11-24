# Organization

<!-- ABOUT THE PROJECT -->
### About The Project

The goal is to implement systems for managing tasks in the organization. Suppose there is a number of organizations in which each organization includes several managers and employees. In addition in top level, there are a number of admins who manage the organization themselves. Individuals in this system can: Define the task and according to the type of access and
The position they hold does not attribute these tasks to themselves or other users.


## Built With

* [python](https://python.org/)
* [Django](https://www.djangoproject.com/)
* [Docker](https://www.docker.com/)
* [Rest framework](https://www.django-rest-framework.org/)

<!-- INSTALLATION -->
## Installation

Below is an example of how you can setting up your app. 
1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Running without Docker cd in root directory:
   ```sh
   python manage.py makemigrations
   ```
4. then migrate :
   ```sh
   python manage.py migrate
   ```
5. and create a superuser to login in main panel:
   ```sh
   python manage.py createsuperuser
   ```
6. Running with Docker cd in root of project:
   ```sh
   docker-compose up
   ```
7. Open a new terminal tab and:
   ```sh
   docker ps
   ```
8. Find myapp container ID and:
   ```sh
   docker exec -it <container_ID> /bin/bash
   ```
9. Now create super user:
   ```sh
   python manage.py createsuperuser
   ```

<!-- CONTACT -->
## Contact

Narges Salehi - nargessalehi998@gmail.com

Project Link: [https://github.com/nargessalehi98/organization/](https://github.com/nargessalehi98/organization/)


