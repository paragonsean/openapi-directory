# 1000000RecipeAndGroceryListApiV2.RecipeApi

All URIs are relative to *https://api2.bigoven.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recipeAutoComplete**](RecipeApi.md#recipeAutoComplete) | **GET** /recipe/autocomplete | Given a query, return recipe titles starting with query. Query must be at least 3 chars in length.
[**recipeAutoCompleteAllRecipes**](RecipeApi.md#recipeAutoCompleteAllRecipes) | **GET** /recipe/autocomplete/all | Automatics the complete all recipes.
[**recipeAutoCompleteMyRecipes**](RecipeApi.md#recipeAutoCompleteMyRecipes) | **GET** /recipe/autocomplete/mine | Automatics the complete my recipes.
[**recipeCategories**](RecipeApi.md#recipeCategories) | **GET** /recipe/categories | Get a list of recipe categories (the ID field can be used for include_cat in search parameters)
[**recipeDelete**](RecipeApi.md#recipeDelete) | **DELETE** /recipe/{id} | Delete a Recipe (you must be authenticated as an owner of the recipe)
[**recipeFeedback**](RecipeApi.md#recipeFeedback) | **POST** /recipe/{recipeId}/feedback | Feedback on a Recipe -- for internal BigOven editors
[**recipeGet**](RecipeApi.md#recipeGet) | **GET** /recipe/{id} | Return full Recipe detail. Returns 403 if the recipe is owned by someone else.
[**recipeGetActiveRecipe**](RecipeApi.md#recipeGetActiveRecipe) | **GET** /recipe/get/active/recipe | Returns last active recipe for the user
[**recipeGetRandomRecipe**](RecipeApi.md#recipeGetRandomRecipe) | **GET** /recipes/random | Get a random, home-page-quality Recipe.
[**recipeGetRecipeWithSteps**](RecipeApi.md#recipeGetRecipeWithSteps) | **GET** /recipe/steps/{id} | Return full Recipe detail with steps. Returns 403 if the recipe is owned by someone else.
[**recipeGetStep**](RecipeApi.md#recipeGetStep) | **POST** /recipe/get/saved/step | Gets recipe single step as text
[**recipeGetStepNumber**](RecipeApi.md#recipeGetStepNumber) | **POST** /recipe/get/step/number | Returns stored step number and number of steps in recipe
[**recipeGetSteps**](RecipeApi.md#recipeGetSteps) | **POST** /recipe/post/step | Stores recipe step number and returns saved step data
[**recipeGetV2**](RecipeApi.md#recipeGetV2) | **GET** /recipes/{id} | Same as GET recipe but also includes the recipe videos (if any)
[**recipePost**](RecipeApi.md#recipePost) | **POST** /recipe | Add a new recipe
[**recipePut**](RecipeApi.md#recipePut) | **PUT** /recipe | Update a recipe
[**recipeRaves**](RecipeApi.md#recipeRaves) | **GET** /recipes/raves | Get the recipe/comment tuples for those recipes with 4 or 5 star ratings
[**recipeRecentViews**](RecipeApi.md#recipeRecentViews) | **GET** /recipes/recentviews | Get a list of recipes that the authenticated user has most recently viewed
[**recipeRecipeSearch**](RecipeApi.md#recipeRecipeSearch) | **GET** /recipes | Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection
[**recipeRecipeSearchRandom**](RecipeApi.md#recipeRecipeSearchRandom) | **GET** /recipes/top25random | Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection
[**recipeRelated**](RecipeApi.md#recipeRelated) | **GET** /recipe/{recipeId}/related | Get recipes related to the given recipeId
[**recipeScan**](RecipeApi.md#recipeScan) | **POST** /recipe/scan | POST an image as a new RecipeScan request                  1)  Fetch the filename -- DONE                  2)  Copy it to the pics/scan folder - ENSURE NO NAMING COLLISIONS -- DONE                  3)  Create 120 thumbnail size  in pics/scan/120 -- DONE                  4)  Insert the CloudTasks record                  5)  Create the HIT                  6)  Update the CloudTasks record with the HIT ID                  7)  Email the requesing user                  8)  Call out to www.bigoven.com to fetch the image and re-create the thumbnail
[**recipeZapRecipe**](RecipeApi.md#recipeZapRecipe) | **GET** /recipe/{id}/zap | Zaps the recipe.



## recipeAutoComplete

> [String] recipeAutoComplete(query, opts)

Given a query, return recipe titles starting with query. Query must be at least 3 chars in length.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let query = "query_example"; // String | 
let opts = {
  'limit': 56 // Number | 
};
apiInstance.recipeAutoComplete(query, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**|  | 
 **limit** | **Number**|  | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeAutoCompleteAllRecipes

> [BigOvenModelRecipeInfoTiny] recipeAutoCompleteAllRecipes(query, limit)

Automatics the complete all recipes.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let query = "query_example"; // String | The query.
let limit = 56; // Number | The limit.
apiInstance.recipeAutoCompleteAllRecipes(query, limit, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| The query. | 
 **limit** | **Number**| The limit. | 

### Return type

[**[BigOvenModelRecipeInfoTiny]**](BigOvenModelRecipeInfoTiny.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeAutoCompleteMyRecipes

> [BigOvenModelRecipeInfoTiny] recipeAutoCompleteMyRecipes(query, limit)

Automatics the complete my recipes.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let query = "query_example"; // String | The query.
let limit = 56; // Number | The limit.
apiInstance.recipeAutoCompleteMyRecipes(query, limit, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| The query. | 
 **limit** | **Number**| The limit. | 

### Return type

[**[BigOvenModelRecipeInfoTiny]**](BigOvenModelRecipeInfoTiny.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeCategories

> [BigOvenModelRecipeCategory] recipeCategories()

Get a list of recipe categories (the ID field can be used for include_cat in search parameters)

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
apiInstance.recipeCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[BigOvenModelRecipeCategory]**](BigOvenModelRecipeCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeDelete

> Object recipeDelete(id)

Delete a Recipe (you must be authenticated as an owner of the recipe)

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let id = 56; // Number | 
apiInstance.recipeDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeFeedback

> Object recipeFeedback(recipeId, aPI2ModelsRecipesFeedbackDTO)

Feedback on a Recipe -- for internal BigOven editors

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let recipeId = 56; // Number | 
let aPI2ModelsRecipesFeedbackDTO = new 1000000RecipeAndGroceryListApiV2.API2ModelsRecipesFeedbackDTO(); // API2ModelsRecipesFeedbackDTO | The payload for feedback, which includes the field \"feedback\"
apiInstance.recipeFeedback(recipeId, aPI2ModelsRecipesFeedbackDTO, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipeId** | **Number**|  | 
 **aPI2ModelsRecipesFeedbackDTO** | [**API2ModelsRecipesFeedbackDTO**](API2ModelsRecipesFeedbackDTO.md)| The payload for feedback, which includes the field \&quot;feedback\&quot; | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeGet

> BigOvenModelAPI2Recipe recipeGet(id, opts)

Return full Recipe detail. Returns 403 if the recipe is owned by someone else.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let id = 56; // Number | The Recipe ID to retrieve
let opts = {
  'prefetch': true // Boolean | The prefetch.
};
apiInstance.recipeGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The Recipe ID to retrieve | 
 **prefetch** | **Boolean**| The prefetch. | [optional] 

### Return type

[**BigOvenModelAPI2Recipe**](BigOvenModelAPI2Recipe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeGetActiveRecipe

> BigOvenResult recipeGetActiveRecipe(userName)

Returns last active recipe for the user

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let userName = "userName_example"; // String | 
apiInstance.recipeGetActiveRecipe(userName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userName** | **String**|  | 

### Return type

[**BigOvenResult**](BigOvenResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeGetRandomRecipe

> BigOvenModelAPIRecipe recipeGetRandomRecipe()

Get a random, home-page-quality Recipe.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
apiInstance.recipeGetRandomRecipe((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeGetRecipeWithSteps

> BigOvenModelAPI2Recipe recipeGetRecipeWithSteps(id, opts)

Return full Recipe detail with steps. Returns 403 if the recipe is owned by someone else.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let id = 56; // Number | the Recipe ID to retrieve
let opts = {
  'prefetch': true // Boolean | 
};
apiInstance.recipeGetRecipeWithSteps(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the Recipe ID to retrieve | 
 **prefetch** | **Boolean**|  | [optional] 

### Return type

[**BigOvenModelAPI2Recipe**](BigOvenModelAPI2Recipe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeGetStep

> String recipeGetStep(userName, recipeId, stepId)

Gets recipe single step as text

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let userName = "userName_example"; // String | 
let recipeId = 56; // Number | 
let stepId = 56; // Number | 
apiInstance.recipeGetStep(userName, recipeId, stepId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userName** | **String**|  | 
 **recipeId** | **Number**|  | 
 **stepId** | **Number**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeGetStepNumber

> API2Result recipeGetStepNumber(userName, recipeId)

Returns stored step number and number of steps in recipe

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let userName = "userName_example"; // String | 
let recipeId = 56; // Number | 
apiInstance.recipeGetStepNumber(userName, recipeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userName** | **String**|  | 
 **recipeId** | **Number**|  | 

### Return type

[**API2Result**](API2Result.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeGetSteps

> BigOvenResult recipeGetSteps(userName, recipeId, stepId)

Stores recipe step number and returns saved step data

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let userName = "userName_example"; // String | 
let recipeId = 56; // Number | 
let stepId = 56; // Number | 
apiInstance.recipeGetSteps(userName, recipeId, stepId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userName** | **String**|  | 
 **recipeId** | **Number**|  | 
 **stepId** | **Number**|  | 

### Return type

[**BigOvenResult**](BigOvenResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeGetV2

> API2ModelsRecipesRecipeResponse recipeGetV2(id, opts)

Same as GET recipe but also includes the recipe videos (if any)

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let id = 56; // Number | The Recipe ID to retrieve
let opts = {
  'prefetch': true // Boolean | The prefetch.
};
apiInstance.recipeGetV2(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The Recipe ID to retrieve | 
 **prefetch** | **Boolean**| The prefetch. | [optional] 

### Return type

[**API2ModelsRecipesRecipeResponse**](API2ModelsRecipesRecipeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipePost

> BigOvenModelAPIRecipe recipePost(bigOvenModelAPIRecipe)

Add a new recipe

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let bigOvenModelAPIRecipe = new 1000000RecipeAndGroceryListApiV2.BigOvenModelAPIRecipe(); // BigOvenModelAPIRecipe | 
apiInstance.recipePost(bigOvenModelAPIRecipe, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bigOvenModelAPIRecipe** | [**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)|  | 

### Return type

[**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## recipePut

> BigOvenModelAPIRecipe recipePut(bigOvenModelAPIRecipe)

Update a recipe

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let bigOvenModelAPIRecipe = new 1000000RecipeAndGroceryListApiV2.BigOvenModelAPIRecipe(); // BigOvenModelAPIRecipe | 
apiInstance.recipePut(bigOvenModelAPIRecipe, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bigOvenModelAPIRecipe** | [**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)|  | 

### Return type

[**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeRaves

> [BigOvenModelRecipeInfoReviewTuple2] recipeRaves(opts)

Get the recipe/comment tuples for those recipes with 4 or 5 star ratings

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let opts = {
  'pg': 56, // Number | page, starting with 1
  'rpp': 56 // Number | results per page
};
apiInstance.recipeRaves(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pg** | **Number**| page, starting with 1 | [optional] 
 **rpp** | **Number**| results per page | [optional] 

### Return type

[**[BigOvenModelRecipeInfoReviewTuple2]**](BigOvenModelRecipeInfoReviewTuple2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeRecentViews

> [BigOvenModelRecipeInfoDateTuple2] recipeRecentViews(opts)

Get a list of recipes that the authenticated user has most recently viewed

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let opts = {
  'pg': 56, // Number | Page number starting with 1
  'rpp': 56 // Number | results per page
};
apiInstance.recipeRecentViews(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pg** | **Number**| Page number starting with 1 | [optional] 
 **rpp** | **Number**| results per page | [optional] 

### Return type

[**[BigOvenModelRecipeInfoDateTuple2]**](BigOvenModelRecipeInfoDateTuple2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeRecipeSearch

> BigOvenModelAPI2RecipeSearchResult recipeRecipeSearch(opts)

Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let opts = {
  'anyKw': "anyKw_example", // String | Search anywhere in the recipe for the keyword
  'folder': "folder_example", // String | Search in a specific folder name for the authenticated user
  'coll': 56, // Number | Limit to a collection ID number
  'filter': "filter_example", // String | optionally set to either \"myrecipes\", \"try\", \"favorites\",\"added\" to filter to just the authenticated user's recipe set
  'titleKw': "titleKw_example", // String | Search just in the recipe title for the keyword
  'userId': 56, // Number | Set the target userid to search their public recipes
  'username': "username_example", // String | Set the target username to search their public recipes
  'token': "token_example", // String | 
  'photos': true, // Boolean | if set to true, limit search results to photos only
  'boostmine': true, // Boolean | if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders)
  'includeCat': "includeCat_example", // String | integer of the subcategory you'd like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \"Main Dish &gt; Casseroles\".
  'excludeCat': "excludeCat_example", // String | like include_cat, set this to an integer to exclude a specific category
  'includePrimarycat': "includePrimarycat_example", // String | csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
  'excludePrimarycat': "excludePrimarycat_example", // String | csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
  'includeIng': "includeIng_example", // String | A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken
  'excludeIng': "excludeIng_example", // String | A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required)
  'cuisine': "cuisine_example", // String | Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese
  'db': "db_example", // String | 
  'userset': "userset_example", // String | If set to a given username, it'll force the search to filter to just that username
  'servingsMin': 3.4, // Number | Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \"dozen\", etc. This parameter simply specifies the minimum number for that value entered in \"yield.\"
  'totalMins': 56, // Number | Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \"1 hour, 15 minutes\" to 75 before passing in.)
  'maxIngredients': 56, // Number | Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less
  'minIngredients': 56, // Number | Optional. If supplied, will restrict results to recipes that have at least {minIngredients}
  'rpp': 56, // Number | integer; results per page
  'pg': 56, // Number | integer: the page number
  'vtn': 56, // Number | when set to 1, limit to vegetarian (Powersearch-capable plan required)
  'vgn': 56, // Number | when set to 1, limit to vegan (Powersearch-capable plan required)
  'chs': 56, // Number | when set to 1, limit to contains-cheese (Powersearch-capable plan required)
  'glf': 56, // Number | when set to 1, limit to gluten-free (Powersearch-capable plan required)
  'ntf': 56, // Number | when set to 1, limit to nut-free (Powersearch-capable plan required)
  'dyf': 56, // Number | when set to 1, limit to dairy-free (Powersearch-capable plan required)
  'sff': 56, // Number | when set to 1, limit to seafood-free (Powersearch-capable plan required)
  'slf': 56, // Number | when set to 1, limit to shellfish-free (Powersearch-capable plan required)
  'tnf': 56, // Number | when set to 1, limit to tree-nut free (Powersearch-capable plan required)
  'wmf': 56, // Number | when set to 1, limit to white-meat free (Powersearch-capable plan required)
  'rmf': 56, // Number | when set to 1, limit to red-meat free (Powersearch-capable plan required)
  'cps': 56, // Number | when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required)
  'champion': 56, // Number | optional. When set to 1, this will limit search results to \"best of\" recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don't include this parameter.
  'synonyms': true // Boolean | optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon)
};
apiInstance.recipeRecipeSearch(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyKw** | **String**| Search anywhere in the recipe for the keyword | [optional] 
 **folder** | **String**| Search in a specific folder name for the authenticated user | [optional] 
 **coll** | **Number**| Limit to a collection ID number | [optional] 
 **filter** | **String**| optionally set to either \&quot;myrecipes\&quot;, \&quot;try\&quot;, \&quot;favorites\&quot;,\&quot;added\&quot; to filter to just the authenticated user&#39;s recipe set | [optional] 
 **titleKw** | **String**| Search just in the recipe title for the keyword | [optional] 
 **userId** | **Number**| Set the target userid to search their public recipes | [optional] 
 **username** | **String**| Set the target username to search their public recipes | [optional] 
 **token** | **String**|  | [optional] 
 **photos** | **Boolean**| if set to true, limit search results to photos only | [optional] 
 **boostmine** | **Boolean**| if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders) | [optional] 
 **includeCat** | **String**| integer of the subcategory you&#39;d like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \&quot;Main Dish &amp;gt; Casseroles\&quot;. | [optional] 
 **excludeCat** | **String**| like include_cat, set this to an integer to exclude a specific category | [optional] 
 **includePrimarycat** | **String**| csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other] | [optional] 
 **excludePrimarycat** | **String**| csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other] | [optional] 
 **includeIng** | **String**| A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken | [optional] 
 **excludeIng** | **String**| A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required) | [optional] 
 **cuisine** | **String**| Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese | [optional] 
 **db** | **String**|  | [optional] 
 **userset** | **String**| If set to a given username, it&#39;ll force the search to filter to just that username | [optional] 
 **servingsMin** | **Number**| Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \&quot;dozen\&quot;, etc. This parameter simply specifies the minimum number for that value entered in \&quot;yield.\&quot; | [optional] 
 **totalMins** | **Number**| Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \&quot;1 hour, 15 minutes\&quot; to 75 before passing in.) | [optional] 
 **maxIngredients** | **Number**| Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less | [optional] 
 **minIngredients** | **Number**| Optional. If supplied, will restrict results to recipes that have at least {minIngredients} | [optional] 
 **rpp** | **Number**| integer; results per page | [optional] 
 **pg** | **Number**| integer: the page number | [optional] 
 **vtn** | **Number**| when set to 1, limit to vegetarian (Powersearch-capable plan required) | [optional] 
 **vgn** | **Number**| when set to 1, limit to vegan (Powersearch-capable plan required) | [optional] 
 **chs** | **Number**| when set to 1, limit to contains-cheese (Powersearch-capable plan required) | [optional] 
 **glf** | **Number**| when set to 1, limit to gluten-free (Powersearch-capable plan required) | [optional] 
 **ntf** | **Number**| when set to 1, limit to nut-free (Powersearch-capable plan required) | [optional] 
 **dyf** | **Number**| when set to 1, limit to dairy-free (Powersearch-capable plan required) | [optional] 
 **sff** | **Number**| when set to 1, limit to seafood-free (Powersearch-capable plan required) | [optional] 
 **slf** | **Number**| when set to 1, limit to shellfish-free (Powersearch-capable plan required) | [optional] 
 **tnf** | **Number**| when set to 1, limit to tree-nut free (Powersearch-capable plan required) | [optional] 
 **wmf** | **Number**| when set to 1, limit to white-meat free (Powersearch-capable plan required) | [optional] 
 **rmf** | **Number**| when set to 1, limit to red-meat free (Powersearch-capable plan required) | [optional] 
 **cps** | **Number**| when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required) | [optional] 
 **champion** | **Number**| optional. When set to 1, this will limit search results to \&quot;best of\&quot; recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don&#39;t include this parameter. | [optional] 
 **synonyms** | **Boolean**| optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon) | [optional] 

### Return type

[**BigOvenModelAPI2RecipeSearchResult**](BigOvenModelAPI2RecipeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeRecipeSearchRandom

> BigOvenModelAPI2RecipeSearchResult recipeRecipeSearchRandom(opts)

Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let opts = {
  'anyKw': "anyKw_example", // String | Search anywhere in the recipe for the keyword
  'folder': "folder_example", // String | Search in a specific folder name for the authenticated user
  'coll': 56, // Number | Limit to a collection ID number
  'filter': "filter_example", // String | optionally set to either \"myrecipes\", \"try\", \"favorites\",\"added\" to filter to just the authenticated user's recipe set
  'titleKw': "titleKw_example", // String | Search just in the recipe title for the keyword
  'userId': 56, // Number | Set the target userid to search their public recipes
  'username': "username_example", // String | Set the target username to search their public recipes
  'token': "token_example", // String | 
  'photos': true, // Boolean | if set to true, limit search results to photos only
  'boostmine': true, // Boolean | if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders)
  'includeCat': "includeCat_example", // String | integer of the subcategory you'd like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \"Main Dish &gt; Casseroles\".
  'excludeCat': "excludeCat_example", // String | like include_cat, set this to an integer to exclude a specific category
  'includePrimarycat': "includePrimarycat_example", // String | csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
  'excludePrimarycat': "excludePrimarycat_example", // String | csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
  'includeIng': "includeIng_example", // String | A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken
  'excludeIng': "excludeIng_example", // String | A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required)
  'cuisine': "cuisine_example", // String | Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese
  'db': "db_example", // String | 
  'userset': "userset_example", // String | If set to a given username, it'll force the search to filter to just that username
  'servingsMin': 3.4, // Number | Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \"dozen\", etc. This parameter simply specifies the minimum number for that value entered in \"yield.\"
  'totalMins': 56, // Number | Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \"1 hour, 15 minutes\" to 75 before passing in.)
  'maxIngredients': 56, // Number | Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less
  'minIngredients': 56, // Number | Optional. If supplied, will restrict results to recipes that have at least {minIngredients}
  'vtn': 56, // Number | when set to 1, limit to vegetarian (Powersearch-capable plan required)
  'vgn': 56, // Number | when set to 1, limit to vegan (Powersearch-capable plan required)
  'chs': 56, // Number | when set to 1, limit to contains-cheese (Powersearch-capable plan required)
  'glf': 56, // Number | when set to 1, limit to gluten-free (Powersearch-capable plan required)
  'ntf': 56, // Number | when set to 1, limit to nut-free (Powersearch-capable plan required)
  'dyf': 56, // Number | when set to 1, limit to dairy-free (Powersearch-capable plan required)
  'sff': 56, // Number | when set to 1, limit to seafood-free (Powersearch-capable plan required)
  'slf': 56, // Number | when set to 1, limit to shellfish-free (Powersearch-capable plan required)
  'tnf': 56, // Number | when set to 1, limit to tree-nut free (Powersearch-capable plan required)
  'wmf': 56, // Number | when set to 1, limit to white-meat free (Powersearch-capable plan required)
  'rmf': 56, // Number | when set to 1, limit to red-meat free (Powersearch-capable plan required)
  'cps': 56, // Number | when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required)
  'champion': 56, // Number | optional. When set to 1, this will limit search results to \"best of\" recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don't include this parameter.
  'synonyms': true // Boolean | optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon)
};
apiInstance.recipeRecipeSearchRandom(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyKw** | **String**| Search anywhere in the recipe for the keyword | [optional] 
 **folder** | **String**| Search in a specific folder name for the authenticated user | [optional] 
 **coll** | **Number**| Limit to a collection ID number | [optional] 
 **filter** | **String**| optionally set to either \&quot;myrecipes\&quot;, \&quot;try\&quot;, \&quot;favorites\&quot;,\&quot;added\&quot; to filter to just the authenticated user&#39;s recipe set | [optional] 
 **titleKw** | **String**| Search just in the recipe title for the keyword | [optional] 
 **userId** | **Number**| Set the target userid to search their public recipes | [optional] 
 **username** | **String**| Set the target username to search their public recipes | [optional] 
 **token** | **String**|  | [optional] 
 **photos** | **Boolean**| if set to true, limit search results to photos only | [optional] 
 **boostmine** | **Boolean**| if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders) | [optional] 
 **includeCat** | **String**| integer of the subcategory you&#39;d like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \&quot;Main Dish &amp;gt; Casseroles\&quot;. | [optional] 
 **excludeCat** | **String**| like include_cat, set this to an integer to exclude a specific category | [optional] 
 **includePrimarycat** | **String**| csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other] | [optional] 
 **excludePrimarycat** | **String**| csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other] | [optional] 
 **includeIng** | **String**| A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken | [optional] 
 **excludeIng** | **String**| A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required) | [optional] 
 **cuisine** | **String**| Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese | [optional] 
 **db** | **String**|  | [optional] 
 **userset** | **String**| If set to a given username, it&#39;ll force the search to filter to just that username | [optional] 
 **servingsMin** | **Number**| Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \&quot;dozen\&quot;, etc. This parameter simply specifies the minimum number for that value entered in \&quot;yield.\&quot; | [optional] 
 **totalMins** | **Number**| Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \&quot;1 hour, 15 minutes\&quot; to 75 before passing in.) | [optional] 
 **maxIngredients** | **Number**| Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less | [optional] 
 **minIngredients** | **Number**| Optional. If supplied, will restrict results to recipes that have at least {minIngredients} | [optional] 
 **vtn** | **Number**| when set to 1, limit to vegetarian (Powersearch-capable plan required) | [optional] 
 **vgn** | **Number**| when set to 1, limit to vegan (Powersearch-capable plan required) | [optional] 
 **chs** | **Number**| when set to 1, limit to contains-cheese (Powersearch-capable plan required) | [optional] 
 **glf** | **Number**| when set to 1, limit to gluten-free (Powersearch-capable plan required) | [optional] 
 **ntf** | **Number**| when set to 1, limit to nut-free (Powersearch-capable plan required) | [optional] 
 **dyf** | **Number**| when set to 1, limit to dairy-free (Powersearch-capable plan required) | [optional] 
 **sff** | **Number**| when set to 1, limit to seafood-free (Powersearch-capable plan required) | [optional] 
 **slf** | **Number**| when set to 1, limit to shellfish-free (Powersearch-capable plan required) | [optional] 
 **tnf** | **Number**| when set to 1, limit to tree-nut free (Powersearch-capable plan required) | [optional] 
 **wmf** | **Number**| when set to 1, limit to white-meat free (Powersearch-capable plan required) | [optional] 
 **rmf** | **Number**| when set to 1, limit to red-meat free (Powersearch-capable plan required) | [optional] 
 **cps** | **Number**| when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required) | [optional] 
 **champion** | **Number**| optional. When set to 1, this will limit search results to \&quot;best of\&quot; recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don&#39;t include this parameter. | [optional] 
 **synonyms** | **Boolean**| optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon) | [optional] 

### Return type

[**BigOvenModelAPI2RecipeSearchResult**](BigOvenModelAPI2RecipeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeRelated

> BigOvenModelAPI2RecipeSearchResult recipeRelated(recipeId, opts)

Get recipes related to the given recipeId

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let recipeId = 56; // Number | The recipe id
let opts = {
  'pg': 56, // Number | The page
  'rpp': 56 // Number | The results per page
};
apiInstance.recipeRelated(recipeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipeId** | **Number**| The recipe id | 
 **pg** | **Number**| The page | [optional] 
 **rpp** | **Number**| The results per page | [optional] 

### Return type

[**BigOvenModelAPI2RecipeSearchResult**](BigOvenModelAPI2RecipeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeScan

> recipeScan(opts)

POST an image as a new RecipeScan request                  1)  Fetch the filename -- DONE                  2)  Copy it to the pics/scan folder - ENSURE NO NAMING COLLISIONS -- DONE                  3)  Create 120 thumbnail size  in pics/scan/120 -- DONE                  4)  Insert the CloudTasks record                  5)  Create the HIT                  6)  Update the CloudTasks record with the HIT ID                  7)  Email the requesing user                  8)  Call out to www.bigoven.com to fetch the image and re-create the thumbnail

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let opts = {
  'test': true, // Boolean | 
  'devicetype': "devicetype_example", // String | 
  'lat': 3.4, // Number | 
  'lng': 3.4 // Number | 
};
apiInstance.recipeScan(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test** | **Boolean**|  | [optional] 
 **devicetype** | **String**|  | [optional] 
 **lat** | **Number**|  | [optional] 
 **lng** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## recipeZapRecipe

> Object recipeZapRecipe(id)

Zaps the recipe.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.RecipeApi();
let id = 56; // Number | The identifier.
apiInstance.recipeZapRecipe(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The identifier. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

