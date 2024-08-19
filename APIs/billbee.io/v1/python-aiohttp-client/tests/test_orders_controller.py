# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_order import BillbeeInterfacesBillbeeAPIModelOrder
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_add_shipment_to_order_model import RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_invoice_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_order import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_order import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_invoice import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_search_controller_search_results_model import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_system_collections_generic_list_billbee_interfaces_billbee_api_models_layout_template import RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_api_controller_parse_text_container import RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_api_controller_send_message_model import RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_api_controller_trigger_event_container import RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_state_update import RechnungsdruckWebAppControllersApiOrderStateUpdate
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_tag_create import RechnungsdruckWebAppControllersApiOrderTagCreate
from openapi_server.models.rechnungsdruck_web_app_controllers_api_search_controller_search_model import RechnungsdruckWebAppControllersApiSearchControllerSearchModel


pytestmark = pytest.mark.asyncio

async def test_layout_api_get_list(client):
    """Test case for layout_api_get_list

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/layouts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_add_shipment(client):
    """Test case for order_api_add_shipment

    Add a shipment to a given order
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/{id}/shipment'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_create_delivery_note(client):
    """Test case for order_api_create_delivery_note

    Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.
    """
    params = [('includePdf', True),
                    ('sendToCloudId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/CreateDeliveryNote/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_create_invoice(client):
    """Test case for order_api_create_invoice

    Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.
    """
    params = [('includeInvoicePdf', True),
                    ('templateId', 56),
                    ('sendToCloudId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/CreateInvoice/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_find(client):
    """Test case for order_api_find

    Find a single order by its external id (order number)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orders/find/{id}/{partner}'.format(id='id_example', partner='partner_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_get(client):
    """Test case for order_api_get

    Get a single order by its internal billbee id. This request is throttled to 6 calls per order in one minute
    """
    params = [('articleTitleSource', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orders/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_get_by_ext_ref(client):
    """Test case for order_api_get_by_ext_ref

    Get a single order by its external order number
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orders/findbyextref/{ext_ref}'.format(ext_ref='ext_ref_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_get_invoice_list(client):
    """Test case for order_api_get_invoice_list

    Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate
    """
    params = [('minInvoiceDate', '2013-10-20T19:20:30+01:00'),
                    ('maxInvoiceDate', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('pageSize', 56),
                    ('shopId', [56]),
                    ('orderStateId', [56]),
                    ('tag', ['tag_example']),
                    ('minPayDate', '2013-10-20T19:20:30+01:00'),
                    ('maxPayDate', '2013-10-20T19:20:30+01:00'),
                    ('includePositions', True),
                    ('excludeTags', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orders/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_get_list(client):
    """Test case for order_api_get_list

    Get a list of all orders optionally filtered by date
    """
    params = [('minOrderDate', '2013-10-20T19:20:30+01:00'),
                    ('maxOrderDate', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('pageSize', 56),
                    ('shopId', [56]),
                    ('orderStateId', [56]),
                    ('tag', ['tag_example']),
                    ('minimumBillBeeOrderId', 56),
                    ('modifiedAtMin', '2013-10-20T19:20:30+01:00'),
                    ('modifiedAtMax', '2013-10-20T19:20:30+01:00'),
                    ('articleTitleSource', 56),
                    ('excludeTags', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_get_patchable_fields(client):
    """Test case for order_api_get_patchable_fields

    Returns a list of fields which can be updated with the orders/{id} patch call
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orders/PatchableFields',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_parse_placeholders(client):
    """Test case for order_api_parse_placeholders

    Parses a text and replaces all placeholders
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/{id}/parse-placeholders'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_patch_order(client):
    """Test case for order_api_patch_order

    Updates one or more fields of an order
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/orders/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_post_new_order(client):
    """Test case for order_api_post_new_order

    Creates a new order in the Billbee account
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelOrder()
    params = [('shopId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_send_message(client):
    """Test case for order_api_send_message

    Sends a message to the buyer
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/{id}/send-message'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_tags_create(client):
    """Test case for order_api_tags_create

    Attach one or more tags to an order
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiOrderTagCreate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/{id}/tags'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_tags_update(client):
    """Test case for order_api_tags_update

    Sets the tags attached to an order
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiOrderTagCreate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/orders/{id}/tags'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_trigger_event(client):
    """Test case for order_api_trigger_event

    Triggers a rule event
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/{id}/trigger-event'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_update_state(client):
    """Test case for order_api_update_state

    Changes the main state of a single order
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiOrderStateUpdate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/orders/{id}/orderstate'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_search_search_1(client):
    """Test case for search_search_1

    Search for products, customers and orders.  Type can be \"order\", \"product\" and / or \"customer\"  Term can contains lucene query syntax
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiSearchControllerSearchModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

