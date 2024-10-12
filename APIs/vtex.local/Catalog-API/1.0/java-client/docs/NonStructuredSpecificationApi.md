# NonStructuredSpecificationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSpecificationNonstructuredDelete**](NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredDelete) | **DELETE** /api/catalog/pvt/specification/nonstructured | Delete Non Structured Specification by SKU ID |
| [**apiCatalogPvtSpecificationNonstructuredGet**](NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredGet) | **GET** /api/catalog/pvt/specification/nonstructured | Get Non Structured Specification by SKU ID |
| [**apiCatalogPvtSpecificationNonstructuredIdDelete**](NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredIdDelete) | **DELETE** /api/catalog/pvt/specification/nonstructured/{Id} | Delete Non Structured Specification |
| [**apiCatalogPvtSpecificationNonstructuredIdGet**](NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredIdGet) | **GET** /api/catalog/pvt/specification/nonstructured/{Id} | Get Non Structured Specification by ID |


<a id="apiCatalogPvtSpecificationNonstructuredDelete"></a>
# **apiCatalogPvtSpecificationNonstructuredDelete**
> apiCatalogPvtSpecificationNonstructuredDelete(contentType, accept, skuId)

Delete Non Structured Specification by SKU ID

Deletes unmapped Specifications of a Seller&#39;S SKU in a Marketplace by SKU ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NonStructuredSpecificationApi;

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

    NonStructuredSpecificationApi apiInstance = new NonStructuredSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtSpecificationNonstructuredDelete(contentType, accept, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NonStructuredSpecificationApi#apiCatalogPvtSpecificationNonstructuredDelete");
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
| **skuId** | **Integer**| SKU’s unique numerical identifier. | |

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

<a id="apiCatalogPvtSpecificationNonstructuredGet"></a>
# **apiCatalogPvtSpecificationNonstructuredGet**
> List&lt;ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner&gt; apiCatalogPvtSpecificationNonstructuredGet(contentType, accept, skuId)

Get Non Structured Specification by SKU ID

Gets general information about unmapped Specifications of a Seller&#39;s SKU in a Marketplace by SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  [  {      \&quot;Id\&quot;: 1010,      \&quot;SkuId\&quot;: 310119072,      \&quot;SpecificationName\&quot;: \&quot;size\&quot;,      \&quot;SpecificationValue\&quot;: \&quot;Small\&quot;  }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NonStructuredSpecificationApi;

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

    NonStructuredSpecificationApi apiInstance = new NonStructuredSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    try {
      List<ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner> result = apiInstance.apiCatalogPvtSpecificationNonstructuredGet(contentType, accept, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NonStructuredSpecificationApi#apiCatalogPvtSpecificationNonstructuredGet");
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
| **skuId** | **Integer**| SKU’s unique numerical identifier. | |

### Return type

[**List&lt;ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner&gt;**](ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSpecificationNonstructuredIdDelete"></a>
# **apiCatalogPvtSpecificationNonstructuredIdDelete**
> apiCatalogPvtSpecificationNonstructuredIdDelete(contentType, accept, id)

Delete Non Structured Specification

Deletes unmapped Specifications of a Seller&#39;S SKU in a Marketplace by its unique ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NonStructuredSpecificationApi;

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

    NonStructuredSpecificationApi apiInstance = new NonStructuredSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer id = 1; // Integer | Non Structured Specification’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtSpecificationNonstructuredIdDelete(contentType, accept, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling NonStructuredSpecificationApi#apiCatalogPvtSpecificationNonstructuredIdDelete");
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
| **id** | **Integer**| Non Structured Specification’s unique numerical identifier. | |

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

<a id="apiCatalogPvtSpecificationNonstructuredIdGet"></a>
# **apiCatalogPvtSpecificationNonstructuredIdGet**
> List&lt;ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner&gt; apiCatalogPvtSpecificationNonstructuredIdGet(contentType, accept, id)

Get Non Structured Specification by ID

Retrieves general information about unmapped Specifications of a Seller&#39;s SKU in a Marketplace.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1010,      \&quot;SkuId\&quot;: 310119072,      \&quot;SpecificationName\&quot;: \&quot;size\&quot;,      \&quot;SpecificationValue\&quot;: \&quot;Small\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NonStructuredSpecificationApi;

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

    NonStructuredSpecificationApi apiInstance = new NonStructuredSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer id = 1010; // Integer | Non Structured Specification’s unique numerical identifier.
    try {
      List<ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner> result = apiInstance.apiCatalogPvtSpecificationNonstructuredIdGet(contentType, accept, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NonStructuredSpecificationApi#apiCatalogPvtSpecificationNonstructuredIdGet");
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
| **id** | **Integer**| Non Structured Specification’s unique numerical identifier. | |

### Return type

[**List&lt;ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner&gt;**](ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

