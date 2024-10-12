# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_credit_note_response import CreateCreditNoteResponse
from openapi_server.models.credit_note import CreditNote
from openapi_server.models.delete_credit_note_response import DeleteCreditNoteResponse
from openapi_server.models.get_credit_note_response import GetCreditNoteResponse
from openapi_server.models.get_credit_notes_response import GetCreditNotesResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_credit_note_response import UpdateCreditNoteResponse


pytestmark = pytest.mark.asyncio

async def test_credit_notes_add(client):
    """Test case for credit_notes_add

    Create Credit Note
    """
    body = {"note":"Some notes about this credit note","created_at":"2020-09-30T07:43:32Z","line_items":[{"tax_amount":27500,"item":{"code":"120-C","name":"Model Y","id":"12344"},"code":"120-C","quantity":1,"department_id":"1234","discount_amount":19.99,"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","discount_percentage":0.01,"type":"sales_item","unit_price":27500.5,"created_by":"12345","location_id":"1234","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"line_number":1,"row_version":"1-12345","updated_by":"12345","unit_of_measure":"pc.","id":"12345","row_id":"12345"},{"tax_amount":27500,"item":{"code":"120-C","name":"Model Y","id":"12344"},"code":"120-C","quantity":1,"department_id":"1234","discount_amount":19.99,"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","discount_percentage":0.01,"type":"sales_item","unit_price":27500.5,"created_by":"12345","location_id":"1234","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"line_number":1,"row_version":"1-12345","updated_by":"12345","unit_of_measure":"pc.","id":"12345","row_id":"12345"}],"type":"accounts_receivable_credit","custom_mappings":"{}","reference":"123456","number":"OIT00546","currency_rate":0.69,"remaining_credit":27500,"allocations":[{"amount":49.99,"code":"N091","id":"123456","type":"invoice"},{"amount":49.99,"code":"N091","id":"123456","type":"invoice"}],"balance":27500,"updated_at":"2020-09-30T07:43:32Z","date_paid":"2021-05-01T12:00:00Z","terms":"Some terms about this credit note","currency":"USD","id":"123456","tax_inclusive":True,"total_tax":2500,"created_by":"12345","tax_code":"1234","total_amount":49.99,"date_issued":"2021-05-01T12:00:00Z","row_version":"1-12345","sub_total":27500,"updated_by":"12345","account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"customer":{"display_id":"CUST00101","company_name":"The boring company","name":"Windsurf Shop","id":"12345","display_name":"Windsurf Shop"},"status":"authorised"}
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
        path='/accounting/credit-notes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credit_notes_all(client):
    """Test case for credit_notes_all

    List Credit Notes
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
        path='/accounting/credit-notes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credit_notes_delete(client):
    """Test case for credit_notes_delete

    Delete Credit Note
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
        path='/accounting/credit-notes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credit_notes_one(client):
    """Test case for credit_notes_one

    Get Credit Note
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
        path='/accounting/credit-notes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credit_notes_update(client):
    """Test case for credit_notes_update

    Update Credit Note
    """
    body = {"note":"Some notes about this credit note","created_at":"2020-09-30T07:43:32Z","line_items":[{"tax_amount":27500,"item":{"code":"120-C","name":"Model Y","id":"12344"},"code":"120-C","quantity":1,"department_id":"1234","discount_amount":19.99,"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","discount_percentage":0.01,"type":"sales_item","unit_price":27500.5,"created_by":"12345","location_id":"1234","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"line_number":1,"row_version":"1-12345","updated_by":"12345","unit_of_measure":"pc.","id":"12345","row_id":"12345"},{"tax_amount":27500,"item":{"code":"120-C","name":"Model Y","id":"12344"},"code":"120-C","quantity":1,"department_id":"1234","discount_amount":19.99,"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","discount_percentage":0.01,"type":"sales_item","unit_price":27500.5,"created_by":"12345","location_id":"1234","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"line_number":1,"row_version":"1-12345","updated_by":"12345","unit_of_measure":"pc.","id":"12345","row_id":"12345"}],"type":"accounts_receivable_credit","custom_mappings":"{}","reference":"123456","number":"OIT00546","currency_rate":0.69,"remaining_credit":27500,"allocations":[{"amount":49.99,"code":"N091","id":"123456","type":"invoice"},{"amount":49.99,"code":"N091","id":"123456","type":"invoice"}],"balance":27500,"updated_at":"2020-09-30T07:43:32Z","date_paid":"2021-05-01T12:00:00Z","terms":"Some terms about this credit note","currency":"USD","id":"123456","tax_inclusive":True,"total_tax":2500,"created_by":"12345","tax_code":"1234","total_amount":49.99,"date_issued":"2021-05-01T12:00:00Z","row_version":"1-12345","sub_total":27500,"updated_by":"12345","account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"customer":{"display_id":"CUST00101","company_name":"The boring company","name":"Windsurf Shop","id":"12345","display_name":"Windsurf Shop"},"status":"authorised"}
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
        path='/accounting/credit-notes/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

