# ЗАПУСК ПРОЕКТ

## prereq
- poetry
- uvicorn
- fastapi
- python@3.12 (установке через deadsnakes/ googlemethod)

## nginx 

nginx проксирует запросы к api шахмат через адресацию:

/api/
за которым скрыты

localhost:8000/api/

Vue стучится на '/api/chess/calculate-rating-fide/

## TODO 
Возможно подправить имплементацию математической логики к алгоритму FIDE ? либо узнать в чём проблема.

