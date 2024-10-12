# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accepted_document_result_object import AcceptedDocumentResultObject
from openapi_server.models.document_industry_utility_consent_result_object import DocumentIndustryUtilityConsentResultObject
from openapi_server.models.document_industry_utility_process_result_object import DocumentIndustryUtilityProcessResultObject
from openapi_server.models.document_industry_utility_switch_result_object import DocumentIndustryUtilitySwitchResultObject
from openapi_server.models.eic_request import EICRequest
from openapi_server.models.error_object import ErrorObject
from openapi_server.models.identity_document_object import IdentityDocumentObject
from openapi_server.models.switch_request import SwitchRequest


pytestmark = pytest.mark.asyncio

async def test_create_process_industry_utility_document(client):
    """Test case for create_process_industry_utility_document

    Create Document and Run Utility Price Comparison.
    """
    document = {"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}
    params = [('planLimit', 30)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'x_frankie_background': 56,
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/document/new/utility/process/compare',
        headers=headers,
        json=document,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_process_industry_utility_document(client):
    """Test case for update_process_industry_utility_document

    Update Document and Run Utility Price Comparison.
    """
    document = {"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}
    params = [('planLimit', 30)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'x_frankie_background': 56,
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/document/{document_id}/utility/process/compare'.format(document_id='document_id_example'),
        headers=headers,
        json=document,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_process_industry_utility_document_consent(client):
    """Test case for update_process_industry_utility_document_consent

    Provide Explicit Consent to Switch Utility Plans.
    """
    consent_request = {"correlationId":"d290f1ee-6c54-4b01-90e6-d701748f0851","details":{"vulnerabilities":{"dependencyType":"Life Support"},"concessionCard":{"firstName":"John","lastName":"Doe","customerReferenceNumber":"123456789","endDate":"2000-01-23","concessionEvidenceType":"Health Care Card","concessionType":"NSW Government Life Support Rebate","startDate":"2000-01-23"}},"planId":"123456"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'x_frankie_background': 56,
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/document/{document_id}/utility/process/consent'.format(document_id='document_id_example'),
        headers=headers,
        json=consent_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_process_industry_utility_document_switch(client):
    """Test case for update_process_industry_utility_document_switch

    Initiate Switching of Utility Plan.
    """
    switch_request = {"correlationId":"d290f1ee-6c54-4b01-90e6-d701748f0851","details":{"customerDetails":{"address":"Level 3, 9 Help Street, Chatswood, NSW 2067","evidenceOfIdentity":{"Passport":{"expiryDate":"10/2022","country":"Australia","number":"B765435","type":"passport"},"DriversLicence":{"expiryDate":"10/2022","number":"1234567890","state":"NSW","type":"driverslicence"},"MedicareCard":{"expiryDate":"2022-10","number":"1234567890","referenceNumber":"1","middleName":"middleName","cardColor":"green","type":"medicare"}},"mobile":"+555 13384337","name":{"middle":"Joan","last":"Doe","title":"Miss","first":"Jane"},"dateOfBirth":"22/04/1983","email":"jane.doe@email.com"}},"confirmation":["",""]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'x_frankie_background': 56,
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/document/{document_id}/utility/process/switch'.format(document_id='document_id_example'),
        headers=headers,
        json=switch_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

