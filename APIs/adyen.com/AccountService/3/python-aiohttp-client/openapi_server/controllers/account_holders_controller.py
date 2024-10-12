from typing import List, Dict
from aiohttp import web

from openapi_server.models.close_account_holder_request import CloseAccountHolderRequest
from openapi_server.models.close_account_holder_response import CloseAccountHolderResponse
from openapi_server.models.create_account_holder_request import CreateAccountHolderRequest
from openapi_server.models.create_account_holder_response import CreateAccountHolderResponse
from openapi_server.models.get_account_holder_request import GetAccountHolderRequest
from openapi_server.models.get_account_holder_response import GetAccountHolderResponse
from openapi_server.models.get_account_holder_status_response import GetAccountHolderStatusResponse
from openapi_server.models.get_tax_form_request import GetTaxFormRequest
from openapi_server.models.get_tax_form_response import GetTaxFormResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.suspend_account_holder_request import SuspendAccountHolderRequest
from openapi_server.models.suspend_account_holder_response import SuspendAccountHolderResponse
from openapi_server.models.un_suspend_account_holder_request import UnSuspendAccountHolderRequest
from openapi_server.models.un_suspend_account_holder_response import UnSuspendAccountHolderResponse
from openapi_server.models.update_account_holder_request import UpdateAccountHolderRequest
from openapi_server.models.update_account_holder_response import UpdateAccountHolderResponse
from openapi_server.models.update_account_holder_state_request import UpdateAccountHolderStateRequest
from openapi_server import util


async def post_close_account_holder(request: web.Request, body=None) -> web.Response:
    """Close an account holder

    Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) to **Closed**. This state is final. If an account holder is closed, you can&#39;t process transactions, pay out funds, or reopen it. If payments are made to an account of an account holder with a **Closed** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status), the payments are sent to your liable account.

    :param body: 
    :type body: dict | bytes

    """
    body = CloseAccountHolderRequest.from_dict(body)
    return web.Response(status=200)


async def post_create_account_holder(request: web.Request, body=None) -> web.Response:
    """Create an account holder

    Creates an account holder that [represents the sub-merchant&#39;s entity](https://docs.adyen.com/marketplaces-and-platforms/classic/account-structure#your-platform) in your platform. The details that you need to provide in the request depend on the sub-merchant&#39;s legal entity type. For more information, refer to [Account holder and accounts](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#legal-entity-types).

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAccountHolderRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_account_holder(request: web.Request, body=None) -> web.Response:
    """Get an account holder

    Returns the details of an account holder.

    :param body: 
    :type body: dict | bytes

    """
    body = GetAccountHolderRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_tax_form(request: web.Request, body=None) -> web.Response:
    """Get a tax form

    Generates a tax form for account holders operating in the US. For more information, refer to [Providing tax forms](https://docs.adyen.com/marketplaces-and-platforms/classic/tax-forms).

    :param body: 
    :type body: dict | bytes

    """
    body = GetTaxFormRequest.from_dict(body)
    return web.Response(status=200)


async def post_suspend_account_holder(request: web.Request, body=None) -> web.Response:
    """Suspend an account holder

    Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) to **Suspended**.

    :param body: 
    :type body: dict | bytes

    """
    body = SuspendAccountHolderRequest.from_dict(body)
    return web.Response(status=200)


async def post_un_suspend_account_holder(request: web.Request, body=None) -> web.Response:
    """Unsuspend an account holder

    Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) from **Suspended** to **Inactive**.  Account holders can have a **Suspended** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status) if you suspend them through the [&#x60;/suspendAccountHolder&#x60;](https://docs.adyen.com/api-explorer/#/Account/v5/post/suspendAccountHolder) endpoint or if a verification deadline expires.  You can only unsuspend account holders if they do not have verification checks with a **FAILED** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status).

    :param body: 
    :type body: dict | bytes

    """
    body = UnSuspendAccountHolderRequest.from_dict(body)
    return web.Response(status=200)


async def post_update_account_holder(request: web.Request, body=None) -> web.Response:
    """Update an account holder

    Updates the &#x60;accountHolderDetails&#x60; and &#x60;processingTier&#x60; of an account holder, and adds bank accounts and shareholders.  When updating &#x60;accountHolderDetails&#x60;, parameters that are not included in the request are left unchanged except for the following object:  * &#x60;metadata&#x60;: Updating the metadata replaces the entire object. This means that to update an existing key-value pair, you must provide the changes, as well as other existing key-value pairs.  When updating any field in the following objects, you must submit all the fields required for validation:   * &#x60;address&#x60;  * &#x60;fullPhoneNumber&#x60;  * &#x60;bankAccountDetails.BankAccountDetail&#x60;  * &#x60;businessDetails.shareholders.ShareholderContact&#x60;   For example, to update the &#x60;address.postalCode&#x60;, you must also submit the &#x60;address.country&#x60;, &#x60;.city&#x60;, &#x60;.street&#x60;, &#x60;.postalCode&#x60;, and possibly &#x60;.stateOrProvince&#x60; so that the address can be validated.  To add a bank account or shareholder, provide the bank account or shareholder details without a &#x60;bankAccountUUID&#x60; or a &#x60;shareholderCode&#x60;.  

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAccountHolderRequest.from_dict(body)
    return web.Response(status=200)


async def post_update_account_holder_state(request: web.Request, body=None) -> web.Response:
    """Update payout or processing state

    Disables or enables the processing or payout state of an account holder.

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAccountHolderStateRequest.from_dict(body)
    return web.Response(status=200)
