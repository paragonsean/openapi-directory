# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.eaadhar_xaml_schema import EaadharXamlSchema
from openapi_server.models.file_upload import FileUpload
from openapi_server.models.file_upload_response import FileUploadResponse
from openapi_server.models.get_e_aadhaar_data_in_xml_format_id401_response import GetEAadhaarDataInXMLFormatId401Response
from openapi_server.models.get_e_aadhaar_data_in_xml_format_id404_response import GetEAadhaarDataInXMLFormatId404Response
from openapi_server.models.get_file_from_uriid400_response import GetFileFromURIId400Response
from openapi_server.models.get_file_from_uriid404_response import GetFileFromURIId404Response
from openapi_server.models.get_file_from_uriid500_response import GetFileFromURIId500Response
from openapi_server.models.get_file_from_uriid503_response import GetFileFromURIId503Response
from openapi_server.models.get_list_of_issued_documents_id200_response import GetListOfIssuedDocumentsId200Response
from openapi_server.models.get_list_of_issued_documents_version1_id500_response import GetListOfIssuedDocumentsVersion1Id500Response
from openapi_server.models.get_list_of_self_uploaded_documents404_response import GetListOfSelfUploadedDocuments404Response
from openapi_server.models.get_list_of_self_uploaded_documents500_response import GetListOfSelfUploadedDocuments500Response
from openapi_server.models.pull_document_id400_response import PullDocumentId400Response
from openapi_server.models.pull_document_id404_response import PullDocumentId404Response
from openapi_server.models.pull_document_id500_response import PullDocumentId500Response
from openapi_server.models.push_urito_account_id500_response import PushURIToAccountId500Response
from openapi_server.models.sample1 import Sample1
from openapi_server.models.sample2 import Sample2
from openapi_server.models.sample3 import Sample3
from openapi_server.models.sample4 import Sample4
from openapi_server.models.upload_file_to_locker_id400_response import UploadFileToLockerId400Response
from openapi_server.models.upload_file_to_locker_id401_response import UploadFileToLockerId401Response
from openapi_server.models.xml_format_schema import XMLFormatSchema


pytestmark = pytest.mark.asyncio

async def test_get_certificate_data_in_xml_format_from_uri_id(client):
    """Test case for get_certificate_data_in_xml_format_from_uri_id

    Get Certificate Data in XML Format from URI
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/1/xml/{uri}'.format(uri='uri_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_e_aadhaar_data_in_xml_format_id(client):
    """Test case for get_e_aadhaar_data_in_xml_format_id

    Get e-Aadhaar Data in XML Format
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/2/xml/eaadhaar',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_from_uri_id(client):
    """Test case for get_file_from_uri_id

    Get File from URI
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/1/file/{uri}'.format(uri='uri_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_of_issued_documents_id(client):
    """Test case for get_list_of_issued_documents_id

    Issued Documents
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/2/files/issued',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_of_issued_documents_version1_id(client):
    """Test case for get_list_of_issued_documents_version1_id

    Issued Documents
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/1/files/issued',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_of_self_uploaded_documents(client):
    """Test case for get_list_of_self_uploaded_documents

    Get List of Self Uploaded Documents
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/1/files/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_of_self_uploaded_documents_id(client):
    """Test case for get_list_of_self_uploaded_documents_id

    Get List of Self Uploaded Documents
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/1/files/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_pull_document_id(client):
    """Test case for pull_document_id

    Pull Document
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'chasis_no': 'chasis_no_example',
        'consent': 'consent_example',
        'doctype': 'doctype_example',
        'orgid': 'orgid_example',
        'reg_no': 'reg_no_example'
        }
    response = await client.request(
        method='POST',
        path='/public/oauth2/1/pull/pulldocument',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_upload_file_to_locker_id(client):
    """Test case for upload_file_to_locker_id

    Upload file to locker
    """
    body = openapi_server.FileUpload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'path': 'path_example',
        'hmac': 'hmac_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/public/oauth2/1/file/upload',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

