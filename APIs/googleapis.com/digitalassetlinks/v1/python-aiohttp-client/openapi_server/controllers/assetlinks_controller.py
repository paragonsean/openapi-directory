from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_check_request import BulkCheckRequest
from openapi_server.models.bulk_check_response import BulkCheckResponse
from openapi_server.models.check_response import CheckResponse
from openapi_server import util


async def digitalassetlinks_assetlinks_bulk_check(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """digitalassetlinks_assetlinks_bulk_check

    Send a bundle of statement checks in a single RPC to minimize latency and service load. Statements need not be all for the same source and/or target. We recommend using this method when you need to check more than one statement in a short period of time.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = BulkCheckRequest.from_dict(body)
    return web.Response(status=200)


async def digitalassetlinks_assetlinks_check(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, relation=None, source_android_app_certificate_sha256_fingerprint=None, source_android_app_package_name=None, source_web_site=None, target_android_app_certificate_sha256_fingerprint=None, target_android_app_package_name=None, target_web_site=None) -> web.Response:
    """digitalassetlinks_assetlinks_check

    Determines whether the specified (directional) relationship exists between the specified source and target assets. The relation describes the intent of the link between the two assets as claimed by the source asset. An example for such relationships is the delegation of privileges or permissions. This command is most often used by infrastructure systems to check preconditions for an action. For example, a client may want to know if it is OK to send a web URL to a particular mobile app instead. The client can check for the relevant asset link from the website to the mobile app to decide if the operation should be allowed. A note about security: if you specify a secure asset as the source, such as an HTTPS website or an Android app, the API will ensure that any statements used to generate the response have been made in a secure way by the owner of that asset. Conversely, if the source asset is an insecure HTTP website (that is, the URL starts with &#x60;http://&#x60; instead of &#x60;https://&#x60;), the API cannot verify its statements securely, and it is not possible to ensure that the website&#39;s statements have not been altered by a third party. For more information, see the [Digital Asset Links technical design specification](https://github.com/google/digitalassetlinks/blob/master/well-known/details.md).

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param relation: Query string for the relation. We identify relations with strings of the format &#x60;/&#x60;, where &#x60;&#x60; must be one of a set of pre-defined purpose categories, and &#x60;&#x60; is a free-form lowercase alphanumeric string that describes the specific use case of the statement. Refer to [our API documentation](/digital-asset-links/v1/relation-strings) for the current list of supported relations. For a query to match an asset link, both the query&#39;s and the asset link&#39;s relation strings must match exactly. Example: A query with relation &#x60;delegate_permission/common.handle_all_urls&#x60; matches an asset link with relation &#x60;delegate_permission/common.handle_all_urls&#x60;.
    :type relation: str
    :param source_android_app_certificate_sha256_fingerprint: The uppercase SHA-265 fingerprint of the certificate. From the PEM certificate, it can be acquired like this: $ keytool -printcert -file $CERTFILE | grep SHA256: SHA256: 14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83: \\ 42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5 or like this: $ openssl x509 -in $CERTFILE -noout -fingerprint -sha256 SHA256 Fingerprint&#x3D;14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64: \\ 16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5 In this example, the contents of this field would be &#x60;14:6D:E9:83:C5:73: 06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF: 44:E5&#x60;. If these tools are not available to you, you can convert the PEM certificate into the DER format, compute the SHA-256 hash of that string and represent the result as a hexstring (that is, uppercase hexadecimal representations of each octet, separated by colons).
    :type source_android_app_certificate_sha256_fingerprint: str
    :param source_android_app_package_name: Android App assets are naturally identified by their Java package name. For example, the Google Maps app uses the package name &#x60;com.google.android.apps.maps&#x60;. REQUIRED
    :type source_android_app_package_name: str
    :param source_web_site: Web assets are identified by a URL that contains only the scheme, hostname and port parts. The format is http[s]://[:] Hostnames must be fully qualified: they must end in a single period (\&quot;&#x60;.&#x60;\&quot;). Only the schemes \&quot;http\&quot; and \&quot;https\&quot; are currently allowed. Port numbers are given as a decimal number, and they must be omitted if the standard port numbers are used: 80 for http and 443 for https. We call this limited URL the \&quot;site\&quot;. All URLs that share the same scheme, hostname and port are considered to be a part of the site and thus belong to the web asset. Example: the asset with the site &#x60;https://www.google.com&#x60; contains all these URLs: * &#x60;https://www.google.com/&#x60; * &#x60;https://www.google.com:443/&#x60; * &#x60;https://www.google.com/foo&#x60; * &#x60;https://www.google.com/foo?bar&#x60; * &#x60;https://www.google.com/foo#bar&#x60; * &#x60;https://user@password:www.google.com/&#x60; But it does not contain these URLs: * &#x60;http://www.google.com/&#x60; (wrong scheme) * &#x60;https://google.com/&#x60; (hostname does not match) * &#x60;https://www.google.com:444/&#x60; (port does not match) REQUIRED
    :type source_web_site: str
    :param target_android_app_certificate_sha256_fingerprint: The uppercase SHA-265 fingerprint of the certificate. From the PEM certificate, it can be acquired like this: $ keytool -printcert -file $CERTFILE | grep SHA256: SHA256: 14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83: \\ 42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5 or like this: $ openssl x509 -in $CERTFILE -noout -fingerprint -sha256 SHA256 Fingerprint&#x3D;14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64: \\ 16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5 In this example, the contents of this field would be &#x60;14:6D:E9:83:C5:73: 06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF: 44:E5&#x60;. If these tools are not available to you, you can convert the PEM certificate into the DER format, compute the SHA-256 hash of that string and represent the result as a hexstring (that is, uppercase hexadecimal representations of each octet, separated by colons).
    :type target_android_app_certificate_sha256_fingerprint: str
    :param target_android_app_package_name: Android App assets are naturally identified by their Java package name. For example, the Google Maps app uses the package name &#x60;com.google.android.apps.maps&#x60;. REQUIRED
    :type target_android_app_package_name: str
    :param target_web_site: Web assets are identified by a URL that contains only the scheme, hostname and port parts. The format is http[s]://[:] Hostnames must be fully qualified: they must end in a single period (\&quot;&#x60;.&#x60;\&quot;). Only the schemes \&quot;http\&quot; and \&quot;https\&quot; are currently allowed. Port numbers are given as a decimal number, and they must be omitted if the standard port numbers are used: 80 for http and 443 for https. We call this limited URL the \&quot;site\&quot;. All URLs that share the same scheme, hostname and port are considered to be a part of the site and thus belong to the web asset. Example: the asset with the site &#x60;https://www.google.com&#x60; contains all these URLs: * &#x60;https://www.google.com/&#x60; * &#x60;https://www.google.com:443/&#x60; * &#x60;https://www.google.com/foo&#x60; * &#x60;https://www.google.com/foo?bar&#x60; * &#x60;https://www.google.com/foo#bar&#x60; * &#x60;https://user@password:www.google.com/&#x60; But it does not contain these URLs: * &#x60;http://www.google.com/&#x60; (wrong scheme) * &#x60;https://google.com/&#x60; (hostname does not match) * &#x60;https://www.google.com:444/&#x60; (port does not match) REQUIRED
    :type target_web_site: str

    """
    return web.Response(status=200)
