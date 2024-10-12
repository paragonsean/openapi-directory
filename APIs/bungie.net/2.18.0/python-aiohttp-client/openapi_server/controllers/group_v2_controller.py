from typing import List, Dict
from aiohttp import web

from openapi_server.models.destiny2_equip_item200_response import Destiny2EquipItem200Response
from openapi_server.models.forum_get_topic_for_content200_response import ForumGetTopicForContent200Response
from openapi_server.models.get_available_locales200_response import GetAvailableLocales200Response
from openapi_server.models.group_v2_approve_all_pending200_response import GroupV2ApproveAllPending200Response
from openapi_server.models.group_v2_get_admins_and_founder_of_group200_response import GroupV2GetAdminsAndFounderOfGroup200Response
from openapi_server.models.group_v2_get_available_themes200_response import GroupV2GetAvailableThemes200Response
from openapi_server.models.group_v2_get_banned_members_of_group200_response import GroupV2GetBannedMembersOfGroup200Response
from openapi_server.models.group_v2_get_group_by_name200_response import GroupV2GetGroupByName200Response
from openapi_server.models.group_v2_get_group_optional_conversations200_response import GroupV2GetGroupOptionalConversations200Response
from openapi_server.models.group_v2_get_groups_for_member200_response import GroupV2GetGroupsForMember200Response
from openapi_server.models.group_v2_get_invited_individuals200_response import GroupV2GetInvitedIndividuals200Response
from openapi_server.models.group_v2_get_potential_groups_for_member200_response import GroupV2GetPotentialGroupsForMember200Response
from openapi_server.models.group_v2_get_recommended_groups200_response import GroupV2GetRecommendedGroups200Response
from openapi_server.models.group_v2_get_user_clan_invite_setting200_response import GroupV2GetUserClanInviteSetting200Response
from openapi_server.models.group_v2_group_search200_response import GroupV2GroupSearch200Response
from openapi_server.models.group_v2_individual_group_invite200_response import GroupV2IndividualGroupInvite200Response
from openapi_server.models.group_v2_kick_member200_response import GroupV2KickMember200Response
from openapi_server.models.group_v2_recover_group_for_founder200_response import GroupV2RecoverGroupForFounder200Response
from openapi_server import util


async def group_v2_abdicate_foundership(request: web.Request, founder_id_new, group_id, membership_type) -> web.Response:
    """group_v2_abdicate_foundership

    An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

    :param founder_id_new: The new founder for this group. Must already be a group admin.
    :type founder_id_new: int
    :param group_id: The target group id.
    :type group_id: int
    :param membership_type: Membership type of the provided founderIdNew.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_add_optional_conversation(request: web.Request, group_id) -> web.Response:
    """group_v2_add_optional_conversation

    Add a new optional conversation/chat channel. Requires admin permissions to the group.

    :param group_id: Group ID of the group to edit.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_approve_all_pending(request: web.Request, group_id) -> web.Response:
    """group_v2_approve_all_pending

    Approve all of the pending users for the given group.

    :param group_id: ID of the group.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_approve_pending(request: web.Request, group_id, membership_id, membership_type) -> web.Response:
    """group_v2_approve_pending

    Approve the given membershipId to join the group/clan as long as they have applied.

    :param group_id: ID of the group.
    :type group_id: int
    :param membership_id: The membership id being approved.
    :type membership_id: int
    :param membership_type: Membership type of the supplied membership ID.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_approve_pending_for_list(request: web.Request, group_id) -> web.Response:
    """group_v2_approve_pending_for_list

    Approve all of the pending users for the given group.

    :param group_id: ID of the group.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_ban_member(request: web.Request, group_id, membership_id, membership_type) -> web.Response:
    """group_v2_ban_member

    Bans the requested member from the requested group for the specified period of time.

    :param group_id: Group ID that has the member to ban.
    :type group_id: int
    :param membership_id: Membership ID of the member to ban from the group.
    :type membership_id: int
    :param membership_type: Membership type of the provided membership ID.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_deny_all_pending(request: web.Request, group_id) -> web.Response:
    """group_v2_deny_all_pending

    Deny all of the pending users for the given group.

    :param group_id: ID of the group.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_deny_pending_for_list(request: web.Request, group_id) -> web.Response:
    """group_v2_deny_pending_for_list

    Deny all of the pending users for the given group that match the passed-in .

    :param group_id: ID of the group.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_edit_clan_banner(request: web.Request, group_id) -> web.Response:
    """group_v2_edit_clan_banner

    Edit an existing group&#39;s clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

    :param group_id: Group ID of the group to edit.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_edit_founder_options(request: web.Request, group_id) -> web.Response:
    """group_v2_edit_founder_options

    Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

    :param group_id: Group ID of the group to edit.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_edit_group(request: web.Request, group_id) -> web.Response:
    """group_v2_edit_group

    Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

    :param group_id: Group ID of the group to edit.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_edit_group_membership(request: web.Request, group_id, membership_id, membership_type, member_type) -> web.Response:
    """group_v2_edit_group_membership

    Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

    :param group_id: ID of the group to which the member belongs.
    :type group_id: int
    :param membership_id: Membership ID to modify.
    :type membership_id: int
    :param membership_type: Membership type of the provide membership ID.
    :type membership_type: int
    :param member_type: New membertype for the specified member.
    :type member_type: int

    """
    return web.Response(status=200)


async def group_v2_edit_optional_conversation(request: web.Request, conversation_id, group_id) -> web.Response:
    """group_v2_edit_optional_conversation

    Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

    :param conversation_id: Conversation Id of the channel being edited.
    :type conversation_id: int
    :param group_id: Group ID of the group to edit.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_get_admins_and_founder_of_group(request: web.Request, currentpage, group_id) -> web.Response:
    """group_v2_get_admins_and_founder_of_group

    Get the list of members in a given group who are of admin level or higher.

    :param currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
    :type currentpage: int
    :param group_id: The ID of the group.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_get_available_avatars(request: web.Request, ) -> web.Response:
    """group_v2_get_available_avatars

    Returns a list of all available group avatars for the signed-in user.


    """
    return web.Response(status=200)


async def group_v2_get_available_themes(request: web.Request, ) -> web.Response:
    """group_v2_get_available_themes

    Returns a list of all available group themes.


    """
    return web.Response(status=200)


async def group_v2_get_banned_members_of_group(request: web.Request, currentpage, group_id) -> web.Response:
    """group_v2_get_banned_members_of_group

    Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

    :param currentpage: Page number (starting with 1). Each page has a fixed size of 50 entries.
    :type currentpage: int
    :param group_id: Group ID whose banned members you are fetching
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_get_group(request: web.Request, group_id) -> web.Response:
    """group_v2_get_group

    Get information about a specific group of the given ID.

    :param group_id: Requested group&#39;s id.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_get_group_by_name(request: web.Request, group_name, group_type) -> web.Response:
    """group_v2_get_group_by_name

    Get information about a specific group with the given name and type.

    :param group_name: Exact name of the group to find.
    :type group_name: str
    :param group_type: Type of group to find.
    :type group_type: int

    """
    return web.Response(status=200)


async def group_v2_get_group_by_name_v2(request: web.Request, ) -> web.Response:
    """group_v2_get_group_by_name_v2

    Get information about a specific group with the given name and type. The POST version.


    """
    return web.Response(status=200)


async def group_v2_get_group_optional_conversations(request: web.Request, group_id) -> web.Response:
    """group_v2_get_group_optional_conversations

    Gets a list of available optional conversation channels and their settings.

    :param group_id: Requested group&#39;s id.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_get_groups_for_member(request: web.Request, filter, group_type, membership_id, membership_type) -> web.Response:
    """group_v2_get_groups_for_member

    Get information about the groups that a given member has joined.

    :param filter: Filter apply to list of joined groups.
    :type filter: int
    :param group_type: Type of group the supplied member founded.
    :type group_type: int
    :param membership_id: Membership ID to for which to find founded groups.
    :type membership_id: int
    :param membership_type: Membership type of the supplied membership ID.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_get_invited_individuals(request: web.Request, currentpage, group_id) -> web.Response:
    """group_v2_get_invited_individuals

    Get the list of users who have been invited into the group.

    :param currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
    :type currentpage: int
    :param group_id: ID of the group.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_get_members_of_group(request: web.Request, currentpage, group_id, member_type=None, name_search=None) -> web.Response:
    """group_v2_get_members_of_group

    Get the list of members in a given group.

    :param currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
    :type currentpage: int
    :param group_id: The ID of the group.
    :type group_id: int
    :param member_type: Filter out other member types. Use None for all members.
    :type member_type: int
    :param name_search: The name fragment upon which a search should be executed for members with matching display or unique names.
    :type name_search: str

    """
    return web.Response(status=200)


async def group_v2_get_pending_memberships(request: web.Request, currentpage, group_id) -> web.Response:
    """group_v2_get_pending_memberships

    Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

    :param currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
    :type currentpage: int
    :param group_id: ID of the group.
    :type group_id: int

    """
    return web.Response(status=200)


async def group_v2_get_potential_groups_for_member(request: web.Request, filter, group_type, membership_id, membership_type) -> web.Response:
    """group_v2_get_potential_groups_for_member

    Get information about the groups that a given member has applied to or been invited to.

    :param filter: Filter apply to list of potential joined groups.
    :type filter: int
    :param group_type: Type of group the supplied member applied.
    :type group_type: int
    :param membership_id: Membership ID to for which to find applied groups.
    :type membership_id: int
    :param membership_type: Membership type of the supplied membership ID.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_get_recommended_groups(request: web.Request, create_date_range, group_type) -> web.Response:
    """group_v2_get_recommended_groups

    Gets groups recommended for you based on the groups to whom those you follow belong.

    :param create_date_range: Requested range in which to pull recommended groups
    :type create_date_range: int
    :param group_type: Type of groups requested
    :type group_type: int

    """
    return web.Response(status=200)


async def group_v2_get_user_clan_invite_setting(request: web.Request, m_type) -> web.Response:
    """group_v2_get_user_clan_invite_setting

    Gets the state of the user&#39;s clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

    :param m_type: The Destiny membership type of the account we wish to access settings.
    :type m_type: int

    """
    return web.Response(status=200)


async def group_v2_group_search(request: web.Request, ) -> web.Response:
    """group_v2_group_search

    Search for Groups.


    """
    return web.Response(status=200)


async def group_v2_individual_group_invite(request: web.Request, group_id, membership_id, membership_type) -> web.Response:
    """group_v2_individual_group_invite

    Invite a user to join this group.

    :param group_id: ID of the group you would like to join.
    :type group_id: int
    :param membership_id: Membership id of the account being invited.
    :type membership_id: int
    :param membership_type: MembershipType of the account being invited.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_individual_group_invite_cancel(request: web.Request, group_id, membership_id, membership_type) -> web.Response:
    """group_v2_individual_group_invite_cancel

    Cancels a pending invitation to join a group.

    :param group_id: ID of the group you would like to join.
    :type group_id: int
    :param membership_id: Membership id of the account being cancelled.
    :type membership_id: int
    :param membership_type: MembershipType of the account being cancelled.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_kick_member(request: web.Request, group_id, membership_id, membership_type) -> web.Response:
    """group_v2_kick_member

    Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

    :param group_id: Group ID to kick the user from.
    :type group_id: int
    :param membership_id: Membership ID to kick.
    :type membership_id: int
    :param membership_type: Membership type of the provided membership ID.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_recover_group_for_founder(request: web.Request, group_type, membership_id, membership_type) -> web.Response:
    """group_v2_recover_group_for_founder

    Allows a founder to manually recover a group they can see in game but not on bungie.net

    :param group_type: Type of group the supplied member founded.
    :type group_type: int
    :param membership_id: Membership ID to for which to find founded groups.
    :type membership_id: int
    :param membership_type: Membership type of the supplied membership ID.
    :type membership_type: int

    """
    return web.Response(status=200)


async def group_v2_unban_member(request: web.Request, group_id, membership_id, membership_type) -> web.Response:
    """group_v2_unban_member

    Unbans the requested member, allowing them to re-apply for membership.

    :param group_id: 
    :type group_id: int
    :param membership_id: Membership ID of the member to unban from the group
    :type membership_id: int
    :param membership_type: Membership type of the provided membership ID.
    :type membership_type: int

    """
    return web.Response(status=200)
