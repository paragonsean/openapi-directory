# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.connection import Connection
from openapi_server.models.connection_import_data import ConnectionImportData
from openapi_server.models.create_connection_response import CreateConnectionResponse
from openapi_server.models.get_connection_response import GetConnectionResponse
from openapi_server.models.get_connections_response import GetConnectionsResponse
from openapi_server.models.get_custom_fields_response import GetCustomFieldsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_connection_response import UpdateConnectionResponse


pytestmark = pytest.mark.asyncio

async def test_connection_settings_all(client):
    """Test case for connection_settings_all

    Get resource settings
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vault/connections/{unified_api}/{service_id}/{resource}/config'.format(unified_api='crm', service_id='pipedrive', resource='leads'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_settings_update(client):
    """Test case for connection_settings_update

    Update settings
    """
    body = {"authorize_url":"https://unify.apideck.com/vault/authorize/salesforce/<application-id>?state=<state>","metadata":{"account":{"id":"c01458a5-7276-41ce-bc19-639906b0450a","name":"My Company"},"plan":"enterprise"},"subscriptions":[{"downstream_event_types":["contacts.CREATED","contacts.CREATED"],"execute_url":"https://unify.apideck.com/webhook/w/{lookupIdToken}/{serviceId}?e={downstreamEventType}","created_at":"2020-10-01T12:00:00.000Z","downstream_id":"5f5f5f5f5f5f5f5f5f5f5f5f","unify_event_types":["crm.contact.created","crm.contact.created"]},{"downstream_event_types":["contacts.CREATED","contacts.CREATED"],"execute_url":"https://unify.apideck.com/webhook/w/{lookupIdToken}/{serviceId}?e={downstreamEventType}","created_at":"2020-10-01T12:00:00.000Z","downstream_id":"5f5f5f5f5f5f5f5f5f5f5f5f","unify_event_types":["crm.contact.created","crm.contact.created"]}],"configuration":[{"defaults":[{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"},{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"}],"resource":"leads"},{"defaults":[{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"},{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"}],"resource":"leads"}],"icon":"https://res.cloudinary.com/apideck/image/upload/v1529456047/catalog/salesforce/icon128x128.png","created_at":1615563533390,"tag_line":"CRM software solutions and enterprise cloud computing from Salesforce, the leader in customer relationship management (CRM) and PaaS. Free 30 day trial.","enabled":True,"custom_mappings":[{"consumer_id":"test_user_id","custom_field":True,"description":"First Aid Training completed after 2019-01-01","id":"hris+employees+first_aid_training","label":"First Aid Training","value":"$.root.training.first_aid","key":"first_aid_training","required":False},{"consumer_id":"test_user_id","custom_field":True,"description":"First Aid Training completed after 2019-01-01","id":"hris+employees+first_aid_training","label":"First Aid Training","value":"$.root.training.first_aid","key":"first_aid_training","required":False}],"form_fields":[{"custom_field":False,"disabled":False,"id":"instance_url","label":"Instance url","mask":False,"placeholder":"","required":True,"sensitive":False,"type":"text","value":"https://eu28.salesforce.com"},{"custom_field":False,"disabled":False,"id":"api_key","label":"API Key","mask":False,"placeholder":"","required":True,"sensitive":True,"type":"text","value":"123455677"}],"revoke_url":"https://unify.apideck.com/vault/revoke/salesforce/<application-id>?state=<state>","updated_at":1616662325753,"service_id":"salesforce","logo":"https://c1.sfdcstatic.com/content/dam/web/en_us/www/images/home/logo-salesforce-m.svg","schema_support":True,"id":"crm+salesforce","state":"authorized","has_guide":True,"resource_schema_support":["leads"],"settings":{"api_key":"12345xxxxxx","instance_url":"https://eu28.salesforce.com"},"auth_type":"oauth2","settings_required_for_authorization":["client_id","client_secret"],"website":"https://www.salesforce.com","configurable_resources":["opportunities","companies","contacts","leads"],"validation_support":True,"oauth_grant_type":"authorization_code","integration_state":"configured","name":"Salesforce","resource_settings_support":["leads"],"unified_api":"crm","status":"live"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/vault/connections/{unified_api}/{service_id}/{resource}/config'.format(service_id='pipedrive', unified_api='crm', resource='leads'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_add(client):
    """Test case for connections_add

    Create connection
    """
    body = {"authorize_url":"https://unify.apideck.com/vault/authorize/salesforce/<application-id>?state=<state>","metadata":{"account":{"id":"c01458a5-7276-41ce-bc19-639906b0450a","name":"My Company"},"plan":"enterprise"},"subscriptions":[{"downstream_event_types":["contacts.CREATED","contacts.CREATED"],"execute_url":"https://unify.apideck.com/webhook/w/{lookupIdToken}/{serviceId}?e={downstreamEventType}","created_at":"2020-10-01T12:00:00.000Z","downstream_id":"5f5f5f5f5f5f5f5f5f5f5f5f","unify_event_types":["crm.contact.created","crm.contact.created"]},{"downstream_event_types":["contacts.CREATED","contacts.CREATED"],"execute_url":"https://unify.apideck.com/webhook/w/{lookupIdToken}/{serviceId}?e={downstreamEventType}","created_at":"2020-10-01T12:00:00.000Z","downstream_id":"5f5f5f5f5f5f5f5f5f5f5f5f","unify_event_types":["crm.contact.created","crm.contact.created"]}],"configuration":[{"defaults":[{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"},{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"}],"resource":"leads"},{"defaults":[{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"},{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"}],"resource":"leads"}],"icon":"https://res.cloudinary.com/apideck/image/upload/v1529456047/catalog/salesforce/icon128x128.png","created_at":1615563533390,"tag_line":"CRM software solutions and enterprise cloud computing from Salesforce, the leader in customer relationship management (CRM) and PaaS. Free 30 day trial.","enabled":True,"custom_mappings":[{"consumer_id":"test_user_id","custom_field":True,"description":"First Aid Training completed after 2019-01-01","id":"hris+employees+first_aid_training","label":"First Aid Training","value":"$.root.training.first_aid","key":"first_aid_training","required":False},{"consumer_id":"test_user_id","custom_field":True,"description":"First Aid Training completed after 2019-01-01","id":"hris+employees+first_aid_training","label":"First Aid Training","value":"$.root.training.first_aid","key":"first_aid_training","required":False}],"form_fields":[{"custom_field":False,"disabled":False,"id":"instance_url","label":"Instance url","mask":False,"placeholder":"","required":True,"sensitive":False,"type":"text","value":"https://eu28.salesforce.com"},{"custom_field":False,"disabled":False,"id":"api_key","label":"API Key","mask":False,"placeholder":"","required":True,"sensitive":True,"type":"text","value":"123455677"}],"revoke_url":"https://unify.apideck.com/vault/revoke/salesforce/<application-id>?state=<state>","updated_at":1616662325753,"service_id":"salesforce","logo":"https://c1.sfdcstatic.com/content/dam/web/en_us/www/images/home/logo-salesforce-m.svg","schema_support":True,"id":"crm+salesforce","state":"authorized","has_guide":True,"resource_schema_support":["leads"],"settings":{"api_key":"12345xxxxxx","instance_url":"https://eu28.salesforce.com"},"auth_type":"oauth2","settings_required_for_authorization":["client_id","client_secret"],"website":"https://www.salesforce.com","configurable_resources":["opportunities","companies","contacts","leads"],"validation_support":True,"oauth_grant_type":"authorization_code","integration_state":"configured","name":"Salesforce","resource_settings_support":["leads"],"unified_api":"crm","status":"live"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vault/connections/{unified_api}/{service_id}'.format(service_id='pipedrive', unified_api='crm'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_all(client):
    """Test case for connections_all

    Get all connections
    """
    params = [('api', 'crm'),
                    ('configured', true)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vault/connections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_authorize(client):
    """Test case for connections_authorize

    Authorize
    """
    params = [('state', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk'),
                    ('redirect_uri', 'http://example.com/integrations'),
                    ('scope', ['[\"openid\",\"leads:write\",\"profile:read\"]'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/vault/authorize/{service_id}/{application_id}'.format(service_id='pipedrive', application_id='dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_callback(client):
    """Test case for connections_callback

    Callback
    """
    params = [('state', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk'),
                    ('code', 'g0ZGZmNjVmOWI')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/vault/callback',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_delete(client):
    """Test case for connections_delete

    Deletes a connection
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/vault/connections/{unified_api}/{service_id}'.format(service_id='pipedrive', unified_api='crm'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_import(client):
    """Test case for connections_import

    Import connection
    """
    body = {"settings":{"instance_url":"https://eu28.salesforce.com"},"metadata":{"account":{"id":"c01458a5-7276-41ce-bc19-639906b0450a","name":"My Company"},"plan":"enterprise"},"credentials":{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c","refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cThIIoDvwdueQB468K5xDc5633seEFoqwxjF_xSJyQQ"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vault/connections/{unified_api}/{service_id}/import'.format(service_id='pipedrive', unified_api='crm'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_one(client):
    """Test case for connections_one

    Get connection
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vault/connections/{unified_api}/{service_id}'.format(service_id='pipedrive', unified_api='crm'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_revoke(client):
    """Test case for connections_revoke

    Revoke connection
    """
    params = [('state', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk'),
                    ('redirect_uri', 'http://example.com/integrations')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/vault/revoke/{service_id}/{application_id}'.format(service_id='pipedrive', application_id='dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_token(client):
    """Test case for connections_token

    Get Access Token
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vault/connections/{unified_api}/{service_id}/token'.format(service_id='pipedrive', unified_api='crm'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_update(client):
    """Test case for connections_update

    Update connection
    """
    body = {"authorize_url":"https://unify.apideck.com/vault/authorize/salesforce/<application-id>?state=<state>","metadata":{"account":{"id":"c01458a5-7276-41ce-bc19-639906b0450a","name":"My Company"},"plan":"enterprise"},"subscriptions":[{"downstream_event_types":["contacts.CREATED","contacts.CREATED"],"execute_url":"https://unify.apideck.com/webhook/w/{lookupIdToken}/{serviceId}?e={downstreamEventType}","created_at":"2020-10-01T12:00:00.000Z","downstream_id":"5f5f5f5f5f5f5f5f5f5f5f5f","unify_event_types":["crm.contact.created","crm.contact.created"]},{"downstream_event_types":["contacts.CREATED","contacts.CREATED"],"execute_url":"https://unify.apideck.com/webhook/w/{lookupIdToken}/{serviceId}?e={downstreamEventType}","created_at":"2020-10-01T12:00:00.000Z","downstream_id":"5f5f5f5f5f5f5f5f5f5f5f5f","unify_event_types":["crm.contact.created","crm.contact.created"]}],"configuration":[{"defaults":[{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"},{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"}],"resource":"leads"},{"defaults":[{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"},{"options":[{"label":"General Channel","value":"general"},{"label":"General Channel","value":"general"}],"id":"ProductInterest","value":"GC5000 series","target":"custom_fields"}],"resource":"leads"}],"icon":"https://res.cloudinary.com/apideck/image/upload/v1529456047/catalog/salesforce/icon128x128.png","created_at":1615563533390,"tag_line":"CRM software solutions and enterprise cloud computing from Salesforce, the leader in customer relationship management (CRM) and PaaS. Free 30 day trial.","enabled":True,"custom_mappings":[{"consumer_id":"test_user_id","custom_field":True,"description":"First Aid Training completed after 2019-01-01","id":"hris+employees+first_aid_training","label":"First Aid Training","value":"$.root.training.first_aid","key":"first_aid_training","required":False},{"consumer_id":"test_user_id","custom_field":True,"description":"First Aid Training completed after 2019-01-01","id":"hris+employees+first_aid_training","label":"First Aid Training","value":"$.root.training.first_aid","key":"first_aid_training","required":False}],"form_fields":[{"custom_field":False,"disabled":False,"id":"instance_url","label":"Instance url","mask":False,"placeholder":"","required":True,"sensitive":False,"type":"text","value":"https://eu28.salesforce.com"},{"custom_field":False,"disabled":False,"id":"api_key","label":"API Key","mask":False,"placeholder":"","required":True,"sensitive":True,"type":"text","value":"123455677"}],"revoke_url":"https://unify.apideck.com/vault/revoke/salesforce/<application-id>?state=<state>","updated_at":1616662325753,"service_id":"salesforce","logo":"https://c1.sfdcstatic.com/content/dam/web/en_us/www/images/home/logo-salesforce-m.svg","schema_support":True,"id":"crm+salesforce","state":"authorized","has_guide":True,"resource_schema_support":["leads"],"settings":{"api_key":"12345xxxxxx","instance_url":"https://eu28.salesforce.com"},"auth_type":"oauth2","settings_required_for_authorization":["client_id","client_secret"],"website":"https://www.salesforce.com","configurable_resources":["opportunities","companies","contacts","leads"],"validation_support":True,"oauth_grant_type":"authorization_code","integration_state":"configured","name":"Salesforce","resource_settings_support":["leads"],"unified_api":"crm","status":"live"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/vault/connections/{unified_api}/{service_id}'.format(service_id='pipedrive', unified_api='crm'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_all(client):
    """Test case for custom_fields_all

    Get resource custom fields
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vault/connections/{unified_api}/{service_id}/{resource}/custom-fields'.format(unified_api='crm', service_id='pipedrive', resource='leads'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

