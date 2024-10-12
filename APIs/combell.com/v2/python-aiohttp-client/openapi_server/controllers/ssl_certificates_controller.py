from typing import List, Dict
from aiohttp import web

from openapi_server.models.ssl_certificate import SslCertificate
from openapi_server.models.ssl_certificate_detail import SslCertificateDetail
from openapi_server.models.ssl_certificate_file_format import SslCertificateFileFormat
from openapi_server import util


async def download_certificate(request: web.Request, sha1_fingerprint, file_format, password, sha1_fingerprint2) -> web.Response:
    """Download a SSL certificate

    Returns the certifcate as binary data with the content-type and the filename information in the response headers.

    :param sha1_fingerprint: The SHA-1 fingerprint of the certificate.
    :type sha1_fingerprint: str
    :param file_format: The file format of the returned file stream:  &lt;ul&gt;&lt;li&gt;PFX: Also known as PKCS #12, is a single, password protected certificate archive that contains the entire certificate chain plus the matching private key.&lt;/li&gt;&lt;/ul&gt;
    :type file_format: dict | bytes
    :param password: The password used to protect the certificate file.&lt;br /&gt;
    :type password: str
    :param sha1_fingerprint2: Automatically added
    :type sha1_fingerprint2: str

    """
    file_format = .from_dict(file_format)
    return web.Response(status=200)


async def get_ssl_certificate(request: web.Request, sha1_fingerprint, sha1_fingerprint2) -> web.Response:
    """Detail of a SSL certificate

    

    :param sha1_fingerprint: The SHA-1 fingerprint of the certificate.
    :type sha1_fingerprint: str
    :param sha1_fingerprint2: Automatically added
    :type sha1_fingerprint2: str

    """
    return web.Response(status=200)


async def get_ssl_certificates(request: web.Request, skip=None, take=None) -> web.Response:
    """Overview of SSL certificates

    

    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int

    """
    return web.Response(status=200)
