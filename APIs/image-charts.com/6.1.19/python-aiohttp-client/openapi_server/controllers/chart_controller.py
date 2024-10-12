from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_chart(request: web.Request, cht, chl, chd=None, chds=None, choe=None, chld=None, chxr=None, chxp=None, chof=None, chs=None, chdl=None, chdls=None, chg=None, chco=None, chtt=None, chts=None, chxt=None, chxl=None, chxs=None, chm=None, chls=None, chlps=None, chma=None, chdlp=None, chf=None, chbh=None, chbr=None, chan=None, chli=None, icac=None, ichm=None, icff=None, icfs=None, iclocale=None, icwt=None, icretina=None, icqrb=None, icqrf=None) -> web.Response:
    """Image-Charts API

    Image-charts

    :param cht: Chart type
    :type cht: str
    :param chl: bar, pie slice, doughnut slice and polar slice chart labels
    :type chl: str
    :param chd: chart data
    :type chd: str
    :param chds: data format with custom scaling
    :type chds: str
    :param choe: QRCode data encoding
    :type choe: str
    :param chld: QRCode error correction level and optional margin
    :type chld: str
    :param chxr: Axis data-range
    :type chxr: str
    :param chxp: axis label positions
    :type chxp: str
    :param chof: Image output format
    :type chof: str
    :param chs: Chart size (&lt;width&gt;x&lt;height&gt;)
    :type chs: str
    :param chdl: Text for each series, to display in the legend
    :type chdl: str
    :param chdls: Chart legend text and style
    :type chdls: str
    :param chg: Solid or dotted grid lines
    :type chg: str
    :param chco: series colors
    :type chco: str
    :param chtt: chart title
    :type chtt: str
    :param chts: chart title colors and font size
    :type chts: str
    :param chxt: Display values on your axis lines or change which axes are shown
    :type chxt: str
    :param chxl: Custom string axis labels on any axis
    :type chxl: str
    :param chxs: Font size, color for axis labels, both custom labels and default label values
    :type chxs: str
    :param chm: compound charts and line fills
    :type chm: str
    :param chls: line thickness and solid/dashed style
    :type chls: str
    :param chlps: Position and style of labels on data
    :type chlps: str
    :param chma: chart margins
    :type chma: str
    :param chdlp: Position of the legend and order of the legend entries
    :type chdlp: str
    :param chf: Background Fills
    :type chf: str
    :param chbh: Bar Width and Spacing. (not supported)  You can optionally specify custom values for bar widths and spacing between bars and groups. You can only specify one set of width values for all bars. If you don&#39;t specify chbh, all bars will be 23 pixels wide, which means that the end bars can be clipped if the total bar + space width is wider than the chart width.
    :type chbh: str
    :param chbr: Bar corner radius. Display bars with rounded corner.
    :type chbr: str
    :param chan: gif configuration
    :type chan: str
    :param chli: doughnut chart inside label
    :type chli: str
    :param icac: image-charts enterprise &#x60;account_id&#x60;
    :type icac: str
    :param ichm: HMAC-SHA256 signature required to activate paid features
    :type ichm: str
    :param icff: Default font family for all text from Google Fonts. Use same syntax as Google Font CSS API
    :type icff: str
    :param icfs: Default font style for all text
    :type icfs: str
    :param iclocale: localization (ISO 639-1)
    :type iclocale: str
    :param icwt: (Private) Force to display the watermark EVEN IF the chart was signed with an enterprise account
    :type icwt: bool
    :param icretina: retina mode
    :type icretina: str
    :param icqrb: Background color for QR Codes
    :type icqrb: str
    :param icqrf: Foreground color for QR Codes
    :type icqrf: str

    """
    return web.Response(status=200)
