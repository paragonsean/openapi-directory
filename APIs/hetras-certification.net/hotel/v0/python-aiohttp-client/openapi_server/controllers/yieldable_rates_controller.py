from typing import List, Dict
from aiohttp import web

from openapi_server.models.yieldable_rate_time_slice import YieldableRateTimeSlice
from openapi_server import util


async def yieldable_rates_save_prices(request: web.Request, app_id, app_key, hotel_id, rateplan_code, yieldable_rate_prices) -> web.Response:
    """Saves Yieldable Rate Prices for existing Yieldable Rateplan.

    Saves Yieldable Rate Prices for existing Yieldable Rateplan. The rateplan has been created before and with this End Point we               create or update the rate prices. If the Yieldable rateplan prices exist it updates them with the new price if not it creates new price entries.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: Specifies the hotelId which identifies Hotel for which the operation will be performed.
    :type hotel_id: int
    :param rateplan_code: Specifies the rateplanCode for which the operation will be performed.
    :type rateplan_code: str
    :param yieldable_rate_prices: Specifies the the Yieldable rateplan and prices details to be created or updated.
    :type yieldable_rate_prices: list | bytes

    """
    yieldable_rate_prices = [YieldableRateTimeSlice.from_dict(d) for d in yieldable_rate_prices]
    return web.Response(status=200)
