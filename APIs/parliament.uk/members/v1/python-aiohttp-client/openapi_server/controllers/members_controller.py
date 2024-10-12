from typing import List, Dict
from aiohttp import web

from openapi_server.models.biography_experience_list_item import BiographyExperienceListItem
from openapi_server.models.contact_information_list_item import ContactInformationListItem
from openapi_server.models.debate_contribution_members_service_search_result import DebateContributionMembersServiceSearchResult
from openapi_server.models.early_day_motion_members_service_search_result import EarlyDayMotionMembersServiceSearchResult
from openapi_server.models.election_result_item import ElectionResultItem
from openapi_server.models.house import House
from openapi_server.models.member_biography_item import MemberBiographyItem
from openapi_server.models.member_focus_list_item import MemberFocusListItem
from openapi_server.models.member_history_item import MemberHistoryItem
from openapi_server.models.member_item import MemberItem
from openapi_server.models.member_members_service_search_result import MemberMembersServiceSearchResult
from openapi_server.models.portrait_crop_enum import PortraitCropEnum
from openapi_server.models.registered_interest_category_list_item import RegisteredInterestCategoryListItem
from openapi_server.models.staff_list_item import StaffListItem
from openapi_server.models.string_item import StringItem
from openapi_server.models.vote_members_service_search_result import VoteMembersServiceSearchResult
from openapi_server.models.written_question_members_service_search_result import WrittenQuestionMembersServiceSearchResult
from openapi_server import util


async def api_members_history_get(request: web.Request, ids=None) -> web.Response:
    """Return members by ID with list of their historical names, parties and memberships

    

    :param ids: List of MemberIds to find
    :type ids: List[int]

    """
    return web.Response(status=200)


async def api_members_id_biography_get(request: web.Request, id) -> web.Response:
    """Return biography of member by ID

    

    :param id: Biography of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_contact_get(request: web.Request, id) -> web.Response:
    """Return list of contact details of member by ID

    

    :param id: Contact details of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_contribution_summary_get(request: web.Request, id, page=None) -> web.Response:
    """Return contribution summary of member by ID

    

    :param id: Contribution summary of Member by ID specified
    :type id: int
    :param page: 
    :type page: int

    """
    return web.Response(status=200)


async def api_members_id_edms_get(request: web.Request, id, page=None) -> web.Response:
    """Return list of early day motions of member by ID

    

    :param id: Early day motions of Member by ID specified
    :type id: int
    :param page: 
    :type page: int

    """
    return web.Response(status=200)


async def api_members_id_experience_get(request: web.Request, id) -> web.Response:
    """Return experience of member by ID

    

    :param id: Experience of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_focus_get(request: web.Request, id) -> web.Response:
    """Return list of areas of focus of member by ID

    

    :param id: Areas of focus of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_get(request: web.Request, id, details_for_date=None) -> web.Response:
    """Return member by ID

    

    :param id: Member by ID specified
    :type id: int
    :param details_for_date: Member object will be populated with details from the date specified
    :type details_for_date: str

    """
    details_for_date = util.deserialize_datetime(details_for_date)
    return web.Response(status=200)


async def api_members_id_latest_election_result_get(request: web.Request, id) -> web.Response:
    """Return latest election result of member by ID

    

    :param id: Latest election result of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_portrait_get(request: web.Request, id, crop_type=None, web_version=None) -> web.Response:
    """Return portrait of member by ID

    

    :param id: Portrait of Member by ID specified
    :type id: int
    :param crop_type: 
    :type crop_type: dict | bytes
    :param web_version: 
    :type web_version: bool

    """
    crop_type = .from_dict(crop_type)
    return web.Response(status=200)


async def api_members_id_portrait_url_get(request: web.Request, id) -> web.Response:
    """Return portrait url of member by ID

    

    :param id: Portrait url of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_registered_interests_get(request: web.Request, id, house=None) -> web.Response:
    """Return list of registered interests of member by ID

    

    :param id: Registered interests of Member by ID specified
    :type id: int
    :param house: Registered interests of Member by House specified
    :type house: dict | bytes

    """
    house = .from_dict(house)
    return web.Response(status=200)


async def api_members_id_staff_get(request: web.Request, id) -> web.Response:
    """Return list of staff of member by ID

    

    :param id: Staff of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_synopsis_get(request: web.Request, id) -> web.Response:
    """Return synopsis of member by ID

    

    :param id: Synopsis of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_thumbnail_get(request: web.Request, id) -> web.Response:
    """Return thumbnail of member by ID

    

    :param id: Thumbnail of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_thumbnail_url_get(request: web.Request, id) -> web.Response:
    """Return thumbnail url of member by ID

    

    :param id: Thumbnail url of Member by ID specified
    :type id: int

    """
    return web.Response(status=200)


async def api_members_id_voting_get(request: web.Request, id, house, page=None) -> web.Response:
    """Return list of votes by member by ID

    

    :param id: Votes by Member by ID specified
    :type id: int
    :param house: 
    :type house: dict | bytes
    :param page: 
    :type page: int

    """
    house = .from_dict(house)
    return web.Response(status=200)


async def api_members_id_written_questions_get(request: web.Request, id, page=None) -> web.Response:
    """Return list of written questions by member by ID

    

    :param id: Written questions by Member by ID specified
    :type id: int
    :param page: 
    :type page: int

    """
    return web.Response(status=200)


async def api_members_search_get(request: web.Request, name=None, location=None, post_title=None, party_id=None, house=None, constituency_id=None, name_starts_with=None, gender=None, membership_started_since=None, membership_ended_membership_ended_since=None, membership_ended_membership_end_reason_ids=None, membership_in_date_range_was_member_on_or_after=None, membership_in_date_range_was_member_on_or_before=None, membership_in_date_range_was_member_of_house=None, is_eligible=None, is_current_member=None, policy_interest_id=None, experience=None, skip=None, take=None) -> web.Response:
    """Returns a list of current members of the Commons or Lords

    

    :param name: Members where name contains term specified
    :type name: str
    :param location: Members where postcode or geographical location matches the term specified
    :type location: str
    :param post_title: Members which have held the post specified
    :type post_title: str
    :param party_id: Members which are currently affiliated with party with party ID
    :type party_id: int
    :param house: Members where their most recent house is the house specified
    :type house: dict | bytes
    :param constituency_id: Members which currently hold the constituency with constituency id
    :type constituency_id: int
    :param name_starts_with: Members with surname begining with letter(s) specified
    :type name_starts_with: str
    :param gender: Members with the gender specified
    :type gender: str
    :param membership_started_since: Members who started on or after the date given
    :type membership_started_since: str
    :param membership_ended_membership_ended_since: Members who left the House on or after the date given
    :type membership_ended_membership_ended_since: str
    :param membership_ended_membership_end_reason_ids: 
    :type membership_ended_membership_end_reason_ids: List[int]
    :param membership_in_date_range_was_member_on_or_after: Members who were active on or after the date specified
    :type membership_in_date_range_was_member_on_or_after: str
    :param membership_in_date_range_was_member_on_or_before: Members who were active on or before the date specified
    :type membership_in_date_range_was_member_on_or_before: str
    :param membership_in_date_range_was_member_of_house: Members who were active in the house specifid
    :type membership_in_date_range_was_member_of_house: dict | bytes
    :param is_eligible: Members currently Eligible to sit in their House
    :type is_eligible: bool
    :param is_current_member: Members who are current or former members
    :type is_current_member: bool
    :param policy_interest_id: Members with specified policy interest
    :type policy_interest_id: int
    :param experience: Members with specified experience
    :type experience: str
    :param skip: The number of records to skip from the first, default is 0
    :type skip: int
    :param take: The number of records to return, default is 20. Maximum is 20
    :type take: int

    """
    house = .from_dict(house)
    membership_started_since = util.deserialize_datetime(membership_started_since)
    membership_ended_membership_ended_since = util.deserialize_datetime(membership_ended_membership_ended_since)
    membership_in_date_range_was_member_on_or_after = util.deserialize_datetime(membership_in_date_range_was_member_on_or_after)
    membership_in_date_range_was_member_on_or_before = util.deserialize_datetime(membership_in_date_range_was_member_on_or_before)
    membership_in_date_range_was_member_of_house = .from_dict(membership_in_date_range_was_member_of_house)
    return web.Response(status=200)


async def api_members_search_historical_get(request: web.Request, name=None, date_to_search_for=None, skip=None, take=None) -> web.Response:
    """Returns a list of members of the Commons or Lords

    

    :param name: Members with names containing the term specified
    :type name: str
    :param date_to_search_for: Members that were an active member of the Commons or Lords on the date specified
    :type date_to_search_for: str
    :param skip: The number of records to skip from the first, default is 0
    :type skip: int
    :param take: The number of records to return, default is 20. Maximum is 20
    :type take: int

    """
    date_to_search_for = util.deserialize_datetime(date_to_search_for)
    return web.Response(status=200)
