# ProductVariantsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsProductIdVariantsGet**](ProductVariantsApi.md#productsProductIdVariantsGet) | **GET** /products/{product_id}/variants | Get a product&#39;s variants |
| [**productsProductIdVariantsPost**](ProductVariantsApi.md#productsProductIdVariantsPost) | **POST** /products/{product_id}/variants | Add a new variant to a product |
| [**productsProductIdVariantsVariantTypeVariantIdDelete**](ProductVariantsApi.md#productsProductIdVariantsVariantTypeVariantIdDelete) | **DELETE** /products/{product_id}/variants/{variant_type}/{variant_id} | Delete a product variant |


<a id="productsProductIdVariantsGet"></a>
# **productsProductIdVariantsGet**
> ProductsProductIdVariantsGet200Response productsProductIdVariantsGet(productId)

Get a product&#39;s variants

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductVariantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ProductVariantsApi apiInstance = new ProductVariantsApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | 
    try {
      ProductsProductIdVariantsGet200Response result = apiInstance.productsProductIdVariantsGet(productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductVariantsApi#productsProductIdVariantsGet");
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
| **productId** | **UUID**|  | |

### Return type

[**ProductsProductIdVariantsGet200Response**](ProductsProductIdVariantsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="productsProductIdVariantsPost"></a>
# **productsProductIdVariantsPost**
> EmptySuccessResponse productsProductIdVariantsPost(productId, ratio, variantId, variantType, name)

Add a new variant to a product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductVariantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ProductVariantsApi apiInstance = new ProductVariantsApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | 
    BigDecimal ratio = new BigDecimal(78); // BigDecimal | 
    UUID variantId = UUID.randomUUID(); // UUID | 
    String variantType = "expense_line"; // String | 
    String name = "name_example"; // String | Filters by name
    try {
      EmptySuccessResponse result = apiInstance.productsProductIdVariantsPost(productId, ratio, variantId, variantType, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductVariantsApi#productsProductIdVariantsPost");
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
| **productId** | **UUID**|  | |
| **ratio** | **BigDecimal**|  | |
| **variantId** | **UUID**|  | |
| **variantType** | **String**|  | [enum: expense_line, vendor_product] |
| **name** | **String**| Filters by name | [optional] |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |

<a id="productsProductIdVariantsVariantTypeVariantIdDelete"></a>
# **productsProductIdVariantsVariantTypeVariantIdDelete**
> EmptySuccessResponse productsProductIdVariantsVariantTypeVariantIdDelete(productId, variantType, variantId)

Delete a product variant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductVariantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ProductVariantsApi apiInstance = new ProductVariantsApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | 
    String variantType = "expense_line"; // String | 
    UUID variantId = UUID.randomUUID(); // UUID | 
    try {
      EmptySuccessResponse result = apiInstance.productsProductIdVariantsVariantTypeVariantIdDelete(productId, variantType, variantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductVariantsApi#productsProductIdVariantsVariantTypeVariantIdDelete");
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
| **productId** | **UUID**|  | |
| **variantType** | **String**|  | [enum: expense_line, vendor_product] |
| **variantId** | **UUID**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |

