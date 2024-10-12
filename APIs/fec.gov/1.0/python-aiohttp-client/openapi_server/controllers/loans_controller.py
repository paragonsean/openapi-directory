from typing import List, Dict
from aiohttp import web

from openapi_server.models.schedules_schedule_c_get_default_response import SchedulesScheduleCGetDefaultResponse
from openapi_server import util


async def schedules_schedule_c_sub_id_get(request: web.Request, api_key, sub_id, page=None, sort_hide_null=None, per_page=None, sort_null_only=None, sort=None, sort_nulls_last=None) -> web.Response:
    """schedules_schedule_c_sub_id_get

     Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid. 

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


async def schedules_schedule_cget(request: web.Request, api_key, min_payment_to_date=None, max_image_number=None, min_image_number=None, max_incurred_date=None, sort_null_only=None, last_index=None, sort_hide_null=None, min_amount=None, per_page=None, loan_source_name=None, line_number=None, sort=None, max_payment_to_date=None, candidate_name=None, sort_nulls_last=None, page=None, committee_id=None, image_number=None, min_incurred_date=None, max_amount=None) -> web.Response:
    """schedules_schedule_cget

     Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_payment_to_date:  Minimum payment to date 
    :type min_payment_to_date: int
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param max_incurred_date:  Maximum incurred date 
    :type max_incurred_date: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param last_index: Index of last result from previous page
    :type last_index: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param min_amount:  Filter for all amounts greater than a value. 
    :type min_amount: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param loan_source_name: Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate
    :type loan_source_name: List[str]
    :param line_number:  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. 
    :type line_number: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param max_payment_to_date:  Maximum payment to date 
    :type max_payment_to_date: int
    :param candidate_name: Name of candidate running for office
    :type candidate_name: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param min_incurred_date:  Minimum incurred date 
    :type min_incurred_date: str
    :param max_amount:  Filter for all amounts less than a value. 
    :type max_amount: str

    """
    max_incurred_date = util.deserialize_date(max_incurred_date)
    min_incurred_date = util.deserialize_date(min_incurred_date)
    return web.Response(status=200)
