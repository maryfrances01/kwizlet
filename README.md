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
5. (Optional) Import the CKA exam flashcard set:

   ```
   mange.py loaddata db.json
   ```

6. Start your development web server:

   ```
   python3 manage.py runserver
   ```

7. (Optional) Create a new flashcard set by entering the following URL in your browser:

   ```
   http://127.0.0.1:8000/flashcards/create/
   ```

### Screenshots
<img src="images/qwizlet_homepage.png" alt="Qwizlet Homepage" width="500" height="300">
<br>
<img src="images/flashcards.png" alt="Qwizlet Flashcards" width="300" height="300">
<br>
<img src="images/study_set.png" alt="Study Flashcard Set" width="300" height="300">
<br>
<img src="images/add_a_card_to_set.png" alt="Add a card to Flashcard Set" width="300" height="300">
