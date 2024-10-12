from typing import List, Dict
from aiohttp import web

from openapi_server.models.actions_comments import ActionsComments
from openapi_server.models.cards import Cards
from openapi_server.models.cards_actions_comments import CardsActionsComments
from openapi_server.models.cards_attachments import CardsAttachments
from openapi_server.models.cards_checklist_check_item import CardsChecklistCheckItem
from openapi_server.models.cards_checklist_check_item_name import CardsChecklistCheckItemName
from openapi_server.models.cards_checklist_check_item_pos import CardsChecklistCheckItemPos
from openapi_server.models.cards_checklist_check_item_state import CardsChecklistCheckItemState
from openapi_server.models.cards_checklist_id_checklist_current_check_item import CardsChecklistIdChecklistCurrentCheckItem
from openapi_server.models.cards_checklists import CardsChecklists
from openapi_server.models.cards_closed import CardsClosed
from openapi_server.models.cards_desc import CardsDesc
from openapi_server.models.cards_due import CardsDue
from openapi_server.models.cards_id_attachment_cover import CardsIdAttachmentCover
from openapi_server.models.cards_id_board import CardsIdBoard
from openapi_server.models.cards_id_labels import CardsIdLabels
from openapi_server.models.cards_id_list import CardsIdList
from openapi_server.models.cards_id_members import CardsIdMembers
from openapi_server.models.cards_labels import CardsLabels
from openapi_server.models.cards_members_voted import CardsMembersVoted
from openapi_server.models.cards_name import CardsName
from openapi_server.models.cards_pos import CardsPos
from openapi_server.models.cards_stickers import CardsStickers
from openapi_server.models.cards_subscribed import CardsSubscribed
from openapi_server import util


async def add_cards(request: web.Request, key, token, body) -> web.Response:
    """addCards()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards\&quot; to be added.
    :type body: dict | bytes

    """
    body = Cards.from_dict(body)
    return web.Response(status=200)


async def add_cards_actions_comments_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """addCardsActionsCommentsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Actions Comments\&quot; to be added.
    :type body: dict | bytes

    """
    body = ActionsComments.from_dict(body)
    return web.Response(status=200)


async def add_cards_attachments_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """addCardsAttachmentsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Attachments\&quot; to be added.
    :type body: dict | bytes

    """
    body = CardsAttachments.from_dict(body)
    return web.Response(status=200)


async def add_cards_checklist_check_item_by_id_card_by_id_checklist(request: web.Request, id_card, id_checklist, key, token, body) -> web.Response:
    """addCardsChecklistCheckItemByIdCardByIdChecklist()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Checklist Check Item\&quot; to be added.
    :type body: dict | bytes

    """
    body = CardsChecklistCheckItem.from_dict(body)
    return web.Response(status=200)


async def add_cards_checklist_check_item_convert_to_card_by_id_card_by_id_checklist_by_id_check_item(request: web.Request, id_card, id_checklist, id_check_item, key, token) -> web.Response:
    """addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem()

    

    :param id_card: card id or shortlink
    :type id_card: str
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


async def add_cards_checklists_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """addCardsChecklistsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Checklists\&quot; to be added.
    :type body: dict | bytes

    """
    body = CardsChecklists.from_dict(body)
    return web.Response(status=200)


async def add_cards_id_labels_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """addCardsIdLabelsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Id Labels\&quot; to be added.
    :type body: dict | bytes

    """
    body = CardsIdLabels.from_dict(body)
    return web.Response(status=200)


async def add_cards_id_members_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """addCardsIdMembersByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Id Members\&quot; to be added.
    :type body: dict | bytes

    """
    body = CardsIdMembers.from_dict(body)
    return web.Response(status=200)


async def add_cards_labels_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """addCardsLabelsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Labels\&quot; to be added.
    :type body: dict | bytes

    """
    body = CardsLabels.from_dict(body)
    return web.Response(status=200)


async def add_cards_mark_associated_notifications_read_by_id_card(request: web.Request, id_card, key, token) -> web.Response:
    """addCardsMarkAssociatedNotificationsReadByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def add_cards_members_voted_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """addCardsMembersVotedByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Members Voted\&quot; to be added.
    :type body: dict | bytes

    """
    body = CardsMembersVoted.from_dict(body)
    return web.Response(status=200)


async def add_cards_stickers_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """addCardsStickersByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Stickers\&quot; to be added.
    :type body: dict | bytes

    """
    body = CardsStickers.from_dict(body)
    return web.Response(status=200)


async def delete_cards_actions_comments_by_id_card_by_id_action(request: web.Request, id_card, id_action, key, token) -> web.Response:
    """deleteCardsActionsCommentsByIdCardByIdAction()

    This can only be done by the original author of the comment, or someone with higher permissions than the original author.

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_action: idAction
    :type id_action: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_cards_attachments_by_id_card_by_id_attachment(request: web.Request, id_card, id_attachment, key, token) -> web.Response:
    """deleteCardsAttachmentsByIdCardByIdAttachment()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_attachment: idAttachment
    :type id_attachment: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_cards_by_id_card(request: web.Request, id_card, key, token) -> web.Response:
    """deleteCardsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_cards_checklist_check_item_by_id_card_by_id_checklist_by_id_check_item(request: web.Request, id_card, id_checklist, id_check_item, key, token) -> web.Response:
    """deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem()

    

    :param id_card: card id or shortlink
    :type id_card: str
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


async def delete_cards_checklists_by_id_card_by_id_checklist(request: web.Request, id_card, id_checklist, key, token) -> web.Response:
    """deleteCardsChecklistsByIdCardByIdChecklist()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_checklist: idChecklist
    :type id_checklist: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_cards_id_labels_by_id_card_by_id_label(request: web.Request, id_card, id_label, key, token) -> web.Response:
    """deleteCardsIdLabelsByIdCardByIdLabel()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_label: idLabel
    :type id_label: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_cards_id_members_by_id_card_by_id_member(request: web.Request, id_card, id_member, key, token) -> web.Response:
    """deleteCardsIdMembersByIdCardByIdMember()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_cards_labels_by_id_card_by_color(request: web.Request, id_card, color, key, token) -> web.Response:
    """deleteCardsLabelsByIdCardByColor()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param color: color
    :type color: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_cards_members_voted_by_id_card_by_id_member(request: web.Request, id_card, id_member, key, token) -> web.Response:
    """deleteCardsMembersVotedByIdCardByIdMember()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_member: idMember
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_cards_stickers_by_id_card_by_id_sticker(request: web.Request, id_card, id_sticker, key, token) -> web.Response:
    """deleteCardsStickersByIdCardByIdSticker()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_sticker: idSticker
    :type id_sticker: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_cards_actions_by_id_card(request: web.Request, id_card, key, token, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, id_models=None, member=None, member_fields=None, member_creator=None, member_creator_fields=None) -> web.Response:
    """getCardsActionsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
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


async def get_cards_attachments_by_id_card(request: web.Request, id_card, key, token, fields=None, filter=None) -> web.Response:
    """getCardsAttachmentsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    :type fields: str
    :param filter: A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments
    :type filter: str

    """
    return web.Response(status=200)


async def get_cards_attachments_by_id_card_by_id_attachment(request: web.Request, id_card, id_attachment, key, token, fields=None) -> web.Response:
    """getCardsAttachmentsByIdCardByIdAttachment()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_attachment: idAttachment
    :type id_attachment: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_cards_board_by_id_card(request: web.Request, id_card, key, token, fields=None) -> web.Response:
    """getCardsBoardByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_cards_board_by_id_card_by_field(request: web.Request, id_card, _field, key, token) -> web.Response:
    """getCardsBoardByIdCardByField()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_cards_by_id_card(request: web.Request, id_card, key, token, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, action_member_creator_fields=None, attachments=None, attachment_fields=None, members=None, member_fields=None, members_voted=None, member_voted_fields=None, check_item_states=None, check_item_state_fields=None, checklists=None, checklist_fields=None, board=None, board_fields=None, list=None, list_fields=None, stickers=None, sticker_fields=None, fields=None) -> web.Response:
    """getCardsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
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
    :param action_member_creator_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type action_member_creator_fields: str
    :param attachments: A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments
    :type attachments: str
    :param attachment_fields: all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    :type attachment_fields: str
    :param members:  true or false
    :type members: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str
    :param members_voted:  true or false
    :type members_voted: str
    :param member_voted_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_voted_fields: str
    :param check_item_states:  true or false
    :type check_item_states: str
    :param check_item_state_fields: all or a comma-separated list of: idCheckItem or state
    :type check_item_state_fields: str
    :param checklists: One of: all or none
    :type checklists: str
    :param checklist_fields: all or a comma-separated list of: idBoard, idCard, name or pos
    :type checklist_fields: str
    :param board:  true or false
    :type board: str
    :param board_fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type board_fields: str
    :param list:  true or false
    :type list: str
    :param list_fields: all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    :type list_fields: str
    :param stickers:  true or false
    :type stickers: str
    :param sticker_fields: all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex
    :type sticker_fields: str
    :param fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_cards_by_id_card_by_field(request: web.Request, id_card, _field, key, token) -> web.Response:
    """getCardsByIdCardByField()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_cards_check_item_states_by_id_card(request: web.Request, id_card, key, token, fields=None) -> web.Response:
    """getCardsCheckItemStatesByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: idCheckItem or state
    :type fields: str

    """
    return web.Response(status=200)


async def get_cards_checklists_by_id_card(request: web.Request, id_card, key, token, cards=None, card_fields=None, check_items=None, check_item_fields=None, filter=None, fields=None) -> web.Response:
    """getCardsChecklistsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
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


async def get_cards_list_by_id_card(request: web.Request, id_card, key, token, fields=None) -> web.Response:
    """getCardsListByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    :type fields: str

    """
    return web.Response(status=200)


async def get_cards_list_by_id_card_by_field(request: web.Request, id_card, _field, key, token) -> web.Response:
    """getCardsListByIdCardByField()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_cards_members_by_id_card(request: web.Request, id_card, key, token, fields=None) -> web.Response:
    """getCardsMembersByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type fields: str

    """
    return web.Response(status=200)


async def get_cards_members_voted_by_id_card(request: web.Request, id_card, key, token, fields=None) -> web.Response:
    """getCardsMembersVotedByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type fields: str

    """
    return web.Response(status=200)


async def get_cards_stickers_by_id_card(request: web.Request, id_card, key, token, fields=None) -> web.Response:
    """getCardsStickersByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex
    :type fields: str

    """
    return web.Response(status=200)


async def get_cards_stickers_by_id_card_by_id_sticker(request: web.Request, id_card, id_sticker, key, token, fields=None) -> web.Response:
    """getCardsStickersByIdCardByIdSticker()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_sticker: idSticker
    :type id_sticker: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex
    :type fields: str

    """
    return web.Response(status=200)


async def update_cards_actions_comments_by_id_card_by_id_action(request: web.Request, id_card, id_action, key, token, body) -> web.Response:
    """updateCardsActionsCommentsByIdCardByIdAction()

    This can only be done by the original author of the comment.

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_action: idAction
    :type id_action: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Actions Comments\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsActionsComments.from_dict(body)
    return web.Response(status=200)


async def update_cards_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Cards.from_dict(body)
    return web.Response(status=200)


async def update_cards_checklist_check_item_by_id_card_by_id_checklist_current_by_id_check_item(request: web.Request, id_card, id_checklist_current, id_check_item, key, token, body) -> web.Response:
    """updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_checklist_current: idChecklistCurrent
    :type id_checklist_current: str
    :param id_check_item: idCheckItem
    :type id_check_item: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Checklist Id Checklist Current Check Item\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsChecklistIdChecklistCurrentCheckItem.from_dict(body)
    return web.Response(status=200)


async def update_cards_checklist_check_item_name_by_id_card_by_id_checklist_by_id_check_item(request: web.Request, id_card, id_checklist, id_check_item, key, token, body) -> web.Response:
    """updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_checklist: idChecklist
    :type id_checklist: str
    :param id_check_item: idCheckItem
    :type id_check_item: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Checklist Check Item Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsChecklistCheckItemName.from_dict(body)
    return web.Response(status=200)


async def update_cards_checklist_check_item_pos_by_id_card_by_id_checklist_by_id_check_item(request: web.Request, id_card, id_checklist, id_check_item, key, token, body) -> web.Response:
    """updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_checklist: idChecklist
    :type id_checklist: str
    :param id_check_item: idCheckItem
    :type id_check_item: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Checklist Check Item Pos\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsChecklistCheckItemPos.from_dict(body)
    return web.Response(status=200)


async def update_cards_checklist_check_item_state_by_id_card_by_id_checklist_by_id_check_item(request: web.Request, id_card, id_checklist, id_check_item, key, token, body) -> web.Response:
    """updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_checklist: idChecklist
    :type id_checklist: str
    :param id_check_item: idCheckItem
    :type id_check_item: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Checklist Check Item State\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsChecklistCheckItemState.from_dict(body)
    return web.Response(status=200)


async def update_cards_closed_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsClosedByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Closed\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsClosed.from_dict(body)
    return web.Response(status=200)


async def update_cards_desc_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsDescByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Desc\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsDesc.from_dict(body)
    return web.Response(status=200)


async def update_cards_due_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsDueByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Due\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsDue.from_dict(body)
    return web.Response(status=200)


async def update_cards_id_attachment_cover_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsIdAttachmentCoverByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Id Attachment Cover\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsIdAttachmentCover.from_dict(body)
    return web.Response(status=200)


async def update_cards_id_board_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsIdBoardByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Id Board\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsIdBoard.from_dict(body)
    return web.Response(status=200)


async def update_cards_id_list_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsIdListByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Id List\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsIdList.from_dict(body)
    return web.Response(status=200)


async def update_cards_id_members_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsIdMembersByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Id Members\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsIdMembers.from_dict(body)
    return web.Response(status=200)


async def update_cards_labels_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsLabelsByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Labels\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsLabels.from_dict(body)
    return web.Response(status=200)


async def update_cards_name_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsNameByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsName.from_dict(body)
    return web.Response(status=200)


async def update_cards_pos_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsPosByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Pos\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsPos.from_dict(body)
    return web.Response(status=200)


async def update_cards_stickers_by_id_card_by_id_sticker(request: web.Request, id_card, id_sticker, key, token, body) -> web.Response:
    """updateCardsStickersByIdCardByIdSticker()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param id_sticker: idSticker
    :type id_sticker: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Stickers\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsStickers.from_dict(body)
    return web.Response(status=200)


async def update_cards_subscribed_by_id_card(request: web.Request, id_card, key, token, body) -> web.Response:
    """updateCardsSubscribedByIdCard()

    

    :param id_card: card id or shortlink
    :type id_card: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Cards Subscribed\&quot; to be updated.
    :type body: dict | bytes

    """
    body = CardsSubscribed.from_dict(body)
    return web.Response(status=200)
