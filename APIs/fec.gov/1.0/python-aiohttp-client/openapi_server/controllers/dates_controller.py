from typing import List, Dict
from aiohttp import web

from openapi_server.models.calendar_date_page import CalendarDatePage
from openapi_server.models.election_dates_get_default_response import ElectionDatesGetDefaultResponse
from openapi_server.models.reporting_dates_get_default_response import ReportingDatesGetDefaultResponse
from openapi_server import util


async def calendar_dates_export_get(request: web.Request, api_key, calendar_category_id=None, description=None, sort_nulls_last=None, sort_null_only=None, page=None, max_end_date=None, summary=None, min_end_date=None, sort_hide_null=None, min_start_date=None, per_page=None, max_start_date=None, renderer=None, sort=None, event_id=None) -> web.Response:
    """calendar_dates_export_get

     Returns CSV or ICS for downloading directly into calendar applications like Google, Outlook or other applications.  Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State filtering now applies to elections, reports and reporting periods.  Presidential pre-primary report due dates are not shown on even years. Filers generally opt to file monthly rather than submit over 50 pre-primary election reports. All reporting deadlines are available at /reporting-dates/ for reference.  This is [the sql function](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V40__omnibus_dates.sql) that creates the calendar.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param calendar_category_id:  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29 
    :type calendar_category_id: List[int]
    :param description: Brief description of event
    :type description: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param max_end_date:  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_end_date: str
    :param summary: Longer description of event
    :type summary: List[str]
    :param min_end_date:  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_end_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param min_start_date:  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_start_date: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param max_start_date:  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_start_date: str
    :param renderer: 
    :type renderer: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param event_id: An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.
    :type event_id: int

    """
    max_end_date = util.deserialize_date(max_end_date)
    min_end_date = util.deserialize_date(min_end_date)
    min_start_date = util.deserialize_date(min_start_date)
    max_start_date = util.deserialize_date(max_start_date)
    return web.Response(status=200)


async def calendar_dates_get(request: web.Request, api_key, calendar_category_id=None, description=None, sort_nulls_last=None, sort_null_only=None, page=None, max_end_date=None, summary=None, min_end_date=None, sort_hide_null=None, min_start_date=None, max_start_date=None, per_page=None, sort=None, event_id=None) -> web.Response:
    """calendar_dates_get

     Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State and report type filtering is no longer available. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param calendar_category_id:  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29 
    :type calendar_category_id: List[int]
    :param description: Brief description of event
    :type description: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param max_end_date:  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_end_date: str
    :param summary: Longer description of event
    :type summary: List[str]
    :param min_end_date:  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_end_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param min_start_date:  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_start_date: str
    :param max_start_date:  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_start_date: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param event_id: An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.
    :type event_id: int

    """
    max_end_date = util.deserialize_date(max_end_date)
    min_end_date = util.deserialize_date(min_end_date)
    min_start_date = util.deserialize_date(min_start_date)
    max_start_date = util.deserialize_date(max_start_date)
    return web.Response(status=200)


async def election_dates_get(request: web.Request, api_key, election_state=None, max_election_date=None, election_district=None, min_update_date=None, sort_null_only=None, sort_hide_null=None, max_create_date=None, per_page=None, election_year=None, sort=None, min_create_date=None, election_party=None, office_sought=None, sort_nulls_last=None, page=None, max_update_date=None, election_type_id=None, max_primary_general_date=None, min_election_date=None, min_primary_general_date=None) -> web.Response:
    """election_dates_get

     FEC election dates since 1995. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param election_state:  State or territory of the office sought. 
    :type election_state: List[str]
    :param max_election_date:  The maximum date of election. 
    :type max_election_date: str
    :param election_district:  House district of the office sought, if applicable. 
    :type election_district: List[str]
    :param min_update_date:  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_update_date: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param max_create_date:  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_create_date: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param min_create_date:  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_create_date: str
    :param election_party:  Party, if applicable. 
    :type election_party: List[str]
    :param office_sought:  House, Senate or presidential office. 
    :type office_sought: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param max_update_date:  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_update_date: str
    :param election_type_id:  Election type id 
    :type election_type_id: List[str]
    :param max_primary_general_date:  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_primary_general_date: str
    :param min_election_date:  The minimum date of election. 
    :type min_election_date: str
    :param min_primary_general_date:  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_primary_general_date: str

    """
    max_election_date = util.deserialize_date(max_election_date)
    min_update_date = util.deserialize_date(min_update_date)
    max_create_date = util.deserialize_date(max_create_date)
    min_create_date = util.deserialize_date(min_create_date)
    max_update_date = util.deserialize_date(max_update_date)
    max_primary_general_date = util.deserialize_date(max_primary_general_date)
    min_election_date = util.deserialize_date(min_election_date)
    min_primary_general_date = util.deserialize_date(min_primary_general_date)
    return web.Response(status=200)


async def reporting_dates_get(request: web.Request, api_key, min_update_date=None, report_type=None, min_due_date=None, sort_null_only=None, page=None, max_due_date=None, report_year=None, sort_nulls_last=None, max_create_date=None, max_update_date=None, per_page=None, sort_hide_null=None, sort=None, min_create_date=None) -> web.Response:
    """reporting_dates_get

     FEC election dates since 1995. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_update_date:  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_update_date: str
    :param report_type: Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
    :type report_type: List[str]
    :param min_due_date:  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_due_date: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param max_due_date:  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_due_date: str
    :param report_year:  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    :type report_year: List[int]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param max_create_date:  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_create_date: str
    :param max_update_date:  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_update_date: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param min_create_date:  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_create_date: str

    """
    min_update_date = util.deserialize_date(min_update_date)
    min_due_date = util.deserialize_date(min_due_date)
    max_due_date = util.deserialize_date(max_due_date)
    max_create_date = util.deserialize_date(max_create_date)
    max_update_date = util.deserialize_date(max_update_date)
    min_create_date = util.deserialize_date(min_create_date)
    return web.Response(status=200)
