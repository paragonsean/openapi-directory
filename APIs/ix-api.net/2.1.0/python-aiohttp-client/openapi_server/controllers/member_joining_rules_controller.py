from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.member_joining_rule import MemberJoiningRule
from openapi_server.models.member_joining_rule_request import MemberJoiningRuleRequest
from openapi_server.models.member_joining_rule_update import MemberJoiningRuleUpdate
from openapi_server.models.member_joining_rule_update_partial import MemberJoiningRuleUpdatePartial
from openapi_server import util


async def member_joining_rules_create(request: web.Request, body=None) -> web.Response:
    """member_joining_rules_create

    Create a member joining rule

    :param body: Polymorphic Member Joining Rule Request
    :type body: dict | bytes

    """
    body = MemberJoiningRuleRequest.from_dict(body)
    return web.Response(status=200)


async def member_joining_rules_destroy(request: web.Request, id) -> web.Response:
    """member_joining_rules_destroy

    Delete a joining rule

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def member_joining_rules_list(request: web.Request, id=None, network_service=None) -> web.Response:
    """member_joining_rules_list

    Get a list of joining rules

    :param id: Filter by id
    :type id: List[str]
    :param network_service: Filter by network_service
    :type network_service: str

    """
    return web.Response(status=200)


async def member_joining_rules_partial_update(request: web.Request, id, body=None) -> web.Response:
    """member_joining_rules_partial_update

    Partially update a joining rule

    :param id: Get by id
    :type id: str
    :param body: Polymorphic Member Joining Rule Update
    :type body: dict | bytes

    """
    body = MemberJoiningRuleUpdatePartial.from_dict(body)
    return web.Response(status=200)


async def member_joining_rules_read(request: web.Request, id) -> web.Response:
    """member_joining_rules_read

    Get a single rule

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def member_joining_rules_update(request: web.Request, id, body=None) -> web.Response:
    """member_joining_rules_update

    Update a joining rule

    :param id: Get by id
    :type id: str
    :param body: Polymorphic Member Joining Rule Update
    :type body: dict | bytes

    """
    body = MemberJoiningRuleUpdate.from_dict(body)
    return web.Response(status=200)
