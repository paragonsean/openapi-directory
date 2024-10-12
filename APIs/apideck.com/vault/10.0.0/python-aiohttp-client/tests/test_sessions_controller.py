# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_session_response import CreateSessionResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.session import Session
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse


pytestmark = pytest.mark.asyncio

async def test_sessions_create(client):
    """Test case for sessions_create

    Create Session
    """
    body = {"settings":{"unified_apis":["crm","crm"],"sandbox_mode":False,"show_suggestions":False,"hide_resource_settings":False,"session_length":"30m","show_logs":True,"isolation_mode":False,"hide_guides":False,"allow_actions":["delete","delete"],"auto_redirect":False,"show_sidebar":True},"consumer_metadata":{"image":"https://www.spacex.com/static/images/share.jpg","user_name":"Elon Musk","account_name":"SpaceX","email":"elon@musk.com"},"custom_consumer_settings":{"feature_flag_1":True,"tax_rates":[{"id":"6","label":"6%"},{"id":"21","label":"21%"}]},"theme":{"sidepanel_text_color":"#FFFFFF","favicon":"https://res.cloudinary.com/apideck/icons/intercom","sidepanel_background_color":"#286efa","terms_url":"https://www.termsfeed.com/terms-conditions/957c85c1b089ae9e3219c83eff65377e","logo":"https://res.cloudinary.com/apideck/icons/intercom","privacy_url":"https://compliance.apideck.com/privacy-policy","vault_name":"Intercom","primary_color":"#286efa"},"redirect_uri":"https://mysaas.com/dashboard"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vault/sessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

