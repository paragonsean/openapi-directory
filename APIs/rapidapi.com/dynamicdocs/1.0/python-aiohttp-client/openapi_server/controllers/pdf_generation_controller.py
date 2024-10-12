from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def compile(request: web.Request, template_token, content_type, doc_url_expires_in=None, latex_compiler=None, latex_runs_=None, main_file_name=None, doc_file_name=None, body=None) -> web.Response:
    """Compile New Document PDF

    Compile a PDF document from a specific template

    :param template_token: The template-token is available in your template settings after publishing your template.
    :type template_token: str
    :param content_type: Should be set to \&quot;application/json\&quot;
    :type content_type: str
    :param doc_url_expires_in: The doc-url-expires-in is a numerical parameter which takes integers and describes after how many seconds the provided URL is available to download the document.
    :type doc_url_expires_in: int
    :param latex_compiler: The latex-compiler parameter can take the following values:  pdflatex lualatex
    :type latex_compiler: str
    :param latex_runs_: The latex-runs is a numerical parameter and can take values of 1, 2 and 3. 
    :type latex_runs_: int
    :param main_file_name: The main-file-name is a string parameter which identifies the main file to compile.
    :type main_file_name: str
    :param doc_file_name: The doc-file-name is a string parameter which determines the name of the file. Note that the extension of the file is not required.
    :type doc_file_name: str
    :param body: Post the dynamic data for the template to compile the document PDF.
    :type body: 

    """
    return web.Response(status=200)
