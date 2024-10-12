# SkuFileApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut**](SkuFileApi.md#apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut) | **PUT** /api/catalog/pvt/stockkeepingunit/copy/{skuIdfrom}/{skuIdto}/file/ | Copy Files from an SKU to another SKU |
| [**apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete**](SkuFileApi.md#apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/disassociate/{skuId}/file/{skuFileId} | Disassociate SKU File |
| [**apiCatalogPvtStockkeepingunitSkuIdFileDelete**](SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Delete All SKU Files |
| [**apiCatalogPvtStockkeepingunitSkuIdFileGet**](SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Get SKU Files |
| [**apiCatalogPvtStockkeepingunitSkuIdFilePost**](SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFilePost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Create SKU File |
| [**apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete**](SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId} | Delete SKU Image File |
| [**apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut**](SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId} | Update SKU File |


<a id="apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut"></a>
# **apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut**
> List&lt;ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner&gt; apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(contentType, accept, skuIdfrom, skuIdto)

Copy Files from an SKU to another SKU

Copy all existing files from an SKU to another SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1964,          \&quot;ArchiveId\&quot;: 155404,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;\&quot;      },      {          \&quot;Id\&quot;: 1965,          \&quot;ArchiveId\&quot;: 155429,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuFileApi;

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

    SkuFileApi apiInstance = new SkuFileApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuIdfrom = 1; // Integer | __Origin__ SKU’s unique numerical identifier.
    Integer skuIdto = 2; // Integer | __Target__ SKU’s unique numerical identifier.
    try {
      List<ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner> result = apiInstance.apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(contentType, accept, skuIdfrom, skuIdto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuFileApi#apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut");
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
| **skuIdfrom** | **Integer**| __Origin__ SKU’s unique numerical identifier. | |
| **skuIdto** | **Integer**| __Target__ SKU’s unique numerical identifier. | |

### Return type

[**List&lt;ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner&gt;**](ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete"></a>
# **apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete**
> apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId)

Disassociate SKU File

Disassociates an SKU File from an SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuFileApi;

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

    SkuFileApi apiInstance = new SkuFileApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    Integer skuFileId = 32; // Integer | ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the `Id` field.
    try {
      apiInstance.apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuFileApi#apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete");
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
| **skuFileId** | **Integer**| ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. | |

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

<a id="apiCatalogPvtStockkeepingunitSkuIdFileDelete"></a>
# **apiCatalogPvtStockkeepingunitSkuIdFileDelete**
> apiCatalogPvtStockkeepingunitSkuIdFileDelete(contentType, accept, skuId)

Delete All SKU Files

Deletes all SKU Image Files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuFileApi;

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

    SkuFileApi apiInstance = new SkuFileApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtStockkeepingunitSkuIdFileDelete(contentType, accept, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuFileApi#apiCatalogPvtStockkeepingunitSkuIdFileDelete");
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

<a id="apiCatalogPvtStockkeepingunitSkuIdFileGet"></a>
# **apiCatalogPvtStockkeepingunitSkuIdFileGet**
> List&lt;ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner&gt; apiCatalogPvtStockkeepingunitSkuIdFileGet(contentType, accept, skuId)

Get SKU Files

Gets general information about all Files in the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 549,          \&quot;ArchiveId\&quot;: 155485,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;chimera-cat-quimera-5\&quot;,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;miau\&quot;      },      {          \&quot;Id\&quot;: 550,          \&quot;ArchiveId\&quot;: 155486,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Gato-siames\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;Gato siames\&quot;      },      {          \&quot;Id\&quot;: 555,          \&quot;ArchiveId\&quot;: 155491,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Cat-Sleeping-Pics\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: null      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuFileApi;

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

    SkuFileApi apiInstance = new SkuFileApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    try {
      List<ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner> result = apiInstance.apiCatalogPvtStockkeepingunitSkuIdFileGet(contentType, accept, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuFileApi#apiCatalogPvtStockkeepingunitSkuIdFileGet");
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

[**List&lt;ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner&gt;**](ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitSkuIdFilePost"></a>
# **apiCatalogPvtStockkeepingunitSkuIdFilePost**
> ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response apiCatalogPvtStockkeepingunitSkuIdFilePost(contentType, accept, skuId, skUFileURL)

Create SKU File

Creates a new Image for an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;Text\&quot;: null,        \&quot;Url\&quot;: \&quot;https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\&quot;          }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {        \&quot;Id\&quot;: 503,        \&quot;ArchiveId\&quot;: 155491,        \&quot;SkuId\&quot;: 1,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuFileApi;

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

    SkuFileApi apiInstance = new SkuFileApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 123456; // Integer | SKU’s unique numerical identifier.
    SKUFileURL skUFileURL = new SKUFileURL(); // SKUFileURL | 
    try {
      ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response result = apiInstance.apiCatalogPvtStockkeepingunitSkuIdFilePost(contentType, accept, skuId, skUFileURL);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuFileApi#apiCatalogPvtStockkeepingunitSkuIdFilePost");
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
| **skUFileURL** | [**SKUFileURL**](SKUFileURL.md)|  | [optional] |

### Return type

[**ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response**](ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json, form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete"></a>
# **apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete**
> apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId)

Delete SKU Image File

Deletes a specific SKU Image File.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuFileApi;

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

    SkuFileApi apiInstance = new SkuFileApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    Integer skuFileId = 1; // Integer | ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the `Id` field.
    try {
      apiInstance.apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuFileApi#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete");
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
| **skuFileId** | **Integer**| ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. | |

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

<a id="apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut"></a>
# **apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut**
> ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(contentType, accept, skuId, skuFileId, skUFileURL)

Update SKU File

Updates a new Image on an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null,      \&quot;Name\&quot;: \&quot;toilet-paper\&quot;,      \&quot;Text\&quot;: null,      \&quot;Url\&quot;: \&quot;https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 508,      \&quot;ArchiveId\&quot;: 155491,      \&quot;SkuId\&quot;: 7,      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuFileApi;

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

    SkuFileApi apiInstance = new SkuFileApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 123456; // Integer | SKU’s unique numerical identifier.
    Integer skuFileId = 517; // Integer | ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the `Id` field.
    SKUFileURL skUFileURL = new SKUFileURL(); // SKUFileURL | 
    try {
      ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response result = apiInstance.apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(contentType, accept, skuId, skuFileId, skUFileURL);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuFileApi#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut");
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
| **skuFileId** | **Integer**| ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. | |
| **skUFileURL** | [**SKUFileURL**](SKUFileURL.md)|  | [optional] |

### Return type

[**ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response**](ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

