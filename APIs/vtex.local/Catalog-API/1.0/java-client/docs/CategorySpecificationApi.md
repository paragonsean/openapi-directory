# CategorySpecificationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**specificationsByCategoryId**](CategorySpecificationApi.md#specificationsByCategoryId) | **GET** /api/catalog_system/pub/specification/field/listByCategoryId/{categoryId} | Get Specifications By Category ID |
| [**specificationsTreeByCategoryId**](CategorySpecificationApi.md#specificationsTreeByCategoryId) | **GET** /api/catalog_system/pub/specification/field/listTreeByCategoryId/{categoryId} | Get Specifications Tree By Category ID |


<a id="specificationsByCategoryId"></a>
# **specificationsByCategoryId**
> List&lt;CategorySpecificationInner&gt; specificationsByCategoryId(contentType, accept, categoryId)

Get Specifications By Category ID

Retrieves all specifications from a category by its ID.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Name\&quot;: \&quot;Specification A\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification B\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification C\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 35,          \&quot;IsActive\&quot;: false,          \&quot;IsStockKeepingUnit\&quot;: false      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategorySpecificationApi;

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

    CategorySpecificationApi apiInstance = new CategorySpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer categoryId = 1; // Integer | Category ID.
    try {
      List<CategorySpecificationInner> result = apiInstance.specificationsByCategoryId(contentType, accept, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategorySpecificationApi#specificationsByCategoryId");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **categoryId** | **Integer**| Category ID. | |

### Return type

[**List&lt;CategorySpecificationInner&gt;**](CategorySpecificationInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="specificationsTreeByCategoryId"></a>
# **specificationsTreeByCategoryId**
> List&lt;CategorySpecificationInner&gt; specificationsTreeByCategoryId(contentType, accept, categoryId)

Get Specifications Tree By Category ID

Lists all specifications including the current category and the level zero specifications from a category by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Name\&quot;: \&quot;Specification A\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification B\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification C\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 35,          \&quot;IsActive\&quot;: false,          \&quot;IsStockKeepingUnit\&quot;: false      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategorySpecificationApi;

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

    CategorySpecificationApi apiInstance = new CategorySpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer categoryId = 1; // Integer | Category ID.
    try {
      List<CategorySpecificationInner> result = apiInstance.specificationsTreeByCategoryId(contentType, accept, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategorySpecificationApi#specificationsTreeByCategoryId");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **categoryId** | **Integer**| Category ID. | |

### Return type

[**List&lt;CategorySpecificationInner&gt;**](CategorySpecificationInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

