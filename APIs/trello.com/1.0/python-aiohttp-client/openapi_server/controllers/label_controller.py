from typing import List, Dict
from aiohttp import web

from openapi_server.models.labels import Labels
from openapi_server.models.labels_color import LabelsColor
from openapi_server.models.labels_name import LabelsName
from openapi_server import util


async def add_labels(request: web.Request, key, token, body) -> web.Response:
    """addLabels()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Labels\&quot; to be added.
    :type body: dict | bytes

    """
    body = Labels.from_dict(body)
    return web.Response(status=200)


async def delete_labels_by_id_label(request: web.Request, id_label, key, token) -> web.Response:
    """deleteLabelsByIdLabel()

    

    :param id_label: idLabel
    :type id_label: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_labels_board_by_id_label(request: web.Request, id_label, key, token, fields=None) -> web.Response:
    """getLabelsBoardByIdLabel()

    

    :param id_label: idLabel
    :type id_label: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param fields: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    :type fields: str

    """
    return web.Response(status=200)


async def get_labels_board_by_id_label_by_field(request: web.Request, id_label, _field, key, token) -> web.Response:
    """getLabelsBoardByIdLabelByField()

    

    :param id_label: idLabel
    :type id_label: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_labels_by_id_label(request: web.Request, id_label, key, token, fields=None) -> web.Response:
    """getLabelsByIdLabel()

    

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


async def update_labels_by_id_label(request: web.Request, id_label, key, token, body) -> web.Response:
    """updateLabelsByIdLabel()

    

    :param id_label: idLabel
    :type id_label: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Labels\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Labels.from_dict(body)
    return web.Response(status=200)


async def update_labels_color_by_id_label(request: web.Request, id_label, key, token, body) -> web.Response:
    """updateLabelsColorByIdLabel()

    

    :param id_label: idLabel
    :type id_label: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Labels Color\&quot; to be updated.
    :type body: dict | bytes

    """
    body = LabelsColor.from_dict(body)
    return web.Response(status=200)


async def update_labels_name_by_id_label(request: web.Request, id_label, key, token, body) -> web.Response:
    """updateLabelsNameByIdLabel()

    

    :param id_label: idLabel
    :type id_label: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Labels Name\&quot; to be updated.
    :type body: dict | bytes

    """
    body = LabelsName.from_dict(body)
    return web.Response(status=200)
