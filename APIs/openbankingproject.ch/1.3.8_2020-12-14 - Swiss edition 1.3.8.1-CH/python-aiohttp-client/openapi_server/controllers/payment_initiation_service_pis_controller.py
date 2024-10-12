from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorisations import Authorisations
from openapi_server.models.error400_ngpis import Error400NGPIS
from openapi_server.models.error400_pis import Error400PIS
from openapi_server.models.error401_ngpis import Error401NGPIS
from openapi_server.models.error401_pis import Error401PIS
from openapi_server.models.error403_ngpis import Error403NGPIS
from openapi_server.models.error403_pis import Error403PIS
from openapi_server.models.error404_ngpis import Error404NGPIS
from openapi_server.models.error404_pis import Error404PIS
from openapi_server.models.error405_ngpis import Error405NGPIS
from openapi_server.models.error405_ngpiscanc import Error405NGPISCANC
from openapi_server.models.error405_pis import Error405PIS
from openapi_server.models.error405_piscanc import Error405PISCANC
from openapi_server.models.error409_ngpis import Error409NGPIS
from openapi_server.models.error409_pis import Error409PIS
from openapi_server.models.get_payment_information200_response import GetPaymentInformation200Response
from openapi_server.models.initiate_payment_request import InitiatePaymentRequest
from openapi_server.models.initiate_payment_request1 import InitiatePaymentRequest1
from openapi_server.models.payment_initation_request_response201 import PaymentInitationRequestResponse201
from openapi_server.models.payment_initiation_cancel_response202 import PaymentInitiationCancelResponse202
from openapi_server.models.payment_initiation_status_response200_json import PaymentInitiationStatusResponse200Json
from openapi_server.models.periodic_payment_initiation_multipart_body import PeriodicPaymentInitiationMultipartBody
from openapi_server.models.sca_status_response import ScaStatusResponse
from openapi_server.models.start_consent_authorisation_request import StartConsentAuthorisationRequest
from openapi_server.models.start_scaprocess_response import StartScaprocessResponse
from openapi_server.models.update_consents_psu_data200_response import UpdateConsentsPsuData200Response
from openapi_server.models.update_consents_psu_data_request import UpdateConsentsPsuDataRequest
from openapi_server import util


async def cancel_payment(request: web.Request, payment_service, payment_product, payment_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, tpp_redirect_preferred=None, tpp_nok_redirect_uri=None, tpp_redirect_uri=None, tpp_explicit_authorisation_preferred=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Payment cancellation request

    This method initiates the cancellation of a payment.  Depending on the payment-service, the payment-product and the ASPSP&#39;s implementation,  this TPP call might be sufficient to cancel a payment.  If an authorisation of the payment cancellation is mandated by the ASPSP,  a corresponding hyperlink will be contained in the response message.  Cancels the addressed payment with resource identification paymentId if applicable to the payment-service, payment-product and received in product related timelines (e.g. before end of business day for scheduled payments of the last business day before the scheduled execution day).   The response to this DELETE command will tell the TPP whether the   * access method was rejected,   * access method was successful, or   * access method is generally applicable, but further authorisation processes are needed. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str
    :param tpp_redirect_preferred: If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
    :type tpp_redirect_preferred: bool
    :param tpp_nok_redirect_uri: If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
    :type tpp_nok_redirect_uri: str
    :param tpp_redirect_uri: URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
    :type tpp_redirect_uri: str
    :param tpp_explicit_authorisation_preferred: If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket. 
    :type tpp_explicit_authorisation_preferred: bool
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


async def get_payment_cancellation_sca_status(request: web.Request, payment_service, payment_product, payment_id, authorisation_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read the SCA status of the payment cancellation&#39;s authorisation

    This method returns the SCA status of a payment initiation&#39;s authorisation sub-resource. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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


async def get_payment_information(request: web.Request, payment_service, payment_product, payment_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Get payment information

    Returns the content of a payment object

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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


async def get_payment_initiation_authorisation(request: web.Request, payment_service, payment_product, payment_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Get payment initiation authorisation sub-resources request

    Read a list of all authorisation subresources IDs which have been created.  This function returns an array of hyperlinks to all generated authorisation sub-resources. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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


async def get_payment_initiation_cancellation_authorisation_information(request: web.Request, payment_service, payment_product, payment_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Will deliver an array of resource identifications to all generated cancellation authorisation sub-resources

    Retrieve a list of all created cancellation authorisation sub-resources. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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


async def get_payment_initiation_sca_status(request: web.Request, payment_service, payment_product, payment_id, authorisation_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Read the SCA status of the payment authorisation

    This method returns the SCA status of a payment initiation&#39;s authorisation sub-resource. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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


async def get_payment_initiation_status(request: web.Request, payment_service, payment_product, payment_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Payment initiation status request

    Check the transaction status of a payment initiation.

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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


async def initiate_payment(request: web.Request, payment_service, payment_product, x_request_id, psu_ip_address, body, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, consent_id=None, tpp_redirect_preferred=None, tpp_redirect_uri=None, tpp_nok_redirect_uri=None, tpp_explicit_authorisation_preferred=None, tpp_rejection_no_funds_preferred=None, tpp_brand_logging_information=None, tpp_notification_uri=None, tpp_notification_content_preferred=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None) -> web.Response:
    """Payment initiation request

    This method is used to initiate a payment at the ASPSP.  ## Variants of payment initiation requests  This method to initiate a payment initiation at the ASPSP can be sent with either a JSON body or an pain.001 body depending on the payment product in the path.  There are the following **payment products**:    - Payment products with payment information in *JSON* format:     - ***domestic-swiss-credit-transfers-isr***     - ***domestic-swiss-credit-transfers***     - ***domestic-swiss-credit-transfers-qr***     - ***domestic-swiss-foreign-credit-transfers***     - ***swiss-sepa-credit-transfers***     - ***swiss-cross-border-credit-transfers***   - Payment products with payment information in *SIX pain.001* XML format:     - ***pain.001-sepa-credit-transfers***     - ***pain.001-cross-border-credit-transfers***     - ***pain.001-swiss-six-credit-transfers***  Furthermore the request body depends on the **payment-service**:   * ***payments***: A single payment initiation request.   * ***bulk-payments***: A collection of several payment initiation requests.        In case of a *pain.001* message there are more than one payments contained in the *pain.001 message.      In case of a *JSON* there are several JSON payment blocks contained in a joining list.   * ***periodic-payments***:     Create a standing order initiation resource for recurrent i.e. periodic payments addressable under {paymentId}      with all data relevant for the corresponding payment product and the execution of the standing order contained in a JSON body.  This is the first step in the API to initiate the related recurring/periodic payment.  ## Single and mulitilevel SCA Processes  The payment initiation requests are independent from the need of one or multilevel  SCA processing, i.e. independent from the number of authorisations needed for the execution of payments.   But the response messages are specific to either one SCA processing or multilevel SCA processing.   For payment initiation with multilevel SCA, this specification requires an explicit start of the authorisation,  i.e. links directly associated with SCA processing like &#39;scaRedirect&#39; or &#39;scaOAuth&#39; cannot be contained in the  response message of a Payment Initation Request for a payment, where multiple authorisations are needed.  Also if any data is needed for the next action, like selecting an SCA method is not supported in the response,  since all starts of the multiple authorisations are fully equal.  In these cases, first an authorisation sub-resource has to be generated following the &#39;startAuthorisation&#39; link. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param psu_ip_address: The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. If not available, the TPP shall use the IP Address used by the TPP when submitting this request. 
    :type psu_ip_address: str
    :param body: JSON request body for a payment inition request message.  There are the following payment-products supported:   * \&quot;domestic-swiss-credit-transfers-isr\&quot;   * \&quot;domestic-swiss-credit-transfers\&quot;   * \&quot;domestic-swiss-credit-transfers-qr\&quot;   * \&quot;domestic-swiss-foreign-credit-transfers\&quot;   * \&quot;swiss-sepa-credit-transfers\&quot; with JSON-Body   * \&quot;swiss-cross-border-credit-transfers\&quot; with JSON-Body   * \&quot;pain.001-sepa-credit-transfers\&quot; with XML pain.001.001.03 body for SCT scheme     Only country specific schemes are currently available   * \&quot;pain.001-cross-border-credit-transfers\&quot; with pain.001 body.     Only country specific schemes are currently available   * \&quot;pain.001-swiss-six-credit-transfers\&quot;  There are the following payment-services supported:   * \&quot;payments\&quot;   * \&quot;periodic-payments\&quot;   * \&quot;bulk-paments\&quot;  All optional, conditional and predefined but not yet used fields are defined. 
    :type body: dict | bytes
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
    :param tpp_rejection_no_funds_preferred: If it equals \&quot;true\&quot; then the TPP prefers a rejection of the payment initiation in case the ASPSP is providing an integrated confirmation of funds request an the result of this is that not sufficient funds are available.  If it equals \&quot;false\&quot; then the TPP prefers that the ASPSP is dealing with the payment initiation like in the ASPSPs online channel, potentially waiting for a certain time period for funds to arrive to initiate the payment.  This parameter might be ignored by the ASPSP. 
    :type tpp_rejection_no_funds_preferred: bool
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

    """
    body = InitiatePaymentRequest.from_dict(body)
    return web.Response(status=200)


async def start_payment_authorisation(request: web.Request, payment_service, payment_product, payment_id, x_request_id, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, tpp_redirect_preferred=None, tpp_redirect_uri=None, tpp_nok_redirect_uri=None, tpp_notification_uri=None, tpp_notification_content_preferred=None, digest=None, signature=None, tpp_signature_certificate=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Start the authorisation process for a payment initiation

    Create an authorisation sub-resource and start the authorisation process. The message might in addition transmit authentication and authorisation related data.  This method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the transaction.  The ASPSP might make the usage of this access method unnecessary in case of only one SCA process needed, since the related authorisation resource might be automatically created by the ASPSP after the submission of the payment data with the first POST payments/{payment-product} call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding Payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;     * &#39;startAuthorisationWithPsuAuthentication&#39;     * &#39;startAuthorisationWithEncryptedPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;   * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding      Payment cancellation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = StartConsentAuthorisationRequest.from_dict(body)
    return web.Response(status=200)


async def start_payment_initiation_cancellation_authorisation(request: web.Request, payment_service, payment_product, payment_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, tpp_redirect_preferred=None, tpp_redirect_uri=None, tpp_nok_redirect_uri=None, tpp_notification_uri=None, tpp_notification_content_preferred=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Start the authorisation process for the cancellation of the addressed payment

    Creates an authorisation sub-resource and start the authorisation process of the cancellation of the addressed payment. The message might in addition transmit authentication and authorisation related data.  This method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the cancellation-authorisation.  The ASPSP might make the usage of this access method unnecessary in case of only one SCA process needed, since the related authorisation resource might be automatically created by the ASPSP after the submission of the payment data with the first POST payments/{payment-product} call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;     * &#39;startAuthorisationWithPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;    * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding      payment cancellation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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


async def update_payment_cancellation_psu_data(request: web.Request, payment_service, payment_product, payment_id, authorisation_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Update PSU data for payment initiation cancellation

    This method updates PSU data on the cancellation authorisation resource if needed.  It may authorise a cancellation of the payment within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of a cancellation authorisation within the payment initiation services needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific Update PSU data request is only applicable for   * adding the PSU Identification, if not provided yet in the payment initiation request or the Account Information Consent Request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA approach might depend on the chosen SCA method.  For that reason, the following possible update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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


async def update_payment_psu_data(request: web.Request, payment_service, payment_product, payment_id, authorisation_id, x_request_id, digest=None, signature=None, tpp_signature_certificate=None, psu_id=None, psu_id_type=None, psu_corporate_id=None, psu_corporate_id_type=None, psu_ip_address=None, psu_ip_port=None, psu_accept=None, psu_accept_charset=None, psu_accept_encoding=None, psu_accept_language=None, psu_user_agent=None, psu_http_method=None, psu_device_id=None, psu_geo_location=None, body=None) -> web.Response:
    """Update PSU data for payment initiation

    This methods updates PSU data on the authorisation resource if needed. It may authorise a payment within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of payment initiation services needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific update PSU data request is only applicable for   * adding the PSU identification, if not provided yet in the payment initiation request or the account information consent request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU Data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA Approach might depend on the chosen SCA method.  For that reason, the following possible Update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

    :param payment_service: Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    :type payment_service: str
    :param payment_product: The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    :type payment_product: str
    :param payment_id: Resource identification of the generated payment initiation resource.
    :type payment_id: str
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
