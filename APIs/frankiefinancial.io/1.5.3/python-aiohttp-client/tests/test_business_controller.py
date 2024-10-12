# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accepted_entity_result_object import AcceptedEntityResultObject
from openapi_server.models.business_report_response_details import BusinessReportResponseDetails
from openapi_server.models.entity_object import EntityObject
from openapi_server.models.error_object import ErrorObject
from openapi_server.models.international_business_profile_criteria import InternationalBusinessProfileCriteria
from openapi_server.models.international_business_profile_response import InternationalBusinessProfileResponse
from openapi_server.models.international_business_search_criteria import InternationalBusinessSearchCriteria
from openapi_server.models.international_business_search_response import InternationalBusinessSearchResponse
from openapi_server.models.organisation_check_response_object import OrganisationCheckResponseObject
from openapi_server.models.ownership_query import OwnershipQuery


pytestmark = pytest.mark.asyncio

async def test_business_ownership_query(client):
    """Test case for business_ownership_query

    Create Business Entity and Query UBO (AUS Only)
    """
    query = {"organisation":{"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}}
    params = [('checkType', ['check_type_example']),
                    ('entityCategories', ['entity_categories_example']),
                    ('resultLevel', summary),
                    ('validation', 'validation_example'),
                    ('generateReport', 'generate_report_example'),
                    ('includeHistorical', True),
                    ('onlyProfile', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/business/ownership/query',
        headers=headers,
        json=query,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_organisation(client):
    """Test case for check_organisation

    Run KYC/AML Checks on Organisation and/or Associated Individuals.
    """
    params = [('checkType', ['check_type_example']),
                    ('entityCategories', ['entity_categories_example']),
                    ('resultLevel', summary),
                    ('generateReport', 'generate_report_example')]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/business/{entity_id}/verify'.format(entity_id='entity_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_international_business_profile(client):
    """Test case for international_business_profile

    Retrieve a business profile from any country (AUS included).
    """
    organisation = {"country":"country","company_code":"company_code"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/business/international/profile',
        headers=headers,
        json=organisation,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_international_business_search(client):
    """Test case for international_business_search

    Search for a business from any country (AUS included).
    """
    organisation = {"country":"country","organisation_number":"organisation_number","organisation_name":"organisation_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/business/international/search',
        headers=headers,
        json=organisation,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_business_reports(client):
    """Test case for run_business_reports

    Run Report(s) against a new or existing organisation entity (AUS Only).
    """
    organisation = {"addresses":[{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"},{"country":"TST","streetType":"Road","town":"Testville","endDate":"2000-01-23","streetNumber":"42a","addressType":"RESIDENTIAL1","postalCode":"123-TST","unitNumber":"Suite 1006","addressId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","buildingName":"Tower of Babel","streetName":"Test Eagle West","careOf":"careOf","longForm":"42a Test Eagle Road, Testville, TST 123-TST, Testalia","suburb":"Testburb","state":"TS","region":"Test County","startDate":"2000-01-23"}],"gender":"F","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"entityType":"INDIVIDUAL","organisationData":{"disclosingEntityIndicator":True,"lastCheckDate":"2000-01-23","includesNonBeneficiallyHeld":True,"kycCustomerType":"kycCustomerType","type":{"code":"code","description":"description"},"registeredName":"registeredName","shareStructure":[{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"},{"amountDue":6.027456183070403,"classCode":"classCode","classTitle":"classTitle","amountPaid":1.4658129805029452,"docNumberQualifier":"docNumberQualifier","docNumber":"docNumber","sharesIssued":5,"status":"status"}],"subclass":{"code":"code","description":"description"},"adverseCreditDataPresent":True,"ownershipResolved":True,"registration":{"date":"2000-01-23","previousNumber":"previousNumber","state":"state"},"class":{"code":"code","description":"description"},"startDate":"2000-01-23","status":{"code":"code","description":"description"}},"entityProfile":"entityProfile","flags":[{"flag":"flag","value":0},{"flag":"flag","value":0}],"name":{"displayName":"Jane Cecily Smith","familyName":"Smith","givenName":"Jane","honourific":"Duchess","middleName":"Cecily"},"dateOfBirth":{"country":"AUS","locality":"Brisbane","dateOfBirth":"1978-11-12","yearOfBirth":"1978"},"entityId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","identityDocs":[{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"},{"idIssued":"1972-11-04","country":"AUS","idType":"DRIVERS_LICENCE","extraData":[{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"},{"kvpKey":"Extra.Information","kvpType":"general.string","kvpValue":"123-456-789A"}],"docScan":[{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"},{"scanCreated":"2000-01-23T04:56:07.000+00:00","scanData":"VGhpcyBpcyBzb21lIGV4YW1wbGUgZGF0YS4gV29vLCBJIGJldCB5b3UgcmVncmV0IHRoZSB0aW1lIHlvdSB3YXN0ZWQgZGVjb2RpbmcgdGhpcywgaHVoPw==","scanDataRetrievalState":"NORMAL","scanDocId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","ScanDelete":True,"scanMIME":"image/png","scanType":"PDF","scanFilename":"Important Document - ID1234567.pdf","scanPageNum":1,"scanSide":"F"}],"manuallyModified":False,"idNumber":"123456789","createdFromScan":True,"idExpiry":"2020-02-01","documentId":"84a9a860-68ae-4d7d-9a53-54a1116d5051","documentStatus":"DOC_SCANNED","region":"VIC","idSubType":"idSubType"}]}
    params = [('reportTypes', 'report_types_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/business/reports',
        headers=headers,
        json=organisation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

