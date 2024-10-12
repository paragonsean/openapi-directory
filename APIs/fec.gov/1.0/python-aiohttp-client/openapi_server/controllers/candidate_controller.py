from typing import List, Dict
from aiohttp import web

from openapi_server.models.candidate_detail_page import CandidateDetailPage
from openapi_server.models.candidate_history_page import CandidateHistoryPage
from openapi_server.models.candidate_history_total_page import CandidateHistoryTotalPage
from openapi_server.models.candidate_page import CandidatePage
from openapi_server.models.candidate_total_aggregate_page import CandidateTotalAggregatePage
from openapi_server.models.committee_totals_page import CommitteeTotalsPage
from openapi_server.models.total_by_office_by_party_page import TotalByOfficeByPartyPage
from openapi_server.models.total_by_office_page import TotalByOfficePage
from openapi_server import util


async def candidate_candidate_id_get(request: web.Request, api_key, candidate_id, incumbent_challenge=None, cycle=None, sort_null_only=None, federal_funds_flag=None, sort_hide_null=None, name=None, per_page=None, election_year=None, office=None, sort=None, candidate_status=None, district=None, has_raised_funds=None, party=None, sort_nulls_last=None, page=None, state=None, year=None) -> web.Response:
    """candidate_candidate_id_get

     This endpoint is useful for finding detailed information about a particular candidate. Use the &#x60;candidate_id&#x60; to find the most recent information about that candidate. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param incumbent_challenge: One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open.
    :type incumbent_challenge: List[str]
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param federal_funds_flag: A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    :type federal_funds_flag: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param name: Name (candidate or committee) to search for. Alias for &#39;q&#39;.
    :type name: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param office: Federal office candidate runs for: H, S or P
    :type office: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param candidate_status: One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
    :type candidate_status: List[str]
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param has_raised_funds: A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    :type has_raised_funds: bool
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param year: Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
    :type year: str

    """
    return web.Response(status=200)


async def candidate_candidate_id_history_cycle_get(request: web.Request, api_key, cycle, candidate_id, page=None, sort_hide_null=None, election_full=None, per_page=None, sort_null_only=None, sort=None, sort_nulls_last=None) -> web.Response:
    """candidate_candidate_id_history_cycle_get

     Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: int
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
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


async def candidate_candidate_id_history_get(request: web.Request, api_key, candidate_id, page=None, sort_hide_null=None, election_full=None, per_page=None, sort_null_only=None, sort=None, sort_nulls_last=None) -> web.Response:
    """candidate_candidate_id_history_get

     Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
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


async def candidate_candidate_id_totals_get(request: web.Request, api_key, candidate_id, election_full=None, cycle=None, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, per_page=None, sort=None) -> web.Response:
    """candidate_candidate_id_totals_get

     This endpoint provides information about a committee&#39;s Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a &#x60;cycle&#x60;.  The cycle is named after the even-numbered year and includes the year before it. To obtain totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
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
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def candidates_get(request: web.Request, api_key, incumbent_challenge=None, min_first_file_date=None, q=None, cycle=None, sort_null_only=None, federal_funds_flag=None, sort_hide_null=None, candidate_id=None, name=None, per_page=None, election_year=None, office=None, sort=None, candidate_status=None, max_first_file_date=None, district=None, has_raised_funds=None, party=None, sort_nulls_last=None, is_active_candidate=None, page=None, state=None, year=None) -> web.Response:
    """candidates_get

     Fetch basic information about candidates, and use parameters to filter results to the candidates you&#39;re looking for.  Each result reflects a unique FEC candidate ID. That ID is particular to the candidate for a particular office sought. If a candidate runs for the same office multiple times, the ID stays the same. If the same person runs for another office — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param incumbent_challenge: One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open.
    :type incumbent_challenge: List[str]
    :param min_first_file_date: Selects all candidates whose first filing was received by the FEC after this date.
    :type min_first_file_date: str
    :param q: Name of candidate running for office
    :type q: List[str]
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param federal_funds_flag: A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    :type federal_funds_flag: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param name: Name (candidate or committee) to search for. Alias for &#39;q&#39;.
    :type name: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param office: Federal office candidate runs for: H, S or P
    :type office: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param candidate_status: One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
    :type candidate_status: List[str]
    :param max_first_file_date: Selects all candidates whose first filing was received by the FEC before this date.
    :type max_first_file_date: str
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param has_raised_funds: A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    :type has_raised_funds: bool
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param is_active_candidate:  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    :type is_active_candidate: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param year: Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
    :type year: str

    """
    min_first_file_date = util.deserialize_date(min_first_file_date)
    max_first_file_date = util.deserialize_date(max_first_file_date)
    return web.Response(status=200)


async def candidates_search_get(request: web.Request, api_key, incumbent_challenge=None, min_first_file_date=None, q=None, cycle=None, sort_null_only=None, federal_funds_flag=None, sort_hide_null=None, candidate_id=None, name=None, per_page=None, election_year=None, office=None, sort=None, candidate_status=None, max_first_file_date=None, district=None, has_raised_funds=None, party=None, sort_nulls_last=None, is_active_candidate=None, page=None, state=None, year=None) -> web.Response:
    """candidates_search_get

     Fetch basic information about candidates and their principal committees.  Each result reflects a unique FEC candidate ID. That ID is assigned to the candidate for a particular office sought. If a candidate runs for the same office over time, that ID stays the same. If the same person runs for multiple offices — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office.  The candidate endpoints primarily use data from FEC registration [Form 1](https://www.fec.gov/pdf/forms/fecfrm1.pdf) for committee information and [Form 2](https://www.fec.gov/pdf/forms/fecfrm2.pdf) for candidate information. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param incumbent_challenge: One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open.
    :type incumbent_challenge: List[str]
    :param min_first_file_date: Selects all candidates whose first filing was received by the FEC after this date.
    :type min_first_file_date: str
    :param q: Name of candidate running for office
    :type q: List[str]
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param federal_funds_flag: A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    :type federal_funds_flag: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param name: Name (candidate or committee) to search for. Alias for &#39;q&#39;.
    :type name: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param office: Federal office candidate runs for: H, S or P
    :type office: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param candidate_status: One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
    :type candidate_status: List[str]
    :param max_first_file_date: Selects all candidates whose first filing was received by the FEC before this date.
    :type max_first_file_date: str
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param has_raised_funds: A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    :type has_raised_funds: bool
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param is_active_candidate:  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    :type is_active_candidate: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param year: Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
    :type year: str

    """
    min_first_file_date = util.deserialize_date(min_first_file_date)
    max_first_file_date = util.deserialize_date(max_first_file_date)
    return web.Response(status=200)


async def candidates_totals_aggregates_get(request: web.Request, api_key, max_election_cycle=None, sort_null_only=None, sort_hide_null=None, per_page=None, election_year=None, office=None, sort=None, min_election_cycle=None, district=None, election_full=None, party=None, is_active_candidate=None, page=None, state=None, sort_nulls_last=None, aggregate_by=None) -> web.Response:
    """candidates_totals_aggregates_get

     Candidate total receipts and disbursements aggregated by &#x60;aggregate_by&#x60;. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param max_election_cycle:  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    :type max_election_cycle: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type election_year: List[int]
    :param office: Federal office candidate runs for: H, S or P
    :type office: str
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]
    :param min_election_cycle:  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    :type min_election_cycle: int
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: str
    :param is_active_candidate:  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    :type is_active_candidate: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param aggregate_by: Candidate totals aggregate_by (Chose one of dropdown options):         - &#39; &#39; grouped by election year         - office grouped by election year, by office         - office-state grouped by election year, by office, by state         - office-state-district grouped by election year, by office, by state, by district         - office-party grouped by election year, by office, by party 
    :type aggregate_by: str

    """
    return web.Response(status=200)


async def candidates_totals_by_office_by_party_get(request: web.Request, api_key, election_full=None, sort_null_only=None, page=None, is_active_candidate=None, sort_nulls_last=None, election_year=None, sort_hide_null=None, per_page=None, office=None, sort=None) -> web.Response:
    """candidates_totals_by_office_by_party_get

     Aggregated candidate receipts and disbursements grouped by office by party by cycle. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param is_active_candidate:  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    :type is_active_candidate: bool
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param election_year:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type election_year: List[int]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param office: Federal office candidate runs for: H, S or P
    :type office: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def candidates_totals_by_office_get(request: web.Request, api_key, max_election_cycle=None, election_full=None, is_active_candidate=None, page=None, sort_null_only=None, sort_nulls_last=None, election_year=None, sort_hide_null=None, per_page=None, office=None, sort=None, min_election_cycle=None) -> web.Response:
    """candidates_totals_by_office_get

     Aggregated candidate receipts and disbursements grouped by office by cycle. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param max_election_cycle:  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    :type max_election_cycle: int
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param is_active_candidate:  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    :type is_active_candidate: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param election_year:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type election_year: List[int]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param office: Federal office candidate runs for: H, S or P
    :type office: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param min_election_cycle:  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    :type min_election_cycle: int

    """
    return web.Response(status=200)


async def candidates_totals_get(request: web.Request, api_key, max_disbursements=None, q=None, cycle=None, sort_null_only=None, max_cash_on_hand_end_period=None, max_debts_owed_by_committee=None, min_disbursements=None, federal_funds_flag=None, sort_hide_null=None, candidate_id=None, per_page=None, election_year=None, office=None, sort=None, district=None, election_full=None, min_debts_owed_by_committee=None, max_receipts=None, has_raised_funds=None, party=None, sort_nulls_last=None, is_active_candidate=None, page=None, state=None, min_cash_on_hand_end_period=None, min_receipts=None) -> web.Response:
    """candidates_totals_get

     Aggregated candidate receipts and disbursements grouped by cycle. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param max_disbursements: Maximum aggregated disbursements
    :type max_disbursements: str
    :param q: Name of candidate running for office
    :type q: List[str]
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param max_cash_on_hand_end_period: Maximum cash on hand
    :type max_cash_on_hand_end_period: str
    :param max_debts_owed_by_committee: Maximum debt
    :type max_debts_owed_by_committee: str
    :param min_disbursements: Minimum aggregated disbursements
    :type min_disbursements: str
    :param federal_funds_flag: A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    :type federal_funds_flag: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type election_year: List[int]
    :param office: Federal office candidate runs for: H, S or P
    :type office: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param district: District of candidate
    :type district: List[str]
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param min_debts_owed_by_committee: Minimum debt
    :type min_debts_owed_by_committee: str
    :param max_receipts: Maximum aggregated receipts
    :type max_receipts: str
    :param has_raised_funds: A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    :type has_raised_funds: bool
    :param party: Three-letter party code
    :type party: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param is_active_candidate:  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    :type is_active_candidate: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: State of candidate
    :type state: List[str]
    :param min_cash_on_hand_end_period: Minimum cash on hand
    :type min_cash_on_hand_end_period: str
    :param min_receipts: Minimum aggregated receipts
    :type min_receipts: str

    """
    return web.Response(status=200)


async def committee_committee_id_candidates_get(request: web.Request, api_key, committee_id, incumbent_challenge=None, cycle=None, sort_null_only=None, federal_funds_flag=None, sort_hide_null=None, name=None, per_page=None, election_year=None, office=None, sort=None, candidate_status=None, district=None, has_raised_funds=None, party=None, sort_nulls_last=None, page=None, state=None, year=None) -> web.Response:
    """committee_committee_id_candidates_get

     This endpoint is useful for finding detailed information about a particular candidate. Use the &#x60;candidate_id&#x60; to find the most recent information about that candidate. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param incumbent_challenge: One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open.
    :type incumbent_challenge: List[str]
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param federal_funds_flag: A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    :type federal_funds_flag: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param name: Name (candidate or committee) to search for. Alias for &#39;q&#39;.
    :type name: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param office: Federal office candidate runs for: H, S or P
    :type office: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param candidate_status: One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
    :type candidate_status: List[str]
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: List[str]
    :param has_raised_funds: A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    :type has_raised_funds: bool
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: List[str]
    :param year: Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
    :type year: str

    """
    return web.Response(status=200)


async def committee_committee_id_candidates_history_cycle_get(request: web.Request, api_key, committee_id, cycle, page=None, sort_hide_null=None, election_full=None, per_page=None, sort_null_only=None, sort=None, sort_nulls_last=None) -> web.Response:
    """committee_committee_id_candidates_history_cycle_get

     Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param cycle:  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. 
    :type cycle: int
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
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


async def committee_committee_id_candidates_history_get(request: web.Request, api_key, committee_id, page=None, sort_hide_null=None, election_full=None, per_page=None, sort_null_only=None, sort=None, sort_nulls_last=None) -> web.Response:
    """committee_committee_id_candidates_history_get

     Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
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
