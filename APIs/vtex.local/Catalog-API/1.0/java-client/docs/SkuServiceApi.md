# SkuServiceApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSkuservicePost**](SkuServiceApi.md#apiCatalogPvtSkuservicePost) | **POST** /api/catalog/pvt/skuservice | Associate SKU Service |
| [**apiCatalogPvtSkuserviceSkuServiceIdDelete**](SkuServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdDelete) | **DELETE** /api/catalog/pvt/skuservice/{skuServiceId} | Dissociate SKU Service |
| [**apiCatalogPvtSkuserviceSkuServiceIdGet**](SkuServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdGet) | **GET** /api/catalog/pvt/skuservice/{skuServiceId} | Get SKU Service |
| [**apiCatalogPvtSkuserviceSkuServiceIdPut**](SkuServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdPut) | **PUT** /api/catalog/pvt/skuservice/{skuServiceId} | Update SKU Service |


<a id="apiCatalogPvtSkuservicePost"></a>
# **apiCatalogPvtSkuservicePost**
> SKUService apiCatalogPvtSkuservicePost(contentType, accept, requestBody3)

Associate SKU Service

Associates an SKU Service to an SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceApi;

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

    SkuServiceApi apiInstance = new SkuServiceApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    RequestBody3 requestBody3 = new RequestBody3(); // RequestBody3 | 
    try {
      SKUService result = apiInstance.apiCatalogPvtSkuservicePost(contentType, accept, requestBody3);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceApi#apiCatalogPvtSkuservicePost");
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
| **requestBody3** | [**RequestBody3**](RequestBody3.md)|  | [optional] |

### Return type

[**SKUService**](SKUService.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuserviceSkuServiceIdDelete"></a>
# **apiCatalogPvtSkuserviceSkuServiceIdDelete**
> apiCatalogPvtSkuserviceSkuServiceIdDelete(contentType, accept, skuServiceId)

Dissociate SKU Service

Dissociates an SKU Service from an SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceApi;

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

    SkuServiceApi apiInstance = new SkuServiceApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceId = 1; // Integer | SKU Service unique identifier.
    try {
      apiInstance.apiCatalogPvtSkuserviceSkuServiceIdDelete(contentType, accept, skuServiceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceApi#apiCatalogPvtSkuserviceSkuServiceIdDelete");
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
| **skuServiceId** | **Integer**| SKU Service unique identifier. | |

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

<a id="apiCatalogPvtSkuserviceSkuServiceIdGet"></a>
# **apiCatalogPvtSkuserviceSkuServiceIdGet**
> SKUService apiCatalogPvtSkuserviceSkuServiceIdGet(contentType, accept, skuServiceId)

Get SKU Service

Retrieves an SKU Service.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1,      \&quot;SkuServiceValueId\&quot;: 1,      \&quot;SkuId\&quot;: 1,      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceApi;

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

    SkuServiceApi apiInstance = new SkuServiceApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceId = 5; // Integer | SKU Service unique identifier.
    try {
      SKUService result = apiInstance.apiCatalogPvtSkuserviceSkuServiceIdGet(contentType, accept, skuServiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceApi#apiCatalogPvtSkuserviceSkuServiceIdGet");
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
| **skuServiceId** | **Integer**| SKU Service unique identifier. | |

### Return type

[**SKUService**](SKUService.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuserviceSkuServiceIdPut"></a>
# **apiCatalogPvtSkuserviceSkuServiceIdPut**
> SKUService apiCatalogPvtSkuserviceSkuServiceIdPut(contentType, accept, skuServiceId, requestBody4)

Update SKU Service

Updates an SKU Service.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1,      \&quot;SkuServiceValueId\&quot;: 1,      \&quot;SkuId\&quot;: 1,      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceApi;

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

    SkuServiceApi apiInstance = new SkuServiceApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceId = 5; // Integer | SKU Service unique identifier.
    RequestBody4 requestBody4 = new RequestBody4(); // RequestBody4 | 
    try {
      SKUService result = apiInstance.apiCatalogPvtSkuserviceSkuServiceIdPut(contentType, accept, skuServiceId, requestBody4);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceApi#apiCatalogPvtSkuserviceSkuServiceIdPut");
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
| **skuServiceId** | **Integer**| SKU Service unique identifier. | |
| **requestBody4** | [**RequestBody4**](RequestBody4.md)|  | [optional] |

### Return type

[**SKUService**](SKUService.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

