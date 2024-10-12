# CategoryRulesApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesIdCategoryRulesPost**](CategoryRulesApi.md#categoriesIdCategoryRulesPost) | **POST** /categories/{id}/category_rules | Create category rule in category |
| [**usersIdCategoryRulesGet**](CategoryRulesApi.md#usersIdCategoryRulesGet) | **GET** /users/{id}/category_rules | List category rules in user |


<a id="categoriesIdCategoryRulesPost"></a>
# **categoriesIdCategoryRulesPost**
> CategoryRule categoriesIdCategoryRulesPost(id, categoriesIdCategoryRulesPostRequest)

Create category rule in category

Creates a rule to allocate a category to transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    CategoryRulesApi apiInstance = new CategoryRulesApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the category.
    CategoriesIdCategoryRulesPostRequest categoriesIdCategoryRulesPostRequest = new CategoriesIdCategoryRulesPostRequest(); // CategoriesIdCategoryRulesPostRequest | 
    try {
      CategoryRule result = apiInstance.categoriesIdCategoryRulesPost(id, categoriesIdCategoryRulesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryRulesApi#categoriesIdCategoryRulesPost");
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
| **id** | **Integer**| The unique identifier of the category. | |
| **categoriesIdCategoryRulesPostRequest** | [**CategoriesIdCategoryRulesPostRequest**](CategoriesIdCategoryRulesPostRequest.md)|  | [optional] |

### Return type

[**CategoryRule**](CategoryRule.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="usersIdCategoryRulesGet"></a>
# **usersIdCategoryRulesGet**
> List&lt;CategoryRule&gt; usersIdCategoryRulesGet(id)

List category rules in user

Lists all category rules belonging to a user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    CategoryRulesApi apiInstance = new CategoryRulesApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    try {
      List<CategoryRule> result = apiInstance.usersIdCategoryRulesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryRulesApi#usersIdCategoryRulesGet");
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
| **id** | **Integer**| The unique identifier of the user. | |

### Return type

[**List&lt;CategoryRule&gt;**](CategoryRule.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

