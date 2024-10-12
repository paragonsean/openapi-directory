from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_alias_request import CreateAliasRequest
from openapi_server.models.create_catch_all_request import CreateCatchAllRequest
from openapi_server.models.create_smtp_domain_request import CreateSmtpDomainRequest
from openapi_server.models.mail_zone import MailZone
from openapi_server.models.update_alias_request import UpdateAliasRequest
from openapi_server.models.update_anti_spam_request import UpdateAntiSpamRequest
from openapi_server.models.update_smtp_domain_request import UpdateSmtpDomainRequest
from openapi_server import util


async def configure_alias(request: web.Request, domain_name, email_address, domain_name2, email_address2, body=None) -> web.Response:
    """Configure a alias

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param email_address: Alias e-mail address.
    :type email_address: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param email_address2: Automatically added
    :type email_address2: str
    :param body: Contains the alias information.
    :type body: dict | bytes

    """
    body = UpdateAliasRequest.from_dict(body)
    return web.Response(status=200)


async def configure_anti_spam(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Configure anti-spam for mail zone

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Contains the anti-spam information.
    :type body: dict | bytes

    """
    body = UpdateAntiSpamRequest.from_dict(body)
    return web.Response(status=200)


async def configure_smtp_domain(request: web.Request, domain_name, hostname, domain_name2, body=None) -> web.Response:
    """Configure an extra smtp domain

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param hostname: Smtp domain name.
    :type hostname: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Contains the smtp domain information.
    :type body: dict | bytes

    """
    body = UpdateSmtpDomainRequest.from_dict(body)
    return web.Response(status=200)


async def create_alias(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Create a new alias

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Contains the alias information.
    :type body: dict | bytes

    """
    body = CreateAliasRequest.from_dict(body)
    return web.Response(status=200)


async def create_catch_all(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Create a catch-all on the mail zone

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Contains the catch-all information.
    :type body: dict | bytes

    """
    body = CreateCatchAllRequest.from_dict(body)
    return web.Response(status=200)


async def create_smtp_domain(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Create an extra smtp domain

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Contains the smtp domain information.
    :type body: dict | bytes

    """
    body = CreateSmtpDomainRequest.from_dict(body)
    return web.Response(status=200)


async def delete_alias(request: web.Request, domain_name, email_address, domain_name2, email_address2) -> web.Response:
    """Delete a alias

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param email_address: Alias e-mail address.
    :type email_address: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param email_address2: Automatically added
    :type email_address2: str

    """
    return web.Response(status=200)


async def delete_catch_all(request: web.Request, domain_name, email_address, domain_name2, email_address2) -> web.Response:
    """Delete a catch-all on the mail zone

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param email_address: E-mail address to which all e-mails are sent to inexistent mailboxes or aliases.
    :type email_address: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param email_address2: Automatically added
    :type email_address2: str

    """
    return web.Response(status=200)


async def delete_smtp_domain(request: web.Request, domain_name, hostname, domain_name2) -> web.Response:
    """Delete an extra smtp domain

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param hostname: Smtp domain name.
    :type hostname: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)


async def get_mail_zone(request: web.Request, domain_name, domain_name2) -> web.Response:
    """Get the mail zone.

    

    :param domain_name: Mail zone domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)
