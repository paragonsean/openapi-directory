from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_custom_field_setting_for_portfolio200_response import AddCustomFieldSettingForPortfolio200Response
from openapi_server.models.add_custom_field_setting_for_portfolio_request import AddCustomFieldSettingForPortfolioRequest
from openapi_server.models.add_item_for_portfolio_request import AddItemForPortfolioRequest
from openapi_server.models.add_members_for_portfolio_request import AddMembersForPortfolioRequest
from openapi_server.models.create_portfolio201_response import CreatePortfolio201Response
from openapi_server.models.create_portfolio_request import CreatePortfolioRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_items_for_portfolio200_response import GetItemsForPortfolio200Response
from openapi_server.models.get_portfolios200_response import GetPortfolios200Response
from openapi_server.models.remove_custom_field_setting_for_portfolio_request import RemoveCustomFieldSettingForPortfolioRequest
from openapi_server.models.remove_item_for_portfolio_request import RemoveItemForPortfolioRequest
from openapi_server.models.remove_members_for_portfolio_request import RemoveMembersForPortfolioRequest
from openapi_server import util


async def add_custom_field_setting_for_portfolio(request: web.Request, portfolio_gid, body, opt_pretty=None) -> web.Response:
    """Add a custom field to a portfolio

    Custom fields are associated with portfolios by way of custom field settings.  This method creates a setting for the portfolio.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param body: Information about the custom field setting.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool

    """
    body = AddCustomFieldSettingForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def add_item_for_portfolio(request: web.Request, portfolio_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add a portfolio item

    Add an item to a portfolio. Returns an empty data block.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param body: Information about the item being inserted.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddItemForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def add_members_for_portfolio(request: web.Request, portfolio_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add users to a portfolio

    Adds the specified list of users as members of the portfolio. Returns the updated portfolio record.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param body: Information about the members being added.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddMembersForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def create_portfolio(request: web.Request, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a portfolio

    Creates a new portfolio in the given workspace with the supplied name.  Note that portfolios created in the Asana UI may have some state (like the “Priority” custom field) which is automatically added to the portfolio when it is created. Portfolios created via our API will *not* be created with the same initial state to allow integrations to create their own starting state on a portfolio.

    :param body: The portfolio to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreatePortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def delete_portfolio(request: web.Request, portfolio_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Delete a portfolio

    An existing portfolio can be deleted by making a DELETE request on the URL for that portfolio.  Returns an empty data record.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_items_for_portfolio(request: web.Request, portfolio_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get portfolio items

    Get a list of the items in compact form in a portfolio.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    return web.Response(status=200)


async def get_portfolio(request: web.Request, portfolio_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a portfolio

    Returns the complete portfolio record for a single portfolio.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_portfolios(request: web.Request, workspace, owner, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get multiple portfolios

    Returns a list of the portfolios in compact representation that are owned by the current API user.

    :param workspace: The workspace or organization to filter portfolios on.
    :type workspace: str
    :param owner: The user who owns the portfolio. Currently, API users can only get a list of portfolios that they themselves own.
    :type owner: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    return web.Response(status=200)


async def remove_custom_field_setting_for_portfolio(request: web.Request, portfolio_gid, body, opt_pretty=None) -> web.Response:
    """Remove a custom field from a portfolio

    Removes a custom field setting from a portfolio.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param body: Information about the custom field setting being removed.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool

    """
    body = RemoveCustomFieldSettingForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def remove_item_for_portfolio(request: web.Request, portfolio_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove a portfolio item

    Remove an item from a portfolio. Returns an empty data block.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param body: Information about the item being removed.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveItemForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def remove_members_for_portfolio(request: web.Request, portfolio_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove users from a portfolio

    Removes the specified list of users from members of the portfolio. Returns the updated portfolio record.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param body: Information about the members being removed.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveMembersForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def update_portfolio(request: web.Request, portfolio_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Update a portfolio

    An existing portfolio can be updated by making a PUT request on the URL for that portfolio. Only the fields provided in the &#x60;data&#x60; block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated portfolio record.

    :param portfolio_gid: Globally unique identifier for the portfolio.
    :type portfolio_gid: str
    :param body: The updated fields for the portfolio.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreatePortfolioRequest.from_dict(body)
    return web.Response(status=200)
