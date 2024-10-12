from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def animate_image(request: web.Request, url, type) -> web.Response:
    """Animate Image

    Returns URL of an animated GIF.

    :param url: URL of the company
    :type url: str
    :param type: URL of the company
    :type type: str

    """
    return web.Response(status=200)


async def auto_emojify(request: web.Request, text) -> web.Response:
    """Auto-Emojify

    Returns text of the post with emoji added

    :param text: Text of the post
    :type text: str

    """
    return web.Response(status=200)


async def auto_hashtag(request: web.Request, post, max_hashtags=None, hashtag_position=None) -> web.Response:
    """Auto-Hashtag

    Returns auto-hashtagged text of the post.

    :param post: Text of the post
    :type post: str
    :param max_hashtags: Max number of hashtags.
    :type max_hashtags: int
    :param hashtag_position: Position of hashtags: end &#x3D;&gt; at the end, auto &#x3D;&gt; anywhere
    :type hashtag_position: str

    """
    return web.Response(status=200)


async def company_logo(request: web.Request, domain) -> web.Response:
    """Company Logo

    Returns a company logo based on website domain. If the logo is not in our database yet, it will be extracted from the site on the fly. White logo background is automatically removed to make the logo look better on color backgrounds.  Note: It is not possible to access our company logo API publicly without authentication. If you wish to do so, you have to create proxy on your own server that calls our API from the server side.

    :param domain: URL of the company
    :type domain: str

    """
    return web.Response(status=200)


async def emoji_suggestions(request: web.Request, text) -> web.Response:
    """Emoji Suggestions

    Returns list of emoji suggestions for a given text of the post

    :param text: Text of the post
    :type text: str

    """
    return web.Response(status=200)


async def hashtag_history(request: web.Request, hashtag) -> web.Response:
    """Hashtag History

    Returns historical stats for a given hashtag from the last 30 days

    :param hashtag: Hashtag without # mark
    :type hashtag: str

    """
    return web.Response(status=200)


async def hashtag_stats(request: web.Request, tags) -> web.Response:
    """Hashtag Stats

    Returns real-time stats for up to 100 hashtags (updated hourly).

    :param tags: Hashtag(s) without # mark
    :type tags: List[]

    """
    return web.Response(status=200)


async def hashtag_suggestions(request: web.Request, text) -> web.Response:
    """Hashtag Suggestions

    Returns list of hashtag suggestions for a single-word topic or a shorter text up to 1000 characters. Takes into account both semantic relevancy and real-time hashtag popularity.

    :param text: Topic
    :type text: str

    """
    return web.Response(status=200)


async def hashtags_cleaner(request: web.Request, post) -> web.Response:
    """Hashtags cleaner

    Remove banned hashtags before posting to Instagram

    :param post: post
    :type post: str

    """
    return web.Response(status=200)


async def list_of_ctas(request: web.Request, ) -> web.Response:
    """List of CTAs

    Returns list of available CTA for current user. Requires each user to authenticate with RiteKit


    """
    return web.Response(status=200)


async def shorten_link(request: web.Request, url, cta) -> web.Response:
    """Shorten Link

    Returns a shorten link with a given CTA.

    :param url: URL
    :type url: str
    :param cta: cta id
    :type cta: int

    """
    return web.Response(status=200)


async def text_to_image(request: web.Request, quote, author, font_size, quote_font, quote_font_color, author_font, author_font_color, enable_highlight, highlight_color, bg_type, background_color, gradient_type, gradient_color1, gradient_color2, brand_logo, animation, show_quote_mark=None) -> web.Response:
    """Text to Image

    Returns URL of an image created from text according to given style parameters

    :param quote: Text of the quote
    :type quote: str
    :param author: Name of the author/source
    :type author: str
    :param font_size: Font size for the quote (author font size is calculated automatically)
    :type font_size: int
    :param quote_font: Font-family used for quote text
    :type quote_font: str
    :param quote_font_color: Font color of the quote text
    :type quote_font_color: str
    :param author_font: Font-family used for author name
    :type author_font: str
    :param author_font_color: Font color of the author
    :type author_font_color: str
    :param enable_highlight: Enable highlight on quote text
    :type enable_highlight: int
    :param highlight_color: Color used for highlight
    :type highlight_color: str
    :param bg_type: Background type (gradient/solid)
    :type bg_type: str
    :param background_color: Background color for solid background type
    :type background_color: str
    :param gradient_type: Type of gradient background (linear/radial)
    :type gradient_type: str
    :param gradient_color1: First color for gradient background type
    :type gradient_color1: str
    :param gradient_color2: Second color for gradient background type
    :type gradient_color2: str
    :param brand_logo: URL of the brand logo
    :type brand_logo: str
    :param animation: Animation type: none, rays, glint, circle
    :type animation: str
    :param show_quote_mark: showing/hiding quote mark
    :type show_quote_mark: int

    """
    return web.Response(status=200)


async def trending_hashtags(request: web.Request, green=None, latin=None) -> web.Response:
    """Trending Hashtags

    Returns list of hashtags currently trending on Twitter

    :param green: Restrict results only to green hashtags. Hides overused (red) hashtags.
    :type green: bool
    :param latin: Restrict results only to hashtags with latin characters
    :type latin: bool

    """
    return web.Response(status=200)
