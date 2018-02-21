# Flask-RESTful-API
From Udemy "REST APIs with Flask and Python" by Jose Salvatierra course. A simple API using Flask-RESTful implementing an Item and Store model and modified here to use the JWT-Extended token autentication method in a basic way.

Configuration Notes:

app.py makes use of two environment variables

	os.getenv('DATABASE_URL')
	os.getenv('APP_SECRET_KEY')

You have to replace these calls with your variables, or set up these environment variables on your deployment environment/system.
