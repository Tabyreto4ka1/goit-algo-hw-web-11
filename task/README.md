Щоб запустит API потрібно спочатку свтворити бд спочатку в  запишіть свій шлях підключення. Після цього потрібно зайти у віртуільне 
середовище відкриваємо термінал у task та вводимо ./.venv/scripts/Activate.ps1, далі треба  виконати міграції
alembic init migrations  alembic revision --autogenerate -m 'Init' alembic upgrade head  
після виконання міграцій уже можа запускати сервер  uvicorn main:app --host localhost --port 8000 --reload 
він буде доступний за почиланням http://localhost:8000/ , але щоб працювати з АPi можна використати Swagger http://localhost:8000/docs