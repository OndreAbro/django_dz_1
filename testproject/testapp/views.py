from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы можете узнать о информации обо мне.</p>
    """
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Меня зовут Абросимов А.В. и я начинающий разработчик.</p>
    <p>Я изучаю Django и создаю свой первый сайт.</p>
    """
    logger.info('About page accessed')
    return HttpResponse(html)


