from rest_framework import serializers
from dogs.models import Dog, Breed



class DogSerializer(serializers.ModelSerializer):
    #breedinfo = serializers.PrimaryKeyRelatedField(many=True, queryset=Breed.objects.all()) 
    class Meta:
        model = Dog
        fields = ['id', 'name', 'breed', 'age', 'gender', 'color', 'favoritefood', 'favoritetoy']

class BreedSerializer(serializers.ModelSerializer):
    #breeds = serializers.RelatedField(read_only=True)
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']        