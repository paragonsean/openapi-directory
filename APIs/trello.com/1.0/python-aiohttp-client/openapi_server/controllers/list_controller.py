from typing import List, Dict
from aiohttp import web

from openapi_server.models.lists import Lists
from openapi_server.models.lists_cards import ListsCards
from openapi_server.models.lists_closed import ListsClosed
from openapi_server.models.lists_id_board import ListsIdBoard
from openapi_server.models.lists_move_all_cards import ListsMoveAllCards
from openapi_server.models.lists_name import ListsName
from openapi_server.models.lists_pos import ListsPos
from openapi_server.models.lists_subscribed import ListsSubscribed
from openapi_server import util


async def add_lists(request: web.Request, key, token, body) -> web.Response:
    """addLists()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists\&quot; to be added.
    :type body: dict | bytes

    """
    body = Lists.from_dict(body)
    return web.Response(status=200)


async def add_lists_archive_all_cards_by_id_list(request: web.Request, id_list, key, token) -> web.Response:
    """addListsArchiveAllCardsByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def add_lists_cards_by_id_list(request: web.Request, id_list, key, token, body) -> web.Response:
    """addListsCardsByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists Cards\&quot; to be added.
    :type body: dict | bytes

    """
    body = ListsCards.from_dict(body)
    return web.Response(status=200)


async def add_lists_move_all_cards_by_id_list(request: web.Request, id_list, key, token, body) -> web.Response:
    """addListsMoveAllCardsByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists Move All Cards\&quot; to be added.
    :type body: dict | bytes

    """
    body = ListsMoveAllCards.from_dict(body)
    return web.Response(status=200)


async def get_lists_actions_by_id_list(request: web.Request, id_list, key, token, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, id_models=None, member=None, member_fields=None, member_creator=None, member_creator_fields=None) -> web.Response:
    """getListsActionsByIdList()

    

    :param id_list: idList
    :type id_list: str
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


async def get_lists_board_by_id_list(request: web.Request, id_list, key, token, fields=None) -> web.Response:
    """getListsBoardByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_lists_board_by_id_list_by_field(request: web.Request, id_list, _field, key, token) -> web.Response:
    """getListsBoardByIdListByField()

    

    :param id_list: idList
    :type id_list: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_lists_by_id_list(request: web.Request, id_list, key, token, cards=None, card_fields=None, board=None, board_fields=None, fields=None) -> web.Response:
    """getListsByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param cards: One of: all, closed, none or open
    :type cards: str
    :param card_fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type card_fields: str
    :param board:  true or false
    :type board: str
    :param board_fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type board_fields: str
    :param fields: all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    :type fields: str

    """
    return web.Response(status=200)


async def get_lists_by_id_list_by_field(request: web.Request, id_list, _field, key, token) -> web.Response:
    """getListsByIdListByField()

    

    :param id_list: idList
    :type id_list: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_lists_cards_by_id_list(request: web.Request, id_list, key, token, actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, check_item_states=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None) -> web.Response:
    """getListsCardsByIdList()

    

    :param id_list: idList
    :type id_list: str
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
    :param filter: One of: all, closed, none or open
    :type filter: str
    :param fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_lists_cards_by_id_list_by_filter(request: web.Request, id_list, filter, key, token) -> web.Response:
    """getListsCardsByIdListByFilter()

    

    :param id_list: idList
    :type id_list: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def update_lists_by_id_list(request: web.Request, id_list, key, token, body) -> web.Response:
    """updateListsByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Lists.from_dict(body)
    return web.Response(status=200)


async def update_lists_closed_by_id_list(request: web.Request, id_list, key, token, body) -> web.Response:
    """updateListsClosedByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists Closed\&quot; to be updated.
    :type body: dict | bytes

    """
    body = ListsClosed.from_dict(body)
    return web.Response(status=200)


async def update_lists_id_board_by_id_list(request: web.Request, id_list, key, token, body) -> web.Response:
    """updateListsIdBoardByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists Id Board\&quot; to be updated.
    :type body: dict | bytes

    """
    body = ListsIdBoard.from_dict(body)
    return web.Response(status=200)


async def update_lists_name_by_id_list(request: web.Request, id_list, key, token, body) -> web.Response:
    """updateListsNameByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = ListsName.from_dict(body)
    return web.Response(status=200)


async def update_lists_pos_by_id_list(request: web.Request, id_list, key, token, body) -> web.Response:
    """updateListsPosByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists Pos\&quot; to be updated.
    :type body: dict | bytes

    """
    body = ListsPos.from_dict(body)
    return web.Response(status=200)


async def update_lists_subscribed_by_id_list(request: web.Request, id_list, key, token, body) -> web.Response:
    """updateListsSubscribedByIdList()

    

    :param id_list: idList
    :type id_list: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Lists Subscribed\&quot; to be updated.
    :type body: dict | bytes

    """
    body = ListsSubscribed.from_dict(body)
    return web.Response(status=200)
