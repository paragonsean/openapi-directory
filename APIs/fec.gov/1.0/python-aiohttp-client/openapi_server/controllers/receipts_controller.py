from typing import List, Dict
from aiohttp import web

from openapi_server.models.schedule_aby_employer_page import ScheduleAByEmployerPage
from openapi_server.models.schedule_aby_occupation_page import ScheduleAByOccupationPage
from openapi_server.models.schedule_aby_size_candidate_page import ScheduleABySizeCandidatePage
from openapi_server.models.schedule_aby_size_page import ScheduleABySizePage
from openapi_server.models.schedule_aby_state_candidate_page import ScheduleAByStateCandidatePage
from openapi_server.models.schedule_aby_state_page import ScheduleAByStatePage
from openapi_server.models.schedule_aby_state_recipient_totals_page import ScheduleAByStateRecipientTotalsPage
from openapi_server.models.schedule_aby_zip_page import ScheduleAByZipPage
from openapi_server.models.schedule_a_efile_page import ScheduleAEfilePage
from openapi_server.models.schedule_a_page import ScheduleAPage
from openapi_server import util


async def schedules_schedule_a_efile_get(request: web.Request, api_key, min_date=None, max_image_number=None, contributor_employer=None, min_image_number=None, sort_null_only=None, sort_hide_null=None, contributor_name=None, min_amount=None, per_page=None, contributor_state=None, sort=None, line_number=None, contributor_occupation=None, contributor_city=None, sort_nulls_last=None, page=None, committee_id=None, image_number=None, max_date=None, max_amount=None) -> web.Response:
    """schedules_schedule_a_efile_get

     Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don&#39;t contain the processed and coded data that you can find on other endpoints. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_date: Minimum date
    :type min_date: str
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param contributor_employer: Employer of contributor, filers need to make an effort to gather this information
    :type contributor_employer: List[str]
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param contributor_name: Name of contributor
    :type contributor_name: List[str]
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param contributor_state: State of contributor
    :type contributor_state: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param line_number: Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.
    :type line_number: str
    :param contributor_occupation: Occupation of contributor, filers need to make an effort to gather this information
    :type contributor_occupation: List[str]
    :param contributor_city: City of contributor
    :type contributor_city: List[str]
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


async def schedules_schedule_a_sub_id_get(request: web.Request, api_key, sub_id, is_individual=None, min_date=None, max_image_number=None, min_image_number=None, contributor_type=None, contributor_id=None, recipient_committee_org_type=None, contributor_employer=None, sort_null_only=None, last_index=None, contributor_name=None, min_amount=None, sort_hide_null=None, recipient_committee_designation=None, max_load_date=None, recipient_committee_type=None, sort=None, last_contribution_receipt_date=None, last_contribution_receipt_amount=None, line_number=None, contributor_state=None, per_page=None, two_year_transaction_period=None, contributor_zip=None, min_load_date=None, contributor_occupation=None, contributor_city=None, committee_id=None, image_number=None, max_date=None, max_amount=None) -> web.Response:
    """schedules_schedule_a_sub_id_get

     This description is for both ​&#x60;/schedules​/schedule_a​/&#x60; and ​ &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60;.  This endpoint provides itemized receipts. Schedule A records describe itemized receipts, including contributions from individuals. If you are interested in contributions from an individual, use the &#x60;/schedules/schedule_a/&#x60; endpoint. For a more complete description of all Schedule A records visit [About receipts data](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/about-receipts-data/). If you are interested in our \&quot;is_individual\&quot; methodology visit our [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology/).  ​The &#x60;/schedules​/schedule_a​/&#x60; endpoint is not paginated by page number. This endpoint uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset. To request the next page, you should append the values found in the &#x60;last_indexes&#x60; object from pagination to the URL of your last request as additional parameters.  For example, when sorting by &#x60;contribution_receipt_date&#x60;, you might receive a page of results with the two scenarios of following pagination information:  case #1: &#x60;&#x60;&#x60; pagination: {     pages: 2152643,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880619\&quot;,         last_contribution_receipt_date: \&quot;2014-01-01\&quot;     } } &#x60;&#x60;&#x60; &lt;br/&gt; case #2 (results which include contribution_receipt_date &#x3D; NULL):  &#x60;&#x60;&#x60; pagination: {     pages: 2152644,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880639\&quot;,         sort_null_only: True     } } &#x60;&#x60;&#x60; To fetch the next page of sorted results, append &#x60;last_index&#x3D;230880619&#x60; and &#x60;last_contribution_receipt_date&#x3D;2014-01-01&#x60; to the URL and when reaching &#x60;contribution_receipt_date&#x3D;NULL&#x60;, append &#x60;last_index&#x3D;230880639&#x60; and &#x60;sort_null_only&#x3D;True&#x60;. We strongly advise paging through these results using sort indices. The default sort is acending by &#x60;contribution_receipt_date&#x60; (&#x60;deprecated&#x60;, will be descending). If you do not page using sort indices, some transactions may be unintentionally filtered out.  Calls to ​&#x60;/schedules​/schedule_a​/&#x60; may return many records. For large result sets, the record counts found in the pagination object are approximate; you will need to page through the records until no records are returned.  To avoid throwing the \&quot;out of range\&quot; exception on the last page, one recommandation is to use total count and &#x60;per_page&#x60; to control the traverse loop of results.  ​The &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60; endpoint returns a single transaction, but it does include a pagination object class. Please ignore the information in that object class.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sub_id: 
    :type sub_id: str
    :param is_individual: Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals.
    :type is_individual: bool
    :param min_date: Minimum date
    :type min_date: str
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param contributor_type: Filters individual or committee contributions based on line number
    :type contributor_type: List[str]
    :param contributor_id: The FEC identifier should be represented here if the contributor is registered with the FEC.
    :type contributor_id: List[str]
    :param recipient_committee_org_type: The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    :type recipient_committee_org_type: List[str]
    :param contributor_employer: Employer of contributor, filers need to make an effort to gather this information
    :type contributor_employer: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param last_index: Index of last result from previous page
    :type last_index: int
    :param contributor_name: Name of contributor
    :type contributor_name: List[str]
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param recipient_committee_designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type recipient_committee_designation: List[str]
    :param max_load_date: Maximum load date
    :type max_load_date: str
    :param recipient_committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type recipient_committee_type: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param last_contribution_receipt_date: When sorting by &#x60;contribution_receipt_date&#x60;, this is populated with the         &#x60;contribution_receipt_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page.
    :type last_contribution_receipt_date: str
    :param last_contribution_receipt_amount: When sorting by &#x60;contribution_receipt_amount&#x60;, this is populated with the         &#x60;contribution_receipt_amount&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page.
    :type last_contribution_receipt_amount: float
    :param line_number: Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.
    :type line_number: str
    :param contributor_state: State of contributor
    :type contributor_state: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param two_year_transaction_period:  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
    :type two_year_transaction_period: List[int]
    :param contributor_zip: Zip code of contributor
    :type contributor_zip: List[str]
    :param min_load_date: Minimum load date
    :type min_load_date: str
    :param contributor_occupation: Occupation of contributor, filers need to make an effort to gather this information
    :type contributor_occupation: List[str]
    :param contributor_city: City of contributor
    :type contributor_city: List[str]
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
    max_load_date = util.deserialize_date(max_load_date)
    last_contribution_receipt_date = util.deserialize_date(last_contribution_receipt_date)
    min_load_date = util.deserialize_date(min_load_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)


async def schedules_schedule_aby_employer_get(request: web.Request, api_key, cycle=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, sort_hide_null=None, employer=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_employer_get

     This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s employer name. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

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
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param employer: Employer of contributor as reported on the committee&#39;s filing
    :type employer: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_aby_occupation_get(request: web.Request, api_key, cycle=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, occupation=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_occupation_get

     This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s occupation. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

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
    :param occupation: Occupation of contributor as reported on the committee&#39;s filing
    :type occupation: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_aby_size_by_candidate_get(request: web.Request, api_key, cycle, candidate_id, election_full=None, sort_null_only=None, sort_nulls_last=None, page=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_size_by_candidate_get

     This endpoint provides itemized individual contributions received by a committee, aggregated by size of contribution and candidate. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_aby_size_get(request: web.Request, api_key, cycle=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, size=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_size_get

     This endpoint provides individual contributions received by a committee, aggregated by size:  &#x60;&#x60;&#x60;  - $200 and under  - $200.01 - $499.99  - $500 - $999.99  - $1000 - $1999.99  - $2000 + &#x60;&#x60;&#x60;  The $200.00 and under category includes contributions of $200 or less combined with unitemized individual contributions. 

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
    :param size:  The total all contributions in the following ranges: &#x60;&#x60;&#x60;   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + &#x60;&#x60;&#x60; Unitemized contributions are included in the &#x60;0&#x60; category. 
    :type size: List[int]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_aby_state_by_candidate_get(request: web.Request, api_key, cycle, candidate_id, election_full=None, sort_null_only=None, sort_nulls_last=None, page=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_state_by_candidate_get

     This endpoint provides itemized individual contributions received by a committee, aggregated by contributor’s state and candidate. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_aby_state_by_candidate_totals_get(request: web.Request, api_key, cycle, candidate_id, election_full=None, sort_null_only=None, sort_nulls_last=None, page=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_state_by_candidate_totals_get

     Itemized individual contributions aggregated by contributor’s state, candidate, committee type and cycle. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_aby_state_get(request: web.Request, api_key, hide_null=None, cycle=None, sort_null_only=None, page=None, state=None, committee_id=None, sort_nulls_last=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_state_get

     This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s state. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param hide_null: Exclude values with missing state
    :type hide_null: bool
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: State of contributor
    :type state: List[str]
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


async def schedules_schedule_aby_state_totals_get(request: web.Request, api_key, committee_type=None, cycle=None, sort_null_only=None, page=None, state=None, sort_nulls_last=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_state_totals_get

     This endpoint provides itemized individual contributions received by a committee, aggregated by contributor’s state, committee type and cycle. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account         - all All Committee Types         - all_candidates All Candidate Committee Types (H, S, P)         - all_pacs All PAC Committee Types (N, O, Q, V, W) 
    :type committee_type: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory
    :type state: List[str]
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


async def schedules_schedule_aby_zip_get(request: web.Request, api_key, zip=None, cycle=None, sort_null_only=None, page=None, state=None, committee_id=None, sort_nulls_last=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_aby_zip_get

     This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s ZIP code. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param zip: Zip code of contributor
    :type zip: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: State of contributor
    :type state: List[str]
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


async def schedules_schedule_aget(request: web.Request, api_key, is_individual=None, min_date=None, max_image_number=None, min_image_number=None, contributor_type=None, contributor_id=None, recipient_committee_org_type=None, contributor_employer=None, sort_null_only=None, last_index=None, contributor_name=None, min_amount=None, sort_hide_null=None, recipient_committee_designation=None, max_load_date=None, recipient_committee_type=None, sort=None, last_contribution_receipt_date=None, last_contribution_receipt_amount=None, line_number=None, contributor_state=None, per_page=None, two_year_transaction_period=None, contributor_zip=None, min_load_date=None, contributor_occupation=None, contributor_city=None, committee_id=None, image_number=None, max_date=None, max_amount=None) -> web.Response:
    """schedules_schedule_aget

     This description is for both ​&#x60;/schedules​/schedule_a​/&#x60; and ​ &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60;.  This endpoint provides itemized receipts. Schedule A records describe itemized receipts, including contributions from individuals. If you are interested in contributions from an individual, use the &#x60;/schedules/schedule_a/&#x60; endpoint. For a more complete description of all Schedule A records visit [About receipts data](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/about-receipts-data/). If you are interested in our \&quot;is_individual\&quot; methodology visit our [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology/).  ​The &#x60;/schedules​/schedule_a​/&#x60; endpoint is not paginated by page number. This endpoint uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset. To request the next page, you should append the values found in the &#x60;last_indexes&#x60; object from pagination to the URL of your last request as additional parameters.  For example, when sorting by &#x60;contribution_receipt_date&#x60;, you might receive a page of results with the two scenarios of following pagination information:  case #1: &#x60;&#x60;&#x60; pagination: {     pages: 2152643,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880619\&quot;,         last_contribution_receipt_date: \&quot;2014-01-01\&quot;     } } &#x60;&#x60;&#x60; &lt;br/&gt; case #2 (results which include contribution_receipt_date &#x3D; NULL):  &#x60;&#x60;&#x60; pagination: {     pages: 2152644,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880639\&quot;,         sort_null_only: True     } } &#x60;&#x60;&#x60; To fetch the next page of sorted results, append &#x60;last_index&#x3D;230880619&#x60; and &#x60;last_contribution_receipt_date&#x3D;2014-01-01&#x60; to the URL and when reaching &#x60;contribution_receipt_date&#x3D;NULL&#x60;, append &#x60;last_index&#x3D;230880639&#x60; and &#x60;sort_null_only&#x3D;True&#x60;. We strongly advise paging through these results using sort indices. The default sort is acending by &#x60;contribution_receipt_date&#x60; (&#x60;deprecated&#x60;, will be descending). If you do not page using sort indices, some transactions may be unintentionally filtered out.  Calls to ​&#x60;/schedules​/schedule_a​/&#x60; may return many records. For large result sets, the record counts found in the pagination object are approximate; you will need to page through the records until no records are returned.  To avoid throwing the \&quot;out of range\&quot; exception on the last page, one recommandation is to use total count and &#x60;per_page&#x60; to control the traverse loop of results.  ​The &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60; endpoint returns a single transaction, but it does include a pagination object class. Please ignore the information in that object class.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param is_individual: Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals.
    :type is_individual: bool
    :param min_date: Minimum date
    :type min_date: str
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param contributor_type: Filters individual or committee contributions based on line number
    :type contributor_type: List[str]
    :param contributor_id: The FEC identifier should be represented here if the contributor is registered with the FEC.
    :type contributor_id: List[str]
    :param recipient_committee_org_type: The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    :type recipient_committee_org_type: List[str]
    :param contributor_employer: Employer of contributor, filers need to make an effort to gather this information
    :type contributor_employer: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param last_index: Index of last result from previous page
    :type last_index: int
    :param contributor_name: Name of contributor
    :type contributor_name: List[str]
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param recipient_committee_designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type recipient_committee_designation: List[str]
    :param max_load_date: Maximum load date
    :type max_load_date: str
    :param recipient_committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type recipient_committee_type: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param last_contribution_receipt_date: When sorting by &#x60;contribution_receipt_date&#x60;, this is populated with the         &#x60;contribution_receipt_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page.
    :type last_contribution_receipt_date: str
    :param last_contribution_receipt_amount: When sorting by &#x60;contribution_receipt_amount&#x60;, this is populated with the         &#x60;contribution_receipt_amount&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page.
    :type last_contribution_receipt_amount: float
    :param line_number: Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.
    :type line_number: str
    :param contributor_state: State of contributor
    :type contributor_state: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param two_year_transaction_period:  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
    :type two_year_transaction_period: List[int]
    :param contributor_zip: Zip code of contributor
    :type contributor_zip: List[str]
    :param min_load_date: Minimum load date
    :type min_load_date: str
    :param contributor_occupation: Occupation of contributor, filers need to make an effort to gather this information
    :type contributor_occupation: List[str]
    :param contributor_city: City of contributor
    :type contributor_city: List[str]
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
    max_load_date = util.deserialize_date(max_load_date)
    last_contribution_receipt_date = util.deserialize_date(last_contribution_receipt_date)
    min_load_date = util.deserialize_date(min_load_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)
