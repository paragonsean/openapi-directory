from typing import List, Dict
from aiohttp import web

from openapi_server.models.article_history_response import ArticleHistoryResponse
from openapi_server.models.article_response import ArticleResponse
from openapi_server.models.article_search_response import ArticleSearchResponse
from openapi_server.models.article_similar_response import ArticleSimilarResponse
from openapi_server.models.search_request import SearchRequest
from openapi_server.models.similar_request import SimilarRequest
from openapi_server import util


async def get_article_by_core_id(request: web.Request, core_id, metadata=None, fulltext=None, citations=None, similar=None, duplicate=None, urls=None, faithful_metadata=None) -> web.Response:
    """Get article by CORE ID

    Method will retrieve an article based on given CORE ID.

    :param core_id: CORE ID of the article that needs to be fetched.
    :type core_id: int
    :param metadata: Whether to retrieve the full article metadata or only the ID. The default value is true.
    :type metadata: bool
    :param fulltext: Whether to retrieve full text of the article. The default value is false
    :type fulltext: bool
    :param citations: Whether to retrieve citations found in the article. The default value is false
    :type citations: bool
    :param similar: Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    :type similar: bool
    :param duplicate: Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
    :type duplicate: bool
    :param urls: Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
    :type urls: bool
    :param faithful_metadata: Returns the records raw XML metadata from the original repository. The default value is false
    :type faithful_metadata: bool

    """
    return web.Response(status=200)


async def get_article_by_core_id_batch(request: web.Request, body, metadata=None, fulltext=None, citations=None, similar=None, duplicate=None, urls=None, faithful_metadata=None) -> web.Response:
    """Batch operation for retrieving articles by CORE ID

    Method accepts a JSON array of CORE IDs and retrieves a list of articles. The response array is ordered based on the order of the IDs in the request array.

    :param body: JSON array with CORE IDs of articles that need to be fetched
    :type body: List[int]
    :param metadata: Whether to retrieve the full article metadata or only the IDs. The default value is true
    :type metadata: bool
    :param fulltext: Whether to retrieve fulltexts of the articles. The default value is false
    :type fulltext: bool
    :param citations: Whether to retrieve citations found in the articles. The default value is false
    :type citations: bool
    :param similar: Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    :type similar: bool
    :param duplicate: Whether to retrieve CORE IDs of different versions of the articles. The default value is false
    :type duplicate: bool
    :param urls: Whether to retrieve lists of URLs of the article fulltexts. The default value is false
    :type urls: bool
    :param faithful_metadata: Returns the records raw XML metadata from the original repository. The default value is false
    :type faithful_metadata: bool

    """
    return web.Response(status=200)


async def get_article_history_by_core_id(request: web.Request, core_id, page=None, page_size=None) -> web.Response:
    """Get article history by CORE ID

    Method accepts a single CORE ID and returns a list of all historical versions of the article, which are stored in CORE database. The results are ordered from the newest one to the oldest one.

    :param core_id: CORE ID of the article which history should be fetched
    :type core_id: str
    :param page: Which page of the history results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    :type page: int
    :param page_size: The number of results to return per page. Can be any number between 10 and 100, default is 10.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_article_pdf_by_core_id(request: web.Request, core_id) -> web.Response:
    """Get fulltext PDF by CORE ID

    Method will retrieve an article based on given CORE ID.

    :param core_id: ID of article history that needs to be fetched
    :type core_id: str

    """
    return web.Response(status=200)


async def near_duplicate_articles(request: web.Request, doi=None, title=None, year=None, description=None, fulltext=None, identifier=None, repository_id=None) -> web.Response:
    """Get all near duplicate articles

    Method accepts values for several parameters and retrieves a JSON array of articles which have near duplicate content matching the input parameters&#39; values. The response array contains ids of the near duplicate articles along with their relevance scores.

    :param doi: The DOI for which the duplicates will be identified
    :type doi: str
    :param title: Title to match when looking for duplicate articles. Only useful when either value for @year or @description is supplied.
    :type title: str
    :param year: Year the article was published. Only useful when value for @title is supplied. 
    :type year: str
    :param description: Abstract for an article based on which its duplicates will be found. Only useful when value for @title is supplied.
    :type description: str
    :param fulltext: Full text for an article based on which its duplicates will be found.
    :type fulltext: str
    :param identifier: Article identifier for which the duplicates will be identified. Only useful when either values for @doi or (@title and @year) or (@title and @abstract) or @fulltext are supplied.
    :type identifier: str
    :param repository_id: Limit the duplicates search to particular repository id. 
    :type repository_id: str

    """
    return web.Response(status=200)


async def search_articles(request: web.Request, query, page=None, page_size=None, metadata=None, fulltext=None, citations=None, similar=None, duplicate=None, urls=None, faithful_metadata=None) -> web.Response:
    """Search through all documents

    Searches through all articles and returns a JSON array with search results. Method searches through all article fields.

    :param query: The search query
    :type query: int
    :param page: Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    :type page: int
    :param page_size: The number of results to return per page. Can be any number between 10 and 100, default is 10.
    :type page_size: int
    :param metadata: Whether to retrieve the full article metadata or only the ID. The default value is true.
    :type metadata: bool
    :param fulltext: Whether to retrieve full text of the article. The default value is false
    :type fulltext: bool
    :param citations: Whether to retrieve citations found in the article. The default value is false
    :type citations: bool
    :param similar: Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    :type similar: bool
    :param duplicate: Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
    :type duplicate: bool
    :param urls: Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
    :type urls: bool
    :param faithful_metadata: Returns the records raw XML metadata from the original repository. The default value is false
    :type faithful_metadata: bool

    """
    return web.Response(status=200)


async def search_articles_batch(request: web.Request, body, metadata=None, fulltext=None, citations=None, similar=None, duplicate=None, urls=None, faithful_metadata=None) -> web.Response:
    """Batch operation for search through articles

    Method accepts a JSON array of search queries and parameters. It then searches through all articles and returns a JSON array of search results for each of the queries. Method searches through all article fields (title, authors, subjects, identifiers, etc.).

    :param body: JSON array with search queries and parameters. One request can contain up to 100 queries
    :type body: list | bytes
    :param metadata: Whether to retrieve the full article metadata or only the ID. The default value is true.
    :type metadata: bool
    :param fulltext: Whether to retrieve full text of the article. The default value is false
    :type fulltext: bool
    :param citations: Whether to retrieve citations found in the article. The default value is false
    :type citations: bool
    :param similar: Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    :type similar: bool
    :param duplicate: Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
    :type duplicate: bool
    :param urls: Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
    :type urls: bool
    :param faithful_metadata: Whether to retrieve the raw XML metadata of the article. The default value is false
    :type faithful_metadata: bool

    """
    body = [SearchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def similar_articles(request: web.Request, body, limit=None, metadata=None, fulltext=None, citations=None, similar=None, duplicate=None, urls=None, faithful_metadata=None) -> web.Response:
    """Get articles by similarity to a text

    Method accepts a text and retrieves a JSON array of articles which are similar to the given text. The response array is ordered based on similarity score, starting from the most similar.

    :param body: The text that requires similar articles to be calculated on
    :type body: dict | bytes
    :param limit: How many similar articles to retrieve at most. Can be any number betwen 1 and 100, default is 10
    :type limit: int
    :param metadata: Whether to retrieve the full article metadata or only the IDs of the similar articles. The default value is true
    :type metadata: bool
    :param fulltext: Whether to retrieve fulltexts of the similar articles. The default value is false
    :type fulltext: bool
    :param citations: Whether to retrieve citations found in the articles. The default value is false
    :type citations: bool
    :param similar: Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    :type similar: bool
    :param duplicate: Whether to retrieve CORE IDs of different versions of the articles. The default value is false
    :type duplicate: bool
    :param urls: Whether to retrieve lists of URLs of the article fulltexts. The default value is false
    :type urls: bool
    :param faithful_metadata: Whether to retrieve the raw XML metadata of the articles. The default value is false
    :type faithful_metadata: bool

    """
    body = SimilarRequest.from_dict(body)
    return web.Response(status=200)
