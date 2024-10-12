# SkuServiceAttachmentApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSkuservicetypeattachmentDelete**](SkuServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentDelete) | **DELETE** /api/catalog/pvt/skuservicetypeattachment | Dissociate Attachment by Attachment ID or SKU Service Type ID |
| [**apiCatalogPvtSkuservicetypeattachmentPost**](SkuServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentPost) | **POST** /api/catalog/pvt/skuservicetypeattachment | Associate SKU Service Attachment |
| [**apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete**](SkuServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete) | **DELETE** /api/catalog/pvt/skuservicetypeattachment/{skuServiceTypeAttachmentId} | Dissociate Attachment from SKU Service Type |


<a id="apiCatalogPvtSkuservicetypeattachmentDelete"></a>
# **apiCatalogPvtSkuservicetypeattachmentDelete**
> apiCatalogPvtSkuservicetypeattachmentDelete(contentType, accept, attachmentId, skuServiceTypeId)

Dissociate Attachment by Attachment ID or SKU Service Type ID

Dissociates an Attachment by its Attachment ID or SKU Service Type ID from an SKU Service Type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceAttachmentApi;

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

    SkuServiceAttachmentApi apiInstance = new SkuServiceAttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer attachmentId = 1; // Integer | SKU Service Attachment unique identifier.
    Integer skuServiceTypeId = 1; // Integer | SKU Service Type unique identifier.
    try {
      apiInstance.apiCatalogPvtSkuservicetypeattachmentDelete(contentType, accept, attachmentId, skuServiceTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceAttachmentApi#apiCatalogPvtSkuservicetypeattachmentDelete");
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
| **attachmentId** | **Integer**| SKU Service Attachment unique identifier. | [optional] |
| **skuServiceTypeId** | **Integer**| SKU Service Type unique identifier. | [optional] |

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

<a id="apiCatalogPvtSkuservicetypeattachmentPost"></a>
# **apiCatalogPvtSkuservicetypeattachmentPost**
> ApiCatalogPvtSkuservicetypeattachmentPost200Response apiCatalogPvtSkuservicetypeattachmentPost(contentType, accept, requestBody5)

Associate SKU Service Attachment

Associates an Attachment for an existing SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceAttachmentApi;

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

    SkuServiceAttachmentApi apiInstance = new SkuServiceAttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    RequestBody5 requestBody5 = new RequestBody5(); // RequestBody5 | 
    try {
      ApiCatalogPvtSkuservicetypeattachmentPost200Response result = apiInstance.apiCatalogPvtSkuservicetypeattachmentPost(contentType, accept, requestBody5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceAttachmentApi#apiCatalogPvtSkuservicetypeattachmentPost");
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
| **requestBody5** | [**RequestBody5**](RequestBody5.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSkuservicetypeattachmentPost200Response**](ApiCatalogPvtSkuservicetypeattachmentPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete"></a>
# **apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete**
> apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete(contentType, accept, skuServiceTypeAttachmentId)

Dissociate Attachment from SKU Service Type

Dissociates an Attachment from an SKU Service Type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuServiceAttachmentApi;

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

    SkuServiceAttachmentApi apiInstance = new SkuServiceAttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuServiceTypeAttachmentId = 1; // Integer | SKU Service Attachment unique identifier.
    try {
      apiInstance.apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete(contentType, accept, skuServiceTypeAttachmentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuServiceAttachmentApi#apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete");
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
| **skuServiceTypeAttachmentId** | **Integer**| SKU Service Attachment unique identifier. | |

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

