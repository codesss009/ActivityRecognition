from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileUpload
from .serializers import FileUploadSerializer
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import os
import logging

logger = logging.getLogger(__name__)


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            uploaded_file_path = file_instance.file.path
            df = pd.read_csv(uploaded_file_path)
            labels = ["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTAIRS", "SITTING", "STANDING", "LYING"]
            X_test = df.drop(['activity', 'activity_name', 'subject_id'], axis=1)
            model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'model', 'model.h5')   
            model = load_model(model_path)
            ypred = model.predict(X_test)
            pred = np.argmax(ypred, axis=1)
            results = [labels[i] for i in pred]
            return Response({"predictions": results})
            
           

        else:
            logger.error(f'Serializer errors: {file_serializer.errors}')
            return Response(file_serializer.errors, status=400)
