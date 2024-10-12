from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_action import CertificateAction
from openapi_server.models.certificate_bundle import CertificateBundle
from openapi_server.models.certificate_callback import CertificateCallback
from openapi_server.models.certificate_create import CertificateCreate
from openapi_server.models.certificate_email_history import CertificateEmailHistory
from openapi_server.models.certificate_identifier import CertificateIdentifier
from openapi_server.models.certificate_reissue import CertificateReissue
from openapi_server.models.certificate_renew import CertificateRenew
from openapi_server.models.certificate_revoke import CertificateRevoke
from openapi_server.models.certificate_site_seal import CertificateSiteSeal
from openapi_server.models.error import Error
from openapi_server import util


async def certificate_action_retrieve(request: web.Request, certificate_id) -> web.Response:
    """Retrieve all certificate actions

    This method is used to retrieve all stateful actions relating to a certificate lifecycle.

    :param certificate_id: Certificate id to register for callback
    :type certificate_id: str

    """
    return web.Response(status=200)


async def certificate_alternate_email_address(request: web.Request, certificate_id, email_address) -> web.Response:
    """Add alternate email address

    This method adds an alternate email address to a certificate order and re-sends all existing request emails to that address.

    :param certificate_id: Certificate id to resend emails
    :type certificate_id: str
    :param email_address: Specific email address to resend email
    :type email_address: str

    """
    return web.Response(status=200)


async def certificate_callback_delete(request: web.Request, certificate_id) -> web.Response:
    """Unregister system callback

    Unregister the callback for a particular certificate.

    :param certificate_id: Certificate id to unregister callback
    :type certificate_id: str

    """
    return web.Response(status=200)


async def certificate_callback_get(request: web.Request, certificate_id) -> web.Response:
    """Retrieve system stateful action callback url

    This method is used to retrieve the registered callback url for a certificate.

    :param certificate_id: Certificate id to register for stateful action callback
    :type certificate_id: str

    """
    return web.Response(status=200)


async def certificate_callback_replace(request: web.Request, certificate_id, callback_url) -> web.Response:
    """Register of certificate action callback

    This method is used to register/replace url for callbacks for stateful actions relating to a certificate lifecycle. The callback url is a Webhook style pattern and will receive POST http requests with json body defined in the CertificateAction model definition for each certificate action.  Only one callback URL is allowed to be registered for each certificateId, so it will replace a previous registration.

    :param certificate_id: Certificate id to register/replace for callback
    :type certificate_id: str
    :param callback_url: Callback url registered/replaced to receive stateful actions
    :type callback_url: str

    """
    return web.Response(status=200)


async def certificate_cancel(request: web.Request, certificate_id) -> web.Response:
    """Cancel a pending certificate

    Use the cancel call to cancel a pending certificate order.

    :param certificate_id: Certificate id to cancel
    :type certificate_id: str

    """
    return web.Response(status=200)


async def certificate_create(request: web.Request, body, x_market_id=None) -> web.Response:
    """Create a pending order for certificate

    &lt;p&gt;Creating a certificate order can be a long running asynchronous operation in the PKI workflow. The PKI API supports 2 options for getting the completion stateful actions for this asynchronous operations: 1) by polling operations -- see /v1/certificates/{certificateId}/actions 2) via WebHook style callback -- see &#39;/v1/certificates/{certificateId}/callback&#39;.&lt;/p&gt;

    :param body: The certificate order information
    :type body: dict | bytes
    :param x_market_id: Setting locale for communications such as emails and error messages
    :type x_market_id: str

    """
    body = CertificateCreate.from_dict(body)
    return web.Response(status=200)


async def certificate_download(request: web.Request, certificate_id) -> web.Response:
    """Download certificate

    

    :param certificate_id: Certificate id to download
    :type certificate_id: str

    """
    return web.Response(status=200)


async def certificate_download_entitlement(request: web.Request, entitlement_id) -> web.Response:
    """Download certificate by entitlement

    

    :param entitlement_id: Entitlement id to download
    :type entitlement_id: str

    """
    return web.Response(status=200)


async def certificate_email_history(request: web.Request, certificate_id) -> web.Response:
    """Retrieve email history

    This method can be used to retrieve all emails sent for a certificate.

    :param certificate_id: Certificate id to retrieve email history
    :type certificate_id: str

    """
    return web.Response(status=200)


async def certificate_get(request: web.Request, certificate_id) -> web.Response:
    """Retrieve certificate details

    Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificate.

    :param certificate_id: Certificate id to lookup
    :type certificate_id: str

    """
    return web.Response(status=200)


async def certificate_get_entitlement(request: web.Request, entitlement_id, latest=None) -> web.Response:
    """Search for certificate details by entitlement

    Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificates associated to an entitlement.

    :param entitlement_id: Entitlement id to lookup
    :type entitlement_id: str
    :param latest: Fetch only the most recent certificate
    :type latest: bool

    """
    return web.Response(status=200)


async def certificate_reissue(request: web.Request, certificate_id, body) -> web.Response:
    """Reissue active certificate

    &lt;p&gt;Rekeying is the process by which the private and public key is changed for a certificate. It is a simplified reissue,where only the CSR is changed. Reissuing is the process by which domain names are added or removed from a certificate.Once a request is validated and approved, the certificate will be reissued with the new common name and sans specified. Unlimited reissues are available during the lifetime of the certificate.New names added to a certificate that do not share the base domain of the common name may take additional time to validate. If this API call is made before a previous pending reissue has been validated and issued, the previous reissue request is automatically rejected and replaced with the current request.&lt;/p&gt;

    :param certificate_id: Certificate id to reissue
    :type certificate_id: str
    :param body: The reissue request info
    :type body: dict | bytes

    """
    body = CertificateReissue.from_dict(body)
    return web.Response(status=200)


async def certificate_renew(request: web.Request, certificate_id, body) -> web.Response:
    """Renew active certificate

    Renewal is the process by which the validity of a certificate is extended. Renewal is only available 60 days prior to expiration of the previous certificate and 30 days after the expiration of the previous certificate. The renewal supports modifying a set of the original certificate order information. Once a request is validated and approved, the certificate will be issued with extended validity. Since subject alternative names can be removed during a renewal, we require that you provide the subject alternative names you expect in the renewed certificate. New names added to a certificate that do not share the base domain of the common name may take additional time to validate. &lt;/p&gt;

    :param certificate_id: Certificate id to renew
    :type certificate_id: str
    :param body: The renew request info
    :type body: dict | bytes

    """
    body = CertificateRenew.from_dict(body)
    return web.Response(status=200)


async def certificate_resend_email(request: web.Request, certificate_id, email_id) -> web.Response:
    """Resend an email

    This method can be used to resend emails by providing the certificate id and the email id

    :param certificate_id: Certificate id to resend email
    :type certificate_id: str
    :param email_id: Email id for email to resend
    :type email_id: str

    """
    return web.Response(status=200)


async def certificate_resend_email_address(request: web.Request, certificate_id, email_id, email_address) -> web.Response:
    """Resend email to email address

    This method can be used to resend emails by providing the certificate id, the email id, and the recipient email address

    :param certificate_id: Certificate id to resend emails
    :type certificate_id: str
    :param email_id: Email id for email to resend
    :type email_id: str
    :param email_address: Specific email address to resend email
    :type email_address: str

    """
    return web.Response(status=200)


async def certificate_revoke(request: web.Request, certificate_id, body) -> web.Response:
    """Revoke active certificate

    Use revoke call to revoke an active certificate, if the certificate has not been issued a 404 response will be returned.

    :param certificate_id: Certificate id to revoke
    :type certificate_id: str
    :param body: The certificate revocation request
    :type body: dict | bytes

    """
    body = CertificateRevoke.from_dict(body)
    return web.Response(status=200)


async def certificate_siteseal_get(request: web.Request, certificate_id, theme=None, locale=None) -> web.Response:
    """Get Site seal

    &lt;p&gt;This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted on the reseller&#39;s website, to minimize delays for customer page load times.&lt;/p&gt;

    :param certificate_id: Certificate id
    :type certificate_id: str
    :param theme: This value represents the visual theme of the seal. If seal doesn&#39;t exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present.
    :type theme: str
    :param locale: Determine locale for text displayed in seal image and verification page. If seal doesn&#39;t exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present.
    :type locale: str

    """
    return web.Response(status=200)


async def certificate_validate(request: web.Request, body, x_market_id=None) -> web.Response:
    """Validate a pending order for certificate

    

    :param body: The certificate order info
    :type body: dict | bytes
    :param x_market_id: Setting locale for communications such as emails and error messages
    :type x_market_id: str

    """
    body = CertificateCreate.from_dict(body)
    return web.Response(status=200)


async def certificate_verifydomaincontrol(request: web.Request, certificate_id) -> web.Response:
    """Check Domain Control

    Domain control is a means for verifying the domain included in the certificate order. This resource is useful for resellers that control the domains for their customers, and can expedite the verification process. See https://www.godaddy.com/help/verifying-your-domain-ownership-for-ssl-certificate-requests-html-or-dns-7452

    :param certificate_id: Certificate id to lookup
    :type certificate_id: str

    """
    return web.Response(status=200)
