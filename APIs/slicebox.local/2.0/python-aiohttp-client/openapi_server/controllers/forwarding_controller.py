from typing import List, Dict
from aiohttp import web

from openapi_server.models.forwardingrule import Forwardingrule
from openapi_server import util


async def forwarding_rule_id_delete(request: web.Request, id) -> web.Response:
    """forwarding_rule_id_delete

    remove the forwarding rule corresponding to the supplied ID

    :param id: id of forwarding rule to remove
    :type id: int

    """
    return web.Response(status=200)


async def forwarding_rules_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """forwarding_rules_get

    get a list of all forwarding rules. A forwarding rule specifies the automatic forwarding of images from a source (SCP, BOX, etc.) to a destimation (BOX, SCU, etc.)

    :param startindex: start index of returned slice of rules
    :type startindex: int
    :param count: size of returned slice of rules
    :type count: int

    """
    return web.Response(status=200)


async def forwarding_rules_post(request: web.Request, fowarding_rule=None) -> web.Response:
    """forwarding_rules_post

    add a new forwarding rule

    :param fowarding_rule: The forwarding rule to add. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    :type fowarding_rule: dict | bytes

    """
    fowarding_rule = Forwardingrule.from_dict(fowarding_rule)
    return web.Response(status=200)
