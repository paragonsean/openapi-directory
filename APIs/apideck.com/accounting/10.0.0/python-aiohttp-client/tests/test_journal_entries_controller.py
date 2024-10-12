# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_journal_entry_response import CreateJournalEntryResponse
from openapi_server.models.delete_journal_entry_response import DeleteJournalEntryResponse
from openapi_server.models.get_journal_entries_response import GetJournalEntriesResponse
from openapi_server.models.get_journal_entry_response import GetJournalEntryResponse
from openapi_server.models.journal_entry import JournalEntry
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_journal_entry_response import UpdateJournalEntryResponse


pytestmark = pytest.mark.asyncio

async def test_journal_entries_add(client):
    """Test case for journal_entries_add

    Create Journal Entry
    """
    body = {"created_at":"2020-09-30T07:43:32Z","memo":"Thank you for your business and have a great day!","line_items":[{"tax_amount":27500,"department_id":"12345","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","tracking_category":{"name":"New York","id":"123456"},"type":"debit","location_id":"12345","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"supplier":{"address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"display_id":"SUPP00101","company_name":"The boring company","id":"12345","display_name":"Windsurf Shop"},"sub_total":27500,"id":"12345","customer":{"display_id":"CUST00101","company_name":"The boring company","name":"Windsurf Shop","id":"12345","display_name":"Windsurf Shop"}},{"tax_amount":27500,"department_id":"12345","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","tracking_category":{"name":"New York","id":"123456"},"type":"debit","location_id":"12345","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"supplier":{"address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"display_id":"SUPP00101","company_name":"The boring company","id":"12345","display_name":"Windsurf Shop"},"sub_total":27500,"id":"12345","customer":{"display_id":"CUST00101","company_name":"The boring company","name":"Windsurf Shop","id":"12345","display_name":"Windsurf Shop"}}],"title":"Purchase Invoice-Inventory (USD): 2019/02/01 Batch Summary Entry","created_by":"12345","custom_mappings":"{}","number":"OIT00546","currency_rate":0.69,"journal_symbol":"IND","tax_code":"1234","updated_at":"2020-09-30T07:43:32Z","tax_type":"sales","row_version":"1-12345","updated_by":"12345","currency":"USD","id":"12345","posted_at":"2020-09-30T07:43:32Z"}
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
        path='/accounting/journal-entries',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_journal_entries_all(client):
    """Test case for journal_entries_all

    List Journal Entries
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
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
        path='/accounting/journal-entries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_journal_entries_delete(client):
    """Test case for journal_entries_delete

    Delete Journal Entry
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
        path='/accounting/journal-entries/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_journal_entries_one(client):
    """Test case for journal_entries_one

    Get Journal Entry
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
        path='/accounting/journal-entries/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_journal_entries_update(client):
    """Test case for journal_entries_update

    Update Journal Entry
    """
    body = {"created_at":"2020-09-30T07:43:32Z","memo":"Thank you for your business and have a great day!","line_items":[{"tax_amount":27500,"department_id":"12345","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","tracking_category":{"name":"New York","id":"123456"},"type":"debit","location_id":"12345","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"supplier":{"address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"display_id":"SUPP00101","company_name":"The boring company","id":"12345","display_name":"Windsurf Shop"},"sub_total":27500,"id":"12345","customer":{"display_id":"CUST00101","company_name":"The boring company","name":"Windsurf Shop","id":"12345","display_name":"Windsurf Shop"}},{"tax_amount":27500,"department_id":"12345","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","tracking_category":{"name":"New York","id":"123456"},"type":"debit","location_id":"12345","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"supplier":{"address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"display_id":"SUPP00101","company_name":"The boring company","id":"12345","display_name":"Windsurf Shop"},"sub_total":27500,"id":"12345","customer":{"display_id":"CUST00101","company_name":"The boring company","name":"Windsurf Shop","id":"12345","display_name":"Windsurf Shop"}}],"title":"Purchase Invoice-Inventory (USD): 2019/02/01 Batch Summary Entry","created_by":"12345","custom_mappings":"{}","number":"OIT00546","currency_rate":0.69,"journal_symbol":"IND","tax_code":"1234","updated_at":"2020-09-30T07:43:32Z","tax_type":"sales","row_version":"1-12345","updated_by":"12345","currency":"USD","id":"12345","posted_at":"2020-09-30T07:43:32Z"}
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
        path='/accounting/journal-entries/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

