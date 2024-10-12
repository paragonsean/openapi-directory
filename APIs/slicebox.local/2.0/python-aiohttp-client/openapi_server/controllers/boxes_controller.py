from typing import List, Dict
from aiohttp import web

from openapi_server.models.box import Box
from openapi_server.models.bulk_anonymization_data import BulkAnonymizationData
from openapi_server.models.image import Image
from openapi_server.models.incoming_transaction import IncomingTransaction
from openapi_server.models.outgoing_transaction import OutgoingTransaction
from openapi_server.models.remote_box import RemoteBox
from openapi_server.models.remote_box_connection_data import RemoteBoxConnectionData
from openapi_server import util


async def boxes_connect_post(request: web.Request, remote_box) -> web.Response:
    """boxes_connect_post

    connect to another box using a received URL. Used to connect to a public box.

    :param remote_box: remote box to connect with
    :type remote_box: dict | bytes

    """
    remote_box = RemoteBox.from_dict(remote_box)
    return web.Response(status=200)


async def boxes_createconnection_post(request: web.Request, remote_box_connection_data) -> web.Response:
    """boxes_createconnection_post

    create a new box connection where the supplied entity holds the remote box name. Used by publicly available boxes.

    :param remote_box_connection_data: name of box to connect (and send URL) to
    :type remote_box_connection_data: dict | bytes

    """
    remote_box_connection_data = RemoteBoxConnectionData.from_dict(remote_box_connection_data)
    return web.Response(status=200)


async def boxes_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """boxes_get

    get a list of box connections

    :param startindex: start index of returned slice of boxes
    :type startindex: int
    :param count: size of returned slice of boxes
    :type count: int

    """
    return web.Response(status=200)


async def boxes_id_delete(request: web.Request, id) -> web.Response:
    """boxes_id_delete

    Delete the remote box with the supplied ID

    :param id: ID of box to remove
    :type id: int

    """
    return web.Response(status=200)


async def boxes_id_send_post(request: web.Request, id, sequence_of_image_tag_values) -> web.Response:
    """boxes_id_send_post

    send images corresponding to the supplied image ids to the remote box with the supplied ID

    :param id: ID of box to send images to
    :type id: int
    :param sequence_of_image_tag_values: specification of which images to send and list of DICOM attribute values to use in anonymized datasets
    :type sequence_of_image_tag_values: dict | bytes

    """
    sequence_of_image_tag_values = BulkAnonymizationData.from_dict(sequence_of_image_tag_values)
    return web.Response(status=200)


async def boxes_incoming_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """boxes_incoming_get

    get incoming transactions (finished, currently receiving, waiting or failed)

    :param startindex: start index of returned slice of transactions
    :type startindex: int
    :param count: size of returned slice of transactions
    :type count: int

    """
    return web.Response(status=200)


async def boxes_incoming_id_delete(request: web.Request, id) -> web.Response:
    """boxes_incoming_id_delete

    delete an incoming transaction. If a currently active transaction is deleted, a new transaction with the remainder of the images is created when receiving the next incoming image.

    :param id: ID of incoming transaction
    :type id: int

    """
    return web.Response(status=200)


async def boxes_incoming_id_images_get(request: web.Request, id) -> web.Response:
    """boxes_incoming_id_images_get

    get the received images corresponding to the incoming transaction with the supplied ID

    :param id: ID of incoming transaction
    :type id: int

    """
    return web.Response(status=200)


async def boxes_outgoing_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """boxes_outgoing_get

    get outgoing transactions (finished, currently sending, waiting or failed)

    :param startindex: start index of returned slice of transactions
    :type startindex: int
    :param count: size of returned slice of transactions
    :type count: int

    """
    return web.Response(status=200)


async def boxes_outgoing_id_delete(request: web.Request, id) -> web.Response:
    """boxes_outgoing_id_delete

    delete an outgoing transaction. This will stop ongoing transactions.

    :param id: ID of outgoing transaction
    :type id: int

    """
    return web.Response(status=200)


async def boxes_outgoing_id_images_get(request: web.Request, id) -> web.Response:
    """boxes_outgoing_id_images_get

    get the sent images corresponding to the outgoing transaction with the supplied ID

    :param id: ID of outgoing transaction
    :type id: int

    """
    return web.Response(status=200)
