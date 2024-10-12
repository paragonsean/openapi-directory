from typing import List, Dict
from aiohttp import web

from openapi_server.models.committee_detail_page import CommitteeDetailPage
from openapi_server.models.committee_history_profile_page import CommitteeHistoryProfilePage
from openapi_server.models.committee_page import CommitteePage
from openapi_server import util


async def candidate_candidate_id_committees_get(request: web.Request, api_key, candidate_id, committee_type=None, cycle=None, sort_null_only=None, page=None, year=None, sort_nulls_last=None, sort_hide_null=None, per_page=None, filing_frequency=None, organization_type=None, designation=None, sort=None) -> web.Response:
    """candidate_candidate_id_committees_get

     This endpoint is useful for finding detailed information about a particular committee or filer. Use the &#x60;committee_id&#x60; to find the most recent information about the committee. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: List[str]
    :param cycle:  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param year: A year that the committee was active— (after original registration date     or filing but before expiration date)
    :type year: List[int]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param filing_frequency: The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived 
    :type filing_frequency: List[str]
    :param organization_type: The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    :type organization_type: List[str]
    :param designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type designation: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def candidate_candidate_id_committees_history_cycle_get(request: web.Request, api_key, cycle, candidate_id, election_full=None, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, per_page=None, designation=None, sort=None) -> web.Response:
    """candidate_candidate_id_committees_history_cycle_get

     Explore a filer&#39;s characteristics over time. This can be particularly useful if the committees change treasurers, designation, or &#x60;committee_type&#x60;. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: int
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
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
    :param designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type designation: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def candidate_candidate_id_committees_history_get(request: web.Request, api_key, candidate_id, election_full=None, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, per_page=None, designation=None, sort=None) -> web.Response:
    """candidate_candidate_id_committees_history_get

     Explore a filer&#39;s characteristics over time. This can be particularly useful if the committees change treasurers, designation, or &#x60;committee_type&#x60;. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
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
    :param designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type designation: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def committee_committee_id_get(request: web.Request, api_key, committee_id, committee_type=None, cycle=None, sort_null_only=None, page=None, year=None, sort_nulls_last=None, sort_hide_null=None, per_page=None, filing_frequency=None, organization_type=None, designation=None, sort=None) -> web.Response:
    """committee_committee_id_get

     This endpoint is useful for finding detailed information about a particular committee or filer. Use the &#x60;committee_id&#x60; to find the most recent information about the committee. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: List[str]
    :param cycle:  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param year: A year that the committee was active— (after original registration date     or filing but before expiration date)
    :type year: List[int]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param filing_frequency: The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived 
    :type filing_frequency: List[str]
    :param organization_type: The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    :type organization_type: List[str]
    :param designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type designation: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def committee_committee_id_history_cycle_get(request: web.Request, api_key, committee_id, cycle, election_full=None, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, per_page=None, designation=None, sort=None) -> web.Response:
    """committee_committee_id_history_cycle_get

     Explore a filer&#39;s characteristics over time. This can be particularly useful if the committees change treasurers, designation, or &#x60;committee_type&#x60;. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param cycle:  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: int
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
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
    :param designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type designation: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def committee_committee_id_history_get(request: web.Request, api_key, committee_id, election_full=None, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, per_page=None, designation=None, sort=None) -> web.Response:
    """committee_committee_id_history_get

     Explore a filer&#39;s characteristics over time. This can be particularly useful if the committees change treasurers, designation, or &#x60;committee_type&#x60;. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
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
    :param designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type designation: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def committees_get(request: web.Request, api_key, treasurer_name=None, q=None, min_first_file_date=None, cycle=None, sponsor_candidate_id=None, sort_null_only=None, sort_hide_null=None, candidate_id=None, per_page=None, filing_frequency=None, sort=None, max_first_file_date=None, min_first_f1_date=None, min_last_f1_date=None, committee_type=None, party=None, sort_nulls_last=None, page=None, year=None, committee_id=None, state=None, max_last_f1_date=None, max_first_f1_date=None, designation=None, organization_type=None) -> web.Response:
    """committees_get

     Fetch basic information about committees and filers. Use parameters to filter for particular characteristics.  

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param treasurer_name: Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown.
    :type treasurer_name: List[str]
    :param q: The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.
    :type q: List[str]
    :param min_first_file_date: Filter for committees whose first filing was received on or after this date.
    :type min_first_file_date: str
    :param cycle:  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sponsor_candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. This is a filter for Leadership PAC sponsor. 
    :type sponsor_candidate_id: List[str]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param filing_frequency: The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived 
    :type filing_frequency: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param max_first_file_date: Filter for committees whose first filing was received on or before this date.
    :type max_first_file_date: str
    :param min_first_f1_date: Filter for committees whose first Form 1 was received on or after this date.
    :type min_first_f1_date: str
    :param min_last_f1_date: Filter for committees whose latest Form 1 was received on or after this date.
    :type min_last_f1_date: str
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: List[str]
    :param party: Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    :type party: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param year: A year that the committee was active— (after original registration date     or filing but before expiration date)
    :type year: List[int]
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param state: US state or territory
    :type state: List[str]
    :param max_last_f1_date: Filter for committees whose latest Form 1 was received on or before this date.
    :type max_last_f1_date: str
    :param max_first_f1_date: Filter for committees whose first Form 1 was received on or before this date.
    :type max_first_f1_date: str
    :param designation: The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    :type designation: List[str]
    :param organization_type: The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    :type organization_type: List[str]

    """
    min_first_file_date = util.deserialize_date(min_first_file_date)
    max_first_file_date = util.deserialize_date(max_first_file_date)
    min_first_f1_date = util.deserialize_date(min_first_f1_date)
    min_last_f1_date = util.deserialize_date(min_last_f1_date)
    max_last_f1_date = util.deserialize_date(max_last_f1_date)
    max_first_f1_date = util.deserialize_date(max_first_f1_date)
    return web.Response(status=200)
