# URL-Shortener


<img src="https://github.com/andrew-raafat/URL-Shortener/assets/83042751/86ecfe29-7091-4a0b-bd45-c6ce12168e7d" width="100%" height="300px" >

## Brief
The URL shortener application is a web-based tool developed using the Django web framework. Its primary purpose is to take long and complex URLs and generate shortened, more user-friendly URLs that can be easily shared and accessed.

## Features
+ **URL Shortening:** The application allows users to input a long URL and generates a short and unique URL as a result. This short URL serves as a redirect to the original long URL when accessed.
+ **URL Management:** Registered users have the ability to manage their shortened URLs. They can view a list of their created URLs.
+ **User Registration and Authentication:** Users can register an account to access additional features. Authentication ensures secure access to user-specific functionalities.

## Installation
+ Clone the repository: **git clone https://github.com/andrew-raafat/URL-Shortener.git**
+ Create a virtual environment and activate it: **virtualenv venv source venv/bin/activate**
+ Install the dependencies: **pip install -r requirements.txt**
+ Run the make migrations: **python manage.py makemigrations**
+ Run the migrations: **python manage.py migrate**
+ Start the development server: **python manage.py runserver**

The development server will be running on port 8000. You can visit the URL shortener at http://localhost:8000.

## Contributing
Pull requests are welcome. For major changes, please open an [issue](https://github.com/andrew-raafat/URL-Shortener/issues) first to discuss what you would like to change.

## License
The URL-Shortener project is licensed under the MIT License.

## Contact
If you have any questions, please contact me at andrewraafat52@gmail.com
