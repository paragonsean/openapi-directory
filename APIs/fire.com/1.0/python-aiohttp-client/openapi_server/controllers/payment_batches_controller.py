from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_bank_transfer_batch_payment_request import AddBankTransferBatchPaymentRequest
from openapi_server.models.batch import Batch
from openapi_server.models.batch_approvers import BatchApprovers
from openapi_server.models.batch_item_internal_transfer import BatchItemInternalTransfer
from openapi_server.models.batch_item_international_transfer_mode1 import BatchItemInternationalTransferMode1
from openapi_server.models.batch_items import BatchItems
from openapi_server.models.new_batch import NewBatch
from openapi_server.models.new_batch_item_response import NewBatchItemResponse
from openapi_server.models.new_batch_response import NewBatchResponse
from openapi_server import util


async def add_bank_transfer_batch_payment(request: web.Request, batch_uuid, body) -> web.Response:
    """Add a bank transfer payment to the batch.

    There are two ways to process bank transfers - by Payee ID (**Mode 1**) or by Payee Account Details (**Mode 2**).  **Mode 1:** Use the payee IDs of existing approved payees set up against your account. These batches can be approved in the normal manner.  **Mode 2:** Use the account details of the payee. In the event that these details correspond to an existing approved payee, the batch can be approved as normal. If the account details are new, a batch of New Payees will automatically be created. This batch will need to be approved before the Payment batch can be approved. These payees will then exist as approved payees for future batches. 

    :param batch_uuid: 
    :type batch_uuid: str
    :param body: Details of **Mode 1** &amp; **Mode 2**.
    :type body: dict | bytes

    """
    body = AddBankTransferBatchPaymentRequest.from_dict(body)
    return web.Response(status=200)


async def add_internal_transfer_batch_payment(request: web.Request, batch_uuid, body) -> web.Response:
    """Add an internal transfer payment to the batch

    Simply specify the source account, destination account, amount and a reference.

    :param batch_uuid: 
    :type batch_uuid: str
    :param body: Details of the source account, destination account, amount and a reference.
    :type body: dict | bytes

    """
    body = BatchItemInternalTransfer.from_dict(body)
    return web.Response(status=200)


async def add_international_transfer_batch_payment(request: web.Request, batch_uuid, body) -> web.Response:
    """Add an international transfer payment to the batch.

    International transfers must be added to a batch using the Payee ID (**Mode 1**). Payees must be set up using the web application.  **Mode 1:** Use the payee IDs of existing approved payees set up against your account. These batches can be approved in the normal manner. 

    :param batch_uuid: 
    :type batch_uuid: str
    :param body: Details of **Mode 1**
    :type body: dict | bytes

    """
    body = BatchItemInternationalTransferMode1.from_dict(body)
    return web.Response(status=200)


async def cancel_batch_payment(request: web.Request, batch_uuid) -> web.Response:
    """Cancel a batch

    Cancels the Batch. You can only cancel a batch before it is submitted for approval (while it is in the OPEN state).

    :param batch_uuid: 
    :type batch_uuid: str

    """
    return web.Response(status=200)


async def create_batch_payment(request: web.Request, body) -> web.Response:
    """Create a new batch of payments

    The fire.com API allows businesses to automate payments between their accounts or to third parties across the UK and Europe.  For added security, the API can only set up the payments in batches. These batches must be approved by an authorised user via the firework mobile app.   The process is as follows:  **1.**Create a new batch  **2.**Add payments to the batch  **3.**Submit the batch for approval  Once the batch is submitted, the authorised users will receive notifications to their firework mobile apps. They can review the contents of the batch and then approve or reject it. If approved, the batch is then processed. You can avail of enhanced security by using Dual Authorisation to verify payments if you wish. Dual Authorisation can be enabled by you when setting up your API application in firework online.  **Batch Life Cycle Events**  A batch webhook can be specified to receive details of all the payments as they are processed. This webhook receives notifications for every event in the batch lifecycle.  The following events are triggered during a batch:  **batch.opened:** Contains the details of the batch opened. Checks that the callback URL exists - unless a HTTP 200 response is returned, the callback URL will not be configured.  **batch.item-added:** Details of the item added to the batch  **batch.item-removed:** Details of the item removed from the batch  **batch.cancelled:** Notifies that the batch was cancelled.  **batch.submitted:** Notifes that the batch was submitted  **batch.approved:** Notifies that the batch was approved.  **batch.rejected:** Notifies that the batch was rejected.  **batch.failed:** Notifies that the batch failed - includes the details of the failure (insufficient funds etc)  **batch.completed:** Notifies that the batch completed successfully. Includes a summary.  Push notifications are sent to the firework mobile app for many of these events too - these can be configured from within the app.  This is the first step in creating a batch payment. 

    :param body: Details of the batch payment
    :type body: dict | bytes

    """
    body = NewBatch.from_dict(body)
    return web.Response(status=200)


async def delete_bank_transfer_batch_payment(request: web.Request, batch_uuid, item_uuid) -> web.Response:
    """Remove a Payment from the Batch (Bank Transfers)

    Removes a Payment from the Batch (Bank Transfers). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

    :param batch_uuid: 
    :type batch_uuid: str
    :param item_uuid: 
    :type item_uuid: str

    """
    return web.Response(status=200)


async def delete_internal_transfer_batch_payment(request: web.Request, batch_uuid, item_uuid) -> web.Response:
    """Remove a Payment from the Batch (Internal Transfer)

    Removes a Payment from the Batch (Internal Transfer). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

    :param batch_uuid: 
    :type batch_uuid: str
    :param item_uuid: 
    :type item_uuid: str

    """
    return web.Response(status=200)


async def delete_international_transfer_batch_payment(request: web.Request, batch_uuid, item_uuid) -> web.Response:
    """Remove a Payment from the Batch (International Transfers)

    Removes a Payment from the Batch (International Transfers). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

    :param batch_uuid: 
    :type batch_uuid: str
    :param item_uuid: 
    :type item_uuid: str

    """
    return web.Response(status=200)


async def get_batches(request: web.Request, batch_status=None, batch_types=None, order_by=None, order=None) -> web.Response:
    """List batches

    Returns the list of batch with the specified types and statuses. 

    :param batch_status: 
    :type batch_status: str
    :param batch_types: 
    :type batch_types: str
    :param order_by: 
    :type order_by: str
    :param order: 
    :type order: str

    """
    return web.Response(status=200)


async def get_details_single_batch(request: web.Request, batch_uuid) -> web.Response:
    """Get details of a single Batch

    Returns the details of the batch specified in the API endpoint - {batchUuid}.

    :param batch_uuid: 
    :type batch_uuid: str

    """
    return web.Response(status=200)


async def get_items_batch_bank_transfer(request: web.Request, batch_uuid, offset=None, limit=None) -> web.Response:
    """List items in a Batch (Bank Transfers)

    Returns a paginated list of items in the specified batch.

    :param batch_uuid: 
    :type batch_uuid: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_items_batch_internal_trasnfer(request: web.Request, batch_uuid, offset=None, limit=None) -> web.Response:
    """List items in a Batch (Internal Transfers)

    Returns a paginated list of items in the specified batch.

    :param batch_uuid: 
    :type batch_uuid: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_items_batch_international_transfer(request: web.Request, batch_uuid, offset=None, limit=None) -> web.Response:
    """List items in a Batch (International Transfers)

    Returns a paginated list of items in the specified batch.

    :param batch_uuid: 
    :type batch_uuid: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_listof_approvers_for_batch(request: web.Request, batch_uuid) -> web.Response:
    """List Approvers for a Batch

    Returns a list of approvers for this batch.

    :param batch_uuid: 
    :type batch_uuid: str

    """
    return web.Response(status=200)


async def submit_batch(request: web.Request, batch_uuid) -> web.Response:
    """Submit a batch for approval

    Submits the Batch (for approval in the case of a **BANK_TRANSFER** or **INTERNATIONAL_TRANSFER**). If this is an **INTERNAL_TRANSFER** batch, the transfers are immediately queued for processing. If this is a **BANK_TRANSFER** or **INTERNATIONAL_TRANSFER** batch, this will trigger requests for approval to the firework mobile apps of authorised users. Once those users approve the batch, it is queued for processing.  You can only submit a batch while it is in the OPEN state. 

    :param batch_uuid: 
    :type batch_uuid: str

    """
    return web.Response(status=200)
