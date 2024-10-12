# ProductsSkuOptionsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductCustomOptionRepositoryV1GetListGet**](ProductsSkuOptionsApi.md#catalogProductCustomOptionRepositoryV1GetListGet) | **GET** /V1/products/{sku}/options | products/{sku}/options |


<a id="catalogProductCustomOptionRepositoryV1GetListGet"></a>
# **catalogProductCustomOptionRepositoryV1GetListGet**
> List&lt;CatalogDataProductCustomOptionInterface&gt; catalogProductCustomOptionRepositoryV1GetListGet(sku)

products/{sku}/options

Get the list of custom options for a specific product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuOptionsApi apiInstance = new ProductsSkuOptionsApi(defaultClient);
    String sku = "sku_example"; // String | 
    try {
      List<CatalogDataProductCustomOptionInterface> result = apiInstance.catalogProductCustomOptionRepositoryV1GetListGet(sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuOptionsApi#catalogProductCustomOptionRepositoryV1GetListGet");
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
| **sku** | **String**|  | |

### Return type

[**List&lt;CatalogDataProductCustomOptionInterface&gt;**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

