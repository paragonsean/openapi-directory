from typing import List, Dict
from aiohttp import web

from openapi_server.models.boards import Boards
from openapi_server.models.boards_checklists import BoardsChecklists
from openapi_server.models.boards_closed import BoardsClosed
from openapi_server.models.boards_desc import BoardsDesc
from openapi_server.models.boards_id_organization import BoardsIdOrganization
from openapi_server.models.boards_labels import BoardsLabels
from openapi_server.models.boards_lists import BoardsLists
from openapi_server.models.boards_members import BoardsMembers
from openapi_server.models.boards_memberships import BoardsMemberships
from openapi_server.models.boards_name import BoardsName
from openapi_server.models.boards_power_ups import BoardsPowerUps
from openapi_server.models.boards_subscribed import BoardsSubscribed
from openapi_server.models.label_names_blue import LabelNamesBlue
from openapi_server.models.label_names_green import LabelNamesGreen
from openapi_server.models.label_names_orange import LabelNamesOrange
from openapi_server.models.label_names_purple import LabelNamesPurple
from openapi_server.models.label_names_red import LabelNamesRed
from openapi_server.models.label_names_yellow import LabelNamesYellow
from openapi_server.models.my_prefs_email_position import MyPrefsEmailPosition
from openapi_server.models.my_prefs_id_email_list import MyPrefsIdEmailList
from openapi_server.models.my_prefs_show_list_guide import MyPrefsShowListGuide
from openapi_server.models.my_prefs_show_sidebar import MyPrefsShowSidebar
from openapi_server.models.my_prefs_show_sidebar_activity import MyPrefsShowSidebarActivity
from openapi_server.models.my_prefs_show_sidebar_board_actions import MyPrefsShowSidebarBoardActions
from openapi_server.models.my_prefs_show_sidebar_members import MyPrefsShowSidebarMembers
from openapi_server.models.prefs_background import PrefsBackground
from openapi_server.models.prefs_calendar_feed_enabled import PrefsCalendarFeedEnabled
from openapi_server.models.prefs_card_aging import PrefsCardAging
from openapi_server.models.prefs_card_covers import PrefsCardCovers
from openapi_server.models.prefs_comments import PrefsComments
from openapi_server.models.prefs_invitations import PrefsInvitations
from openapi_server.models.prefs_permission_level import PrefsPermissionLevel
from openapi_server.models.prefs_self_join import PrefsSelfJoin
from openapi_server.models.prefs_voting import PrefsVoting
from openapi_server import util


async def add_boards(request: web.Request, key, token, body) -> web.Response:
    """addBoards()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards\&quot; to be added.
    :type body: dict | bytes

    """
    body = Boards.from_dict(body)
    return web.Response(status=200)


async def add_boards_calendar_key_generate_by_id_board(request: web.Request, id_board, key, token) -> web.Response:
    """addBoardsCalendarKeyGenerateByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def add_boards_checklists_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """addBoardsChecklistsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Checklists\&quot; to be added.
    :type body: dict | bytes

    """
    body = BoardsChecklists.from_dict(body)
    return web.Response(status=200)


async def add_boards_email_key_generate_by_id_board(request: web.Request, id_board, key, token) -> web.Response:
    """addBoardsEmailKeyGenerateByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def add_boards_labels_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """addBoardsLabelsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Labels\&quot; to be added.
    :type body: dict | bytes

    """
    body = BoardsLabels.from_dict(body)
    return web.Response(status=200)


async def add_boards_lists_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """addBoardsListsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Lists\&quot; to be added.
    :type body: dict | bytes

    """
    body = BoardsLists.from_dict(body)
    return web.Response(status=200)


async def add_boards_mark_as_viewed_by_id_board(request: web.Request, id_board, key, token) -> web.Response:
    """addBoardsMarkAsViewedByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def add_boards_power_ups_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """addBoardsPowerUpsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Power Ups\&quot; to be added.
    :type body: dict | bytes

    """
    body = BoardsPowerUps.from_dict(body)
    return web.Response(status=200)


async def delete_boards_members_by_id_board_by_id_member(request: web.Request, id_board, id_member, key, token) -> web.Response:
    """deleteBoardsMembersByIdBoardByIdMember()

    

    :param id_board: board_id
    :type id_board: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_boards_power_ups_by_id_board_by_power_up(request: web.Request, id_board, power_up, key, token) -> web.Response:
    """deleteBoardsPowerUpsByIdBoardByPowerUp()

    

    :param id_board: board_id
    :type id_board: str
    :param power_up: powerUp
    :type power_up: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_boards_actions_by_id_board(request: web.Request, id_board, key, token, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, id_models=None, member=None, member_fields=None, member_creator=None, member_creator_fields=None) -> web.Response:
    """getBoardsActionsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
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


async def get_boards_board_stars_by_id_board(request: web.Request, id_board, key, token, filter=None) -> web.Response:
    """getBoardsBoardStarsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: mine or none
    :type filter: str

    """
    return web.Response(status=200)


async def get_boards_by_id_board(request: web.Request, id_board, key, token, actions=None, actions_entities=None, actions_display=None, actions_format=None, actions_since=None, actions_limit=None, action_fields=None, action_member=None, action_member_fields=None, action_member_creator=None, action_member_creator_fields=None, cards=None, card_fields=None, card_attachments=None, card_attachment_fields=None, card_checklists=None, card_stickers=None, board_stars=None, labels=None, label_fields=None, labels_limit=None, lists=None, list_fields=None, memberships=None, memberships_member=None, memberships_member_fields=None, members=None, member_fields=None, members_invited=None, members_invited_fields=None, checklists=None, checklist_fields=None, organization=None, organization_fields=None, organization_memberships=None, my_prefs=None, fields=None) -> web.Response:
    """getBoardsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
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
    :param actions_format: One of: count, list or minimal
    :type actions_format: str
    :param actions_since: A date, null or lastView
    :type actions_since: str
    :param actions_limit: a number from 0 to 1000
    :type actions_limit: str
    :param action_fields: all or a comma-separated list of: data, date, idMemberCreator or type
    :type action_fields: str
    :param action_member:  true or false
    :type action_member: str
    :param action_member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type action_member_fields: str
    :param action_member_creator:  true or false
    :type action_member_creator: str
    :param action_member_creator_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type action_member_creator_fields: str
    :param cards: One of: all, closed, none, open or visible
    :type cards: str
    :param card_fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type card_fields: str
    :param card_attachments: A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments
    :type card_attachments: str
    :param card_attachment_fields: all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    :type card_attachment_fields: str
    :param card_checklists: One of: all or none
    :type card_checklists: str
    :param card_stickers:  true or false
    :type card_stickers: str
    :param board_stars: One of: mine or none
    :type board_stars: str
    :param labels: One of: all or none
    :type labels: str
    :param label_fields: all or a comma-separated list of: color, idBoard, name or uses
    :type label_fields: str
    :param labels_limit: a number from 0 to 1000
    :type labels_limit: str
    :param lists: One of: all, closed, none or open
    :type lists: str
    :param list_fields: all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    :type list_fields: str
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
    :param members_invited: One of: admins, all, none, normal or owners
    :type members_invited: str
    :param members_invited_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type members_invited_fields: str
    :param checklists: One of: all or none
    :type checklists: str
    :param checklist_fields: all or a comma-separated list of: idBoard, idCard, name or pos
    :type checklist_fields: str
    :param organization:  true or false
    :type organization: str
    :param organization_fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type organization_fields: str
    :param organization_memberships: all or a comma-separated list of: active, admin, deactivated, me or normal
    :type organization_memberships: str
    :param my_prefs:  true or false
    :type my_prefs: str
    :param fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_boards_by_id_board_by_field(request: web.Request, id_board, _field, key, token) -> web.Response:
    """getBoardsByIdBoardByField()

    

    :param id_board: board_id
    :type id_board: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_boards_cards_by_id_board(request: web.Request, id_board, key, token, actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, check_item_states=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None) -> web.Response:
    """getBoardsCardsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
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
    :param stickers:  true or false
    :type stickers: str
    :param members:  true or false
    :type members: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str
    :param check_item_states:  true or false
    :type check_item_states: str
    :param checklists: One of: all or none
    :type checklists: str
    :param limit: a number from 1 to 1000
    :type limit: str
    :param since: A date, or null
    :type since: str
    :param before: A date, or null
    :type before: str
    :param filter: One of: all, closed, none, open or visible
    :type filter: str
    :param fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_boards_cards_by_id_board_by_filter(request: web.Request, id_board, filter, key, token) -> web.Response:
    """getBoardsCardsByIdBoardByFilter()

    

    :param id_board: board_id
    :type id_board: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_boards_cards_by_id_board_by_id_card(request: web.Request, id_board, id_card, key, token, attachments=None, attachment_fields=None, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, action_member_creator_fields=None, members=None, member_fields=None, check_item_states=None, check_item_state_fields=None, labels=None, checklists=None, checklist_fields=None, fields=None) -> web.Response:
    """getBoardsCardsByIdBoardByIdCard()

    

    :param id_board: board_id
    :type id_board: str
    :param id_card: idCard
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param attachments: A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments
    :type attachments: str
    :param attachment_fields: all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    :type attachment_fields: str
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
    :param action_member_creator_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type action_member_creator_fields: str
    :param members:  true or false
    :type members: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str
    :param check_item_states:  true or false
    :type check_item_states: str
    :param check_item_state_fields: all or a comma-separated list of: idCheckItem or state
    :type check_item_state_fields: str
    :param labels:  true or false
    :type labels: str
    :param checklists: One of: all or none
    :type checklists: str
    :param checklist_fields: all or a comma-separated list of: idBoard, idCard, name or pos
    :type checklist_fields: str
    :param fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_boards_checklists_by_id_board(request: web.Request, id_board, key, token, cards=None, card_fields=None, check_items=None, check_item_fields=None, filter=None, fields=None) -> web.Response:
    """getBoardsChecklistsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param cards: One of: all, closed, none, open or visible
    :type cards: str
    :param card_fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type card_fields: str
    :param check_items: One of: all or none
    :type check_items: str
    :param check_item_fields: all or a comma-separated list of: name, nameData, pos, state or type
    :type check_item_fields: str
    :param filter: One of: all or none
    :type filter: str
    :param fields: all or a comma-separated list of: idBoard, idCard, name or pos
    :type fields: str

    """
    return web.Response(status=200)


async def get_boards_deltas_by_id_board(request: web.Request, id_board, tags, ix_last_update, key, token) -> web.Response:
    """getBoardsDeltasByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
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


async def get_boards_labels_by_id_board(request: web.Request, id_board, key, token, fields=None, limit=None) -> web.Response:
    """getBoardsLabelsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: color, idBoard, name or uses
    :type fields: str
    :param limit: a number from 0 to 1000
    :type limit: str

    """
    return web.Response(status=200)


async def get_boards_labels_by_id_board_by_id_label(request: web.Request, id_board, id_label, key, token, fields=None) -> web.Response:
    """getBoardsLabelsByIdBoardByIdLabel()

    

    :param id_board: board_id
    :type id_board: str
    :param id_label: idLabel
    :type id_label: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: color, idBoard, name or uses
    :type fields: str

    """
    return web.Response(status=200)


async def get_boards_lists_by_id_board(request: web.Request, id_board, key, token, cards=None, card_fields=None, filter=None, fields=None) -> web.Response:
    """getBoardsListsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param cards: One of: all, closed, none, open or visible
    :type cards: str
    :param card_fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type card_fields: str
    :param filter: One of: all, closed, none or open
    :type filter: str
    :param fields: all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    :type fields: str

    """
    return web.Response(status=200)


async def get_boards_lists_by_id_board_by_filter(request: web.Request, id_board, filter, key, token) -> web.Response:
    """getBoardsListsByIdBoardByFilter()

    

    :param id_board: board_id
    :type id_board: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_boards_members_by_id_board(request: web.Request, id_board, key, token, filter=None, fields=None, activity=None) -> web.Response:
    """getBoardsMembersByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
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


async def get_boards_members_by_id_board_by_filter(request: web.Request, id_board, filter, key, token) -> web.Response:
    """getBoardsMembersByIdBoardByFilter()

    

    :param id_board: board_id
    :type id_board: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_boards_members_cards_by_id_board_by_id_member(request: web.Request, id_board, id_member, key, token, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, check_item_states=None, checklists=None, board=None, board_fields=None, list=None, list_fields=None, filter=None, fields=None) -> web.Response:
    """getBoardsMembersCardsByIdBoardByIdMember()

    

    :param id_board: board_id
    :type id_board: str
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


async def get_boards_members_invited_by_id_board(request: web.Request, id_board, key, token, fields=None) -> web.Response:
    """getBoardsMembersInvitedByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
    :type fields: str

    """
    return web.Response(status=200)


async def get_boards_members_invited_by_id_board_by_field(request: web.Request, id_board, _field, key, token) -> web.Response:
    """getBoardsMembersInvitedByIdBoardByField()

    

    :param id_board: board_id
    :type id_board: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_boards_memberships_by_id_board(request: web.Request, id_board, key, token, filter=None, member=None, member_fields=None) -> web.Response:
    """getBoardsMembershipsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
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


async def get_boards_memberships_by_id_board_by_id_membership(request: web.Request, id_board, id_membership, key, token, member=None, member_fields=None) -> web.Response:
    """getBoardsMembershipsByIdBoardByIdMembership()

    

    :param id_board: board_id
    :type id_board: str
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


async def get_boards_my_prefs_by_id_board(request: web.Request, id_board, key, token) -> web.Response:
    """getBoardsMyPrefsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_boards_organization_by_id_board(request: web.Request, id_board, key, token, fields=None) -> web.Response:
    """getBoardsOrganizationByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type fields: str

    """
    return web.Response(status=200)


async def get_boards_organization_by_id_board_by_field(request: web.Request, id_board, _field, key, token) -> web.Response:
    """getBoardsOrganizationByIdBoardByField()

    

    :param id_board: board_id
    :type id_board: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def update_boards_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Boards.from_dict(body)
    return web.Response(status=200)


async def update_boards_closed_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsClosedByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Closed\&quot; to be updated.
    :type body: dict | bytes

    """
    body = BoardsClosed.from_dict(body)
    return web.Response(status=200)


async def update_boards_desc_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsDescByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Desc\&quot; to be updated.
    :type body: dict | bytes

    """
    body = BoardsDesc.from_dict(body)
    return web.Response(status=200)


async def update_boards_id_organization_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsIdOrganizationByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Id Organization\&quot; to be updated.
    :type body: dict | bytes

    """
    body = BoardsIdOrganization.from_dict(body)
    return web.Response(status=200)


async def update_boards_label_names_blue_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsLabelNamesBlueByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Label Names Blue\&quot; to be updated.
    :type body: dict | bytes

    """
    body = LabelNamesBlue.from_dict(body)
    return web.Response(status=200)


async def update_boards_label_names_green_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsLabelNamesGreenByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Label Names Green\&quot; to be updated.
    :type body: dict | bytes

    """
    body = LabelNamesGreen.from_dict(body)
    return web.Response(status=200)


async def update_boards_label_names_orange_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsLabelNamesOrangeByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Label Names Orange\&quot; to be updated.
    :type body: dict | bytes

    """
    body = LabelNamesOrange.from_dict(body)
    return web.Response(status=200)


async def update_boards_label_names_purple_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsLabelNamesPurpleByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Label Names Purple\&quot; to be updated.
    :type body: dict | bytes

    """
    body = LabelNamesPurple.from_dict(body)
    return web.Response(status=200)


async def update_boards_label_names_red_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsLabelNamesRedByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Label Names Red\&quot; to be updated.
    :type body: dict | bytes

    """
    body = LabelNamesRed.from_dict(body)
    return web.Response(status=200)


async def update_boards_label_names_yellow_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsLabelNamesYellowByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Label Names Yellow\&quot; to be updated.
    :type body: dict | bytes

    """
    body = LabelNamesYellow.from_dict(body)
    return web.Response(status=200)


async def update_boards_members_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsMembersByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Members\&quot; to be updated.
    :type body: dict | bytes

    """
    body = BoardsMembers.from_dict(body)
    return web.Response(status=200)


async def update_boards_members_by_id_board_by_id_member(request: web.Request, id_board, id_member, key, token, body) -> web.Response:
    """updateBoardsMembersByIdBoardByIdMember()

    

    :param id_board: board_id
    :type id_board: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Members\&quot; to be updated.
    :type body: dict | bytes

    """
    body = BoardsMembers.from_dict(body)
    return web.Response(status=200)


async def update_boards_memberships_by_id_board_by_id_membership(request: web.Request, id_board, id_membership, key, token, body) -> web.Response:
    """updateBoardsMembershipsByIdBoardByIdMembership()

    

    :param id_board: board_id
    :type id_board: str
    :param id_membership: idMembership
    :type id_membership: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Memberships\&quot; to be updated.
    :type body: dict | bytes

    """
    body = BoardsMemberships.from_dict(body)
    return web.Response(status=200)


async def update_boards_my_prefs_email_position_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsMyPrefsEmailPositionByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;My Prefs Email Position\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MyPrefsEmailPosition.from_dict(body)
    return web.Response(status=200)


async def update_boards_my_prefs_id_email_list_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsMyPrefsIdEmailListByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;My Prefs Id Email List\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MyPrefsIdEmailList.from_dict(body)
    return web.Response(status=200)


async def update_boards_my_prefs_show_list_guide_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsMyPrefsShowListGuideByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;My Prefs Show List Guide\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MyPrefsShowListGuide.from_dict(body)
    return web.Response(status=200)


async def update_boards_my_prefs_show_sidebar_activity_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsMyPrefsShowSidebarActivityByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;My Prefs Show Sidebar Activity\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MyPrefsShowSidebarActivity.from_dict(body)
    return web.Response(status=200)


async def update_boards_my_prefs_show_sidebar_board_actions_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;My Prefs Show Sidebar Board Actions\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MyPrefsShowSidebarBoardActions.from_dict(body)
    return web.Response(status=200)


async def update_boards_my_prefs_show_sidebar_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsMyPrefsShowSidebarByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;My Prefs Show Sidebar\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MyPrefsShowSidebar.from_dict(body)
    return web.Response(status=200)


async def update_boards_my_prefs_show_sidebar_members_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsMyPrefsShowSidebarMembersByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;My Prefs Show Sidebar Members\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MyPrefsShowSidebarMembers.from_dict(body)
    return web.Response(status=200)


async def update_boards_name_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsNameByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = BoardsName.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_background_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsBackgroundByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Background\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsBackground.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_calendar_feed_enabled_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsCalendarFeedEnabledByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Calendar Feed Enabled\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsCalendarFeedEnabled.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_card_aging_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsCardAgingByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Card Aging\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsCardAging.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_card_covers_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsCardCoversByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Card Covers\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsCardCovers.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_comments_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsCommentsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Comments\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsComments.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_invitations_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsInvitationsByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Invitations\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsInvitations.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_permission_level_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsPermissionLevelByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Permission Level\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsPermissionLevel.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_self_join_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsSelfJoinByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Self Join\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsSelfJoin.from_dict(body)
    return web.Response(status=200)


async def update_boards_prefs_voting_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsPrefsVotingByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Voting\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsVoting.from_dict(body)
    return web.Response(status=200)


async def update_boards_subscribed_by_id_board(request: web.Request, id_board, key, token, body) -> web.Response:
    """updateBoardsSubscribedByIdBoard()

    

    :param id_board: board_id
    :type id_board: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Boards Subscribed\&quot; to be updated.
    :type body: dict | bytes

    """
    body = BoardsSubscribed.from_dict(body)
    return web.Response(status=200)
