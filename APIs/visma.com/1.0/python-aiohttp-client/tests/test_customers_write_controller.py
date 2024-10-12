# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_model import AddressModel
from openapi_server.models.contact_communication_model import ContactCommunicationModel
from openapi_server.models.contact_keyword_model import ContactKeywordModel
from openapi_server.models.contact_model import ContactModel
from openapi_server.models.customer_country_settings_input_model import CustomerCountrySettingsInputModel
from openapi_server.models.customer_country_settings_output_model import CustomerCountrySettingsOutputModel
from openapi_server.models.customer_custom_value_model import CustomerCustomValueModel
from openapi_server.models.customer_market_segment_model import CustomerMarketSegmentModel
from openapi_server.models.customer_model import CustomerModel
from openapi_server.models.customer_sales_note_input_model import CustomerSalesNoteInputModel
from openapi_server.models.customer_sales_note_output_model import CustomerSalesNoteOutputModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation


pytestmark = pytest.mark.asyncio

async def test_addresses_patch_address(client):
    """Test case for addresses_patch_address

    Update (Patch) an address or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/addresses/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_addresses_post_customer_address(client):
    """Test case for addresses_post_customer_address

    Insert an address.
    """
    body = {"country":{"englishName":"englishName","hasRegions":"NoRegion","name":"name","guid":"guid"},"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"city":"city","isVisitAddress":True,"isPostalAddress":True,"countryRegion":{"name":"name","guid":"guid"},"postalCode":"postalCode","createdDateTime":"2000-01-23T04:56:07.000+00:00","isBillingAddress":True,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"phone":"phone","guid":"guid","addressline":"addressline","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","fax":"fax","contacts":[{"name":"name","guid":"guid"},{"name":"name","guid":"guid"}],"customer":{"number":0,"name":"name","guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/customers/{customer_guid}/addresses'.format(customer_guid='customer_guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_communications_patch_contact_communication(client):
    """Test case for contact_communications_patch_contact_communication

    Update (Patch) a contact's communication or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/contactcommunications/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_communications_post_contact_communication(client):
    """Test case for contact_communications_post_contact_communication

    Insert a communication for a contact.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isForbiddenToUse":True,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"contact":{"name":"name","guid":"guid"},"createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","communicationType":{"name":"name","guid":"guid","isActive":True,"type":"Phone"},"lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/contactcommunications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_patch_contact(client):
    """Test case for contacts_patch_contact

    Update (Patch) an contact or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/contactpersons/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_post_contact(client):
    """Test case for contacts_post_contact

    Insert a contact.
    """
    body = {"lastName":"lastName","lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"role":{"name":"name","guid":"guid"},"jobTitle":"jobTitle","createdDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","timeZone":{"name":"name","guid":"guid"},"dateOfBirth":"2000-01-23","language":{"name":"name","guid":"guid"},"isActive":True,"phoneNumbers":["phoneNumbers","phoneNumbers"],"emails":["emails","emails"],"firstName":"firstName","isDeleted":True,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isEmailAllowed":False,"satisfactionLevel":"Unsatisfied","name":"name","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","salutation":"Mr.","addressGuid":"addressGuid","customer":{"number":0,"name":"name","guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/contactpersons',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_country_settings_patch_customer_country_settings(client):
    """Test case for customer_country_settings_patch_customer_country_settings

    Update (Patch) a customer country setting.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/customercountrysettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_country_settings_post_customer_country_settings(client):
    """Test case for customer_country_settings_post_customer_country_settings

    Insert a customer country setting.
    """
    body = {"country":{"guid":"guid"},"valueAddedTax":{"guid":"guid"},"taxFreeDescription":"taxFreeDescription","isTaxFree":True,"zeroVatCategoryCodeEn16931":"zeroVatCategoryCodeEn16931","customer":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/customercountrysettings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_values_patch_customer_custom_value(client):
    """Test case for customer_custom_values_patch_customer_custom_value

    Update (Patch) a customer custom value or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/customers/customvalues/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_values_post_customer_custom_value(client):
    """Test case for customer_custom_values_post_customer_custom_value

    Insert a customer custom value.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"customerGuid":"customerGuid","createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","value":"value","customProperty":{"name":"name","guid":"guid","type":"Numeric","parameters":"parameters"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/customers/customvalues',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_market_segments_post_customer_market_segment(client):
    """Test case for customer_market_segments_post_customer_market_segment

    Add a market segment for customer.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","parentMarketSegment":{"name":"name","guid":"guid","isActive":True},"customer":{"name":"name","guid":"guid"},"marketSegment":{"name":"name","guid":"guid","isActive":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/customermarketsegments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_patch_customer(client):
    """Test case for customers_patch_customer

    Update (Patch) an customer or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/customers/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_post_customer(client):
    """Test case for customers_post_customer

    Insert a customer.
    """
    body = {"overdueInterest":5.637376656633329,"eInvoiceOperator":"eInvoiceOperator","notes":"notes","timezone":{"name":"name","guid":"guid"},"headquarterAddress":{"country":"country","city":"city","postalCode":"postalCode","guid":"guid","addressline":"addressline"},"createdDateTime":"2000-01-23T04:56:07.000+00:00","industry":{"name":"name","guid":"guid"},"language":{"englishName":"englishName","code":"code","name":"name","guid":"guid"},"isActive":True,"number":1,"kvkNumber":"kvkNumber","currency":{"symbol":"symbol","code":"code","name":"name","guid":"guid"},"email":"email","owner":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"website":"website","invoicingVat":{"code":"code","percentage":6.027456183070403,"guid":"guid"},"eInvoiceAddress":"eInvoiceAddress","numberOfEmployees":5,"isInternal":True,"pricelist":{"name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"invoiceTemplate":{"name":"name","guid":"guid"},"name":"name","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","paymentTerm":2,"annualRevenue":0,"vatNumber":"vatNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/customers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_link_keyword_to_contact(client):
    """Test case for keywords_link_keyword_to_contact

    Link existing keyword to contact
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/contacts/{contact_guid}/keywords/{guid}'.format(contact_guid='contact_guid_example', guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_patch_customer_sales_note(client):
    """Test case for sales_notes_patch_customer_sales_note

    Update (Patch) a customer sales note or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/customersalesnotes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_post_customer_sales_notes(client):
    """Test case for sales_notes_post_customer_sales_notes

    Insert a customer sales note.
    """
    body = {"note":"note","user":{"guid":"guid"},"customer":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/customersalesnotes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

