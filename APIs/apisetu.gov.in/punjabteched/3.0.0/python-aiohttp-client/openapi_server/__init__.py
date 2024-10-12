import os
import connexion

def main():
    options = {
        "swagger_ui": True
        }
    specification_dir = os.path.join(os.path.dirname(__file__), 'openapi')
    app = connexion.AioHttpApp(__name__, specification_dir=specification_dir, options=options)
    app.add_api('openapi.yaml',
                arguments={'title': 'The Punjab State Board of Technical Education &amp; Industrial Training'},
                pythonic_params=True,
                pass_context_arg_name='request')

    app.run(port=8080)
