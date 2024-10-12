# SimilarCategoryApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete**](SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete) | **DELETE** /api/catalog/pvt/product/{productId}/similarcategory/{categoryId} | Delete Similar Category |
| [**apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost**](SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost) | **POST** /api/catalog/pvt/product/{productId}/similarcategory/{categoryId} | Add Similar Category |
| [**apiCatalogPvtProductProductIdSimilarcategoryGet**](SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryGet) | **GET** /api/catalog/pvt/product/{productId}/similarcategory/ | Get Similar Categories |


<a id="apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete"></a>
# **apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete**
> apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete(contentType, accept, productId, categoryId)

Delete Similar Category

Deletes a Similar Category from a Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SimilarCategoryApi apiInstance = new SimilarCategoryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    Integer categoryId = 1; // Integer | Similar Category’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete(contentType, accept, productId, categoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarCategoryApi#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |
| **categoryId** | **Integer**| Similar Category’s unique numerical identifier. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost"></a>
# **apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost**
> ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost(contentType, accept, productId, categoryId)

Add Similar Category

Adds a Similar Category to a Product.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ProductId\&quot;: 1,      \&quot;StoreId\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SimilarCategoryApi apiInstance = new SimilarCategoryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    Integer categoryId = 1; // Integer | Similar Category’s unique numerical identifier.
    try {
      ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response result = apiInstance.apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost(contentType, accept, productId, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarCategoryApi#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |
| **categoryId** | **Integer**| Similar Category’s unique numerical identifier. | |

### Return type

[**ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response**](ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtProductProductIdSimilarcategoryGet"></a>
# **apiCatalogPvtProductProductIdSimilarcategoryGet**
> List&lt;ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner&gt; apiCatalogPvtProductProductIdSimilarcategoryGet(contentType, accept, productId)

Get Similar Categories

Retrieves Similar Categories from a Product.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;CategoryId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;CategoryId\&quot;: 20      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SimilarCategoryApi apiInstance = new SimilarCategoryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    try {
      List<ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner> result = apiInstance.apiCatalogPvtProductProductIdSimilarcategoryGet(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarCategoryApi#apiCatalogPvtProductProductIdSimilarcategoryGet");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |

### Return type

[**List&lt;ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner&gt;**](ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

