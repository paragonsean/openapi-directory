from typing import List, Dict
from aiohttp import web

from openapi_server.models.joke_response import JokeResponse
from openapi_server import util


async def joke_categories_search_get(request: web.Request, query, start=None) -> web.Response:
    """joke_categories_search_get

    Gets a list of &#x60;Joke&#x60; Categories, based on a query term. 

    :param query: Search Query
    :type query: str
    :param start: Response is paged. This parameter controls where response starts the listing at
    :type start: int

    """
    return web.Response(status=200)


async def joke_delete(request: web.Request, id) -> web.Response:
    """joke_delete

    Delete a joke. The user needs to be the owner of the joke to be able to delete it. 

    :param id: Joke ID
    :type id: str

    """
    return web.Response(status=200)


async def joke_get(request: web.Request, id=None) -> web.Response:
    """joke_get

    Gets a &#x60;Joke&#x60; with a given &#x60;id&#x60;.

    :param id: Joke ID
    :type id: str

    """
    return web.Response(status=200)


async def joke_list_get(request: web.Request, start=None) -> web.Response:
    """joke_list_get

    Get the list of jokes in your private collection.

    :param start: Response is paged. This parameter controls where response starts the listing at
    :type start: int

    """
    return web.Response(status=200)


async def joke_patch(request: web.Request, id, title=None, text=None, author=None, tags=None) -> web.Response:
    """joke_patch

    Update a joke

    :param id: Joke ID
    :type id: str
    :param title: title
    :type title: str
    :param text: text
    :type text: str
    :param author: Joke Author
    :type author: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def joke_put(request: web.Request, title, text, author=None, tags=None) -> web.Response:
    """joke_put

    Add a new joke to your private collection.

    :param title: Joke Title
    :type title: str
    :param text: Joke Text
    :type text: str
    :param author: Joke Author
    :type author: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def joke_random_get(request: web.Request, ) -> web.Response:
    """joke_random_get

    Gets a &#x60;Random Joke&#x60;. When you are in a hurry this is what you call to get a random famous joke.


    """
    return web.Response(status=200)


async def joke_search_get(request: web.Request, category=None, query=None, minlength=None, maxlength=None, author=None, private=None) -> web.Response:
    """joke_search_get

    Search for a &#x60;Joke&#x60; in Jokes One platform. Optional &#x60;category&#x60; , &#x60;author&#x60;, &#x60;minlength&#x60;, &#x60;maxlength&#x60; params determines the filters applied while searching for the joke. 

    :param category: Joke Category
    :type category: str
    :param query: keyword to search for in the joke
    :type query: str
    :param minlength: Joke minimum Length
    :type minlength: int
    :param maxlength: Joke maximum Length
    :type maxlength: int
    :param author: Joke Author
    :type author: str
    :param private: Should search private collection? Default searches public collection.
    :type private: bool

    """
    return web.Response(status=200)


async def joke_tags_add_post(request: web.Request, id, tags) -> web.Response:
    """joke_tags_add_post

    Add a tag to a given Joke.

    :param id: Joke ID
    :type id: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def joke_tags_remove_post(request: web.Request, id, tags) -> web.Response:
    """joke_tags_remove_post

    Remove a tag from a given joke.

    :param id: Joke ID
    :type id: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)
