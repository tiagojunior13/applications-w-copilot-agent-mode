from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'URL for users',
        'teams': 'URL for teams',
        'activity': 'URL for activity',
        'leaderboard': 'URL for leaderboard',
        'workouts': 'URL for workouts',
    })