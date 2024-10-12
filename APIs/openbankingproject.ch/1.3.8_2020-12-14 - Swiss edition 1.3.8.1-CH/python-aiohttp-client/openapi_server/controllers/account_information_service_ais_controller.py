from typing import List, Dict
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
from openapi_server import util


async def create_consent(request: web.Request, x_request_id, psu_ip_address, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, tpp_redirect_preferred=None, tpp_redirect_uri=None, tpp_nok_redirect_uri=None, tpp_explicit_authorisation_preferred=None, tpp_brand_logging_information=None, tpp_notification_uri=None, tpp_notification_content_preferred=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Create consent

    This method create a consent resource, defining access rights to dedicated accounts of  a given PSU-ID. These accounts are addressed explicitly in the method as  parameters as a core function.  **Side Effects** When this consent request is a request where the \&quot;recurringIndicator\&quot; equals \&quot;true\&quot;, and if it exists already a former consent for recurring access on account information  for the addressed PSU, then the former consent automatically expires as soon as the new  consent request is authorised by the PSU.  Optional Extension: As an option, an ASPSP might optionally accept a specific access right on the access on all PSD2 related services for all available accounts.  As another option an ASPSP might optionally also accept a command, where only access rights are inserted without mentioning the addressed account.  The relation to accounts is then handled afterwards between PSU and ASPSP.  This option is not supported for the Embedded SCA Approach.  As a last option, an ASPSP might in addition accept a command with access rights   * to see the list of available payment accounts or   * to see the list of available payment accounts with balances. 

    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. If not available, the TPP shall use the IP Address used by the TPP when submitting this request. 
    :type psu_ip_address: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_id: Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
    :type psu_id: str
    :param psu_id_type: Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation. 
    :type psu_id_type: str
    :param psu_corporate_id: Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context. 
    :type psu_corporate_id: str
    :param psu_corporate_id_type: Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context. 
    :type psu_corporate_id_type: str
    :param tpp_redirect_preferred: If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
    :type tpp_redirect_preferred: bool
    :param tpp_redirect_uri: URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
    :type tpp_redirect_uri: str
    :param tpp_nok_redirect_uri: If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
    :type tpp_nok_redirect_uri: str
    :param tpp_explicit_authorisation_preferred: If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket. 
    :type tpp_explicit_authorisation_preferred: bool
    :param tpp_brand_logging_information: This header might be used by TPPs to inform the ASPSP about the brand used by the TPP towards the PSU.  This information is meant for logging entries to enhance communication between ASPSP and PSU or ASPSP and TPP.  This header might be ignored by the ASPSP. 
    :type tpp_brand_logging_information: str
    :param tpp_notification_uri: URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply. 
    :type tpp_notification_uri: str
    :param tpp_notification_content_preferred: The string has the form  status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP. 
    :type tpp_notification_content_preferred: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str
    :param body: Request body for a consents request. 
    :type body: dict | bytes

    """
    body = Consents.from_dict(body)
    return web.Response(status=200)


async def delete_consent(request: web.Request, consent_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Delete Consent

    The TPP can delete an account information consent object if needed.

    :param consent_id: ID of the corresponding consent object as returned by an account information consent request. 
    :type consent_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def get_account_list(request: web.Request, x_request_id, consent_id, with_balance=None, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read account list

    Read the identifiers of the available payment account together with  booking balance information, depending on the consent granted.  It is assumed that a consent of the PSU to this access is already given and stored on the ASPSP system. The addressed list of accounts depends then on the PSU ID and the stored consent addressed by consentId, respectively the OAuth2 access token.  Returns all identifiers of the accounts, to which an account access has been granted to through the /consents endpoint by the PSU. In addition, relevant information about the accounts and hyperlinks to corresponding account information resources are provided if a related consent has been already granted.  Remark: Note that the /consents endpoint optionally offers to grant an access on all available payment accounts of a PSU. In this case, this endpoint will deliver the information about all available payment accounts of the PSU at this ASPSP. 

    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param consent_id: This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
    :type consent_id: str
    :param with_balance: If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP. 
    :type with_balance: bool
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def get_balances(request: web.Request, account_id, x_request_id, consent_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read balance

    Reads account data from a given account addressed by \&quot;account-id\&quot;.   **Remark:** This account-id can be a tokenised identification due to data protection reason since the path  information might be logged on intermediary servers within the ASPSP sphere.  This account-id then can be retrieved by the \&quot;Get account list\&quot; call.  The account-id is constant at least throughout the lifecycle of a given consent. 

    :param account_id: This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; or \&quot;Read Card Account list\&quot; call.  The account-id is the \&quot;resourceId\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
    :type account_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param consent_id: This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
    :type consent_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def get_consent_authorisation(request: web.Request, consent_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Get consent authorisation sub-resources request

    Return a list of all authorisation subresources IDs which have been created.  This function returns an array of hyperlinks to all generated authorisation sub-resources. 

    :param consent_id: ID of the corresponding consent object as returned by an account information consent request. 
    :type consent_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def get_consent_information(request: web.Request, consent_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Get consent request

    Returns the content of an account information consent object.  This is returning the data for the TPP especially in cases,  where the consent was directly managed between ASPSP and PSU e.g. in a redirect SCA Approach. 

    :param consent_id: ID of the corresponding consent object as returned by an account information consent request. 
    :type consent_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def get_consent_sca_status(request: web.Request, consent_id, authorisation_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read the SCA status of the consent authorisation

    This method returns the SCA status of a consent initiation&#39;s authorisation sub-resource. 

    :param consent_id: ID of the corresponding consent object as returned by an account information consent request. 
    :type consent_id: str
    :param authorisation_id: Resource identification of the related SCA.
    :type authorisation_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def get_consent_status(request: web.Request, consent_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Consent status request

    Read the status of an account information consent resource.

    :param consent_id: ID of the corresponding consent object as returned by an account information consent request. 
    :type consent_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def get_transaction_details(request: web.Request, account_id, transaction_id, x_request_id, consent_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read transaction details

    Reads transaction details from a given transaction addressed by \&quot;transactionId\&quot; on a given account addressed by \&quot;account-id\&quot;. This call is only available on transactions as reported in a JSON format.  **Remark:** Please note that the PATH might be already given in detail by the corresponding entry of the response of the \&quot;Read Transaction List\&quot; call within the _links subfield. 

    :param account_id: This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; or \&quot;Read Card Account list\&quot; call.  The account-id is the \&quot;resourceId\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
    :type account_id: str
    :param transaction_id: This identification is given by the attribute transactionId of the corresponding entry of a transaction list. 
    :type transaction_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param consent_id: This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
    :type consent_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def get_transaction_list(request: web.Request, account_id, booking_status, x_request_id, consent_id, date_from=None, date_to=None, entry_reference_from=None, delta_list=None, with_balance=None, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read transaction list of an account

    Read transaction reports or transaction lists of a given account ddressed by \&quot;account-id\&quot;, depending on the steering parameter \&quot;bookingStatus\&quot; together with balances.  For a given account, additional parameters are e.g. the attributes \&quot;dateFrom\&quot; and \&quot;dateTo\&quot;. The ASPSP might add balance information, if transaction lists without balances are not supported. 

    :param account_id: This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; or \&quot;Read Card Account list\&quot; call.  The account-id is the \&quot;resourceId\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
    :type account_id: str
    :param booking_status: Permitted codes are    * \&quot;information\&quot;,   * \&quot;booked\&quot;,   * \&quot;pending\&quot;, and    * \&quot;both\&quot; \&quot;booked\&quot; shall be supported by the ASPSP. To support the \&quot;pending\&quot; and \&quot;both\&quot; feature is optional for the ASPSP, Error code if not supported in the online banking frontend 
    :type booking_status: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param consent_id: This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
    :type consent_id: str
    :param date_from: Conditional: Starting date (inclusive the date dateFrom) of the transaction list, mandated if no delta access is required and if bookingStatus does not equal \&quot;information\&quot;.  For booked transactions, the relevant date is the booking date.   For pending transactions, the relevant date is the entry date, which may not be transparent  neither in this API nor other channels of the ASPSP. 
    :type date_from: str
    :param date_to: End date (inclusive the data dateTo) of the transaction list, default is \&quot;now\&quot; if not given.  Might be ignored if a delta function is used.  For booked transactions, the relevant date is the booking date.  For pending transactions, the relevant date is the entry date, which may not be transparent neither in this API nor other channels of the ASPSP. 
    :type date_to: str
    :param entry_reference_from: This data attribute is indicating that the AISP is in favour to get all transactions after the transaction with identification entryReferenceFrom alternatively to the above defined period. This is a implementation of a delta access. If this data element is contained, the entries \&quot;dateFrom\&quot; and \&quot;dateTo\&quot; might be ignored by the ASPSP if a delta report is supported.  Optional if supported by API provider. 
    :type entry_reference_from: str
    :param delta_list: This data attribute is indicating that the AISP is in favour to get all transactions after the last report access for this PSU on the addressed account. This is another implementation of a delta access-report. This delta indicator might be rejected by the ASPSP if this function is not supported. Optional if supported by API provider
    :type delta_list: bool
    :param with_balance: If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP. 
    :type with_balance: bool
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)


async def read_account_details(request: web.Request, account_id, x_request_id, consent_id, with_balance=None, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read account details

    Reads details about an account, with balances where required.  It is assumed that a consent of the PSU to  this access is already given and stored on the ASPSP system.  The addressed details of this account depends then on the stored consent addressed by consentId,  respectively the OAuth2 access token.  **NOTE:** The account-id can represent a multicurrency account. In this case the currency code is set to \&quot;XXX\&quot;.  Give detailed information about the addressed account.  Give detailed information about the addressed account together with balance information 

    :param account_id: This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; or \&quot;Read Card Account list\&quot; call.  The account-id is the \&quot;resourceId\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
    :type account_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param consent_id: This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
    :type consent_id: str
    :param with_balance: If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP. 
    :type with_balance: bool
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str

    """
    return web.Response(status=200)


async def start_consent_authorisation(request: web.Request, consent_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, tpp_redirect_preferred=None, tpp_redirect_uri=None, tpp_nok_redirect_uri=None, tpp_notification_uri=None, tpp_notification_content_preferred=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Start the authorisation process for a consent

    Create an authorisation sub-resource and start the authorisation process of a consent. The message might in addition transmit authentication and authorisation related data.  his method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the consent.  The ASPSP might make the usage of this access method unnecessary, since the related authorisation resource will be automatically created by the ASPSP after the submission of the consent data with the first POST consents call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with an &#39;startAuthorisation&#39; hyperlink in the preceding Payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;,      * &#39;startAuthorisationWithPsuAuthentication&#39;      * &#39;startAuthorisationWithEncryptedPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;   * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with an &#39;startAuthorisation&#39; hyperlink in the preceding      payment cancellation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

    :param consent_id: ID of the corresponding consent object as returned by an account information consent request. 
    :type consent_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_id: Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
    :type psu_id: str
    :param psu_id_type: Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation. 
    :type psu_id_type: str
    :param psu_corporate_id: Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context. 
    :type psu_corporate_id: str
    :param psu_corporate_id_type: Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context. 
    :type psu_corporate_id_type: str
    :param tpp_redirect_preferred: If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
    :type tpp_redirect_preferred: bool
    :param tpp_redirect_uri: URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
    :type tpp_redirect_uri: str
    :param tpp_nok_redirect_uri: If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
    :type tpp_nok_redirect_uri: str
    :param tpp_notification_uri: URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply. 
    :type tpp_notification_uri: str
    :param tpp_notification_content_preferred: The string has the form  status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP. 
    :type tpp_notification_content_preferred: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str
    :param body: 
    :type body: dict | bytes

    """
    body = StartConsentAuthorisationRequest.from_dict(body)
    return web.Response(status=200)


async def update_consents_psu_data(request: web.Request, consent_id, authorisation_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Update PSU Data for consents

    This method update PSU data on the consents  resource if needed. It may authorise a consent within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of a consent request if needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific update PSU data request is only applicable for   * adding the PSU Identification, if not provided yet in the payment initiation request or the Account Information Consent Request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA Approach might depend on the chosen SCA method.  For that reason, the following possible update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

    :param consent_id: ID of the corresponding consent object as returned by an account information consent request. 
    :type consent_id: str
    :param authorisation_id: Resource identification of the related SCA.
    :type authorisation_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_id: Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
    :type psu_id: str
    :param psu_id_type: Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation. 
    :type psu_id_type: str
    :param psu_corporate_id: Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context. 
    :type psu_corporate_id: str
    :param psu_corporate_id_type: Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context. 
    :type psu_corporate_id_type: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
    :type psu_ip_address: str
    :param psu_ip_port: The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    :type psu_ip_port: str
    :param psu_accept: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept: str
    :param psu_accept_charset: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_charset: str
    :param psu_accept_encoding: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_encoding: str
    :param psu_accept_language: The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    :type psu_accept_language: str
    :param psu_user_agent: The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    :type psu_user_agent: str
    :param psu_http_method: HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    :type psu_http_method: str
    :param psu_device_id: UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    :type psu_device_id: str
    :param psu_geo_location: The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    :type psu_geo_location: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateConsentsPsuDataRequest.from_dict(body)
    return web.Response(status=200)
