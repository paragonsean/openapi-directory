from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_installation200_response import DeleteInstallation200Response
from openapi_server import util


async def delete_installation(request: web.Request, ) -> web.Response:
    """アプリストアアプリのアンインストール

    このAPIは OAuth のアクセストークンに紐付くアプリケーションをショップから削除します。 このAPIを利用した場合、ショップオーナーがアンインストールした場合と異なり、アンインストールフックは実行されません。 代わりにアンインストールフックで通知される情報は、このAPIのレスポンスに含まれています。  アンインストール時の注意点については、[アプリのアンインストール](https://app.shop-pro.jp/open_api#section/API/アプリのインストール)を参照して下さい。 


    """
    return web.Response(status=200)
