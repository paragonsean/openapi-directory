from typing import List, Dict
from aiohttp import web

from openapi_server.models.legal_search_get_default_response import LegalSearchGetDefaultResponse
from openapi_server import util


async def legal_search_get(request: web.Request, api_key, case_statutory_citation=None, af_min_rtb_date=None, af_report_year=None, q=None, from_hit=None, ao_requestor_type=None, case_max_close_date=None, ao_is_pending=None, af_fd_fine_amount=None, case_min_open_date=None, ao_min_issue_date=None, sort=None, ao_citation_require_all=None, case_doc_category_id=None, ao_status=None, af_max_rtb_date=None, af_rtb_fine_amount=None, case_respondents=None, ao_entity_name=None, ao_requestor=None, ao_category=None, ao_regulatory_citation=None, case_regulatory_citation=None, case_citation_require_all=None, case_dispositions=None, ao_name=None, af_max_fd_date=None, ao_max_request_date=None, mur_type=None, hits_returned=None, case_election_cycles=None, case_min_close_date=None, ao_max_issue_date=None, af_committee_id=None, af_min_fd_date=None, case_max_open_date=None, ao_min_request_date=None, ao_no=None, type=None, case_no=None, ao_statutory_citation=None, af_name=None) -> web.Response:
    """legal_search_get

     Search legal documents by document type, or across all document types using keywords, parameter values and ranges. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param case_statutory_citation:  Statutory citations 
    :type case_statutory_citation: List[str]
    :param af_min_rtb_date:  The earliest Reason to Believe date 
    :type af_min_rtb_date: str
    :param af_report_year:  Admin fine report year 
    :type af_report_year: str
    :param q:  Text to search legal documents for 
    :type q: str
    :param from_hit:  Get results starting from this index 
    :type from_hit: int
    :param ao_requestor_type:  Code of the advisory opinion requestor type. 
    :type ao_requestor_type: List[int]
    :param case_max_close_date:  The latest date closed of case 
    :type case_max_close_date: str
    :param ao_is_pending:  AO is pending 
    :type ao_is_pending: bool
    :param af_fd_fine_amount:  Final Determination fine amount 
    :type af_fd_fine_amount: int
    :param case_min_open_date:  The earliest date opened of case 
    :type case_min_open_date: str
    :param ao_min_issue_date:  Earliest issue date of advisory opinion 
    :type ao_min_issue_date: str
    :param sort:  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60; 
    :type sort: str
    :param ao_citation_require_all:  Require all citations to be in document (default behavior is any) 
    :type ao_citation_require_all: bool
    :param case_doc_category_id:  Select one or more case_doc_category_id to filter by corresponding CASE_DOCUMENT_CATEGORY:         - 1 - Conciliation and Settlement Agreements         - 2 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 3 - General Counsel Reports, Briefs, Notifications and Responses         - 4 - Certifications         - 5 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 6 - Statement of Reasons          - 1001 - ADR Settlement Agreements         - 1002 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 1003 - ADR Memoranda, Notifications and Responses         - 1004 - Certifications         - 1005 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 1006 - Statement of Reasons          - 2001 - Administrative Fine Case 
    :type case_doc_category_id: List[str]
    :param ao_status:  Status of AO (pending, withdrawn, or final) 
    :type ao_status: str
    :param af_max_rtb_date:  The latest Reason to Believe date 
    :type af_max_rtb_date: str
    :param af_rtb_fine_amount:  Reason to Believe fine amount 
    :type af_rtb_fine_amount: int
    :param case_respondents:  Cases respondents 
    :type case_respondents: str
    :param ao_entity_name:  Name of commenter or representative 
    :type ao_entity_name: List[str]
    :param ao_requestor:  The requestor of the advisory opinion 
    :type ao_requestor: str
    :param ao_category:  Category of the document 
    :type ao_category: List[str]
    :param ao_regulatory_citation:  Regulatory citations 
    :type ao_regulatory_citation: List[str]
    :param case_regulatory_citation:  Regulatory citations 
    :type case_regulatory_citation: List[str]
    :param case_citation_require_all:  Require all citations to be in document (default behavior is any) 
    :type case_citation_require_all: bool
    :param case_dispositions:  Cases dispositions 
    :type case_dispositions: List[str]
    :param ao_name:  Force advisory opinion name 
    :type ao_name: List[str]
    :param af_max_fd_date:  The latest Final Determination date 
    :type af_max_fd_date: str
    :param ao_max_request_date:  Latest request date of advisory opinion 
    :type ao_max_request_date: str
    :param mur_type:  Type of MUR : current or archived 
    :type mur_type: str
    :param hits_returned:  Number of results to return (max 10) 
    :type hits_returned: int
    :param case_election_cycles:  Cases election cycles 
    :type case_election_cycles: int
    :param case_min_close_date:  The earliest date closed of case 
    :type case_min_close_date: str
    :param ao_max_issue_date:  Latest issue date of advisory opinion 
    :type ao_max_issue_date: str
    :param af_committee_id:  Admin fine committee ID 
    :type af_committee_id: str
    :param af_min_fd_date:  The earliest Final Determination date 
    :type af_min_fd_date: str
    :param case_max_open_date:  The latest date opened of case 
    :type case_max_open_date: str
    :param ao_min_request_date:  Earliest request date of advisory opinion 
    :type ao_min_request_date: str
    :param ao_no:  Force advisory opinion number 
    :type ao_no: List[str]
    :param type:  Choose a legal document type 
    :type type: str
    :param case_no:  Enforcement matter case number 
    :type case_no: List[str]
    :param ao_statutory_citation:  Statutory citations 
    :type ao_statutory_citation: List[str]
    :param af_name:  Admin fine committee name 
    :type af_name: List[str]

    """
    af_min_rtb_date = util.deserialize_date(af_min_rtb_date)
    case_max_close_date = util.deserialize_date(case_max_close_date)
    case_min_open_date = util.deserialize_date(case_min_open_date)
    ao_min_issue_date = util.deserialize_date(ao_min_issue_date)
    af_max_rtb_date = util.deserialize_date(af_max_rtb_date)
    af_max_fd_date = util.deserialize_date(af_max_fd_date)
    ao_max_request_date = util.deserialize_date(ao_max_request_date)
    case_min_close_date = util.deserialize_date(case_min_close_date)
    ao_max_issue_date = util.deserialize_date(ao_max_issue_date)
    af_min_fd_date = util.deserialize_date(af_min_fd_date)
    case_max_open_date = util.deserialize_date(case_max_open_date)
    ao_min_request_date = util.deserialize_date(ao_min_request_date)
    return web.Response(status=200)
