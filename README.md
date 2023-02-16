# openai-API
Django application that integrates with the OpenAI API to generate natural language responses to user inputs. The application is designed to work with both Telegram and web browsers, allowing users to interact with it in whichever way is most convenient for them.

![telegram-cloud-document-2-5436324961939630234](https://user-images.githubusercontent.com/109435929/219484501-5df534fe-9af5-49d1-b30f-e241853a68ad.jpg)



The application comes with Login, Logout, and Sign up pages, which allow users to create accounts and access the full functionality of the app. Additionally, users have the option to remove their conversation with one click, ensuring that their privacy is protected.


![telegram-cloud-document-2-5436324961939630241](https://user-images.githubusercontent.com/109435929/219484314-820627b2-09d7-4545-837c-1f03119434f1.jpg)


Once a user inputs a message via Telegram or the web interface, the Django application uses the OpenAI API to generate a response, which is then sent back to the user via the same channel. The application's integration with the OpenAI API allows for a wide range of possible use cases, from customer service chatbots to intelligent assistants for websites and apps.

![telegram-cloud-document-2-5436324961939630239](https://user-images.githubusercontent.com/109435929/219484568-22823544-93e8-49a6-b424-fe89992e4dbc.jpg)



The code is written in Python, using the Django web framework and the OpenAI API for natural language processing. The repository includes all the necessary files to run the application, as well as documentation on how to set it up and use it.

If you're interested in exploring the possibilities of natural language generation with Django and the OpenAI API, this repository is a great starting point. Feel free to clone the repo and start experimenting!

Prerequisites:

Python >=3.7.1 
Git 
OpenAI API key 
Telegram bot token (if using Telegram integration)

Clone the repository 
Create Venv and Install dependencies by running : pip install -r requirements.txt 
Run the migrations: 
python manage.py makemigrations 
python manage.py migrate

