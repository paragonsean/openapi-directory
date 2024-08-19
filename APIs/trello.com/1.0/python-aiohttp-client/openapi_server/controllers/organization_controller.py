from typing import List, Dict
from aiohttp import web

from openapi_server.models.organizations import Organizations
from openapi_server.models.organizations_desc import OrganizationsDesc
from openapi_server.models.organizations_display_name import OrganizationsDisplayName
from openapi_server.models.organizations_logo import OrganizationsLogo
from openapi_server.models.organizations_members import OrganizationsMembers
from openapi_server.models.organizations_members_deactivated import OrganizationsMembersDeactivated
from openapi_server.models.organizations_memberships import OrganizationsMemberships
from openapi_server.models.organizations_name import OrganizationsName
from openapi_server.models.organizations_website import OrganizationsWebsite
from openapi_server.models.prefs_associated_domain import PrefsAssociatedDomain
from openapi_server.models.prefs_board_visibility_restrict import PrefsBoardVisibilityRestrict
from openapi_server.models.prefs_external_members_disabled import PrefsExternalMembersDisabled
from openapi_server.models.prefs_google_apps_version import PrefsGoogleAppsVersion
from openapi_server.models.prefs_org_invite_restrict import PrefsOrgInviteRestrict
from openapi_server.models.prefs_permission_level import PrefsPermissionLevel
from openapi_server import util


async def add_organizations(request: web.Request, key, token, body) -> web.Response:
    """addOrganizations()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations\&quot; to be added.
    :type body: dict | bytes

    """
    body = Organizations.from_dict(body)
    return web.Response(status=200)


async def add_organizations_logo_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """addOrganizationsLogoByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Logo\&quot; to be added.
    :type body: dict | bytes

    """
    body = OrganizationsLogo.from_dict(body)
    return web.Response(status=200)


async def delete_organizations_by_id_org(request: web.Request, id_org, key, token) -> web.Response:
    """deleteOrganizationsByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_organizations_logo_by_id_org(request: web.Request, id_org, key, token) -> web.Response:
    """deleteOrganizationsLogoByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_organizations_members_all_by_id_org_by_id_member(request: web.Request, id_org, id_member, key, token) -> web.Response:
    """deleteOrganizationsMembersAllByIdOrgByIdMember()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_organizations_members_by_id_org_by_id_member(request: web.Request, id_org, id_member, key, token) -> web.Response:
    """deleteOrganizationsMembersByIdOrgByIdMember()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_organizations_prefs_associated_domain_by_id_org(request: web.Request, id_org, key, token) -> web.Response:
    """deleteOrganizationsPrefsAssociatedDomainByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_organizations_prefs_org_invite_restrict_by_id_org(request: web.Request, id_org, value, key, token) -> web.Response:
    """deleteOrganizationsPrefsOrgInviteRestrictByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param value: An email address with optional expansion tokens
    :type value: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_organizations_actions_by_id_org(request: web.Request, id_org, key, token, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, id_models=None, member=None, member_fields=None, member_creator=None, member_creator_fields=None) -> web.Response:
    """getOrganizationsActionsByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param entities:  true or false
    :type entities: str
    :param display:  true or false
    :type display: str
    :param filter: all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    :type filter: str
    :param fields: all or a comma-separated list of: data, date, idMemberCreator or type
    :type fields: str
    :param limit: a number from 0 to 1000
    :type limit: str
    :param format: One of: count, list or minimal
    :type format: str
    :param since: A date, null or lastView
    :type since: str
    :param before: A date, or null
    :type before: str
    :param page: Page * limit must be less than 1000
    :type page: str
    :param id_models: Only return actions related to these model ids
    :type id_models: str
    :param member:  true or false
    :type member: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str
    :param member_creator:  true or false
    :type member_creator: str
    :param member_creator_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_creator_fields: str

    """
    return web.Response(status=200)


async def get_organizations_boards_by_id_org(request: web.Request, id_org, key, token, filter=None, fields=None, actions=None, actions_entities=None, actions_limit=None, actions_format=None, actions_since=None, action_fields=None, memberships=None, organization=None, organization_fields=None, lists=None) -> web.Response:
    """getOrganizationsBoardsByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned
    :type filter: str
    :param fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type fields: str
    :param actions: all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    :type actions: str
    :param actions_entities:  true or false
    :type actions_entities: str
    :param actions_limit: a number from 0 to 1000
    :type actions_limit: str
    :param actions_format: One of: count, list or minimal
    :type actions_format: str
    :param actions_since: A date, null or lastView
    :type actions_since: str
    :param action_fields: all or a comma-separated list of: data, date, idMemberCreator or type
    :type action_fields: str
    :param memberships: all or a comma-separated list of: active, admin, deactivated, me or normal
    :type memberships: str
    :param organization:  true or false
    :type organization: str
    :param organization_fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type organization_fields: str
    :param lists: One of: all, closed, none or open
    :type lists: str

    """
    return web.Response(status=200)


async def get_organizations_boards_by_id_org_by_filter(request: web.Request, id_org, filter, key, token) -> web.Response:
    """getOrganizationsBoardsByIdOrgByFilter()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_organizations_by_id_org(request: web.Request, id_org, key, token, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, memberships=None, memberships_member=None, memberships_member_fields=None, members=None, member_fields=None, member_activity=None, members_invited=None, members_invited_fields=None, boards=None, board_fields=None, board_actions=None, board_actions_entities=None, board_actions_display=None, board_actions_format=None, board_actions_since=None, board_actions_limit=None, board_action_fields=None, board_lists=None, paid_account=None, fields=None) -> web.Response:
    """getOrganizationsByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param actions: all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    :type actions: str
    :param actions_entities:  true or false
    :type actions_entities: str
    :param actions_display:  true or false
    :type actions_display: str
    :param actions_limit: a number from 0 to 1000
    :type actions_limit: str
    :param action_fields: all or a comma-separated list of: data, date, idMemberCreator or type
    :type action_fields: str
    :param memberships: all or a comma-separated list of: active, admin, deactivated, me or normal
    :type memberships: str
    :param memberships_member:  true or false
    :type memberships_member: str
    :param memberships_member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type memberships_member_fields: str
    :param members: One of: admins, all, none, normal or owners
    :type members: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str
    :param member_activity: true or false ; works for premium organizations only.
    :type member_activity: str
    :param members_invited: One of: admins, all, none, normal or owners
    :type members_invited: str
    :param members_invited_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type members_invited_fields: str
    :param boards: all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned
    :type boards: str
    :param board_fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type board_fields: str
    :param board_actions: all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    :type board_actions: str
    :param board_actions_entities:  true or false
    :type board_actions_entities: str
    :param board_actions_display:  true or false
    :type board_actions_display: str
    :param board_actions_format: One of: count, list or minimal
    :type board_actions_format: str
    :param board_actions_since: A date, null or lastView
    :type board_actions_since: str
    :param board_actions_limit: a number from 0 to 1000
    :type board_actions_limit: str
    :param board_action_fields: all or a comma-separated list of: data, date, idMemberCreator or type
    :type board_action_fields: str
    :param board_lists: One of: all, closed, none or open
    :type board_lists: str
    :param paid_account:  true or false
    :type paid_account: str
    :param fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type fields: str

    """
    return web.Response(status=200)


async def get_organizations_by_id_org_by_field(request: web.Request, id_org, _field, key, token) -> web.Response:
    """getOrganizationsByIdOrgByField()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_organizations_deltas_by_id_org(request: web.Request, id_org, tags, ix_last_update, key, token) -> web.Response:
    """getOrganizationsDeltasByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param tags: A valid tag for subscribing
    :type tags: str
    :param ix_last_update: a number from -1 to Infinity
    :type ix_last_update: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_organizations_members_by_id_org(request: web.Request, id_org, key, token, filter=None, fields=None, activity=None) -> web.Response:
    """getOrganizationsMembersByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: admins, all, none, normal or owners
    :type filter: str
    :param fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type fields: str
    :param activity: true or false ; works for premium organizations only.
    :type activity: str

    """
    return web.Response(status=200)


async def get_organizations_members_by_id_org_by_filter(request: web.Request, id_org, filter, key, token) -> web.Response:
    """getOrganizationsMembersByIdOrgByFilter()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_organizations_members_cards_by_id_org_by_id_member(request: web.Request, id_org, id_member, key, token, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, check_item_states=None, checklists=None, board=None, board_fields=None, list=None, list_fields=None, filter=None, fields=None) -> web.Response:
    """getOrganizationsMembersCardsByIdOrgByIdMember()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param actions: all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    :type actions: str
    :param attachments: A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments
    :type attachments: str
    :param attachment_fields: all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    :type attachment_fields: str
    :param members:  true or false
    :type members: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str
    :param check_item_states:  true or false
    :type check_item_states: str
    :param checklists: One of: all or none
    :type checklists: str
    :param board:  true or false
    :type board: str
    :param board_fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type board_fields: str
    :param list:  true or false
    :type list: str
    :param list_fields: all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    :type list_fields: str
    :param filter: One of: all, closed, none, open or visible
    :type filter: str
    :param fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_organizations_members_invited_by_id_org(request: web.Request, id_org, key, token, fields=None) -> web.Response:
    """getOrganizationsMembersInvitedByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
    :type fields: str

    """
    return web.Response(status=200)


async def get_organizations_members_invited_by_id_org_by_field(request: web.Request, id_org, _field, key, token) -> web.Response:
    """getOrganizationsMembersInvitedByIdOrgByField()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_organizations_memberships_by_id_org(request: web.Request, id_org, key, token, filter=None, member=None, member_fields=None) -> web.Response:
    """getOrganizationsMembershipsByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: all or a comma-separated list of: active, admin, deactivated, me or normal
    :type filter: str
    :param member:  true or false
    :type member: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str

    """
    return web.Response(status=200)


async def get_organizations_memberships_by_id_org_by_id_membership(request: web.Request, id_org, id_membership, key, token, member=None, member_fields=None) -> web.Response:
    """getOrganizationsMembershipsByIdOrgByIdMembership()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param id_membership: idMembership
    :type id_membership: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param member:  true or false
    :type member: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str

    """
    return web.Response(status=200)


async def update_organizations_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Organizations.from_dict(body)
    return web.Response(status=200)


async def update_organizations_desc_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsDescByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Desc\&quot; to be updated.
    :type body: dict | bytes

    """
    body = OrganizationsDesc.from_dict(body)
    return web.Response(status=200)


async def update_organizations_display_name_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsDisplayNameByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Display Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = OrganizationsDisplayName.from_dict(body)
    return web.Response(status=200)


async def update_organizations_members_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsMembersByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Members\&quot; to be updated.
    :type body: dict | bytes

    """
    body = OrganizationsMembers.from_dict(body)
    return web.Response(status=200)


async def update_organizations_members_by_id_org_by_id_member(request: web.Request, id_org, id_member, key, token, body) -> web.Response:
    """updateOrganizationsMembersByIdOrgByIdMember()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Members\&quot; to be updated.
    :type body: dict | bytes

    """
    body = OrganizationsMembers.from_dict(body)
    return web.Response(status=200)


async def update_organizations_members_deactivated_by_id_org_by_id_member(request: web.Request, id_org, id_member, key, token, body) -> web.Response:
    """updateOrganizationsMembersDeactivatedByIdOrgByIdMember()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Members Deactivated\&quot; to be updated.
    :type body: dict | bytes

    """
    body = OrganizationsMembersDeactivated.from_dict(body)
    return web.Response(status=200)


async def update_organizations_memberships_by_id_org_by_id_membership(request: web.Request, id_org, id_membership, key, token, body) -> web.Response:
    """updateOrganizationsMembershipsByIdOrgByIdMembership()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param id_membership: idMembership
    :type id_membership: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Memberships\&quot; to be updated.
    :type body: dict | bytes

    """
    body = OrganizationsMemberships.from_dict(body)
    return web.Response(status=200)


async def update_organizations_name_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsNameByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = OrganizationsName.from_dict(body)
    return web.Response(status=200)


async def update_organizations_prefs_associated_domain_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsPrefsAssociatedDomainByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Associated Domain\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsAssociatedDomain.from_dict(body)
    return web.Response(status=200)


async def update_organizations_prefs_board_visibility_restrict_org_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Board Visibility Restrict\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsBoardVisibilityRestrict.from_dict(body)
    return web.Response(status=200)


async def update_organizations_prefs_board_visibility_restrict_private_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Board Visibility Restrict\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsBoardVisibilityRestrict.from_dict(body)
    return web.Response(status=200)


async def update_organizations_prefs_board_visibility_restrict_public_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Board Visibility Restrict\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsBoardVisibilityRestrict.from_dict(body)
    return web.Response(status=200)


async def update_organizations_prefs_external_members_disabled_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsPrefsExternalMembersDisabledByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs External Members Disabled\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsExternalMembersDisabled.from_dict(body)
    return web.Response(status=200)


async def update_organizations_prefs_google_apps_version_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsPrefsGoogleAppsVersionByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Google Apps Version\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsGoogleAppsVersion.from_dict(body)
    return web.Response(status=200)


async def update_organizations_prefs_org_invite_restrict_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsPrefsOrgInviteRestrictByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Org Invite Restrict\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsOrgInviteRestrict.from_dict(body)
    return web.Response(status=200)


async def update_organizations_prefs_permission_level_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsPrefsPermissionLevelByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Permission Level\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsPermissionLevel.from_dict(body)
    return web.Response(status=200)


async def update_organizations_website_by_id_org(request: web.Request, id_org, key, token, body) -> web.Response:
    """updateOrganizationsWebsiteByIdOrg()

    

    :param id_org: idOrg or name
    :type id_org: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Organizations Website\&quot; to be updated.
    :type body: dict | bytes

    """
    body = OrganizationsWebsite.from_dict(body)
    return web.Response(status=200)
