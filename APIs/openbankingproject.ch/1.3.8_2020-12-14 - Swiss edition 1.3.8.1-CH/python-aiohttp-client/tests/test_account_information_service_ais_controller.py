# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_list import AccountList
from openapi_server.models.authorisations import Authorisations
from openapi_server.models.consent_information_response200_json import ConsentInformationResponse200Json
from openapi_server.models.consent_status_response200 import ConsentStatusResponse200
from openapi_server.models.consents import Consents
from openapi_server.models.consents_response201 import ConsentsResponse201
from openapi_server.models.error400_ais import Error400AIS
from openapi_server.models.error400_ngais import Error400NGAIS
from openapi_server.models.error401_ais import Error401AIS
from openapi_server.models.error401_ngais import Error401NGAIS
from openapi_server.models.error403_ais import Error403AIS
from openapi_server.models.error403_ngais import Error403NGAIS
from openapi_server.models.error404_ais import Error404AIS
from openapi_server.models.error404_ngais import Error404NGAIS
from openapi_server.models.error405_ais import Error405AIS
from openapi_server.models.error405_ngais import Error405NGAIS
from openapi_server.models.error406_ais import Error406AIS
from openapi_server.models.error406_ngais import Error406NGAIS
from openapi_server.models.error409_ais import Error409AIS
from openapi_server.models.error409_ngais import Error409NGAIS
from openapi_server.models.error429_ais import Error429AIS
from openapi_server.models.error429_ngais import Error429NGAIS
from openapi_server.models.get_transaction_details200_response import GetTransactionDetails200Response
from openapi_server.models.get_transaction_list200_response import GetTransactionList200Response
from openapi_server.models.get_transaction_list200_response1 import GetTransactionList200Response1
from openapi_server.models.read_account_balance_response200 import ReadAccountBalanceResponse200
from openapi_server.models.read_account_details200_response import ReadAccountDetails200Response
from openapi_server.models.sca_status_response import ScaStatusResponse
from openapi_server.models.start_consent_authorisation_request import StartConsentAuthorisationRequest
from openapi_server.models.start_scaprocess_response import StartScaprocessResponse
from openapi_server.models.transactions_response200_json import TransactionsResponse200Json
from openapi_server.models.update_consents_psu_data200_response import UpdateConsentsPsuData200Response
from openapi_server.models.update_consents_psu_data_request import UpdateConsentsPsuDataRequest


pytestmark = pytest.mark.asyncio

async def test_create_consent(client):
    """Test case for create_consent

    Create consent
    """
    body = openapi_server.Consents()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_id': 'PSU-1234',
        'psu_id_type': 'psu_id_type_example',
        'psu_corporate_id': 'psu_corporate_id_example',
        'psu_corporate_id_type': 'psu_corporate_id_type_example',
        'tpp_redirect_preferred': True,
        'tpp_redirect_uri': 'tpp_redirect_uri_example',
        'tpp_nok_redirect_uri': 'tpp_nok_redirect_uri_example',
        'tpp_explicit_authorisation_preferred': True,
        'tpp_brand_logging_information': 'tpp_brand_logging_information_example',
        'tpp_notification_uri': 'tpp_notification_uri_example',
        'tpp_notification_content_preferred': 'tpp_notification_content_preferred_example',
        'psu_ip_port': '1234',
        'psu_ip_address': '192.168.8.78',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/consents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_consent(client):
    """Test case for delete_consent

    Delete Consent
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/consents/{consent_id}'.format(consent_id='consent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_list(client):
    """Test case for get_account_list

    Read account list
    """
    params = [('withBalance', True)]
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'consent_id': 'consent_id_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_balances(client):
    """Test case for get_balances

    Read balance
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'consent_id': 'consent_id_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/balances'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_consent_authorisation(client):
    """Test case for get_consent_authorisation

    Get consent authorisation sub-resources request
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/consents/{consent_id}/authorisations'.format(consent_id='consent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_consent_information(client):
    """Test case for get_consent_information

    Get consent request
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/consents/{consent_id}'.format(consent_id='consent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_consent_sca_status(client):
    """Test case for get_consent_sca_status

    Read the SCA status of the consent authorisation
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/consents/{consent_id}/authorisations/{authorisation_id}'.format(consent_id='consent_id_example', authorisation_id='authorisation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_consent_status(client):
    """Test case for get_consent_status

    Consent status request
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/consents/{consent_id}/status'.format(consent_id='consent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_details(client):
    """Test case for get_transaction_details

    Read transaction details
    """
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'consent_id': 'consent_id_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/transactions/{transaction_id}'.format(account_id='account_id_example', transaction_id='transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_list(client):
    """Test case for get_transaction_list

    Read transaction list of an account
    """
    params = [('dateFrom', '2013-10-20'),
                    ('dateTo', '2013-10-20'),
                    ('entryReferenceFrom', 'entry_reference_from_example'),
                    ('bookingStatus', 'booking_status_example'),
                    ('deltaList', True),
                    ('withBalance', True)]
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'consent_id': 'consent_id_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/transactions'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_account_details(client):
    """Test case for read_account_details

    Read account details
    """
    params = [('withBalance', True)]
    headers = { 
        'Accept': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'consent_id': 'consent_id_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_consent_authorisation(client):
    """Test case for start_consent_authorisation

    Start the authorisation process for a consent
    """
    body = openapi_server.StartConsentAuthorisationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_id': 'PSU-1234',
        'psu_id_type': 'psu_id_type_example',
        'psu_corporate_id': 'psu_corporate_id_example',
        'psu_corporate_id_type': 'psu_corporate_id_type_example',
        'tpp_redirect_preferred': True,
        'tpp_redirect_uri': 'tpp_redirect_uri_example',
        'tpp_nok_redirect_uri': 'tpp_nok_redirect_uri_example',
        'tpp_notification_uri': 'tpp_notification_uri_example',
        'tpp_notification_content_preferred': 'tpp_notification_content_preferred_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/consents/{consent_id}/authorisations'.format(consent_id='consent_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_consents_psu_data(client):
    """Test case for update_consents_psu_data

    Update PSU Data for consents
    """
    body = openapi_server.UpdateConsentsPsuDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'psu_id': 'PSU-1234',
        'psu_id_type': 'psu_id_type_example',
        'psu_corporate_id': 'psu_corporate_id_example',
        'psu_corporate_id_type': 'psu_corporate_id_type_example',
        'psu_ip_address': '192.168.8.78',
        'psu_ip_port': '1234',
        'psu_accept': 'psu_accept_example',
        'psu_accept_charset': 'psu_accept_charset_example',
        'psu_accept_encoding': 'psu_accept_encoding_example',
        'psu_accept_language': 'psu_accept_language_example',
        'psu_user_agent': 'psu_user_agent_example',
        'psu_http_method': 'psu_http_method_example',
        'psu_device_id': '99435c7e-ad88-49ec-a2ad-99ddcb1f5555',
        'psu_geo_location': 'GEO:52.506931;13.144558',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/consents/{consent_id}/authorisations/{authorisation_id}'.format(consent_id='consent_id_example', authorisation_id='authorisation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

