# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_opportunity_response import CreateOpportunityResponse
from openapi_server.models.delete_opportunity_response import DeleteOpportunityResponse
from openapi_server.models.get_opportunities_response import GetOpportunitiesResponse
from openapi_server.models.get_opportunity_response import GetOpportunityResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.opportunities_filter import OpportunitiesFilter
from openapi_server.models.opportunities_sort import OpportunitiesSort
from openapi_server.models.opportunity import Opportunity
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_opportunity_response import UpdateOpportunityResponse


pytestmark = pytest.mark.asyncio

async def test_opportunities_add(client):
    """Test case for opportunities_add

    Create opportunity
    """
    body = {"close_date":"2020-10-30","won_reason_id":"12345","owner_id":"12345","lead_source":"Website","created_at":"2020-09-30T07:43:32Z","description":"Opportunities are created for People and Companies that are interested in buying your products or services. Create Opportunities for People and Companies to move them through one of your Pipelines.","monetary_amount":75000,"won_reason":"Best pitch","contact_id":"12345","title":"New Rocket","type":"Existing Customer - Upgrade","loss_reason":"No budget","custom_mappings":"{}","win_probability":40,"expected_revenue":75000,"status_id":"12345","updated_at":"2020-09-30T07:43:32Z","last_activity_at":"2020-09-30T07:43:32.000Z","date_stage_changed":"2020-09-30T00:00:00Z","pipeline_id":"12345","currency":"USD","id":"12345","stage_last_changed_at":"2020-09-30T07:43:32Z","lead_id":"12345","loss_reason_id":"12345","company_id":"12345","custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"priority":"None","contact_ids":["12345","12345"],"created_by":"12345","date_last_contacted":"2020-09-30T00:00:00Z","interaction_count":0,"tags":["New"],"primary_contact_id":"12345","date_lead_created":"2020-09-30T00:00:00Z","deleted":False,"company_name":"Copper","updated_by":"12345","source_id":"12345","pipeline_stage_id":"12345","status":"Open"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/crm/opportunities',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opportunities_all(client):
    """Test case for opportunities_all

    List opportunities
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.OpportunitiesFilter()),
                    ('sort', openapi_server.OpportunitiesSort()),
                    ('pass_through', None),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crm/opportunities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opportunities_delete(client):
    """Test case for opportunities_delete

    Delete opportunity
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/crm/opportunities/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opportunities_one(client):
    """Test case for opportunities_one

    Get opportunity
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crm/opportunities/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opportunities_update(client):
    """Test case for opportunities_update

    Update opportunity
    """
    body = {"close_date":"2020-10-30","won_reason_id":"12345","owner_id":"12345","lead_source":"Website","created_at":"2020-09-30T07:43:32Z","description":"Opportunities are created for People and Companies that are interested in buying your products or services. Create Opportunities for People and Companies to move them through one of your Pipelines.","monetary_amount":75000,"won_reason":"Best pitch","contact_id":"12345","title":"New Rocket","type":"Existing Customer - Upgrade","loss_reason":"No budget","custom_mappings":"{}","win_probability":40,"expected_revenue":75000,"status_id":"12345","updated_at":"2020-09-30T07:43:32Z","last_activity_at":"2020-09-30T07:43:32.000Z","date_stage_changed":"2020-09-30T00:00:00Z","pipeline_id":"12345","currency":"USD","id":"12345","stage_last_changed_at":"2020-09-30T07:43:32Z","lead_id":"12345","loss_reason_id":"12345","company_id":"12345","custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"priority":"None","contact_ids":["12345","12345"],"created_by":"12345","date_last_contacted":"2020-09-30T00:00:00Z","interaction_count":0,"tags":["New"],"primary_contact_id":"12345","date_lead_created":"2020-09-30T00:00:00Z","deleted":False,"company_name":"Copper","updated_by":"12345","source_id":"12345","pipeline_stage_id":"12345","status":"Open"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/crm/opportunities/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

