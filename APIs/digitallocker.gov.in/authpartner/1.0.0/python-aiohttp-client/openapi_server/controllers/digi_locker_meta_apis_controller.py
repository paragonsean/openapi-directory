from typing import List, Dict
from aiohttp import web

from openapi_server.models.doc_type_response import DocTypeResponse
from openapi_server.models.get_device_code_id401_response import GetDeviceCodeId401Response
from openapi_server.models.get_list_of_documents_provided_by_an_issuer_id400_response import GetListOfDocumentsProvidedByAnIssuerId400Response
from openapi_server.models.get_list_of_issuers_id400_response import GetListOfIssuersId400Response
from openapi_server.models.get_search_parameters_for_a_document_id400_response import GetSearchParametersForADocumentId400Response
from openapi_server.models.get_statistics_id400_response import GetStatisticsId400Response
from openapi_server.models.get_statistics_response import GetStatisticsResponse
from openapi_server.models.issuer_response import IssuerResponse
from openapi_server.models.push_urito_account_id400_response import PushURIToAccountId400Response
from openapi_server.models.push_urito_account_id401_response import PushURIToAccountId401Response
from openapi_server.models.push_urito_account_id404_response import PushURIToAccountId404Response
from openapi_server.models.push_urito_account_id500_response import PushURIToAccountId500Response
from openapi_server.models.search_parameters_response_inner import SearchParametersResponseInner
from openapi_server.models.verify_account_id400_response import VerifyAccountId400Response
from openapi_server.models.verify_account_id500_response import VerifyAccountId500Response
from openapi_server.models.verify_account_response import VerifyAccountResponse
from openapi_server import util


async def get_list_of_documents_provided_by_an_issuer_id(request: web.Request, clientid=None, hmac=None, orgid=None, ts=None) -> web.Response:
    """Get List of Documents Provided by an Issuer

    Returns a list of documents/certificates issued by an issuer organization registered with DigiLocker.

    :param clientid: Provide the client id that was created during the application registration process on Partners Portal.
    :type clientid: str
    :param hmac: Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    :type hmac: str
    :param orgid: The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier.
    :type orgid: str
    :param ts: Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    :type ts: str

    """
    return web.Response(status=200)


async def get_list_of_issuers_id(request: web.Request, clientid=None, hmac=None, ts=None) -> web.Response:
    """Get List of Issuers

    Returns the list of issuers registered with DigiLocker.

    :param clientid: Provide the client id that was created during the application registration process on Partners Portal.
    :type clientid: str
    :param hmac: Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    :type hmac: str
    :param ts: Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    :type ts: str

    """
    return web.Response(status=200)


async def get_search_parameters_for_a_document_id(request: web.Request, clientid=None, doctype=None, hmac=None, orgid=None, ts=None) -> web.Response:
    """Get Search Parameters for a Document

    Returns a list of parameters required to search a document/certificate of an issuer organization registered with DigiLocker. These parameters are used to pull a document from issuer’s repository using Pull Document API mentioned in subsequent section.

    :param clientid: Provide the client id that was created during the application registration process on Partners Portal.
    :type clientid: str
    :param doctype: A 5 character unique document type provided by DigiLocker.
    :type doctype: str
    :param hmac: Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    :type hmac: str
    :param orgid: The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier.
    :type orgid: str
    :param ts: Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    :type ts: str

    """
    return web.Response(status=200)


async def get_statistics_id(request: web.Request, clientid=None, hmac=None, ts=None) -> web.Response:
    """Get Statistics

    Returns DigiLocker statistics such as the count of users, authentic documents, issuers and requesters as on a specific date.

    :param clientid: Provide the client id that was created during the application registration process on Partners Portal.
    :type clientid: str
    :param hmac: Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    :type hmac: str
    :param ts: Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    :type ts: str

    """
    return web.Response(status=200)


async def push_uri_to_account_id(request: web.Request, action=None, clientid=None, digilockerid=None, docid=None, hmac=None, issuedate=None, ts=None, uri=None, validfrom=None, validto=None) -> web.Response:
    """Push URI to Account

    The API can use to push or delete a single URI into Digital Locker using DigiLocker Id acquired using Get User Details API. This API can be used to push the certificate details to Digital Locker as and when a certificate is generated in the issuer system. The issuing departments must register on DigiLocker as a registered Issuer and implement the requisite Issuer APIs as mentioned in Digital Locker Issuer API Specification document prior to pushing certificates using this API.

    :param action: Action that needs to be taken for the Aadhaar number and URI combination. Possible values are A for adding a new URI, U for updating an already added URI details or D for deleting the URI.
    :type action: str
    :param clientid: Provide the client id that was created during the application registration process on Partners Portal.
    :type clientid: str
    :param digilockerid: This is the DigiLocker Id of the user that was acquired using Get User Details API.
    :type digilockerid: int
    :param docid: A unique number of the document. This id will be unique within the document type issued by the issuer.
    :type docid: str
    :param hmac: Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    :type hmac: str
    :param issuedate: The issue date of the document in DDMMYYYY format.
    :type issuedate: str
    :param ts: Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    :type ts: str
    :param uri: This is the unique identifier of the document.
    :type uri: str
    :param validfrom: The date from which the document is valid in DDMMYYYY format. This may be same as the issue date.
    :type validfrom: int
    :param validto: The expiry date of the document in DDMMYYYY format.
    :type validto: str

    """
    return web.Response(status=200)


async def verify_account_id(request: web.Request, clientid=None, hmac=None, mobile=None, ts=None, uid=None) -> web.Response:
    """Verify Account

    This API can be used to verify whether a mobile number or Aadhaar number is already registered with DigiLocker.

    :param clientid: Provide the client id that was created during the application registration process on Partners Portal.
    :type clientid: str
    :param hmac: Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    :type hmac: str
    :param mobile: This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
    :type mobile: int
    :param ts: Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    :type ts: str
    :param uid: This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists.
    :type uid: int

    """
    return web.Response(status=200)
