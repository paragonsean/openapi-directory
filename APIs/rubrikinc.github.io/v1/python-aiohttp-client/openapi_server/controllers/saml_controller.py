from typing import List, Dict
from aiohttp import web

from openapi_server.models.rubrik_saml_metadata_info import RubrikSamlMetadataInfo
from openapi_server.models.rubrik_saml_metadata_summary import RubrikSamlMetadataSummary
from openapi_server.models.saml_sso_authn_request_detail import SamlSsoAuthnRequestDetail
from openapi_server.models.saml_sso_authn_request_info import SamlSsoAuthnRequestInfo
from openapi_server.models.saml_sso_status import SamlSsoStatus
from openapi_server import util


async def config_rubrik_saml_metadata(request: web.Request, body) -> web.Response:
    """Configure and generate Rubrik SAML metadata

    Configure and generate the SAML metadata for this Rubrik cluster. The call returns the download URL for the metadata.

    :param body: Information for generating Rubrik SAML metadata file.
    :type body: dict | bytes

    """
    body = RubrikSamlMetadataInfo.from_dict(body)
    return web.Response(status=200)


async def get_saml_sso_status(request: web.Request, ) -> web.Response:
    """Check SAML SSO Status

    An object that contains two values. A Boolean value that determines whether or not SSO is enabled and an optional String value that indicates the name of the default IdP authentication domain for SSO login. When the boolean value is &#39;true,&#39; SAML SSO is enabled. When the Boolean value is &#39;false,&#39; SAML SSO is disabled.


    """
    return web.Response(status=200)


async def make_saml_authn_request(request: web.Request, idp_name, body=None) -> web.Response:
    """Make SAML authentication request

    Make a SAML authentication request for a specified IdP Authentication Domain.

    :param idp_name: Name of the IdP Authentication Domain to authenticate with.
    :type idp_name: str
    :param body: Additional information associated with a single sign-on (SSO) authentication request.
    :type body: dict | bytes

    """
    body = SamlSsoAuthnRequestInfo.from_dict(body)
    return web.Response(status=200)
