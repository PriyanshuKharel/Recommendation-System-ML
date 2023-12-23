from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from joblib import load
import pickle


# model = load('./customer_recommendation.joblib')
model = pickle.load(open('artifacts/customer_recommendation.pkl', 'rb'))

# print(model)



def predict(request):
    return render(request, 'index.html', {'model': model})
    # return render(request,'index.html')

