from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_search(request: web.Request, query, id_organizations, key, token, id_boards=None, id_cards=None, model_types=None, board_fields=None, boards_limit=None, card_fields=None, cards_limit=None, cards_page=None, card_board=None, card_list=None, card_members=None, card_stickers=None, card_attachments=None, organization_fields=None, organizations_limit=None, member_fields=None, members_limit=None, partial=None) -> web.Response:
    """getSearch()

    

    :param query: a string with a length from 1 to 16384
    :type query: str
    :param id_organizations: A comma-separated list of objectIds, 24-character hex strings
    :type id_organizations: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param id_boards: A comma-separated list of objectIds, 24-character hex strings
    :type id_boards: str
    :param id_cards: A comma-separated list of objectIds, 24-character hex strings
    :type id_cards: str
    :param model_types: all or a comma-separated list of: actions, boards, cards, members or organizations
    :type model_types: str
    :param board_fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type board_fields: str
    :param boards_limit: a number from 1 to 1000
    :type boards_limit: str
    :param card_fields: all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    :type card_fields: str
    :param cards_limit: a number from 1 to 1000
    :type cards_limit: str
    :param cards_page: a number from 0 to 100
    :type cards_page: str
    :param card_board:  true or false
    :type card_board: str
    :param card_list:  true or false
    :type card_list: str
    :param card_members:  true or false
    :type card_members: str
    :param card_stickers:  true or false
    :type card_stickers: str
    :param card_attachments: A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments
    :type card_attachments: str
    :param organization_fields: all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    :type organization_fields: str
    :param organizations_limit: a number from 1 to 1000
    :type organizations_limit: str
    :param member_fields: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    :type member_fields: str
    :param members_limit: a number from 1 to 1000
    :type members_limit: str
    :param partial:  true or false
    :type partial: str

    """
    return web.Response(status=200)


async def get_search_members(request: web.Request, query, key, token, limit=None, id_board=None, id_organization=None, only_org_members=None) -> web.Response:
    """getSearchMembers()

    

    :param query: a string with a length from 1 to 16384
    :type query: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param limit: a number from 1 to 20
    :type limit: str
    :param id_board: An id, or null
    :type id_board: str
    :param id_organization: An id, or null
    :type id_organization: str
    :param only_org_members: A boolean
    :type only_org_members: str

    """
    return web.Response(status=200)
