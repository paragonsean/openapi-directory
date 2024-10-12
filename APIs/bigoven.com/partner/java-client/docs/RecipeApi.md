# RecipeApi

All URIs are relative to *https://api2.bigoven.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recipeAutoComplete**](RecipeApi.md#recipeAutoComplete) | **GET** /recipe/autocomplete | Given a query, return recipe titles starting with query. Query must be at least 3 chars in length. |
| [**recipeAutoCompleteAllRecipes**](RecipeApi.md#recipeAutoCompleteAllRecipes) | **GET** /recipe/autocomplete/all | Automatics the complete all recipes. |
| [**recipeAutoCompleteMyRecipes**](RecipeApi.md#recipeAutoCompleteMyRecipes) | **GET** /recipe/autocomplete/mine | Automatics the complete my recipes. |
| [**recipeCategories**](RecipeApi.md#recipeCategories) | **GET** /recipe/categories | Get a list of recipe categories (the ID field can be used for include_cat in search parameters) |
| [**recipeDelete**](RecipeApi.md#recipeDelete) | **DELETE** /recipe/{id} | Delete a Recipe (you must be authenticated as an owner of the recipe) |
| [**recipeFeedback**](RecipeApi.md#recipeFeedback) | **POST** /recipe/{recipeId}/feedback | Feedback on a Recipe -- for internal BigOven editors |
| [**recipeGet**](RecipeApi.md#recipeGet) | **GET** /recipe/{id} | Return full Recipe detail. Returns 403 if the recipe is owned by someone else. |
| [**recipeGetActiveRecipe**](RecipeApi.md#recipeGetActiveRecipe) | **GET** /recipe/get/active/recipe | Returns last active recipe for the user |
| [**recipeGetRandomRecipe**](RecipeApi.md#recipeGetRandomRecipe) | **GET** /recipes/random | Get a random, home-page-quality Recipe. |
| [**recipeGetRecipeWithSteps**](RecipeApi.md#recipeGetRecipeWithSteps) | **GET** /recipe/steps/{id} | Return full Recipe detail with steps. Returns 403 if the recipe is owned by someone else. |
| [**recipeGetStep**](RecipeApi.md#recipeGetStep) | **POST** /recipe/get/saved/step | Gets recipe single step as text |
| [**recipeGetStepNumber**](RecipeApi.md#recipeGetStepNumber) | **POST** /recipe/get/step/number | Returns stored step number and number of steps in recipe |
| [**recipeGetSteps**](RecipeApi.md#recipeGetSteps) | **POST** /recipe/post/step | Stores recipe step number and returns saved step data |
| [**recipeGetV2**](RecipeApi.md#recipeGetV2) | **GET** /recipes/{id} | Same as GET recipe but also includes the recipe videos (if any) |
| [**recipePost**](RecipeApi.md#recipePost) | **POST** /recipe | Add a new recipe |
| [**recipePut**](RecipeApi.md#recipePut) | **PUT** /recipe | Update a recipe |
| [**recipeRaves**](RecipeApi.md#recipeRaves) | **GET** /recipes/raves | Get the recipe/comment tuples for those recipes with 4 or 5 star ratings |
| [**recipeRecentViews**](RecipeApi.md#recipeRecentViews) | **GET** /recipes/recentviews | Get a list of recipes that the authenticated user has most recently viewed |
| [**recipeRecipeSearch**](RecipeApi.md#recipeRecipeSearch) | **GET** /recipes | Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection |
| [**recipeRecipeSearchRandom**](RecipeApi.md#recipeRecipeSearchRandom) | **GET** /recipes/top25random | Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection |
| [**recipeRelated**](RecipeApi.md#recipeRelated) | **GET** /recipe/{recipeId}/related | Get recipes related to the given recipeId |
| [**recipeScan**](RecipeApi.md#recipeScan) | **POST** /recipe/scan | POST an image as a new RecipeScan request                  1)  Fetch the filename -- DONE                  2)  Copy it to the pics/scan folder - ENSURE NO NAMING COLLISIONS -- DONE                  3)  Create 120 thumbnail size  in pics/scan/120 -- DONE                  4)  Insert the CloudTasks record                  5)  Create the HIT                  6)  Update the CloudTasks record with the HIT ID                  7)  Email the requesing user                  8)  Call out to www.bigoven.com to fetch the image and re-create the thumbnail |
| [**recipeZapRecipe**](RecipeApi.md#recipeZapRecipe) | **GET** /recipe/{id}/zap | Zaps the recipe. |


<a id="recipeAutoComplete"></a>
# **recipeAutoComplete**
> List&lt;String&gt; recipeAutoComplete(query, limit)

Given a query, return recipe titles starting with query. Query must be at least 3 chars in length.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String query = "query_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      List<String> result = apiInstance.recipeAutoComplete(query, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeAutoComplete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**|  | |
| **limit** | **Integer**|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeAutoCompleteAllRecipes"></a>
# **recipeAutoCompleteAllRecipes**
> List&lt;BigOvenModelRecipeInfoTiny&gt; recipeAutoCompleteAllRecipes(query, limit)

Automatics the complete all recipes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String query = "query_example"; // String | The query.
    Integer limit = 56; // Integer | The limit.
    try {
      List<BigOvenModelRecipeInfoTiny> result = apiInstance.recipeAutoCompleteAllRecipes(query, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeAutoCompleteAllRecipes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| The query. | |
| **limit** | **Integer**| The limit. | |

### Return type

[**List&lt;BigOvenModelRecipeInfoTiny&gt;**](BigOvenModelRecipeInfoTiny.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeAutoCompleteMyRecipes"></a>
# **recipeAutoCompleteMyRecipes**
> List&lt;BigOvenModelRecipeInfoTiny&gt; recipeAutoCompleteMyRecipes(query, limit)

Automatics the complete my recipes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String query = "query_example"; // String | The query.
    Integer limit = 56; // Integer | The limit.
    try {
      List<BigOvenModelRecipeInfoTiny> result = apiInstance.recipeAutoCompleteMyRecipes(query, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeAutoCompleteMyRecipes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| The query. | |
| **limit** | **Integer**| The limit. | |

### Return type

[**List&lt;BigOvenModelRecipeInfoTiny&gt;**](BigOvenModelRecipeInfoTiny.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeCategories"></a>
# **recipeCategories**
> List&lt;BigOvenModelRecipeCategory&gt; recipeCategories()

Get a list of recipe categories (the ID field can be used for include_cat in search parameters)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    try {
      List<BigOvenModelRecipeCategory> result = apiInstance.recipeCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;BigOvenModelRecipeCategory&gt;**](BigOvenModelRecipeCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeDelete"></a>
# **recipeDelete**
> Object recipeDelete(id)

Delete a Recipe (you must be authenticated as an owner of the recipe)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      Object result = apiInstance.recipeDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeFeedback"></a>
# **recipeFeedback**
> Object recipeFeedback(recipeId, apI2ModelsRecipesFeedbackDTO)

Feedback on a Recipe -- for internal BigOven editors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer recipeId = 56; // Integer | 
    API2ModelsRecipesFeedbackDTO apI2ModelsRecipesFeedbackDTO = new API2ModelsRecipesFeedbackDTO(); // API2ModelsRecipesFeedbackDTO | The payload for feedback, which includes the field \"feedback\"
    try {
      Object result = apiInstance.recipeFeedback(recipeId, apI2ModelsRecipesFeedbackDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeFeedback");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **recipeId** | **Integer**|  | |
| **apI2ModelsRecipesFeedbackDTO** | [**API2ModelsRecipesFeedbackDTO**](API2ModelsRecipesFeedbackDTO.md)| The payload for feedback, which includes the field \&quot;feedback\&quot; | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeGet"></a>
# **recipeGet**
> BigOvenModelAPI2Recipe recipeGet(id, prefetch)

Return full Recipe detail. Returns 403 if the recipe is owned by someone else.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer id = 56; // Integer | The Recipe ID to retrieve
    Boolean prefetch = true; // Boolean | The prefetch.
    try {
      BigOvenModelAPI2Recipe result = apiInstance.recipeGet(id, prefetch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| The Recipe ID to retrieve | |
| **prefetch** | **Boolean**| The prefetch. | [optional] |

### Return type

[**BigOvenModelAPI2Recipe**](BigOvenModelAPI2Recipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeGetActiveRecipe"></a>
# **recipeGetActiveRecipe**
> BigOvenResult recipeGetActiveRecipe(userName)

Returns last active recipe for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String userName = "userName_example"; // String | 
    try {
      BigOvenResult result = apiInstance.recipeGetActiveRecipe(userName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeGetActiveRecipe");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userName** | **String**|  | |

### Return type

[**BigOvenResult**](BigOvenResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeGetRandomRecipe"></a>
# **recipeGetRandomRecipe**
> BigOvenModelAPIRecipe recipeGetRandomRecipe()

Get a random, home-page-quality Recipe.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    try {
      BigOvenModelAPIRecipe result = apiInstance.recipeGetRandomRecipe();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeGetRandomRecipe");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeGetRecipeWithSteps"></a>
# **recipeGetRecipeWithSteps**
> BigOvenModelAPI2Recipe recipeGetRecipeWithSteps(id, prefetch)

Return full Recipe detail with steps. Returns 403 if the recipe is owned by someone else.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer id = 56; // Integer | the Recipe ID to retrieve
    Boolean prefetch = true; // Boolean | 
    try {
      BigOvenModelAPI2Recipe result = apiInstance.recipeGetRecipeWithSteps(id, prefetch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeGetRecipeWithSteps");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| the Recipe ID to retrieve | |
| **prefetch** | **Boolean**|  | [optional] |

### Return type

[**BigOvenModelAPI2Recipe**](BigOvenModelAPI2Recipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeGetStep"></a>
# **recipeGetStep**
> String recipeGetStep(userName, recipeId, stepId)

Gets recipe single step as text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String userName = "userName_example"; // String | 
    Integer recipeId = 56; // Integer | 
    Integer stepId = 56; // Integer | 
    try {
      String result = apiInstance.recipeGetStep(userName, recipeId, stepId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeGetStep");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userName** | **String**|  | |
| **recipeId** | **Integer**|  | |
| **stepId** | **Integer**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeGetStepNumber"></a>
# **recipeGetStepNumber**
> API2Result recipeGetStepNumber(userName, recipeId)

Returns stored step number and number of steps in recipe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String userName = "userName_example"; // String | 
    Integer recipeId = 56; // Integer | 
    try {
      API2Result result = apiInstance.recipeGetStepNumber(userName, recipeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeGetStepNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userName** | **String**|  | |
| **recipeId** | **Integer**|  | |

### Return type

[**API2Result**](API2Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeGetSteps"></a>
# **recipeGetSteps**
> BigOvenResult recipeGetSteps(userName, recipeId, stepId)

Stores recipe step number and returns saved step data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String userName = "userName_example"; // String | 
    Integer recipeId = 56; // Integer | 
    Integer stepId = 56; // Integer | 
    try {
      BigOvenResult result = apiInstance.recipeGetSteps(userName, recipeId, stepId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeGetSteps");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userName** | **String**|  | |
| **recipeId** | **Integer**|  | |
| **stepId** | **Integer**|  | |

### Return type

[**BigOvenResult**](BigOvenResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeGetV2"></a>
# **recipeGetV2**
> API2ModelsRecipesRecipeResponse recipeGetV2(id, prefetch)

Same as GET recipe but also includes the recipe videos (if any)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer id = 56; // Integer | The Recipe ID to retrieve
    Boolean prefetch = true; // Boolean | The prefetch.
    try {
      API2ModelsRecipesRecipeResponse result = apiInstance.recipeGetV2(id, prefetch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeGetV2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| The Recipe ID to retrieve | |
| **prefetch** | **Boolean**| The prefetch. | [optional] |

### Return type

[**API2ModelsRecipesRecipeResponse**](API2ModelsRecipesRecipeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipePost"></a>
# **recipePost**
> BigOvenModelAPIRecipe recipePost(bigOvenModelAPIRecipe)

Add a new recipe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    BigOvenModelAPIRecipe bigOvenModelAPIRecipe = new BigOvenModelAPIRecipe(); // BigOvenModelAPIRecipe | 
    try {
      BigOvenModelAPIRecipe result = apiInstance.recipePost(bigOvenModelAPIRecipe);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipePost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bigOvenModelAPIRecipe** | [**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)|  | |

### Return type

[**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipePut"></a>
# **recipePut**
> BigOvenModelAPIRecipe recipePut(bigOvenModelAPIRecipe)

Update a recipe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    BigOvenModelAPIRecipe bigOvenModelAPIRecipe = new BigOvenModelAPIRecipe(); // BigOvenModelAPIRecipe | 
    try {
      BigOvenModelAPIRecipe result = apiInstance.recipePut(bigOvenModelAPIRecipe);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipePut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bigOvenModelAPIRecipe** | [**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)|  | |

### Return type

[**BigOvenModelAPIRecipe**](BigOvenModelAPIRecipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeRaves"></a>
# **recipeRaves**
> List&lt;BigOvenModelRecipeInfoReviewTuple2&gt; recipeRaves(pg, rpp)

Get the recipe/comment tuples for those recipes with 4 or 5 star ratings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer pg = 56; // Integer | page, starting with 1
    Integer rpp = 56; // Integer | results per page
    try {
      List<BigOvenModelRecipeInfoReviewTuple2> result = apiInstance.recipeRaves(pg, rpp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeRaves");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pg** | **Integer**| page, starting with 1 | [optional] |
| **rpp** | **Integer**| results per page | [optional] |

### Return type

[**List&lt;BigOvenModelRecipeInfoReviewTuple2&gt;**](BigOvenModelRecipeInfoReviewTuple2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeRecentViews"></a>
# **recipeRecentViews**
> List&lt;BigOvenModelRecipeInfoDateTuple2&gt; recipeRecentViews(pg, rpp)

Get a list of recipes that the authenticated user has most recently viewed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer pg = 56; // Integer | Page number starting with 1
    Integer rpp = 56; // Integer | results per page
    try {
      List<BigOvenModelRecipeInfoDateTuple2> result = apiInstance.recipeRecentViews(pg, rpp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeRecentViews");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pg** | **Integer**| Page number starting with 1 | [optional] |
| **rpp** | **Integer**| results per page | [optional] |

### Return type

[**List&lt;BigOvenModelRecipeInfoDateTuple2&gt;**](BigOvenModelRecipeInfoDateTuple2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeRecipeSearch"></a>
# **recipeRecipeSearch**
> BigOvenModelAPI2RecipeSearchResult recipeRecipeSearch(anyKw, folder, coll, filter, titleKw, userId, username, token, photos, boostmine, includeCat, excludeCat, includePrimarycat, excludePrimarycat, includeIng, excludeIng, cuisine, db, userset, servingsMin, totalMins, maxIngredients, minIngredients, rpp, pg, vtn, vgn, chs, glf, ntf, dyf, sff, slf, tnf, wmf, rmf, cps, champion, synonyms)

Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String anyKw = "anyKw_example"; // String | Search anywhere in the recipe for the keyword
    String folder = "folder_example"; // String | Search in a specific folder name for the authenticated user
    Integer coll = 56; // Integer | Limit to a collection ID number
    String filter = "filter_example"; // String | optionally set to either \"myrecipes\", \"try\", \"favorites\",\"added\" to filter to just the authenticated user's recipe set
    String titleKw = "titleKw_example"; // String | Search just in the recipe title for the keyword
    Integer userId = 56; // Integer | Set the target userid to search their public recipes
    String username = "username_example"; // String | Set the target username to search their public recipes
    String token = "token_example"; // String | 
    Boolean photos = true; // Boolean | if set to true, limit search results to photos only
    Boolean boostmine = true; // Boolean | if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders)
    String includeCat = "includeCat_example"; // String | integer of the subcategory you'd like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \"Main Dish &gt; Casseroles\".
    String excludeCat = "excludeCat_example"; // String | like include_cat, set this to an integer to exclude a specific category
    String includePrimarycat = "includePrimarycat_example"; // String | csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
    String excludePrimarycat = "excludePrimarycat_example"; // String | csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
    String includeIng = "includeIng_example"; // String | A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken
    String excludeIng = "excludeIng_example"; // String | A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required)
    String cuisine = "cuisine_example"; // String | Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese
    String db = "db_example"; // String | 
    String userset = "userset_example"; // String | If set to a given username, it'll force the search to filter to just that username
    Double servingsMin = 3.4D; // Double | Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \"dozen\", etc. This parameter simply specifies the minimum number for that value entered in \"yield.\"
    Integer totalMins = 56; // Integer | Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \"1 hour, 15 minutes\" to 75 before passing in.)
    Integer maxIngredients = 56; // Integer | Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less
    Integer minIngredients = 56; // Integer | Optional. If supplied, will restrict results to recipes that have at least {minIngredients}
    Integer rpp = 56; // Integer | integer; results per page
    Integer pg = 56; // Integer | integer: the page number
    Integer vtn = 56; // Integer | when set to 1, limit to vegetarian (Powersearch-capable plan required)
    Integer vgn = 56; // Integer | when set to 1, limit to vegan (Powersearch-capable plan required)
    Integer chs = 56; // Integer | when set to 1, limit to contains-cheese (Powersearch-capable plan required)
    Integer glf = 56; // Integer | when set to 1, limit to gluten-free (Powersearch-capable plan required)
    Integer ntf = 56; // Integer | when set to 1, limit to nut-free (Powersearch-capable plan required)
    Integer dyf = 56; // Integer | when set to 1, limit to dairy-free (Powersearch-capable plan required)
    Integer sff = 56; // Integer | when set to 1, limit to seafood-free (Powersearch-capable plan required)
    Integer slf = 56; // Integer | when set to 1, limit to shellfish-free (Powersearch-capable plan required)
    Integer tnf = 56; // Integer | when set to 1, limit to tree-nut free (Powersearch-capable plan required)
    Integer wmf = 56; // Integer | when set to 1, limit to white-meat free (Powersearch-capable plan required)
    Integer rmf = 56; // Integer | when set to 1, limit to red-meat free (Powersearch-capable plan required)
    Integer cps = 56; // Integer | when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required)
    Integer champion = 56; // Integer | optional. When set to 1, this will limit search results to \"best of\" recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don't include this parameter.
    Boolean synonyms = true; // Boolean | optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon)
    try {
      BigOvenModelAPI2RecipeSearchResult result = apiInstance.recipeRecipeSearch(anyKw, folder, coll, filter, titleKw, userId, username, token, photos, boostmine, includeCat, excludeCat, includePrimarycat, excludePrimarycat, includeIng, excludeIng, cuisine, db, userset, servingsMin, totalMins, maxIngredients, minIngredients, rpp, pg, vtn, vgn, chs, glf, ntf, dyf, sff, slf, tnf, wmf, rmf, cps, champion, synonyms);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeRecipeSearch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **anyKw** | **String**| Search anywhere in the recipe for the keyword | [optional] |
| **folder** | **String**| Search in a specific folder name for the authenticated user | [optional] |
| **coll** | **Integer**| Limit to a collection ID number | [optional] |
| **filter** | **String**| optionally set to either \&quot;myrecipes\&quot;, \&quot;try\&quot;, \&quot;favorites\&quot;,\&quot;added\&quot; to filter to just the authenticated user&#39;s recipe set | [optional] |
| **titleKw** | **String**| Search just in the recipe title for the keyword | [optional] |
| **userId** | **Integer**| Set the target userid to search their public recipes | [optional] |
| **username** | **String**| Set the target username to search their public recipes | [optional] |
| **token** | **String**|  | [optional] |
| **photos** | **Boolean**| if set to true, limit search results to photos only | [optional] |
| **boostmine** | **Boolean**| if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders) | [optional] |
| **includeCat** | **String**| integer of the subcategory you&#39;d like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \&quot;Main Dish &amp;gt; Casseroles\&quot;. | [optional] |
| **excludeCat** | **String**| like include_cat, set this to an integer to exclude a specific category | [optional] |
| **includePrimarycat** | **String**| csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other] | [optional] |
| **excludePrimarycat** | **String**| csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other] | [optional] |
| **includeIng** | **String**| A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken | [optional] |
| **excludeIng** | **String**| A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required) | [optional] |
| **cuisine** | **String**| Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese | [optional] |
| **db** | **String**|  | [optional] |
| **userset** | **String**| If set to a given username, it&#39;ll force the search to filter to just that username | [optional] |
| **servingsMin** | **Double**| Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \&quot;dozen\&quot;, etc. This parameter simply specifies the minimum number for that value entered in \&quot;yield.\&quot; | [optional] |
| **totalMins** | **Integer**| Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \&quot;1 hour, 15 minutes\&quot; to 75 before passing in.) | [optional] |
| **maxIngredients** | **Integer**| Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less | [optional] |
| **minIngredients** | **Integer**| Optional. If supplied, will restrict results to recipes that have at least {minIngredients} | [optional] |
| **rpp** | **Integer**| integer; results per page | [optional] |
| **pg** | **Integer**| integer: the page number | [optional] |
| **vtn** | **Integer**| when set to 1, limit to vegetarian (Powersearch-capable plan required) | [optional] |
| **vgn** | **Integer**| when set to 1, limit to vegan (Powersearch-capable plan required) | [optional] |
| **chs** | **Integer**| when set to 1, limit to contains-cheese (Powersearch-capable plan required) | [optional] |
| **glf** | **Integer**| when set to 1, limit to gluten-free (Powersearch-capable plan required) | [optional] |
| **ntf** | **Integer**| when set to 1, limit to nut-free (Powersearch-capable plan required) | [optional] |
| **dyf** | **Integer**| when set to 1, limit to dairy-free (Powersearch-capable plan required) | [optional] |
| **sff** | **Integer**| when set to 1, limit to seafood-free (Powersearch-capable plan required) | [optional] |
| **slf** | **Integer**| when set to 1, limit to shellfish-free (Powersearch-capable plan required) | [optional] |
| **tnf** | **Integer**| when set to 1, limit to tree-nut free (Powersearch-capable plan required) | [optional] |
| **wmf** | **Integer**| when set to 1, limit to white-meat free (Powersearch-capable plan required) | [optional] |
| **rmf** | **Integer**| when set to 1, limit to red-meat free (Powersearch-capable plan required) | [optional] |
| **cps** | **Integer**| when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required) | [optional] |
| **champion** | **Integer**| optional. When set to 1, this will limit search results to \&quot;best of\&quot; recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don&#39;t include this parameter. | [optional] |
| **synonyms** | **Boolean**| optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon) | [optional] |

### Return type

[**BigOvenModelAPI2RecipeSearchResult**](BigOvenModelAPI2RecipeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeRecipeSearchRandom"></a>
# **recipeRecipeSearchRandom**
> BigOvenModelAPI2RecipeSearchResult recipeRecipeSearchRandom(anyKw, folder, coll, filter, titleKw, userId, username, token, photos, boostmine, includeCat, excludeCat, includePrimarycat, excludePrimarycat, includeIng, excludeIng, cuisine, db, userset, servingsMin, totalMins, maxIngredients, minIngredients, vtn, vgn, chs, glf, ntf, dyf, sff, slf, tnf, wmf, rmf, cps, champion, synonyms)

Search for recipes. There are many parameters that you can apply. Starting with the most common, use title_kw to search within a title.              Use any_kw to search across the entire recipe.              If you&#39;d like to limit by course, set the parameter \&quot;include_primarycat\&quot; to one of (appetizers,bread,breakfast,dessert,drinks,maindish,salad,sidedish,soup,marinades,other).              If you&#39;d like to exclude a category, set exclude_cat to one or more (comma-separated) list of those categories to exclude.              If you&#39;d like to include a category, set include_cat to one or more (comma-separated) of those categories to include.              To explicitly include an ingredient in your search, set the parameter \&quot;include_ing\&quot; to a CSV of up to three ingredients, e.g.:include_ing&#x3D;mustard,chicken,beef%20tips              To explicitly exclude an ingredient in your search, set the parameter \&quot;exclude_ing\&quot; to a CSV of up to three ingredients.              All searches must contain the paging parameters pg and rpp, which are integers, and represent the page number (1-based) and results per page (rpp).              So, to get the third page of a result set paged with 25 recipes per page, you&#39;d pass pg&#x3D;3&amp;amp;rpp&#x3D;25              If you&#39;d like to target searches to just a single target user&#39;s recipes, set userId&#x3D;the target userId (number).              Or, you can set username&#x3D;theirusername              vtn;vgn;chs;glf;ntf;dyf;sff;slf;tnf;wmf;rmf;cps              cuisine              photos              filter&#x3D;added,try,favorites,myrecipes\\r\\n\\r\\n              folder&#x3D;FolderNameCaseSensitive              coll&#x3D;ID of Collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    String anyKw = "anyKw_example"; // String | Search anywhere in the recipe for the keyword
    String folder = "folder_example"; // String | Search in a specific folder name for the authenticated user
    Integer coll = 56; // Integer | Limit to a collection ID number
    String filter = "filter_example"; // String | optionally set to either \"myrecipes\", \"try\", \"favorites\",\"added\" to filter to just the authenticated user's recipe set
    String titleKw = "titleKw_example"; // String | Search just in the recipe title for the keyword
    Integer userId = 56; // Integer | Set the target userid to search their public recipes
    String username = "username_example"; // String | Set the target username to search their public recipes
    String token = "token_example"; // String | 
    Boolean photos = true; // Boolean | if set to true, limit search results to photos only
    Boolean boostmine = true; // Boolean | if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders)
    String includeCat = "includeCat_example"; // String | integer of the subcategory you'd like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \"Main Dish &gt; Casseroles\".
    String excludeCat = "excludeCat_example"; // String | like include_cat, set this to an integer to exclude a specific category
    String includePrimarycat = "includePrimarycat_example"; // String | csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
    String excludePrimarycat = "excludePrimarycat_example"; // String | csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other]
    String includeIng = "includeIng_example"; // String | A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken
    String excludeIng = "excludeIng_example"; // String | A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required)
    String cuisine = "cuisine_example"; // String | Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese
    String db = "db_example"; // String | 
    String userset = "userset_example"; // String | If set to a given username, it'll force the search to filter to just that username
    Double servingsMin = 3.4D; // Double | Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \"dozen\", etc. This parameter simply specifies the minimum number for that value entered in \"yield.\"
    Integer totalMins = 56; // Integer | Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \"1 hour, 15 minutes\" to 75 before passing in.)
    Integer maxIngredients = 56; // Integer | Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less
    Integer minIngredients = 56; // Integer | Optional. If supplied, will restrict results to recipes that have at least {minIngredients}
    Integer vtn = 56; // Integer | when set to 1, limit to vegetarian (Powersearch-capable plan required)
    Integer vgn = 56; // Integer | when set to 1, limit to vegan (Powersearch-capable plan required)
    Integer chs = 56; // Integer | when set to 1, limit to contains-cheese (Powersearch-capable plan required)
    Integer glf = 56; // Integer | when set to 1, limit to gluten-free (Powersearch-capable plan required)
    Integer ntf = 56; // Integer | when set to 1, limit to nut-free (Powersearch-capable plan required)
    Integer dyf = 56; // Integer | when set to 1, limit to dairy-free (Powersearch-capable plan required)
    Integer sff = 56; // Integer | when set to 1, limit to seafood-free (Powersearch-capable plan required)
    Integer slf = 56; // Integer | when set to 1, limit to shellfish-free (Powersearch-capable plan required)
    Integer tnf = 56; // Integer | when set to 1, limit to tree-nut free (Powersearch-capable plan required)
    Integer wmf = 56; // Integer | when set to 1, limit to white-meat free (Powersearch-capable plan required)
    Integer rmf = 56; // Integer | when set to 1, limit to red-meat free (Powersearch-capable plan required)
    Integer cps = 56; // Integer | when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required)
    Integer champion = 56; // Integer | optional. When set to 1, this will limit search results to \"best of\" recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don't include this parameter.
    Boolean synonyms = true; // Boolean | optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon)
    try {
      BigOvenModelAPI2RecipeSearchResult result = apiInstance.recipeRecipeSearchRandom(anyKw, folder, coll, filter, titleKw, userId, username, token, photos, boostmine, includeCat, excludeCat, includePrimarycat, excludePrimarycat, includeIng, excludeIng, cuisine, db, userset, servingsMin, totalMins, maxIngredients, minIngredients, vtn, vgn, chs, glf, ntf, dyf, sff, slf, tnf, wmf, rmf, cps, champion, synonyms);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeRecipeSearchRandom");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **anyKw** | **String**| Search anywhere in the recipe for the keyword | [optional] |
| **folder** | **String**| Search in a specific folder name for the authenticated user | [optional] |
| **coll** | **Integer**| Limit to a collection ID number | [optional] |
| **filter** | **String**| optionally set to either \&quot;myrecipes\&quot;, \&quot;try\&quot;, \&quot;favorites\&quot;,\&quot;added\&quot; to filter to just the authenticated user&#39;s recipe set | [optional] |
| **titleKw** | **String**| Search just in the recipe title for the keyword | [optional] |
| **userId** | **Integer**| Set the target userid to search their public recipes | [optional] |
| **username** | **String**| Set the target username to search their public recipes | [optional] |
| **token** | **String**|  | [optional] |
| **photos** | **Boolean**| if set to true, limit search results to photos only | [optional] |
| **boostmine** | **Boolean**| if set to true, boost my own recipes in my folders so they show up high in the list (at the expense of other sort orders) | [optional] |
| **includeCat** | **String**| integer of the subcategory you&#39;d like to limit searches to (see the /recipe/categories endpoint for available id numbers). For instance, 58 is \&quot;Main Dish &amp;gt; Casseroles\&quot;. | [optional] |
| **excludeCat** | **String**| like include_cat, set this to an integer to exclude a specific category | [optional] |
| **includePrimarycat** | **String**| csv indicating up to three top-level categories -- valid values are [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other] | [optional] |
| **excludePrimarycat** | **String**| csv indicating integer values for up to 3 top-level categories -- valid values are 1...11 [appetizers,bread,breakfast,desserts,drinks,maindish,salads,sidedish,soups,marinades,other] | [optional] |
| **includeIng** | **String**| A CSV representing up to 3 ingredients to include, e.g., tomatoes,corn%20%starch,chicken | [optional] |
| **excludeIng** | **String**| A CSV representing up to 3 ingredients to exclude  (Powersearch-capable plan required) | [optional] |
| **cuisine** | **String**| Limit to a specific cuisine. Cooks can enter anything free-form, but the few dozen preconfigured values are Afghan,African,American,American-South,Asian,Australian,Brazilian,Cajun,Canadian,Caribbean,Chinese,Croatian,Cuban,Dessert,Eastern European,English,French,German,Greek,Hawaiian,Hungarian,India,Indian,Irish,Italian,Japanese,Jewish,Korean,Latin,Mediterranean,Mexican,Middle Eastern,Moroccan,Polish,Russian,Scandanavian,Seafood,Southern,Southwestern,Spanish,Tex-Mex,Thai,Vegan,Vegetarian,Vietnamese | [optional] |
| **db** | **String**|  | [optional] |
| **userset** | **String**| If set to a given username, it&#39;ll force the search to filter to just that username | [optional] |
| **servingsMin** | **Double**| Limit to yield of a given number size or greater. Note that cooks usually enter recipes by Servings, but sometimes they are posted by \&quot;dozen\&quot;, etc. This parameter simply specifies the minimum number for that value entered in \&quot;yield.\&quot; | [optional] |
| **totalMins** | **Integer**| Optional. If supplied, will restrict results to recipes that can be made in {totalMins} or less. (Convert \&quot;1 hour, 15 minutes\&quot; to 75 before passing in.) | [optional] |
| **maxIngredients** | **Integer**| Optional. If supplied, will restrict results to recipes that can be made with {maxIngredients} ingredients or less | [optional] |
| **minIngredients** | **Integer**| Optional. If supplied, will restrict results to recipes that have at least {minIngredients} | [optional] |
| **vtn** | **Integer**| when set to 1, limit to vegetarian (Powersearch-capable plan required) | [optional] |
| **vgn** | **Integer**| when set to 1, limit to vegan (Powersearch-capable plan required) | [optional] |
| **chs** | **Integer**| when set to 1, limit to contains-cheese (Powersearch-capable plan required) | [optional] |
| **glf** | **Integer**| when set to 1, limit to gluten-free (Powersearch-capable plan required) | [optional] |
| **ntf** | **Integer**| when set to 1, limit to nut-free (Powersearch-capable plan required) | [optional] |
| **dyf** | **Integer**| when set to 1, limit to dairy-free (Powersearch-capable plan required) | [optional] |
| **sff** | **Integer**| when set to 1, limit to seafood-free (Powersearch-capable plan required) | [optional] |
| **slf** | **Integer**| when set to 1, limit to shellfish-free (Powersearch-capable plan required) | [optional] |
| **tnf** | **Integer**| when set to 1, limit to tree-nut free (Powersearch-capable plan required) | [optional] |
| **wmf** | **Integer**| when set to 1, limit to white-meat free (Powersearch-capable plan required) | [optional] |
| **rmf** | **Integer**| when set to 1, limit to red-meat free (Powersearch-capable plan required) | [optional] |
| **cps** | **Integer**| when set to 1, recipe contains pasta, set to 0 means contains no pasta (Powersearch-capable plan required) | [optional] |
| **champion** | **Integer**| optional. When set to 1, this will limit search results to \&quot;best of\&quot; recipes as determined by various internal editorial and programmatic algorithms. For the most comprehensive results, don&#39;t include this parameter. | [optional] |
| **synonyms** | **Boolean**| optional, default is false. When set to true, BigOven will attempt to apply synonyms in search (e.g., excluding pork will also exclude bacon) | [optional] |

### Return type

[**BigOvenModelAPI2RecipeSearchResult**](BigOvenModelAPI2RecipeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeRelated"></a>
# **recipeRelated**
> BigOvenModelAPI2RecipeSearchResult recipeRelated(recipeId, pg, rpp)

Get recipes related to the given recipeId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer recipeId = 56; // Integer | The recipe id
    Integer pg = 56; // Integer | The page
    Integer rpp = 56; // Integer | The results per page
    try {
      BigOvenModelAPI2RecipeSearchResult result = apiInstance.recipeRelated(recipeId, pg, rpp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **recipeId** | **Integer**| The recipe id | |
| **pg** | **Integer**| The page | [optional] |
| **rpp** | **Integer**| The results per page | [optional] |

### Return type

[**BigOvenModelAPI2RecipeSearchResult**](BigOvenModelAPI2RecipeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeScan"></a>
# **recipeScan**
> recipeScan(test, devicetype, lat, lng)

POST an image as a new RecipeScan request                  1)  Fetch the filename -- DONE                  2)  Copy it to the pics/scan folder - ENSURE NO NAMING COLLISIONS -- DONE                  3)  Create 120 thumbnail size  in pics/scan/120 -- DONE                  4)  Insert the CloudTasks record                  5)  Create the HIT                  6)  Update the CloudTasks record with the HIT ID                  7)  Email the requesing user                  8)  Call out to www.bigoven.com to fetch the image and re-create the thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Boolean test = true; // Boolean | 
    String devicetype = "devicetype_example"; // String | 
    Double lat = 3.4D; // Double | 
    Double lng = 3.4D; // Double | 
    try {
      apiInstance.recipeScan(test, devicetype, lat, lng);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeScan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **test** | **Boolean**|  | [optional] |
| **devicetype** | **String**|  | [optional] |
| **lat** | **Double**|  | [optional] |
| **lng** | **Double**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **401** | Not authorized |  -  |
| **402** | Payment required (not enough credits) |  -  |
| **415** | Bad media type (bad JPG) |  -  |
| **500** | General error on initiating RecipeScan task; please try again or contact us at support[at]bigoven.com |  -  |

<a id="recipeZapRecipe"></a>
# **recipeZapRecipe**
> Object recipeZapRecipe(id)

Zaps the recipe.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    RecipeApi apiInstance = new RecipeApi(defaultClient);
    Integer id = 56; // Integer | The identifier.
    try {
      Object result = apiInstance.recipeZapRecipe(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipeApi#recipeZapRecipe");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| The identifier. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

