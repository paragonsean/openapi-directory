# SkuSpecificationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete**](SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Delete all SKU Specifications |
| [**apiCatalogPvtStockkeepingunitSkuIdSpecificationGet**](SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Get SKU Specifications |
| [**apiCatalogPvtStockkeepingunitSkuIdSpecificationPost**](SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationPost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Associate SKU Specification |
| [**apiCatalogPvtStockkeepingunitSkuIdSpecificationPut**](SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Update SKU Specification |
| [**apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete**](SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/specification/{specificationId} | Delete SKU Specification |
| [**apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut**](SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/specificationvalue | Associate SKU specification using specification name and group name |


<a id="apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete"></a>
# **apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete**
> apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete(contentType, accept, skuId)

Delete all SKU Specifications

Deletes all SKU Specifications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSpecificationApi;

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

    SkuSpecificationApi apiInstance = new SkuSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete(contentType, accept, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSpecificationApi#apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete");
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

<a id="apiCatalogPvtStockkeepingunitSkuIdSpecificationGet"></a>
# **apiCatalogPvtStockkeepingunitSkuIdSpecificationGet**
> List&lt;SKUSpecificationResponse&gt; apiCatalogPvtStockkeepingunitSkuIdSpecificationGet(contentType, accept, skuId)

Get SKU Specifications

Retrieves information about an SKU&#39;s Specifications.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 427,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 32,          \&quot;FieldValueId\&quot;: 131,          \&quot;Text\&quot;: \&quot;500g\&quot;      },      {          \&quot;Id\&quot;: 428,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 40,          \&quot;FieldValueId\&quot;: 133,          \&quot;Text\&quot;: \&quot;A\&quot;      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSpecificationApi;

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

    SkuSpecificationApi apiInstance = new SkuSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    try {
      List<SKUSpecificationResponse> result = apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationGet(contentType, accept, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSpecificationApi#apiCatalogPvtStockkeepingunitSkuIdSpecificationGet");
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

[**List&lt;SKUSpecificationResponse&gt;**](SKUSpecificationResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitSkuIdSpecificationPost"></a>
# **apiCatalogPvtStockkeepingunitSkuIdSpecificationPost**
> SKUSpecificationResponse apiCatalogPvtStockkeepingunitSkuIdSpecificationPost(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest)

Associate SKU Specification

Associates a previously created Specification to an SKU.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 730,      \&quot;SkuId\&quot;: 31,      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138,      \&quot;Text\&quot;: \&quot;Size\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSpecificationApi;

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

    SkuSpecificationApi apiInstance = new SkuSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1234568387; // Integer | SKU’s unique numerical identifier.
    ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest = new ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest(); // ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest | 
    try {
      SKUSpecificationResponse result = apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationPost(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSpecificationApi#apiCatalogPvtStockkeepingunitSkuIdSpecificationPost");
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
| **apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest** | [**ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest**](ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest.md)|  | [optional] |

### Return type

[**SKUSpecificationResponse**](SKUSpecificationResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitSkuIdSpecificationPut"></a>
# **apiCatalogPvtStockkeepingunitSkuIdSpecificationPut**
> List&lt;SKUSpecificationResponse&gt; apiCatalogPvtStockkeepingunitSkuIdSpecificationPut(contentType, accept, skuId, requestBody)

Update SKU Specification

Updates an existing Specification on an existing SKU. This endpoint only updates the &#x60;FieldValueId&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSpecificationApi;

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

    SkuSpecificationApi apiInstance = new SkuSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 21; // Integer | SKU’s unique numerical identifier.
    RequestBody requestBody = new RequestBody(); // RequestBody | 
    try {
      List<SKUSpecificationResponse> result = apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationPut(contentType, accept, skuId, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSpecificationApi#apiCatalogPvtStockkeepingunitSkuIdSpecificationPut");
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
| **requestBody** | [**RequestBody**](RequestBody.md)|  | [optional] |

### Return type

[**List&lt;SKUSpecificationResponse&gt;**](SKUSpecificationResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete"></a>
# **apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete**
> apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(contentType, accept, skuId, specificationId)

Delete SKU Specification

Deletes a specific SKU Specification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSpecificationApi;

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

    SkuSpecificationApi apiInstance = new SkuSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    Integer specificationId = 1; // Integer | Specification’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(contentType, accept, skuId, specificationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSpecificationApi#apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete");
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
| **specificationId** | **Integer**| Specification’s unique numerical identifier. | |

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

<a id="apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut"></a>
# **apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut**
> List&lt;ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner&gt; apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest)

Associate SKU specification using specification name and group name

Associates a specification to an SKU using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Size\&quot;,      \&quot;GroupName\&quot;: \&quot;Sizes\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;M\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 419,          \&quot;SkuId\&quot;: 5,          \&quot;FieldId\&quot;: 22,          \&quot;FieldValueId\&quot;: 62,          \&quot;Text\&quot;: \&quot;M\&quot;      }  ]  &#x60;&#x60;&#x60;  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSpecificationApi;

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

    SkuSpecificationApi apiInstance = new SkuSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest = new ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest(); // ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest | 
    try {
      List<ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner> result = apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSpecificationApi#apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut");
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
| **apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest** | [**ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest**](ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest.md)|  | [optional] |

### Return type

[**List&lt;ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner&gt;**](ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

