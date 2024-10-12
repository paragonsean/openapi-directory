# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.analyze_a_recipe_search_query200_response import AnalyzeARecipeSearchQuery200Response
from openapi_server.models.analyze_recipe_instructions200_response import AnalyzeRecipeInstructions200Response
from openapi_server.models.classify_cuisine200_response import ClassifyCuisine200Response
from openapi_server.models.compute_glycemic_load200_response import ComputeGlycemicLoad200Response
from openapi_server.models.compute_glycemic_load_request import ComputeGlycemicLoadRequest
from openapi_server.models.convert_amounts200_response import ConvertAmounts200Response
from openapi_server.models.create_recipe_card200_response import CreateRecipeCard200Response
from openapi_server.models.extract_recipe_from_website200_response import ExtractRecipeFromWebsite200Response
from openapi_server.models.generate_meal_plan200_response_meals_inner import GenerateMealPlan200ResponseMealsInner
from openapi_server.models.get_analyzed_recipe_instructions200_response import GetAnalyzedRecipeInstructions200Response
from openapi_server.models.get_random_recipes200_response import GetRandomRecipes200Response
from openapi_server.models.get_recipe_equipment_by_id200_response import GetRecipeEquipmentByID200Response
from openapi_server.models.get_recipe_information_bulk200_response_inner import GetRecipeInformationBulk200ResponseInner
from openapi_server.models.get_recipe_ingredients_by_id200_response import GetRecipeIngredientsByID200Response
from openapi_server.models.get_recipe_nutrition_widget_by_id200_response import GetRecipeNutritionWidgetByID200Response
from openapi_server.models.get_recipe_price_breakdown_by_id200_response import GetRecipePriceBreakdownByID200Response
from openapi_server.models.get_recipe_taste_by_id200_response import GetRecipeTasteByID200Response
from openapi_server.models.guess_nutrition_by_dish_name200_response import GuessNutritionByDishName200Response
from openapi_server.models.parse_ingredients200_response_inner import ParseIngredients200ResponseInner
from openapi_server.models.quick_answer200_response import QuickAnswer200Response
from openapi_server.models.search_grocery_products200_response_products_inner import SearchGroceryProducts200ResponseProductsInner
from openapi_server.models.search_recipes200_response import SearchRecipes200Response
from openapi_server.models.search_recipes200_response_results_inner import SearchRecipes200ResponseResultsInner
from openapi_server.models.search_recipes_by_ingredients200_response_inner import SearchRecipesByIngredients200ResponseInner
from openapi_server.models.summarize_recipe200_response import SummarizeRecipe200Response


pytestmark = pytest.mark.asyncio

async def test_analyze_a_recipe_search_query(client):
    """Test case for analyze_a_recipe_search_query

    Analyze a Recipe Search Query
    """
    params = [('q', 'salmon with fusilli and no nuts')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/queries/analyze',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_analyze_recipe_instructions(client):
    """Test case for analyze_recipe_instructions

    Analyze Recipe Instructions
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/analyzeInstructions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_autocomplete_recipe_search(client):
    """Test case for autocomplete_recipe_search

    Autocomplete Recipe Search
    """
    params = [('query', 'burger'),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_classify_cuisine(client):
    """Test case for classify_cuisine

    Classify Cuisine
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/cuisine',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compute_glycemic_load(client):
    """Test case for compute_glycemic_load

    Compute Glycemic Load
    """
    body = {"ingredients":["1 kiwi","2 cups rice","2 glasses of water"]}
    params = [('language', 'en')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/food/ingredients/glycemicLoad',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_amounts(client):
    """Test case for convert_amounts

    Convert Amounts
    """
    params = [('ingredientName', 'flour'),
                    ('sourceAmount', 2.5),
                    ('sourceUnit', 'cups'),
                    ('targetUnit', 'grams')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/convert',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_recipe_card(client):
    """Test case for create_recipe_card

    Create Recipe Card
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'content_type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/visualizeRecipe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_equipment_by_id_image(client):
    """Test case for equipment_by_id_image

    Equipment by ID Image
    """
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/equipmentWidget.png'.format(id=44860),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extract_recipe_from_website(client):
    """Test case for extract_recipe_from_website

    Extract Recipe from Website
    """
    params = [('url', 'https://foodista.com/recipe/ZHK4KPB6/chocolate-crinkle-cookies'),
                    ('forceExtraction', true),
                    ('analyze', false),
                    ('includeNutrition', False),
                    ('includeTaste', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/extract',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analyzed_recipe_instructions(client):
    """Test case for get_analyzed_recipe_instructions

    Get Analyzed Recipe Instructions
    """
    params = [('stepBreakdown', true)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/analyzedInstructions'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_random_recipes(client):
    """Test case for get_random_recipes

    Get Random Recipes
    """
    params = [('limitLicense', True),
                    ('tags', 'tags_example'),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/random',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recipe_equipment_by_id(client):
    """Test case for get_recipe_equipment_by_id

    Equipment by ID
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/equipmentWidget.json'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recipe_information(client):
    """Test case for get_recipe_information

    Get Recipe Information
    """
    params = [('includeNutrition', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/information'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recipe_information_bulk(client):
    """Test case for get_recipe_information_bulk

    Get Recipe Information Bulk
    """
    params = [('ids', '715538,716429'),
                    ('includeNutrition', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/informationBulk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recipe_ingredients_by_id(client):
    """Test case for get_recipe_ingredients_by_id

    Ingredients by ID
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/ingredientWidget.json'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recipe_nutrition_widget_by_id(client):
    """Test case for get_recipe_nutrition_widget_by_id

    Nutrition by ID
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/nutritionWidget.json'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recipe_price_breakdown_by_id(client):
    """Test case for get_recipe_price_breakdown_by_id

    Price Breakdown by ID
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/priceBreakdownWidget.json'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recipe_taste_by_id(client):
    """Test case for get_recipe_taste_by_id

    Taste by ID
    """
    params = [('normalize', True)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/tasteWidget.json'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_recipes(client):
    """Test case for get_similar_recipes

    Get Similar Recipes
    """
    params = [('number', 10),
                    ('limitLicense', True)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/similar'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_guess_nutrition_by_dish_name(client):
    """Test case for guess_nutrition_by_dish_name

    Guess Nutrition by Dish Name
    """
    params = [('title', 'Spaghetti Aglio et Olio')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/guessNutrition',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ingredients_by_id_image_0(client):
    """Test case for ingredients_by_id_image_0

    Ingredients by ID Image
    """
    params = [('measure', 'metric')]
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/ingredientWidget.png'.format(id=1082038),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_parse_ingredients(client):
    """Test case for parse_ingredients

    Parse Ingredients
    """
    params = [('language', 'en')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/parseIngredients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_breakdown_by_id_image(client):
    """Test case for price_breakdown_by_id_image

    Price Breakdown by ID Image
    """
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/priceBreakdownWidget.png'.format(id=1082038),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quick_answer(client):
    """Test case for quick_answer

    Quick Answer
    """
    params = [('q', 'How much vitamin c is in 2 apples?')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/quickAnswer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_nutrition_by_id_image(client):
    """Test case for recipe_nutrition_by_id_image

    Recipe Nutrition by ID Image
    """
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/nutritionWidget.png'.format(id=1082038),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_nutrition_label_image(client):
    """Test case for recipe_nutrition_label_image

    Recipe Nutrition Label Image
    """
    params = [('showOptionalNutrients', false),
                    ('showZeroValues', false),
                    ('showIngredients', false)]
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/nutritionLabel.png'.format(id=641166),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_nutrition_label_widget(client):
    """Test case for recipe_nutrition_label_widget

    Recipe Nutrition Label Widget
    """
    params = [('defaultCss', True),
                    ('showOptionalNutrients', false),
                    ('showZeroValues', false),
                    ('showIngredients', false)]
    headers = { 
        'Accept': 'text/html',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/nutritionLabel'.format(id=641166),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_taste_by_id_image(client):
    """Test case for recipe_taste_by_id_image

    Recipe Taste by ID Image
    """
    params = [('normalize', false),
                    ('rgb', '75,192,192')]
    headers = { 
        'Accept': 'image/png',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/tasteWidget.png'.format(id=69095),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_recipes(client):
    """Test case for search_recipes

    Search Recipes
    """
    params = [('query', 'burger'),
                    ('cuisine', 'italian'),
                    ('excludeCuisine', 'greek'),
                    ('diet', 'vegetarian'),
                    ('intolerances', 'gluten'),
                    ('equipment', 'pan'),
                    ('includeIngredients', 'tomato,cheese'),
                    ('excludeIngredients', 'eggs'),
                    ('type', 'main course'),
                    ('instructionsRequired', true),
                    ('fillIngredients', false),
                    ('addRecipeInformation', false),
                    ('addRecipeNutrition', false),
                    ('author', 'coffeebean'),
                    ('tags', 'tags_example'),
                    ('recipeBoxId', 2468),
                    ('titleMatch', 'Crock Pot'),
                    ('maxReadyTime', 20),
                    ('ignorePantry', False),
                    ('sort', 'calories'),
                    ('sortDirection', 'asc'),
                    ('minCarbs', 10),
                    ('maxCarbs', 100),
                    ('minProtein', 10),
                    ('maxProtein', 100),
                    ('minCalories', 50),
                    ('maxCalories', 800),
                    ('minFat', 1),
                    ('maxFat', 100),
                    ('minAlcohol', 0),
                    ('maxAlcohol', 100),
                    ('minCaffeine', 0),
                    ('maxCaffeine', 100),
                    ('minCopper', 0),
                    ('maxCopper', 100),
                    ('minCalcium', 0),
                    ('maxCalcium', 100),
                    ('minCholine', 0),
                    ('maxCholine', 100),
                    ('minCholesterol', 0),
                    ('maxCholesterol', 100),
                    ('minFluoride', 0),
                    ('maxFluoride', 100),
                    ('minSaturatedFat', 0),
                    ('maxSaturatedFat', 100),
                    ('minVitaminA', 0),
                    ('maxVitaminA', 100),
                    ('minVitaminC', 0),
                    ('maxVitaminC', 100),
                    ('minVitaminD', 0),
                    ('maxVitaminD', 100),
                    ('minVitaminE', 0),
                    ('maxVitaminE', 100),
                    ('minVitaminK', 0),
                    ('maxVitaminK', 100),
                    ('minVitaminB1', 0),
                    ('maxVitaminB1', 100),
                    ('minVitaminB2', 0),
                    ('maxVitaminB2', 100),
                    ('minVitaminB5', 0),
                    ('maxVitaminB5', 100),
                    ('minVitaminB3', 0),
                    ('maxVitaminB3', 100),
                    ('minVitaminB6', 0),
                    ('maxVitaminB6', 100),
                    ('minVitaminB12', 0),
                    ('maxVitaminB12', 100),
                    ('minFiber', 0),
                    ('maxFiber', 100),
                    ('minFolate', 0),
                    ('maxFolate', 100),
                    ('minFolicAcid', 0),
                    ('maxFolicAcid', 100),
                    ('minIodine', 0),
                    ('maxIodine', 100),
                    ('minIron', 0),
                    ('maxIron', 100),
                    ('minMagnesium', 0),
                    ('maxMagnesium', 100),
                    ('minManganese', 0),
                    ('maxManganese', 100),
                    ('minPhosphorus', 0),
                    ('maxPhosphorus', 100),
                    ('minPotassium', 0),
                    ('maxPotassium', 100),
                    ('minSelenium', 0),
                    ('maxSelenium', 100),
                    ('minSodium', 0),
                    ('maxSodium', 100),
                    ('minSugar', 0),
                    ('maxSugar', 100),
                    ('minZinc', 0),
                    ('maxZinc', 100),
                    ('offset', 56),
                    ('number', 10),
                    ('limitLicense', True)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/complexSearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_recipes_by_ingredients(client):
    """Test case for search_recipes_by_ingredients

    Search Recipes by Ingredients
    """
    params = [('ingredients', 'carrots,tomatoes'),
                    ('number', 10),
                    ('limitLicense', True),
                    ('ranking', 1),
                    ('ignorePantry', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/findByIngredients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_recipes_by_nutrients(client):
    """Test case for search_recipes_by_nutrients

    Search Recipes by Nutrients
    """
    params = [('minCarbs', 10),
                    ('maxCarbs', 100),
                    ('minProtein', 10),
                    ('maxProtein', 100),
                    ('minCalories', 50),
                    ('maxCalories', 800),
                    ('minFat', 1),
                    ('maxFat', 100),
                    ('minAlcohol', 0),
                    ('maxAlcohol', 100),
                    ('minCaffeine', 0),
                    ('maxCaffeine', 100),
                    ('minCopper', 0),
                    ('maxCopper', 100),
                    ('minCalcium', 0),
                    ('maxCalcium', 100),
                    ('minCholine', 0),
                    ('maxCholine', 100),
                    ('minCholesterol', 0),
                    ('maxCholesterol', 100),
                    ('minFluoride', 0),
                    ('maxFluoride', 100),
                    ('minSaturatedFat', 0),
                    ('maxSaturatedFat', 100),
                    ('minVitaminA', 0),
                    ('maxVitaminA', 100),
                    ('minVitaminC', 0),
                    ('maxVitaminC', 100),
                    ('minVitaminD', 0),
                    ('maxVitaminD', 100),
                    ('minVitaminE', 0),
                    ('maxVitaminE', 100),
                    ('minVitaminK', 0),
                    ('maxVitaminK', 100),
                    ('minVitaminB1', 0),
                    ('maxVitaminB1', 100),
                    ('minVitaminB2', 0),
                    ('maxVitaminB2', 100),
                    ('minVitaminB5', 0),
                    ('maxVitaminB5', 100),
                    ('minVitaminB3', 0),
                    ('maxVitaminB3', 100),
                    ('minVitaminB6', 0),
                    ('maxVitaminB6', 100),
                    ('minVitaminB12', 0),
                    ('maxVitaminB12', 100),
                    ('minFiber', 0),
                    ('maxFiber', 100),
                    ('minFolate', 0),
                    ('maxFolate', 100),
                    ('minFolicAcid', 0),
                    ('maxFolicAcid', 100),
                    ('minIodine', 0),
                    ('maxIodine', 100),
                    ('minIron', 0),
                    ('maxIron', 100),
                    ('minMagnesium', 0),
                    ('maxMagnesium', 100),
                    ('minManganese', 0),
                    ('maxManganese', 100),
                    ('minPhosphorus', 0),
                    ('maxPhosphorus', 100),
                    ('minPotassium', 0),
                    ('maxPotassium', 100),
                    ('minSelenium', 0),
                    ('maxSelenium', 100),
                    ('minSodium', 0),
                    ('maxSodium', 100),
                    ('minSugar', 0),
                    ('maxSugar', 100),
                    ('minZinc', 0),
                    ('maxZinc', 100),
                    ('offset', 56),
                    ('number', 10),
                    ('random', false),
                    ('limitLicense', True)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/findByNutrients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_summarize_recipe(client):
    """Test case for summarize_recipe

    Summarize Recipe
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/summary'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_visualize_equipment(client):
    """Test case for visualize_equipment

    Equipment Widget
    """
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/visualizeEquipment',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_visualize_price_breakdown(client):
    """Test case for visualize_price_breakdown

    Price Breakdown Widget
    """
    params = [('language', 'en')]
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/visualizePriceEstimator',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_visualize_recipe_equipment_by_id(client):
    """Test case for visualize_recipe_equipment_by_id

    Equipment by ID Widget
    """
    params = [('defaultCss', True)]
    headers = { 
        'Accept': 'text/html',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/equipmentWidget'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_visualize_recipe_ingredients_by_id(client):
    """Test case for visualize_recipe_ingredients_by_id

    Ingredients by ID Widget
    """
    params = [('defaultCss', True),
                    ('measure', 'metric')]
    headers = { 
        'Accept': 'text/html',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/ingredientWidget'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_visualize_recipe_nutrition(client):
    """Test case for visualize_recipe_nutrition

    Recipe Nutrition Widget
    """
    params = [('language', 'en')]
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/visualizeNutrition',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_visualize_recipe_nutrition_by_id(client):
    """Test case for visualize_recipe_nutrition_by_id

    Recipe Nutrition by ID Widget
    """
    params = [('defaultCss', True)]
    headers = { 
        'Accept': 'text/html',
        'accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/nutritionWidget'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_visualize_recipe_price_breakdown_by_id(client):
    """Test case for visualize_recipe_price_breakdown_by_id

    Price Breakdown by ID Widget
    """
    params = [('defaultCss', True)]
    headers = { 
        'Accept': 'text/html',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/priceBreakdownWidget'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_visualize_recipe_taste(client):
    """Test case for visualize_recipe_taste

    Recipe Taste Widget
    """
    params = [('language', 'en'),
                    ('normalize', True),
                    ('rgb', '75,192,192')]
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/json',
        'accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recipes/visualizeTaste',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_visualize_recipe_taste_by_id(client):
    """Test case for visualize_recipe_taste_by_id

    Recipe Taste by ID Widget
    """
    params = [('normalize', True),
                    ('rgb', '75,192,192')]
    headers = { 
        'Accept': 'text/html',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipes/{id}/tasteWidget'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

