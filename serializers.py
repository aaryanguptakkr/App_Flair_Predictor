from rest_framework import serializers
from .rscraper import flair_predictor
from .models import Upload
 
class UploadSerializer(serializers.ModelSerializer):
    # key = serializers.SerializerMethodField()

    class Meta:
        model = Upload
        fields = '__all__'
        
    # def get_anss(self, obj):
    #     file=self.context
    #     print(file)
    #     # data=file.read()
    #     # y=""
    #     # for x in data:
    #     #     y+=chr(x)
    #     # ans={}
    #     # for line in y.split("\n"):
    #     #     if(line!=""):
    #     #         # print(flair_predictor(line)[0])
    #     #         ans[line]=flair_predictor(line)[0]
    #     print(self)
    #     return 0