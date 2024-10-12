from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_holding_model import AccountHoldingModel
from openapi_server.models.account_holding_with_id_model import AccountHoldingWithIdModel
from openapi_server.models.account_holdings_model import AccountHoldingsModel
from openapi_server.models.account_holdings_without_id_model import AccountHoldingsWithoutIdModel
from openapi_server.models.account_model import AccountModel
from openapi_server.models.account_with_id_model import AccountWithIdModel
from openapi_server.models.accounts_model import AccountsModel
from openapi_server.models.savings_strategies_model import SavingsStrategiesModel
from openapi_server.models.savings_strategy_model import SavingsStrategyModel
from openapi_server.models.savings_strategy_with_id_model import SavingsStrategyWithIdModel
from openapi_server import util


async def accounts_delete_account_by_id(request: web.Request, id) -> web.Response:
    """accounts_delete_account_by_id

    Description: The operation removes an Account tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Account from a Fact Finder.

    :param id: The Account ID used to identify which Account to remove
    :type id: int

    """
    return web.Response(status=200)


async def accounts_delete_account_holding_by_accountid_id(request: web.Request, account_id, id) -> web.Response:
    """accounts_delete_account_holding_by_accountid_id

    Description: This operation deletes a single Account Holding for the specified Account Holding ID and Account ID.&lt;br /&gt;                Purpose: Provides the ability to remove individual holdings from a specified Account.

    :param account_id: The ID of the Account used to retrieve the Account data that the specified holding belongs to.
    :type account_id: int
    :param id: The ID of the Account Holding used to delete the Account Holding
    :type id: int

    """
    return web.Response(status=200)


async def accounts_delete_savings_strategies_by_accountid(request: web.Request, account_id) -> web.Response:
    """accounts_delete_savings_strategies_by_accountid

    Deletes all savings strategies tied to an account

    :param account_id: Id of the account that holds the savings strategies
    :type account_id: int

    """
    return web.Response(status=200)


async def accounts_delete_savings_strategy_by_accountid_id(request: web.Request, account_id, id) -> web.Response:
    """accounts_delete_savings_strategy_by_accountid_id

    Deletes a specific savings strategy

    :param account_id: Id of the account that holds the savings strategy
    :type account_id: int
    :param id: Id of the savings strategy to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def accounts_get_account_holding_by_accountid_id(request: web.Request, account_id, id) -> web.Response:
    """accounts_get_account_holding_by_accountid_id

    Description: This operation retrieves a single Account Holding for the specified Account Holding ID and Account ID.&lt;br /&gt;                Purpose: Provides access to the Account Holding information including description and market value.

    :param account_id: The ID of the Account used to retrieve the Account Holding data
    :type account_id: int
    :param id: The ID of the Account Holding used to retrieve the Account Holding data
    :type id: int

    """
    return web.Response(status=200)


async def accounts_get_account_holdings_by_accountid(request: web.Request, account_id) -> web.Response:
    """accounts_get_account_holdings_by_accountid

    Retrieves all holdings in the specified Account.

    :param account_id: The ID of the Account used to retrieve the Account Holding data
    :type account_id: int

    """
    return web.Response(status=200)


async def accounts_get_accounts_by_fact_finder_id_by_factfinderid_externalsourceid(request: web.Request, fact_finder_id, external_source_id=None) -> web.Response:
    """accounts_get_accounts_by_fact_finder_id_by_factfinderid_externalsourceid

    Description: This operation retrieves all Accounts for the specified Fact Finder ID and/or external source ID.&lt;br /&gt;                Purpose: Provides access to the Account information including description and market value.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Accounts
    :type fact_finder_id: int
    :param external_source_id: The external ID used to filter Accounts
    :type external_source_id: str

    """
    return web.Response(status=200)


async def accounts_get_by_id(request: web.Request, id) -> web.Response:
    """accounts_get_by_id

    Description: This operation retrieves a single Account for the specified Account ID.&lt;br /&gt;                Purpose: Provides access to the Account information including description and market value.

    :param id: The ID of the Account used to retrieve the Account data
    :type id: int

    """
    return web.Response(status=200)


async def accounts_get_savings_strategies_by_account_id_and_savings_strategy_id_by_accountid_id(request: web.Request, account_id, id) -> web.Response:
    """accounts_get_savings_strategies_by_account_id_and_savings_strategy_id_by_accountid_id

    Get a specific savings strategy for an account

    :param account_id: The id of the account to retrieve the savings strategies from
    :type account_id: int
    :param id: The id of the savings strategy to get
    :type id: int

    """
    return web.Response(status=200)


async def accounts_get_savings_strategies_by_account_id_by_accountid(request: web.Request, account_id) -> web.Response:
    """accounts_get_savings_strategies_by_account_id_by_accountid

    Get all of the savings strategies for a specific account

    :param account_id: The id of the account to retrieve the savings strategies from
    :type account_id: int

    """
    return web.Response(status=200)


async def accounts_post_account_holding_by_accountid_model(request: web.Request, account_id, model) -> web.Response:
    """accounts_post_account_holding_by_accountid_model

    Creates a holding and adds it to an existing Account.

    :param account_id: The existing Account ID used to identify which Account to add the holding to
    :type account_id: int
    :param model: The holding data
    :type model: dict | bytes

    """
    model = AccountHoldingModel.from_dict(model)
    return web.Response(status=200)


async def accounts_post_by_model(request: web.Request, model) -> web.Response:
    """accounts_post_by_model

    Description: The operation creates an Account.&lt;br /&gt;                Purpose: Allows for creation of Accounts on a Fact Finder.

    :param model: The Account to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = AccountModel.from_dict(model)
    return web.Response(status=200)


async def accounts_post_savings_strategy_by_accountid_savingsstrategy(request: web.Request, account_id, savings_strategy) -> web.Response:
    """accounts_post_savings_strategy_by_accountid_savingsstrategy

    Creates a savings strategy on a specific account

    :param account_id: Id of the account to create a savings strategy for
    :type account_id: int
    :param savings_strategy: Values for the strategy to be created
    :type savings_strategy: dict | bytes

    """
    savings_strategy = SavingsStrategyModel.from_dict(savings_strategy)
    return web.Response(status=200)


async def accounts_put_by_accountid_id_holding(request: web.Request, account_id, id, holding) -> web.Response:
    """accounts_put_by_accountid_id_holding

    Updates a holding associated with an account

    :param account_id: The account with the holding to be updated
    :type account_id: int
    :param id: The id of the holding to update
    :type id: int
    :param holding: The holding values used to update the current holding
    :type holding: dict | bytes

    """
    holding = AccountHoldingModel.from_dict(holding)
    return web.Response(status=200)


async def accounts_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """accounts_put_by_id_model

    Description: The operation updates an Account, deletes associated saving strategies if the account type changes.&lt;br /&gt;                Purpose: Allows for complete replacement of an Account on a Fact Finder.

    :param id: The existing Account ID used to identify which Account to update
    :type id: int
    :param model: The Account to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = AccountModel.from_dict(model)
    return web.Response(status=200)


async def accounts_put_holdings_by_accountid_holdings(request: web.Request, account_id, holdings) -> web.Response:
    """accounts_put_holdings_by_accountid_holdings

    Updates all holdings associated with an account

    :param account_id: The account with the holding to be updated
    :type account_id: int
    :param holdings: The list of holdings for an account
    :type holdings: dict | bytes

    """
    holdings = AccountHoldingsWithoutIdModel.from_dict(holdings)
    return web.Response(status=200)


async def accounts_put_savings_strategy_by_accountid_id_savingsstrategy(request: web.Request, account_id, id, savings_strategy) -> web.Response:
    """accounts_put_savings_strategy_by_accountid_id_savingsstrategy

    Updates a specific savings strategy

    :param account_id: Id of the account that holds the savings strategy
    :type account_id: int
    :param id: Id of the savings strategy to update
    :type id: int
    :param savings_strategy: The model with which to update the savings strategy with
    :type savings_strategy: dict | bytes

    """
    savings_strategy = SavingsStrategyModel.from_dict(savings_strategy)
    return web.Response(status=200)
