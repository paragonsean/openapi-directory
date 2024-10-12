from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def create_transaction(request: web.Request, active, source, status, date_closed=None, date_created=None, licensee_number=None, number=None, payment_method=None) -> web.Response:
    """Create Transaction

    Creates a new Transaction

    :param active: Always &#39;true&#39; for Transactions
    :type active: bool
    :param source: AUTO Transaction for internal use only
    :type source: str
    :param status: 
    :type status: str
    :param date_closed: 
    :type date_closed: str
    :param date_created: 
    :type date_created: str
    :param licensee_number: 
    :type licensee_number: str
    :param number: Unique number (across all Products of a Vendor) that identifies the Transaction
    :type number: str
    :param payment_method: 
    :type payment_method: str

    """
    date_closed = util.deserialize_datetime(date_closed)
    date_created = util.deserialize_datetime(date_created)
    return web.Response(status=200)


async def get_transaction(request: web.Request, transaction_number) -> web.Response:
    """Get Transaction 

    Return a Transaction by &#39;transactionNumber&#39;

    :param transaction_number: Unique number (across all Products of a Vendor) that identifies the Transaction
    :type transaction_number: str

    """
    return web.Response(status=200)


async def list_transactions(request: web.Request, ) -> web.Response:
    """List Transactions

    Return a list of all Transactions for the current Vendor


    """
    return web.Response(status=200)


async def update_transaction(request: web.Request, transaction_number, active=None, date_closed=None, date_created=None, number=None, payment_method=None, source=None, status=None) -> web.Response:
    """Update Transaction

    Sets the provided properties to a Transaction. Return an updated Transaction

    :param transaction_number: Unique number (across all Products of a Vendor) that identifies the Transaction
    :type transaction_number: str
    :param active: Always &#39;true&#39; for Transactions
    :type active: bool
    :param date_closed: 
    :type date_closed: str
    :param date_created: 
    :type date_created: str
    :param number: Unique number (across all Products of a Vendor) that identifies the Transaction
    :type number: str
    :param payment_method: 
    :type payment_method: str
    :param source: AUTO Transaction for internal use only
    :type source: str
    :param status: 
    :type status: str

    """
    date_closed = util.deserialize_datetime(date_closed)
    date_created = util.deserialize_datetime(date_created)
    return web.Response(status=200)
