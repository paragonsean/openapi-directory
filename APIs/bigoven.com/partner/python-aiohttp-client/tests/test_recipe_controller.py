# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_recipe_auto_complete(client):
    """Test case for recipe_auto_complete

    Given a query, return recipe titles starting with query. Query must be at least 3 chars in length.
    """
    params = [('query', 'query_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_auto_complete_all_recipes(client):
    """Test case for recipe_auto_complete_all_recipes

    Automatics the complete all recipes.
    """
    params = [('query', 'query_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/autocomplete/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_auto_complete_my_recipes(client):
    """Test case for recipe_auto_complete_my_recipes

    Automatics the complete my recipes.
    """
    params = [('query', 'query_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/autocomplete/mine',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_categories(client):
    """Test case for recipe_categories

    Get a list of recipe categories (the ID field can be used for include_cat in search parameters)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_delete(client):
    """Test case for recipe_delete

    Delete a Recipe (you must be authenticated as an owner of the recipe)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/recipe/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_recipe_feedback(client):
    """Test case for recipe_feedback

    Feedback on a Recipe -- for internal BigOven editors
    """
    body = openapi_server.API2ModelsRecipesFeedbackDTO()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe/{recipe_id}/feedback'.format(recipe_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_get(client):
    """Test case for recipe_get

    Return full Recipe detail. Returns 403 if the recipe is owned by someone else.
    """
    params = [('prefetch', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_get_active_recipe(client):
    """Test case for recipe_get_active_recipe

    Returns last active recipe for the user
    """
    params = [('userName', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/get/active/recipe',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_get_random_recipe(client):
    """Test case for recipe_get_random_recipe

    Get a random, home-page-quality Recipe.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipes/random',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_get_recipe_with_steps(client):
    """Test case for recipe_get_recipe_with_steps

    Return full Recipe detail with steps. Returns 403 if the recipe is owned by someone else.
    """
    params = [('prefetch', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/steps/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_get_step(client):
    """Test case for recipe_get_step

    Gets recipe single step as text
    """
    params = [('userName', 'user_name_example'),
                    ('recipeId', 56),
                    ('stepId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe/get/saved/step',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_get_step_number(client):
    """Test case for recipe_get_step_number

    Returns stored step number and number of steps in recipe
    """
    params = [('userName', 'user_name_example'),
                    ('recipeId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe/get/step/number',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_get_steps(client):
    """Test case for recipe_get_steps

    Stores recipe step number and returns saved step data
    """
    params = [('userName', 'user_name_example'),
                    ('recipeId', 56),
                    ('stepId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe/post/step',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_get_v2(client):
    """Test case for recipe_get_v2

    Same as GET recipe but also includes the recipe videos (if any)
    """
    params = [('prefetch', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_recipe_post(client):
    """Test case for recipe_post

    Add a new recipe
    """
    body = openapi_server.BigOvenModelAPIRecipe()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_recipe_put(client):
    """Test case for recipe_put

    Update a recipe
    """
    body = openapi_server.BigOvenModelAPIRecipe()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/recipe',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_raves(client):
    """Test case for recipe_raves

    Get the recipe/comment tuples for those recipes with 4 or 5 star ratings
    """
    params = [('pg', 56),
                    ('rpp', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipes/raves',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_recent_views(client):
    """Test case for recipe_recent_views

    Get a list of recipes that the authenticated user has most recently viewed
    """
    params = [('pg', 56),
                    ('rpp', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipes/recentviews',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_recipe_search(client):
    """Test case for recipe_recipe_search

    Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you'd like to limit by course, set the parameter \"include_primarycat\" to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you'd like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you'd like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \"include_ing\" to a CSV of up to three ingredients, e.g.:include_ing=mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \"exclude_ing\" to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you'd pass pg=3&amp;rpp=25              If you'd like to target searches to just a single target user's recipes, set userId=the target userId (number).              Or, you can set username=theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter=added,try,favorites,myrecipes\\r\\n\\r\\n              folder=FolderNameCaseSensitive              coll=ID of Collection
    """
    params = [('any_kw', 'any_kw_example'),
                    ('folder', 'folder_example'),
                    ('coll', 56),
                    ('filter', 'filter_example'),
                    ('title_kw', 'title_kw_example'),
                    ('userId', 56),
                    ('username', 'username_example'),
                    ('token', 'token_example'),
                    ('photos', True),
                    ('boostmine', True),
                    ('include_cat', 'include_cat_example'),
                    ('exclude_cat', 'exclude_cat_example'),
                    ('include_primarycat', 'include_primarycat_example'),
                    ('exclude_primarycat', 'exclude_primarycat_example'),
                    ('include_ing', 'include_ing_example'),
                    ('exclude_ing', 'exclude_ing_example'),
                    ('cuisine', 'cuisine_example'),
                    ('db', 'db_example'),
                    ('userset', 'userset_example'),
                    ('servingsMin', 3.4),
                    ('totalMins', 56),
                    ('maxIngredients', 56),
                    ('minIngredients', 56),
                    ('rpp', 56),
                    ('pg', 56),
                    ('vtn', 56),
                    ('vgn', 56),
                    ('chs', 56),
                    ('glf', 56),
                    ('ntf', 56),
                    ('dyf', 56),
                    ('sff', 56),
                    ('slf', 56),
                    ('tnf', 56),
                    ('wmf', 56),
                    ('rmf', 56),
                    ('cps', 56),
                    ('champion', 56),
                    ('synonyms', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_recipe_search_random(client):
    """Test case for recipe_recipe_search_random

    Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you'd like to limit by course, set the parameter \"include_primarycat\" to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you'd like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you'd like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \"include_ing\" to a CSV of up to three ingredients, e.g.:include_ing=mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \"exclude_ing\" to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you'd pass pg=3&amp;rpp=25              If you'd like to target searches to just a single target user's recipes, set userId=the target userId (number).              Or, you can set username=theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter=added,try,favorites,myrecipes\\r\\n\\r\\n              folder=FolderNameCaseSensitive              coll=ID of Collection
    """
    params = [('any_kw', 'any_kw_example'),
                    ('folder', 'folder_example'),
                    ('coll', 56),
                    ('filter', 'filter_example'),
                    ('title_kw', 'title_kw_example'),
                    ('userId', 56),
                    ('username', 'username_example'),
                    ('token', 'token_example'),
                    ('photos', True),
                    ('boostmine', True),
                    ('include_cat', 'include_cat_example'),
                    ('exclude_cat', 'exclude_cat_example'),
                    ('include_primarycat', 'include_primarycat_example'),
                    ('exclude_primarycat', 'exclude_primarycat_example'),
                    ('include_ing', 'include_ing_example'),
                    ('exclude_ing', 'exclude_ing_example'),
                    ('cuisine', 'cuisine_example'),
                    ('db', 'db_example'),
                    ('userset', 'userset_example'),
                    ('servingsMin', 3.4),
                    ('totalMins', 56),
                    ('maxIngredients', 56),
                    ('minIngredients', 56),
                    ('vtn', 56),
                    ('vgn', 56),
                    ('chs', 56),
                    ('glf', 56),
                    ('ntf', 56),
                    ('dyf', 56),
                    ('sff', 56),
                    ('slf', 56),
                    ('tnf', 56),
                    ('wmf', 56),
                    ('rmf', 56),
                    ('cps', 56),
                    ('champion', 56),
                    ('synonyms', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipes/top25random',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_related(client):
    """Test case for recipe_related

    Get recipes related to the given recipeId
    """
    params = [('pg', 56),
                    ('rpp', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/related'.format(recipe_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_scan(client):
    """Test case for recipe_scan

    POST an image as a new RecipeScan request                  1)  Fetch the filename -- DONE                  2)  Copy it to the pics/scan folder - ENSURE NO NAMING COLLISIONS -- DONE                  3)  Create 120 thumbnail size  in pics/scan/120 -- DONE                  4)  Insert the CloudTasks record                  5)  Create the HIT                  6)  Update the CloudTasks record with the HIT ID                  7)  Email the requesing user                  8)  Call out to www.bigoven.com to fetch the image and re-create the thumbnail
    """
    params = [('test', True),
                    ('devicetype', 'devicetype_example'),
                    ('lat', 3.4),
                    ('lng', 3.4)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/recipe/scan',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_zap_recipe(client):
    """Test case for recipe_zap_recipe

    Zaps the recipe.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{id}/zap'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

