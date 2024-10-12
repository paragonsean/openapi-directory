from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorisations import Authorisations
from openapi_server.models.error400_ngsbs import Error400NGSBS
from openapi_server.models.error400_sbs import Error400SBS
from openapi_server.models.error401_ngsbs import Error401NGSBS
from openapi_server.models.error401_sbs import Error401SBS
from openapi_server.models.error403_ngsbs import Error403NGSBS
from openapi_server.models.error403_sbs import Error403SBS
from openapi_server.models.error404_ngsbs import Error404NGSBS
from openapi_server.models.error404_sbs import Error404SBS
from openapi_server.models.error405_ngsbs import Error405NGSBS
from openapi_server.models.error405_sbs import Error405SBS
from openapi_server.models.error409_ngsbs import Error409NGSBS
from openapi_server.models.error409_sbs import Error409SBS
from openapi_server.models.sca_status_response import ScaStatusResponse
from openapi_server.models.signing_basket import SigningBasket
from openapi_server.models.signing_basket_response200 import SigningBasketResponse200
from openapi_server.models.signing_basket_response201 import SigningBasketResponse201
from openapi_server.models.signing_basket_status_response200 import SigningBasketStatusResponse200
from openapi_server.models.start_consent_authorisation_request import StartConsentAuthorisationRequest
from openapi_server.models.start_scaprocess_response import StartScaprocessResponse
from openapi_server.models.update_consents_psu_data200_response import UpdateConsentsPsuData200Response
from openapi_server.models.update_consents_psu_data_request import UpdateConsentsPsuDataRequest
from openapi_server import util


async def create_signing_basket(request: web.Request, x_request_id, psu_ip_address, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, consent_id=None, tpp_redirect_preferred=None, tpp_redirect_uri=None, tpp_nok_redirect_uri=None, tpp_explicit_authorisation_preferred=None, tpp_notification_uri=None, tpp_notification_content_preferred=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Create a signing basket resource

    Create a signing basket resource for authorising several transactions with one SCA method.  The resource identifications of these transactions are contained in the payload of this access method 

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
    :param consent_id: This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
    :type consent_id: str
    :param tpp_redirect_preferred: If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
    :type tpp_redirect_preferred: bool
    :param tpp_redirect_uri: URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
    :type tpp_redirect_uri: str
    :param tpp_nok_redirect_uri: If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
    :type tpp_nok_redirect_uri: str
    :param tpp_explicit_authorisation_preferred: If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket. 
    :type tpp_explicit_authorisation_preferred: bool
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
    :param body: Request body for a confirmation of an establishing signing basket request. 
    :type body: dict | bytes

    """
    body = SigningBasket.from_dict(body)
    return web.Response(status=200)


async def delete_signing_basket(request: web.Request, basket_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Delete the signing basket

    Delete the signing basket structure as long as no (partial) authorisation has yet been applied. The undlerying transactions are not affected by this deletion.  Remark: The signing basket as such is not deletable after a first (partial) authorisation has been applied. Nevertheless, single transactions might be cancelled on an individual basis on the XS2A interface. 

    :param basket_id: This identification of the corresponding signing basket object. 
    :type basket_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
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


async def get_signing_basket(request: web.Request, basket_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Returns the content of an signing basket object

    Returns the content of a signing basket object.

    :param basket_id: This identification of the corresponding signing basket object. 
    :type basket_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
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


async def get_signing_basket_authorisation(request: web.Request, basket_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Get signing basket authorisation sub-resources request

    Read a list of all authorisation subresources IDs which have been created.  This function returns an array of hyperlinks to all generated authorisation sub-resources. 

    :param basket_id: This identification of the corresponding signing basket object. 
    :type basket_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
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


async def get_signing_basket_sca_status(request: web.Request, basket_id, authorisation_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read the SCA status of the signing basket authorisation

    This method returns the SCA status of a signing basket&#39;s authorisation sub-resource. 

    :param basket_id: This identification of the corresponding signing basket object. 
    :type basket_id: str
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
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
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


async def get_signing_basket_status(request: web.Request, basket_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read the status of the signing basket

    Returns the status of a signing basket object. 

    :param basket_id: This identification of the corresponding signing basket object. 
    :type basket_id: str
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
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
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


async def start_signing_basket_authorisation(request: web.Request, basket_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, tpp_redirect_preferred=None, tpp_redirect_uri=None, tpp_nok_redirect_uri=None, tpp_notification_uri=None, tpp_notification_content_preferred=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Start the authorisation process for a signing basket

    Create an authorisation sub-resource and start the authorisation process of a signing basket. The message might in addition transmit authentication and authorisation related data.  This method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the signing-baskets.  The ASPSP might make the usage of this access method unnecessary in case of only one SCA process needed, since the related authorisation resource might be automatically created by the ASPSP after the submission of the payment data with the first POST signing basket call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;,      * &#39;startAuthorisationWithPsuAuthentication&#39;      * &#39;startAuthorisationWithEncryptedPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;   * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding      payment cancellation response that an explicit start of the authorisation process is needed by the TPP.     The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded     by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

    :param basket_id: This identification of the corresponding signing basket object. 
    :type basket_id: str
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
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
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


async def update_signing_basket_psu_data(request: web.Request, basket_id, authorisation_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Update PSU data for signing basket

    This method update PSU data on the signing basket resource if needed.  It may authorise a igning basket within the embedded SCA approach where needed.  Independently from the SCA Approach it supports e.g. the selection of  the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of a consent request if needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific Update PSU data request is only applicable for   * adding the PSU Identification, if not provided yet in the payment initiation request or the account information consent request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The update PSU data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA approach might depend on the chosen SCA method.  For that reason, the following possible update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization Method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

    :param basket_id: This identification of the corresponding signing basket object. 
    :type basket_id: str
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
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
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
