# SkuServiceValueApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSkuservicevaluePost**](SkuServiceValueApi.md#apiCatalogPvtSkuservicevaluePost) | **POST** /api/catalog/pvt/skuservicevalue | Create SKU Service Value |
| [**apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete**](SkuServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete) | **DELETE** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Delete SKU Service Value |
| [**apiCatalogPvtSkuservicevalueSkuServiceValueIdGet**](SkuServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdGet) | **GET** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Get SKU Service Value |
| [**apiCatalogPvtSkuservicevalueSkuServiceValueIdPut**](SkuServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdPut) | **PUT** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Update SKU Service Value |


<a id="apiCatalogPvtSkuservicevaluePost"></a>
# **apiCatalogPvtSkuservicevaluePost**
> SKUServiceValueResponse apiCatalogPvtSkuservicevaluePost(contentType, accept, skUServiceValueRequest)

Create SKU Service Value

Creates an SKU Service Value for an existing SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceValueApi;

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

    SkuServiceValueApi apiInstance = new SkuServiceValueApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    SKUServiceValueRequest skUServiceValueRequest = new SKUServiceValueRequest(); // SKUServiceValueRequest | 
    try {
      SKUServiceValueResponse result = apiInstance.apiCatalogPvtSkuservicevaluePost(contentType, accept, skUServiceValueRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceValueApi#apiCatalogPvtSkuservicevaluePost");
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
| **skUServiceValueRequest** | [**SKUServiceValueRequest**](SKUServiceValueRequest.md)|  | [optional] |

### Return type

[**SKUServiceValueResponse**](SKUServiceValueResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete"></a>
# **apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete**
> apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete(contentType, accept, skuServiceValueId)

Delete SKU Service Value

Deletes an existing SKU Service Value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceValueApi;

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

    SkuServiceValueApi apiInstance = new SkuServiceValueApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceValueId = 1; // Integer | SKU Service Value unique identifier.
    try {
      apiInstance.apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete(contentType, accept, skuServiceValueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceValueApi#apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete");
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
| **skuServiceValueId** | **Integer**| SKU Service Value unique identifier. | |

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

<a id="apiCatalogPvtSkuservicevalueSkuServiceValueIdGet"></a>
# **apiCatalogPvtSkuservicevalueSkuServiceValueIdGet**
> SKUServiceValueResponse apiCatalogPvtSkuservicevalueSkuServiceValueIdGet(contentType, accept, skuServiceValueId)

Get SKU Service Value

Retrieves an existing SKU Service Value.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceValueApi;

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

    SkuServiceValueApi apiInstance = new SkuServiceValueApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceValueId = 1; // Integer | SKU Service Value unique identifier.
    try {
      SKUServiceValueResponse result = apiInstance.apiCatalogPvtSkuservicevalueSkuServiceValueIdGet(contentType, accept, skuServiceValueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceValueApi#apiCatalogPvtSkuservicevalueSkuServiceValueIdGet");
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
| **skuServiceValueId** | **Integer**| SKU Service Value unique identifier. | |

### Return type

[**SKUServiceValueResponse**](SKUServiceValueResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuservicevalueSkuServiceValueIdPut"></a>
# **apiCatalogPvtSkuservicevalueSkuServiceValueIdPut**
> SKUServiceValueResponse apiCatalogPvtSkuservicevalueSkuServiceValueIdPut(contentType, accept, skuServiceValueId, skUServiceValueRequest)

Update SKU Service Value

Updates an existing SKU Service Value.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceValueApi;

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

    SkuServiceValueApi apiInstance = new SkuServiceValueApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceValueId = 1; // Integer | SKU Service Value unique identifier.
    SKUServiceValueRequest skUServiceValueRequest = new SKUServiceValueRequest(); // SKUServiceValueRequest | 
    try {
      SKUServiceValueResponse result = apiInstance.apiCatalogPvtSkuservicevalueSkuServiceValueIdPut(contentType, accept, skuServiceValueId, skUServiceValueRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceValueApi#apiCatalogPvtSkuservicevalueSkuServiceValueIdPut");
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
| **skuServiceValueId** | **Integer**| SKU Service Value unique identifier. | |
| **skUServiceValueRequest** | [**SKUServiceValueRequest**](SKUServiceValueRequest.md)|  | [optional] |

### Return type

[**SKUServiceValueResponse**](SKUServiceValueResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

