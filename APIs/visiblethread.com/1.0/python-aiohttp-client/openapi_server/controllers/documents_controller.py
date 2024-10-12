from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_list_summary import DocumentListSummary
from openapi_server.models.document_response_detailed import DocumentResponseDetailed
from openapi_server.models.document_response_not_ready import DocumentResponseNotReady
from openapi_server.models.new_document_response import NewDocumentResponse
from openapi_server.models.search import Search
from openapi_server import util


async def dictionaries_get(request: web.Request, ) -> web.Response:
    """Get your list of dictionaries

    Get your list of dictionaries


    """
    return web.Response(status=200)


async def documents_get(request: web.Request, ) -> web.Response:
    """Get your list of documents

    Get your list of documents


    """
    return web.Response(status=200)


async def get_doc_by_id(request: web.Request, doc_id) -> web.Response:
    """Get data from a previously submitted document

    Get data from a previously submitted document identified by ***docId***

    :param doc_id: Id of document to fetch
    :type doc_id: int

    """
    return web.Response(status=200)


async def get_search_results(request: web.Request, doc_id, dictionary_id, matching_only) -> web.Response:
    """Gets search results for a particular document/dictionary

    Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** &amp; **urlId**

    :param doc_id: Id of document
    :type doc_id: int
    :param dictionary_id: Id of dictionary
    :type dictionary_id: int
    :param matching_only: Only returning paragraphs containing a match
    :type matching_only: bool

    """
    return web.Response(status=200)


async def run_search(request: web.Request, body) -> web.Response:
    """Run a search

    Run a search on document **docId** using dictionary **dictId** 

    :param body: Run a search on document **docId** using dictionary**dictId**
    :type body: dict | bytes

    """
    body = Search.from_dict(body)
    return web.Response(status=200)


async def searches_get(request: web.Request, ) -> web.Response:
    """Get your list of searches

    Get your list of searches


    """
    return web.Response(status=200)


async def upload_dictionary(request: web.Request, file) -> web.Response:
    """Upload a dictionary (CSV)

    Upload a dictionary (CSV format) to your VisibleThread account. 

    :param file: The uploaded CSV dictionary
    :type file: str

    """
    return web.Response(status=200)


async def upload_doc(request: web.Request, file, long_sentence_word_count=None, very_long_sentence_word_count=None) -> web.Response:
    """Upload a document

    Upload a document to your VisibleThread account.  We return a JSON response that contains a \&quot;docId\&quot; that represents your document.         You can use this id in other requests to check on the analysis status for the document and run a dictionary search and retrieve search results. 

    :param file: The uploaded file data
    :type file: str
    :param long_sentence_word_count: Optional setting what constitutes a long sentence (default 25)
    :type long_sentence_word_count: int
    :param very_long_sentence_word_count: Optional setting what constitutes a very long sentence (default 30)
    :type very_long_sentence_word_count: int

    """
    return web.Response(status=200)
