from django.shortcuts import render
from user.models import Costumer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
def costumers(request):
    costumers_ = Costumer.objects.all()
    costumers_list = []
    for costumer in costumers_:
        costumer_dict = {
            "first_name": costumer.name,
            "last_name": costumer.last_name,
            "email": costumer.email,
            "phone_number": costumer.phone_number,
            'city' : costumer.city,
            'address' : costumer.address
        }
        costumers_list.append(costumer_dict)
    return JsonResponse(costumers_list)
@csrf_exempt
def add_costumer(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            name = body['name']
            last_name = body['last_name']
            username = body['username']
            email = body['email']
            phone_number = body['phone_number']
            city = body['city']
            address = body['address']
            password = body['password']
            if Costumer.objects.filter(email=email).exists():
                return JsonResponse({'error': 'A customer with this email already exists.'}, status=400)

            if Costumer.objects.filter(phone_number=phone_number).exists():
                return JsonResponse({'error': 'A customer with this phone number already exists.'}, status=400)
            
            if Costumer.objects.filter(username=username).exists():
                return JsonResponse({'error': 'A customer with this username already exists.'}, status=400)

            costumer = Costumer.objects.create(name=name,
                                                last_name=last_name,
                                                username=username, 
                                                email=email, 
                                                phone_number=phone_number, 
                                                city=city, 
                                                address=address, 
                                                password=make_password(password)
                                                )
            costumer.save()
            return JsonResponse({'message': 'Customer added successfully', 'costumer_id': costumer.id}, status=201)


        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        except IntegrityError as e:
            return JsonResponse({'error': str(e)}, status=400)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        
    else :
        return JsonResponse({'error' : 'invalid request method'}, status = 405)


    

