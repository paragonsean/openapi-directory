from typing import List, Dict
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
from openapi_server import util


async def get_certificate_data_in_xml_format_from_uri_id(request: web.Request, uri) -> web.Response:
    """Get Certificate Data in XML Format from URI

    Returns the certificate data in machine readable XML format for a URI. This API can be used to only for issued documents. The XML data may not be available for all documents. If the XML data is available for a particular document, the mime parameter in Get List of Issued Documents API will contain application/xml. Please refer to Digital Locker XML Certificate Formats for more details of XML formats of various documents.

    :param uri: 
    :type uri: str

    """
    return web.Response(status=200)


async def get_e_aadhaar_data_in_xml_format_id(request: web.Request, ) -> web.Response:
    """Get e-Aadhaar Data in XML Format

    Returns e-Aadhaar data in XML format for the account.


    """
    return web.Response(status=200)


async def get_file_from_uri_id(request: web.Request, uri) -> web.Response:
    """Get File from URI

    Returns a file from URI. This API can be used to fetch both issued document and uploaded document.

    :param uri: This is the unique identifier of the document.
    :type uri: str

    """
    return web.Response(status=200)


async def get_list_of_issued_documents_id(request: web.Request, ) -> web.Response:
    """Issued Documents

    Returns the list of meta-data about issued documents in user’s DigiLocker.


    """
    return web.Response(status=200)


async def get_list_of_issued_documents_version1_id(request: web.Request, ) -> web.Response:
    """Issued Documents

    Returns the list of meta-data about issued documents in user’s DigiLocker.


    """
    return web.Response(status=200)


async def get_list_of_self_uploaded_documents(request: web.Request, ) -> web.Response:
    """Get List of Self Uploaded Documents

    Returns the list of meta-data about documents or folders in user’s DigiLocker in a specific location.


    """
    return web.Response(status=200)


async def get_list_of_self_uploaded_documents_id(request: web.Request, id) -> web.Response:
    """Get List of Self Uploaded Documents

    Returns the list of meta-data about documents or folders in user’s DigiLocker in a specific location.

    :param id: The id of the folder to list. To list the files of root folder of a user’s locker, do not send this parameter. This is sent as a part of the URL.
    :type id: str

    """
    return web.Response(status=200)


async def pull_document_id(request: web.Request, chasis_no=None, consent=None, doctype=None, orgid=None, reg_no=None) -> web.Response:
    """Pull Document

    This API allows a client application to search a document/certificate from issuer’s repository using the parameters provided by a user. The searched document is saved in user’s issued document section of DigiLocker if the search is successful.

    :param chasis_no: Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API.
    :type chasis_no: str
    :param consent: The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’.
    :type consent: str
    :param doctype: A 5 character unique document type provided by DigiLocker.
    :type doctype: str
    :param orgid: The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned above.
    :type orgid: str
    :param reg_no: Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API.
    :type reg_no: str

    """
    return web.Response(status=200)


async def upload_file_to_locker_id(request: web.Request, path=None, hmac=None, body=None) -> web.Response:
    """Upload file to locker

    This API can be used to save/upload a file to uploaded documents in DigiLocker. The allowed file types are JPG, JPEG, PNG and PDF. The file size must not exceed 10MB.

    :param path: The destination path of the file in DigiLocker including filename.
    :type path: str
    :param hmac: This is used to verify the integrity of the file data. The client app calculates the hash message authentication code (HMAC) of the file content using SHA256 hashing algorithm and the client secret as the hashing key. The resulting HMAC is converted to Base64 format and sent in this parameter. Upon upload of file, DigiLocker calculates the HMAC of the file data and compares it with this HMAC..
    :type hmac: str
    :param body: 
    :type body: dict | bytes

    """
    body = FileUpload.from_dict(body)
    return web.Response(status=200)
