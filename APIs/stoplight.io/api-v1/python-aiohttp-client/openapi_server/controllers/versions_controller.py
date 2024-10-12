from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_versions_version_id_export_format200_response import GETVersionsVersionIdExportFormat200Response
from openapi_server.models.post_versions_version_id_publish200_response import POSTVersionsVersionIdPublish200Response
from openapi_server.models.put_versions_version_id_import200_response import PUTVersionsVersionIdImport200Response
from openapi_server.models.put_versions_version_id_import_request import PUTVersionsVersionIdImportRequest
from openapi_server.models.put_versions_version_id_unpublish200_response import PUTVersionsVersionIdUnpublish200Response
from openapi_server import util


async def g_et_versions_version_id_export_format(request: web.Request, version_id, format) -> web.Response:
    """Export

    Export a version to your choice of API specification.  ### Allowed Formats:  - oas.json - oas.yaml - raml08.yaml - raml10.yaml - stoplight.json - stoplight.yaml  The stoplight format actually returns OAS (Swagger 2) with x-stoplight annotations. If you are exporting with the intent on importing back into Stoplight, this export format preserves the most information.  ### Example URL:  &#x60;https://api.stoplight.io/v1/versions/123/export/oas.json&#x60;

    :param version_id: This is the unique identifier for the version.
    :type version_id: str
    :param format: The specification / format that you want to export.
    :type format: str

    """
    return web.Response(status=200)


async def p_ost_versions_version_id_publish(request: web.Request, version_id) -> web.Response:
    """Publish

    Re-publish an API version in Stoplight. This will re-publish the given API version, with whatever publish settings have already been setup in the app.  This will only work with APIs that have previously been published at least once.  This works well with the #endpoint:957qEfc97BB5XGAeZ endpoint to augment your continuous integration processes, and automatically re-publish your documentation when certain events happen. Once such scenario is:  1. Swagger is generated from your codebase, and pushed up to Github. 2. A simple script that you write sends a request to the Stoplight API to import the new specification, passing in the URL to the swagger file on Github. 3. After the import succeeds, and your API in Stoplight is up to date, the script sends a request to the Stoplight API (this endpoint) to re-publish your documentation.

    :param version_id: This is the unique identifier for the version.
    :type version_id: str

    """
    return web.Response(status=200)


async def p_ut_versions_version_id_import(request: web.Request, version_id, body=None) -> web.Response:
    """Import

    Import the given specification into an existing version.   **Warning, this is a destructive action! Any resources present in both the existing version, and the specification being imported, will be overwritten.**  This endpoint is particularly useful when you manage a specification file (Swagger or RAML) outside of Stoplight, and want to keep your Stoplight API version up to date as that specification changes.  By default, a \&quot;merge\&quot; is performed when importing. If a resource exists in the specification that you are importing, and in the Stoplight API, the resource will be overwritten. If a resource exists in the Stoplight API, but not in the spefication that you are importing, the resource will be left alone (and not deleted).  You can include an optional &#x60;options&#x60; property in the request body, to indicate if you would like to perform more of a replacement (instead of a merge). The options are documented in full in the response definition below these notes.  Take this request + request body for example:  &#x60;PUT https://api.stoplight.io/v1/versions/123/import&#x60; &#x60;&#x60;&#x60;json {   \&quot;url\&quot;: \&quot;http://petstore.swagger.io/v2/swagger.json\&quot;,   \&quot;options\&quot;: {     \&quot;removeExtraEndpoints\&quot;: true,     \&quot;removeExtraSchemas\&quot;: true   } } &#x60;&#x60;&#x60;  This request will grab the swagger specification described at &#x60;http://petstore.swagger.io/v2/swagger.json&#x60;, and import it into the Stoplight API version with id &#x60;123&#x60;. Additionally, it will delete any existing endpoints or models that are not described in the petstore swagger being imported.  Instead of a URL, you can provide the actual specification to be imported, either as a string (in the case of YAML) or an object (in the case of JSON). That request would look something like this:  &#x60;PUT https://api.stoplight.io/v1/versions/123/import&#x60; &#x60;&#x60;&#x60;json {   \&quot;specData\&quot;: {     \&quot;swagger\&quot;: \&quot;2.0\&quot;,     \&quot;info\&quot;: {}     ... rest of spec   } } &#x60;&#x60;&#x60;

    :param version_id: This is the unique identifier for the version.
    :type version_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PUTVersionsVersionIdImportRequest.from_dict(body)
    return web.Response(status=200)


async def p_ut_versions_version_id_unpublish(request: web.Request, version_id) -> web.Response:
    """Unpublish

    Unpublish the documentation associated with the given API version.

    :param version_id: This is the unique identifier for the version.
    :type version_id: str

    """
    return web.Response(status=200)
