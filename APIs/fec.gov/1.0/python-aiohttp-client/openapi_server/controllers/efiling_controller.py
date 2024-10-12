from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_f3_filing_page import BaseF3FilingPage
from openapi_server.models.base_f3_p_filing_page import BaseF3PFilingPage
from openapi_server.models.base_f3_x_filing_page import BaseF3XFilingPage
from openapi_server.models.e_filings_page import EFilingsPage
from openapi_server import util


async def efile_filings_get(request: web.Request, api_key, min_receipt_date=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, max_receipt_date=None, sort_hide_null=None, file_number=None, per_page=None, sort=None, q_filer=None) -> web.Response:
    """efile_filings_get

    Basic information about electronic files coming into the FEC, posted as they are received.

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_receipt_date:  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param max_receipt_date:  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_receipt_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param file_number: Filing ID number
    :type file_number: List[int]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param q_filer:  Keyword search for filer name or ID 
    :type q_filer: List[str]

    """
    min_receipt_date = util.deserialize_date(min_receipt_date)
    max_receipt_date = util.deserialize_date(max_receipt_date)
    return web.Response(status=200)


async def efile_reports_house_senate_get(request: web.Request, api_key, min_receipt_date=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, max_receipt_date=None, sort_hide_null=None, file_number=None, per_page=None, sort=None, q_filer=None) -> web.Response:
    """efile_reports_house_senate_get

     Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_receipt_date:  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param max_receipt_date:  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_receipt_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param file_number: Filing ID number
    :type file_number: List[int]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param q_filer:  Keyword search for filer name or ID 
    :type q_filer: List[str]

    """
    min_receipt_date = util.deserialize_date(min_receipt_date)
    max_receipt_date = util.deserialize_date(max_receipt_date)
    return web.Response(status=200)


async def efile_reports_pac_party_get(request: web.Request, api_key, min_receipt_date=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, max_receipt_date=None, sort_hide_null=None, file_number=None, per_page=None, sort=None, q_filer=None) -> web.Response:
    """efile_reports_pac_party_get

     Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_receipt_date:  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param max_receipt_date:  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_receipt_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param file_number: Filing ID number
    :type file_number: List[int]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param q_filer:  Keyword search for filer name or ID 
    :type q_filer: List[str]

    """
    min_receipt_date = util.deserialize_date(min_receipt_date)
    max_receipt_date = util.deserialize_date(max_receipt_date)
    return web.Response(status=200)


async def efile_reports_presidential_get(request: web.Request, api_key, min_receipt_date=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, max_receipt_date=None, sort_hide_null=None, file_number=None, per_page=None, sort=None, q_filer=None) -> web.Response:
    """efile_reports_presidential_get

     Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_receipt_date:  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param max_receipt_date:  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_receipt_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param file_number: Filing ID number
    :type file_number: List[int]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param q_filer:  Keyword search for filer name or ID 
    :type q_filer: List[str]

    """
    min_receipt_date = util.deserialize_date(min_receipt_date)
    max_receipt_date = util.deserialize_date(max_receipt_date)
    return web.Response(status=200)
