# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.add_contact_list_contacts_request import AddContactListContactsRequest
from openapi_server.models.add_do_not_contact_request import AddDoNotContactRequest
from openapi_server.models.contact import Contact
from openapi_server.models.contact_history import ContactHistory
from openapi_server.models.contact_list import ContactList
from openapi_server.models.contact_list_page import ContactListPage
from openapi_server.models.contact_page import ContactPage
from openapi_server.models.create_contact_list_request import CreateContactListRequest
from openapi_server.models.do_not_contact import DoNotContact
from openapi_server.models.do_not_contact_page import DoNotContactPage
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.item_list_universal_do_not_contact import ItemListUniversalDoNotContact
from openapi_server.models.resource_id import ResourceId
from openapi_server.models.resource_id_list import ResourceIdList
from openapi_server.models.update_contact_list_request import UpdateContactListRequest


pytestmark = pytest.mark.asyncio

async def test_add_contact_list_items(client):
    """Test case for add_contact_list_items

    Add contacts to a contact list
    """
    body = {"contactNumbers":["contactNumbers","contactNumbers"],"useCustomFields":True,"contactNumbersField":"contactNumbersField","contactIds":[0,0],"contacts":[{"lastName":"lastName","homePhone":"homePhone","extraPhone3":"extraPhone3","externalId":"externalId","extraPhone2":"extraPhone2","extraPhone1":"extraPhone1","externalSystem":"externalSystem","zipcode":"zipcode","firstName":"firstName","deleted":True,"mobilePhone":"mobilePhone","workPhone":"workPhone","id":2,"properties":{"key":"properties"}},{"lastName":"lastName","homePhone":"homePhone","extraPhone3":"extraPhone3","externalId":"externalId","extraPhone2":"extraPhone2","extraPhone1":"extraPhone1","externalSystem":"externalSystem","zipcode":"zipcode","firstName":"firstName","deleted":True,"mobilePhone":"mobilePhone","workPhone":"workPhone","id":2,"properties":{"key":"properties"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/contacts/lists/{id}/items'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_do_not_contacts(client):
    """Test case for add_do_not_contacts

    Add do not contact (dnc) numbers
    """
    body = {"call":True,"inboundText":True,"inboundCall":True,"numbers":["numbers","numbers"],"source":"source","text":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/contacts/dncs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_contact_list(client):
    """Test case for create_contact_list

    Create contact lists
    """
    body = {"contactNumbers":["contactNumbers","contactNumbers"],"useCustomFields":True,"contactNumbersField":"contactNumbersField","name":"name","contactIds":[0,0],"contacts":[{"lastName":"lastName","homePhone":"homePhone","extraPhone3":"extraPhone3","externalId":"externalId","extraPhone2":"extraPhone2","extraPhone1":"extraPhone1","externalSystem":"externalSystem","zipcode":"zipcode","firstName":"firstName","deleted":True,"mobilePhone":"mobilePhone","workPhone":"workPhone","id":2,"properties":{"key":"properties"}},{"lastName":"lastName","homePhone":"homePhone","extraPhone3":"extraPhone3","externalId":"externalId","extraPhone2":"extraPhone2","extraPhone1":"extraPhone1","externalSystem":"externalSystem","zipcode":"zipcode","firstName":"firstName","deleted":True,"mobilePhone":"mobilePhone","workPhone":"workPhone","id":2,"properties":{"key":"properties"}}]}
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/contacts/lists',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_contact_list_from_file(client):
    """Test case for create_contact_list_from_file

    Create contact list from file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('name', 'name_example')
    data.add_field('use_custom_fields', True)
    response = await client.request(
        method='POST',
        path='/v2/contacts/lists/upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_contacts(client):
    """Test case for create_contacts

    Create contacts
    """
    body = {"lastName":"lastName","homePhone":"homePhone","extraPhone3":"extraPhone3","externalId":"externalId","extraPhone2":"extraPhone2","extraPhone1":"extraPhone1","externalSystem":"externalSystem","zipcode":"zipcode","firstName":"firstName","deleted":True,"mobilePhone":"mobilePhone","workPhone":"workPhone","id":2,"properties":{"key":"properties"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/contacts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_contact(client):
    """Test case for delete_contact

    Delete a contact
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/contacts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_contact_list(client):
    """Test case for delete_contact_list

    Delete a contact list
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/contacts/lists/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_do_not_contact(client):
    """Test case for delete_do_not_contact

    Delete do not contact (dnc) number. If number contains commas treat as list of numbers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/contacts/dncs/{number}'.format(number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_do_not_contacts_by_source(client):
    """Test case for delete_do_not_contacts_by_source

    Delete do not contact (dnc) numbers contained in source.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/contacts/dncs/sources/{source}'.format(source='source_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_contact_lists(client):
    """Test case for find_contact_lists

    Find contact lists
    """
    params = [('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0),
                    ('name', 'name_example'),
                    ('exactMatch', True),
                    ('contactCount', 56),
                    ('orderBy', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts/lists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_contacts(client):
    """Test case for find_contacts

    Find contacts
    """
    params = [('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0),
                    ('id', [56]),
                    ('number', ['number_example']),
                    ('contactListId', 56),
                    ('propertyName', 'property_name_example'),
                    ('propertyValue', 'property_value_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_do_not_contacts(client):
    """Test case for find_do_not_contacts

    Find do not contact (dnc) items
    """
    params = [('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0),
                    ('prefix', 'prefix_example'),
                    ('campaignId', 56),
                    ('source', 'source_example'),
                    ('call', True),
                    ('text', True),
                    ('inboundCall', True),
                    ('inboundText', True),
                    ('number', ['number_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts/dncs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact(client):
    """Test case for get_contact

    Find a specific contact
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact_history(client):
    """Test case for get_contact_history

    Find a contact's history
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts/{id}/history'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact_list(client):
    """Test case for get_contact_list

    Find a specific contact list
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts/lists/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact_list_items(client):
    """Test case for get_contact_list_items

    Find contacts in a contact list
    """
    params = [('fields', 'fields_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts/lists/{id}/items'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_do_not_contact(client):
    """Test case for get_do_not_contact

    Get do not contact (dnc)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts/dncs/{number}'.format(number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universal_do_not_contacts(client):
    """Test case for get_universal_do_not_contacts

    Find universal do not contacts (udnc) associated with toNumber
    """
    params = [('fromNumber', 'from_number_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contacts/dncs/universals/{to_number}'.format(to_number='to_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_contact_list_item(client):
    """Test case for remove_contact_list_item

    Delete a contact from a contact list
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/contacts/lists/{id}/items/{contact_id}'.format(id=56, contact_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_contact_list_items(client):
    """Test case for remove_contact_list_items

    Delete contacts from a contact list
    """
    params = [('contactId', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/contacts/lists/{id}/items'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_contact(client):
    """Test case for update_contact

    Update a contact
    """
    body = {"lastName":"lastName","homePhone":"homePhone","extraPhone3":"extraPhone3","externalId":"externalId","extraPhone2":"extraPhone2","extraPhone1":"extraPhone1","externalSystem":"externalSystem","zipcode":"zipcode","firstName":"firstName","deleted":True,"mobilePhone":"mobilePhone","workPhone":"workPhone","id":2,"properties":{"key":"properties"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/contacts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_contact_list(client):
    """Test case for update_contact_list

    Update a contact list
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/contacts/lists/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_do_not_contact(client):
    """Test case for update_do_not_contact

    Update an individual do not contact (dnc) number
    """
    body = {"call":True,"inboundText":True,"number":"number","campaignId":5,"created":5,"inboundCall":True,"source":"source","text":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/contacts/dncs/{number}'.format(number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

