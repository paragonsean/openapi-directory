# ProductsTierPricesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogTierPriceStorageV1ReplacePut**](ProductsTierPricesApi.md#catalogTierPriceStorageV1ReplacePut) | **PUT** /V1/products/tier-prices | products/tier-prices |
| [**catalogTierPriceStorageV1UpdatePost**](ProductsTierPricesApi.md#catalogTierPriceStorageV1UpdatePost) | **POST** /V1/products/tier-prices | products/tier-prices |


<a id="catalogTierPriceStorageV1ReplacePut"></a>
# **catalogTierPriceStorageV1ReplacePut**
> List&lt;CatalogDataPriceUpdateResultInterface&gt; catalogTierPriceStorageV1ReplacePut(catalogTierPriceStorageV1ReplacePutRequest)

products/tier-prices

Remove existing tier prices and replace them with the new ones. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from replace list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsTierPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsTierPricesApi apiInstance = new ProductsTierPricesApi(defaultClient);
    CatalogTierPriceStorageV1ReplacePutRequest catalogTierPriceStorageV1ReplacePutRequest = new CatalogTierPriceStorageV1ReplacePutRequest(); // CatalogTierPriceStorageV1ReplacePutRequest | 
    try {
      List<CatalogDataPriceUpdateResultInterface> result = apiInstance.catalogTierPriceStorageV1ReplacePut(catalogTierPriceStorageV1ReplacePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsTierPricesApi#catalogTierPriceStorageV1ReplacePut");
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
| **catalogTierPriceStorageV1ReplacePutRequest** | [**CatalogTierPriceStorageV1ReplacePutRequest**](CatalogTierPriceStorageV1ReplacePutRequest.md)|  | [optional] |

### Return type

[**List&lt;CatalogDataPriceUpdateResultInterface&gt;**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="catalogTierPriceStorageV1UpdatePost"></a>
# **catalogTierPriceStorageV1UpdatePost**
> List&lt;CatalogDataPriceUpdateResultInterface&gt; catalogTierPriceStorageV1UpdatePost(catalogTierPriceStorageV1ReplacePutRequest)

products/tier-prices

Add or update product prices. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsTierPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsTierPricesApi apiInstance = new ProductsTierPricesApi(defaultClient);
    CatalogTierPriceStorageV1ReplacePutRequest catalogTierPriceStorageV1ReplacePutRequest = new CatalogTierPriceStorageV1ReplacePutRequest(); // CatalogTierPriceStorageV1ReplacePutRequest | 
    try {
      List<CatalogDataPriceUpdateResultInterface> result = apiInstance.catalogTierPriceStorageV1UpdatePost(catalogTierPriceStorageV1ReplacePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsTierPricesApi#catalogTierPriceStorageV1UpdatePost");
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
| **catalogTierPriceStorageV1ReplacePutRequest** | [**CatalogTierPriceStorageV1ReplacePutRequest**](CatalogTierPriceStorageV1ReplacePutRequest.md)|  | [optional] |

### Return type

[**List&lt;CatalogDataPriceUpdateResultInterface&gt;**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

