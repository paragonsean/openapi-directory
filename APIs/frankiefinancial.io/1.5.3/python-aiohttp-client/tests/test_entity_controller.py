# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accepted_entity_result_object import AcceptedEntityResultObject
from openapi_server.models.basic_status_result_object import BasicStatusResultObject
from openapi_server.models.check_entity_check_result_object import CheckEntityCheckResultObject
from openapi_server.models.check_result_update_object import CheckResultUpdateObject
from openapi_server.models.entity_check_details_object import EntityCheckDetailsObject
from openapi_server.models.entity_idv_details_object import EntityIDVDetailsObject
from openapi_server.models.entity_idv_result_object import EntityIDVResultObject
from openapi_server.models.entity_object import EntityObject
from openapi_server.models.entity_result_object import EntityResultObject
from openapi_server.models.entity_search_result_object import EntitySearchResultObject
from openapi_server.models.error_object import ErrorObject


pytestmark = pytest.mark.asyncio

async def test_create_check_entity(client):
    """Test case for create_check_entity

    Create and Verify Entity
    """
    entity_details = {"deviceCheckDetails":[{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"},{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"}],"entity":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
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
        path='/compliance/v1.2/entity/new/verify/{check_type}/{result_level}'.format(check_type='default', result_level='result_level_example'),
        headers=headers,
        json=entity_details,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_check_entity_push_to_mobile(client):
    """Test case for create_check_entity_push_to_mobile

    Create Entity and Push Self-Verification Link
    """
    entity_details = {"deviceCheckDetails":[{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"},{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"}],"entity":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
    params = [('nopush', True)]
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
        path='/compliance/v1.2/entity/new/verify/pushToMobile',
        headers=headers,
        json=entity_details,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_entity(client):
    """Test case for create_entity

    Create New Entity.
    """
    entity = {"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity',
        headers=headers,
        json=entity,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_entity_get_idv_token(client):
    """Test case for create_entity_get_idv_token

    Create Entity and Get IDV Token
    """
    entity_idv_details = {"referrer":"referrer","applicantId":"applicantId","applicationId":"applicationId","entity":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/new/idvalidate/getToken',
        headers=headers,
        json=entity_idv_details,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_entity(client):
    """Test case for delete_entity

    Delete Entity
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
        path='/compliance/v1.2/entity/{entity_id}'.format(entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_entity(client):
    """Test case for query_entity

    Retrieve Entity Details
    """
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/compliance/v1.2/entity/{entity_id}'.format(entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_entity_checks(client):
    """Test case for query_entity_checks

    Retrieve Entity Verication Check Details 
    """
    params = [('alldata', True)]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/compliance/v1.2/entity/{entity_id}/checks'.format(entity_id='entity_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_entity_full(client):
    """Test case for query_entity_full

    Retrieve Entity Details and Document Scan Data 
    """
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/compliance/v1.2/entity/{entity_id}/full'.format(entity_id='entity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_entity(client):
    """Test case for search_entity

    Search for Entity
    """
    search_entity = {"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/search',
        headers=headers,
        json=search_entity,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_check_class_result(client):
    """Test case for update_check_class_result

    Update Check Result State
    """
    params = [('status', 'status_example'),
                    ('undo', True)]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/check/{check_id}/{check_class}/{check_class_id}'.format(entity_id='entity_id_example', check_id='check_id_example', check_class='check_class_example', check_class_id='check_class_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_check_class_results(client):
    """Test case for update_check_class_results

    Update Check Result States (Batch)
    """
    check_result_update = {"checkClassIds":["checkClassIds","checkClassIds"],"comment":"comment","status":"UNKNOWN"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/check/{check_id}/{check_class}'.format(entity_id='entity_id_example', check_id='check_id_example', check_class='check_class_example'),
        headers=headers,
        json=check_result_update,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_check_entity(client):
    """Test case for update_check_entity

    Update Entity and Verify Details
    """
    entity_details = {"deviceCheckDetails":[{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"},{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"}],"entity":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
    params = [('force', True),
                    ('noInvalidate', True)]
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
        path='/compliance/v1.2/entity/{entity_id}/verify/{check_type}/{result_level}'.format(entity_id='entity_id_example', check_type='default', result_level='result_level_example'),
        headers=headers,
        json=entity_details,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_check_entity_push_to_mobile(client):
    """Test case for update_check_entity_push_to_mobile

    Update Entity and Push Self-Verification Link
    """
    entity_details = {"deviceCheckDetails":[{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"},{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"}],"entity":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
    params = [('nopush', True),
                    ('phase', 56)]
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
        path='/compliance/v1.2/entity/{entity_id}/verify/pushToMobile'.format(entity_id='entity_id_example'),
        headers=headers,
        json=entity_details,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_entity(client):
    """Test case for update_entity

    Update Existing Entity.
    """
    entity = {"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}
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
        path='/compliance/v1.2/entity/{entity_id}'.format(entity_id='entity_id_example'),
        headers=headers,
        json=entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_entity_get_idv_token(client):
    """Test case for update_entity_get_idv_token

    Update Entity and Get IDV Token
    """
    entity_idv_details = {"referrer":"referrer","applicantId":"applicantId","applicationId":"applicationId","entity":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/idvalidate/getToken'.format(entity_id='entity_id_example'),
        headers=headers,
        json=entity_idv_details,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_entity_init_idv_process(client):
    """Test case for update_entity_init_idv_process

    Update Entity and Initiate IDV Process
    """
    entity_details = {"deviceCheckDetails":[{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"},{"checkType":"DEVICE","additionalData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"activityType":"SIGNUP","checkSessionKey":"checkSessionKey"}],"entity":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/idvalidate/initProcess'.format(entity_id='entity_id_example'),
        headers=headers,
        json=entity_details,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_entity_state(client):
    """Test case for update_entity_state

    Update Entity States
    """
    params = [('set', 'set_example'),
                    ('risk', 'risk_example'),
                    ('comment', 'comment_example')]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/entity/{entity_id}/status'.format(entity_id='entity_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

