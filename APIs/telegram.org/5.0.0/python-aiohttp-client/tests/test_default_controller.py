# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.add_sticker_to_set_post200_response import AddStickerToSetPost200Response
from openapi_server.models.answer_callback_query_post_request import AnswerCallbackQueryPostRequest
from openapi_server.models.answer_inline_query_post_request import AnswerInlineQueryPostRequest
from openapi_server.models.answer_pre_checkout_query_post_request import AnswerPreCheckoutQueryPostRequest
from openapi_server.models.answer_shipping_query_post_request import AnswerShippingQueryPostRequest
from openapi_server.models.copy_message_post200_response import CopyMessagePost200Response
from openapi_server.models.copy_message_post_request import CopyMessagePostRequest
from openapi_server.models.copy_message_post_request_chat_id import CopyMessagePostRequestChatId
from openapi_server.models.copy_message_post_request_reply_markup import CopyMessagePostRequestReplyMarkup
from openapi_server.models.delete_chat_photo_post_request import DeleteChatPhotoPostRequest
from openapi_server.models.delete_chat_sticker_set_post_request import DeleteChatStickerSetPostRequest
from openapi_server.models.delete_message_post_request import DeleteMessagePostRequest
from openapi_server.models.delete_sticker_from_set_post_request import DeleteStickerFromSetPostRequest
from openapi_server.models.delete_webhook_post_request import DeleteWebhookPostRequest
from openapi_server.models.edit_message_caption_post200_response import EditMessageCaptionPost200Response
from openapi_server.models.edit_message_caption_post_request import EditMessageCaptionPostRequest
from openapi_server.models.edit_message_caption_post_request_chat_id import EditMessageCaptionPostRequestChatId
from openapi_server.models.edit_message_live_location_post_request import EditMessageLiveLocationPostRequest
from openapi_server.models.edit_message_reply_markup_post_request import EditMessageReplyMarkupPostRequest
from openapi_server.models.edit_message_text_post_request import EditMessageTextPostRequest
from openapi_server.models.error import Error
from openapi_server.models.export_chat_invite_link_post200_response import ExportChatInviteLinkPost200Response
from openapi_server.models.forward_message_post200_response import ForwardMessagePost200Response
from openapi_server.models.forward_message_post_request import ForwardMessagePostRequest
from openapi_server.models.get_chat_administrators_post200_response import GetChatAdministratorsPost200Response
from openapi_server.models.get_chat_member_post200_response import GetChatMemberPost200Response
from openapi_server.models.get_chat_member_post_request import GetChatMemberPostRequest
from openapi_server.models.get_chat_members_count_post200_response import GetChatMembersCountPost200Response
from openapi_server.models.get_chat_post200_response import GetChatPost200Response
from openapi_server.models.get_chat_post_request import GetChatPostRequest
from openapi_server.models.get_file_post200_response import GetFilePost200Response
from openapi_server.models.get_file_post_request import GetFilePostRequest
from openapi_server.models.get_game_high_scores_post200_response import GetGameHighScoresPost200Response
from openapi_server.models.get_game_high_scores_post_request import GetGameHighScoresPostRequest
from openapi_server.models.get_me_post200_response import GetMePost200Response
from openapi_server.models.get_my_commands_post200_response import GetMyCommandsPost200Response
from openapi_server.models.get_sticker_set_post200_response import GetStickerSetPost200Response
from openapi_server.models.get_sticker_set_post_request import GetStickerSetPostRequest
from openapi_server.models.get_updates_post200_response import GetUpdatesPost200Response
from openapi_server.models.get_updates_post_request import GetUpdatesPostRequest
from openapi_server.models.get_user_profile_photos_post200_response import GetUserProfilePhotosPost200Response
from openapi_server.models.get_user_profile_photos_post_request import GetUserProfilePhotosPostRequest
from openapi_server.models.get_webhook_info_post200_response import GetWebhookInfoPost200Response
from openapi_server.models.inline_keyboard_markup import InlineKeyboardMarkup
from openapi_server.models.input_media import InputMedia
from openapi_server.models.kick_chat_member_post_request import KickChatMemberPostRequest
from openapi_server.models.mask_position import MaskPosition
from openapi_server.models.message_entity import MessageEntity
from openapi_server.models.pin_chat_message_post_request import PinChatMessagePostRequest
from openapi_server.models.promote_chat_member_post_request import PromoteChatMemberPostRequest
from openapi_server.models.restrict_chat_member_post_request import RestrictChatMemberPostRequest
from openapi_server.models.send_chat_action_post_request import SendChatActionPostRequest
from openapi_server.models.send_contact_post_request import SendContactPostRequest
from openapi_server.models.send_dice_post_request import SendDicePostRequest
from openapi_server.models.send_game_post_request import SendGamePostRequest
from openapi_server.models.send_invoice_post_request import SendInvoicePostRequest
from openapi_server.models.send_location_post_request import SendLocationPostRequest
from openapi_server.models.send_media_group_post200_response import SendMediaGroupPost200Response
from openapi_server.models.send_media_group_post_request_media_inner import SendMediaGroupPostRequestMediaInner
from openapi_server.models.send_message_post_request import SendMessagePostRequest
from openapi_server.models.send_poll_post_request import SendPollPostRequest
from openapi_server.models.send_venue_post_request import SendVenuePostRequest
from openapi_server.models.set_chat_administrator_custom_title_post_request import SetChatAdministratorCustomTitlePostRequest
from openapi_server.models.set_chat_description_post_request import SetChatDescriptionPostRequest
from openapi_server.models.set_chat_permissions_post_request import SetChatPermissionsPostRequest
from openapi_server.models.set_chat_sticker_set_post_request import SetChatStickerSetPostRequest
from openapi_server.models.set_chat_title_post_request import SetChatTitlePostRequest
from openapi_server.models.set_game_score_post_request import SetGameScorePostRequest
from openapi_server.models.set_my_commands_post_request import SetMyCommandsPostRequest
from openapi_server.models.set_passport_data_errors_post_request import SetPassportDataErrorsPostRequest
from openapi_server.models.set_sticker_position_in_set_post_request import SetStickerPositionInSetPostRequest
from openapi_server.models.stop_message_live_location_post_request import StopMessageLiveLocationPostRequest
from openapi_server.models.stop_poll_post200_response import StopPollPost200Response
from openapi_server.models.stop_poll_post_request import StopPollPostRequest
from openapi_server.models.unban_chat_member_post_request import UnbanChatMemberPostRequest
from openapi_server.models.unpin_chat_message_post_request import UnpinChatMessagePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_add_sticker_to_set_post(client):
    """Test case for add_sticker_to_set_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('emojis', 'emojis_example')
    data.add_field('mask_position', openapi_server.MaskPosition())
    data.add_field('name', 'name_example')
    data.add_field('png_sticker', 'png_sticker_example')
    data.add_field('tgs_sticker', None)
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/addStickerToSet',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_answer_callback_query_post(client):
    """Test case for answer_callback_query_post

    
    """
    body = openapi_server.AnswerCallbackQueryPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/answerCallbackQuery',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_answer_inline_query_post(client):
    """Test case for answer_inline_query_post

    
    """
    body = openapi_server.AnswerInlineQueryPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/answerInlineQuery',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_answer_pre_checkout_query_post(client):
    """Test case for answer_pre_checkout_query_post

    
    """
    body = openapi_server.AnswerPreCheckoutQueryPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/answerPreCheckoutQuery',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_answer_shipping_query_post(client):
    """Test case for answer_shipping_query_post

    
    """
    body = openapi_server.AnswerShippingQueryPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/answerShippingQuery',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_close_post(client):
    """Test case for close_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/close',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_copy_message_post(client):
    """Test case for copy_message_post

    
    """
    body = openapi_server.CopyMessagePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/copyMessage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_new_sticker_set_post(client):
    """Test case for create_new_sticker_set_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('contains_masks', True)
    data.add_field('emojis', 'emojis_example')
    data.add_field('mask_position', openapi_server.MaskPosition())
    data.add_field('name', 'name_example')
    data.add_field('png_sticker', 'png_sticker_example')
    data.add_field('tgs_sticker', None)
    data.add_field('title', 'title_example')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/createNewStickerSet',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_delete_chat_photo_post(client):
    """Test case for delete_chat_photo_post

    
    """
    body = openapi_server.DeleteChatPhotoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/deleteChatPhoto',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_delete_chat_sticker_set_post(client):
    """Test case for delete_chat_sticker_set_post

    
    """
    body = openapi_server.DeleteChatStickerSetPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/deleteChatStickerSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_delete_message_post(client):
    """Test case for delete_message_post

    
    """
    body = openapi_server.DeleteMessagePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/deleteMessage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_delete_sticker_from_set_post(client):
    """Test case for delete_sticker_from_set_post

    
    """
    body = openapi_server.DeleteStickerFromSetPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/deleteStickerFromSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_delete_webhook_post(client):
    """Test case for delete_webhook_post

    
    """
    body = openapi_server.DeleteWebhookPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/deleteWebhook',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_edit_message_caption_post(client):
    """Test case for edit_message_caption_post

    
    """
    body = openapi_server.EditMessageCaptionPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/editMessageCaption',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_edit_message_live_location_post(client):
    """Test case for edit_message_live_location_post

    
    """
    body = openapi_server.EditMessageLiveLocationPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/editMessageLiveLocation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_edit_message_media_post(client):
    """Test case for edit_message_media_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('chat_id', openapi_server.EditMessageCaptionPostRequestChatId())
    data.add_field('inline_message_id', 'inline_message_id_example')
    data.add_field('media', openapi_server.InputMedia())
    data.add_field('message_id', 56)
    data.add_field('reply_markup', openapi_server.InlineKeyboardMarkup())
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/editMessageMedia',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_edit_message_reply_markup_post(client):
    """Test case for edit_message_reply_markup_post

    
    """
    body = openapi_server.EditMessageReplyMarkupPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/editMessageReplyMarkup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_edit_message_text_post(client):
    """Test case for edit_message_text_post

    
    """
    body = openapi_server.EditMessageTextPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/editMessageText',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_export_chat_invite_link_post(client):
    """Test case for export_chat_invite_link_post

    
    """
    body = openapi_server.DeleteChatPhotoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/exportChatInviteLink',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forward_message_post(client):
    """Test case for forward_message_post

    
    """
    body = openapi_server.ForwardMessagePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/forwardMessage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_chat_administrators_post(client):
    """Test case for get_chat_administrators_post

    
    """
    body = openapi_server.GetChatPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getChatAdministrators',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_chat_member_post(client):
    """Test case for get_chat_member_post

    
    """
    body = openapi_server.GetChatMemberPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getChatMember',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_chat_members_count_post(client):
    """Test case for get_chat_members_count_post

    
    """
    body = openapi_server.GetChatPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getChatMembersCount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_chat_post(client):
    """Test case for get_chat_post

    
    """
    body = openapi_server.GetChatPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getChat',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_file_post(client):
    """Test case for get_file_post

    
    """
    body = openapi_server.GetFilePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getFile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_game_high_scores_post(client):
    """Test case for get_game_high_scores_post

    
    """
    body = openapi_server.GetGameHighScoresPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getGameHighScores',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_me_post(client):
    """Test case for get_me_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_my_commands_post(client):
    """Test case for get_my_commands_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMyCommands',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_sticker_set_post(client):
    """Test case for get_sticker_set_post

    
    """
    body = openapi_server.GetStickerSetPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getStickerSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_updates_post(client):
    """Test case for get_updates_post

    
    """
    body = openapi_server.GetUpdatesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getUpdates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_user_profile_photos_post(client):
    """Test case for get_user_profile_photos_post

    
    """
    body = openapi_server.GetUserProfilePhotosPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getUserProfilePhotos',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_info_post(client):
    """Test case for get_webhook_info_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getWebhookInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_kick_chat_member_post(client):
    """Test case for kick_chat_member_post

    
    """
    body = openapi_server.KickChatMemberPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/kickChatMember',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_leave_chat_post(client):
    """Test case for leave_chat_post

    
    """
    body = openapi_server.GetChatPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/leaveChat',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_out_post(client):
    """Test case for log_out_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/logOut',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_pin_chat_message_post(client):
    """Test case for pin_chat_message_post

    
    """
    body = openapi_server.PinChatMessagePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/pinChatMessage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_promote_chat_member_post(client):
    """Test case for promote_chat_member_post

    
    """
    body = openapi_server.PromoteChatMemberPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/promoteChatMember',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_restrict_chat_member_post(client):
    """Test case for restrict_chat_member_post

    
    """
    body = openapi_server.RestrictChatMemberPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/restrictChatMember',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_animation_post(client):
    """Test case for send_animation_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('animation', 'animation_example')
    data.add_field('caption', 'caption_example')
    data.add_field('caption_entities', [openapi_server.MessageEntity()])
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_notification', True)
    data.add_field('duration', 56)
    data.add_field('height', 56)
    data.add_field('parse_mode', 'parse_mode_example')
    data.add_field('reply_markup', openapi_server.CopyMessagePostRequestReplyMarkup())
    data.add_field('reply_to_message_id', 56)
    data.add_field('thumb', 'thumb_example')
    data.add_field('width', 56)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendAnimation',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_audio_post(client):
    """Test case for send_audio_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('audio', 'audio_example')
    data.add_field('caption', 'caption_example')
    data.add_field('caption_entities', [openapi_server.MessageEntity()])
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_notification', True)
    data.add_field('duration', 56)
    data.add_field('parse_mode', 'parse_mode_example')
    data.add_field('performer', 'performer_example')
    data.add_field('reply_markup', openapi_server.CopyMessagePostRequestReplyMarkup())
    data.add_field('reply_to_message_id', 56)
    data.add_field('thumb', 'thumb_example')
    data.add_field('title', 'title_example')
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendAudio',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_chat_action_post(client):
    """Test case for send_chat_action_post

    
    """
    body = openapi_server.SendChatActionPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendChatAction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_contact_post(client):
    """Test case for send_contact_post

    
    """
    body = openapi_server.SendContactPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendContact',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_dice_post(client):
    """Test case for send_dice_post

    
    """
    body = openapi_server.SendDicePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendDice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_document_post(client):
    """Test case for send_document_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('caption', 'caption_example')
    data.add_field('caption_entities', [openapi_server.MessageEntity()])
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_content_type_detection', True)
    data.add_field('disable_notification', True)
    data.add_field('document', 'document_example')
    data.add_field('parse_mode', 'parse_mode_example')
    data.add_field('reply_markup', openapi_server.CopyMessagePostRequestReplyMarkup())
    data.add_field('reply_to_message_id', 56)
    data.add_field('thumb', 'thumb_example')
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendDocument',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_game_post(client):
    """Test case for send_game_post

    
    """
    body = openapi_server.SendGamePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendGame',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_invoice_post(client):
    """Test case for send_invoice_post

    
    """
    body = openapi_server.SendInvoicePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendInvoice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_location_post(client):
    """Test case for send_location_post

    
    """
    body = openapi_server.SendLocationPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendLocation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_media_group_post(client):
    """Test case for send_media_group_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_notification', True)
    data.add_field('media', [openapi_server.SendMediaGroupPostRequestMediaInner()])
    data.add_field('reply_to_message_id', 56)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendMediaGroup',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_message_post(client):
    """Test case for send_message_post

    
    """
    body = openapi_server.SendMessagePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendMessage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_photo_post(client):
    """Test case for send_photo_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('caption', 'caption_example')
    data.add_field('caption_entities', [openapi_server.MessageEntity()])
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_notification', True)
    data.add_field('parse_mode', 'parse_mode_example')
    data.add_field('photo', 'photo_example')
    data.add_field('reply_markup', openapi_server.CopyMessagePostRequestReplyMarkup())
    data.add_field('reply_to_message_id', 56)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendPhoto',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_poll_post(client):
    """Test case for send_poll_post

    
    """
    body = openapi_server.SendPollPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendPoll',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_sticker_post(client):
    """Test case for send_sticker_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_notification', True)
    data.add_field('reply_markup', openapi_server.CopyMessagePostRequestReplyMarkup())
    data.add_field('reply_to_message_id', 56)
    data.add_field('sticker', 'sticker_example')
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendSticker',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_send_venue_post(client):
    """Test case for send_venue_post

    
    """
    body = openapi_server.SendVenuePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendVenue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_video_note_post(client):
    """Test case for send_video_note_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_notification', True)
    data.add_field('duration', 56)
    data.add_field('length', 56)
    data.add_field('reply_markup', openapi_server.CopyMessagePostRequestReplyMarkup())
    data.add_field('reply_to_message_id', 56)
    data.add_field('thumb', 'thumb_example')
    data.add_field('video_note', 'video_note_example')
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendVideoNote',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_video_post(client):
    """Test case for send_video_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('caption', 'caption_example')
    data.add_field('caption_entities', [openapi_server.MessageEntity()])
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_notification', True)
    data.add_field('duration', 56)
    data.add_field('height', 56)
    data.add_field('parse_mode', 'parse_mode_example')
    data.add_field('reply_markup', openapi_server.CopyMessagePostRequestReplyMarkup())
    data.add_field('reply_to_message_id', 56)
    data.add_field('supports_streaming', True)
    data.add_field('thumb', 'thumb_example')
    data.add_field('video', 'video_example')
    data.add_field('width', 56)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendVideo',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_send_voice_post(client):
    """Test case for send_voice_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allow_sending_without_reply', True)
    data.add_field('caption', 'caption_example')
    data.add_field('caption_entities', [openapi_server.MessageEntity()])
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('disable_notification', True)
    data.add_field('duration', 56)
    data.add_field('parse_mode', 'parse_mode_example')
    data.add_field('reply_markup', openapi_server.CopyMessagePostRequestReplyMarkup())
    data.add_field('reply_to_message_id', 56)
    data.add_field('voice', 'voice_example')
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendVoice',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_chat_administrator_custom_title_post(client):
    """Test case for set_chat_administrator_custom_title_post

    
    """
    body = openapi_server.SetChatAdministratorCustomTitlePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setChatAdministratorCustomTitle',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_chat_description_post(client):
    """Test case for set_chat_description_post

    
    """
    body = openapi_server.SetChatDescriptionPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setChatDescription',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_chat_permissions_post(client):
    """Test case for set_chat_permissions_post

    
    """
    body = openapi_server.SetChatPermissionsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setChatPermissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_set_chat_photo_post(client):
    """Test case for set_chat_photo_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('chat_id', openapi_server.CopyMessagePostRequestChatId())
    data.add_field('photo', None)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setChatPhoto',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_chat_sticker_set_post(client):
    """Test case for set_chat_sticker_set_post

    
    """
    body = openapi_server.SetChatStickerSetPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setChatStickerSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_chat_title_post(client):
    """Test case for set_chat_title_post

    
    """
    body = openapi_server.SetChatTitlePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setChatTitle',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_game_score_post(client):
    """Test case for set_game_score_post

    
    """
    body = openapi_server.SetGameScorePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setGameScore',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_my_commands_post(client):
    """Test case for set_my_commands_post

    
    """
    body = openapi_server.SetMyCommandsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setMyCommands',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_passport_data_errors_post(client):
    """Test case for set_passport_data_errors_post

    
    """
    body = openapi_server.SetPassportDataErrorsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setPassportDataErrors',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_sticker_position_in_set_post(client):
    """Test case for set_sticker_position_in_set_post

    
    """
    body = openapi_server.SetStickerPositionInSetPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setStickerPositionInSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_set_sticker_set_thumb_post(client):
    """Test case for set_sticker_set_thumb_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('name', 'name_example')
    data.add_field('thumb', 'thumb_example')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setStickerSetThumb',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_set_webhook_post(client):
    """Test case for set_webhook_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allowed_updates', ['allowed_updates_example'])
    data.add_field('certificate', None)
    data.add_field('drop_pending_updates', True)
    data.add_field('ip_address', 'ip_address_example')
    data.add_field('max_connections', 40)
    data.add_field('url', 'url_example')
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setWebhook',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stop_message_live_location_post(client):
    """Test case for stop_message_live_location_post

    
    """
    body = openapi_server.StopMessageLiveLocationPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/stopMessageLiveLocation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stop_poll_post(client):
    """Test case for stop_poll_post

    
    """
    body = openapi_server.StopPollPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/stopPoll',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_unban_chat_member_post(client):
    """Test case for unban_chat_member_post

    
    """
    body = openapi_server.UnbanChatMemberPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/unbanChatMember',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_unpin_all_chat_messages_post(client):
    """Test case for unpin_all_chat_messages_post

    
    """
    body = openapi_server.DeleteChatPhotoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/unpinAllChatMessages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_unpin_chat_message_post(client):
    """Test case for unpin_chat_message_post

    
    """
    body = openapi_server.UnpinChatMessagePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/unpinChatMessage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_sticker_file_post(client):
    """Test case for upload_sticker_file_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('png_sticker', None)
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/uploadStickerFile',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

