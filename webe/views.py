
from django.conf import settings
from rest_framework import generics, response, status
import datetime
from django.contrib.auth.models import User
from django.views import generic as views_generic
from firebase_admin import messaging

class ZenDeskWebHookApiView(generics.GenericAPIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        fcm_token = data.get('fcm_token')
        body = data.get('body')
        if not fcm_token:
            return response.Response(
                {'error': 'FCM token not provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        message = messaging.Message(
            notification=messaging.Notification(
                title='Mada Support Team',
                body=body,
            ),
            token=fcm_token,
        )

        try:
            # Send the message
            response_message = messaging.send(message)
            return response.Response(
                {'message': 'Notification sent successfully', 'response': response_message},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return response.Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
