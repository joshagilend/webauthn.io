from django.shortcuts import render

from .forms import UsernameForm


def index(request):
    """
    Render the homepage
    """
    username_form = UsernameForm()
    context = {
        "username_form": username_form,
        "libraries": [
            {
                "language": "Go",
                "url": "https://github.com/duo-labs/webauthn",
                "title": "duo-labs/webauthn",
                "author": "Duo Labs",
                "type": "Server",
            },
            {
                "language": "Python",
                "url": "https://github.com/duo-labs/webauthn.io",
                "title": "duo-labs/webauthn-io-2",
                "author": "Duo Labs",
                "type": "Demo",
            },
            {
                "language": "Go",
                "url": "https://github.com/koesie10/webauthn",
                "title": "koesie10/webauthn",
                "author": "Koen Vlaswinkel",
                "type": "Server",
            },
            {
                "language": "Java",
                "url": "https://github.com/duo-labs/android-webauthn-authenticator",
                "title": "duo-labs/android-webauthn-authenticator",
                "author": "Duo Labs",
                "type": "Authenticator",
            },
            {
                "language": "Java",
                "url": "https://github.com/google/webauthndemo",
                "title": "google/webauthndemo",
                "author": "Google",
                "type": "Demo",
            },
            {
                "language": "Java",
                "url": "https://github.com/webauthn4j/webauthn4j",
                "title": "webauthn4j/webauthn4j",
                "author": "Yoshikazu Nojima",
                "type": "Server",
            },
            {
                "language": "Java",
                "url": "https://github.com/Yubico/java-webauthn-server",
                "title": "Yubico/java-webauthn-server",
                "author": "Yubico",
                "type": "Server",
            },
            {
                "language": "Javascript",
                "url": "https://github.com/fido-alliance/webauthn-demo",
                "title": "fido-alliance/webauthn-demo",
                "author": "Fido Alliance",
                "type": "Demo",
            },
            {
                "language": ".NET",
                "url": "https://github.com/abergs/fido2-net-lib",
                "title": "abergs/fido2-net-lib",
                "author": "Anders Åberg",
                "type": "Server/Demo",
            },
            {
                "language": "Python",
                "url": "https://github.com/duo-labs/py_webauthn",
                "title": "duo-labs/py_webauthn",
                "author": "Duo Labs",
                "type": "Server/Demo",
            },
            {
                "language": "Ruby",
                "url": "https://github.com/cedarcode/webauthn-ruby",
                "title": "cedarcode/webauthn-ruby",
                "author": "Cedarcode",
                "type": "Server",
            },
            {
                "language": "Chrome Extension",
                "url": "https://github.com/google/virtual-authenticators-tab",
                "title": "google/virtual-authenticators-tab",
                "author": "Nina Satragno",
                "type": "Authenticator",
            },
        ],
    }

    return render(request, "homepage/index.html", context)
