from typing import List, Dict
from aiohttp import web

from openapi_server.models.checklists import Checklists
from openapi_server.models.checklists_check_items import ChecklistsCheckItems
from openapi_server.models.checklists_id_card import ChecklistsIdCard
from openapi_server.models.checklists_name import ChecklistsName
from openapi_server.models.checklists_pos import ChecklistsPos
from openapi_server import util


async def add_checklists(request: web.Request, key, token, body) -> web.Response:
    """addChecklists()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Checklists\&quot; to be added.
    :type body: dict | bytes

    """
    body = Checklists.from_dict(body)
    return web.Response(status=200)


async def add_checklists_check_items_by_id_checklist(request: web.Request, id_checklist, key, token, body) -> web.Response:
    """addChecklistsCheckItemsByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Checklists Check Items\&quot; to be added.
    :type body: dict | bytes

    """
    body = ChecklistsCheckItems.from_dict(body)
    return web.Response(status=200)


async def delete_checklists_by_id_checklist(request: web.Request, id_checklist, key, token) -> web.Response:
    """deleteChecklistsByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_checklists_check_items_by_id_checklist_by_id_check_item(request: web.Request, id_checklist, id_check_item, key, token) -> web.Response:
    """deleteChecklistsCheckItemsByIdChecklistByIdCheckItem()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param id_check_item: idCheckItem
    :type id_check_item: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_checklists_board_by_id_checklist(request: web.Request, id_checklist, key, token, fields=None) -> web.Response:
    """getChecklistsBoardByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_checklists_board_by_id_checklist_by_field(request: web.Request, id_checklist, _field, key, token) -> web.Response:
    """getChecklistsBoardByIdChecklistByField()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_checklists_by_id_checklist(request: web.Request, id_checklist, key, token, cards=None, card_fields=None, check_items=None, check_item_fields=None, fields=None) -> web.Response:
    """getChecklistsByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
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
    :param fields: all or a comma-separated list of: idBoard, idCard, name or pos
    :type fields: str

    """
    return web.Response(status=200)


async def get_checklists_by_id_checklist_by_field(request: web.Request, id_checklist, _field, key, token) -> web.Response:
    """getChecklistsByIdChecklistByField()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_checklists_cards_by_id_checklist(request: web.Request, id_checklist, key, token, actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, check_item_states=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None) -> web.Response:
    """getChecklistsCardsByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
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


async def get_checklists_cards_by_id_checklist_by_filter(request: web.Request, id_checklist, filter, key, token) -> web.Response:
    """getChecklistsCardsByIdChecklistByFilter()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_checklists_check_items_by_id_checklist(request: web.Request, id_checklist, key, token, filter=None, fields=None) -> web.Response:
    """getChecklistsCheckItemsByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: all or none
    :type filter: str
    :param fields: all or a comma-separated list of: name, nameData, pos, state or type
    :type fields: str

    """
    return web.Response(status=200)


async def get_checklists_check_items_by_id_checklist_by_id_check_item(request: web.Request, id_checklist, id_check_item, key, token, fields=None) -> web.Response:
    """getChecklistsCheckItemsByIdChecklistByIdCheckItem()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param id_check_item: idCheckItem
    :type id_check_item: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: name, nameData, pos, state or type
    :type fields: str

    """
    return web.Response(status=200)


async def update_checklists_by_id_checklist(request: web.Request, id_checklist, key, token, body) -> web.Response:
    """updateChecklistsByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Checklists\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Checklists.from_dict(body)
    return web.Response(status=200)


async def update_checklists_id_card_by_id_checklist(request: web.Request, id_checklist, key, token, body) -> web.Response:
    """updateChecklistsIdCardByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Checklists Id Card\&quot; to be updated.
    :type body: dict | bytes

    """
    body = ChecklistsIdCard.from_dict(body)
    return web.Response(status=200)


async def update_checklists_name_by_id_checklist(request: web.Request, id_checklist, key, token, body) -> web.Response:
    """updateChecklistsNameByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Checklists Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = ChecklistsName.from_dict(body)
    return web.Response(status=200)


async def update_checklists_pos_by_id_checklist(request: web.Request, id_checklist, key, token, body) -> web.Response:
    """updateChecklistsPosByIdChecklist()

    

    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Checklists Pos\&quot; to be updated.
    :type body: dict | bytes

    """
    body = ChecklistsPos.from_dict(body)
    return web.Response(status=200)
