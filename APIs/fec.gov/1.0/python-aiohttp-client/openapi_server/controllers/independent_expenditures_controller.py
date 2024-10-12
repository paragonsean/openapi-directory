from typing import List, Dict
from aiohttp import web

from openapi_server.models.ie_totals_by_candidate_page import IETotalsByCandidatePage
from openapi_server.models.schedule_eby_candidate_page import ScheduleEByCandidatePage
from openapi_server.models.schedule_e_efile_page import ScheduleEEfilePage
from openapi_server.models.schedule_e_page import ScheduleEPage
from openapi_server import util


async def schedules_schedule_e_efile_get(request: web.Request, api_key, max_expenditure_amount=None, support_oppose_indicator=None, min_expenditure_date=None, filing_form=None, max_expenditure_date=None, max_filed_date=None, is_notice=None, sort_null_only=None, sort_hide_null=None, payee_name=None, candidate_id=None, per_page=None, candidate_office_district=None, sort=None, min_expenditure_amount=None, spender_name=None, min_dissemination_date=None, candidate_office_state=None, sort_nulls_last=None, page=None, committee_id=None, candidate_search=None, image_number=None, candidate_party=None, min_filed_date=None, max_dissemination_date=None, most_recent=None, candidate_office=None) -> web.Response:
    """schedules_schedule_e_efile_get

     Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don&#39;t contain the processed and coded data that you can find on other endpoints. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param max_expenditure_amount: Selects all items expended by this committee less than this amount
    :type max_expenditure_amount: int
    :param support_oppose_indicator: Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs.
    :type support_oppose_indicator: List[str]
    :param min_expenditure_date: Selects all items expended by this committee after this date
    :type min_expenditure_date: str
    :param filing_form: The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
    :type filing_form: List[str]
    :param max_expenditure_date: Selects all items expended by this committee before this date
    :type max_expenditure_date: str
    :param max_filed_date: Timestamp of electronic or paper record that FEC received
    :type max_filed_date: str
    :param is_notice:  Record filed as 24- or 48-hour notice. 
    :type is_notice: bool
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param payee_name:  Name of the entity that received the payment. 
    :type payee_name: List[str]
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param candidate_office_district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type candidate_office_district: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param min_expenditure_amount: Selects all items expended by this committee greater than this amount
    :type min_expenditure_amount: int
    :param spender_name: The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.
    :type spender_name: List[str]
    :param min_dissemination_date: Selects all items distributed by this committee after this date
    :type min_dissemination_date: str
    :param candidate_office_state: US state or territory where a candidate runs for office
    :type candidate_office_state: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param candidate_search:  Search for candidates by candiate id or candidate first or last name 
    :type candidate_search: List[str]
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param candidate_party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type candidate_party: List[str]
    :param min_filed_date: Timestamp of electronic or paper record that FEC received
    :type min_filed_date: str
    :param max_dissemination_date: Selects all items distributed by this committee before this date
    :type max_dissemination_date: str
    :param most_recent:  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included. 
    :type most_recent: bool
    :param candidate_office: Federal office candidate runs for: H, S or P
    :type candidate_office: str

    """
    min_expenditure_date = util.deserialize_date(min_expenditure_date)
    max_expenditure_date = util.deserialize_date(max_expenditure_date)
    max_filed_date = util.deserialize_date(max_filed_date)
    min_dissemination_date = util.deserialize_date(min_dissemination_date)
    min_filed_date = util.deserialize_date(min_filed_date)
    max_dissemination_date = util.deserialize_date(max_dissemination_date)
    return web.Response(status=200)


async def schedules_schedule_e_totals_by_candidate_get(request: web.Request, api_key, election_full=None, cycle=None, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, candidate_id=None, per_page=None, sort=None) -> web.Response:
    """schedules_schedule_e_totals_by_candidate_get

     Total independent expenditure on supported or opposed candidates by cycle or candidate election year. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_eby_candidate_get(request: web.Request, api_key, district=None, support_oppose=None, election_full=None, cycle=None, sort_null_only=None, page=None, state=None, committee_id=None, sort_nulls_last=None, sort_hide_null=None, candidate_id=None, per_page=None, office=None, sort=None) -> web.Response:
    """schedules_schedule_eby_candidate_get

     Schedule E receipts aggregated by recipient candidate. To avoid double counting, memoed items are not included. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: str
    :param support_oppose: Support or opposition
    :type support_oppose: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param office: Federal office candidate runs for: H, S or P
    :type office: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def schedules_schedule_eget(request: web.Request, api_key, last_expenditure_date=None, max_image_number=None, is_notice=None, payee_name=None, min_amount=None, candidate_id=None, sort_hide_null=None, last_office_total_ytd=None, sort=None, min_filing_date=None, q_spender=None, min_dissemination_date=None, candidate_office_state=None, sort_nulls_last=None, last_expenditure_amount=None, image_number=None, max_date=None, max_dissemination_date=None, min_date=None, filing_form=None, support_oppose_indicator=None, min_image_number=None, cycle=None, max_filing_date=None, sort_null_only=None, last_support_oppose_indicator=None, last_index=None, per_page=None, candidate_office_district=None, line_number=None, committee_id=None, candidate_party=None, max_amount=None, most_recent=None, candidate_office=None) -> web.Response:
    """schedules_schedule_eget

     Schedule E covers the line item expenditures for independent expenditures. For example, if a super PAC bought ads on TV to oppose a federal candidate, each ad purchase would be recorded here with the expenditure amount, name and id of the candidate, and whether the ad supported or opposed the candidate.  An independent expenditure is an expenditure for a communication \&quot;expressly advocating the election or defeat of a clearly identified candidate that is not made in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate, a candidate’s authorized committee, or their agents, or a political party or its agents.\&quot;  Aggregates by candidate do not include 24 and 48 hour reports. This ensures we don&#39;t double count expenditures and the totals are more accurate. You can still find the information from 24 and 48 hour reports in &#x60;/schedule/schedule_e/&#x60;.  Due to the large quantity of Schedule E filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;expenditure_amount&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60;  \&quot;pagination\&quot;: {     \&quot;count\&quot;: 152623,     \&quot;last_indexes\&quot;: {       \&quot;last_index\&quot;: \&quot;3023037\&quot;,       \&quot;last_expenditure_amount\&quot;: -17348.5     },     \&quot;per_page\&quot;: 20,     \&quot;pages\&quot;: 7632   } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;3023037&#x60; and &#x60;last_expenditure_amount&#x3D;&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out.  This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule E data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param last_expenditure_date:  When sorting by &#x60;expenditure_date&#x60;, this is populated with the &#x60;expenditure_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. 
    :type last_expenditure_date: str
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param is_notice:  Record filed as 24- or 48-hour notice. 
    :type is_notice: List[bool]
    :param payee_name:  Name of the entity that received the payment. 
    :type payee_name: List[str]
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param last_office_total_ytd:  When sorting by &#x60;office_total_ytd&#x60;, this is populated with the &#x60;office_total_ytd&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39; 
    :type last_office_total_ytd: float
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param min_filing_date:  Selects all filings received after this date 
    :type min_filing_date: str
    :param q_spender:  Keyword search for spender name or ID 
    :type q_spender: List[str]
    :param min_dissemination_date: Selects all items distributed by this committee after this date
    :type min_dissemination_date: str
    :param candidate_office_state: US state or territory
    :type candidate_office_state: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param last_expenditure_amount:  When sorting by &#x60;expenditure_amount&#x60;, this is populated with the &#x60;expenditure_amount&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. 
    :type last_expenditure_amount: float
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param max_date: Maximum date
    :type max_date: str
    :param max_dissemination_date: Selects all items distributed by this committee before this date
    :type max_dissemination_date: str
    :param min_date: Minimum date
    :type min_date: str
    :param filing_form: The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
    :type filing_form: List[str]
    :param support_oppose_indicator: Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs.
    :type support_oppose_indicator: List[str]
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param max_filing_date:  Selects all filings received before this date 
    :type max_filing_date: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param last_support_oppose_indicator:  When sorting by &#x60;support_oppose_indicator&#x60;, this is populated with the &#x60;support_oppose_indicator&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39; 
    :type last_support_oppose_indicator: str
    :param last_index: Index of last result from previous page
    :type last_index: int
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param candidate_office_district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type candidate_office_district: List[str]
    :param line_number: Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.
    :type line_number: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param candidate_party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type candidate_party: List[str]
    :param max_amount: Filter for all amounts less than a value.
    :type max_amount: str
    :param most_recent:  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included. 
    :type most_recent: bool
    :param candidate_office: Federal office candidate runs for: H, S or P
    :type candidate_office: List[str]

    """
    last_expenditure_date = util.deserialize_date(last_expenditure_date)
    min_filing_date = util.deserialize_date(min_filing_date)
    min_dissemination_date = util.deserialize_date(min_dissemination_date)
    max_date = util.deserialize_date(max_date)
    max_dissemination_date = util.deserialize_date(max_dissemination_date)
    min_date = util.deserialize_date(min_date)
    max_filing_date = util.deserialize_date(max_filing_date)
    return web.Response(status=200)
