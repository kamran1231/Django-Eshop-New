from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if not request.session.get('customer'):
            return redirect('login')
        

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware