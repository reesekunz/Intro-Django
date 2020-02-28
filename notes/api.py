from rest_framework import serializers, viewsets
from .models import PersonalNote
# determine which fields you want to export to api (from models)


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # register model interested in with metadata
    class Meta:
        # connects this class to PersonalNote model (in models.py)
        model = PersonalNote
        # title and content come from models fields
        fields = ("title", "content")

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        # pass in validated data as keyword arguments (title and content)
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

# validated_data returns POST request: {'title': 'postin note', 'content': 'hihi'}

# define which rows you want to export to api (do this using viewsets)


class PersonalNoteViewSet(viewsets.ModelViewSet):
    # attach to PersonalNoteSerializer class above
    serializer_class = PersonalNoteSerializer
    # what we want to return - return all
    queryset = PersonalNote.objects.none()
# want to base the data being returned on which user is logged in 
    def get_queryset(self):
        # get user
        user = self.request.user
        # user is not logged in, return nothing
        if user.is_anonymous:
            return PersonalNote.objects.none()
        # user is logged in, filter objects displayed based on logged in user (grabbed out of the request)
        else:
            return PersonalNote.objects.filter(user=user)



    # had an error: class PersonalNote has no objects member
    # steps to resolve -
    # 1. pip install pylint-django
    # 2. command + shift + p => preferences: Configure Language specific settings => Python
    # 3. "python.linting.pylintArgs": ["--load-plugins=pylint_django", ]
