from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_fec_pacs(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_fec_pacs_committee=None, search_db_fec_pacs_total_receipts=None, search_db_fec_pacs_beginning_cash=None, search_db_fec_pacs_ending_cash=None, search_db_fec_pacs_contributions_from_individuals=None, search_db_fec_pacs_contributions_from_other_committees=None, search_db_fec_pacs_trans_from_affiliates=None, search_db_fec_pacs_contributions_to_other_committee=None, search_db_fec_pacs_contributions_from_candidate=None, search_db_fec_pacs_loans_from_candidate=None, search_db_fec_pacs_total_loans_received=None, search_db_fec_pacs_total_distributions=None, search_db_fec_pacs_transfers_to_affiliates=None, search_db_fec_pacs_refunds_to_individuals=None, search_db_fec_pacs_refends_to_othercommittees=None, search_db_fec_pacs_candidate_loan_repayments=None, search_db_fec_pacs_loan_repayments=None) -> web.Response:
    """Search API for &#39;FEC PACs&#39; entry type

    API to search for entries of type FEC PACs

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
    :param search_db_fec_pacs_committee: Committee
    :type search_db_fec_pacs_committee: str
    :param search_db_fec_pacs_total_receipts: Total Receipts
    :type search_db_fec_pacs_total_receipts: float
    :param search_db_fec_pacs_beginning_cash: Beginning Cash
    :type search_db_fec_pacs_beginning_cash: float
    :param search_db_fec_pacs_ending_cash: Ending Cash
    :type search_db_fec_pacs_ending_cash: float
    :param search_db_fec_pacs_contributions_from_individuals: Contributions From Individuals
    :type search_db_fec_pacs_contributions_from_individuals: float
    :param search_db_fec_pacs_contributions_from_other_committees: Contributions From Other Committees
    :type search_db_fec_pacs_contributions_from_other_committees: float
    :param search_db_fec_pacs_trans_from_affiliates: Trans From Affiliates
    :type search_db_fec_pacs_trans_from_affiliates: float
    :param search_db_fec_pacs_contributions_to_other_committee: Contributions To Other Committee
    :type search_db_fec_pacs_contributions_to_other_committee: float
    :param search_db_fec_pacs_contributions_from_candidate: Contributions From Candidate
    :type search_db_fec_pacs_contributions_from_candidate: float
    :param search_db_fec_pacs_loans_from_candidate: Loans From Candidate
    :type search_db_fec_pacs_loans_from_candidate: float
    :param search_db_fec_pacs_total_loans_received: Total Loans Received
    :type search_db_fec_pacs_total_loans_received: float
    :param search_db_fec_pacs_total_distributions: Total Distributions
    :type search_db_fec_pacs_total_distributions: float
    :param search_db_fec_pacs_transfers_to_affiliates: Transfers To Affiliates
    :type search_db_fec_pacs_transfers_to_affiliates: float
    :param search_db_fec_pacs_refunds_to_individuals: Refunds To Individuals
    :type search_db_fec_pacs_refunds_to_individuals: float
    :param search_db_fec_pacs_refends_to_othercommittees: Refends To Othercommittees
    :type search_db_fec_pacs_refends_to_othercommittees: float
    :param search_db_fec_pacs_candidate_loan_repayments: Candidate Loan Repayments
    :type search_db_fec_pacs_candidate_loan_repayments: float
    :param search_db_fec_pacs_loan_repayments: Loan Repayments
    :type search_db_fec_pacs_loan_repayments: float

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
