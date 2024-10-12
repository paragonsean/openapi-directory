# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insert_affiliation_request import InsertAffiliationRequest
from openapi_server.models.insert_rule_request import InsertRuleRequest
from openapi_server.models.payment_systems_response import PaymentSystemsResponse
from openapi_server.models.rule_by_id_request import RuleByIdRequest
from openapi_server.models.update_affiliation_request import UpdateAffiliationRequest


pytestmark = pytest.mark.asyncio

async def test_affiliation_by_id(client):
    """Test case for affiliation_by_id

    Affiliation By Id
    """
    headers = { 
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/affiliations/{affiliation_id}'.format(affiliation_id='e046d326-5421-45ab-95ae-f13d37f260b5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_affiliations(client):
    """Test case for affiliations

    Affiliations
    """
    headers = { 
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/affiliations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_available_payment_methods(client):
    """Test case for available_payment_methods

    Available Payment Methods
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/merchants/payment-systems',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_insert_affiliation(client):
    """Test case for insert_affiliation

    Insert Affiliation
    """
    body = {"configuration":[{"name":"HowTo","value":"https://developercielo.github.io/Habilitacao-meios-de-pagamento/"},{"name":"MerchantId","value":"sampleData"},{"name":"MerchantKey","value":"sampleData"},{"name":"softDescriptor","value":"teste"},{"name":"bankInvoiceProvider","value":"Disabled"},{"name":"bankIDebitProvider","value":"Disabled"},{"name":"useEarlySecurityCapture","value":"0"},{"name":"isProduction","value":"false"},{"name":"bankDebitProvider","value":"Disabled"},{"name":"Registered","value":"false"}],"implementation":"Vtex.PaymentGateway.Connectors.CieloV3Connector","isConfigured":True,"isdelivered":True,"name":"CieloV3 - Teste Ellen"}
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/affiliations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_insert_rule(client):
    """Test case for insert_rule

    Insert Rule
    """
    body = {"antifraud":{"affiliationId":null,"implementation":null},"beginDate":null,"condition":null,"connector":{"affiliationId":"e046d326-5421-45ab-95ae-f13d37f260b5","implementation":"Vtex.PaymentGateway.Connectors.PromissoryConnector"},"country":null,"dateIntervals":null,"enabled":True,"endDate":null,"installmentOptions":null,"installmentsService":null,"isDefault":False,"isSelfAuthorized":null,"issuer":{"name":null},"multiMerchantList":null,"name":"Cash - Custom","paymentSystem":{"id":47,"implementation":null,"name":"Cash"},"requiresAuthentication":null,"salesChannels":[{"id":":ALL:"}]}
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_rule_by_id(client):
    """Test case for put_rule_by_id

    Rule By Id
    """
    body = {"antifraud":{"affiliationId":"f952588c-8b41-41cc-a06f-c0f48f7320ef"},"beginDate":"0001-01-01T00:00:00","condition":null,"connector":{"affiliationId":"d0d7097e-0959-43dc-b335-852eda7b2992","implementation":"Vtex.PaymentGateway.Connectors.MundipaggConnector"},"country":null,"dateIntervals":null,"enabled":True,"endDate":"9999-12-31T23:59:59.9999999","id":"eff4f368-b671-443b-b5a9-82616e87ea1c","installmentOptions":{"interestRateMethod":null},"isDefault":null,"isSelfAuthorized":null,"issuer":{"name":null},"multiMerchantList":null,"name":"Visa gatewayqa","paymentSystem":{"id":2,"implementation":null,"name":"Visa"},"salesChannels":[{"id":"2"}]}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/pvt/rules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rule(client):
    """Test case for rule

    Delete Rule
    """
    headers = { 
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/pvt/rules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rule_by_id(client):
    """Test case for rule_by_id

    Rule By Id
    """
    headers = { 
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/rules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rules(client):
    """Test case for rules

    Rules
    """
    headers = { 
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_affiliation(client):
    """Test case for update_affiliation

    Update Affiliation
    """
    body = {"configuration":[{"name":"HowTo","value":"https://developercielo.github.io/Habilitacao-meios-de-pagamento/"},{"name":"MerchantId","value":"DATA TEST"},{"name":"MerchantKey","value":"DATA TEST"},{"name":"softDescriptor","value":"teste"},{"name":"bankInvoiceProvider","value":"Disabled"},{"name":"bankIDebitProvider","value":"Disabled"},{"name":"useEarlySecurityCapture","value":"0"},{"name":"isProduction","value":"false"},{"name":"bankDebitProvider","value":"Disabled"},{"name":"Registered","value":"false"}],"id":"61c3b25b-554d-41a4-b989-a0ba215e4bba","implementation":"Vtex.PaymentGateway.Connectors.CieloV3Connector","isConfigured":True,"isdelivered":True,"name":"CieloV3 - Teste Ellen"}
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/pvt/affiliations/{affiliation_id}'.format(affiliation_id='e046d326-5421-45ab-95ae-f13d37f260b5'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

