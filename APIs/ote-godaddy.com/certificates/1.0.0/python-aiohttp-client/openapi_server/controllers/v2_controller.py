from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_detail_v2 import CertificateDetailV2
from openapi_server.models.certificate_summaries_v2 import CertificateSummariesV2
from openapi_server.models.domain_verification_detail import DomainVerificationDetail
from openapi_server.models.domain_verification_summary import DomainVerificationSummary
from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.external_account_binding import ExternalAccountBinding
from openapi_server import util


async def get_acme_external_account_binding(request: web.Request, customer_id) -> web.Response:
    """Retrieves the external account binding for the specified customer

    Use this endpoint to retrieve a key identifier and Hash-based Message Authentication Code (HMAC) key for Automated Certificate Management Environment (ACME) External Account Binding (EAB). These credentials can be used with an ACME client that supports EAB (ex. CertBot) to automate the issuance request and deployment of DV SSL certificates

    :param customer_id: An identifier for a customer
    :type customer_id: str

    """
    return web.Response(status=200)


async def get_certificate_detail_by_cert_identifier(request: web.Request, customer_id, certificate_id) -> web.Response:
    """Retrieve individual certificate details

    Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificate. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**. **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

    :param customer_id: An identifier for a customer
    :type customer_id: str
    :param certificate_id: Certificate id to lookup
    :type certificate_id: str

    """
    return web.Response(status=200)


async def get_customer_certificates_by_customer_id(request: web.Request, customer_id, offset=None, limit=None) -> web.Response:
    """Retrieve customer&#39;s certificates

    This method can be used to retrieve a list of certificates for a specified customer. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

    :param customer_id: An identifier for a customer
    :type customer_id: str
    :param offset: Number of results to skip for pagination
    :type offset: int
    :param limit: Maximum number of items to return
    :type limit: int

    """
    return web.Response(status=200)


async def get_domain_details_by_domain(request: web.Request, customer_id, certificate_id, domain) -> web.Response:
    """Retrieve detailed information for supplied domain

    Retrieve detailed information for supplied domain, including domain verification details and Certificate Authority Authorization (CAA) verification details. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

    :param customer_id: An identifier for a customer
    :type customer_id: str
    :param certificate_id: Certificate id to lookup
    :type certificate_id: str
    :param domain: A valid domain name in the certificate request
    :type domain: str

    """
    return web.Response(status=200)


async def get_domain_information_by_certificate_id(request: web.Request, customer_id, certificate_id) -> web.Response:
    """Retrieve domain verification status

    This method can be used to retrieve the domain verification status for a certificate request.&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;\&quot;

    :param customer_id: An identifier for a customer
    :type customer_id: str
    :param certificate_id: Certificate id to lookup
    :type certificate_id: str

    """
    return web.Response(status=200)
