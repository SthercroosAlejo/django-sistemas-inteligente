# example/views.py
from datetime import datetime
from django.http import JsonResponse

def index(request):
    # Obtener la fecha y hora actuales
    now = datetime.now()

    # Formatear la respuesta en JSON
    data = {
        "time": now.strftime("%H:%M:%S"),  # Hora en formato HH:MM:SS
        "day": now.strftime("%A"),  # Día de la semana completo (ejemplo: Monday)
        "full_date": now.strftime("%Y-%m-%d"),  # Fecha completa en formato YYYY-MM-DD
    }

    return JsonResponse(data)