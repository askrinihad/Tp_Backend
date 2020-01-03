from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name=serializers.CharField(max_length=10)


#class LoginSerializer(serializers.Serializer):

   # class Meta :
   #     model = models.Login
    #    fields =('login' , 'mot_de_passe' , 'type' ,)
     #   extra_kwargs = {'mot_de_passe': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects ."""

    class Meta :
        model = models.UserProfile
        fields= ('id' , 'name' , 'email', 'password','type')
        extra_kwargs = {'password' : {'write_only' :True}}

    def create(self, validated_data):
        """Create and return a new user ."""

        user = models.UserProfile(
            email= validated_data['email'] ,
            name = validated_data['name'] ,
            label = validated_data['label']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class VerificationSerializer(serializers.ModelSerializer):

     class Meta :
       model = models.Verification
       fields = ('id' , 'matricule')






class ProfileFeedItemSerializer(serializers.ModelSerializer):
     """A serializer for profile feed items."""

     class Meta :
         model = models.ProfileFeedItem
         fields = ('id' , 'user_profile' , 'status_text' , 'created_on')
         extra_kwargs = {'user_profile': {'read_only' : True}}



#############NIHAL##########################"
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Etudiant
        fields =('id' , 'matricule')


    #########################################