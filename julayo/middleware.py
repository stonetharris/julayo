from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin

class SecureMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.is_secure():
            if not any(map(request.get_host().__contains__, ['localhost', '127.0.0.1'])):
                request_url = request.build_absolute_uri(request.get_full_path())
                secure_url = request_url.replace('http://', 'https://')
                return HttpResponsePermanentRedirect(secure_url)
