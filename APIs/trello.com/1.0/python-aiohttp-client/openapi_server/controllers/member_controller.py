from typing import List, Dict
from aiohttp import web

from openapi_server.models.members import Members
from openapi_server.models.members_avatar import MembersAvatar
from openapi_server.models.members_avatar_source import MembersAvatarSource
from openapi_server.models.members_bio import MembersBio
from openapi_server.models.members_board_backgrounds import MembersBoardBackgrounds
from openapi_server.models.members_board_stars import MembersBoardStars
from openapi_server.models.members_board_stars_id_board import MembersBoardStarsIdBoard
from openapi_server.models.members_board_stars_pos import MembersBoardStarsPos
from openapi_server.models.members_custom_board_backgrounds import MembersCustomBoardBackgrounds
from openapi_server.models.members_custom_emoji import MembersCustomEmoji
from openapi_server.models.members_custom_stickers import MembersCustomStickers
from openapi_server.models.members_full_name import MembersFullName
from openapi_server.models.members_initials import MembersInitials
from openapi_server.models.members_one_time_messages_dismissed import MembersOneTimeMessagesDismissed
from openapi_server.models.members_saved_searches import MembersSavedSearches
from openapi_server.models.members_saved_searches_name import MembersSavedSearchesName
from openapi_server.models.members_saved_searches_pos import MembersSavedSearchesPos
from openapi_server.models.members_saved_searches_query import MembersSavedSearchesQuery
from openapi_server.models.members_username import MembersUsername
from openapi_server.models.prefs_color_blind import PrefsColorBlind
from openapi_server.models.prefs_locale import PrefsLocale
from openapi_server.models.prefs_minutes_between_summaries import PrefsMinutesBetweenSummaries
from openapi_server import util


async def add_members_avatar_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """addMembersAvatarByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Avatar\&quot; to be added.
    :type body: dict | bytes

    """
    body = MembersAvatar.from_dict(body)
    return web.Response(status=200)


async def add_members_board_backgrounds_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """addMembersBoardBackgroundsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Board Backgrounds\&quot; to be added.
    :type body: dict | bytes

    """
    body = MembersBoardBackgrounds.from_dict(body)
    return web.Response(status=200)


async def add_members_board_stars_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """addMembersBoardStarsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Board Stars\&quot; to be added.
    :type body: dict | bytes

    """
    body = MembersBoardStars.from_dict(body)
    return web.Response(status=200)


async def add_members_custom_board_backgrounds_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """addMembersCustomBoardBackgroundsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Custom Board Backgrounds\&quot; to be added.
    :type body: dict | bytes

    """
    body = MembersCustomBoardBackgrounds.from_dict(body)
    return web.Response(status=200)


async def add_members_custom_emoji_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """addMembersCustomEmojiByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Custom Emoji\&quot; to be added.
    :type body: dict | bytes

    """
    body = MembersCustomEmoji.from_dict(body)
    return web.Response(status=200)


async def add_members_custom_stickers_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """addMembersCustomStickersByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Custom Stickers\&quot; to be added.
    :type body: dict | bytes

    """
    body = MembersCustomStickers.from_dict(body)
    return web.Response(status=200)


async def add_members_one_time_messages_dismissed_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """addMembersOneTimeMessagesDismissedByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members One Time Messages Dismissed\&quot; to be added.
    :type body: dict | bytes

    """
    body = MembersOneTimeMessagesDismissed.from_dict(body)
    return web.Response(status=200)


async def add_members_saved_searches_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """addMembersSavedSearchesByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Saved Searches\&quot; to be added.
    :type body: dict | bytes

    """
    body = MembersSavedSearches.from_dict(body)
    return web.Response(status=200)


async def delete_members_board_backgrounds_by_id_member_by_id_board_background(request: web.Request, id_member, id_board_background, key, token) -> web.Response:
    """deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_background: idBoardBackground
    :type id_board_background: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_members_board_stars_by_id_member_by_id_board_star(request: web.Request, id_member, id_board_star, key, token) -> web.Response:
    """deleteMembersBoardStarsByIdMemberByIdBoardStar()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_star: idBoardStar
    :type id_board_star: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_members_custom_board_backgrounds_by_id_member_by_id_board_background(request: web.Request, id_member, id_board_background, key, token) -> web.Response:
    """deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_background: idBoardBackground
    :type id_board_background: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_members_custom_stickers_by_id_member_by_id_custom_sticker(request: web.Request, id_member, id_custom_sticker, key, token) -> web.Response:
    """deleteMembersCustomStickersByIdMemberByIdCustomSticker()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_custom_sticker: idCustomSticker
    :type id_custom_sticker: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def delete_members_saved_searches_by_id_member_by_id_saved_search(request: web.Request, id_member, id_saved_search, key, token) -> web.Response:
    """deleteMembersSavedSearchesByIdMemberByIdSavedSearch()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_saved_search: idSavedSearch
    :type id_saved_search: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_actions_by_id_member(request: web.Request, id_member, key, token, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, id_models=None, member=None, member_fields=None, member_creator=None, member_creator_fields=None) -> web.Response:
    """getMembersActionsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
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


async def get_members_board_backgrounds_by_id_member(request: web.Request, id_member, key, token, filter=None) -> web.Response:
    """getMembersBoardBackgroundsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: all, custom, default, none or premium
    :type filter: str

    """
    return web.Response(status=200)


async def get_members_board_backgrounds_by_id_member_by_id_board_background(request: web.Request, id_member, id_board_background, key, token, fields=None) -> web.Response:
    """getMembersBoardBackgroundsByIdMemberByIdBoardBackground()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_background: idBoardBackground
    :type id_board_background: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: brightness, fullSizeUrl, scaled or tile
    :type fields: str

    """
    return web.Response(status=200)


async def get_members_board_stars_by_id_member(request: web.Request, id_member, key, token) -> web.Response:
    """getMembersBoardStarsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_board_stars_by_id_member_by_id_board_star(request: web.Request, id_member, id_board_star, key, token) -> web.Response:
    """getMembersBoardStarsByIdMemberByIdBoardStar()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_star: idBoardStar
    :type id_board_star: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_boards_by_id_member(request: web.Request, id_member, key, token, filter=None, fields=None, actions=None, actions_entities=None, actions_limit=None, actions_format=None, actions_since=None, action_fields=None, memberships=None, organization=None, organization_fields=None, lists=None) -> web.Response:
    """getMembersBoardsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
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


async def get_members_boards_by_id_member_by_filter(request: web.Request, id_member, filter, key, token) -> web.Response:
    """getMembersBoardsByIdMemberByFilter()

    

    :param id_member: idMember or username
    :type id_member: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_boards_invited_by_id_member(request: web.Request, id_member, key, token, fields=None) -> web.Response:
    """getMembersBoardsInvitedByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_members_boards_invited_by_id_member_by_field(request: web.Request, id_member, _field, key, token) -> web.Response:
    """getMembersBoardsInvitedByIdMemberByField()

    

    :param id_member: idMember or username
    :type id_member: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_by_id_member(request: web.Request, id_member, key, token, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, action_since=None, action_before=None, cards=None, card_fields=None, card_members=None, card_member_fields=None, card_attachments=None, card_attachment_fields=None, card_stickers=None, boards=None, board_fields=None, board_actions=None, board_actions_entities=None, board_actions_display=None, board_actions_format=None, board_actions_since=None, board_actions_limit=None, board_action_fields=None, board_lists=None, board_memberships=None, board_organization=None, board_organization_fields=None, boards_invited=None, boards_invited_fields=None, board_stars=None, saved_searches=None, organizations=None, organization_fields=None, organization_paid_account=None, organizations_invited=None, organizations_invited_fields=None, notifications=None, notifications_entities=None, notifications_display=None, notifications_limit=None, notification_fields=None, notification_member_creator=None, notification_member_creator_fields=None, notification_before=None, notification_since=None, tokens=None, paid_account=None, board_backgrounds=None, custom_board_backgrounds=None, custom_stickers=None, custom_emoji=None, fields=None) -> web.Response:
    """getMembersByIdMember()

    If you specify &#39;me&#39; as the username, this call will respond as if you had supplied the username associated with the supplied token

    :param id_member: idMember or username
    :type id_member: str
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
    :param action_since: A date, null or lastView
    :type action_since: str
    :param action_before: A date, or null
    :type action_before: str
    :param cards: One of: all, closed, none, open or visible
    :type cards: str
    :param card_fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type card_fields: str
    :param card_members:  true or false
    :type card_members: str
    :param card_member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type card_member_fields: str
    :param card_attachments: A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments
    :type card_attachments: str
    :param card_attachment_fields: all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    :type card_attachment_fields: str
    :param card_stickers:  true or false
    :type card_stickers: str
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
    :param board_memberships: all or a comma-separated list of: active, admin, deactivated, me or normal
    :type board_memberships: str
    :param board_organization:  true or false
    :type board_organization: str
    :param board_organization_fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type board_organization_fields: str
    :param boards_invited: all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned
    :type boards_invited: str
    :param boards_invited_fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type boards_invited_fields: str
    :param board_stars:  true or false
    :type board_stars: str
    :param saved_searches:  true or false
    :type saved_searches: str
    :param organizations: One of: all, members, none or public
    :type organizations: str
    :param organization_fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type organization_fields: str
    :param organization_paid_account:  true or false
    :type organization_paid_account: str
    :param organizations_invited: One of: all, members, none or public
    :type organizations_invited: str
    :param organizations_invited_fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type organizations_invited_fields: str
    :param notifications: all or a comma-separated list of: addAdminToBoard, addAdminToOrganization, addedAttachmentToCard, addedMemberToCard, addedToBoard, addedToCard, addedToOrganization, cardDueSoon, changeCard, closeBoard, commentCard, createdCard, declinedInvitationToBoard, declinedInvitationToOrganization, invitedToBoard, invitedToOrganization, makeAdminOfBoard, makeAdminOfOrganization, memberJoinedTrello, mentionedOnCard, removedFromBoard, removedFromCard, removedFromOrganization, removedMemberFromCard, unconfirmedInvitedToBoard, unconfirmedInvitedToOrganization or updateCheckItemStateOnCard
    :type notifications: str
    :param notifications_entities:  true or false
    :type notifications_entities: str
    :param notifications_display:  true or false
    :type notifications_display: str
    :param notifications_limit: a number from 1 to 1000
    :type notifications_limit: str
    :param notification_fields: all or a comma-separated list of: data, date, idMemberCreator, type or unread
    :type notification_fields: str
    :param notification_member_creator:  true or false
    :type notification_member_creator: str
    :param notification_member_creator_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type notification_member_creator_fields: str
    :param notification_before: An id, or null
    :type notification_before: str
    :param notification_since: An id, or null
    :type notification_since: str
    :param tokens: One of: all or none
    :type tokens: str
    :param paid_account:  true or false
    :type paid_account: str
    :param board_backgrounds: One of: all, custom, default, none or premium
    :type board_backgrounds: str
    :param custom_board_backgrounds: One of: all or none
    :type custom_board_backgrounds: str
    :param custom_stickers: One of: all or none
    :type custom_stickers: str
    :param custom_emoji: One of: all or none
    :type custom_emoji: str
    :param fields: all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
    :type fields: str

    """
    return web.Response(status=200)


async def get_members_by_id_member_by_field(request: web.Request, id_member, _field, key, token) -> web.Response:
    """getMembersByIdMemberByField()

    

    :param id_member: idMember or username
    :type id_member: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_cards_by_id_member(request: web.Request, id_member, key, token, actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, check_item_states=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None) -> web.Response:
    """getMembersCardsByIdMember()

    

    :param id_member: idMember or username
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


async def get_members_cards_by_id_member_by_filter(request: web.Request, id_member, filter, key, token) -> web.Response:
    """getMembersCardsByIdMemberByFilter()

    

    :param id_member: idMember or username
    :type id_member: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_custom_board_backgrounds_by_id_member(request: web.Request, id_member, key, token, filter=None) -> web.Response:
    """getMembersCustomBoardBackgroundsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: all or none
    :type filter: str

    """
    return web.Response(status=200)


async def get_members_custom_board_backgrounds_by_id_member_by_id_board_background(request: web.Request, id_member, id_board_background, key, token, fields=None) -> web.Response:
    """getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_background: idBoardBackground
    :type id_board_background: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: brightness, fullSizeUrl, scaled or tile
    :type fields: str

    """
    return web.Response(status=200)


async def get_members_custom_emoji_by_id_member(request: web.Request, id_member, key, token, filter=None) -> web.Response:
    """getMembersCustomEmojiByIdMember()

    This gets the list of all of the user’s uploaded emoji

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: all or none
    :type filter: str

    """
    return web.Response(status=200)


async def get_members_custom_emoji_by_id_member_by_id_custom_emoji(request: web.Request, id_member, id_custom_emoji, key, token, fields=None) -> web.Response:
    """getMembersCustomEmojiByIdMemberByIdCustomEmoji()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_custom_emoji: idCustomEmoji
    :type id_custom_emoji: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: name or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_members_custom_stickers_by_id_member(request: web.Request, id_member, key, token, filter=None) -> web.Response:
    """getMembersCustomStickersByIdMember()

    This gets a list of all of the user’s uploaded stickers

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: all or none
    :type filter: str

    """
    return web.Response(status=200)


async def get_members_custom_stickers_by_id_member_by_id_custom_sticker(request: web.Request, id_member, id_custom_sticker, key, token, fields=None) -> web.Response:
    """getMembersCustomStickersByIdMemberByIdCustomSticker()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_custom_sticker: idCustomSticker
    :type id_custom_sticker: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: scaled or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_members_deltas_by_id_member(request: web.Request, id_member, tags, ix_last_update, key, token) -> web.Response:
    """getMembersDeltasByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
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


async def get_members_notifications_by_id_member(request: web.Request, id_member, key, token, entities=None, display=None, filter=None, read_filter=None, fields=None, limit=None, page=None, before=None, since=None, member_creator=None, member_creator_fields=None) -> web.Response:
    """getMembersNotificationsByIdMember()

    You can only read the notifications for the member associated with the supplied token

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param entities:  true or false
    :type entities: str
    :param display:  true or false
    :type display: str
    :param filter: all or a comma-separated list of: addAdminToBoard, addAdminToOrganization, addedAttachmentToCard, addedMemberToCard, addedToBoard, addedToCard, addedToOrganization, cardDueSoon, changeCard, closeBoard, commentCard, createdCard, declinedInvitationToBoard, declinedInvitationToOrganization, invitedToBoard, invitedToOrganization, makeAdminOfBoard, makeAdminOfOrganization, memberJoinedTrello, mentionedOnCard, removedFromBoard, removedFromCard, removedFromOrganization, removedMemberFromCard, unconfirmedInvitedToBoard, unconfirmedInvitedToOrganization or updateCheckItemStateOnCard
    :type filter: str
    :param read_filter: One of: all, read or unread
    :type read_filter: str
    :param fields: all or a comma-separated list of: data, date, idMemberCreator, type or unread
    :type fields: str
    :param limit: a number from 1 to 1000
    :type limit: str
    :param page: a number from 0 to 100
    :type page: str
    :param before: An id, or null
    :type before: str
    :param since: An id, or null
    :type since: str
    :param member_creator:  true or false
    :type member_creator: str
    :param member_creator_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_creator_fields: str

    """
    return web.Response(status=200)


async def get_members_notifications_by_id_member_by_filter(request: web.Request, id_member, filter, key, token) -> web.Response:
    """getMembersNotificationsByIdMemberByFilter()

    

    :param id_member: idMember or username
    :type id_member: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_organizations_by_id_member(request: web.Request, id_member, key, token, filter=None, fields=None, paid_account=None) -> web.Response:
    """getMembersOrganizationsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: all, members, none or public
    :type filter: str
    :param fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type fields: str
    :param paid_account:  true or false
    :type paid_account: str

    """
    return web.Response(status=200)


async def get_members_organizations_by_id_member_by_filter(request: web.Request, id_member, filter, key, token) -> web.Response:
    """getMembersOrganizationsByIdMemberByFilter()

    

    :param id_member: idMember or username
    :type id_member: str
    :param filter: filter
    :type filter: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_organizations_invited_by_id_member(request: web.Request, id_member, key, token, fields=None) -> web.Response:
    """getMembersOrganizationsInvitedByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type fields: str

    """
    return web.Response(status=200)


async def get_members_organizations_invited_by_id_member_by_field(request: web.Request, id_member, _field, key, token) -> web.Response:
    """getMembersOrganizationsInvitedByIdMemberByField()

    

    :param id_member: idMember or username
    :type id_member: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_saved_searches_by_id_member(request: web.Request, id_member, key, token) -> web.Response:
    """getMembersSavedSearchesByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_saved_searches_by_id_member_by_id_saved_search(request: web.Request, id_member, id_saved_search, key, token) -> web.Response:
    """getMembersSavedSearchesByIdMemberByIdSavedSearch()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_saved_search: idSavedSearch
    :type id_saved_search: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_members_tokens_by_id_member(request: web.Request, id_member, key, token, filter=None) -> web.Response:
    """getMembersTokensByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param filter: One of: all or none
    :type filter: str

    """
    return web.Response(status=200)


async def update_members_avatar_source_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersAvatarSourceByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Avatar Source\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersAvatarSource.from_dict(body)
    return web.Response(status=200)


async def update_members_bio_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersBioByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Bio\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersBio.from_dict(body)
    return web.Response(status=200)


async def update_members_board_backgrounds_by_id_member_by_id_board_background(request: web.Request, id_member, id_board_background, key, token, body) -> web.Response:
    """updateMembersBoardBackgroundsByIdMemberByIdBoardBackground()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_background: idBoardBackground
    :type id_board_background: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Board Backgrounds\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersBoardBackgrounds.from_dict(body)
    return web.Response(status=200)


async def update_members_board_stars_by_id_member_by_id_board_star(request: web.Request, id_member, id_board_star, key, token, body) -> web.Response:
    """updateMembersBoardStarsByIdMemberByIdBoardStar()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_star: idBoardStar
    :type id_board_star: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Board Stars\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersBoardStars.from_dict(body)
    return web.Response(status=200)


async def update_members_board_stars_id_board_by_id_member_by_id_board_star(request: web.Request, id_member, id_board_star, key, token, body) -> web.Response:
    """updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_star: idBoardStar
    :type id_board_star: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Board Stars Id Board\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersBoardStarsIdBoard.from_dict(body)
    return web.Response(status=200)


async def update_members_board_stars_pos_by_id_member_by_id_board_star(request: web.Request, id_member, id_board_star, key, token, body) -> web.Response:
    """updateMembersBoardStarsPosByIdMemberByIdBoardStar()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_star: idBoardStar
    :type id_board_star: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Board Stars Pos\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersBoardStarsPos.from_dict(body)
    return web.Response(status=200)


async def update_members_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Members.from_dict(body)
    return web.Response(status=200)


async def update_members_custom_board_backgrounds_by_id_member_by_id_board_background(request: web.Request, id_member, id_board_background, key, token, body) -> web.Response:
    """updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_board_background: idBoardBackground
    :type id_board_background: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Custom Board Backgrounds\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersCustomBoardBackgrounds.from_dict(body)
    return web.Response(status=200)


async def update_members_full_name_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersFullNameByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Full Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersFullName.from_dict(body)
    return web.Response(status=200)


async def update_members_initials_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersInitialsByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Initials\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersInitials.from_dict(body)
    return web.Response(status=200)


async def update_members_prefs_color_blind_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersPrefsColorBlindByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Color Blind\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsColorBlind.from_dict(body)
    return web.Response(status=200)


async def update_members_prefs_locale_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersPrefsLocaleByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Locale\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsLocale.from_dict(body)
    return web.Response(status=200)


async def update_members_prefs_minutes_between_summaries_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersPrefsMinutesBetweenSummariesByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Prefs Minutes Between Summaries\&quot; to be updated.
    :type body: dict | bytes

    """
    body = PrefsMinutesBetweenSummaries.from_dict(body)
    return web.Response(status=200)


async def update_members_saved_searches_by_id_member_by_id_saved_search(request: web.Request, id_member, id_saved_search, key, token, body) -> web.Response:
    """updateMembersSavedSearchesByIdMemberByIdSavedSearch()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_saved_search: idSavedSearch
    :type id_saved_search: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Saved Searches\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersSavedSearches.from_dict(body)
    return web.Response(status=200)


async def update_members_saved_searches_name_by_id_member_by_id_saved_search(request: web.Request, id_member, id_saved_search, key, token, body) -> web.Response:
    """updateMembersSavedSearchesNameByIdMemberByIdSavedSearch()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_saved_search: idSavedSearch
    :type id_saved_search: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Saved Searches Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersSavedSearchesName.from_dict(body)
    return web.Response(status=200)


async def update_members_saved_searches_pos_by_id_member_by_id_saved_search(request: web.Request, id_member, id_saved_search, key, token, body) -> web.Response:
    """updateMembersSavedSearchesPosByIdMemberByIdSavedSearch()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_saved_search: idSavedSearch
    :type id_saved_search: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Saved Searches Pos\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersSavedSearchesPos.from_dict(body)
    return web.Response(status=200)


async def update_members_saved_searches_query_by_id_member_by_id_saved_search(request: web.Request, id_member, id_saved_search, key, token, body) -> web.Response:
    """updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch()

    

    :param id_member: idMember or username
    :type id_member: str
    :param id_saved_search: idSavedSearch
    :type id_saved_search: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Saved Searches Query\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersSavedSearchesQuery.from_dict(body)
    return web.Response(status=200)


async def update_members_username_by_id_member(request: web.Request, id_member, key, token, body) -> web.Response:
    """updateMembersUsernameByIdMember()

    

    :param id_member: idMember or username
    :type id_member: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Members Username\&quot; to be updated.
    :type body: dict | bytes

    """
    body = MembersUsername.from_dict(body)
    return web.Response(status=200)
