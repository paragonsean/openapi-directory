from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def quote_image_background_delete(request: web.Request, id) -> web.Response:
    """quote_image_background_delete

    Delete a background image file. The user needs to be the owner of the background image to be able to delete it. 

    :param id: Font ID
    :type id: str

    """
    return web.Response(status=200)


async def quote_image_background_list_get(request: web.Request, start=None) -> web.Response:
    """quote_image_background_list_get

    Lists background images in your private collection.  

    :param start: Response is paged. This parameter determines where the response should start.
    :type start: int

    """
    return web.Response(status=200)


async def quote_image_background_post(request: web.Request, image, tags=None) -> web.Response:
    """quote_image_background_post

    Add an image for use later as a quote background image.

    :param image: Image file to add to your collection (png/jpg/gif are supported)
    :type image: str
    :param tags: Optional comma separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def quote_image_background_search_get(request: web.Request, query=None) -> web.Response:
    """quote_image_background_search_get

    Searches for a background image with a given tag.  

    :param query: Tag string
    :type query: str

    """
    return web.Response(status=200)


async def quote_image_background_tags_add_post(request: web.Request, id, tags) -> web.Response:
    """quote_image_background_tags_add_post

    Add a tag to a given Image.

    :param id: Image ID
    :type id: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def quote_image_background_tags_remove_post(request: web.Request, id, tags) -> web.Response:
    """quote_image_background_tags_remove_post

    Remove a tag from a given Image.

    :param id: Image ID
    :type id: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def quote_image_delete(request: web.Request, id) -> web.Response:
    """quote_image_delete

    Delete a quote image. The user needs to be the owner of the quote image to be able to delete it. 

    :param id: Quote Image ID
    :type id: str

    """
    return web.Response(status=200)


async def quote_image_font_delete(request: web.Request, id) -> web.Response:
    """quote_image_font_delete

    Delete a font file. The user needs to be the owner of the font to be able to delete it. 

    :param id: Font ID
    :type id: str

    """
    return web.Response(status=200)


async def quote_image_font_list_get(request: web.Request, start=None) -> web.Response:
    """quote_image_font_list_get

    Lists background images in your private collection.  

    :param start: Response is paged. This parameter determines where the response should start.
    :type start: int

    """
    return web.Response(status=200)


async def quote_image_font_post(request: web.Request, font, tags=None) -> web.Response:
    """quote_image_font_post

    Add a font file for use later in creating a quote image. This is essentially a &#x60;PUT&#x60; but not many clients handle PUT with binary stream i.e. a file, gracefully.

    :param font: Font file to add to your collection (ttf/otf are supported)
    :type font: str
    :param tags: Optional comma separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def quote_image_font_search_get(request: web.Request, query=None) -> web.Response:
    """quote_image_font_search_get

    Searches for a font with a given tag.  

    :param query: Tag string
    :type query: str

    """
    return web.Response(status=200)


async def quote_image_font_tags_add_post(request: web.Request, id, tags) -> web.Response:
    """quote_image_font_tags_add_post

    Add a tag to a given font.

    :param id: Font ID
    :type id: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def quote_image_font_tags_remove_post(request: web.Request, id, tags) -> web.Response:
    """quote_image_font_tags_remove_post

    Remove a tag from a given Font.

    :param id: Font ID
    :type id: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def quote_image_get(request: web.Request, id, binary=None) -> web.Response:
    """quote_image_get

    Gets a Quote image for a given id. Response can be an image file as a binary or a base64 encoded contents wrapped in json. &#x60;TODO&#x60; 

    :param id: Quote Image id
    :type id: str
    :param binary: Should the response be a direct file download of the image or a base64 encoded image file wrapped in json?
    :type binary: bool

    """
    return web.Response(status=200)


async def quote_image_put(request: web.Request, quote_id, bgimage_id=None, bg_color=None, font_id=None, text_color=None, text_size=None, halign=None, valign=None, width=None, height=None, branding=None, include_transparent_layer=None) -> web.Response:
    """quote_image_put

    Create a new quote image for a given quote. Choose background colors/images , choose different font styles and generate a beautiful quote image. Did you just had a feeling of being a god or what?! 

    :param quote_id: Quote id
    :type quote_id: str
    :param bgimage_id: Background Image id ( Will override bgcolor if supplied)
    :type bgimage_id: str
    :param bg_color: Background Color(if background image id is not supplied)
    :type bg_color: str
    :param font_id: Font id
    :type font_id: str
    :param text_color: Text Color
    :type text_color: str
    :param text_size: Text/font size
    :type text_size: str
    :param halign: Horizontal text Alignment Value
    :type halign: str
    :param valign: Vertical text Alignment Value
    :type valign: str
    :param width: Image Width(By default this takes the width of the background image)
    :type width: int
    :param height: Image Height(By default this takes the height of the background image)
    :type height: int
    :param branding: Disable They Said So branding (Only available in certain subscription levels. Ignored in other levels)
    :type branding: bool
    :param include_transparent_layer: Should include a transparent layer between the text and the background image? This helps when the background image is bright and obscures the text.
    :type include_transparent_layer: bool

    """
    return web.Response(status=200)


async def quote_image_search_get(request: web.Request, category=None, author=None, private=None) -> web.Response:
    """quote_image_search_get

    Gets a Random Quote image. Optional &#x60;category&#x60; param determines the category of quote used in the image. Optional &#x60;author&#x60; param gets the quote image of a given author.  

    :param category: Quote Category
    :type category: str
    :param author: Quote Author
    :type author: str
    :param private: Should search private collection. Default searches public image collection.
    :type private: bool

    """
    return web.Response(status=200)
