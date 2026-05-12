from rest_framework import serializers 
from watchlist_app.models import Review, WatchList, StreamPlatform

def name_length(value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value
    
# Model serializer    

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'               

class WatchListSerializer(serializers.ModelSerializer):
    
    len_title = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'  
        
    def get_len_title(self, object):
        return len(object.title)    
        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description cannot be the same")
        return data
    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist= WatchListSerializer(many=True, read_only=True)
    #watchlist = serializers.StringRelatedField(many=True) # to get the name of the movie instead of the id
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        


# Normal serializer without model serializer


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField(max_length=200)
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and description cannot be the same")
#         return data
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         return value
    