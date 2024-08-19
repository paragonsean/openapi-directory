from typing import List, Dict
from aiohttp import web

from openapi_server.models.tokens_webhooks import TokensWebhooks
from openapi_server import util


async def add_tokens_webhooks_by_token(request: web.Request, token, key, token2, body) -> web.Response:
    """addTokensWebhooksByToken()

    

    :param token: token
    :type token: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str
    :param body: Attributes of \&quot;Tokens Webhooks\&quot; to be added.
    :type body: dict | bytes

    """
    body = TokensWebhooks.from_dict(body)
    return web.Response(status=200)


async def delete_tokens_by_token(request: web.Request, token, key, token2) -> web.Response:
    """deleteTokensByToken()

    

    :param token: token
    :type token: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str

    """
    return web.Response(status=200)


async def delete_tokens_webhooks_by_token_by_id_webhook(request: web.Request, token, id_webhook, key, token2) -> web.Response:
    """deleteTokensWebhooksByTokenByIdWebhook()

    

    :param token: token
    :type token: str
    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str

    """
    return web.Response(status=200)


async def get_tokens_by_token(request: web.Request, token, key, token2, fields=None, webhooks=None) -> web.Response:
    """getTokensByToken()

    

    :param token: token
    :type token: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str
    :param fields: all or a comma-separated list of: dateCreated, dateExpires, idMember, identifier or permissions
    :type fields: str
    :param webhooks:  true or false
    :type webhooks: str

    """
    return web.Response(status=200)


async def get_tokens_by_token_by_field(request: web.Request, token, _field, key, token2) -> web.Response:
    """getTokensByTokenByField()

    

    :param token: token
    :type token: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str

    """
    return web.Response(status=200)


async def get_tokens_member_by_token(request: web.Request, token, key, token2, fields=None) -> web.Response:
    """getTokensMemberByToken()

    

    :param token: token
    :type token: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str
    :param fields: all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
    :type fields: str

    """
    return web.Response(status=200)


async def get_tokens_member_by_token_by_field(request: web.Request, token, _field, key, token2) -> web.Response:
    """getTokensMemberByTokenByField()

    

    :param token: token
    :type token: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str

    """
    return web.Response(status=200)


async def get_tokens_webhooks_by_token(request: web.Request, token, key, token2) -> web.Response:
    """getTokensWebhooksByToken()

    

    :param token: token
    :type token: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str

    """
    return web.Response(status=200)


async def get_tokens_webhooks_by_token_by_id_webhook(request: web.Request, token, id_webhook, key, token2) -> web.Response:
    """getTokensWebhooksByTokenByIdWebhook()

    

    :param token: token
    :type token: str
    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str

    """
    return web.Response(status=200)


async def update_tokens_webhooks_by_token(request: web.Request, token, key, token2, body) -> web.Response:
    """updateTokensWebhooksByToken()

    

    :param token: token
    :type token: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token2: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token2: str
    :param body: Attributes of \&quot;Tokens Webhooks\&quot; to be updated.
    :type body: dict | bytes

    """
    body = TokensWebhooks.from_dict(body)
    return web.Response(status=200)
