from typing import List, Dict
from aiohttp import web

from openapi_server.models.api2_models_recipes_feedback_dto import API2ModelsRecipesFeedbackDTO
from openapi_server.models.api2_models_recipes_recipe_response import API2ModelsRecipesRecipeResponse
from openapi_server.models.api2_result import API2Result
from openapi_server.models.big_oven_model_api2_recipe import BigOvenModelAPI2Recipe
from openapi_server.models.big_oven_model_api2_recipe_search_result import BigOvenModelAPI2RecipeSearchResult
from openapi_server.models.big_oven_model_api_recipe import BigOvenModelAPIRecipe
from openapi_server.models.big_oven_model_recipe_category import BigOvenModelRecipeCategory
from openapi_server.models.big_oven_model_recipe_info_date_tuple2 import BigOvenModelRecipeInfoDateTuple2
from openapi_server.models.big_oven_model_recipe_info_review_tuple2 import BigOvenModelRecipeInfoReviewTuple2
from openapi_server.models.big_oven_model_recipe_info_tiny import BigOvenModelRecipeInfoTiny
from openapi_server.models.big_oven_result import BigOvenResult
from openapi_server import util


async def recipe_auto_complete(request: web.Request, query, limit=None) -> web.Response:
    """Given a query, return recipe titles starting with query. Query must be at least 3 chars in length.

    

    :param query: 
    :type query: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def recipe_auto_complete_all_recipes(request: web.Request, query, limit) -> web.Response:
    """Automatics the complete all recipes.

    

    :param query: The query.
    :type query: str
    :param limit: The limit.
    :type limit: int

    """
    return web.Response(status=200)


async def recipe_auto_complete_my_recipes(request: web.Request, query, limit) -> web.Response:
    """Automatics the complete my recipes.

    

    :param query: The query.
    :type query: str
    :param limit: The limit.
    :type limit: int

    """
    return web.Response(status=200)


async def recipe_categories(request: web.Request, ) -> web.Response:
    """Get a list of recipe categories (the ID field can be used for include_cat in search parameters)

    


    """
    return web.Response(status=200)


async def recipe_delete(request: web.Request, id) -> web.Response:
    """Delete a Recipe (you must be authenticated as an owner of the recipe)

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def recipe_feedback(request: web.Request, recipe_id, body) -> web.Response:
    """Feedback on a Recipe -- for internal BigOven editors

    

    :param recipe_id: 
    :type recipe_id: int
    :param body: The payload for feedback, which includes the field \&quot;feedback\&quot;
    :type body: dict | bytes

    """
    body = API2ModelsRecipesFeedbackDTO.from_dict(body)
    return web.Response(status=200)


async def recipe_get(request: web.Request, id, prefetch=None) -> web.Response:
    """Return full Recipe detail. Returns 403 if the recipe is owned by someone else.

    

    :param id: The Recipe ID to retrieve
    :type id: int
    :param prefetch: The prefetch.
    :type prefetch: bool

    """
    return web.Response(status=200)


async def recipe_get_active_recipe(request: web.Request, user_name) -> web.Response:
    """Returns last active recipe for the user

    

    :param user_name: 
    :type user_name: str

    """
    return web.Response(status=200)


async def recipe_get_random_recipe(request: web.Request, ) -> web.Response:
    """Get a random, home-page-quality Recipe.

    


    """
    return web.Response(status=200)


async def recipe_get_recipe_with_steps(request: web.Request, id, prefetch=None) -> web.Response:
    """Return full Recipe detail with steps. Returns 403 if the recipe is owned by someone else.

    

    :param id: the Recipe ID to retrieve
    :type id: int
    :param prefetch: 
    :type prefetch: bool

    """
    return web.Response(status=200)


async def recipe_get_step(request: web.Request, user_name, recipe_id, step_id) -> web.Response:
    """Gets recipe single step as text

    

    :param user_name: 
    :type user_name: str
    :param recipe_id: 
    :type recipe_id: int
    :param step_id: 
    :type step_id: int

    """
    return web.Response(status=200)


async def recipe_get_step_number(request: web.Request, user_name, recipe_id) -> web.Response:
    """Returns stored step number and number of steps in recipe

    

    :param user_name: 
    :type user_name: str
    :param recipe_id: 
    :type recipe_id: int

    """
    return web.Response(status=200)


async def recipe_get_steps(request: web.Request, user_name, recipe_id, step_id) -> web.Response:
    """Stores recipe step number and returns saved step data

    

    :param user_name: 
    :type user_name: str
    :param recipe_id: 
    :type recipe_id: int
    :param step_id: 
    :type step_id: int

    """
    return web.Response(status=200)


async def recipe_get_v2(request: web.Request, id, prefetch=None) -> web.Response:
    """Same as GET recipe but also includes the recipe videos (if any)

    

    :param id: The Recipe ID to retrieve
    :type id: int
    :param prefetch: The prefetch.
    :type prefetch: bool

    """
    return web.Response(status=200)


async def recipe_post(request: web.Request, body) -> web.Response:
    """Add a new recipe

    

    :param body: 
    :type body: dict | bytes

    """
    body = BigOvenModelAPIRecipe.from_dict(body)
    return web.Response(status=200)


async def recipe_put(request: web.Request, body) -> web.Response:
    """Update a recipe

    

    :param body: 
    :type body: dict | bytes

    """
    body = BigOvenModelAPIRecipe.from_dict(body)
    return web.Response(status=200)


async def recipe_raves(request: web.Request, pg=None, rpp=None) -> web.Response:
    """Get the recipe/comment tuples for those recipes with 4 or 5 star ratings

    

    :param pg: page, starting with 1
    :type pg: int
    :param rpp: results per page
    :type rpp: int

    """
    return web.Response(status=200)


async def recipe_recent_views(request: web.Request, pg=None, rpp=None) -> web.Response:
    """Get a list of recipes that the authenticated user has most recently viewed

    

    :param pg: Page number starting with 1
    :type pg: int
    :param rpp: results per page
    :type rpp: int

    """
    return web.Response(status=200)


async def recipe_recipe_search(request: web.Request, any_kw=None, folder=None, coll=None, filter=None, title_kw=None, user_id=None, username=None, token=None, photos=None, boostmine=None, include_cat=None, exclude_cat=None, include_primarycat=None, exclude_primarycat=None, include_ing=None, exclude_ing=None, cuisine=None, db=None, userset=None, servings_min=None, total_mins=None, max_ingredients=None, min_ingredients=None, rpp=None, pg=None, vtn=None, vgn=None, chs=None, glf=None, ntf=None, dyf=None, sff=None, slf=None, tnf=None, wmf=None, rmf=None, cps=None, champion=None, synonyms=None) -> web.Response:
    """Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection

    

    :param any_kw: Search anywhere in the recipe for the keyword
    :type any_kw: str
    :param folder: Search in a specific folder name for the authenticated user
    :type folder: str
    :param coll: Limit to a collection ID number
    :type coll: int
    :param filter: optionally set to either \&quot;myrecipes\&quot;, \&quot;try\&quot;, \&quot;favorites\&quot;,\&quot;added\&quot; to filter to just the authenticated user&#39;s recipe set
    :type filter: str
    :param title_kw: Search just in the recipe title for the keyword
    :type title_kw: str
    :param user_id: Set the target userid to search their public recipes
    :type user_id: int
    :param username: Set the target username to search their public recipes
    :type username: str
    :param token: 
    :type token: str
    :param photos: if set to true, limit search results to photos only
    :type photos: bool
    :param boostmine: if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders)
    :type boostmine: bool
    :param include_cat: integer of the subcategory you&#39;d like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \&quot;Main Dish &amp;gt; Casseroles\&quot;.
    :type include_cat: str
    :param exclude_cat: like include_cat, set this to an integer to exclude a specific category
    :type exclude_cat: str
    :param include_primarycat: csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
    :type include_primarycat: str
    :param exclude_primarycat: csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
    :type exclude_primarycat: str
    :param include_ing: A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken
    :type include_ing: str
    :param exclude_ing: A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required)
    :type exclude_ing: str
    :param cuisine: Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese
    :type cuisine: str
    :param db: 
    :type db: str
    :param userset: If set to a given username, it&#39;ll force the search to filter to just that username
    :type userset: str
    :param servings_min: Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \&quot;dozen\&quot;, etc. This parameter simply specifies the minimum number for that value entered in \&quot;yield.\&quot;
    :type servings_min: float
    :param total_mins: Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \&quot;1 hour, 15 minutes\&quot; to 75 before passing in.)
    :type total_mins: int
    :param max_ingredients: Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less
    :type max_ingredients: int
    :param min_ingredients: Optional. If supplied, will restrict results to recipes that have at least {minIngredients}
    :type min_ingredients: int
    :param rpp: integer; results per page
    :type rpp: int
    :param pg: integer: the page number
    :type pg: int
    :param vtn: when set to 1, limit to vegetarian (Powersearch-capable plan required)
    :type vtn: int
    :param vgn: when set to 1, limit to vegan (Powersearch-capable plan required)
    :type vgn: int
    :param chs: when set to 1, limit to contains-cheese (Powersearch-capable plan required)
    :type chs: int
    :param glf: when set to 1, limit to gluten-free (Powersearch-capable plan required)
    :type glf: int
    :param ntf: when set to 1, limit to nut-free (Powersearch-capable plan required)
    :type ntf: int
    :param dyf: when set to 1, limit to dairy-free (Powersearch-capable plan required)
    :type dyf: int
    :param sff: when set to 1, limit to seafood-free (Powersearch-capable plan required)
    :type sff: int
    :param slf: when set to 1, limit to shellfish-free (Powersearch-capable plan required)
    :type slf: int
    :param tnf: when set to 1, limit to tree-nut free (Powersearch-capable plan required)
    :type tnf: int
    :param wmf: when set to 1, limit to white-meat free (Powersearch-capable plan required)
    :type wmf: int
    :param rmf: when set to 1, limit to red-meat free (Powersearch-capable plan required)
    :type rmf: int
    :param cps: when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required)
    :type cps: int
    :param champion: optional. When set to 1, this will limit search results to \&quot;best of\&quot; recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don&#39;t include this parameter.
    :type champion: int
    :param synonyms: optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon)
    :type synonyms: bool

    """
    return web.Response(status=200)


async def recipe_recipe_search_random(request: web.Request, any_kw=None, folder=None, coll=None, filter=None, title_kw=None, user_id=None, username=None, token=None, photos=None, boostmine=None, include_cat=None, exclude_cat=None, include_primarycat=None, exclude_primarycat=None, include_ing=None, exclude_ing=None, cuisine=None, db=None, userset=None, servings_min=None, total_mins=None, max_ingredients=None, min_ingredients=None, vtn=None, vgn=None, chs=None, glf=None, ntf=None, dyf=None, sff=None, slf=None, tnf=None, wmf=None, rmf=None, cps=None, champion=None, synonyms=None) -> web.Response:
    """Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection

    

    :param any_kw: Search anywhere in the recipe for the keyword
    :type any_kw: str
    :param folder: Search in a specific folder name for the authenticated user
    :type folder: str
    :param coll: Limit to a collection ID number
    :type coll: int
    :param filter: optionally set to either \&quot;myrecipes\&quot;, \&quot;try\&quot;, \&quot;favorites\&quot;,\&quot;added\&quot; to filter to just the authenticated user&#39;s recipe set
    :type filter: str
    :param title_kw: Search just in the recipe title for the keyword
    :type title_kw: str
    :param user_id: Set the target userid to search their public recipes
    :type user_id: int
    :param username: Set the target username to search their public recipes
    :type username: str
    :param token: 
    :type token: str
    :param photos: if set to true, limit search results to photos only
    :type photos: bool
    :param boostmine: if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders)
    :type boostmine: bool
    :param include_cat: integer of the subcategory you&#39;d like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \&quot;Main Dish &amp;gt; Casseroles\&quot;.
    :type include_cat: str
    :param exclude_cat: like include_cat, set this to an integer to exclude a specific category
    :type exclude_cat: str
    :param include_primarycat: csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
    :type include_primarycat: str
    :param exclude_primarycat: csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
    :type exclude_primarycat: str
    :param include_ing: A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken
    :type include_ing: str
    :param exclude_ing: A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required)
    :type exclude_ing: str
    :param cuisine: Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese
    :type cuisine: str
    :param db: 
    :type db: str
    :param userset: If set to a given username, it&#39;ll force the search to filter to just that username
    :type userset: str
    :param servings_min: Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \&quot;dozen\&quot;, etc. This parameter simply specifies the minimum number for that value entered in \&quot;yield.\&quot;
    :type servings_min: float
    :param total_mins: Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \&quot;1 hour, 15 minutes\&quot; to 75 before passing in.)
    :type total_mins: int
    :param max_ingredients: Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less
    :type max_ingredients: int
    :param min_ingredients: Optional. If supplied, will restrict results to recipes that have at least {minIngredients}
    :type min_ingredients: int
    :param vtn: when set to 1, limit to vegetarian (Powersearch-capable plan required)
    :type vtn: int
    :param vgn: when set to 1, limit to vegan (Powersearch-capable plan required)
    :type vgn: int
    :param chs: when set to 1, limit to contains-cheese (Powersearch-capable plan required)
    :type chs: int
    :param glf: when set to 1, limit to gluten-free (Powersearch-capable plan required)
    :type glf: int
    :param ntf: when set to 1, limit to nut-free (Powersearch-capable plan required)
    :type ntf: int
    :param dyf: when set to 1, limit to dairy-free (Powersearch-capable plan required)
    :type dyf: int
    :param sff: when set to 1, limit to seafood-free (Powersearch-capable plan required)
    :type sff: int
    :param slf: when set to 1, limit to shellfish-free (Powersearch-capable plan required)
    :type slf: int
    :param tnf: when set to 1, limit to tree-nut free (Powersearch-capable plan required)
    :type tnf: int
    :param wmf: when set to 1, limit to white-meat free (Powersearch-capable plan required)
    :type wmf: int
    :param rmf: when set to 1, limit to red-meat free (Powersearch-capable plan required)
    :type rmf: int
    :param cps: when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required)
    :type cps: int
    :param champion: optional. When set to 1, this will limit search results to \&quot;best of\&quot; recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don&#39;t include this parameter.
    :type champion: int
    :param synonyms: optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon)
    :type synonyms: bool

    """
    return web.Response(status=200)


async def recipe_related(request: web.Request, recipe_id, pg=None, rpp=None) -> web.Response:
    """Get recipes related to the given recipeId

    

    :param recipe_id: The recipe id
    :type recipe_id: int
    :param pg: The page
    :type pg: int
    :param rpp: The results per page
    :type rpp: int

    """
    return web.Response(status=200)


async def recipe_scan(request: web.Request, test=None, devicetype=None, lat=None, lng=None) -> web.Response:
    """POST an image as a new RecipeScan request                  1)  Fetch the filename -- DONE                  2)  Copy it to the pics/scan folder - ENSURE NO NAMING COLLISIONS -- DONE                  3)  Create 120 thumbnail size  in pics/scan/120 -- DONE                  4)  Insert the CloudTasks record                  5)  Create the HIT                  6)  Update the CloudTasks record with the HIT ID                  7)  Email the requesing user                  8)  Call out to www.bigoven.com to fetch the image and re-create the thumbnail

    

    :param test: 
    :type test: bool
    :param devicetype: 
    :type devicetype: str
    :param lat: 
    :type lat: float
    :param lng: 
    :type lng: float

    """
    return web.Response(status=200)


async def recipe_zap_recipe(request: web.Request, id) -> web.Response:
    """Zaps the recipe.

    

    :param id: The identifier.
    :type id: int

    """
    return web.Response(status=200)
