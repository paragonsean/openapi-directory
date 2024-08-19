# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ardef_request import ArdefRequest
from openapi_server.models.ardef_response import ArdefResponse
from openapi_server.models.pg_api_bad_response import PGApiBadResponse
from openapi_server.models.pg_api_batch_close_request import PGApiBatchCloseRequest
from openapi_server.models.pg_api_batch_close_response import PGApiBatchCloseResponse
from openapi_server.models.pg_api_capture_request import PGApiCaptureRequest
from openapi_server.models.pg_api_capture_response import PGApiCaptureResponse
from openapi_server.models.pg_api_decline_response import PGApiDeclineResponse
from openapi_server.models.pg_api_email_receipt_request import PGApiEmailReceiptRequest
from openapi_server.models.pg_api_email_receipt_response import PGApiEmailReceiptResponse
from openapi_server.models.pg_api_expire_token_request import PGApiExpireTokenRequest
from openapi_server.models.pg_api_expire_token_response import PGApiExpireTokenResponse
from openapi_server.models.pg_api_internal_error_response import PGApiInternalErrorResponse
from openapi_server.models.pg_api_recharge_request import PGApiRechargeRequest
from openapi_server.models.pg_api_recharge_response import PGApiRechargeResponse
from openapi_server.models.pg_api_refund_request import PGApiRefundRequest
from openapi_server.models.pg_api_refund_response import PGApiRefundResponse
from openapi_server.models.pg_api_response import PGApiResponse
from openapi_server.models.pg_api_timeout_response import PGApiTimeoutResponse
from openapi_server.models.pg_api_tokenize_request import PGApiTokenizeRequest
from openapi_server.models.pg_api_tokenize_response import PGApiTokenizeResponse
from openapi_server.models.pg_api_transaction_request import PGApiTransactionRequest
from openapi_server.models.pg_api_transaction_response import PGApiTransactionResponse
from openapi_server.models.pg_api_unauth_response import PGApiUnauthResponse
from openapi_server.models.pg_api_verify_request import PGApiVerifyRequest
from openapi_server.models.pg_api_verify_response import PGApiVerifyResponse
from openapi_server.models.pg_api_void_request import PGApiVoidRequest
from openapi_server.models.pg_api_void_response import PGApiVoidResponse


pytestmark = pytest.mark.asyncio

async def test_authorization(client):
    """Test case for authorization

    Authorize Transaction
    """
    body = {"fbo_id":999000000001,"cvv2":"152","amt_convenience_fee":2.0,"line_items":"[{\"quantity\": \"1\",\"description\": \"Traffic Cones\", \"unit_of_measure\": \"each\", \"product_code\": \"SKU-123\", \"debit_credit_ind\": \"D\", \"unit_cost\": \"14.99\"},{\"quantity\": \"3\", \"description\": \"Spray Paint\", \"unit_of_measure\": \"EA\", \"product_code\": \"SKU-456\", \"debit_credit_ind\": \"D\", \"unit_cost\": \"5.00\"}]","tokenize":True,"subscription_id":1234,"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","xid_3ds":"ASNFZ4kBI0VniQEjRWeJASNFZ4k=","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","payload_apple_pay":"xxxxxxx","email_receipt":True,"client_ip":"10.1.1.4","customer_code":"PO # abc123","developer_id":"QualpayV1.2","retry_id":1234,"amt_tran_fee":2.35,"card_number":"4111111111111111","purchase_id":"55-1212","mc_ucaf_data":"ASNFZ4nwEjRWeI8BI0VnifASNFZ4jwHyL0U=","dba_name":"SHOE CO","cardholder_name":"JOHN CUSTOMER","card_id":"86e1b00d9b0811e68df3069d8f743581","auth_code":"620376","mc_ucaf_ind":"2","user_id":6,"cavv_3ds":"ASNFZ4kBI0VniQEjRWeJASNFZ4k=","profile_id":"21200001000300000978","customer_email":"testme@qualpay.com","vendor_id":212100026512,"payload_google_pay":"xxxxxxx","pg_id":"d24ac6189b0b11e6966ca68d5edbef41","duplicate_seconds":300,"tr_number":"011111111","emv_tran_id":"ASNFZ4nwEjR1We3I85BI70V9nifASNFZ4jwHyL0U=","partial_auth":True,"tran_currency":840,"merchant_id":0,"moto_ecomm_ind":"1","avs_zip":"94402","exp_date":"0921","retry_attempt":1,"dda_number":"3456776866","type_id":"S","session_id":"session_id","loc_id":"0001","dba_suffix":"END PROMO","amt_fbo":1.5,"email_address":["jdoe@qualpay.com","john.doe@qualpay.com"],"avs_address":"123 Main St","amt_tax":93.5,"card_swipe":";4111111111111111=08051010912345678901?8","customer_id":"JOECUSTOMER_12","amt_tran":1193.5,"customer":{"customer_first_name":"Joe","billing_country":"USA","customer_phone":"6503885200","shipping_addresses":[{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"},{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"}],"billing_addr2":"Suite #1234","billing_addr1":"123 Main Street","billing_city":"San Mateo","billing_country_code":"840","customer_last_name":"Smith","billing_state":"CA","customer_email":"jsmith@somewhere.com","billing_zip":"94402","customer_firm_name":"Qualpay","billing_zip4":"1234"},"merch_ref_num":"ITEM 16126 Purchased 12-15-2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/auth',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_close(client):
    """Test case for batch_close

    Close Batch
    """
    body = {"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","user_id":6,"profile_id":"21200001000300000978","tran_currency":840,"session_id":"session_id","merchant_id":0,"retry_attempt":1,"loc_id":"0001","developer_id":"QualpayV1.2","retry_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/batchClose',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capture(client):
    """Test case for capture

    Capture an Authorized Transaction
    """
    body = {"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","user_id":6,"profile_id":"21200001000300000978","vendor_id":212100026512,"session_id":"session_id","merchant_id":0,"retry_attempt":1,"loc_id":"0001","amt_tran":1193.5,"developer_id":"QualpayV1.2","retry_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/capture/{pg_id_orig}'.format(pg_id_orig='pg_id_orig_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credit(client):
    """Test case for credit

    Issue Credit to Cardholder
    """
    body = {"fbo_id":999000000001,"cvv2":"152","amt_convenience_fee":2.0,"line_items":"[{\"quantity\": \"1\",\"description\": \"Traffic Cones\", \"unit_of_measure\": \"each\", \"product_code\": \"SKU-123\", \"debit_credit_ind\": \"D\", \"unit_cost\": \"14.99\"},{\"quantity\": \"3\", \"description\": \"Spray Paint\", \"unit_of_measure\": \"EA\", \"product_code\": \"SKU-456\", \"debit_credit_ind\": \"D\", \"unit_cost\": \"5.00\"}]","tokenize":True,"subscription_id":1234,"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","xid_3ds":"ASNFZ4kBI0VniQEjRWeJASNFZ4k=","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","payload_apple_pay":"xxxxxxx","email_receipt":True,"client_ip":"10.1.1.4","customer_code":"PO # abc123","developer_id":"QualpayV1.2","retry_id":1234,"amt_tran_fee":2.35,"card_number":"4111111111111111","purchase_id":"55-1212","mc_ucaf_data":"ASNFZ4nwEjRWeI8BI0VnifASNFZ4jwHyL0U=","dba_name":"SHOE CO","cardholder_name":"JOHN CUSTOMER","card_id":"86e1b00d9b0811e68df3069d8f743581","auth_code":"620376","mc_ucaf_ind":"2","user_id":6,"cavv_3ds":"ASNFZ4kBI0VniQEjRWeJASNFZ4k=","profile_id":"21200001000300000978","customer_email":"testme@qualpay.com","vendor_id":212100026512,"payload_google_pay":"xxxxxxx","pg_id":"d24ac6189b0b11e6966ca68d5edbef41","duplicate_seconds":300,"tr_number":"011111111","emv_tran_id":"ASNFZ4nwEjR1We3I85BI70V9nifASNFZ4jwHyL0U=","partial_auth":True,"tran_currency":840,"merchant_id":0,"moto_ecomm_ind":"1","avs_zip":"94402","exp_date":"0921","retry_attempt":1,"dda_number":"3456776866","type_id":"S","session_id":"session_id","loc_id":"0001","dba_suffix":"END PROMO","amt_fbo":1.5,"email_address":["jdoe@qualpay.com","john.doe@qualpay.com"],"avs_address":"123 Main St","amt_tax":93.5,"card_swipe":";4111111111111111=08051010912345678901?8","customer_id":"JOECUSTOMER_12","amt_tran":1193.5,"customer":{"customer_first_name":"Joe","billing_country":"USA","customer_phone":"6503885200","shipping_addresses":[{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"},{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"}],"billing_addr2":"Suite #1234","billing_addr1":"123 Main Street","billing_city":"San Mateo","billing_country_code":"840","customer_last_name":"Smith","billing_state":"CA","customer_email":"jsmith@somewhere.com","billing_zip":"94402","customer_firm_name":"Qualpay","billing_zip4":"1234"},"merch_ref_num":"ITEM 16126 Purchased 12-15-2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/credit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expire(client):
    """Test case for expire

    Expire Token
    """
    body = {"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","user_id":6,"profile_id":"21200001000300000978","vendor_id":212100026512,"session_id":"session_id","merchant_id":0,"retry_attempt":1,"loc_id":"0001","card_id":"86e1b00d9b0811e68df3069d8f743581","developer_id":"QualpayV1.2","retry_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/expireToken',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_force(client):
    """Test case for force

    Force Transaction Approval
    """
    body = {"fbo_id":999000000001,"cvv2":"152","amt_convenience_fee":2.0,"line_items":"[{\"quantity\": \"1\",\"description\": \"Traffic Cones\", \"unit_of_measure\": \"each\", \"product_code\": \"SKU-123\", \"debit_credit_ind\": \"D\", \"unit_cost\": \"14.99\"},{\"quantity\": \"3\", \"description\": \"Spray Paint\", \"unit_of_measure\": \"EA\", \"product_code\": \"SKU-456\", \"debit_credit_ind\": \"D\", \"unit_cost\": \"5.00\"}]","tokenize":True,"subscription_id":1234,"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","xid_3ds":"ASNFZ4kBI0VniQEjRWeJASNFZ4k=","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","payload_apple_pay":"xxxxxxx","email_receipt":True,"client_ip":"10.1.1.4","customer_code":"PO # abc123","developer_id":"QualpayV1.2","retry_id":1234,"amt_tran_fee":2.35,"card_number":"4111111111111111","purchase_id":"55-1212","mc_ucaf_data":"ASNFZ4nwEjRWeI8BI0VnifASNFZ4jwHyL0U=","dba_name":"SHOE CO","cardholder_name":"JOHN CUSTOMER","card_id":"86e1b00d9b0811e68df3069d8f743581","auth_code":"620376","mc_ucaf_ind":"2","user_id":6,"cavv_3ds":"ASNFZ4kBI0VniQEjRWeJASNFZ4k=","profile_id":"21200001000300000978","customer_email":"testme@qualpay.com","vendor_id":212100026512,"payload_google_pay":"xxxxxxx","pg_id":"d24ac6189b0b11e6966ca68d5edbef41","duplicate_seconds":300,"tr_number":"011111111","emv_tran_id":"ASNFZ4nwEjR1We3I85BI70V9nifASNFZ4jwHyL0U=","partial_auth":True,"tran_currency":840,"merchant_id":0,"moto_ecomm_ind":"1","avs_zip":"94402","exp_date":"0921","retry_attempt":1,"dda_number":"3456776866","type_id":"S","session_id":"session_id","loc_id":"0001","dba_suffix":"END PROMO","amt_fbo":1.5,"email_address":["jdoe@qualpay.com","john.doe@qualpay.com"],"avs_address":"123 Main St","amt_tax":93.5,"card_swipe":";4111111111111111=08051010912345678901?8","customer_id":"JOECUSTOMER_12","amt_tran":1193.5,"customer":{"customer_first_name":"Joe","billing_country":"USA","customer_phone":"6503885200","shipping_addresses":[{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"},{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"}],"billing_addr2":"Suite #1234","billing_addr1":"123 Main Street","billing_city":"San Mateo","billing_country_code":"840","customer_last_name":"Smith","billing_state":"CA","customer_email":"jsmith@somewhere.com","billing_zip":"94402","customer_firm_name":"Qualpay","billing_zip4":"1234"},"merch_ref_num":"ITEM 16126 Purchased 12-15-2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/force',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_card_type_information(client):
    """Test case for get_card_type_information

    Get Card type Information for Visa, Mastercard, and Discover
    """
    body = {"card_number":"4111111111111111","merchant_id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/ardef',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recharge(client):
    """Test case for recharge

    Recharge Previously Settled Transaction
    """
    body = {"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","user_id":6,"profile_id":"21200001000300000978","session_id":"session_id","merchant_id":0,"retry_attempt":1,"loc_id":"0001","amt_tran":1139.5,"developer_id":"QualpayV1.2","retry_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/recharge/{pg_id_orig}'.format(pg_id_orig='pg_id_orig_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refund(client):
    """Test case for refund

    Refund Previously Captured Transaction
    """
    body = {"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","user_id":6,"profile_id":"21200001000300000978","vendor_id":212100026512,"session_id":"session_id","merchant_id":0,"retry_attempt":1,"loc_id":"0001","amt_tran":1193.5,"developer_id":"QualpayV1.2","retry_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/refund/{pg_id_orig}'.format(pg_id_orig='pg_id_orig_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sale(client):
    """Test case for sale

    Sale (Auth + Capture)
    """
    body = {"fbo_id":999000000001,"cvv2":"152","amt_convenience_fee":2.0,"line_items":"[{\"quantity\": \"1\",\"description\": \"Traffic Cones\", \"unit_of_measure\": \"each\", \"product_code\": \"SKU-123\", \"debit_credit_ind\": \"D\", \"unit_cost\": \"14.99\"},{\"quantity\": \"3\", \"description\": \"Spray Paint\", \"unit_of_measure\": \"EA\", \"product_code\": \"SKU-456\", \"debit_credit_ind\": \"D\", \"unit_cost\": \"5.00\"}]","tokenize":True,"subscription_id":1234,"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","xid_3ds":"ASNFZ4kBI0VniQEjRWeJASNFZ4k=","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","payload_apple_pay":"xxxxxxx","email_receipt":True,"client_ip":"10.1.1.4","customer_code":"PO # abc123","developer_id":"QualpayV1.2","retry_id":1234,"amt_tran_fee":2.35,"card_number":"4111111111111111","purchase_id":"55-1212","mc_ucaf_data":"ASNFZ4nwEjRWeI8BI0VnifASNFZ4jwHyL0U=","dba_name":"SHOE CO","cardholder_name":"JOHN CUSTOMER","card_id":"86e1b00d9b0811e68df3069d8f743581","auth_code":"620376","mc_ucaf_ind":"2","user_id":6,"cavv_3ds":"ASNFZ4kBI0VniQEjRWeJASNFZ4k=","profile_id":"21200001000300000978","customer_email":"testme@qualpay.com","vendor_id":212100026512,"payload_google_pay":"xxxxxxx","pg_id":"d24ac6189b0b11e6966ca68d5edbef41","duplicate_seconds":300,"tr_number":"011111111","emv_tran_id":"ASNFZ4nwEjR1We3I85BI70V9nifASNFZ4jwHyL0U=","partial_auth":True,"tran_currency":840,"merchant_id":0,"moto_ecomm_ind":"1","avs_zip":"94402","exp_date":"0921","retry_attempt":1,"dda_number":"3456776866","type_id":"S","session_id":"session_id","loc_id":"0001","dba_suffix":"END PROMO","amt_fbo":1.5,"email_address":["jdoe@qualpay.com","john.doe@qualpay.com"],"avs_address":"123 Main St","amt_tax":93.5,"card_swipe":";4111111111111111=08051010912345678901?8","customer_id":"JOECUSTOMER_12","amt_tran":1193.5,"customer":{"customer_first_name":"Joe","billing_country":"USA","customer_phone":"6503885200","shipping_addresses":[{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"},{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"}],"billing_addr2":"Suite #1234","billing_addr1":"123 Main Street","billing_city":"San Mateo","billing_country_code":"840","customer_last_name":"Smith","billing_state":"CA","customer_email":"jsmith@somewhere.com","billing_zip":"94402","customer_firm_name":"Qualpay","billing_zip4":"1234"},"merch_ref_num":"ITEM 16126 Purchased 12-15-2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/sale',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_receipt(client):
    """Test case for send_receipt

    Send Transaction Receipt Email
    """
    body = {"email_address":["jdoe@qualpay.com","john.doe@qualpay.com"],"logo_url":"https://app.qualpay.com/shared/images/qp-icon.png","vendor_id":212100026512,"merchant_id":0,"developer_id":"QualpayV1.2"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/emailReceipt/{pg_id}'.format(pg_id='pg_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokenize(client):
    """Test case for tokenize

    Tokenize Card
    """
    body = {"cvv2":"152","merchant_id":0,"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","payload_apple_pay":"xxxxxxx","avs_zip":"94402","client_ip":"10.1.1.4","exp_date":"0921","retry_attempt":1,"developer_id":"QualpayV1.2","retry_id":1234,"dda_number":"3456776866","card_number":"4111111111111111","type_id":"S","session_id":"session_id","single_use":True,"cardholder_name":"JOHN CUSTOMER","loc_id":"0001","card_id":"86e1b00d9b0811e68df3069d8f743581","email_address":["jdoe@qualpay.com","john.doe@qualpay.com"],"avs_address":"123 Main St","user_id":6,"profile_id":"21200001000300000978","vendor_id":212100026512,"card_swipe":";4111111111111111=08051010912345678901?8","payload_google_pay":"xxxxxxx","tr_number":"011111111"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/tokenize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify(client):
    """Test case for verify

    Verify Card
    """
    body = {"cvv2":"152","merchant_id":0,"tokenize":True,"moto_ecomm_ind":"1","report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","payload_apple_pay":"xxxxxxx","avs_zip":"94402","client_ip":"10.1.1.4","exp_date":"0921","retry_attempt":1,"customer_code":"PO # abc123","developer_id":"QualpayV1.2","retry_id":1234,"dda_number":"3456776866","card_number":"4111111111111111","type_id":"S","session_id":"session_id","cardholder_name":"JOHN CUSTOMER","loc_id":"0001","card_id":"86e1b00d9b0811e68df3069d8f743581","email_address":["jdoe@qualpay.com","john.doe@qualpay.com"],"avs_address":"123 Main St","user_id":6,"profile_id":"21200001000300000978","card_swipe":";4111111111111111=08051010912345678901?8","payload_google_pay":"xxxxxxx","tr_number":"011111111","customer":{"customer_first_name":"Joe","billing_country":"USA","customer_phone":"6503885200","shipping_addresses":[{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"},{"shipping_addr1":"1234 Main Street","shipping_zip4":"1234","shipping_state":"CA","shipping_zip":"94402","shipping_first_name":"Joe","shipping_city":"San Mateo","shipping_last_name":"Smith","shipping_firm_name":"Qualpay","shipping_country":"USA","shipping_country_code":"840","primary":True,"shipping_addr2":"Ste 123"}],"billing_addr2":"Suite #1234","billing_addr1":"123 Main Street","billing_city":"San Mateo","billing_country_code":"840","customer_last_name":"Smith","billing_state":"CA","customer_email":"jsmith@somewhere.com","billing_zip":"94402","customer_firm_name":"Qualpay","billing_zip4":"1234"},"merch_ref_num":"ITEM 16126 Purchased 12-15-2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/verify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_void(client):
    """Test case for void

    Void a Previously Authorized Transaction
    """
    body = {"report_data":"[ {\"shipping address\" : \"123 Main St.\"},{\"shipping city, state zip\" : \"San Mateo, CA 94402\"} ]","echo_fields":"[ {\"product\" : \"lawnmower\"},{\"purchase\" : \"1 yr maintenance\"} ]","user_id":6,"profile_id":"21200001000300000978","vendor_id":212100026512,"session_id":"session_id","merchant_id":0,"retry_attempt":1,"loc_id":"0001","developer_id":"QualpayV1.2","retry_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/pg/void/{pg_id_orig}'.format(pg_id_orig='pg_id_orig_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

