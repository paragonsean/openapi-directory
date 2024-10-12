from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_data_inner import BatchDataInner
from openapi_server.models.data import Data
from openapi_server.models.get_templates401_response import GetTemplates401Response
from openapi_server.models.get_templates403_response import GetTemplates403Response
from openapi_server.models.get_templates404_response import GetTemplates404Response
from openapi_server.models.get_templates422_response import GetTemplates422Response
from openapi_server.models.get_templates500_response import GetTemplates500Response
from openapi_server.models.merge_templates200_response import MergeTemplates200Response
from openapi_server import util


async def merge_template(request: web.Request, template_id, body, name=None, format=None, output=None) -> web.Response:
    """Generate document

    Merges template with data and returns base64 encoded document or a public URL to a document. You can send json encoded data in request body or a public URL to your json file as the data parameter. NB! When the public URL option is used, the document is stored for 30 days and automatically deleted.

    :param template_id: Template unique identifier
    :type template_id: int
    :param body: Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file.
    :type body: dict | bytes
    :param name: Document name, returned in the meta data.
    :type name: str
    :param format: Document format. The zip option will return a ZIP file with PDF files.
    :type format: str
    :param output: Response format. With the url option, the document is stored for 30 days and automatically deleted.
    :type output: str

    """
    body = Data.from_dict(body)
    return web.Response(status=200)


async def merge_templates(request: web.Request, body, name=None, format=None, output=None) -> web.Response:
    """Generate document (multiple templates)

    Allows to merge multiples template with data and returns base64 encoded document or public URL to a document. NB! When the public URL option is used, the document is stored for 30 days and automatically deleted.

    :param body: Data used to specify templates and data objects which are used to merge the template
    :type body: list | bytes
    :param name: Document name, returned in the meta data.
    :type name: str
    :param format: Document format. The zip option will return a ZIP file with PDF files.
    :type format: str
    :param output: Response format. With the url option, the document is stored for 30 days and automatically deleted.
    :type output: str

    """
    body = [BatchDataInner.from_dict(d) for d in body]
    return web.Response(status=200)
