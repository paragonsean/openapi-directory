from typing import List, Dict
from aiohttp import web

from openapi_server.models.comparators import Comparators
from openapi_server.models.division_group_by_party_view_model import DivisionGroupByPartyViewModel
from openapi_server.models.division_view_model import DivisionViewModel
from openapi_server.models.member_voting_record_view_model import MemberVotingRecordViewModel
from openapi_server import util


async def data_divisions_division_id_get(request: web.Request, division_id) -> web.Response:
    """Return a Division

    Get a single Division which has the Id specified.

    :param division_id: Division with ID specified
    :type division_id: int

    """
    return web.Response(status=200)


async def data_divisions_groupedbyparty_get(request: web.Request, search_term=None, member_id=None, include_when_member_was_teller=None, start_date=None, end_date=None, division_number=None, total_votes_cast_comparator=None, total_votes_cast_value_to_compare=None, majority_comparator=None, majority_value_to_compare=None) -> web.Response:
    """Return Divisions results grouped by party

    Get a list of Divisions which contain grouped by party

    :param search_term: Divisions containing search term within title or number
    :type search_term: str
    :param member_id: Divisions returning Member with Member ID voting records
    :type member_id: int
    :param include_when_member_was_teller: Divisions where member was a teller as well as if they actually voted
    :type include_when_member_was_teller: bool
    :param start_date: Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    :type start_date: str
    :param end_date: Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    :type end_date: str
    :param division_number: Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    :type division_number: int
    :param total_votes_cast_comparator: comparison operator to use
    :type total_votes_cast_comparator: dict | bytes
    :param total_votes_cast_value_to_compare: value to compare to with the operator provided
    :type total_votes_cast_value_to_compare: int
    :param majority_comparator: comparison operator to use
    :type majority_comparator: dict | bytes
    :param majority_value_to_compare: value to compare to with the operator provided
    :type majority_value_to_compare: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    total_votes_cast_comparator = .from_dict(total_votes_cast_comparator)
    majority_comparator = .from_dict(majority_comparator)
    return web.Response(status=200)


async def data_divisions_membervoting_get(request: web.Request, member_id, search_term=None, include_when_member_was_teller=None, start_date=None, end_date=None, division_number=None, total_votes_cast_comparator=None, total_votes_cast_value_to_compare=None, majority_comparator=None, majority_value_to_compare=None, skip=None, take=None) -> web.Response:
    """Return voting records for a Member

    Get a list of voting records for a Member.

    :param member_id: Id number of a Member whose voting records are to be returned
    :type member_id: int
    :param search_term: Divisions containing search term within title or number
    :type search_term: str
    :param include_when_member_was_teller: Divisions where member was a teller as well as if they actually voted
    :type include_when_member_was_teller: bool
    :param start_date: Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    :type start_date: str
    :param end_date: Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    :type end_date: str
    :param division_number: Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    :type division_number: int
    :param total_votes_cast_comparator: comparison operator to use
    :type total_votes_cast_comparator: dict | bytes
    :param total_votes_cast_value_to_compare: value to compare to with the operator provided
    :type total_votes_cast_value_to_compare: int
    :param majority_comparator: comparison operator to use
    :type majority_comparator: dict | bytes
    :param majority_value_to_compare: value to compare to with the operator provided
    :type majority_value_to_compare: int
    :param skip: The number of records to skip. Must be a positive integer. Default is 0
    :type skip: int
    :param take: The number of records to return per page. Must be more than 0. Default is 25
    :type take: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    total_votes_cast_comparator = .from_dict(total_votes_cast_comparator)
    majority_comparator = .from_dict(majority_comparator)
    return web.Response(status=200)


async def data_divisions_search_get(request: web.Request, search_term=None, member_id=None, include_when_member_was_teller=None, start_date=None, end_date=None, division_number=None, total_votes_cast_comparator=None, total_votes_cast_value_to_compare=None, majority_comparator=None, majority_value_to_compare=None, skip=None, take=None) -> web.Response:
    """Return a list of Divisions

    Get a list of Divisions which meet the specified criteria.

    :param search_term: Divisions containing search term within title or number
    :type search_term: str
    :param member_id: Divisions returning Member with Member ID voting records
    :type member_id: int
    :param include_when_member_was_teller: Divisions where member was a teller as well as if they actually voted
    :type include_when_member_was_teller: bool
    :param start_date: Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    :type start_date: str
    :param end_date: Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    :type end_date: str
    :param division_number: Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    :type division_number: int
    :param total_votes_cast_comparator: comparison operator to use
    :type total_votes_cast_comparator: dict | bytes
    :param total_votes_cast_value_to_compare: value to compare to with the operator provided
    :type total_votes_cast_value_to_compare: int
    :param majority_comparator: comparison operator to use
    :type majority_comparator: dict | bytes
    :param majority_value_to_compare: value to compare to with the operator provided
    :type majority_value_to_compare: int
    :param skip: The number of records to skip. Must be a positive integer. Default is 0
    :type skip: int
    :param take: The number of records to return per page. Must be more than 0. Default is 25
    :type take: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    total_votes_cast_comparator = .from_dict(total_votes_cast_comparator)
    majority_comparator = .from_dict(majority_comparator)
    return web.Response(status=200)


async def data_divisions_search_total_results_get(request: web.Request, search_term=None, member_id=None, include_when_member_was_teller=None, start_date=None, end_date=None, division_number=None, total_votes_cast_comparator=None, total_votes_cast_value_to_compare=None, majority_comparator=None, majority_value_to_compare=None) -> web.Response:
    """Return total results count

    Get total count of Divisions meeting the specified query, useful for paging lists etc...

    :param search_term: Divisions containing search term within title or number
    :type search_term: str
    :param member_id: Divisions returning Member with Member ID voting records
    :type member_id: int
    :param include_when_member_was_teller: Divisions where member was a teller as well as if they actually voted
    :type include_when_member_was_teller: bool
    :param start_date: Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    :type start_date: str
    :param end_date: Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    :type end_date: str
    :param division_number: Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    :type division_number: int
    :param total_votes_cast_comparator: comparison operator to use
    :type total_votes_cast_comparator: dict | bytes
    :param total_votes_cast_value_to_compare: value to compare to with the operator provided
    :type total_votes_cast_value_to_compare: int
    :param majority_comparator: comparison operator to use
    :type majority_comparator: dict | bytes
    :param majority_value_to_compare: value to compare to with the operator provided
    :type majority_value_to_compare: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    total_votes_cast_comparator = .from_dict(total_votes_cast_comparator)
    majority_comparator = .from_dict(majority_comparator)
    return web.Response(status=200)
