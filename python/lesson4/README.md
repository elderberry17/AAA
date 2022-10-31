### Как запускать тесты?


1. test_issue1.py

Запуск в PyCharm: интерпретатор предложит запустить doctests  автоматически при попытке исполнить файл. Далее мы увидим результат работы в командной строке
Запуск в терминале: python -m doctest -v test_issue1.py 

2. test_issue2.py

python -m pytest test_issue2.py

3. test_issue3.py

python -m unittest test_issue3.py


4. test_issue4.py

Повторяем действия из шага 3


5. test_issue5.py

python -m pytest -q test_issue5.py --cov . --cov-report html
