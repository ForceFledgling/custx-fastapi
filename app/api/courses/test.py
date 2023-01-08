from fastapi import APIRouter


router = APIRouter()

@router.get('/test')
async def test():
    return {
        'id': '1',
        'title': 'Тестовый курс',
        'description': 'Описание тестового курса',
        'poster': 'https://248006.selcdn.ru/intgen-prod/landings/TgG5Rx53QzWvKpQ3H5HjHAf8C9AUaGgDAmCetuV4.png'
    }