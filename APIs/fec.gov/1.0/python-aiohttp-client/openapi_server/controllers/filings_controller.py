from typing import List, Dict
from aiohttp import web

from openapi_server.models.filings_page import FilingsPage
from openapi_server.models.operations_log_page import OperationsLogPage
from openapi_server import util


async def candidate_candidate_id_filings_get(request: web.Request, api_key, candidate_id, is_amended=None, min_receipt_date=None, form_category=None, request_type=None, primary_general_indicator=None, cycle=None, sort_null_only=None, max_receipt_date=None, sort_hide_null=None, file_number=None, per_page=None, office=None, sort=None, q_filer=None, district=None, filer_type=None, most_recent=None, report_type=None, committee_type=None, party=None, form_type=None, sort_nulls_last=None, page=None, state=None, report_year=None, amendment_indicator=None, document_type=None, beginning_image_number=None) -> web.Response:
    """candidate_candidate_id_filings_get

     All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param is_amended:  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
    :type is_amended: bool
    :param min_receipt_date:  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param form_category:  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ 
    :type form_category: List[str]
    :param request_type:  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status 
    :type request_type: List[str]
    :param primary_general_indicator:  Primary, general or special election indicator. 
    :type primary_general_indicator: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
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
    :param office: Federal office candidate runs for: H, S or P
    :type office: List[str]
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]
    :param q_filer:  Keyword search for filer name or ID 
    :type q_filer: List[str]
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param filer_type: The method used to file with the FEC, either electronic or on paper.
    :type filer_type: str
    :param most_recent:  Report is either new or is the most-recently filed amendment 
    :type most_recent: bool
    :param report_type: Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
    :type report_type: List[str]
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: str
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: List[str]
    :param form_type: The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
    :type form_type: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param report_year:  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    :type report_year: List[int]
    :param amendment_indicator: Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
    :type amendment_indicator: List[str]
    :param document_type:  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice 
    :type document_type: List[str]
    :param beginning_image_number:  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
    :type beginning_image_number: List[str]

    """
    min_receipt_date = util.deserialize_date(min_receipt_date)
    max_receipt_date = util.deserialize_date(max_receipt_date)
    return web.Response(status=200)


async def committee_committee_id_filings_get(request: web.Request, api_key, committee_id, is_amended=None, min_receipt_date=None, form_category=None, request_type=None, primary_general_indicator=None, cycle=None, sort_null_only=None, max_receipt_date=None, sort_hide_null=None, file_number=None, per_page=None, office=None, sort=None, q_filer=None, district=None, filer_type=None, most_recent=None, report_type=None, committee_type=None, party=None, form_type=None, sort_nulls_last=None, page=None, state=None, report_year=None, amendment_indicator=None, document_type=None, beginning_image_number=None) -> web.Response:
    """committee_committee_id_filings_get

     All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param is_amended:  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
    :type is_amended: bool
    :param min_receipt_date:  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param form_category:  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ 
    :type form_category: List[str]
    :param request_type:  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status 
    :type request_type: List[str]
    :param primary_general_indicator:  Primary, general or special election indicator. 
    :type primary_general_indicator: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
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
    :param office: Federal office candidate runs for: H, S or P
    :type office: List[str]
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]
    :param q_filer:  Keyword search for filer name or ID 
    :type q_filer: List[str]
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param filer_type: The method used to file with the FEC, either electronic or on paper.
    :type filer_type: str
    :param most_recent:  Report is either new or is the most-recently filed amendment 
    :type most_recent: bool
    :param report_type: Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
    :type report_type: List[str]
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: str
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: List[str]
    :param form_type: The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
    :type form_type: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param report_year:  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    :type report_year: List[int]
    :param amendment_indicator: Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
    :type amendment_indicator: List[str]
    :param document_type:  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice 
    :type document_type: List[str]
    :param beginning_image_number:  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
    :type beginning_image_number: List[str]

    """
    min_receipt_date = util.deserialize_date(min_receipt_date)
    max_receipt_date = util.deserialize_date(max_receipt_date)
    return web.Response(status=200)


async def filings_get(request: web.Request, api_key, is_amended=None, min_receipt_date=None, form_category=None, request_type=None, primary_general_indicator=None, cycle=None, sort_null_only=None, max_receipt_date=None, sort_hide_null=None, candidate_id=None, file_number=None, per_page=None, office=None, sort=None, q_filer=None, district=None, filer_type=None, most_recent=None, report_type=None, committee_type=None, party=None, form_type=None, sort_nulls_last=None, page=None, state=None, report_year=None, committee_id=None, amendment_indicator=None, document_type=None, beginning_image_number=None) -> web.Response:
    """filings_get

     All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param is_amended:  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
    :type is_amended: bool
    :param min_receipt_date:  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param form_category:  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ 
    :type form_category: List[str]
    :param request_type:  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status 
    :type request_type: List[str]
    :param primary_general_indicator:  Primary, general or special election indicator. 
    :type primary_general_indicator: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param max_receipt_date:  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_receipt_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param file_number: Filing ID number
    :type file_number: List[int]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param office: Federal office candidate runs for: H, S or P
    :type office: List[str]
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]
    :param q_filer:  Keyword search for filer name or ID 
    :type q_filer: List[str]
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param filer_type: The method used to file with the FEC, either electronic or on paper.
    :type filer_type: str
    :param most_recent:  Report is either new or is the most-recently filed amendment 
    :type most_recent: bool
    :param report_type: Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
    :type report_type: List[str]
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: str
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: List[str]
    :param form_type: The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
    :type form_type: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param report_year:  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    :type report_year: List[int]
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param amendment_indicator: Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
    :type amendment_indicator: List[str]
    :param document_type:  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice 
    :type document_type: List[str]
    :param beginning_image_number:  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
    :type beginning_image_number: List[str]

    """
    min_receipt_date = util.deserialize_date(min_receipt_date)
    max_receipt_date = util.deserialize_date(max_receipt_date)
    return web.Response(status=200)


async def operations_log_get(request: web.Request, api_key, min_receipt_date=None, candidate_committee_id=None, sort_null_only=None, max_receipt_date=None, sort_hide_null=None, max_transaction_data_complete_date=None, per_page=None, sort=None, report_type=None, min_transaction_data_complete_date=None, form_type=None, sort_nulls_last=None, max_coverage_end_date=None, page=None, report_year=None, status_num=None, amendment_indicator=None, beginning_image_number=None, min_coverage_end_date=None) -> web.Response:
    """operations_log_get

     The Operations log contains details of each report loaded into the database. It is primarily used as status check to determine when all of the data processes, from initial entry through review are complete. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_receipt_date:  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_receipt_date: str
    :param candidate_committee_id:  A unique identifier of the registered filer. 
    :type candidate_committee_id: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param max_receipt_date:  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_receipt_date: str
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param max_transaction_data_complete_date:  Select all filings processed completely before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_transaction_data_complete_date: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]
    :param report_type: Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
    :type report_type: List[str]
    :param min_transaction_data_complete_date:  Select all filings processed completely after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_transaction_data_complete_date: str
    :param form_type: The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
    :type form_type: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param max_coverage_end_date:  Ending date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type max_coverage_end_date: str
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param report_year:  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    :type report_year: List[int]
    :param status_num:  Status of the transactional report.     -0- Transaction is entered            into the system.           But not verified.     -1- Transaction is verified. 
    :type status_num: List[str]
    :param amendment_indicator: Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
    :type amendment_indicator: List[str]
    :param beginning_image_number:  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
    :type beginning_image_number: List[str]
    :param min_coverage_end_date:  Ending date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD) 
    :type min_coverage_end_date: str

    """
    min_receipt_date = util.deserialize_date(min_receipt_date)
    max_receipt_date = util.deserialize_date(max_receipt_date)
    max_transaction_data_complete_date = util.deserialize_date(max_transaction_data_complete_date)
    min_transaction_data_complete_date = util.deserialize_date(min_transaction_data_complete_date)
    max_coverage_end_date = util.deserialize_date(max_coverage_end_date)
    min_coverage_end_date = util.deserialize_date(min_coverage_end_date)
    return web.Response(status=200)
