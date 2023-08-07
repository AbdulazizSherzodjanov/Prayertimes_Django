from django.shortcuts import render
import requests
def home(request):
    responce = requests.get("https://islomapi.uz/api/present/day?region=Toshkent")
    bomdod_n = responce.json()['times']['tong_saharlik']
    peshin_n = responce.json()['times']['peshin']
    asr_n = responce.json()['times']['asr']
    shom_n = responce.json()['times']['shom_iftor']
    hufton_n = responce.json()['times']['hufton']
    from django.utils.timezone import datetime #important if using timezones
    today = datetime.today()
    ctx = {
        'bomdod':bomdod_n,
        'peshin':peshin_n,
        'asr':asr_n,
        'shom':shom_n,
        'hufton':hufton_n,
        'today':today
    }
    
    return render(request,'home.html',ctx)

