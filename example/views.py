# example/views.py
from datetime import datetime
from django.http import JsonResponse
import pandas as pd


def index(request):
    url = 'https://firebasestorage.googleapis.com/v0/b/react-web-c4127.appspot.com/o/reviews.csv?alt=media&token=c7336dbd-0109-4270-9c39-2967ffbe59a8'
    df = pd.read_csv(url)
    data = df.to_dict(orient='records')

    return JsonResponse(data)