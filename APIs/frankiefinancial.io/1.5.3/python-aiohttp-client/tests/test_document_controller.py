# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accepted_document_result_object import AcceptedDocumentResultObject
from openapi_server.models.basic_status_result_object import BasicStatusResultObject
from openapi_server.models.comparison_set import ComparisonSet
from openapi_server.models.document_checks_result_object import DocumentChecksResultObject
from openapi_server.models.document_compare_result_object import DocumentCompareResultObject
from openapi_server.models.document_result_object import DocumentResultObject
from openapi_server.models.document_scan_result_object import DocumentScanResultObject
from openapi_server.models.document_search_result_object import DocumentSearchResultObject
from openapi_server.models.document_verify import DocumentVerify
from openapi_server.models.document_verify_result_object import DocumentVerifyResultObject
from openapi_server.models.error_object import ErrorObject
from openapi_server.models.identity_document_object import IdentityDocumentObject


pytestmark = pytest.mark.asyncio

async def test_compare_document(client):
    """Test case for compare_document

    Create Document and Compare to Original.
    """
    comparison_set = {"compareDocument":{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},"toDocument":{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}}
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
        path='/compliance/v1.2/document/new/compare',
        headers=headers,
        json=comparison_set,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_document(client):
    """Test case for create_document

    Create New Document.
    """
    document = {"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/document',
        headers=headers,
        json=document,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_scan_document(client):
    """Test case for create_scan_document

    Create and OCR Scan Document.
    """
    document = {"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}
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
        path='/compliance/v1.2/document/new/scan',
        headers=headers,
        json=document,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_document(client):
    """Test case for delete_document

    Delete Document.
    """
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'x_frankie_background': 56,
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/compliance/v1.2/document/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_document(client):
    """Test case for query_document

    Retrieve Document Details
    """
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/compliance/v1.2/document/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_document_checks(client):
    """Test case for query_document_checks

    Retrieve Document Verification Check Details. 
    """
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'x_frankie_background': 56,
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/compliance/v1.2/document/{document_id}/checks'.format(document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_document_full(client):
    """Test case for query_document_full

    Retrieve Document and Scan Data
    """
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/compliance/v1.2/document/{document_id}/full'.format(document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_document(client):
    """Test case for search_document

    Search For a Document !! EXPERIMENTAL !!
    """
    search_document = {"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/document/search',
        headers=headers,
        json=search_document,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_compare_document(client):
    """Test case for update_compare_document

    Update Document and Compare to Original.
    """
    comparison_set = {"compareDocument":{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},"toDocument":{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}}
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
        path='/compliance/v1.2/document/{document_id}/compare'.format(document_id='document_id_example'),
        headers=headers,
        json=comparison_set,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_document(client):
    """Test case for update_document

    Update Existing Document.
    """
    document = {"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}
    params = [('noInvalidate', True)]
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
        path='/compliance/v1.2/document/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        json=document,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_scan_document(client):
    """Test case for update_scan_document

    Update and OCR Scan Document
    """
    document = {"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}
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
        path='/compliance/v1.2/document/{document_id}/scan'.format(document_id='document_id_example'),
        headers=headers,
        json=document,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_verify_document(client):
    """Test case for update_verify_document

    Update and Verify Document.
    """
    process_document = {"document":{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},"entityData":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
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
        path='/compliance/v1.2/document/{document_id}/verify'.format(document_id='document_id_example'),
        headers=headers,
        json=process_document,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_document(client):
    """Test case for verify_document

    Create and Verify Document.
    """
    process_document = {"document":{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},"entityData":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
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
        path='/compliance/v1.2/document/new/verify',
        headers=headers,
        json=process_document,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

