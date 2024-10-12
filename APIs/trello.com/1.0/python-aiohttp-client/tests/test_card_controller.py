# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_add_cards(client):
    """Test case for add_cards

    addCards()
    """
    body = openapi_server.Cards()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_actions_comments_by_id_card(client):
    """Test case for add_cards_actions_comments_by_id_card

    addCardsActionsCommentsByIdCard()
    """
    body = openapi_server.ActionsComments()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/actions/comments'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_attachments_by_id_card(client):
    """Test case for add_cards_attachments_by_id_card

    addCardsAttachmentsByIdCard()
    """
    body = openapi_server.CardsAttachments()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/attachments'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_checklist_check_item_by_id_card_by_id_checklist(client):
    """Test case for add_cards_checklist_check_item_by_id_card_by_id_checklist

    addCardsChecklistCheckItemByIdCardByIdChecklist()
    """
    body = openapi_server.CardsChecklistCheckItem()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/checklist/{id_checklist}/checkItem'.format(id_card='id_card_example', id_checklist='id_checklist_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_checklist_check_item_convert_to_card_by_id_card_by_id_checklist_by_id_check_item(client):
    """Test case for add_cards_checklist_check_item_convert_to_card_by_id_card_by_id_checklist_by_id_check_item

    addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/checklist/{id_checklist}/checkItem/{id_check_item}/convertToCard'.format(id_card='id_card_example', id_checklist='id_checklist_example', id_check_item='id_check_item_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_checklists_by_id_card(client):
    """Test case for add_cards_checklists_by_id_card

    addCardsChecklistsByIdCard()
    """
    body = openapi_server.CardsChecklists()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/checklists'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_id_labels_by_id_card(client):
    """Test case for add_cards_id_labels_by_id_card

    addCardsIdLabelsByIdCard()
    """
    body = openapi_server.CardsIdLabels()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/idLabels'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_id_members_by_id_card(client):
    """Test case for add_cards_id_members_by_id_card

    addCardsIdMembersByIdCard()
    """
    body = openapi_server.CardsIdMembers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/idMembers'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_labels_by_id_card(client):
    """Test case for add_cards_labels_by_id_card

    addCardsLabelsByIdCard()
    """
    body = openapi_server.CardsLabels()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/labels'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_mark_associated_notifications_read_by_id_card(client):
    """Test case for add_cards_mark_associated_notifications_read_by_id_card

    addCardsMarkAssociatedNotificationsReadByIdCard()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/markAssociatedNotificationsRead'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_members_voted_by_id_card(client):
    """Test case for add_cards_members_voted_by_id_card

    addCardsMembersVotedByIdCard()
    """
    body = openapi_server.CardsMembersVoted()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/membersVoted'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_cards_stickers_by_id_card(client):
    """Test case for add_cards_stickers_by_id_card

    addCardsStickersByIdCard()
    """
    body = openapi_server.CardsStickers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/cards/{id_card}/stickers'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_actions_comments_by_id_card_by_id_action(client):
    """Test case for delete_cards_actions_comments_by_id_card_by_id_action

    deleteCardsActionsCommentsByIdCardByIdAction()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/actions/{id_action}/comments'.format(id_card='id_card_example', id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_attachments_by_id_card_by_id_attachment(client):
    """Test case for delete_cards_attachments_by_id_card_by_id_attachment

    deleteCardsAttachmentsByIdCardByIdAttachment()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/attachments/{id_attachment}'.format(id_card='id_card_example', id_attachment='id_attachment_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_by_id_card(client):
    """Test case for delete_cards_by_id_card

    deleteCardsByIdCard()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_checklist_check_item_by_id_card_by_id_checklist_by_id_check_item(client):
    """Test case for delete_cards_checklist_check_item_by_id_card_by_id_checklist_by_id_check_item

    deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/checklist/{id_checklist}/checkItem/{id_check_item}'.format(id_card='id_card_example', id_checklist='id_checklist_example', id_check_item='id_check_item_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_checklists_by_id_card_by_id_checklist(client):
    """Test case for delete_cards_checklists_by_id_card_by_id_checklist

    deleteCardsChecklistsByIdCardByIdChecklist()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/checklists/{id_checklist}'.format(id_card='id_card_example', id_checklist='id_checklist_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_id_labels_by_id_card_by_id_label(client):
    """Test case for delete_cards_id_labels_by_id_card_by_id_label

    deleteCardsIdLabelsByIdCardByIdLabel()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/idLabels/{id_label}'.format(id_card='id_card_example', id_label='id_label_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_id_members_by_id_card_by_id_member(client):
    """Test case for delete_cards_id_members_by_id_card_by_id_member

    deleteCardsIdMembersByIdCardByIdMember()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/idMembers/{id_member}'.format(id_card='id_card_example', id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_labels_by_id_card_by_color(client):
    """Test case for delete_cards_labels_by_id_card_by_color

    deleteCardsLabelsByIdCardByColor()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/labels/{color}'.format(id_card='id_card_example', color='color_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_members_voted_by_id_card_by_id_member(client):
    """Test case for delete_cards_members_voted_by_id_card_by_id_member

    deleteCardsMembersVotedByIdCardByIdMember()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/membersVoted/{id_member}'.format(id_card='id_card_example', id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cards_stickers_by_id_card_by_id_sticker(client):
    """Test case for delete_cards_stickers_by_id_card_by_id_sticker

    deleteCardsStickersByIdCardByIdSticker()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/cards/{id_card}/stickers/{id_sticker}'.format(id_card='id_card_example', id_sticker='id_sticker_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_actions_by_id_card(client):
    """Test case for get_cards_actions_by_id_card

    getCardsActionsByIdCard()
    """
    params = [('entities', 'entities_example'),
                    ('display', 'display_example'),
                    ('filter', 'commentCard and updateCard:idList'),
                    ('fields', 'all'),
                    ('limit', '50'),
                    ('format', 'list'),
                    ('since', 'since_example'),
                    ('before', 'before_example'),
                    ('page', '0'),
                    ('idModels', 'id_models_example'),
                    ('member', 'member_example'),
                    ('member_fields', 'avatarHash, fullName, initials and username'),
                    ('memberCreator', 'member_creator_example'),
                    ('memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/actions'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_attachments_by_id_card(client):
    """Test case for get_cards_attachments_by_id_card

    getCardsAttachmentsByIdCard()
    """
    params = [('fields', 'all'),
                    ('filter', 'filter_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/attachments'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_attachments_by_id_card_by_id_attachment(client):
    """Test case for get_cards_attachments_by_id_card_by_id_attachment

    getCardsAttachmentsByIdCardByIdAttachment()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/attachments/{id_attachment}'.format(id_card='id_card_example', id_attachment='id_attachment_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_board_by_id_card(client):
    """Test case for get_cards_board_by_id_card

    getCardsBoardByIdCard()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/board'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_board_by_id_card_by_field(client):
    """Test case for get_cards_board_by_id_card_by_field

    getCardsBoardByIdCardByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/board/{_field}'.format(id_card='id_card_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_by_id_card(client):
    """Test case for get_cards_by_id_card

    getCardsByIdCard()
    """
    params = [('actions', 'actions_example'),
                    ('actions_entities', 'actions_entities_example'),
                    ('actions_display', 'actions_display_example'),
                    ('actions_limit', '50'),
                    ('action_fields', 'all'),
                    ('action_memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('attachments', 'attachments_example'),
                    ('attachment_fields', 'all'),
                    ('members', 'members_example'),
                    ('member_fields', 'avatarHash, fullName, initials and username'),
                    ('membersVoted', 'members_voted_example'),
                    ('memberVoted_fields', 'avatarHash, fullName, initials and username'),
                    ('checkItemStates', 'check_item_states_example'),
                    ('checkItemState_fields', 'all'),
                    ('checklists', 'none'),
                    ('checklist_fields', 'all'),
                    ('board', 'board_example'),
                    ('board_fields', 'name, desc, descData, closed, idOrganization, pinned, url and prefs'),
                    ('list', 'list_example'),
                    ('list_fields', 'all'),
                    ('stickers', 'stickers_example'),
                    ('sticker_fields', 'all'),
                    ('fields', 'badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl and url'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_by_id_card_by_field(client):
    """Test case for get_cards_by_id_card_by_field

    getCardsByIdCardByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/{_field}'.format(id_card='id_card_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_check_item_states_by_id_card(client):
    """Test case for get_cards_check_item_states_by_id_card

    getCardsCheckItemStatesByIdCard()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/checkItemStates'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_checklists_by_id_card(client):
    """Test case for get_cards_checklists_by_id_card

    getCardsChecklistsByIdCard()
    """
    params = [('cards', 'none'),
                    ('card_fields', 'all'),
                    ('checkItems', 'all'),
                    ('checkItem_fields', 'name, nameData, pos and state'),
                    ('filter', 'all'),
                    ('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/checklists'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_list_by_id_card(client):
    """Test case for get_cards_list_by_id_card

    getCardsListByIdCard()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/list'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_list_by_id_card_by_field(client):
    """Test case for get_cards_list_by_id_card_by_field

    getCardsListByIdCardByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/list/{_field}'.format(id_card='id_card_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_members_by_id_card(client):
    """Test case for get_cards_members_by_id_card

    getCardsMembersByIdCard()
    """
    params = [('fields', 'avatarHash, fullName, initials and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/members'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_members_voted_by_id_card(client):
    """Test case for get_cards_members_voted_by_id_card

    getCardsMembersVotedByIdCard()
    """
    params = [('fields', 'avatarHash, fullName, initials and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/membersVoted'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_stickers_by_id_card(client):
    """Test case for get_cards_stickers_by_id_card

    getCardsStickersByIdCard()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/stickers'.format(id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cards_stickers_by_id_card_by_id_sticker(client):
    """Test case for get_cards_stickers_by_id_card_by_id_sticker

    getCardsStickersByIdCardByIdSticker()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/cards/{id_card}/stickers/{id_sticker}'.format(id_card='id_card_example', id_sticker='id_sticker_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_actions_comments_by_id_card_by_id_action(client):
    """Test case for update_cards_actions_comments_by_id_card_by_id_action

    updateCardsActionsCommentsByIdCardByIdAction()
    """
    body = openapi_server.CardsActionsComments()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/actions/{id_action}/comments'.format(id_card='id_card_example', id_action='id_action_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_by_id_card(client):
    """Test case for update_cards_by_id_card

    updateCardsByIdCard()
    """
    body = openapi_server.Cards()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_checklist_check_item_by_id_card_by_id_checklist_current_by_id_check_item(client):
    """Test case for update_cards_checklist_check_item_by_id_card_by_id_checklist_current_by_id_check_item

    updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem()
    """
    body = openapi_server.CardsChecklistIdChecklistCurrentCheckItem()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/checklist/{id_checklist_current}/checkItem/{id_check_item}'.format(id_card='id_card_example', id_checklist_current='id_checklist_current_example', id_check_item='id_check_item_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_checklist_check_item_name_by_id_card_by_id_checklist_by_id_check_item(client):
    """Test case for update_cards_checklist_check_item_name_by_id_card_by_id_checklist_by_id_check_item

    updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem()
    """
    body = openapi_server.CardsChecklistCheckItemName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/checklist/{id_checklist}/checkItem/{id_check_item}/name'.format(id_card='id_card_example', id_checklist='id_checklist_example', id_check_item='id_check_item_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_checklist_check_item_pos_by_id_card_by_id_checklist_by_id_check_item(client):
    """Test case for update_cards_checklist_check_item_pos_by_id_card_by_id_checklist_by_id_check_item

    updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem()
    """
    body = openapi_server.CardsChecklistCheckItemPos()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/checklist/{id_checklist}/checkItem/{id_check_item}/pos'.format(id_card='id_card_example', id_checklist='id_checklist_example', id_check_item='id_check_item_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_checklist_check_item_state_by_id_card_by_id_checklist_by_id_check_item(client):
    """Test case for update_cards_checklist_check_item_state_by_id_card_by_id_checklist_by_id_check_item

    updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem()
    """
    body = openapi_server.CardsChecklistCheckItemState()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/checklist/{id_checklist}/checkItem/{id_check_item}/state'.format(id_card='id_card_example', id_checklist='id_checklist_example', id_check_item='id_check_item_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_closed_by_id_card(client):
    """Test case for update_cards_closed_by_id_card

    updateCardsClosedByIdCard()
    """
    body = openapi_server.CardsClosed()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/closed'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_desc_by_id_card(client):
    """Test case for update_cards_desc_by_id_card

    updateCardsDescByIdCard()
    """
    body = openapi_server.CardsDesc()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/desc'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_due_by_id_card(client):
    """Test case for update_cards_due_by_id_card

    updateCardsDueByIdCard()
    """
    body = openapi_server.CardsDue()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/due'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_id_attachment_cover_by_id_card(client):
    """Test case for update_cards_id_attachment_cover_by_id_card

    updateCardsIdAttachmentCoverByIdCard()
    """
    body = openapi_server.CardsIdAttachmentCover()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/idAttachmentCover'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_id_board_by_id_card(client):
    """Test case for update_cards_id_board_by_id_card

    updateCardsIdBoardByIdCard()
    """
    body = openapi_server.CardsIdBoard()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/idBoard'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_id_list_by_id_card(client):
    """Test case for update_cards_id_list_by_id_card

    updateCardsIdListByIdCard()
    """
    body = openapi_server.CardsIdList()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/idList'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_id_members_by_id_card(client):
    """Test case for update_cards_id_members_by_id_card

    updateCardsIdMembersByIdCard()
    """
    body = openapi_server.CardsIdMembers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/idMembers'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_labels_by_id_card(client):
    """Test case for update_cards_labels_by_id_card

    updateCardsLabelsByIdCard()
    """
    body = openapi_server.CardsLabels()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/labels'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_name_by_id_card(client):
    """Test case for update_cards_name_by_id_card

    updateCardsNameByIdCard()
    """
    body = openapi_server.CardsName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/name'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_pos_by_id_card(client):
    """Test case for update_cards_pos_by_id_card

    updateCardsPosByIdCard()
    """
    body = openapi_server.CardsPos()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/pos'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_stickers_by_id_card_by_id_sticker(client):
    """Test case for update_cards_stickers_by_id_card_by_id_sticker

    updateCardsStickersByIdCardByIdSticker()
    """
    body = openapi_server.CardsStickers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/stickers/{id_sticker}'.format(id_card='id_card_example', id_sticker='id_sticker_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cards_subscribed_by_id_card(client):
    """Test case for update_cards_subscribed_by_id_card

    updateCardsSubscribedByIdCard()
    """
    body = openapi_server.CardsSubscribed()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/cards/{id_card}/subscribed'.format(id_card='id_card_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

