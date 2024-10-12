# SpecificationValueApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSpecificationvaluePost**](SpecificationValueApi.md#apiCatalogPvtSpecificationvaluePost) | **POST** /api/catalog/pvt/specificationvalue | Create Specification Value |
| [**apiCatalogPvtSpecificationvalueSpecificationValueIdGet**](SpecificationValueApi.md#apiCatalogPvtSpecificationvalueSpecificationValueIdGet) | **GET** /api/catalog/pvt/specificationvalue/{specificationValueId} | Get Specification Value |
| [**apiCatalogPvtSpecificationvalueSpecificationValueIdPut**](SpecificationValueApi.md#apiCatalogPvtSpecificationvalueSpecificationValueIdPut) | **PUT** /api/catalog/pvt/specificationvalue/{specificationValueId} | Update Specification Value |


<a id="apiCatalogPvtSpecificationvaluePost"></a>
# **apiCatalogPvtSpecificationvaluePost**
> ApiCatalogPvtSpecificationvaluePost200Response apiCatalogPvtSpecificationvaluePost(contentType, accept, apiCatalogPvtSpecificationvaluePostRequest)

Create Specification Value

Creates a new Specification Value for a Category.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 193,      \&quot;Name\&quot;: \&quot;Metal\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 1    }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;FieldValueId\&quot;: 360,    \&quot;FieldId\&quot;: 193,    \&quot;Name\&quot;: \&quot;Metal\&quot;,    \&quot;Text\&quot;: null,    \&quot;IsActive\&quot;: true,    \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationValueApi;

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

    SpecificationValueApi apiInstance = new SpecificationValueApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    ApiCatalogPvtSpecificationvaluePostRequest apiCatalogPvtSpecificationvaluePostRequest = new ApiCatalogPvtSpecificationvaluePostRequest(); // ApiCatalogPvtSpecificationvaluePostRequest | 
    try {
      ApiCatalogPvtSpecificationvaluePost200Response result = apiInstance.apiCatalogPvtSpecificationvaluePost(contentType, accept, apiCatalogPvtSpecificationvaluePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationValueApi#apiCatalogPvtSpecificationvaluePost");
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
| **apiCatalogPvtSpecificationvaluePostRequest** | [**ApiCatalogPvtSpecificationvaluePostRequest**](ApiCatalogPvtSpecificationvaluePostRequest.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSpecificationvaluePost200Response**](ApiCatalogPvtSpecificationvaluePost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSpecificationvalueSpecificationValueIdGet"></a>
# **apiCatalogPvtSpecificationvalueSpecificationValueIdGet**
> ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response apiCatalogPvtSpecificationvalueSpecificationValueIdGet(contentType, accept, specificationValueId)

Get Specification Value

Retrieves general information about a Specification Value.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationValueApi;

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

    SpecificationValueApi apiInstance = new SpecificationValueApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer specificationValueId = 143; // Integer | Specification Value’s unique numerical identifier.
    try {
      ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response result = apiInstance.apiCatalogPvtSpecificationvalueSpecificationValueIdGet(contentType, accept, specificationValueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationValueApi#apiCatalogPvtSpecificationvalueSpecificationValueIdGet");
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
| **specificationValueId** | **Integer**| Specification Value’s unique numerical identifier. | |

### Return type

[**ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response**](ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSpecificationvalueSpecificationValueIdPut"></a>
# **apiCatalogPvtSpecificationvalueSpecificationValueIdPut**
> ApiCatalogPvtSpecificationvaluePost200Response apiCatalogPvtSpecificationvalueSpecificationValueIdPut(contentType, accept, specificationValueId, apiCatalogPvtSpecificationvaluePostRequest)

Update Specification Value

Updates a new Specification Value for a Category.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 193,      \&quot;Name\&quot;: \&quot;Metal\&quot;,      \&quot;Text\&quot;: null,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 1    }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;FieldValueId\&quot;: 360,    \&quot;FieldId\&quot;: 193,    \&quot;Name\&quot;: \&quot;Metal\&quot;,    \&quot;Text\&quot;: null,    \&quot;IsActive\&quot;: true,    \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationValueApi;

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

    SpecificationValueApi apiInstance = new SpecificationValueApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer specificationValueId = 1; // Integer |  Specification Value’s unique numerical identifier.
    ApiCatalogPvtSpecificationvaluePostRequest apiCatalogPvtSpecificationvaluePostRequest = new ApiCatalogPvtSpecificationvaluePostRequest(); // ApiCatalogPvtSpecificationvaluePostRequest | 
    try {
      ApiCatalogPvtSpecificationvaluePost200Response result = apiInstance.apiCatalogPvtSpecificationvalueSpecificationValueIdPut(contentType, accept, specificationValueId, apiCatalogPvtSpecificationvaluePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationValueApi#apiCatalogPvtSpecificationvalueSpecificationValueIdPut");
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
| **specificationValueId** | **Integer**|  Specification Value’s unique numerical identifier. | |
| **apiCatalogPvtSpecificationvaluePostRequest** | [**ApiCatalogPvtSpecificationvaluePostRequest**](ApiCatalogPvtSpecificationvaluePostRequest.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSpecificationvaluePost200Response**](ApiCatalogPvtSpecificationvaluePost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

