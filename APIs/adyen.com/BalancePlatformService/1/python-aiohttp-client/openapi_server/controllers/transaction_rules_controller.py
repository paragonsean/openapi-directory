from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.transaction_rule import TransactionRule
from openapi_server.models.transaction_rule_info import TransactionRuleInfo
from openapi_server.models.transaction_rule_response import TransactionRuleResponse
from openapi_server import util


async def delete_transaction_rules_transaction_rule_id(request: web.Request, transaction_rule_id) -> web.Response:
    """Delete a transaction rule

    Deletes a transaction rule.

    :param transaction_rule_id: The unique identifier of the transaction rule.
    :type transaction_rule_id: str

    """
    return web.Response(status=200)


async def get_transaction_rules_transaction_rule_id(request: web.Request, transaction_rule_id) -> web.Response:
    """Get a transaction rule

    Returns the details of a transaction rule.

    :param transaction_rule_id: The unique identifier of the transaction rule.
    :type transaction_rule_id: str

    """
    return web.Response(status=200)


async def patch_transaction_rules_transaction_rule_id(request: web.Request, transaction_rule_id, body=None) -> web.Response:
    """Update a transaction rule

    Updates a transaction rule.   * To update only the status of a transaction rule, send only the &#x60;status&#x60; parameter. All other parameters not provided in the request are left unchanged.  * When updating any other parameter, you need to send all existing resource parameters. If you omit a parameter in the request, that parameter is removed from the resource.

    :param transaction_rule_id: The unique identifier of the transaction rule.
    :type transaction_rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TransactionRuleInfo.from_dict(body)
    return web.Response(status=200)


async def post_transaction_rules(request: web.Request, body=None) -> web.Response:
    """Create a transaction rule

    Creates a [transaction rule](https://docs.adyen.com/issuing/transaction-rules). When your user makes a transaction with their Adyen-issued card, the transaction is allowed or declined based on the conditions and outcome defined in the transaction rule. You can apply the transaction rule to several cards, such as all the cards in your platform, or to a specific card. For use cases, see [examples](https://docs.adyen.com/issuing/transaction-rules/examples).

    :param body: 
    :type body: dict | bytes

    """
    body = TransactionRuleInfo.from_dict(body)
    return web.Response(status=200)
