from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileUpload
from .serializers import FileUploadSerializer
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            file_path = file_serializer.data['file']
            name = file_serializer.data['name']
            df = pd.read_csv(file_path)
            labels = ["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTAIRS", "SITTING", "STANDING", "LYING"]
            X_test = df.drop(['activity', 'activity_name', 'subject_id'], axis=1)
            model = load_model('path_to_your_model/model.h5')
            ypred = model.predict(X_test)
            pred = np.argmax(ypred, axis=1)
            results = [labels[i] for i in pred]
            return Response({"predictions": results})
        else:
            return Response(file_serializer.errors, status=400)
