from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_boulder_consulting_services(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_boulder_consulting_services_fund=None, search_db_boulder_consulting_services_department=None, search_db_boulder_consulting_services_organization=None, search_db_boulder_consulting_services_object=None, search_db_boulder_consulting_services_project=None, search_db_boulder_consulting_services_account_description=None, search_db_boulder_consulting_services_date=None, search_db_boulder_consulting_services_amount=None, search_db_boulder_consulting_services_purchase_order=None, search_db_boulder_consulting_services_vendor_name=None, search_db_boulder_consulting_services_comment=None) -> web.Response:
    """Search API for &#39;Boulder Consulting Services Database&#39; entry type

    API to search for entries of type Boulder Consulting Services Database

    :param text: Search text
    :type text: str
    :param name: Search name
    :type name: str
    :param description: Search description
    :type description: str
    :param fromdate: From date
    :type fromdate: str
    :param todate: To date
    :type todate: str
    :param createdate_from: Archive create date from
    :type createdate_from: str
    :param createdate_to: Archive create date to
    :type createdate_to: str
    :param changedate_from: Archive change date from
    :type changedate_from: str
    :param changedate_to: Archive change date to
    :type changedate_to: str
    :param group: Parent entry
    :type group: str
    :param filesuffix: File suffix
    :type filesuffix: str
    :param maxlatitude: Northern bounds of search
    :type maxlatitude: float
    :param minlongitude: Western bounds of search
    :type minlongitude: float
    :param minlatitude: Southern bounds of search
    :type minlatitude: float
    :param maxlongitude: Eastern bounds of search
    :type maxlongitude: float
    :param max: Max number of results
    :type max: int
    :param skip: Number to skip
    :type skip: int
    :param search_db_boulder_consulting_services_fund: Fund
    :type search_db_boulder_consulting_services_fund: str
    :param search_db_boulder_consulting_services_department: Department
    :type search_db_boulder_consulting_services_department: str
    :param search_db_boulder_consulting_services_organization: Organization
    :type search_db_boulder_consulting_services_organization: str
    :param search_db_boulder_consulting_services_object: Object
    :type search_db_boulder_consulting_services_object: str
    :param search_db_boulder_consulting_services_project: Project
    :type search_db_boulder_consulting_services_project: str
    :param search_db_boulder_consulting_services_account_description: Account Description
    :type search_db_boulder_consulting_services_account_description: str
    :param search_db_boulder_consulting_services_date: Date
    :type search_db_boulder_consulting_services_date: str
    :param search_db_boulder_consulting_services_amount: Amount
    :type search_db_boulder_consulting_services_amount: float
    :param search_db_boulder_consulting_services_purchase_order: Purchase Order
    :type search_db_boulder_consulting_services_purchase_order: str
    :param search_db_boulder_consulting_services_vendor_name: Vendor Name
    :type search_db_boulder_consulting_services_vendor_name: str
    :param search_db_boulder_consulting_services_comment: Comment
    :type search_db_boulder_consulting_services_comment: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
