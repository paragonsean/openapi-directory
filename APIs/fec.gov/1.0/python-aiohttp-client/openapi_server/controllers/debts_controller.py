from typing import List, Dict
from aiohttp import web

from openapi_server.models.schedules_schedule_d_get_default_response import SchedulesScheduleDGetDefaultResponse
from openapi_server import util


async def schedules_schedule_d_sub_id_get(request: web.Request, api_key, sub_id, page=None, sort_hide_null=None, per_page=None, sort_null_only=None, sort=None, sort_nulls_last=None) -> web.Response:
    """schedules_schedule_d_sub_id_get

     Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.   

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sub_id: 
    :type sub_id: str
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool

    """
    return web.Response(status=200)


async def schedules_schedule_dget(request: web.Request, api_key, max_payment_period=None, min_date=None, max_image_number=None, max_amount_outstanding_close=None, min_image_number=None, sort_null_only=None, min_payment_period=None, min_amount_incurred=None, creditor_debtor_name=None, sort_hide_null=None, candidate_id=None, per_page=None, min_amount_outstanding_beginning=None, sort=None, min_amount_outstanding_close=None, nature_of_debt=None, max_amount_incurred=None, sort_nulls_last=None, page=None, committee_id=None, image_number=None, max_date=None, max_amount_outstanding_beginning=None) -> web.Response:
    """schedules_schedule_dget

     Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.   

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param max_payment_period: 
    :type max_payment_period: float
    :param min_date: Minimum load date
    :type min_date: str
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param max_amount_outstanding_close: 
    :type max_amount_outstanding_close: float
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param min_payment_period: 
    :type min_payment_period: float
    :param min_amount_incurred: 
    :type min_amount_incurred: float
    :param creditor_debtor_name: 
    :type creditor_debtor_name: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param min_amount_outstanding_beginning: 
    :type min_amount_outstanding_beginning: float
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param min_amount_outstanding_close: 
    :type min_amount_outstanding_close: float
    :param nature_of_debt: 
    :type nature_of_debt: str
    :param max_amount_incurred: 
    :type max_amount_incurred: float
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param max_date: Maximum load date
    :type max_date: str
    :param max_amount_outstanding_beginning: 
    :type max_amount_outstanding_beginning: float

    """
    min_date = util.deserialize_date(min_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)
