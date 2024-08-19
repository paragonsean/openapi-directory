# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_model import AddressModel
from openapi_server.models.contact_communication_model import ContactCommunicationModel
from openapi_server.models.contact_model import ContactModel
from openapi_server.models.customer_country_settings_output_model import CustomerCountrySettingsOutputModel
from openapi_server.models.customer_custom_value_model import CustomerCustomValueModel
from openapi_server.models.customer_market_segment_model import CustomerMarketSegmentModel
from openapi_server.models.customer_model import CustomerModel
from openapi_server.models.customer_sales_note_output_model import CustomerSalesNoteOutputModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.key_value_pair_of_string_and_object import KeyValuePairOfStringAndObject
from openapi_server.models.key_value_pair_of_string_and_sort_direction import KeyValuePairOfStringAndSortDirection
from openapi_server.models.keyword_model import KeywordModel
from openapi_server.models.sales_note_output_model import SalesNoteOutputModel


pytestmark = pytest.mark.asyncio

async def test_addresses_get_address(client):
    """Test case for addresses_get_address

    Get address by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/addresses/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_addresses_get_addresses(client):
    """Test case for addresses_get_addresses

    Get the addresses.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('calculateRowCount', False),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/addresses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_addresses_get_contact_address(client):
    """Test case for addresses_get_contact_address

    Get contact person's address
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contactpersons/{contact_guid}/addresses'.format(contact_guid='contact_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_addresses_get_customer_addresses(client):
    """Test case for addresses_get_customer_addresses

    Get customer's addresses
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('calculateRowCount', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{customer_guid}/addresses'.format(customer_guid='customer_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_communications_get_communication(client):
    """Test case for contact_communications_get_communication

    Get contact communication by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contactcommunications/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_communications_get_communications(client):
    """Test case for contact_communications_get_communications

    Get all contact communications.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contactcommunications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_communications_get_communications2(client):
    """Test case for contact_communications_get_communications2

    Get all communications for a contact.
    """
    params = [('active', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contacts/{contact_guid}/contactcommunications'.format(contact_guid='contact_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_get_contact(client):
    """Test case for contacts_get_contact

    Get contact by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contactpersons/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_get_contacts(client):
    """Test case for contacts_get_contacts

    Get all the contact persons.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('searchCriterias', [openapi_server.KeyValuePairOfStringAndObject()]),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()]),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contactpersons',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_get_customer_contacts(client):
    """Test case for contacts_get_customer_contacts

    Get the contact persons for a customer.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', '')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{customer_guid}/contactpersons'.format(customer_guid='customer_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_country_settings_get_customer_country_settings(client):
    """Test case for customer_country_settings_get_customer_country_settings

    Get all the country settings for a customer.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{customer_guid}/customercountrysettings'.format(customer_guid='customer_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_values_get_customer_custom_value(client):
    """Test case for customer_custom_values_get_customer_custom_value

    Get customer custom value by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/customvalues/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_values_get_customer_custom_values(client):
    """Test case for customer_custom_values_get_customer_custom_values

    Get the customer custom values.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('active', True),
                    ('target', ['target_example']),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{customer_guid}/customvalues'.format(customer_guid='customer_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_market_segments_get_all_customer_market_segments(client):
    """Test case for customer_market_segments_get_all_customer_market_segments

    Get all Customer Market Segments.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('parentMarketSegmentGuid', 'parent_market_segment_guid_example'),
                    ('includeParentLevel', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customermarketsegments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_market_segments_get_customer_market_segment(client):
    """Test case for customer_market_segments_get_customer_market_segment

    Get the customer market segment.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customermarketsegments/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_market_segments_get_customer_market_segments(client):
    """Test case for customer_market_segments_get_customer_market_segments

    Get the Market Segments for a customer.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('includeMarketSegmentsFromRegistry', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{customer_guid}/customermarketsegments'.format(customer_guid='customer_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_get_customer(client):
    """Test case for customers_get_customer

    Get customer by GUID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_get_customers(client):
    """Test case for customers_get_customers

    Get all the customers
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isActive', True),
                    ('customerOwnerGuids', ['customer_owner_guids_example']),
                    ('isInternal', True),
                    ('numbers', [56]),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('emailAddresses', ['email_addresses_example']),
                    ('customerNames', ['customer_names_example'])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_get_contact_keywords(client):
    """Test case for keywords_get_contact_keywords

    Get all the keywords for contact.
    """
    params = [('active', True),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contacts/{contact_guid}/keywords'.format(contact_guid='contact_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_get_all_customer_sales_notes_0(client):
    """Test case for sales_notes_get_all_customer_sales_notes_0

    Get the sales notes by customer guid.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{customer_guid}/salesnotes'.format(customer_guid='customer_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_get_customer_sales_note(client):
    """Test case for sales_notes_get_customer_sales_note

    Get customer sales note by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customersalesnotes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_get_customer_sales_notes(client):
    """Test case for sales_notes_get_customer_sales_notes

    Get the customer sales notes.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{customer_guid}/customersalesnotes'.format(customer_guid='customer_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

