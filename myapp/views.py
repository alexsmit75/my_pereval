from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, Coords, Image, PerevalAdded
from .serializers import PerevalAddedSerializer, CustomUserSerializer, CoordsSerializer, ImageSerializer

class SubmitDataView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        images_data = request.FILES.getlist('images')

        print("Received data:", request.data)

        try:
            # Проверка наличия необходимых полей в данных
            required_fields = ['beautyTitle', 'title', 'add_time', 'user', 'coords', 'images']
            if not all(field in data for field in required_fields):
                raise ValueError("Недостаточно обязательных полей в данных")

            # Создание и сохранение связанных объектов
            user_serializer = CustomUserSerializer(data=data['user'])
            coords_serializer = CoordsSerializer(data=data['coords'])
            if not user_serializer.is_valid() or not coords_serializer.is_valid():
                print("Invalid user data:", user_serializer.errors)
                print("Invalid coords data:", coords_serializer.errors)
                raise ValueError("Некорректные данные для пользователя или координат")

            user_instance = user_serializer.save()
            coords_instance = coords_serializer.save()

            # Создание и сохранение объекта PerevalAdded
            pereval_data = {
                'beautyTitle': data['beautyTitle'],
                'title': data['title'],
                'other_titles': data.get('other_titles', ''),
                'connect': data.get('connect', ''),
                'add_time': data['add_time'],
                'user': user_instance.id,
                'coords': coords_instance.id,
                'winter_level': data.get('winter_level', ''),
                'summer_level': data.get('summer_level', ''),
                'autumn_level': data.get('autumn_level', ''),
                'spring_level': data.get('spring_level', ''),
                'status': 'new',
            }
            pereval_serializer = PerevalAddedSerializer(data=pereval_data)
            if not pereval_serializer.is_valid():
                print("Invalid PerevalAdded data:", pereval_serializer.errors)
                raise ValueError("Некорректные данные для PerevalAdded")

            pereval_instance = pereval_serializer.save()

            # Создание и сохранение связанных объектов Image через PerevalImages
            images_data = data.get('images', [])
            for image_data in images_data:
                image_data['pereval'] = pereval_instance.id
                image_serializer = ImageSerializer(data=image_data)
                if not image_serializer.is_valid():
                    print("Invalid Image data:", image_serializer.errors)
                    raise ValueError("Некорректные данные для изображения")
                image_serializer.save()

            response_data = {
                "status": 200,
                "message": "Отправлено успешно",
                "id": pereval_instance.id
            }
        except ValueError as ve:
            response_data = {
                "status": 400,
                "message": str(ve),
                "id": None
            }
        except Exception as e:
            response_data = {
                "status": 500,
                "message": "Ошибка при выполнении операции: " + str(e),
                "id": None
            }
        return Response(response_data)