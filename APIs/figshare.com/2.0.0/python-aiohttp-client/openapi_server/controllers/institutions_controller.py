from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_create import AccountCreate
from openapi_server.models.account_update import AccountUpdate
from openapi_server.models.article import Article
from openapi_server.models.category import Category
from openapi_server.models.curation import Curation
from openapi_server.models.curation_comment import CurationComment
from openapi_server.models.curation_comment_create import CurationCommentCreate
from openapi_server.models.curation_detail import CurationDetail
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.group import Group
from openapi_server.models.group_embargo_options import GroupEmbargoOptions
from openapi_server.models.institution import Institution
from openapi_server.models.institution_accounts_search import InstitutionAccountsSearch
from openapi_server.models.response_message import ResponseMessage
from openapi_server.models.role import Role
from openapi_server.models.short_account import ShortAccount
from openapi_server.models.short_custom_field import ShortCustomField
from openapi_server.models.user import User
from openapi_server import util


async def account_institution_curation(request: web.Request, curation_id) -> web.Response:
    """Institution Curation Review

    Retrieve a certain curation review by its ID

    :param curation_id: ID of the curation
    :type curation_id: int

    """
    return web.Response(status=200)


async def account_institution_curation_comments(request: web.Request, curation_id, limit=None, offset=None) -> web.Response:
    """Institution Curation Review Comments

    Retrieve a certain curation review&#39;s comments.

    :param curation_id: ID of the curation
    :type curation_id: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int

    """
    return web.Response(status=200)


async def account_institution_curations(request: web.Request, group_id=None, article_id=None, status=None, limit=None, offset=None) -> web.Response:
    """Institution Curation Reviews

    Retrieve a list of curation reviews for this institution

    :param group_id: Filter by the group ID
    :type group_id: int
    :param article_id: Retrieve the reviews for this article
    :type article_id: int
    :param status: Filter by the status of the review
    :type status: str
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int

    """
    return web.Response(status=200)


async def account_institution_review_curation_id_comments_post(request: web.Request, curation_id, body) -> web.Response:
    """POST Institution Curation Review Comment

    Add a new comment to the review.

    :param curation_id: ID of the curation
    :type curation_id: int
    :param body: The content/value of the comment.
    :type body: dict | bytes

    """
    body = CurationCommentCreate.from_dict(body)
    return web.Response(status=200)


async def custom_fields_list(request: web.Request, group_id=None) -> web.Response:
    """Private account institution group custom fields

    Returns the custom fields in the group the user belongs to, or the ones in the group specified, if the user has access.

    :param group_id: Group_id
    :type group_id: int

    """
    return web.Response(status=200)


async def custom_fields_upload(request: web.Request, custom_field_id, external_file=None) -> web.Response:
    """Custom fields values files upload

    Uploads a CSV containing values for a specific custom field of type &lt;b&gt;dropdown_large_list&lt;/b&gt;. More details in the &lt;a href&#x3D;\&quot;#custom_fields\&quot;&gt;Custom Fields section&lt;/a&gt;

    :param custom_field_id: Custom field identifier
    :type custom_field_id: int
    :param external_file: CSV file to be uploaded
    :type external_file: str

    """
    return web.Response(status=200)


async def institution_articles(request: web.Request, institution_string_id, resource_id, filename) -> web.Response:
    """Public Licenses

    Returns a list of articles belonging to the institution

    :param institution_string_id: 
    :type institution_string_id: str
    :param resource_id: 
    :type resource_id: str
    :param filename: 
    :type filename: str

    """
    return web.Response(status=200)


async def institution_hrfeed_upload(request: web.Request, hrfeed=None) -> web.Response:
    """Private Institution HRfeed Upload

    More info in the &lt;a href&#x3D;\&quot;#hr_feed\&quot;&gt;HR Feed section&lt;/a&gt;

    :param hrfeed: You can find an example in the Hr Feed section
    :type hrfeed: str

    """
    return web.Response(status=200)


async def private_account_institution_user(request: web.Request, account_id) -> web.Response:
    """Private Account Institution User

    Retrieve institution user information using the account_id

    :param account_id: Account identifier the user is associated to
    :type account_id: int

    """
    return web.Response(status=200)


async def private_categories_list(request: web.Request, ) -> web.Response:
    """Private Account Categories

    List institution categories (including parent Categories)


    """
    return web.Response(status=200)


async def private_group_embargo_options_details(request: web.Request, group_id) -> web.Response:
    """Private Account Institution Group Embargo Options

    Account institution group embargo options details

    :param group_id: Group identifier
    :type group_id: int

    """
    return web.Response(status=200)


async def private_institution_account_group_role_delete(request: web.Request, account_id, group_id, role_id) -> web.Response:
    """Delete Institution Account Group Role

    Delete Institution Account Group Role

    :param account_id: Account identifier for which to remove the role
    :type account_id: int
    :param group_id: Group identifier for which to remove the role
    :type group_id: int
    :param role_id: Role identifier
    :type role_id: int

    """
    return web.Response(status=200)


async def private_institution_account_group_roles(request: web.Request, account_id) -> web.Response:
    """List Institution Account Group Roles

    List Institution Account Group Roles

    :param account_id: Account identifier the user is associated to
    :type account_id: int

    """
    return web.Response(status=200)


async def private_institution_account_group_roles_create(request: web.Request, account_id, body) -> web.Response:
    """Add Institution Account Group Roles

    Add Institution Account Group Roles

    :param account_id: Account identifier the user is associated to
    :type account_id: int
    :param body: Account description
    :type body: 

    """
    return web.Response(status=200)


async def private_institution_accounts_create(request: web.Request, body) -> web.Response:
    """Create new Institution Account

    Create a new Account by sending account information

    :param body: Account description
    :type body: dict | bytes

    """
    body = AccountCreate.from_dict(body)
    return web.Response(status=200)


async def private_institution_accounts_list(request: web.Request, page=None, page_size=None, limit=None, offset=None, is_active=None, institution_user_id=None, email=None, id_lte=None, id_gte=None) -> web.Response:
    """Private Account Institution Accounts

    Returns the accounts for which the account has administrative privileges (assigned and inherited).

    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int
    :param is_active: Filter by active status
    :type is_active: int
    :param institution_user_id: Filter by institution_user_id
    :type institution_user_id: str
    :param email: Filter by email
    :type email: str
    :param id_lte: Retrieve accounts with an ID lower or equal to the specified value
    :type id_lte: int
    :param id_gte: Retrieve accounts with an ID greater or equal to the specified value
    :type id_gte: int

    """
    return web.Response(status=200)


async def private_institution_accounts_search(request: web.Request, body) -> web.Response:
    """Private Account Institution Accounts Search

    Returns the accounts for which the account has administrative privileges (assigned and inherited).

    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = InstitutionAccountsSearch.from_dict(body)
    return web.Response(status=200)


async def private_institution_accounts_update(request: web.Request, account_id, body) -> web.Response:
    """Update Institution Account

    Update Institution Account

    :param account_id: Account identifier the user is associated to
    :type account_id: int
    :param body: Account description
    :type body: dict | bytes

    """
    body = AccountUpdate.from_dict(body)
    return web.Response(status=200)


async def private_institution_articles(request: web.Request, page=None, page_size=None, limit=None, offset=None, order=None, order_direction=None, published_since=None, modified_since=None, status=None, resource_doi=None, item_type=None) -> web.Response:
    """Private Institution Articles

    Get Articles from own institution. User must be administrator of the institution

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
    :param published_since: Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    :type published_since: str
    :param modified_since: Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    :type modified_since: str
    :param status: only return collections with this status
    :type status: int
    :param resource_doi: only return collections with this resource_doi
    :type resource_doi: str
    :param item_type: Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model
    :type item_type: int

    """
    return web.Response(status=200)


async def private_institution_details(request: web.Request, ) -> web.Response:
    """Private Account Institutions

    Account institution details


    """
    return web.Response(status=200)


async def private_institution_embargo_options_details(request: web.Request, ) -> web.Response:
    """Private Account Institution embargo options

    Account institution embargo options details


    """
    return web.Response(status=200)


async def private_institution_groups_list(request: web.Request, ) -> web.Response:
    """Private Account Institution Groups

    Returns the groups for which the account has administrative privileges (assigned and inherited).


    """
    return web.Response(status=200)


async def private_institution_roles_list(request: web.Request, ) -> web.Response:
    """Private Account Institution Roles

    Returns the roles available for groups and the institution group.


    """
    return web.Response(status=200)
