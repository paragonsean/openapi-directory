# ProductApi

All URIs are relative to *https://api.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productListingsAll**](ProductApi.md#productListingsAll) | **GET** /ecosystems/{ecosystem_id}/products/{id}/listings | List product listings |
| [**productsAll**](ProductApi.md#productsAll) | **GET** /ecosystems/{ecosystem_id}/products | List products |
| [**productsOne**](ProductApi.md#productsOne) | **GET** /ecosystems/{ecosystem_id}/products/{id} | Get product |


<a id="productListingsAll"></a>
# **productListingsAll**
> GetListingsResponse productListingsAll(ecosystemId, id, cursor, limit)

List product listings

List product listings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String id = "id_example"; // String | ID of the record you are acting upon.
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 50; // Integer | Number of records to return
    try {
      GetListingsResponse result = apiInstance.productListingsAll(ecosystemId, id, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productListingsAll");
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
| **ecosystemId** | **String**|  | |
| **id** | **String**| ID of the record you are acting upon. | |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of records to return | [optional] [default to 50] |

### Return type

[**GetListingsResponse**](GetListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listings |  -  |

<a id="productsAll"></a>
# **productsAll**
> GetProductsResponse productsAll(ecosystemId)

List products

List products

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    try {
      GetProductsResponse result = apiInstance.productsAll(ecosystemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productsAll");
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
| **ecosystemId** | **String**|  | |

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products |  -  |

<a id="productsOne"></a>
# **productsOne**
> GetProductResponse productsOne(ecosystemId, id)

Get product

Get product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String id = "id_example"; // String | ID of the record you are acting upon.
    try {
      GetProductResponse result = apiInstance.productsOne(ecosystemId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productsOne");
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
| **ecosystemId** | **String**|  | |
| **id** | **String**| ID of the record you are acting upon. | |

### Return type

[**GetProductResponse**](GetProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product |  -  |

