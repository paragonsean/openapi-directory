from typing import List, Dict
from aiohttp import web

from openapi_server.models.audit_candidate_search_list import AuditCandidateSearchList
from openapi_server.models.audit_case_page import AuditCasePage
from openapi_server.models.audit_category_page import AuditCategoryPage
from openapi_server.models.audit_committee_search_list import AuditCommitteeSearchList
from openapi_server.models.audit_primary_category_page import AuditPrimaryCategoryPage
from openapi_server import util


async def audit_case_get(request: web.Request, api_key, max_election_cycle=None, q=None, sub_category_id=None, cycle=None, sort_null_only=None, audit_case_id=None, sort_hide_null=None, candidate_id=None, qq=None, per_page=None, sort=None, min_election_cycle=None, audit_id=None, committee_designation=None, committee_type=None, sort_nulls_last=None, page=None, committee_id=None, primary_category_id=None) -> web.Response:
    """audit_case_get

     This endpoint contains Final Audit Reports approved by the Commission since inception. The search can be based on information about the audited committee (Name, FEC ID Number, Type,  Election Cycle) or the issues covered in the report. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param max_election_cycle:  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    :type max_election_cycle: int
    :param q: The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.
    :type q: List[str]
    :param sub_category_id:  The finding id of an audit. Finding are a category of broader issues. Each category has an unique ID. 
    :type sub_category_id: str
    :param cycle:  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param audit_case_id:  Primary/foreign key for audit tables 
    :type audit_case_id: List[str]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param qq: Name of candidate running for office
    :type qq: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: List[str]
    :param min_election_cycle:  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    :type min_election_cycle: int
    :param audit_id:  The audit issue. Each subcategory has an unique ID 
    :type audit_id: List[int]
    :param committee_designation: Type of committee:         - H or S - Congressional         - P - Presidential         - X or Y or Z - Party         - N or Q - PAC         - I - Independent expenditure         - O - Super PAC  
    :type committee_designation: str
    :param committee_type: The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    :type committee_type: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param primary_category_id:  Audit category ID (table PK) 
    :type primary_category_id: str

    """
    return web.Response(status=200)


async def audit_category_get(request: web.Request, api_key, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, per_page=None, primary_category_id=None, sort=None, primary_category_name=None) -> web.Response:
    """audit_category_get

     This lists the options for the categories and subcategories available in the /audit-search/ endpoint. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
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
    :param primary_category_id:  Audit category ID (table PK) 
    :type primary_category_id: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param primary_category_name: Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed 
    :type primary_category_name: List[str]

    """
    return web.Response(status=200)


async def audit_primary_category_get(request: web.Request, api_key, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, per_page=None, primary_category_id=None, sort=None, primary_category_name=None) -> web.Response:
    """audit_primary_category_get

     This lists the options for the primary categories available in the /audit-search/ endpoint. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
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
    :param primary_category_id:  Audit category ID (table PK) 
    :type primary_category_id: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param primary_category_name: Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed 
    :type primary_category_name: List[str]

    """
    return web.Response(status=200)


async def names_audit_candidates_get(request: web.Request, api_key, q) -> web.Response:
    """names_audit_candidates_get

     Search for candidates or committees by name. If you&#39;re looking for information on a particular person or group, using a name to find the &#x60;candidate_id&#x60; or &#x60;committee_id&#x60; on this endpoint can be a helpful first step. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param q: Name (candidate or committee) to search for
    :type q: List[str]

    """
    return web.Response(status=200)


async def names_audit_committees_get(request: web.Request, api_key, q) -> web.Response:
    """names_audit_committees_get

     Search for candidates or committees by name. If you&#39;re looking for information on a particular person or group, using a name to find the &#x60;candidate_id&#x60; or &#x60;committee_id&#x60; on this endpoint can be a helpful first step. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param q: Name (candidate or committee) to search for
    :type q: List[str]

    """
    return web.Response(status=200)
