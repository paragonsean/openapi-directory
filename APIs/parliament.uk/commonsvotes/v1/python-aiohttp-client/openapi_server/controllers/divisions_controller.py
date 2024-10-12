from typing import List, Dict
from aiohttp import web

from openapi_server.models.division_grouped_by_party import DivisionGroupedByParty
from openapi_server.models.member_voting_record import MemberVotingRecord
from openapi_server.models.published_division import PublishedDivision
from openapi_server import util


async def divisions_get_division_by_id(request: web.Request, division_id, format) -> web.Response:
    """Return a Division

    Single Division which has the specified Id

    :param division_id: Id number of a Division whose records are to be returned
    :type division_id: int
    :param format: xml or json
    :type format: str

    """
    return web.Response(status=200)


async def divisions_get_divisions_groups_by_party(request: web.Request, format, query_parameters_search_term=None, query_parameters_member_id=None, query_parameters_include_when_member_was_teller=None, query_parameters_start_date=None, query_parameters_end_date=None, query_parameters_division_number=None) -> web.Response:
    """Return Divisions results grouped by party

    Division results which meet the specified criteria grouped by parties

    :param format: xml or json
    :type format: str
    :param query_parameters_search_term: Divisions containing search term within title or number
    :type query_parameters_search_term: str
    :param query_parameters_member_id: Divisions returning Member with Member ID voting records
    :type query_parameters_member_id: int
    :param query_parameters_include_when_member_was_teller: Divisions where member was a teller as well as if they actually voted
    :type query_parameters_include_when_member_was_teller: bool
    :param query_parameters_start_date: Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    :type query_parameters_start_date: str
    :param query_parameters_end_date: Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    :type query_parameters_end_date: str
    :param query_parameters_division_number: Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    :type query_parameters_division_number: int

    """
    query_parameters_start_date = util.deserialize_datetime(query_parameters_start_date)
    query_parameters_end_date = util.deserialize_datetime(query_parameters_end_date)
    return web.Response(status=200)


async def divisions_get_voting_records_for_member(request: web.Request, format, query_parameters_member_id, query_parameters_skip=None, query_parameters_take=None, query_parameters_search_term=None, query_parameters_include_when_member_was_teller=None, query_parameters_start_date=None, query_parameters_end_date=None, query_parameters_division_number=None) -> web.Response:
    """Return voting records for a Member

    List of voting records for a member which meet the specified criteria.

    :param format: xml or json
    :type format: str
    :param query_parameters_member_id: Id number of a Member whose voting records are to be returned
    :type query_parameters_member_id: int
    :param query_parameters_skip: The number of records to skip. Default is 0
    :type query_parameters_skip: int
    :param query_parameters_take: The number of records to return per page. Default is 25
    :type query_parameters_take: int
    :param query_parameters_search_term: Divisions containing search term within title or number
    :type query_parameters_search_term: str
    :param query_parameters_include_when_member_was_teller: Divisions where member was a teller as well as if they actually voted
    :type query_parameters_include_when_member_was_teller: bool
    :param query_parameters_start_date: Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    :type query_parameters_start_date: str
    :param query_parameters_end_date: Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    :type query_parameters_end_date: str
    :param query_parameters_division_number: Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    :type query_parameters_division_number: int

    """
    query_parameters_start_date = util.deserialize_datetime(query_parameters_start_date)
    query_parameters_end_date = util.deserialize_datetime(query_parameters_end_date)
    return web.Response(status=200)


async def divisions_search_divisions(request: web.Request, format, query_parameters_skip=None, query_parameters_take=None, query_parameters_search_term=None, query_parameters_member_id=None, query_parameters_include_when_member_was_teller=None, query_parameters_start_date=None, query_parameters_end_date=None, query_parameters_division_number=None) -> web.Response:
    """Return a list of Divisions

    List of Divisions which meet the specified criteria

    :param format: json or xml
    :type format: str
    :param query_parameters_skip: The number of records to skip. Default is 0
    :type query_parameters_skip: int
    :param query_parameters_take: The number of records to return per page. Default is 25
    :type query_parameters_take: int
    :param query_parameters_search_term: Divisions containing search term within title or number
    :type query_parameters_search_term: str
    :param query_parameters_member_id: Divisions returning Member with Member ID voting records
    :type query_parameters_member_id: int
    :param query_parameters_include_when_member_was_teller: Divisions where member was a teller as well as if they actually voted
    :type query_parameters_include_when_member_was_teller: bool
    :param query_parameters_start_date: Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    :type query_parameters_start_date: str
    :param query_parameters_end_date: Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    :type query_parameters_end_date: str
    :param query_parameters_division_number: Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    :type query_parameters_division_number: int

    """
    query_parameters_start_date = util.deserialize_datetime(query_parameters_start_date)
    query_parameters_end_date = util.deserialize_datetime(query_parameters_end_date)
    return web.Response(status=200)


async def divisions_search_total_results(request: web.Request, format, query_parameters_search_term=None, query_parameters_member_id=None, query_parameters_include_when_member_was_teller=None, query_parameters_start_date=None, query_parameters_end_date=None, query_parameters_division_number=None) -> web.Response:
    """Return total results count

    Total count of Divisions meeting the specified criteria

    :param format: json or xml
    :type format: str
    :param query_parameters_search_term: Divisions containing search term within title or number
    :type query_parameters_search_term: str
    :param query_parameters_member_id: Divisions returning Member with Member ID voting records
    :type query_parameters_member_id: int
    :param query_parameters_include_when_member_was_teller: Divisions where member was a teller as well as if they actually voted
    :type query_parameters_include_when_member_was_teller: bool
    :param query_parameters_start_date: Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    :type query_parameters_start_date: str
    :param query_parameters_end_date: Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    :type query_parameters_end_date: str
    :param query_parameters_division_number: Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    :type query_parameters_division_number: int

    """
    query_parameters_start_date = util.deserialize_datetime(query_parameters_start_date)
    query_parameters_end_date = util.deserialize_datetime(query_parameters_end_date)
    return web.Response(status=200)
