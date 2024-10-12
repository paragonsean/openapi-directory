from typing import List, Dict
from aiohttp import web

from openapi_server.models.schedule_bby_purpose_page import ScheduleBByPurposePage
from openapi_server.models.schedule_bby_recipient_id_page import ScheduleBByRecipientIDPage
from openapi_server.models.schedule_bby_recipient_page import ScheduleBByRecipientPage
from openapi_server.models.schedule_b_efile_page import ScheduleBEfilePage
from openapi_server.models.schedule_b_page import ScheduleBPage
from openapi_server import util


async def schedules_schedule_b_efile_get(request: web.Request, api_key, min_date=None, disbursement_description=None, sort_null_only=None, page=None, committee_id=None, sort_nulls_last=None, image_number=None, sort_hide_null=None, max_date=None, per_page=None, min_amount=None, max_amount=None, sort=None, recipient_city=None, recipient_state=None) -> web.Response:
    """schedules_schedule_b_efile_get

     Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don&#39;t contain the processed and coded data that you can find on other endpoints. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_date: When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page.
    :type min_date: str
    :param disbursement_description: Description of disbursement
    :type disbursement_description: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param max_date: When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page.
    :type max_date: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param min_amount: Filter for all amounts less than a value.
    :type min_amount: str
    :param max_amount: Filter for all amounts less than a value.
    :type max_amount: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param recipient_city: City of recipient
    :type recipient_city: List[str]
    :param recipient_state: State of recipient
    :type recipient_state: List[str]

    """
    min_date = util.deserialize_date(min_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)


async def schedules_schedule_b_sub_id_get(request: web.Request, api_key, sub_id, min_date=None, spender_committee_designation=None, recipient_committee_id=None, last_disbursement_date=None, max_image_number=None, disbursement_description=None, disbursement_purpose_category=None, min_image_number=None, sort_null_only=None, last_index=None, sort_hide_null=None, min_amount=None, per_page=None, line_number=None, sort=None, recipient_city=None, spender_committee_type=None, last_disbursement_amount=None, spender_committee_org_type=None, two_year_transaction_period=None, committee_id=None, image_number=None, max_date=None, recipient_name=None, max_amount=None, recipient_state=None) -> web.Response:
    """schedules_schedule_b_sub_id_get

     Schedule B filings describe itemized disbursements. This data explains how committees and other filers spend their money. These figures are reported as part of forms F3, F3X and F3P.  The data is divided in two-year periods, called &#x60;two_year_transaction_period&#x60;, which is derived from the &#x60;report_year&#x60; submitted of the corresponding form. If no value is supplied, the results will default to the most recent two-year period that is named after the ending, even-numbered year.  Due to the large quantity of Schedule B filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;disbursement_date&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60; pagination: {     pages: 965191,     per_page: 20,     count: 19303814,     last_indexes: {         last_index: \&quot;230906248\&quot;,         last_disbursement_date: \&quot;2014-07-04\&quot;     } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;230906248&#x60; and &#x60;last_disbursement_date&#x3D;2014-07-04&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out. This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule B data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sub_id: 
    :type sub_id: str
    :param min_date: Minimum date
    :type min_date: str
    :param spender_committee_designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type spender_committee_designation: List[str]
    :param recipient_committee_id: The FEC identifier should be represented here if the contributor is registered with the FEC.
    :type recipient_committee_id: List[str]
    :param last_disbursement_date: When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.
    :type last_disbursement_date: str
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param disbursement_description: Description of disbursement
    :type disbursement_description: List[str]
    :param disbursement_purpose_category: Disbursement purpose category
    :type disbursement_purpose_category: List[str]
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param last_index: Index of last result from previous page
    :type last_index: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param line_number: Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.
    :type line_number: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param recipient_city: City of recipient
    :type recipient_city: List[str]
    :param spender_committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type spender_committee_type: List[str]
    :param last_disbursement_amount: When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.
    :type last_disbursement_amount: float
    :param spender_committee_org_type: The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    :type spender_committee_org_type: List[str]
    :param two_year_transaction_period:  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
    :type two_year_transaction_period: List[int]
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param max_date: Maximum date
    :type max_date: str
    :param recipient_name: Name of the entity receiving the disbursement
    :type recipient_name: List[str]
    :param max_amount: Filter for all amounts less than a value.
    :type max_amount: str
    :param recipient_state: State of recipient
    :type recipient_state: List[str]

    """
    min_date = util.deserialize_date(min_date)
    last_disbursement_date = util.deserialize_date(last_disbursement_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)


async def schedules_schedule_bby_purpose_get(request: web.Request, api_key, purpose=None, cycle=None, sort_null_only=None, page=None, committee_id=None, sort_nulls_last=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_bby_purpose_get

     Schedule B disbursements aggregated by disbursement purpose category. To avoid double counting, memoed items are not included. Purpose is a combination of transaction codes, category codes and disbursement description. Inspect the &#x60;disbursement_purpose&#x60; sql function within the migrations for more details. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param purpose: Disbursement purpose category
    :type purpose: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_bby_recipient_get(request: web.Request, api_key, recipient_name=None, cycle=None, sort_null_only=None, page=None, committee_id=None, sort_nulls_last=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_bby_recipient_get

     Schedule B disbursements aggregated by recipient name. To avoid double counting, memoed items are not included. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param recipient_name: Name of the entity receiving the disbursement
    :type recipient_name: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_bby_recipient_id_get(request: web.Request, api_key, cycle=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, recipient_id=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_bby_recipient_id_get

     Schedule B disbursements aggregated by recipient committee ID, if applicable. To avoid double counting, memoed items are not included. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param recipient_id: The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC.
    :type recipient_id: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_bget(request: web.Request, api_key, min_date=None, spender_committee_designation=None, recipient_committee_id=None, last_disbursement_date=None, max_image_number=None, disbursement_description=None, disbursement_purpose_category=None, min_image_number=None, sort_null_only=None, last_index=None, sort_hide_null=None, min_amount=None, per_page=None, line_number=None, sort=None, recipient_city=None, spender_committee_type=None, last_disbursement_amount=None, spender_committee_org_type=None, two_year_transaction_period=None, committee_id=None, image_number=None, max_date=None, recipient_name=None, max_amount=None, recipient_state=None) -> web.Response:
    """schedules_schedule_bget

     Schedule B filings describe itemized disbursements. This data explains how committees and other filers spend their money. These figures are reported as part of forms F3, F3X and F3P.  The data is divided in two-year periods, called &#x60;two_year_transaction_period&#x60;, which is derived from the &#x60;report_year&#x60; submitted of the corresponding form. If no value is supplied, the results will default to the most recent two-year period that is named after the ending, even-numbered year.  Due to the large quantity of Schedule B filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;disbursement_date&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60; pagination: {     pages: 965191,     per_page: 20,     count: 19303814,     last_indexes: {         last_index: \&quot;230906248\&quot;,         last_disbursement_date: \&quot;2014-07-04\&quot;     } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;230906248&#x60; and &#x60;last_disbursement_date&#x3D;2014-07-04&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out. This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule B data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_date: Minimum date
    :type min_date: str
    :param spender_committee_designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type spender_committee_designation: List[str]
    :param recipient_committee_id: The FEC identifier should be represented here if the contributor is registered with the FEC.
    :type recipient_committee_id: List[str]
    :param last_disbursement_date: When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.
    :type last_disbursement_date: str
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param disbursement_description: Description of disbursement
    :type disbursement_description: List[str]
    :param disbursement_purpose_category: Disbursement purpose category
    :type disbursement_purpose_category: List[str]
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param last_index: Index of last result from previous page
    :type last_index: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param line_number: Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.
    :type line_number: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param recipient_city: City of recipient
    :type recipient_city: List[str]
    :param spender_committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type spender_committee_type: List[str]
    :param last_disbursement_amount: When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.
    :type last_disbursement_amount: float
    :param spender_committee_org_type: The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    :type spender_committee_org_type: List[str]
    :param two_year_transaction_period:  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
    :type two_year_transaction_period: List[int]
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param max_date: Maximum date
    :type max_date: str
    :param recipient_name: Name of the entity receiving the disbursement
    :type recipient_name: List[str]
    :param max_amount: Filter for all amounts less than a value.
    :type max_amount: str
    :param recipient_state: State of recipient
    :type recipient_state: List[str]

    """
    min_date = util.deserialize_date(min_date)
    last_disbursement_date = util.deserialize_date(last_disbursement_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)
