# custom_headers_middleware.py

class CustomHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Set and send the 'ngrok-skip-browser-warning' header with any value
        request.META['HTTP_NGROK_SKIP_BROWSER_WARNING'] = '1'  # Change '1' to any value you prefer

        response = self.get_response(request)
        return response
