from rest_framework import serializers
from Paper.models import Papers,Subject


class PapersSerializer(serializers.ModelSerializer):
    #subject_id= serializers.ReadOnlyField(source='Subject.subjectname')
    #subject_id = serializers.StringRelatedField()


    class Meta:
        model=Papers
        fields= ('id','paper_name','paper_desc','subject_id','created_at','updated_at')

    #def to_representation(self,instance):
    #    data= super().to_representation(instance)

    #    return data
