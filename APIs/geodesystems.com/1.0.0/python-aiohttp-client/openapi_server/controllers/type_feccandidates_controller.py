from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_feccandidates(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_feccandidates_name=None, search_db_feccandidates_party=None, search_db_feccandidates_state=None, search_db_feccandidates_district=None, search_db_feccandidates_gender=None, search_db_feccandidates_beginning_cash=None, search_db_feccandidates_ending_cash=None, search_db_feccandidates_total_receipts=None, search_db_feccandidates_total_indivual_contributions=None, search_db_feccandidates_transfers_from_committees=None, search_db_feccandidates_transfers_to_committees=None, search_db_feccandidates_total_disbursements=None, search_db_feccandidates_contributions_from_candidate=None, search_db_feccandidates_loans_from_candidates=None, search_db_feccandidates_other_loans=None, search_db_feccandidates_candidate_loan_repayments=None, search_db_feccandidates_other_loan_repayments=None, search_db_feccandidates_debts_owed_by=None, search_db_feccandidates_contributions_from_other_committees=None, search_db_feccandidates_contributions_from_party_committees=None, search_db_feccandidates_coverage_end_date=None, search_db_feccandidates_individual_refunds=None, search_db_feccandidates_committee_refunds=None) -> web.Response:
    """Search API for &#39;Candidates&#39; entry type

    API to search for entries of type Candidates

    :param text: Search text
    :type text: str
    :param name: Search name
    :type name: str
    :param description: Search description
    :type description: str
    :param fromdate: From date
    :type fromdate: str
    :param todate: To date
    :type todate: str
    :param createdate_from: Archive create date from
    :type createdate_from: str
    :param createdate_to: Archive create date to
    :type createdate_to: str
    :param changedate_from: Archive change date from
    :type changedate_from: str
    :param changedate_to: Archive change date to
    :type changedate_to: str
    :param group: Parent entry
    :type group: str
    :param filesuffix: File suffix
    :type filesuffix: str
    :param maxlatitude: Northern bounds of search
    :type maxlatitude: float
    :param minlongitude: Western bounds of search
    :type minlongitude: float
    :param minlatitude: Southern bounds of search
    :type minlatitude: float
    :param maxlongitude: Eastern bounds of search
    :type maxlongitude: float
    :param max: Max number of results
    :type max: int
    :param skip: Number to skip
    :type skip: int
    :param search_db_feccandidates_name: Name
    :type search_db_feccandidates_name: str
    :param search_db_feccandidates_party: Party
    :type search_db_feccandidates_party: str
    :param search_db_feccandidates_state: State
    :type search_db_feccandidates_state: str
    :param search_db_feccandidates_district: District
    :type search_db_feccandidates_district: str
    :param search_db_feccandidates_gender: Gender
    :type search_db_feccandidates_gender: str
    :param search_db_feccandidates_beginning_cash: Beginning Cash
    :type search_db_feccandidates_beginning_cash: float
    :param search_db_feccandidates_ending_cash: Ending Cash
    :type search_db_feccandidates_ending_cash: float
    :param search_db_feccandidates_total_receipts: Total Receipts
    :type search_db_feccandidates_total_receipts: float
    :param search_db_feccandidates_total_indivual_contributions: Total Indivual Contributions
    :type search_db_feccandidates_total_indivual_contributions: float
    :param search_db_feccandidates_transfers_from_committees: Transfers From Committees
    :type search_db_feccandidates_transfers_from_committees: float
    :param search_db_feccandidates_transfers_to_committees: Transfers To Committees
    :type search_db_feccandidates_transfers_to_committees: float
    :param search_db_feccandidates_total_disbursements: Total Disbursements
    :type search_db_feccandidates_total_disbursements: float
    :param search_db_feccandidates_contributions_from_candidate: Contributions From Candidate
    :type search_db_feccandidates_contributions_from_candidate: float
    :param search_db_feccandidates_loans_from_candidates: Loans From Candidates
    :type search_db_feccandidates_loans_from_candidates: float
    :param search_db_feccandidates_other_loans: Other Loans
    :type search_db_feccandidates_other_loans: float
    :param search_db_feccandidates_candidate_loan_repayments: Candidate Loan Repayments
    :type search_db_feccandidates_candidate_loan_repayments: float
    :param search_db_feccandidates_other_loan_repayments: Other Loan Repayments
    :type search_db_feccandidates_other_loan_repayments: float
    :param search_db_feccandidates_debts_owed_by: Debts Owed By
    :type search_db_feccandidates_debts_owed_by: float
    :param search_db_feccandidates_contributions_from_other_committees: Contributions From Other Committees
    :type search_db_feccandidates_contributions_from_other_committees: float
    :param search_db_feccandidates_contributions_from_party_committees: Contributions From Party Committees
    :type search_db_feccandidates_contributions_from_party_committees: float
    :param search_db_feccandidates_coverage_end_date: Coverage End Date
    :type search_db_feccandidates_coverage_end_date: str
    :param search_db_feccandidates_individual_refunds: Individual Refunds
    :type search_db_feccandidates_individual_refunds: float
    :param search_db_feccandidates_committee_refunds: Committee Refunds
    :type search_db_feccandidates_committee_refunds: float

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
