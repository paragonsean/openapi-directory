# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_add import CustomerAdd
from openapi_server.models.customer_add200_response import CustomerAdd200Response
from openapi_server.models.customer_count200_response import CustomerCount200Response
from openapi_server.models.customer_find200_response import CustomerFind200Response
from openapi_server.models.customer_group_add200_response import CustomerGroupAdd200Response
from openapi_server.models.customer_info200_response import CustomerInfo200Response
from openapi_server.models.customer_update import CustomerUpdate
from openapi_server.models.customer_update200_response import CustomerUpdate200Response
from openapi_server.models.customer_wishlist_list200_response import CustomerWishlistList200Response
from openapi_server.models.model_response_customer_attribute_list import ModelResponseCustomerAttributeList
from openapi_server.models.model_response_customer_group_list import ModelResponseCustomerGroupList
from openapi_server.models.model_response_customer_list import ModelResponseCustomerList


pytestmark = pytest.mark.asyncio

async def test_customer_add(client):
    """Test case for customer_add

    
    """
    body = {"store_id":"store_id","created_time":"created_time","website":"website","address":[{"address_book_company":"address_book_company","address_book_state":"address_book_state","address_book_phone_mobile":"address_book_phone_mobile","address_book_city":"address_book_city","address_book_region":"address_book_region","address_book_postcode":"address_book_postcode","address_book_first_name":"address_book_first_name","address_book_address2":"address_book_address2","address_book_address1":"address_book_address1","address_book_country":"address_book_country","address_book_last_name":"address_book_last_name","address_book_tax_id":"address_book_tax_id","address_book_phone":"address_book_phone","address_book_gender":"address_book_gender","address_book_default":True,"address_book_identification_number":"address_book_identification_number","address_book_website":"address_book_website","address_book_type":"address_book_type","address_book_fax":"address_book_fax"},{"address_book_company":"address_book_company","address_book_state":"address_book_state","address_book_phone_mobile":"address_book_phone_mobile","address_book_city":"address_book_city","address_book_region":"address_book_region","address_book_postcode":"address_book_postcode","address_book_first_name":"address_book_first_name","address_book_address2":"address_book_address2","address_book_address1":"address_book_address1","address_book_country":"address_book_country","address_book_last_name":"address_book_last_name","address_book_tax_id":"address_book_tax_id","address_book_phone":"address_book_phone","address_book_gender":"address_book_gender","address_book_default":True,"address_book_identification_number":"address_book_identification_number","address_book_website":"address_book_website","address_book_type":"address_book_type","address_book_fax":"address_book_fax"}],"gender":"gender","last_login":"last_login","last_name":"last_name","login":"login","birth_day":"birth_day","password":"password","modified_time":"modified_time","phone":"phone","company":"company","fax":"fax","news_letter_subscription":False,"first_name":"first_name","email":"email","group":"group","status":"enabled"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/customer.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_attribute_list(client):
    """Test case for customer_attribute_list

    
    """
    params = [('count', 10),
                    ('page_cursor', 'page_cursor_example'),
                    ('customer_id', 'customer_id_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('params', 'force_all'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/customer.attribute.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_count(client):
    """Test case for customer_count

    
    """
    params = [('group_id', 'group_id_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('store_id', 'store_id_example'),
                    ('customer_list_id', 'customer_list_id_example'),
                    ('avail', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/customer.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_find(client):
    """Test case for customer_find

    
    """
    params = [('find_value', 'find_value_example'),
                    ('find_where', 'email'),
                    ('find_params', 'whole_words'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/customer.find.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_group_add(client):
    """Test case for customer_group_add

    
    """
    params = [('name', 'name_example'),
                    ('store_id', 'store_id_example'),
                    ('stores_ids', 'stores_ids_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/customer.group.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_group_list(client):
    """Test case for customer_group_list

    
    """
    params = [('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('group_ids', 'group_ids_example'),
                    ('params', 'id,name,additional_fields'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/customer.group.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_info(client):
    """Test case for customer_info

    
    """
    params = [('id', 'id_example'),
                    ('params', 'id,email,first_name,last_name'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/customer.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_list(client):
    """Test case for customer_list

    
    """
    params = [('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('params', 'id,email,first_name,last_name'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('group_id', 'group_id_example'),
                    ('store_id', 'store_id_example'),
                    ('customer_list_id', 'customer_list_id_example'),
                    ('avail', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/customer.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_update(client):
    """Test case for customer_update

    
    """
    body = {"address":[{"address_book_company":"address_book_company","address_book_state":"address_book_state","address_book_phone_mobile":"address_book_phone_mobile","address_book_city":"address_book_city","address_book_postcode":"address_book_postcode","address_book_first_name":"address_book_first_name","address_book_address2":"address_book_address2","address_book_address1":"address_book_address1","address_book_country":"address_book_country","address_book_last_name":"address_book_last_name","address_book_tax_id":"address_book_tax_id","address_book_phone":"address_book_phone","address_book_default":True,"address_book_id":"address_book_id","address_book_identification_number":"address_book_identification_number","address_book_type":"address_book_type","address_book_fax":"address_book_fax"},{"address_book_company":"address_book_company","address_book_state":"address_book_state","address_book_phone_mobile":"address_book_phone_mobile","address_book_city":"address_book_city","address_book_postcode":"address_book_postcode","address_book_first_name":"address_book_first_name","address_book_address2":"address_book_address2","address_book_address1":"address_book_address1","address_book_country":"address_book_country","address_book_last_name":"address_book_last_name","address_book_tax_id":"address_book_tax_id","address_book_phone":"address_book_phone","address_book_default":True,"address_book_id":"address_book_id","address_book_identification_number":"address_book_identification_number","address_book_type":"address_book_type","address_book_fax":"address_book_fax"}],"group_id":"group_id","phone":"phone","group_ids":"group_ids","last_name":"last_name","id":"id","news_letter_subscription":True,"first_name":"first_name","email":"email","tags":"tags"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/customer.update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_wishlist_list(client):
    """Test case for customer_wishlist_list

    
    """
    params = [('customer_id', 'customer_id_example'),
                    ('id', 'id_example'),
                    ('store_id', 'store_id_example'),
                    ('start', 0),
                    ('count', 10),
                    ('page_cursor', 'page_cursor_example'),
                    ('response_fields', '{return_code,return_message,pagination,result}')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/customer.wishlist.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

