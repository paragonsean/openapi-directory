from typing import List, Dict
from aiohttp import web

from openapi_server.models.schedules_schedule_f_get_default_response import SchedulesScheduleFGetDefaultResponse
from openapi_server import util


async def schedules_schedule_f_sub_id_get(request: web.Request, api_key, sub_id, page=None, per_page=None) -> web.Response:
    """schedules_schedule_f_sub_id_get

     Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sub_id: 
    :type sub_id: str
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int

    """
    return web.Response(status=200)


async def schedules_schedule_fget(request: web.Request, api_key, min_date=None, max_image_number=None, cycle=None, min_image_number=None, sort_null_only=None, payee_name=None, min_amount=None, per_page=None, candidate_id=None, sort_hide_null=None, line_number=None, sort=None, sort_nulls_last=None, page=None, committee_id=None, image_number=None, max_date=None, max_amount=None) -> web.Response:
    """schedules_schedule_fget

     Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_date: Minimum date
    :type min_date: str
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param payee_name: 
    :type payee_name: List[str]
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param line_number: Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.
    :type line_number: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param max_date: Maximum date
    :type max_date: str
    :param max_amount: Filter for all amounts less than a value.
    :type max_amount: str

    """
    min_date = util.deserialize_date(min_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)
