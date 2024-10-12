from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.browser_bot_response import BrowserBotResponse
from openapi_server.models.url_info_response import URLInfoResponse
from openapi_server import util


async def browser_bot(request: web.Request, url, delay=None, _exec=None, ignore_certificate_errors=None, selector=None, timeout=None, user_agent=None) -> web.Response:
    """Browser Bot

    Browser bot can extract content, interact with keyboard and mouse events, and execute JavaScript on a website

    :param url: The URL to load
    :type url: str
    :param delay: Delay in seconds to wait before capturing any page data, executing selectors or JavaScript
    :type delay: int
    :param _exec: Execute JavaScript on the website. This parameter accepts JavaScript as either a string containing JavaScript or for sending multiple separate statements a JSON array or POST array can also be used. If a statement returns any value it will be returned in the &#39;exec-results&#39; response. You can also use the following specially defined user interaction functions: &lt;br&gt; &lt;br&gt; &lt;div&gt; sleep(seconds); Just wait/sleep for the specified number of seconds. &lt;br&gt;click(&#39;selector&#39;); Click on the first element matching the given selector. &lt;br&gt;focus(&#39;selector&#39;); Focus on the first element matching the given selector. &lt;br&gt;keys(&#39;characters&#39;); Send the specified keyboard characters. Use click() or focus() first to send keys to a specific element. &lt;br&gt;enter(); Send the Enter key. &lt;br&gt;tab(); Send the Tab key. &lt;br&gt; &lt;/div&gt;
    :type _exec: List[str]
    :param ignore_certificate_errors: Ignore any TLS/SSL certificate errors and load the page anyway
    :type ignore_certificate_errors: bool
    :param selector: Extract content from the page DOM using this selector. Commonly known as a CSS selector, you can find a good reference &lt;a href&#x3D;\\\&quot;https://www.w3schools.com/cssref/css_selectors.asp\\\&quot;&gt;here&lt;/a&gt;
    :type selector: str
    :param timeout: Timeout in seconds. Give up if still trying to load the page after this number of seconds
    :type timeout: int
    :param user_agent: Override the browsers default user-agent string with this one
    :type user_agent: str

    """
    return web.Response(status=200)


async def h_tml_clean(request: web.Request, content, output_type) -> web.Response:
    """HTML Clean

    Clean and sanitize untrusted HTML

    :param content: The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string
    :type content: str
    :param output_type: The level of sanitization, possible values are: &lt;br&gt;&lt;b&gt;plain-text&lt;/b&gt;: reduce the content to plain text only (no HTML tags at all) &lt;br&gt;&lt;b&gt;simple-text&lt;/b&gt;: allow only very basic text formatting tags like b, em, i, strong, u &lt;br&gt;&lt;b&gt;basic-html&lt;/b&gt;: allow advanced text formatting and hyper links &lt;br&gt;&lt;b&gt;basic-html-with-images&lt;/b&gt;: same as basic html but also allows image tags &lt;br&gt;&lt;b&gt;advanced-html&lt;/b&gt;: same as basic html with images but also allows many more common HTML tags like table, ul, dl, pre &lt;br&gt;
    :type output_type: str

    """
    return web.Response(status=200)


async def u_rl_info(request: web.Request, url, fetch_content=None, ignore_certificate_errors=None, timeout=None, retry=None) -> web.Response:
    """URL Info

    Parse, analyze and retrieve content from the supplied URL

    :param url: The URL to probe
    :type url: str
    :param fetch_content: If this URL responds with html, text, json or xml then return the response. This option is useful if you want to perform further processing on the URL content (e.g. with the HTML Extract or HTML Clean APIs)
    :type fetch_content: bool
    :param ignore_certificate_errors: Ignore any TLS/SSL certificate errors and load the URL anyway
    :type ignore_certificate_errors: bool
    :param timeout: Timeout in seconds. Give up if still trying to load the URL after this number of seconds
    :type timeout: int
    :param retry: If the request fails for any reason try again this many times
    :type retry: int

    """
    return web.Response(status=200)
