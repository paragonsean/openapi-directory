# OffersApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogSystemPubProductsOffersProductIdGet**](OffersApi.md#apiCatalogSystemPubProductsOffersProductIdGet) | **GET** /api/catalog_system/pub/products/offers/{productId} | Search Product offers |
| [**apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet**](OffersApi.md#apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet) | **GET** /api/catalog_system/pub/products/offers/{productId}/sku/{skuId} | Search SKU offers |


<a id="apiCatalogSystemPubProductsOffersProductIdGet"></a>
# **apiCatalogSystemPubProductsOffersProductIdGet**
> List&lt;ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner&gt; apiCatalogSystemPubProductsOffersProductIdGet(accept, contentType, productId)

Search Product offers

Retrieves existing offers of a specific product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OffersApi;

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

    OffersApi apiInstance = new OffersApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String productId = "3"; // String | Product unique number identifier.
    try {
      List<ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner> result = apiInstance.apiCatalogSystemPubProductsOffersProductIdGet(accept, contentType, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#apiCatalogSystemPubProductsOffersProductIdGet");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **String**| Product unique number identifier. | |

### Return type

[**List&lt;ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner&gt;**](ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet"></a>
# **apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet**
> List&lt;ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner&gt; apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet(accept, contentType, productId, skuId)

Search SKU offers

Retrieves existing offers of a specific SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OffersApi;

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

    OffersApi apiInstance = new OffersApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String productId = "3"; // String | Product unique number identifier.
    String skuId = "5"; // String | Product unique number identifier.
    try {
      List<ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner> result = apiInstance.apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet(accept, contentType, productId, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **String**| Product unique number identifier. | |
| **skuId** | **String**| Product unique number identifier. | |

### Return type

[**List&lt;ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner&gt;**](ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

