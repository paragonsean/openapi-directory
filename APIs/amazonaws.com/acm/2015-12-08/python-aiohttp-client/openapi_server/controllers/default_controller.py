from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tags_to_certificate_request import AddTagsToCertificateRequest
from openapi_server.models.delete_certificate_request import DeleteCertificateRequest
from openapi_server.models.describe_certificate_request import DescribeCertificateRequest
from openapi_server.models.describe_certificate_response import DescribeCertificateResponse
from openapi_server.models.export_certificate_request import ExportCertificateRequest
from openapi_server.models.export_certificate_response import ExportCertificateResponse
from openapi_server.models.get_account_configuration_response import GetAccountConfigurationResponse
from openapi_server.models.get_certificate_request import GetCertificateRequest
from openapi_server.models.get_certificate_response import GetCertificateResponse
from openapi_server.models.import_certificate_request import ImportCertificateRequest
from openapi_server.models.import_certificate_response import ImportCertificateResponse
from openapi_server.models.list_certificates_request import ListCertificatesRequest
from openapi_server.models.list_certificates_response import ListCertificatesResponse
from openapi_server.models.list_tags_for_certificate_request import ListTagsForCertificateRequest
from openapi_server.models.list_tags_for_certificate_response import ListTagsForCertificateResponse
from openapi_server.models.put_account_configuration_request import PutAccountConfigurationRequest
from openapi_server.models.remove_tags_from_certificate_request import RemoveTagsFromCertificateRequest
from openapi_server.models.renew_certificate_request import RenewCertificateRequest
from openapi_server.models.request_certificate_request import RequestCertificateRequest
from openapi_server.models.request_certificate_response import RequestCertificateResponse
from openapi_server.models.resend_validation_email_request import ResendValidationEmailRequest
from openapi_server.models.update_certificate_options_request import UpdateCertificateOptionsRequest
from openapi_server import util


async def add_tags_to_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_tags_to_certificate

    &lt;p&gt;Adds one or more tags to an ACM certificate. Tags are labels that you can use to identify and organize your Amazon Web Services resources. Each tag consists of a &lt;code&gt;key&lt;/code&gt; and an optional &lt;code&gt;value&lt;/code&gt;. You specify the certificate on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair. &lt;/p&gt; &lt;p&gt;You can apply a tag to just one certificate if you want to identify a specific characteristic of that certificate, or you can apply the same tag to multiple certificates if you want to filter for a common relationship among those certificates. Similarly, you can apply the same tag to multiple resources if you want to specify a relationship among those resources. For example, you can add the same tag to an ACM certificate and an Elastic Load Balancing load balancer to indicate that they are both used by the same website. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/tags.html\&quot;&gt;Tagging ACM certificates&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;To remove one or more tags, use the &lt;a&gt;RemoveTagsFromCertificate&lt;/a&gt; action. To view all of the tags that have been applied to the certificate, use the &lt;a&gt;ListTagsForCertificate&lt;/a&gt; action. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AddTagsToCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_certificate

    &lt;p&gt;Deletes a certificate and its associated private key. If this action succeeds, the certificate no longer appears in the list that can be displayed by calling the &lt;a&gt;ListCertificates&lt;/a&gt; action or be retrieved by calling the &lt;a&gt;GetCertificate&lt;/a&gt; action. The certificate will not be available for use by Amazon Web Services services integrated with ACM. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete an ACM certificate that is being used by another Amazon Web Services service. To delete a certificate that is in use, the certificate association must first be removed.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def describe_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_certificate

    &lt;p&gt;Returns detailed metadata about the specified ACM certificate.&lt;/p&gt; &lt;p&gt;If you have just created a certificate using the &lt;code&gt;RequestCertificate&lt;/code&gt; action, there is a delay of several seconds before you can retrieve information about it.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def export_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """export_certificate

    &lt;p&gt;Exports a private certificate issued by a private certificate authority (CA) for use anywhere. The exported file contains the certificate, the certificate chain, and the encrypted private 2048-bit RSA key associated with the public key that is embedded in the certificate. For security, you must assign a passphrase for the private key when exporting it. &lt;/p&gt; &lt;p&gt;For information about exporting and formatting a certificate using the ACM console or CLI, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-export-private.html\&quot;&gt;Export a Private Certificate&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ExportCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def get_account_configuration(request: web.Request, x_amz_target, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_configuration

    Returns the account configuration options associated with an Amazon Web Services account.

    :param x_amz_target: 
    :type x_amz_target: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_certificate

    Retrieves an Amazon-issued certificate and its certificate chain. The chain consists of the certificate of the issuing CA and the intermediate certificates of any other subordinate CAs. All of the certificates are base64 encoded. You can use &lt;a href&#x3D;\&quot;https://wiki.openssl.org/index.php/Command_Line_Utilities\&quot;&gt;OpenSSL&lt;/a&gt; to decode the certificates and inspect individual fields.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def import_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """import_certificate

    &lt;p&gt;Imports a certificate into Certificate Manager (ACM) to use with services that are integrated with ACM. Note that &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html\&quot;&gt;integrated services&lt;/a&gt; allow only certificate types and keys they support to be associated with their resources. Further, their support differs depending on whether the certificate is imported into IAM or into ACM. For more information, see the documentation for each service. For more information about importing certificates into ACM, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\&quot;&gt;Importing Certificates&lt;/a&gt; in the &lt;i&gt;Certificate Manager User Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;ACM does not provide &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html\&quot;&gt;managed renewal&lt;/a&gt; for certificates that you import.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Note the following guidelines when importing third party certificates:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must enter the private key that matches the certificate you are importing.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The private key must be unencrypted. You cannot import a private key that is protected by a password or a passphrase.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The private key must be no larger than 5 KB (5,120 bytes).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the certificate you are importing is not self-signed, you must enter its certificate chain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If a certificate chain is included, the issuer must be the subject of one of the certificates in the chain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The certificate, private key, and certificate chain must be PEM-encoded.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The current time must be between the &lt;code&gt;Not Before&lt;/code&gt; and &lt;code&gt;Not After&lt;/code&gt; certificate fields.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Issuer&lt;/code&gt; field must not be empty.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The OCSP authority URL, if present, must not exceed 1000 characters.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To import a new certificate, omit the &lt;code&gt;CertificateArn&lt;/code&gt; argument. Include this argument only when you want to replace a previously imported certificate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you import a certificate by using the CLI, you must specify the certificate, the certificate chain, and the private key by their file names preceded by &lt;code&gt;fileb://&lt;/code&gt;. For example, you can specify a certificate saved in the &lt;code&gt;C:\\temp&lt;/code&gt; folder as &lt;code&gt;fileb://C:\\temp\\certificate_to_import.pem&lt;/code&gt;. If you are making an HTTP or HTTPS Query request, include these arguments as BLOBs. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you import a certificate by using an SDK, you must specify the certificate, the certificate chain, and the private key files in the manner required by the programming language you&#39;re using. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The cryptographic algorithm of an imported certificate must match the algorithm of the signing CA. For example, if the signing CA key type is RSA, then the certificate key type must also be RSA.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation returns the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the imported certificate.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ImportCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def list_certificates(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, next_token=None) -> web.Response:
    """list_certificates

    Retrieves a list of certificate ARNs and domain names. You can request that only certificates that match a specific status be listed. You can also filter by specific attributes of the certificate. Default filtering returns only &lt;code&gt;RSA_2048&lt;/code&gt; certificates. For more information, see &lt;a&gt;Filters&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_items: Pagination limit
    :type max_items: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListCertificatesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_certificate

    Lists the tags that have been applied to the ACM certificate. Use the certificate&#39;s Amazon Resource Name (ARN) to specify the certificate. To add a tag to an ACM certificate, use the &lt;a&gt;AddTagsToCertificate&lt;/a&gt; action. To delete a tag, use the &lt;a&gt;RemoveTagsFromCertificate&lt;/a&gt; action. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListTagsForCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_configuration

    &lt;p&gt;Adds or modifies account-level configurations in ACM. &lt;/p&gt; &lt;p&gt;The supported configuration option is &lt;code&gt;DaysBeforeExpiry&lt;/code&gt;. This option specifies the number of days prior to certificate expiration when ACM starts generating &lt;code&gt;EventBridge&lt;/code&gt; events. ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def remove_tags_from_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_tags_from_certificate

    &lt;p&gt;Remove one or more tags from an ACM certificate. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this function, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value. &lt;/p&gt; &lt;p&gt;To add tags to a certificate, use the &lt;a&gt;AddTagsToCertificate&lt;/a&gt; action. To view all of the tags that have been applied to a specific ACM certificate, use the &lt;a&gt;ListTagsForCertificate&lt;/a&gt; action. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RemoveTagsFromCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def renew_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """renew_certificate

    Renews an eligible ACM certificate. At this time, only exported private certificates can be renewed with this operation. In order to renew your Amazon Web Services Private CA certificates with ACM, you must first &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/PcaPermissions.html\&quot;&gt;grant the ACM service principal permission to do so&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/manual-renewal.html\&quot;&gt;Testing Managed Renewal&lt;/a&gt; in the ACM User Guide.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RenewCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def request_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """request_certificate

    &lt;p&gt;Requests an ACM certificate for use with other Amazon Web Services services. To request an ACM certificate, you must specify a fully qualified domain name (FQDN) in the &lt;code&gt;DomainName&lt;/code&gt; parameter. You can also specify additional FQDNs in the &lt;code&gt;SubjectAlternativeNames&lt;/code&gt; parameter. &lt;/p&gt; &lt;p&gt;If you are requesting a private certificate, domain validation is not required. If you are requesting a public certificate, each domain name that you specify must be validated to verify that you own or control the domain. You can use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html\&quot;&gt;DNS validation&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html\&quot;&gt;email validation&lt;/a&gt;. We recommend that you use DNS validation. ACM issues public certificates after receiving approval from the domain owner. &lt;/p&gt; &lt;note&gt; &lt;p&gt;ACM behavior differs from the &lt;a href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc6125#appendix-B.2\&quot;&gt;RFC 6125&lt;/a&gt; specification of the certificate validation process. ACM first checks for a Subject Alternative Name, and, if it finds one, ignores the common name (CN).&lt;/p&gt; &lt;/note&gt; &lt;p&gt;After successful completion of the &lt;code&gt;RequestCertificate&lt;/code&gt; action, there is a delay of several seconds before you can retrieve information about the new certificate.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RequestCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def resend_validation_email(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resend_validation_email

    Resends the email that requests domain ownership validation. The domain owner or an authorized representative must approve the ACM certificate before it can be issued. The certificate can be approved by clicking a link in the mail to navigate to the Amazon certificate approval website and then clicking &lt;b&gt;I Approve&lt;/b&gt;. However, the validation email can be blocked by spam filters. Therefore, if you do not receive the original mail, you can request that the mail be resent within 72 hours of requesting the ACM certificate. If more than 72 hours have elapsed since your original request or since your last attempt to resend validation mail, you must request a new certificate. For more information about setting up your contact email addresses, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/setup-email.html\&quot;&gt;Configure Email for your Domain&lt;/a&gt;. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ResendValidationEmailRequest.from_dict(body)
    return web.Response(status=200)


async def update_certificate_options(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_certificate_options

    Updates a certificate. Currently, you can use this function to specify whether to opt in to or out of recording your certificate in a certificate transparency log. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency\&quot;&gt; Opting Out of Certificate Transparency Logging&lt;/a&gt;. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateCertificateOptionsRequest.from_dict(body)
    return web.Response(status=200)
