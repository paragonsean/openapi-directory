# ConfigurableProductsSkuOptionsAllApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurableProductOptionRepositoryV1GetListGet**](ConfigurableProductsSkuOptionsAllApi.md#configurableProductOptionRepositoryV1GetListGet) | **GET** /V1/configurable-products/{sku}/options/all | configurable-products/{sku}/options/all |


<a id="configurableProductOptionRepositoryV1GetListGet"></a>
# **configurableProductOptionRepositoryV1GetListGet**
> List&lt;ConfigurableProductDataOptionInterface&gt; configurableProductOptionRepositoryV1GetListGet(sku)

configurable-products/{sku}/options/all

Get all options for configurable product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsSkuOptionsAllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsSkuOptionsAllApi apiInstance = new ConfigurableProductsSkuOptionsAllApi(defaultClient);
    String sku = "sku_example"; // String | 
    try {
      List<ConfigurableProductDataOptionInterface> result = apiInstance.configurableProductOptionRepositoryV1GetListGet(sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsSkuOptionsAllApi#configurableProductOptionRepositoryV1GetListGet");
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

[**List&lt;ConfigurableProductDataOptionInterface&gt;**](ConfigurableProductDataOptionInterface.md)

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

