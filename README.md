# openai-API
Django application that integrates with the OpenAI API to generate natural language responses to user inputs. The application is designed to work with both Telegram and web browsers, allowing users to interact with it in whichever way is most convenient for them.

The application comes with Login, Logout, and Sign up pages, which allow users to create accounts and access the full functionality of the app. Additionally, users have the option to remove their conversation with one click, ensuring that their privacy is protected.

Once a user inputs a message via Telegram or the web interface, the Django application uses the OpenAI API to generate a response, which is then sent back to the user via the same channel. The application's integration with the OpenAI API allows for a wide range of possible use cases, from customer service chatbots to intelligent assistants for websites and apps.

The code is written in Python, using the Django web framework and the OpenAI API for natural language processing. The repository includes all the necessary files to run the application, as well as documentation on how to set it up and use it.

If you're interested in exploring the possibilities of natural language generation with Django and the OpenAI API, this repository is a great starting point. Feel free to clone the repo and start experimenting!

Prerequisites:

Python >=3.7.1 Git OpenAI API key Telegram bot token (if using Telegram integration)

Clone the repository Create Venv Install dependencies by running : pip install -r requirements.txt Run the migrations: python manage.py makemigrations python manage.py migrate

![telegram-cloud-document-2-5436324961939630234](https://user-images.githubusercontent.com/109435929/219484089-4d42612a-473e-4959-a2b3-add18615c55b.jpg)
