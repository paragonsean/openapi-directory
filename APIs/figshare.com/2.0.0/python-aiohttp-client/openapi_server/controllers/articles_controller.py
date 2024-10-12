from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_report import AccountReport
from openapi_server.models.article import Article
from openapi_server.models.article_complete import ArticleComplete
from openapi_server.models.article_complete_private import ArticleCompletePrivate
from openapi_server.models.article_confidentiality import ArticleConfidentiality
from openapi_server.models.article_create import ArticleCreate
from openapi_server.models.article_doi import ArticleDOI
from openapi_server.models.article_embargo import ArticleEmbargo
from openapi_server.models.article_embargo_updater import ArticleEmbargoUpdater
from openapi_server.models.article_handle import ArticleHandle
from openapi_server.models.article_search import ArticleSearch
from openapi_server.models.article_update import ArticleUpdate
from openapi_server.models.article_versions import ArticleVersions
from openapi_server.models.article_with_project import ArticleWithProject
from openapi_server.models.author import Author
from openapi_server.models.authors_creator import AuthorsCreator
from openapi_server.models.categories_creator import CategoriesCreator
from openapi_server.models.category import Category
from openapi_server.models.confidentiality_creator import ConfidentialityCreator
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.file_creator import FileCreator
from openapi_server.models.file_id import FileId
from openapi_server.models.location import Location
from openapi_server.models.location_warnings import LocationWarnings
from openapi_server.models.location_warnings_update import LocationWarningsUpdate
from openapi_server.models.private_article_search import PrivateArticleSearch
from openapi_server.models.private_file import PrivateFile
from openapi_server.models.private_link import PrivateLink
from openapi_server.models.private_link_creator import PrivateLinkCreator
from openapi_server.models.private_link_response import PrivateLinkResponse
from openapi_server.models.public_file import PublicFile
from openapi_server.models.resource import Resource
from openapi_server import util


async def account_article_report(request: web.Request, group_id=None) -> web.Response:
    """Account Article Report

    Return status on all reports generated for the account from the oauth credentials

    :param group_id: A group ID to filter by
    :type group_id: int

    """
    return web.Response(status=200)


async def account_article_report_generate(request: web.Request, ) -> web.Response:
    """Initiate a new Report

    Initiate a new Article Report for this Account. There is a limit of 1 report per day.


    """
    return web.Response(status=200)


async def article_details(request: web.Request, article_id) -> web.Response:
    """View article details

    View an article

    :param article_id: Article Unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def article_file_details(request: web.Request, article_id, file_id) -> web.Response:
    """Article file details

    File by id

    :param article_id: Article Unique identifier
    :type article_id: int
    :param file_id: File Unique identifier
    :type file_id: int

    """
    return web.Response(status=200)


async def article_files(request: web.Request, article_id) -> web.Response:
    """List article files

    Files list for article

    :param article_id: Article Unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def article_version_confidentiality(request: web.Request, article_id, v_number) -> web.Response:
    """Public Article Confidentiality for article version

    Confidentiality for article version. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

    :param article_id: Article Unique identifier
    :type article_id: int
    :param v_number: Version Number
    :type v_number: int

    """
    return web.Response(status=200)


async def article_version_details(request: web.Request, article_id, v_number) -> web.Response:
    """Article details for version

    Article with specified version

    :param article_id: Article Unique identifier
    :type article_id: int
    :param v_number: Article Version Number
    :type v_number: int

    """
    return web.Response(status=200)


async def article_version_embargo(request: web.Request, article_id, v_number) -> web.Response:
    """Public Article Embargo for article version

    Embargo for article version

    :param article_id: Article Unique identifier
    :type article_id: int
    :param v_number: Version Number
    :type v_number: int

    """
    return web.Response(status=200)


async def article_version_update(request: web.Request, article_id, version_id, body) -> web.Response:
    """Update article version

    Updating an article version by passing body parameters; request can also be made with the PATCH method.

    :param article_id: Article unique identifier
    :type article_id: int
    :param version_id: Article version identifier
    :type version_id: int
    :param body: Article description
    :type body: dict | bytes

    """
    body = ArticleUpdate.from_dict(body)
    return web.Response(status=200)


async def article_version_update_thumb(request: web.Request, article_id, version_id, body) -> web.Response:
    """Update article version thumbnail

    For a given public article version update the article thumbnail by choosing one of the associated files

    :param article_id: Article unique identifier
    :type article_id: int
    :param version_id: Article version identifier
    :type version_id: int
    :param body: File ID
    :type body: dict | bytes

    """
    body = FileId.from_dict(body)
    return web.Response(status=200)


async def article_versions(request: web.Request, article_id) -> web.Response:
    """List article versions

    List public article versions

    :param article_id: Article Unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def articles_list(request: web.Request, x_cursor=None, page=None, page_size=None, limit=None, offset=None, order=None, order_direction=None, institution=None, published_since=None, modified_since=None, group=None, resource_doi=None, item_type=None, doi=None, handle=None) -> web.Response:
    """Public Articles

    Returns a list of public articles

    :param x_cursor: Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    :type x_cursor: str
    :type x_cursor: str
    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int
    :param order: The field by which to order. Default varies by endpoint/resource.
    :type order: str
    :param order_direction: 
    :type order_direction: str
    :param institution: only return articles from this institution
    :type institution: int
    :param published_since: Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    :type published_since: str
    :param modified_since: Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    :type modified_since: str
    :param group: only return articles from this group
    :type group: int
    :param resource_doi: only return articles with this resource_doi
    :type resource_doi: str
    :param item_type: Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model
    :type item_type: int
    :param doi: only return articles with this doi
    :type doi: str
    :param handle: only return articles with this handle
    :type handle: str

    """
    return web.Response(status=200)


async def articles_search(request: web.Request, x_cursor=None, body=None) -> web.Response:
    """Public Articles Search

    Returns a list of public articles, filtered by the search parameters

    :param x_cursor: Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    :type x_cursor: str
    :type x_cursor: str
    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = ArticleSearch.from_dict(body)
    return web.Response(status=200)


async def private_article_author_delete(request: web.Request, article_id, author_id) -> web.Response:
    """Delete article author

    De-associate author from article

    :param article_id: Article unique identifier
    :type article_id: int
    :param author_id: Article Author unique identifier
    :type author_id: int

    """
    return web.Response(status=200)


async def private_article_authors_add(request: web.Request, article_id, body) -> web.Response:
    """Add article authors

    Associate new authors with the article. This will add new authors to the list of already associated authors

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: Authors description
    :type body: dict | bytes

    """
    body = AuthorsCreator.from_dict(body)
    return web.Response(status=200)


async def private_article_authors_list(request: web.Request, article_id) -> web.Response:
    """List article authors

    List article authors

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_authors_replace(request: web.Request, article_id, body) -> web.Response:
    """Replace article authors

    Associate new authors with the article. This will remove all already associated authors and add these new ones

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: Authors description
    :type body: dict | bytes

    """
    body = AuthorsCreator.from_dict(body)
    return web.Response(status=200)


async def private_article_categories_add(request: web.Request, article_id, body) -> web.Response:
    """Add article categories

    Associate new categories with the article. This will add new categories to the list of already associated categories

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CategoriesCreator.from_dict(body)
    return web.Response(status=200)


async def private_article_categories_list(request: web.Request, article_id) -> web.Response:
    """List article categories

    List article categories

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_categories_replace(request: web.Request, article_id, body) -> web.Response:
    """Replace article categories

    Associate new categories with the article. This will remove all already associated categories and add these new ones

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CategoriesCreator.from_dict(body)
    return web.Response(status=200)


async def private_article_category_delete(request: web.Request, article_id, category_id) -> web.Response:
    """Delete article category

    De-associate category from article

    :param article_id: Article unique identifier
    :type article_id: int
    :param category_id: Category unique identifier
    :type category_id: int

    """
    return web.Response(status=200)


async def private_article_confidentiality_delete(request: web.Request, article_id) -> web.Response:
    """Delete article confidentiality

    Delete confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_confidentiality_details(request: web.Request, article_id) -> web.Response:
    """Article confidentiality details

    View confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_confidentiality_update(request: web.Request, article_id, body) -> web.Response:
    """Update article confidentiality

    Update confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ConfidentialityCreator.from_dict(body)
    return web.Response(status=200)


async def private_article_create(request: web.Request, body) -> web.Response:
    """Create new Article

    Create a new Article by sending article information

    :param body: Article description
    :type body: dict | bytes

    """
    body = ArticleCreate.from_dict(body)
    return web.Response(status=200)


async def private_article_delete(request: web.Request, article_id) -> web.Response:
    """Delete article

    Delete an article

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_details(request: web.Request, article_id) -> web.Response:
    """Article details

    View a private article

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_embargo_delete(request: web.Request, article_id) -> web.Response:
    """Delete Article Embargo

    Will lift the embargo for the specified article

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_embargo_details(request: web.Request, article_id) -> web.Response:
    """Article Embargo Details

    View a private article embargo details

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_embargo_update(request: web.Request, article_id, body) -> web.Response:
    """Update Article Embargo

    Note: setting an article under whole embargo does not imply that the article will be published when the embargo will expire. You must explicitly call the publish endpoint to enable this functionality.

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: Embargo description
    :type body: dict | bytes

    """
    body = ArticleEmbargoUpdater.from_dict(body)
    return web.Response(status=200)


async def private_article_file(request: web.Request, article_id, file_id) -> web.Response:
    """Single File

    View details of file for specified article

    :param article_id: Article unique identifier
    :type article_id: int
    :param file_id: File unique identifier
    :type file_id: int

    """
    return web.Response(status=200)


async def private_article_file_delete(request: web.Request, article_id, file_id) -> web.Response:
    """File Delete

    Complete file upload

    :param article_id: Article unique identifier
    :type article_id: int
    :param file_id: File unique identifier
    :type file_id: int

    """
    return web.Response(status=200)


async def private_article_files_list(request: web.Request, article_id) -> web.Response:
    """List article files

    List private files

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_private_link(request: web.Request, article_id) -> web.Response:
    """List private links

    List private links

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_private_link_create(request: web.Request, article_id, body=None) -> web.Response:
    """Create private link

    Create new private link for this article

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PrivateLinkCreator.from_dict(body)
    return web.Response(status=200)


async def private_article_private_link_delete(request: web.Request, article_id, link_id) -> web.Response:
    """Disable private link

    Disable/delete private link for this article

    :param article_id: Article unique identifier
    :type article_id: int
    :param link_id: Private link token
    :type link_id: str

    """
    return web.Response(status=200)


async def private_article_private_link_update(request: web.Request, article_id, link_id, body=None) -> web.Response:
    """Update private link

    Update existing private link for this article

    :param article_id: Article unique identifier
    :type article_id: int
    :param link_id: Private link token
    :type link_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PrivateLinkCreator.from_dict(body)
    return web.Response(status=200)


async def private_article_publish(request: web.Request, article_id) -> web.Response:
    """Private Article Publish

    - If the whole article is under embargo, it will not be published immediately, but when the embargo expires or is lifted. - When an article is published, a new public version will be generated. Any further updates to the article will affect the private article data. In order to make these changes publicly visible, an explicit publish operation is needed.

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_reserve_doi(request: web.Request, article_id) -> web.Response:
    """Private Article Reserve DOI

    Reserve DOI for article

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_reserve_handle(request: web.Request, article_id) -> web.Response:
    """Private Article Reserve Handle

    Reserve Handle for article

    :param article_id: Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_article_resource(request: web.Request, article_id, body) -> web.Response:
    """Private Article Resource

    Edit article resource data.

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: Resource data
    :type body: dict | bytes

    """
    body = Resource.from_dict(body)
    return web.Response(status=200)


async def private_article_update(request: web.Request, article_id, body) -> web.Response:
    """Update article

    Updating an article by passing body parameters; request can also be made with the PATCH method.

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: Article description
    :type body: dict | bytes

    """
    body = ArticleUpdate.from_dict(body)
    return web.Response(status=200)


async def private_article_upload_complete(request: web.Request, article_id, file_id) -> web.Response:
    """Complete Upload

    Complete file upload

    :param article_id: Article unique identifier
    :type article_id: int
    :param file_id: File unique identifier
    :type file_id: int

    """
    return web.Response(status=200)


async def private_article_upload_initiate(request: web.Request, article_id, body) -> web.Response:
    """Initiate Upload

    Initiate a new file upload within the article. Either use the link property to point to an existing file that resides elsewhere and will not be uploaded to Figshare or use the other 3 parameters (md5, name, size).

    :param article_id: Article unique identifier
    :type article_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = FileCreator.from_dict(body)
    return web.Response(status=200)


async def private_articles_list(request: web.Request, page=None, page_size=None, limit=None, offset=None) -> web.Response:
    """Private Articles

    Get Own Articles

    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int

    """
    return web.Response(status=200)


async def private_articles_search(request: web.Request, body) -> web.Response:
    """Private Articles search

    Returns a list of private articles filtered by the search parameters

    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = PrivateArticleSearch.from_dict(body)
    return web.Response(status=200)
