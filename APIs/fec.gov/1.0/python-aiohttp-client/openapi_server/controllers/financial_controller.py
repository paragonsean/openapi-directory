from typing import List, Dict
from aiohttp import web

from openapi_server.models.committee_reports_page import CommitteeReportsPage
from openapi_server.models.committee_totals_page import CommitteeTotalsPage
from openapi_server.models.election_page import ElectionPage
from openapi_server.models.election_summary import ElectionSummary
from openapi_server.models.elections_list_page import ElectionsListPage
from openapi_server.models.entity_receipt_disbursement_totals_page import EntityReceiptDisbursementTotalsPage
from openapi_server.models.inaugural_donations_page import InauguralDonationsPage
from openapi_server import util


async def committee_committee_id_reports_get(request: web.Request, api_key, committee_id, min_party_coordinated_expenditures=None, is_amended=None, max_party_coordinated_expenditures=None, max_cash_on_hand_end_period_amount=None, max_disbursements_amount=None, max_debts_owed_expenditures=None, min_receipts_amount=None, cycle=None, sort_null_only=None, min_debts_owed_amount=None, sort_hide_null=None, candidate_id=None, min_independent_expenditures=None, per_page=None, sort=None, max_receipts_amount=None, report_type=None, max_total_contributions=None, sort_nulls_last=None, page=None, year=None, max_independent_expenditures=None, type=None, min_cash_on_hand_end_period_amount=None, min_disbursements_amount=None, min_total_contributions=None, beginning_image_number=None) -> web.Response:
    """committee_committee_id_reports_get

     Each report represents the summary information from Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee&#39;s financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use &#x60;is_amended&#x3D;false&#x60;; to retrieve only reports that have been amended, use &#x60;is_amended&#x3D;true&#x60;.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param min_party_coordinated_expenditures:  Filter for all amounts greater than a value. 
    :type min_party_coordinated_expenditures: str
    :param is_amended:  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
    :type is_amended: bool
    :param max_party_coordinated_expenditures:  Filter for all amounts less than a value. 
    :type max_party_coordinated_expenditures: str
    :param max_cash_on_hand_end_period_amount:  Filter for all amounts less than a value. 
    :type max_cash_on_hand_end_period_amount: str
    :param max_disbursements_amount:  Filter for all amounts less than a value. 
    :type max_disbursements_amount: str
    :param max_debts_owed_expenditures:  Filter for all amounts less than a value. 
    :type max_debts_owed_expenditures: str
    :param min_receipts_amount:  Filter for all amounts greater than a value. 
    :type min_receipts_amount: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param min_debts_owed_amount:  Filter for all amounts greater than a value. 
    :type min_debts_owed_amount: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param min_independent_expenditures:  Filter for all amounts greater than a value. 
    :type min_independent_expenditures: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]
    :param max_receipts_amount:  Filter for all amounts less than a value. 
    :type max_receipts_amount: str
    :param report_type: Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND 
    :type report_type: List[str]
    :param max_total_contributions:  Filter for all amounts less than a value. 
    :type max_total_contributions: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param year:  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    :type year: List[int]
    :param max_independent_expenditures:  Filter for all amounts less than a value. 
    :type max_independent_expenditures: str
    :param type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type type: List[str]
    :param min_cash_on_hand_end_period_amount:  Filter for all amounts greater than a value. 
    :type min_cash_on_hand_end_period_amount: str
    :param min_disbursements_amount:  Filter for all amounts greater than a value. 
    :type min_disbursements_amount: str
    :param min_total_contributions:  Filter for all amounts greater than a value. 
    :type min_total_contributions: str
    :param beginning_image_number:  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
    :type beginning_image_number: List[str]

    """
    return web.Response(status=200)


async def committee_committee_id_totals_get(request: web.Request, api_key, committee_id, page=None, sort_hide_null=None, per_page=None, sort_nulls_last=None, sort=None, cycle=None, sort_null_only=None) -> web.Response:
    """committee_committee_id_totals_get

     This endpoint provides information about a committee&#39;s Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a &#x60;cycle&#x60;.  The cycle is named after the even-numbered year and includes the year before it. To obtain totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool

    """
    return web.Response(status=200)


async def elections_get(request: web.Request, api_key, cycle, office, district=None, election_full=None, sort_null_only=None, page=None, state=None, sort_nulls_last=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """elections_get

     Look at the top-level financial information for all candidates running for the same office.  Choose a 2-year cycle, and &#x60;house&#x60;, &#x60;senate&#x60; or &#x60;presidential&#x60;.  If you are looking for a Senate seat, you will need to select the state using a two-letter abbreviation.  House races require state and a two-digit district number.  Since this endpoint reflects financial information, it will only have candidates once they file financial reporting forms. Query the &#x60;/candidates&#x60; endpoint to retrieve an-up-to-date list of all the candidates that filed to run for a particular seat. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: int
    :param office: Federal office candidate runs for: H, S or P
    :type office: str
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: str
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


async def elections_search_get(request: web.Request, api_key, zip=None, district=None, cycle=None, sort_null_only=None, sort_nulls_last=None, page=None, state=None, sort_hide_null=None, per_page=None, office=None, sort=None) -> web.Response:
    """elections_search_get

     List elections by cycle, office, state, and district. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param zip: Zip code
    :type zip: List[int]
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param office: 
    :type office: List[str]
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]

    """
    return web.Response(status=200)


async def elections_summary_get(request: web.Request, api_key, office, cycle, state=None, district=None, election_full=None) -> web.Response:
    """elections_summary_get

     List elections by cycle, office, state, and district. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param office: Federal office candidate runs for: H, S or P
    :type office: str
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: int
    :param state: US state or territory where a candidate runs for office
    :type state: str
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool

    """
    return web.Response(status=200)


async def reports_entity_type_get(request: web.Request, api_key, entity_type, max_party_coordinated_expenditures=None, max_debts_owed_expenditures=None, min_receipts_amount=None, min_debts_owed_amount=None, max_receipt_date=None, sort_hide_null=None, candidate_id=None, sort=None, q_spender=None, max_receipts_amount=None, filer_type=None, report_type=None, max_total_contributions=None, sort_nulls_last=None, max_independent_expenditures=None, min_total_contributions=None, min_party_coordinated_expenditures=None, beginning_image_number=None, min_receipt_date=None, is_amended=None, max_disbursements_amount=None, max_cash_on_hand_end_period_amount=None, amendment_indicator=None, cycle=None, sort_null_only=None, min_independent_expenditures=None, per_page=None, q_filer=None, committee_type=None, page=None, year=None, committee_id=None, min_cash_on_hand_end_period_amount=None, min_disbursements_amount=None, most_recent=None) -> web.Response:
    """reports_entity_type_get

     Each report represents the summary information from Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee&#39;s financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use &#x60;is_amended&#x3D;false&#x60;; to retrieve only reports that have been amended, use &#x60;is_amended&#x3D;true&#x60;.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param entity_type: Committee groupings based on FEC filing form.                 Choose one of: &#x60;presidential&#x60;, &#x60;pac-party&#x60;, &#x60;house-senate&#x60;, or &#x60;ie-only&#x60;
    :type entity_type: str
    :param max_party_coordinated_expenditures:  Filter for all amounts less than a value. 
    :type max_party_coordinated_expenditures: str
    :param max_debts_owed_expenditures:  Filter for all amounts less than a value. 
    :type max_debts_owed_expenditures: str
    :param min_receipts_amount:  Filter for all amounts greater than a value. 
    :type min_receipts_amount: str
    :param min_debts_owed_amount:  Filter for all amounts greater than a value. 
    :type min_debts_owed_amount: str
    :param max_receipt_date:  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_receipt_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]
    :param q_spender:  Keyword search for spender name or ID 
    :type q_spender: List[str]
    :param max_receipts_amount:  Filter for all amounts less than a value. 
    :type max_receipts_amount: str
    :param filer_type: The method used to file with the FEC, either electronic or on paper.
    :type filer_type: str
    :param report_type: Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND 
    :type report_type: List[str]
    :param max_total_contributions:  Filter for all amounts less than a value. 
    :type max_total_contributions: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param max_independent_expenditures:  Filter for all amounts less than a value. 
    :type max_independent_expenditures: str
    :param min_total_contributions:  Filter for all amounts greater than a value. 
    :type min_total_contributions: str
    :param min_party_coordinated_expenditures:  Filter for all amounts greater than a value. 
    :type min_party_coordinated_expenditures: str
    :param beginning_image_number:  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
    :type beginning_image_number: List[str]
    :param min_receipt_date:  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param is_amended:  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
    :type is_amended: bool
    :param max_disbursements_amount:  Filter for all amounts less than a value. 
    :type max_disbursements_amount: str
    :param max_cash_on_hand_end_period_amount:  Filter for all amounts less than a value. 
    :type max_cash_on_hand_end_period_amount: str
    :param amendment_indicator: Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
    :type amendment_indicator: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param min_independent_expenditures:  Filter for all amounts greater than a value. 
    :type min_independent_expenditures: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param q_filer:  Keyword search for filer name or ID 
    :type q_filer: List[str]
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: List[str]
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param year:  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    :type year: List[int]
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param min_cash_on_hand_end_period_amount:  Filter for all amounts greater than a value. 
    :type min_cash_on_hand_end_period_amount: str
    :param min_disbursements_amount:  Filter for all amounts greater than a value. 
    :type min_disbursements_amount: str
    :param most_recent:  Report is either new or is the most-recently filed amendment 
    :type most_recent: bool

    """
    max_receipt_date = util.deserialize_date(max_receipt_date)
    min_receipt_date = util.deserialize_date(min_receipt_date)
    return web.Response(status=200)


async def totals_by_entity_get(request: web.Request, api_key, cycle, page=None, sort_hide_null=None, per_page=None, sort_null_only=None, sort=None, sort_nulls_last=None) -> web.Response:
    """totals_by_entity_get

     Provides cumulative receipt totals by entity type, over a two year cycle. Totals are adjusted to avoid double counting.  This is [the sql](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V41__large_aggregates.sql) that creates these calculations. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: int
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


async def totals_entity_type_get(request: web.Request, api_key, entity_type, treasurer_name=None, max_disbursements=None, committee_state=None, cycle=None, sort_null_only=None, sponsor_candidate_id=None, min_disbursements=None, min_last_cash_on_hand_end_period=None, max_last_cash_on_hand_end_period=None, sort_hide_null=None, per_page=None, filing_frequency=None, sort=None, max_last_debts_owed_by_committee=None, min_first_f1_date=None, committee_designation=None, max_receipts=None, committee_type=None, sort_nulls_last=None, page=None, committee_id=None, min_last_debts_owed_by_committee=None, max_first_f1_date=None, organization_type=None, min_receipts=None) -> web.Response:
    """totals_entity_type_get

     This endpoint provides information about a committee&#39;s Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a &#x60;cycle&#x60;.  The cycle is named after the even-numbered year and includes the year before it. To obtain totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param entity_type: Committee groupings based on FEC filing form.                 Choose one of: &#x60;presidential&#x60;, &#x60;pac&#x60;, &#x60;party&#x60;, &#x60;pac-party&#x60;,                 &#x60;house-senate&#x60;, or &#x60;ie-only&#x60;
    :type entity_type: str
    :param treasurer_name: Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown.
    :type treasurer_name: List[str]
    :param max_disbursements:  Filter for all amounts less than a value. 
    :type max_disbursements: str
    :param committee_state: US state or territory
    :type committee_state: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sponsor_candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. This is a filter for Leadership PAC sponsor. 
    :type sponsor_candidate_id: List[str]
    :param min_disbursements:  Filter for all amounts greater than a value. 
    :type min_disbursements: str
    :param min_last_cash_on_hand_end_period:  Filter for all amounts greater than a value. 
    :type min_last_cash_on_hand_end_period: str
    :param max_last_cash_on_hand_end_period:  Filter for all amounts less than a value. 
    :type max_last_cash_on_hand_end_period: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param filing_frequency: The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived 
    :type filing_frequency: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param max_last_debts_owed_by_committee:  Filter for all amounts less than a value. 
    :type max_last_debts_owed_by_committee: str
    :param min_first_f1_date: Filter for committees whose first Form 1 was received on or after this date.
    :type min_first_f1_date: str
    :param committee_designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type committee_designation: List[str]
    :param max_receipts:  Filter for all amounts less than a value. 
    :type max_receipts: str
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param min_last_debts_owed_by_committee:  Filter for all amounts greater than a value. 
    :type min_last_debts_owed_by_committee: str
    :param max_first_f1_date: Filter for committees whose first Form 1 was received on or before this date.
    :type max_first_f1_date: str
    :param organization_type: The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    :type organization_type: List[str]
    :param min_receipts:  Filter for all amounts greater than a value. 
    :type min_receipts: str

    """
    min_first_f1_date = util.deserialize_date(min_first_f1_date)
    max_first_f1_date = util.deserialize_date(max_first_f1_date)
    return web.Response(status=200)


async def totals_inaugural_committees_by_contributor_get(request: web.Request, api_key, cycle=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, contributor_name=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """totals_inaugural_committees_by_contributor_get

     This endpoint provides information about an inaugural committee&#39;s Form 13 report of donations accepted. The data is aggregated by the contributor and the two-year period. We refer to two-year periods as a &#x60;cycle&#x60;.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param contributor_name: Name of contributor
    :type contributor_name: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]

    """
    return web.Response(status=200)
