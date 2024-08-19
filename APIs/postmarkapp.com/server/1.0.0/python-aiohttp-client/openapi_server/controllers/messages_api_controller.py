from typing import List, Dict
from aiohttp import web

from openapi_server.models.inbound_message_full_details_response import InboundMessageFullDetailsResponse
from openapi_server.models.inbound_search_response import InboundSearchResponse
from openapi_server.models.message_click_search_response import MessageClickSearchResponse
from openapi_server.models.message_open_search_response import MessageOpenSearchResponse
from openapi_server.models.outbound_message_details_response import OutboundMessageDetailsResponse
from openapi_server.models.outbound_message_dump_response import OutboundMessageDumpResponse
from openapi_server.models.outbound_search_response import OutboundSearchResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def bypass_rules_for_inbound_message(request: web.Request, x_postmark_server_token, messageid) -> web.Response:
    """Bypass rules for a blocked inbound message

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param messageid: The ID of the message which should bypass inbound rules.
    :type messageid: str

    """
    return web.Response(status=200)


async def get_clicks_for_single_outbound_message(request: web.Request, x_postmark_server_token, messageid, count, offset) -> web.Response:
    """Retrieve Message Clicks

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param messageid: The ID of the Outbound Message for which click statistics should be retrieved.
    :type messageid: str
    :param count: Number of message clicks to return per request. Max 500.
    :type count: int
    :param offset: Number of messages to skip.
    :type offset: int

    """
    return web.Response(status=200)


async def get_inbound_message_details(request: web.Request, x_postmark_server_token, messageid) -> web.Response:
    """Inbound message details

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param messageid: The ID of the message for which to details will be retrieved.
    :type messageid: str

    """
    return web.Response(status=200)


async def get_opens_for_single_outbound_message(request: web.Request, x_postmark_server_token, messageid, count, offset) -> web.Response:
    """Retrieve Message Opens

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param messageid: The ID of the Outbound Message for which open statistics should be retrieved.
    :type messageid: str
    :param count: Number of message opens to return per request. Max 500.
    :type count: int
    :param offset: Number of messages to skip.
    :type offset: int

    """
    return web.Response(status=200)


async def get_outbound_message_details(request: web.Request, x_postmark_server_token, messageid) -> web.Response:
    """Outbound message details

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param messageid: The ID of the message for which to retrieve details.
    :type messageid: str

    """
    return web.Response(status=200)


async def get_outbound_message_dump(request: web.Request, x_postmark_server_token, messageid) -> web.Response:
    """Outbound message dump

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param messageid: The ID of the message for which to retrieve a dump.
    :type messageid: str

    """
    return web.Response(status=200)


async def retry_inbound_message_processing(request: web.Request, x_postmark_server_token, messageid) -> web.Response:
    """Retry a failed inbound message for processing

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param messageid: The ID of the inbound message on which we should retry processing.
    :type messageid: str

    """
    return web.Response(status=200)


async def search_clicks_for_outbound_messages(request: web.Request, x_postmark_server_token, count, offset, recipient=None, tag=None, client_name=None, client_company=None, client_family=None, os_name=None, os_family=None, os_company=None, platform=None, country=None, region=None, city=None) -> web.Response:
    """Clicks for a all messages

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param count: Number of message clicks to return per request. Max 500.
    :type count: int
    :param offset: Number of messages to skip
    :type offset: int
    :param recipient: Filter by To, Cc, Bcc
    :type recipient: str
    :param tag: Filter by tag
    :type tag: str
    :param client_name: Filter by client name, i.e. Outlook, Gmail
    :type client_name: str
    :param client_company: Filter by company, i.e. Microsoft, Apple, Google
    :type client_company: str
    :param client_family: Filter by client family, i.e. OS X, Chrome
    :type client_family: str
    :param os_name: Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7
    :type os_name: str
    :param os_family: Filter by kind of OS used without specific version, i.e. OS X, Windows
    :type os_family: str
    :param os_company: Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation
    :type os_company: str
    :param platform: Filter by platform, i.e. webmail, desktop, mobile
    :type platform: str
    :param country: Filter by country messages were opened in, i.e. Denmark, Russia
    :type country: str
    :param region: Filter by full name of region messages were opened in, i.e. Moscow, New York
    :type region: str
    :param city: Filter by full name of region messages were opened in, i.e. Moscow, New York
    :type city: str

    """
    return web.Response(status=200)


async def search_inbound_messages(request: web.Request, x_postmark_server_token, count, offset, recipient=None, fromemail=None, subject=None, mailboxhash=None, tag=None, status=None, todate=None, fromdate=None) -> web.Response:
    """Inbound message search

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param count: Number of messages to return per request. Max 500.
    :type count: int
    :param offset: Number of messages to skip
    :type offset: int
    :param recipient: Filter by the user who was receiving the email
    :type recipient: str
    :param fromemail: Filter by the sender email address
    :type fromemail: str
    :param subject: Filter by email subject
    :type subject: str
    :param mailboxhash: Filter by mailboxhash
    :type mailboxhash: str
    :param tag: Filter by tag
    :type tag: str
    :param status: Filter by status (&#x60;blocked&#x60;, &#x60;processed&#x60;, &#x60;queued&#x60;, &#x60;failed&#x60;, &#x60;scheduled&#x60;)
    :type status: str
    :param todate: Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str
    :param fromdate: Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60;
    :type fromdate: str

    """
    todate = util.deserialize_date(todate)
    fromdate = util.deserialize_date(fromdate)
    return web.Response(status=200)


async def search_opens_for_outbound_messages(request: web.Request, x_postmark_server_token, count, offset, recipient=None, tag=None, client_name=None, client_company=None, client_family=None, os_name=None, os_family=None, os_company=None, platform=None, country=None, region=None, city=None) -> web.Response:
    """Opens for all messages

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param count: Number of message opens to return per request. Max 500.
    :type count: int
    :param offset: Number of messages to skip
    :type offset: int
    :param recipient: Filter by To, Cc, Bcc
    :type recipient: str
    :param tag: Filter by tag
    :type tag: str
    :param client_name: Filter by client name, i.e. Outlook, Gmail
    :type client_name: str
    :param client_company: Filter by company, i.e. Microsoft, Apple, Google
    :type client_company: str
    :param client_family: Filter by client family, i.e. OS X, Chrome
    :type client_family: str
    :param os_name: Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7
    :type os_name: str
    :param os_family: Filter by kind of OS used without specific version, i.e. OS X, Windows
    :type os_family: str
    :param os_company: Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation
    :type os_company: str
    :param platform: Filter by platform, i.e. webmail, desktop, mobile
    :type platform: str
    :param country: Filter by country messages were opened in, i.e. Denmark, Russia
    :type country: str
    :param region: Filter by full name of region messages were opened in, i.e. Moscow, New York
    :type region: str
    :param city: Filter by full name of region messages were opened in, i.e. Moscow, New York
    :type city: str

    """
    return web.Response(status=200)


async def search_outbound_messages(request: web.Request, x_postmark_server_token, count, offset, recipient=None, fromemail=None, tag=None, status=None, todate=None, fromdate=None) -> web.Response:
    """Outbound message search

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param count: Number of messages to return per request. Max 500.
    :type count: int
    :param offset: Number of messages to skip
    :type offset: int
    :param recipient: Filter by the user who was receiving the email
    :type recipient: str
    :param fromemail: Filter by the sender email address
    :type fromemail: str
    :param tag: Filter by tag
    :type tag: str
    :param status: Filter by status (&#x60;queued&#x60; or &#x60;sent&#x60;)
    :type status: str
    :param todate: Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str
    :param fromdate: Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60;
    :type fromdate: str

    """
    todate = util.deserialize_date(todate)
    fromdate = util.deserialize_date(fromdate)
    return web.Response(status=200)
