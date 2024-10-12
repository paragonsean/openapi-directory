# SkuServiceTypeApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSkuservicetypePost**](SkuServiceTypeApi.md#apiCatalogPvtSkuservicetypePost) | **POST** /api/catalog/pvt/skuservicetype | Create SKU Service Type |
| [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete**](SkuServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete) | **DELETE** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Delete SKU Service Type |
| [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet**](SkuServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet) | **GET** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Get SKU Service Type |
| [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut**](SkuServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut) | **PUT** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Update SKU Service Type |


<a id="apiCatalogPvtSkuservicetypePost"></a>
# **apiCatalogPvtSkuservicetypePost**
> SKUServiceTypeResponse apiCatalogPvtSkuservicetypePost(contentType, accept, skUServiceTypeRequest)

Create SKU Service Type

Creates a new SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Test API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Teste API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceTypeApi;

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

    SkuServiceTypeApi apiInstance = new SkuServiceTypeApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    SKUServiceTypeRequest skUServiceTypeRequest = new SKUServiceTypeRequest(); // SKUServiceTypeRequest | 
    try {
      SKUServiceTypeResponse result = apiInstance.apiCatalogPvtSkuservicetypePost(contentType, accept, skUServiceTypeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceTypeApi#apiCatalogPvtSkuservicetypePost");
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
| **skUServiceTypeRequest** | [**SKUServiceTypeRequest**](SKUServiceTypeRequest.md)|  | [optional] |

### Return type

[**SKUServiceTypeResponse**](SKUServiceTypeResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete"></a>
# **apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete**
> apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete(contentType, accept, skuServiceTypeId)

Delete SKU Service Type

Deletes an existing SKU Service Type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceTypeApi;

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

    SkuServiceTypeApi apiInstance = new SkuServiceTypeApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceTypeId = 1; // Integer | SKU Service Type unique identifier.
    try {
      apiInstance.apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete(contentType, accept, skuServiceTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceTypeApi#apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete");
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
| **skuServiceTypeId** | **Integer**| SKU Service Type unique identifier. | |

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

<a id="apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet"></a>
# **apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet**
> SKUServiceTypeResponse apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet(contentType, accept, skuServiceTypeId)

Get SKU Service Type

Retrieves information about an existing SKU Service Type.   ## Response body example:    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test API SKU Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceTypeApi;

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

    SkuServiceTypeApi apiInstance = new SkuServiceTypeApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceTypeId = 1; // Integer | SKU Service Type unique identifier.
    try {
      SKUServiceTypeResponse result = apiInstance.apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet(contentType, accept, skuServiceTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceTypeApi#apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet");
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
| **skuServiceTypeId** | **Integer**| SKU Service Type unique identifier. | |

### Return type

[**SKUServiceTypeResponse**](SKUServiceTypeResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut"></a>
# **apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut**
> SKUServiceTypeResponse apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut(contentType, accept, skuServiceTypeId, skUServiceTypeRequest)

Update SKU Service Type

Updates an existing SKU Service Type.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Test API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Teste API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceTypeApi;

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

    SkuServiceTypeApi apiInstance = new SkuServiceTypeApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceTypeId = 1; // Integer | SKU Service Type unique identifier.
    SKUServiceTypeRequest skUServiceTypeRequest = new SKUServiceTypeRequest(); // SKUServiceTypeRequest | 
    try {
      SKUServiceTypeResponse result = apiInstance.apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut(contentType, accept, skuServiceTypeId, skUServiceTypeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceTypeApi#apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut");
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
| **skuServiceTypeId** | **Integer**| SKU Service Type unique identifier. | |
| **skUServiceTypeRequest** | [**SKUServiceTypeRequest**](SKUServiceTypeRequest.md)|  | [optional] |

### Return type

[**SKUServiceTypeResponse**](SKUServiceTypeResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

