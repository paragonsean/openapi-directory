# BundleProductsOptionsTypesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductOptionTypeListV1GetItemsGet**](BundleProductsOptionsTypesApi.md#bundleProductOptionTypeListV1GetItemsGet) | **GET** /V1/bundle-products/options/types | bundle-products/options/types |


<a id="bundleProductOptionTypeListV1GetItemsGet"></a>
# **bundleProductOptionTypeListV1GetItemsGet**
> List&lt;BundleDataOptionTypeInterface&gt; bundleProductOptionTypeListV1GetItemsGet()

bundle-products/options/types

Get all types for options for bundle products

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsOptionsTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsOptionsTypesApi apiInstance = new BundleProductsOptionsTypesApi(defaultClient);
    try {
      List<BundleDataOptionTypeInterface> result = apiInstance.bundleProductOptionTypeListV1GetItemsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsOptionsTypesApi#bundleProductOptionTypeListV1GetItemsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;BundleDataOptionTypeInterface&gt;**](BundleDataOptionTypeInterface.md)

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

