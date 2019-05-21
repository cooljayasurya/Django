from django.core import serializers

class Serializer:
    
    def makeSerialize(self, type, myObject):
        return serializers.serialize(type ,[myObject])