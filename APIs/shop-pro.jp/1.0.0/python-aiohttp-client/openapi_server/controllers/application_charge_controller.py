from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_usage_charge201_response import CreateUsageCharge201Response
from openapi_server.models.create_usage_charge_request import CreateUsageChargeRequest
from openapi_server.models.post_application_charge201_response import PostApplicationCharge201Response
from openapi_server.models.post_application_charge_request import PostApplicationChargeRequest
from openapi_server import util


async def create_usage_charge(request: web.Request, recurring_application_charge_id, body, x_appstore_usage_charge_token=None) -> web.Response:
    """従量課金データの作成

    アプリ内で基本機能が利用された頻度に伴って毎月の請求が変動するようなアプリの場合は「従量課金」を使って利用者に変動分の請求を行うことができます。 ※無料お試し期間中のショップに対しては従量課金データを作成できません。 

    :param recurring_application_charge_id: 課金契約ID
    :type recurring_application_charge_id: str
    :param body: 従量課金データ
    :type body: dict | bytes
    :param x_appstore_usage_charge_token: アンインストール後の従量課金の精算をする際に、 &#x60;Authorization&#x60; ヘッダへアクセストークンを指定する代わりにこのヘッダを指定することで、このAPIを実行することができます。 インストール中は指定不要で、アンインストール後のみ必須となります。 アンインストールフックで通知される &#x60;usage_charge.api_token&#x60; の値を指定してください。 このヘッダは、アンインストールフックで通知される &#x60;usage_charge.closing_on&#x60; まで有効です。この期間を過ぎると従量課金を精算できなくなりますのでご注意ください。詳しくは [アプリのアンインストール](#section/API/アプリのアンインストール) をご確認ください。
    :type x_appstore_usage_charge_token: str

    """
    body = CreateUsageChargeRequest.from_dict(body)
    return web.Response(status=200)


async def post_application_charge(request: web.Request, body) -> web.Response:
    """アプリ内課金データの作成

    「アプリ内課金」はすでにインストール済みのアプリ上において、利用者が追加の買い切りによる課金によって新たなアプリ内の機能を提供される場合などに、利用者へ買い切りの課金分の請求を行うための課金形式です。  この課金はプラン課金の情報に紐付かないため、リクエストされたタイミングで課金データが作成されます。また、同一のアプリ内課金IDで同じ利用者へ複数回請求を行うことも可能です。  ただし、アプリの基本機能として提供しているサービスを利用した量やその頻度などに伴って毎月異なった額の請求を行うような課金については、プラン課金の「従量による課金」の機能を使って請求を行う必要があります。 

    :param body: 
    :type body: dict | bytes

    """
    body = PostApplicationChargeRequest.from_dict(body)
    return web.Response(status=200)
