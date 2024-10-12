from typing import List, Dict
from aiohttp import web

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
from openapi_server import util


async def add_sticker_to_set_post(request: web.Request, emojis, name, user_id, mask_position=None, png_sticker=None, tgs_sticker=None) -> web.Response:
    """add_sticker_to_set_post

    Use this method to add a new sticker to a set created by the bot. You **must** use exactly one of the fields *png\\_sticker* or *tgs\\_sticker*. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns *True* on success.

    :param emojis: One or more emoji corresponding to the sticker
    :type emojis: str
    :param name: Sticker set name
    :type name: str
    :param user_id: User identifier of sticker set owner
    :type user_id: int
    :param mask_position: 
    :type mask_position: dict | bytes
    :param png_sticker: 
    :type png_sticker: str
    :param tgs_sticker: This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
    :type tgs_sticker: dict | bytes

    """
    mask_position = MaskPosition.from_dict(mask_position)
    tgs_sticker = object.from_dict(tgs_sticker)
    return web.Response(status=200)


async def answer_callback_query_post(request: web.Request, body) -> web.Response:
    """answer_callback_query_post

    Use this method to send answers to callback queries sent from [inline keyboards](/bots#inline-keyboards-and-on-the-fly-updating). The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, *True* is returned.  Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via [@Botfather](https://t.me/botfather) and accept the terms. Otherwise, you may use links like &#x60;t.me/your_bot?start&#x3D;XXXX&#x60; that open your bot with a parameter.

    :param body: 
    :type body: dict | bytes

    """
    body = AnswerCallbackQueryPostRequest.from_dict(body)
    return web.Response(status=200)


async def answer_inline_query_post(request: web.Request, body) -> web.Response:
    """answer_inline_query_post

    Use this method to send answers to an inline query. On success, *True* is returned.   No more than **50** results per query are allowed.

    :param body: 
    :type body: dict | bytes

    """
    body = AnswerInlineQueryPostRequest.from_dict(body)
    return web.Response(status=200)


async def answer_pre_checkout_query_post(request: web.Request, body) -> web.Response:
    """answer_pre_checkout_query_post

    Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an [Update](https://core.telegram.org/bots/api/#update) with the field *pre\\_checkout\\_query*. Use this method to respond to such pre-checkout queries. On success, True is returned. **Note:** The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

    :param body: 
    :type body: dict | bytes

    """
    body = AnswerPreCheckoutQueryPostRequest.from_dict(body)
    return web.Response(status=200)


async def answer_shipping_query_post(request: web.Request, body) -> web.Response:
    """answer_shipping_query_post

    If you sent an invoice requesting a shipping address and the parameter *is\\_flexible* was specified, the Bot API will send an [Update](https://core.telegram.org/bots/api/#update) with a *shipping\\_query* field to the bot. Use this method to reply to shipping queries. On success, True is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = AnswerShippingQueryPostRequest.from_dict(body)
    return web.Response(status=200)


async def close_post(request: web.Request, ) -> web.Response:
    """close_post

    Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn&#39;t launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns *True* on success. Requires no parameters.


    """
    return web.Response(status=200)


async def copy_message_post(request: web.Request, body) -> web.Response:
    """copy_message_post

    Use this method to copy messages of any kind. The method is analogous to the method [forwardMessages](https://core.telegram.org/bots/api/#forwardmessages), but the copied message doesn&#39;t have a link to the original message. Returns the [MessageId](https://core.telegram.org/bots/api/#messageid) of the sent message on success.

    :param body: 
    :type body: dict | bytes

    """
    body = CopyMessagePostRequest.from_dict(body)
    return web.Response(status=200)


async def create_new_sticker_set_post(request: web.Request, emojis, name, title, user_id, contains_masks=None, mask_position=None, png_sticker=None, tgs_sticker=None) -> web.Response:
    """create_new_sticker_set_post

    Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You **must** use exactly one of the fields *png\\_sticker* or *tgs\\_sticker*. Returns *True* on success.

    :param emojis: One or more emoji corresponding to the sticker
    :type emojis: str
    :param name: Short name of sticker set, to be used in &#x60;t.me/addstickers/&#x60; URLs (e.g., *animals*). Can contain only english letters, digits and underscores. Must begin with a letter, can&#39;t contain consecutive underscores and must end in *“\\\\_by\\\\_&lt;bot username&gt;”*. *&lt;bot\\\\_username&gt;* is case insensitive. 1-64 characters.
    :type name: str
    :param title: Sticker set title, 1-64 characters
    :type title: str
    :param user_id: User identifier of created sticker set owner
    :type user_id: int
    :param contains_masks: Pass *True*, if a set of mask stickers should be created
    :type contains_masks: bool
    :param mask_position: 
    :type mask_position: dict | bytes
    :param png_sticker: 
    :type png_sticker: str
    :param tgs_sticker: This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
    :type tgs_sticker: dict | bytes

    """
    mask_position = MaskPosition.from_dict(mask_position)
    tgs_sticker = object.from_dict(tgs_sticker)
    return web.Response(status=200)


async def delete_chat_photo_post(request: web.Request, body) -> web.Response:
    """delete_chat_photo_post

    Use this method to delete a chat photo. Photos can&#39;t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteChatPhotoPostRequest.from_dict(body)
    return web.Response(status=200)


async def delete_chat_sticker_set_post(request: web.Request, body) -> web.Response:
    """delete_chat_sticker_set_post

    Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Use the field *can\\_set\\_sticker\\_set* optionally returned in [getChat](https://core.telegram.org/bots/api/#getchat) requests to check if the bot can use this method. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteChatStickerSetPostRequest.from_dict(body)
    return web.Response(status=200)


async def delete_message_post(request: web.Request, body) -> web.Response:
    """delete_message_post

    Use this method to delete a message, including service messages, with the following limitations:   \\- A message can only be deleted if it was sent less than 48 hours ago.   \\- A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.   \\- Bots can delete outgoing messages in private chats, groups, and supergroups.   \\- Bots can delete incoming messages in private chats.   \\- Bots granted *can\\_post\\_messages* permissions can delete outgoing messages in channels.   \\- If the bot is an administrator of a group, it can delete any message there.   \\- If the bot has *can\\_delete\\_messages* permission in a supergroup or a channel, it can delete any message there.   Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteMessagePostRequest.from_dict(body)
    return web.Response(status=200)


async def delete_sticker_from_set_post(request: web.Request, body) -> web.Response:
    """delete_sticker_from_set_post

    Use this method to delete a sticker from a set created by the bot. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteStickerFromSetPostRequest.from_dict(body)
    return web.Response(status=200)


async def delete_webhook_post(request: web.Request, body) -> web.Response:
    """delete_webhook_post

    Use this method to remove webhook integration if you decide to switch back to [getUpdates](https://core.telegram.org/bots/api/#getupdates). Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteWebhookPostRequest.from_dict(body)
    return web.Response(status=200)


async def edit_message_caption_post(request: web.Request, body) -> web.Response:
    """edit_message_caption_post

    Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = EditMessageCaptionPostRequest.from_dict(body)
    return web.Response(status=200)


async def edit_message_live_location_post(request: web.Request, body) -> web.Response:
    """edit_message_live_location_post

    Use this method to edit live location messages. A location can be edited until its *live\\_period* expires or editing is explicitly disabled by a call to [stopMessageLiveLocation](https://core.telegram.org/bots/api/#stopmessagelivelocation). On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = EditMessageLiveLocationPostRequest.from_dict(body)
    return web.Response(status=200)


async def edit_message_media_post(request: web.Request, media, chat_id=None, inline_message_id=None, message_id=None, reply_markup=None) -> web.Response:
    """edit_message_media_post

    Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can&#39;t be uploaded. Use a previously uploaded file via its file\\_id or specify a URL. On success, if the edited message was sent by the bot, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

    :param media: 
    :type media: dict | bytes
    :param chat_id: 
    :type chat_id: dict | bytes
    :param inline_message_id: Required if *chat\\\\_id* and *message\\\\_id* are not specified. Identifier of the inline message
    :type inline_message_id: str
    :param message_id: Required if *inline\\\\_message\\\\_id* is not specified. Identifier of the message to edit
    :type message_id: int
    :param reply_markup: 
    :type reply_markup: dict | bytes

    """
    media = InputMedia.from_dict(media)
    chat_id = EditMessageCaptionPostRequestChatId.from_dict(chat_id)
    reply_markup = InlineKeyboardMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def edit_message_reply_markup_post(request: web.Request, body) -> web.Response:
    """edit_message_reply_markup_post

    Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = EditMessageReplyMarkupPostRequest.from_dict(body)
    return web.Response(status=200)


async def edit_message_text_post(request: web.Request, body) -> web.Response:
    """edit_message_text_post

    Use this method to edit text and [game](https://core.telegram.org/bots/api/#games) messages. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = EditMessageTextPostRequest.from_dict(body)
    return web.Response(status=200)


async def export_chat_invite_link_post(request: web.Request, body) -> web.Response:
    """export_chat_invite_link_post

    Use this method to generate a new invite link for a chat; any previously generated link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns the new invite link as *String* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteChatPhotoPostRequest.from_dict(body)
    return web.Response(status=200)


async def forward_message_post(request: web.Request, body) -> web.Response:
    """forward_message_post

    Use this method to forward messages of any kind. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = ForwardMessagePostRequest.from_dict(body)
    return web.Response(status=200)


async def get_chat_administrators_post(request: web.Request, body) -> web.Response:
    """get_chat_administrators_post

    Use this method to get a list of administrators in a chat. On success, returns an Array of [ChatMember](https://core.telegram.org/bots/api/#chatmember) objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.

    :param body: 
    :type body: dict | bytes

    """
    body = GetChatPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_chat_member_post(request: web.Request, body) -> web.Response:
    """get_chat_member_post

    Use this method to get information about a member of a chat. Returns a [ChatMember](https://core.telegram.org/bots/api/#chatmember) object on success.

    :param body: 
    :type body: dict | bytes

    """
    body = GetChatMemberPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_chat_members_count_post(request: web.Request, body) -> web.Response:
    """get_chat_members_count_post

    Use this method to get the number of members in a chat. Returns *Int* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = GetChatPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_chat_post(request: web.Request, body) -> web.Response:
    """get_chat_post

    Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a [Chat](https://core.telegram.org/bots/api/#chat) object on success.

    :param body: 
    :type body: dict | bytes

    """
    body = GetChatPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_file_post(request: web.Request, body) -> web.Response:
    """get_file_post

    Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a [File](https://core.telegram.org/bots/api/#file) object is returned. The file can then be downloaded via the link &#x60;https://api.telegram.org/file/bot&lt;token&gt;/&lt;file_path&gt;&#x60;, where &#x60;&lt;file_path&gt;&#x60; is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling [getFile](https://core.telegram.org/bots/api/#getfile) again.

    :param body: 
    :type body: dict | bytes

    """
    body = GetFilePostRequest.from_dict(body)
    return web.Response(status=200)


async def get_game_high_scores_post(request: web.Request, body) -> web.Response:
    """get_game_high_scores_post

    Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an *Array* of [GameHighScore](https://core.telegram.org/bots/api/#gamehighscore) objects.  This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.

    :param body: 
    :type body: dict | bytes

    """
    body = GetGameHighScoresPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_me_post(request: web.Request, ) -> web.Response:
    """get_me_post

    A simple method for testing your bot&#39;s auth token. Requires no parameters. Returns basic information about the bot in form of a [User](https://core.telegram.org/bots/api/#user) object.


    """
    return web.Response(status=200)


async def get_my_commands_post(request: web.Request, ) -> web.Response:
    """get_my_commands_post

    Use this method to get the current list of the bot&#39;s commands. Requires no parameters. Returns Array of [BotCommand](https://core.telegram.org/bots/api/#botcommand) on success.


    """
    return web.Response(status=200)


async def get_sticker_set_post(request: web.Request, body) -> web.Response:
    """get_sticker_set_post

    Use this method to get a sticker set. On success, a [StickerSet](https://core.telegram.org/bots/api/#stickerset) object is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = GetStickerSetPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_updates_post(request: web.Request, body) -> web.Response:
    """get_updates_post

    Use this method to receive incoming updates using long polling ([wiki](https://en.wikipedia.org/wiki/Push_technology#Long_polling)). An Array of [Update](https://core.telegram.org/bots/api/#update) objects is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = GetUpdatesPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_user_profile_photos_post(request: web.Request, body) -> web.Response:
    """get_user_profile_photos_post

    Use this method to get a list of profile pictures for a user. Returns a [UserProfilePhotos](https://core.telegram.org/bots/api/#userprofilephotos) object.

    :param body: 
    :type body: dict | bytes

    """
    body = GetUserProfilePhotosPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_webhook_info_post(request: web.Request, ) -> web.Response:
    """get_webhook_info_post

    Use this method to get current webhook status. Requires no parameters. On success, returns a [WebhookInfo](https://core.telegram.org/bots/api/#webhookinfo) object. If the bot is using [getUpdates](https://core.telegram.org/bots/api/#getupdates), will return an object with the *url* field empty.


    """
    return web.Response(status=200)


async def kick_chat_member_post(request: web.Request, body) -> web.Response:
    """kick_chat_member_post

    Use this method to kick a user from a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless [unbanned](https://core.telegram.org/bots/api/#unbanchatmember) first. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = KickChatMemberPostRequest.from_dict(body)
    return web.Response(status=200)


async def leave_chat_post(request: web.Request, body) -> web.Response:
    """leave_chat_post

    Use this method for your bot to leave a group, supergroup or channel. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = GetChatPostRequest.from_dict(body)
    return web.Response(status=200)


async def log_out_post(request: web.Request, ) -> web.Response:
    """log_out_post

    Use this method to log out from the cloud Bot API server before launching the bot locally. You **must** log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns *True* on success. Requires no parameters.


    """
    return web.Response(status=200)


async def pin_chat_message_post(request: web.Request, body) -> web.Response:
    """pin_chat_message_post

    Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the &#39;can\\_pin\\_messages&#39; admin right in a supergroup or &#39;can\\_edit\\_messages&#39; admin right in a channel. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = PinChatMessagePostRequest.from_dict(body)
    return web.Response(status=200)


async def promote_chat_member_post(request: web.Request, body) -> web.Response:
    """promote_chat_member_post

    Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Pass *False* for all boolean parameters to demote a user. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = PromoteChatMemberPostRequest.from_dict(body)
    return web.Response(status=200)


async def restrict_chat_member_post(request: web.Request, body) -> web.Response:
    """restrict_chat_member_post

    Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate admin rights. Pass *True* for all permissions to lift restrictions from a user. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = RestrictChatMemberPostRequest.from_dict(body)
    return web.Response(status=200)


async def send_animation_post(request: web.Request, animation, chat_id, allow_sending_without_reply=None, caption=None, caption_entities=None, disable_notification=None, duration=None, height=None, parse_mode=None, reply_markup=None, reply_to_message_id=None, thumb=None, width=None) -> web.Response:
    """send_animation_post

    Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

    :param animation: 
    :type animation: str
    :param chat_id: 
    :type chat_id: dict | bytes
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param caption: Animation caption (may also be used when resending animation by *file\\\\_id*), 0-1024 characters after entities parsing
    :type caption: str
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse\\\\_mode*
    :type caption_entities: list | bytes
    :param disable_notification: Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param duration: Duration of sent animation in seconds
    :type duration: int
    :param height: Animation height
    :type height: int
    :param parse_mode: Mode for parsing entities in the animation caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    :type parse_mode: str
    :param reply_markup: 
    :type reply_markup: dict | bytes
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :type reply_to_message_id: int
    :param thumb: 
    :type thumb: str
    :param width: Animation width
    :type width: int

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    caption_entities = [MessageEntity.from_dict(d) for d in caption_entities]
    reply_markup = CopyMessagePostRequestReplyMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def send_audio_post(request: web.Request, audio, chat_id, allow_sending_without_reply=None, caption=None, caption_entities=None, disable_notification=None, duration=None, parse_mode=None, performer=None, reply_markup=None, reply_to_message_id=None, thumb=None, title=None) -> web.Response:
    """send_audio_post

    Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.  For sending voice messages, use the [sendVoice](https://core.telegram.org/bots/api/#sendvoice) method instead.

    :param audio: 
    :type audio: str
    :param chat_id: 
    :type chat_id: dict | bytes
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param caption: Audio caption, 0-1024 characters after entities parsing
    :type caption: str
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse\\\\_mode*
    :type caption_entities: list | bytes
    :param disable_notification: Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param duration: Duration of the audio in seconds
    :type duration: int
    :param parse_mode: Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    :type parse_mode: str
    :param performer: Performer
    :type performer: str
    :param reply_markup: 
    :type reply_markup: dict | bytes
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :type reply_to_message_id: int
    :param thumb: 
    :type thumb: str
    :param title: Track name
    :type title: str

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    caption_entities = [MessageEntity.from_dict(d) for d in caption_entities]
    reply_markup = CopyMessagePostRequestReplyMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def send_chat_action_post(request: web.Request, body) -> web.Response:
    """send_chat_action_post

    Use this method when you need to tell the user that something is happening on the bot&#39;s side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns *True* on success.  Example: The [ImageBot](https://t.me/imagebot) needs some time to process a request and upload the image. Instead of sending a text message along the lines of “Retrieving image, please wait…”, the bot may use [sendChatAction](https://core.telegram.org/bots/api/#sendchataction) with *action* &#x3D; *upload\\_photo*. The user will see a “sending photo” status for the bot.  We only recommend using this method when a response from the bot will take a **noticeable** amount of time to arrive.

    :param body: 
    :type body: dict | bytes

    """
    body = SendChatActionPostRequest.from_dict(body)
    return web.Response(status=200)


async def send_contact_post(request: web.Request, body) -> web.Response:
    """send_contact_post

    Use this method to send phone contacts. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = SendContactPostRequest.from_dict(body)
    return web.Response(status=200)


async def send_dice_post(request: web.Request, body) -> web.Response:
    """send_dice_post

    Use this method to send an animated emoji that will display a random value. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = SendDicePostRequest.from_dict(body)
    return web.Response(status=200)


async def send_document_post(request: web.Request, chat_id, document, allow_sending_without_reply=None, caption=None, caption_entities=None, disable_content_type_detection=None, disable_notification=None, parse_mode=None, reply_markup=None, reply_to_message_id=None, thumb=None) -> web.Response:
    """send_document_post

    Use this method to send general files. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

    :param chat_id: 
    :type chat_id: dict | bytes
    :param document: 
    :type document: str
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param caption: Document caption (may also be used when resending documents by *file\\\\_id*), 0-1024 characters after entities parsing
    :type caption: str
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse\\\\_mode*
    :type caption_entities: list | bytes
    :param disable_content_type_detection: Disables automatic server-side content type detection for files uploaded using multipart/form-data
    :type disable_content_type_detection: bool
    :param disable_notification: Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param parse_mode: Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    :type parse_mode: str
    :param reply_markup: 
    :type reply_markup: dict | bytes
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :type reply_to_message_id: int
    :param thumb: 
    :type thumb: str

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    caption_entities = [MessageEntity.from_dict(d) for d in caption_entities]
    reply_markup = CopyMessagePostRequestReplyMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def send_game_post(request: web.Request, body) -> web.Response:
    """send_game_post

    Use this method to send a game. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = SendGamePostRequest.from_dict(body)
    return web.Response(status=200)


async def send_invoice_post(request: web.Request, body) -> web.Response:
    """send_invoice_post

    Use this method to send invoices. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = SendInvoicePostRequest.from_dict(body)
    return web.Response(status=200)


async def send_location_post(request: web.Request, body) -> web.Response:
    """send_location_post

    Use this method to send point on the map. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = SendLocationPostRequest.from_dict(body)
    return web.Response(status=200)


async def send_media_group_post(request: web.Request, chat_id, media, allow_sending_without_reply=None, disable_notification=None, reply_to_message_id=None) -> web.Response:
    """send_media_group_post

    Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of [Messages](https://core.telegram.org/bots/api/#message) that were sent is returned.

    :param chat_id: 
    :type chat_id: dict | bytes
    :param media: A JSON-serialized array describing messages to be sent, must include 2-10 items
    :type media: list | bytes
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param disable_notification: Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param reply_to_message_id: If the messages are a reply, ID of the original message
    :type reply_to_message_id: int

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    media = [SendMediaGroupPostRequestMediaInner.from_dict(d) for d in media]
    return web.Response(status=200)


async def send_message_post(request: web.Request, body) -> web.Response:
    """send_message_post

    Use this method to send text messages. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = SendMessagePostRequest.from_dict(body)
    return web.Response(status=200)


async def send_photo_post(request: web.Request, chat_id, photo, allow_sending_without_reply=None, caption=None, caption_entities=None, disable_notification=None, parse_mode=None, reply_markup=None, reply_to_message_id=None) -> web.Response:
    """send_photo_post

    Use this method to send photos. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param chat_id: 
    :type chat_id: dict | bytes
    :param photo: 
    :type photo: str
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param caption: Photo caption (may also be used when resending photos by *file\\\\_id*), 0-1024 characters after entities parsing
    :type caption: str
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse\\\\_mode*
    :type caption_entities: list | bytes
    :param disable_notification: Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param parse_mode: Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    :type parse_mode: str
    :param reply_markup: 
    :type reply_markup: dict | bytes
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :type reply_to_message_id: int

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    caption_entities = [MessageEntity.from_dict(d) for d in caption_entities]
    reply_markup = CopyMessagePostRequestReplyMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def send_poll_post(request: web.Request, body) -> web.Response:
    """send_poll_post

    Use this method to send a native poll. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = SendPollPostRequest.from_dict(body)
    return web.Response(status=200)


async def send_sticker_post(request: web.Request, chat_id, sticker, allow_sending_without_reply=None, disable_notification=None, reply_markup=None, reply_to_message_id=None) -> web.Response:
    """send_sticker_post

    Use this method to send static .WEBP or [animated](https://telegram.org/blog/animated-stickers) .TGS stickers. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param chat_id: 
    :type chat_id: dict | bytes
    :param sticker: 
    :type sticker: str
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param disable_notification: Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param reply_markup: 
    :type reply_markup: dict | bytes
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :type reply_to_message_id: int

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    reply_markup = CopyMessagePostRequestReplyMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def send_venue_post(request: web.Request, body) -> web.Response:
    """send_venue_post

    Use this method to send information about a venue. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = SendVenuePostRequest.from_dict(body)
    return web.Response(status=200)


async def send_video_note_post(request: web.Request, chat_id, video_note, allow_sending_without_reply=None, disable_notification=None, duration=None, length=None, reply_markup=None, reply_to_message_id=None, thumb=None) -> web.Response:
    """send_video_note_post

    As of [v.4.0](https://telegram.org/blog/video-messages-and-telescope), Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

    :param chat_id: 
    :type chat_id: dict | bytes
    :param video_note: 
    :type video_note: str
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param disable_notification: Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param duration: Duration of sent video in seconds
    :type duration: int
    :param length: Video width and height, i.e. diameter of the video message
    :type length: int
    :param reply_markup: 
    :type reply_markup: dict | bytes
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :type reply_to_message_id: int
    :param thumb: 
    :type thumb: str

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    reply_markup = CopyMessagePostRequestReplyMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def send_video_post(request: web.Request, chat_id, video, allow_sending_without_reply=None, caption=None, caption_entities=None, disable_notification=None, duration=None, height=None, parse_mode=None, reply_markup=None, reply_to_message_id=None, supports_streaming=None, thumb=None, width=None) -> web.Response:
    """send_video_post

    Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as [Document](https://core.telegram.org/bots/api/#document)). On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

    :param chat_id: 
    :type chat_id: dict | bytes
    :param video: 
    :type video: str
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param caption: Video caption (may also be used when resending videos by *file\\\\_id*), 0-1024 characters after entities parsing
    :type caption: str
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse\\\\_mode*
    :type caption_entities: list | bytes
    :param disable_notification: Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param duration: Duration of sent video in seconds
    :type duration: int
    :param height: Video height
    :type height: int
    :param parse_mode: Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    :type parse_mode: str
    :param reply_markup: 
    :type reply_markup: dict | bytes
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :type reply_to_message_id: int
    :param supports_streaming: Pass *True*, if the uploaded video is suitable for streaming
    :type supports_streaming: bool
    :param thumb: 
    :type thumb: str
    :param width: Video width
    :type width: int

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    caption_entities = [MessageEntity.from_dict(d) for d in caption_entities]
    reply_markup = CopyMessagePostRequestReplyMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def send_voice_post(request: web.Request, chat_id, voice, allow_sending_without_reply=None, caption=None, caption_entities=None, disable_notification=None, duration=None, parse_mode=None, reply_markup=None, reply_to_message_id=None) -> web.Response:
    """send_voice_post

    Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as [Audio](https://core.telegram.org/bots/api/#audio) or [Document](https://core.telegram.org/bots/api/#document)). On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

    :param chat_id: 
    :type chat_id: dict | bytes
    :param voice: 
    :type voice: str
    :param allow_sending_without_reply: Pass *True*, if the message should be sent even if the specified replied-to message is not found
    :type allow_sending_without_reply: bool
    :param caption: Voice message caption, 0-1024 characters after entities parsing
    :type caption: str
    :param caption_entities: List of special entities that appear in the caption, which can be specified instead of *parse\\\\_mode*
    :type caption_entities: list | bytes
    :param disable_notification: Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    :type disable_notification: bool
    :param duration: Duration of the voice message in seconds
    :type duration: int
    :param parse_mode: Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    :type parse_mode: str
    :param reply_markup: 
    :type reply_markup: dict | bytes
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :type reply_to_message_id: int

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    caption_entities = [MessageEntity.from_dict(d) for d in caption_entities]
    reply_markup = CopyMessagePostRequestReplyMarkup.from_dict(reply_markup)
    return web.Response(status=200)


async def set_chat_administrator_custom_title_post(request: web.Request, body) -> web.Response:
    """set_chat_administrator_custom_title_post

    Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = SetChatAdministratorCustomTitlePostRequest.from_dict(body)
    return web.Response(status=200)


async def set_chat_description_post(request: web.Request, body) -> web.Response:
    """set_chat_description_post

    Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = SetChatDescriptionPostRequest.from_dict(body)
    return web.Response(status=200)


async def set_chat_permissions_post(request: web.Request, body) -> web.Response:
    """set_chat_permissions_post

    Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the *can\\_restrict\\_members* admin rights. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = SetChatPermissionsPostRequest.from_dict(body)
    return web.Response(status=200)


async def set_chat_photo_post(request: web.Request, chat_id, photo) -> web.Response:
    """set_chat_photo_post

    Use this method to set a new profile photo for the chat. Photos can&#39;t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns *True* on success.

    :param chat_id: 
    :type chat_id: dict | bytes
    :param photo: This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
    :type photo: dict | bytes

    """
    chat_id = CopyMessagePostRequestChatId.from_dict(chat_id)
    photo = object.from_dict(photo)
    return web.Response(status=200)


async def set_chat_sticker_set_post(request: web.Request, body) -> web.Response:
    """set_chat_sticker_set_post

    Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Use the field *can\\_set\\_sticker\\_set* optionally returned in [getChat](https://core.telegram.org/bots/api/#getchat) requests to check if the bot can use this method. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = SetChatStickerSetPostRequest.from_dict(body)
    return web.Response(status=200)


async def set_chat_title_post(request: web.Request, body) -> web.Response:
    """set_chat_title_post

    Use this method to change the title of a chat. Titles can&#39;t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = SetChatTitlePostRequest.from_dict(body)
    return web.Response(status=200)


async def set_game_score_post(request: web.Request, body) -> web.Response:
    """set_game_score_post

    Use this method to set the score of the specified user in a game. On success, if the message was sent by the bot, returns the edited [Message](https://core.telegram.org/bots/api/#message), otherwise returns *True*. Returns an error, if the new score is not greater than the user&#39;s current score in the chat and *force* is *False*.

    :param body: 
    :type body: dict | bytes

    """
    body = SetGameScorePostRequest.from_dict(body)
    return web.Response(status=200)


async def set_my_commands_post(request: web.Request, body) -> web.Response:
    """set_my_commands_post

    Use this method to change the list of the bot&#39;s commands. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = SetMyCommandsPostRequest.from_dict(body)
    return web.Response(status=200)


async def set_passport_data_errors_post(request: web.Request, body) -> web.Response:
    """set_passport_data_errors_post

    Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns *True* on success.  Use this if the data submitted by the user doesn&#39;t satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

    :param body: 
    :type body: dict | bytes

    """
    body = SetPassportDataErrorsPostRequest.from_dict(body)
    return web.Response(status=200)


async def set_sticker_position_in_set_post(request: web.Request, body) -> web.Response:
    """set_sticker_position_in_set_post

    Use this method to move a sticker in a set created by the bot to a specific position. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = SetStickerPositionInSetPostRequest.from_dict(body)
    return web.Response(status=200)


async def set_sticker_set_thumb_post(request: web.Request, name, user_id, thumb=None) -> web.Response:
    """set_sticker_set_thumb_post

    Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Returns *True* on success.

    :param name: Sticker set name
    :type name: str
    :param user_id: User identifier of the sticker set owner
    :type user_id: int
    :param thumb: 
    :type thumb: str

    """
    return web.Response(status=200)


async def set_webhook_post(request: web.Request, url, allowed_updates=None, certificate=None, drop_pending_updates=None, ip_address=None, max_connections=None) -> web.Response:
    """set_webhook_post

    Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized [Update](https://core.telegram.org/bots/api/#update). In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns *True* on success.  If you&#39;d like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. &#x60;https://www.example.com/&lt;token&gt;&#x60;. Since nobody else knows your bot&#39;s token, you can be pretty sure it&#39;s us.

    :param url: HTTPS url to send updates to. Use an empty string to remove webhook integration
    :type url: str
    :param allowed_updates: A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited\\\\_channel\\\\_post”, “callback\\\\_query”] to only receive updates of these types. See [Update](https://core.telegram.org/bots/api/#update) for a complete list of available update types. Specify an empty list to receive all updates regardless of type (default). If not specified, the previous setting will be used.   Please note that this parameter doesn&#39;t affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.
    :type allowed_updates: List[str]
    :param certificate: This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
    :type certificate: dict | bytes
    :param drop_pending_updates: Pass *True* to drop all pending updates
    :type drop_pending_updates: bool
    :param ip_address: The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS
    :type ip_address: str
    :param max_connections: Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to *40*. Use lower values to limit the load on your bot&#39;s server, and higher values to increase your bot&#39;s throughput.
    :type max_connections: int

    """
    certificate = object.from_dict(certificate)
    return web.Response(status=200)


async def stop_message_live_location_post(request: web.Request, body) -> web.Response:
    """stop_message_live_location_post

    Use this method to stop updating a live location message before *live\\_period* expires. On success, if the message was sent by the bot, the sent [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = StopMessageLiveLocationPostRequest.from_dict(body)
    return web.Response(status=200)


async def stop_poll_post(request: web.Request, body) -> web.Response:
    """stop_poll_post

    Use this method to stop a poll which was sent by the bot. On success, the stopped [Poll](https://core.telegram.org/bots/api/#poll) with the final results is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = StopPollPostRequest.from_dict(body)
    return web.Response(status=200)


async def unban_chat_member_post(request: web.Request, body) -> web.Response:
    """unban_chat_member_post

    Use this method to unban a previously kicked user in a supergroup or channel. The user will **not** return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be **removed** from the chat. If you don&#39;t want this, use the parameter *only\\_if\\_banned*. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = UnbanChatMemberPostRequest.from_dict(body)
    return web.Response(status=200)


async def unpin_all_chat_messages_post(request: web.Request, body) -> web.Response:
    """unpin_all_chat_messages_post

    Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the &#39;can\\_pin\\_messages&#39; admin right in a supergroup or &#39;can\\_edit\\_messages&#39; admin right in a channel. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteChatPhotoPostRequest.from_dict(body)
    return web.Response(status=200)


async def unpin_chat_message_post(request: web.Request, body) -> web.Response:
    """unpin_chat_message_post

    Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the &#39;can\\_pin\\_messages&#39; admin right in a supergroup or &#39;can\\_edit\\_messages&#39; admin right in a channel. Returns *True* on success.

    :param body: 
    :type body: dict | bytes

    """
    body = UnpinChatMessagePostRequest.from_dict(body)
    return web.Response(status=200)


async def upload_sticker_file_post(request: web.Request, png_sticker, user_id) -> web.Response:
    """upload_sticker_file_post

    Use this method to upload a .PNG file with a sticker for later use in *createNewStickerSet* and *addStickerToSet* methods (can be used multiple times). Returns the uploaded [File](https://core.telegram.org/bots/api/#file) on success.

    :param png_sticker: This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
    :type png_sticker: dict | bytes
    :param user_id: User identifier of sticker file owner
    :type user_id: int

    """
    png_sticker = object.from_dict(png_sticker)
    return web.Response(status=200)
