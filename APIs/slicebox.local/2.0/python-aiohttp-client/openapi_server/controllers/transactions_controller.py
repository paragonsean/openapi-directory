from typing import List, Dict
from aiohttp import web

from openapi_server.models.failed_outgoing_transaction_image import FailedOutgoingTransactionImage
from openapi_server.models.outgoing_transaction_image import OutgoingTransactionImage
from openapi_server import util


async def transactions_token_image_post(request: web.Request, token, transactionid, sequencenumber, totalimagecount, dataset) -> web.Response:
    """transactions_token_image_post

    add an image (dataset) as part of a transaction. This method is used when sending images using the push method to a public slicebox.

    :param token: authentication token identifying the current box-to-box connection
    :type token: str
    :param transactionid: the ID of the client&#39;s outgoing transaction
    :type transactionid: int
    :param sequencenumber: the index of this image in the transaction
    :type sequencenumber: int
    :param totalimagecount: the total number of images in this transaction
    :type totalimagecount: int
    :param dataset: the dataset byte array
    :type dataset: 

    """
    return web.Response(status=200)


async def transactions_token_outgoing_done_post(request: web.Request, token, outgoing_entry_and_image_information_block) -> web.Response:
    """transactions_token_outgoing_done_post

    signal that the supplied outgoing transaction and image was successfully received and can be marked as sent. This method is used when sending images using the poll method from a public slicebox.

    :param token: authentication token identifying the current box-to-box connection
    :type token: str
    :param outgoing_entry_and_image_information_block: outgoing transaction and image that has been successfully received
    :type outgoing_entry_and_image_information_block: dict | bytes

    """
    outgoing_entry_and_image_information_block = OutgoingTransactionImage.from_dict(outgoing_entry_and_image_information_block)
    return web.Response(status=200)


async def transactions_token_outgoing_failed_post(request: web.Request, token, outgoing_transaction_and_image_and_error_message) -> web.Response:
    """transactions_token_outgoing_failed_post

    signal that the image corresponding to the supplied outgoing transaction and image could not be read or stored properly on the receiving side, and that the transaction should be marked as failed.

    :param token: authentication token identifying the current box-to-box connection
    :type token: str
    :param outgoing_transaction_and_image_and_error_message: the outgoing transaction and image information block corresponding to the failed image transfer, along with the associated error message
    :type outgoing_transaction_and_image_and_error_message: dict | bytes

    """
    outgoing_transaction_and_image_and_error_message = FailedOutgoingTransactionImage.from_dict(outgoing_transaction_and_image_and_error_message)
    return web.Response(status=200)


async def transactions_token_outgoing_get(request: web.Request, token, transactionid, imageid) -> web.Response:
    """transactions_token_outgoing_get

    fetch an image from the connected box as part of a transaction. This method is used when sending images using the poll method from a public slicebox.

    :param token: authentication token identifying the current box-to-box connection
    :type token: str
    :param transactionid: the ID of the outgoing transaction
    :type transactionid: int
    :param imageid: the ID of the outgoing transaction image
    :type imageid: int

    """
    return web.Response(status=200)


async def transactions_token_outgoing_poll_get(request: web.Request, token) -> web.Response:
    """transactions_token_outgoing_poll_get

    get next outgoing transaction and image (information on the next image that the connected box wishes to send to you), if any. This method is used when sending images using the poll method from a public slicebox.

    :param token: authentication token identifying the current box-to-box connection
    :type token: str

    """
    return web.Response(status=200)


async def transactions_token_status_get(request: web.Request, token, transactionid) -> web.Response:
    """transactions_token_status_get

    get the status of the remote incoming transaction with the supplied transaction ID

    :param token: authentication token identifying the current box-to-box connection
    :type token: str
    :param transactionid: the ID of the client&#39;s outgoing transaction
    :type transactionid: int

    """
    return web.Response(status=200)


async def transactions_token_status_put(request: web.Request, token, transactionid, transaction_status) -> web.Response:
    """transactions_token_status_put

    update the status of the transaction with the supplied ID

    :param token: authentication token identifying the current box-to-box connection
    :type token: str
    :param transactionid: the ID of the client&#39;s outgoing transaction
    :type transactionid: int
    :param transaction_status: the updated status of the transaction
    :type transaction_status: str

    """
    return web.Response(status=200)
