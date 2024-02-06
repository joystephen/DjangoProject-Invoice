from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed

from .models import InvoiceHeader, InvoiceBillSundry, InvoiceItem
from .serializers import InvoiceHeaderSerializer, InvoiceBillSundrySerializer, InvoiceItemSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CustomAuthentication(BasicAuthentication):
    """
    Custom authentication class
    """
    def authenticate(self, request):
        # Example logic: Check if a specific header is present in the request
        token = request.headers.get('Authorization')

        if not token:
            # If the token is not present, return None to indicate authentication failed
            return None

        # Example logic: Validate the token against some criteria
        try:
            # Extract the token from the header
            # Assuming the token is in the format: "Bearer <token>"
            token_parts = token.split(' ')
            if len(token_parts) != 2 or token_parts[0].lower() != 'bearer':
                raise AuthenticationFailed('Invalid token format')

            # Get the user associated with the token

            # uncomment below 4 lines when user is defined and stuff
        #     user = User.objects.get(auth_token=token_parts[1])  # Assuming you have a custom token field in the User model
        # except User.DoesNotExist:
        #     # If user is not found, authentication fails
        #     raise AuthenticationFailed('User not found')
        except Exception as e:
            # If any other exception occurs, authentication fails
            raise AuthenticationFailed('Authentication failed: ' + str(e))

        # Return a tuple of (user, auth) if authentication is successful

        # uncomment below
        # return (user, None)

class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderSerializer
    # authentication_classes = [CustomAuthentication]  # Specify the authentication class(es)
    # permission_classes = [IsAuthenticated]  # Specify permissions if needed

    def post(self, request, format=None):
        pass

        # Your view logic here = do validations here
        # return Response({"message": "This is a protected view and requires authentication."})


class InvoiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderSerializer


class BillSundryListCreateAPIView(generics.ListCreateAPIView):
    queryset = InvoiceBillSundry.objects.all()
    serializer_class = InvoiceBillSundrySerializer

class BillSundryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceBillSundry.objects.all()
    serializer_class = InvoiceBillSundrySerializer


class InvoiceItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

class InvoiceItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
