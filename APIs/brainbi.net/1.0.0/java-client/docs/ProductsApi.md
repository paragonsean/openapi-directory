# ProductsApi

All URIs are relative to *http://,*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**betaScrapeProductCopy**](ProductsApi.md#betaScrapeProductCopy) | **GET** /api/analyze/pricing | [BETA] Scrape Product Copy |
| [**products**](ProductsApi.md#products) | **GET** /api/products | Products |
| [**products1**](ProductsApi.md#products1) | **DELETE** /api/products/1137 | Products |


<a id="betaScrapeProductCopy"></a>
# **betaScrapeProductCopy**
> betaScrapeProductCopy(url)

[BETA] Scrape Product Copy

To update a product, please use the listed attributes listed underneath. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String url = "https://www.apple.com/de/shop/buy-homepod/homepod-mini"; // String | 
    try {
      apiInstance.betaScrapeProductCopy(url);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#betaScrapeProductCopy");
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
| **url** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="products"></a>
# **products**
> products()

Products

This resource lists all products that are currently saved in you account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.products();
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#products");
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
| **** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="products1"></a>
# **products1**
> products1()

Products

Products

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.products1();
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#products1");
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
| **** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

