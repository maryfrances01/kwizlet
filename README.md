# Qwizlet Flashcard App

## Qwizlet is a configurable flashcard application created with Django.

### Qwizlet Features
- Create new flashcard sets to save to a database.
- Edit old flashcard sets.
- Learn flashcards by flipping through the cards.

### Installation
1. Clone this repo:

   ```
   git clone https://github.com/maryfrances01/qwizlet.git
   ```
   
2. Create your virtual environment: 

   ```
   python3 -m venv venv
   ```
   ```
   source venv/bin/activate
   ```

3. Install the required packages using:

   ```
   pip3 install -r requirements.txt
   ```

4. Setup the SQLite database:

   ```
   python3 manage.py makemigrations
   ```
   ```
   python3 manage.py migrate
   ```

5. Start your development web server:

   ```
   python3 manage.py runserver
   ```

6. Create a new flashcard set by entering the following URL in your browser:

   ```
   http://127.0.0.1:8000/flashcards/create/
   ```