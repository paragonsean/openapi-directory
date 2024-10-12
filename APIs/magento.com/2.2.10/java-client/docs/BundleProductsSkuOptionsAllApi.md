# BundleProductsSkuOptionsAllApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductOptionRepositoryV1GetListGet**](BundleProductsSkuOptionsAllApi.md#bundleProductOptionRepositoryV1GetListGet) | **GET** /V1/bundle-products/{sku}/options/all | bundle-products/{sku}/options/all |


<a id="bundleProductOptionRepositoryV1GetListGet"></a>
# **bundleProductOptionRepositoryV1GetListGet**
> List&lt;BundleDataOptionInterface&gt; bundleProductOptionRepositoryV1GetListGet(sku)

bundle-products/{sku}/options/all

Get all options for bundle product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsSkuOptionsAllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsSkuOptionsAllApi apiInstance = new BundleProductsSkuOptionsAllApi(defaultClient);
    String sku = "sku_example"; // String | 
    try {
      List<BundleDataOptionInterface> result = apiInstance.bundleProductOptionRepositoryV1GetListGet(sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsSkuOptionsAllApi#bundleProductOptionRepositoryV1GetListGet");
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

[**List&lt;BundleDataOptionInterface&gt;**](BundleDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

