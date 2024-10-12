# DefaultApi

All URIs are relative to *https://chompthis.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**foodBrandedBarcodePhpGet**](DefaultApi.md#foodBrandedBarcodePhpGet) | **GET** /food/branded/barcode.php | Get a branded food item using a barcode |
| [**foodBrandedNamePhpGet**](DefaultApi.md#foodBrandedNamePhpGet) | **GET** /food/branded/name.php | Get a branded food item by name |
| [**foodBrandedSearchPhpGet**](DefaultApi.md#foodBrandedSearchPhpGet) | **GET** /food/branded/search.php | Get data for branded food items using various search parameters |
| [**foodIngredientSearchPhpGet**](DefaultApi.md#foodIngredientSearchPhpGet) | **GET** /food/ingredient/search.php | Get raw/generic food ingredient item(s) |


<a id="foodBrandedBarcodePhpGet"></a>
# **foodBrandedBarcodePhpGet**
> BrandedFoodObject foodBrandedBarcodePhpGet(code)

Get a branded food item using a barcode

## Get data for a branded food using the food&#39;s UPC/EAN barcode.  **Example**  &gt; &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/barcode.php?api_key&#x3D;API_KEY&amp;code&#x3D;CODE&#x60;&#x60;&#x60;  **Tips**   * Read our **[Knowledge Base article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do)** for helpful tips and tricks. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chompthis.com/api/v2");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String code = "code_example"; // String | #### UPC/EAN barcode  **Example** > ```&code=0842234000988``` 
    try {
      BrandedFoodObject result = apiInstance.foodBrandedBarcodePhpGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#foodBrandedBarcodePhpGet");
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
| **code** | **String**| #### UPC/EAN barcode  **Example** &gt; &#x60;&#x60;&#x60;&amp;code&#x3D;0842234000988&#x60;&#x60;&#x60;  | |

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | **Valid** - Will return an object containing any matching foods.   |  -  |
| **400** | **Validation error** - Invalid parameters or request.  |  -  |
| **401** | **Unauthorized** - Invalid API key, unauthorized access, or usage limits exceeded. ***[More information &amp;raquo;](https://desk.zoho.com/portal/chompthis/kb/articles/what-is-a-rate-limit)***  |  -  |
| **404** | **Not found** - No food items were found.  |  -  |
| **500** | **Server error** - Internal server error, request failed, or base error. *Please **[contact us](https://chompthis.com/api/ticket-new.php)** if you see this.*  |  -  |

<a id="foodBrandedNamePhpGet"></a>
# **foodBrandedNamePhpGet**
> BrandedFoodObject foodBrandedNamePhpGet(name, limit, page)

Get a branded food item by name

## Search for branded food items by name.  **Example** &gt; &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/name.php?api_key&#x3D;API_KEY&amp;name&#x3D;NAME&#x60;&#x60;&#x60;  **Tips**   * Get started by using our **[food lookup tool](https://chompthis.com/api/lookup.php)**.  &gt; This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren&#39;t sure how to upgrade your subscription. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chompthis.com/api/v2");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | #### Search for branded food items using a general food name keyword. This does not have to exactly match the \"official\" name for the food.  **Example** > ```&name=Starburst``` 
    Integer limit = 1; // Integer | #### Set maximum number of records you want the API to return. The default value is \"**10**.\"  **Example** > ```&limit=10``` 
    Integer page = 56; // Integer | #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \"**1**.\"  **Example** > ```&page=1``` 
    try {
      BrandedFoodObject result = apiInstance.foodBrandedNamePhpGet(name, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#foodBrandedNamePhpGet");
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
| **name** | **String**| #### Search for branded food items using a general food name keyword. This does not have to exactly match the \&quot;official\&quot; name for the food.  **Example** &gt; &#x60;&#x60;&#x60;&amp;name&#x3D;Starburst&#x60;&#x60;&#x60;  | |
| **limit** | **Integer**| #### Set maximum number of records you want the API to return. The default value is \&quot;**10**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;10&#x60;&#x60;&#x60;  | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| **page** | **Integer**| #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \&quot;**1**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;page&#x3D;1&#x60;&#x60;&#x60;  | [optional] |

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | **Valid** - Will return an object containing any matching foods.   |  -  |
| **400** | **Validation error** - Invalid parameters or request.  |  -  |
| **401** | **Unauthorized** - Invalid API key, unauthorized access, or usage limits exceeded. ***[More information &amp;raquo;](https://desk.zoho.com/portal/chompthis/kb/articles/what-is-a-rate-limit)***  |  -  |
| **404** | **Not found** - No food items were found.  |  -  |
| **500** | **Server error** - Internal server error, request failed, or base error. *Please **[contact us](https://chompthis.com/api/ticket-new.php)** if you see this.*  |  -  |

<a id="foodBrandedSearchPhpGet"></a>
# **foodBrandedSearchPhpGet**
> BrandedFoodObject foodBrandedSearchPhpGet(allergen, brand, category, country, diet, ingredient, keyword, mineral, nutrient, palmOil, trace, vitamin, limit, page)

Get data for branded food items using various search parameters

## Search for branded food items using various parameters.  **Example** &gt; &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/search.php?api_key&#x3D;API_KEY&amp;brand&#x3D;BRAND&amp;country&#x3D;COUNTRY&amp;page&#x3D;1&#x60;&#x60;&#x60;  **Tips**    * Get started by using the **[Query Builder](https://chompthis.com/api/build.php)**.  &gt; This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren&#39;t sure how to upgrade your subscription. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chompthis.com/api/v2");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String allergen = "allergen_example"; // String | #### Filter the search to only include branded foods that contain a specific allergen.  **Example** > ```&allergen=Peanuts```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
    String brand = "brand_example"; // String | #### Filter the search to only include branded foods that are owned by a specific brand.  **Example** > ```&brand=Starbucks``` 
    String category = "category_example"; // String | #### Filter the search to only include branded foods from a specific category.  **Example** > ```&category=Plant Based Foods``` 
    String country = "country_example"; // String | #### Filter the search to only include branded foods that are sold in a specific country.  **Example** > ```&country=United States```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
    String diet = "Vegan"; // String | #### Filter the search to only include branded foods that are considered compatible with a specific diet.  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
    String ingredient = "ingredient_example"; // String | #### Filter the search to only include branded foods that contain a specific ingredient.  **Example** > ```&ingredient=Salt``` 
    String keyword = "keyword_example"; // String | #### Filter the search to only include branded foods that are associated with a specific keyword.  **Example** > ```&keyword=Organic```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
    String mineral = "mineral_example"; // String | #### Filter the search to only include branded foods that contain a specific mineral.  **Example** > ```&mineral=Potassium``` 
    String nutrient = "nutrient_example"; // String | #### Filter the search to only include branded foods that contain a specific nutrient.  **Example** > ```&nutrient=Caffeine```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
    String palmOil = "palmOil_example"; // String | #### Filter the search to only include branded foods that contain a specific ingredient made using palm oil.  **Example** > ```&palm_oil=E160a Beta Carotene``` 
    String trace = "trace_example"; // String | ### Filter the search to only include branded foods that contain a specific trace ingredient.  **Example** > ```&trace=Tree Nuts```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter. 
    String vitamin = "vitamin_example"; // String | #### Filter the search to only include branded foods that contain a specific vitamin.  **Example** > ```&vitamin=Biotin``` 
    Integer limit = 1; // Integer | #### Set maximum number of records you want the API to return. The default value is \"**10**.\"  **Example** > ```&limit=10``` 
    Integer page = 56; // Integer | #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \"**1**.\"  **Example** > ```&page=1``` 
    try {
      BrandedFoodObject result = apiInstance.foodBrandedSearchPhpGet(allergen, brand, category, country, diet, ingredient, keyword, mineral, nutrient, palmOil, trace, vitamin, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#foodBrandedSearchPhpGet");
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
| **allergen** | **String**| #### Filter the search to only include branded foods that contain a specific allergen.  **Example** &gt; &#x60;&#x60;&#x60;&amp;allergen&#x3D;Peanuts&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] |
| **brand** | **String**| #### Filter the search to only include branded foods that are owned by a specific brand.  **Example** &gt; &#x60;&#x60;&#x60;&amp;brand&#x3D;Starbucks&#x60;&#x60;&#x60;  | [optional] |
| **category** | **String**| #### Filter the search to only include branded foods from a specific category.  **Example** &gt; &#x60;&#x60;&#x60;&amp;category&#x3D;Plant Based Foods&#x60;&#x60;&#x60;  | [optional] |
| **country** | **String**| #### Filter the search to only include branded foods that are sold in a specific country.  **Example** &gt; &#x60;&#x60;&#x60;&amp;country&#x3D;United States&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] |
| **diet** | **String**| #### Filter the search to only include branded foods that are considered compatible with a specific diet.  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] [enum: Vegan, Vegetarian, Gluten Free] |
| **ingredient** | **String**| #### Filter the search to only include branded foods that contain a specific ingredient.  **Example** &gt; &#x60;&#x60;&#x60;&amp;ingredient&#x3D;Salt&#x60;&#x60;&#x60;  | [optional] |
| **keyword** | **String**| #### Filter the search to only include branded foods that are associated with a specific keyword.  **Example** &gt; &#x60;&#x60;&#x60;&amp;keyword&#x3D;Organic&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] |
| **mineral** | **String**| #### Filter the search to only include branded foods that contain a specific mineral.  **Example** &gt; &#x60;&#x60;&#x60;&amp;mineral&#x3D;Potassium&#x60;&#x60;&#x60;  | [optional] |
| **nutrient** | **String**| #### Filter the search to only include branded foods that contain a specific nutrient.  **Example** &gt; &#x60;&#x60;&#x60;&amp;nutrient&#x3D;Caffeine&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] |
| **palmOil** | **String**| #### Filter the search to only include branded foods that contain a specific ingredient made using palm oil.  **Example** &gt; &#x60;&#x60;&#x60;&amp;palm_oil&#x3D;E160a Beta Carotene&#x60;&#x60;&#x60;  | [optional] |
| **trace** | **String**| ### Filter the search to only include branded foods that contain a specific trace ingredient.  **Example** &gt; &#x60;&#x60;&#x60;&amp;trace&#x3D;Tree Nuts&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] |
| **vitamin** | **String**| #### Filter the search to only include branded foods that contain a specific vitamin.  **Example** &gt; &#x60;&#x60;&#x60;&amp;vitamin&#x3D;Biotin&#x60;&#x60;&#x60;  | [optional] |
| **limit** | **Integer**| #### Set maximum number of records you want the API to return. The default value is \&quot;**10**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;10&#x60;&#x60;&#x60;  | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| **page** | **Integer**| #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \&quot;**1**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;page&#x3D;1&#x60;&#x60;&#x60;  | [optional] |

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | **Valid** - Will return an object containing any matching foods.   |  -  |
| **400** | **Validation error** - Invalid parameters or request.  |  -  |
| **401** | **Unauthorized** - Invalid API key, unauthorized access, or usage limits exceeded. ***[More information &amp;raquo;](https://desk.zoho.com/portal/chompthis/kb/articles/what-is-a-rate-limit)***  |  -  |
| **404** | **Not found** - No food items were found.  |  -  |
| **500** | **Server error** - Internal server error, request failed, or base error. *Please **[contact us](https://chompthis.com/api/ticket-new.php)** if you see this.*  |  -  |

<a id="foodIngredientSearchPhpGet"></a>
# **foodIngredientSearchPhpGet**
> IngredientObject foodIngredientSearchPhpGet(find, limit)

Get raw/generic food ingredient item(s)

## Get data for a specific ingredient or a specific set of ingredients.  **Example #1: Single Ingredient** &gt; &#x60;&#x60;&#x60;https://chompthis.com/api/v2/ingredient/search.php?api_key&#x3D;API_KEY&amp;find&#x3D;raw broccoli&#x60;&#x60;&#x60;  **Example #2: Set of Ingredients** &gt; &#x60;&#x60;&#x60;https://chompthis.com/api/v2/ingredient/search.php?api_key&#x3D;API_KEY&amp;find&#x3D;raw broccoli,mashed potatoes,chicken drumstick&#x60;&#x60;&#x60;  **Tips**   * Expose ingredient endpoints by using our **[food lookup tool](https://chompthis.com/api/lookup.php)**.  &gt; This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren&#39;t sure how to upgrade your subscription. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chompthis.com/api/v2");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String find = "find_example"; // String | Search our database for a single ingredient or a specific set of ingredients.  **Example #1: Single Ingredient** > ```&find=raw broccoli```  **Example #2: Set of Ingredients** > ```&find=raw broccoli,buttermilk waffle,mashed potatoes```  **Important Notes**    * Comma-separated lists cannot contain more than **10 ingredients**. You must perform additional API calls if you are looking up more than 10 ingredients. 
    Integer limit = 1; // Integer | #### Set maximum number of records you want the API to return, per search term. The default value is \"**1**.\"  **Example** > ```&limit=3``` 
    try {
      IngredientObject result = apiInstance.foodIngredientSearchPhpGet(find, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#foodIngredientSearchPhpGet");
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
| **find** | **String**| Search our database for a single ingredient or a specific set of ingredients.  **Example #1: Single Ingredient** &gt; &#x60;&#x60;&#x60;&amp;find&#x3D;raw broccoli&#x60;&#x60;&#x60;  **Example #2: Set of Ingredients** &gt; &#x60;&#x60;&#x60;&amp;find&#x3D;raw broccoli,buttermilk waffle,mashed potatoes&#x60;&#x60;&#x60;  **Important Notes**    * Comma-separated lists cannot contain more than **10 ingredients**. You must perform additional API calls if you are looking up more than 10 ingredients.  | |
| **limit** | **Integer**| #### Set maximum number of records you want the API to return, per search term. The default value is \&quot;**1**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;3&#x60;&#x60;&#x60;  | [optional] [enum: 1, 2, 3] |

### Return type

[**IngredientObject**](IngredientObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | **Valid** - Will return an object containing any matching ingredient foods.   |  -  |
| **400** | **Validation error** - Invalid parameters or request.  |  -  |
| **401** | **Unauthorized** - Invalid API key, unauthorized access, or usage limits exceeded. ***[More information &amp;raquo;](https://desk.zoho.com/portal/chompthis/kb/articles/what-is-a-rate-limit)***  |  -  |
| **404** | **Not found** - No food items were found.  |  -  |
| **500** | **Server error** - Internal server error, request failed, or base error. *Please **[contact us](https://chompthis.com/api/ticket-new.php)** if you see this.*  |  -  |

