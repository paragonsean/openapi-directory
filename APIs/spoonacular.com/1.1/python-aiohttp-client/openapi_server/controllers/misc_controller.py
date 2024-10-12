from typing import List, Dict
from aiohttp import web

from openapi_server.models.detect_food_in_text200_response import DetectFoodInText200Response
from openapi_server.models.get_a_random_food_joke200_response import GetARandomFoodJoke200Response
from openapi_server.models.get_conversation_suggests200_response import GetConversationSuggests200Response
from openapi_server.models.get_random_food_trivia200_response import GetRandomFoodTrivia200Response
from openapi_server.models.image_analysis_by_url200_response import ImageAnalysisByURL200Response
from openapi_server.models.image_classification_by_url200_response import ImageClassificationByURL200Response
from openapi_server.models.search_all_food200_response import SearchAllFood200Response
from openapi_server.models.search_custom_foods200_response import SearchCustomFoods200Response
from openapi_server.models.search_food_videos200_response import SearchFoodVideos200Response
from openapi_server.models.search_site_content200_response import SearchSiteContent200Response
from openapi_server.models.talk_to_chatbot200_response import TalkToChatbot200Response
from openapi_server import util


async def detect_food_in_text(request: web.Request, content_type=None) -> web.Response:
    """Detect Food in Text

    Take any text and find all mentions of food contained within it. This task is also called Named Entity Recognition (NER). In this case, the entities are foods. Either dishes, such as pizza or cheeseburger, or ingredients, such as cucumber or almonds.

    :param content_type: The content type.
    :type content_type: str

    """
    return web.Response(status=200)


async def get_a_random_food_joke(request: web.Request, ) -> web.Response:
    """Random Food Joke

    Get a random joke that is related to food. Caution: this is an endpoint for adults!


    """
    return web.Response(status=200)


async def get_conversation_suggests(request: web.Request, query, number=None) -> web.Response:
    """Conversation Suggests

    This endpoint returns suggestions for things the user can say or ask the chatbot.

    :param query: A (partial) query from the user. The endpoint will return if it matches topics it can talk about.
    :type query: str
    :param number: The number of suggestions to return (between 1 and 25).
    :type number: 

    """
    return web.Response(status=200)


async def get_random_food_trivia(request: web.Request, ) -> web.Response:
    """Random Food Trivia

    Returns random food trivia.


    """
    return web.Response(status=200)


async def image_analysis_by_url(request: web.Request, image_url) -> web.Response:
    """Image Analysis by URL

    Analyze a food image. The API tries to classify the image, guess the nutrition, and find a matching recipes.

    :param image_url: The URL of the image to be analyzed.
    :type image_url: str

    """
    return web.Response(status=200)


async def image_classification_by_url(request: web.Request, image_url) -> web.Response:
    """Image Classification by URL

    Classify a food image.

    :param image_url: The URL of the image to be classified.
    :type image_url: str

    """
    return web.Response(status=200)


async def search_all_food(request: web.Request, query, offset=None, number=None) -> web.Response:
    """Search All Food

    Search all food content with one call. That includes recipes, grocery products, menu items, simple foods (ingredients), and food videos.

    :param query: The search query.
    :type query: str
    :param offset: The number of results to skip (between 0 and 900).
    :type offset: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int

    """
    return web.Response(status=200)


async def search_custom_foods(request: web.Request, username, hash, query=None, offset=None, number=None) -> web.Response:
    """Search Custom Foods

    Search custom foods in a user&#39;s account.

    :param username: The username.
    :type username: str
    :param hash: The private hash for the username.
    :type hash: str
    :param query: The (natural language) search query.
    :type query: str
    :param offset: The number of results to skip (between 0 and 900).
    :type offset: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int

    """
    return web.Response(status=200)


async def search_food_videos(request: web.Request, query=None, type=None, cuisine=None, diet=None, include_ingredients=None, exclude_ingredients=None, min_length=None, max_length=None, offset=None, number=None) -> web.Response:
    """Search Food Videos

    Find recipe and other food related videos.

    :param query: The (natural language) search query.
    :type query: str
    :param type: The type of the recipes. See a full list of supported meal types.
    :type type: str
    :param cuisine: The cuisine(s) of the recipes. One or more, comma separated. See a full list of supported cuisines.
    :type cuisine: str
    :param diet: The diet for which the recipes must be suitable. See a full list of supported diets.
    :type diet: str
    :param include_ingredients: A comma-separated list of ingredients that the recipes should contain.
    :type include_ingredients: str
    :param exclude_ingredients: A comma-separated list of ingredients or ingredient types that the recipes must not contain.
    :type exclude_ingredients: str
    :param min_length: Minimum video length in seconds.
    :type min_length: 
    :param max_length: Maximum video length in seconds.
    :type max_length: 
    :param offset: The number of results to skip (between 0 and 900).
    :type offset: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int

    """
    return web.Response(status=200)


async def search_site_content(request: web.Request, query) -> web.Response:
    """Search Site Content

    Search spoonacular&#39;s site content. You&#39;ll be able to find everything that you could also find using the search suggestions on spoonacular.com. This is a suggest API so you can send partial strings as queries.

    :param query: The query to search for. You can also use partial queries such as \&quot;spagh\&quot; to already find spaghetti recipes, articles, grocery products, and other content.
    :type query: str

    """
    return web.Response(status=200)


async def talk_to_chatbot(request: web.Request, text, context_id=None) -> web.Response:
    """Talk to Chatbot

    This endpoint can be used to have a conversation about food with the spoonacular chatbot. Use the \&quot;Get Conversation Suggests\&quot; endpoint to show your user what he or she can say.

    :param text: The request / question / answer from the user to the chatbot.
    :type text: str
    :param context_id: An arbitrary globally unique id for your conversation. The conversation can contain states so you should pass your context id if you want the bot to be able to remember the conversation.
    :type context_id: str

    """
    return web.Response(status=200)
