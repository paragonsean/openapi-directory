# ConfigurableProductsSkuChildrenApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurableProductLinkManagementV1GetChildrenGet**](ConfigurableProductsSkuChildrenApi.md#configurableProductLinkManagementV1GetChildrenGet) | **GET** /V1/configurable-products/{sku}/children | configurable-products/{sku}/children |


<a id="configurableProductLinkManagementV1GetChildrenGet"></a>
# **configurableProductLinkManagementV1GetChildrenGet**
> List&lt;CatalogDataProductInterface&gt; configurableProductLinkManagementV1GetChildrenGet(sku)

configurable-products/{sku}/children

Get all children for Configurable product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsSkuChildrenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsSkuChildrenApi apiInstance = new ConfigurableProductsSkuChildrenApi(defaultClient);
    String sku = "sku_example"; // String | 
    try {
      List<CatalogDataProductInterface> result = apiInstance.configurableProductLinkManagementV1GetChildrenGet(sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsSkuChildrenApi#configurableProductLinkManagementV1GetChildrenGet");
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

[**List&lt;CatalogDataProductInterface&gt;**](CatalogDataProductInterface.md)

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

