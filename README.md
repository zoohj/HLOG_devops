# HLOG_devops

aws 배포

#시작 설정

#가상환경 생성
python -m venv venv

#가상환경 실행
./venv/Scripts/activate

#필요 package 설치
pip install -r requirements.txt

#DB 생성
python manage.py makemigrations
python manage.py migrate

#서버 실행
python manage.py runserver




#requirements.txt 생성
pip freeze > requirements.txt





