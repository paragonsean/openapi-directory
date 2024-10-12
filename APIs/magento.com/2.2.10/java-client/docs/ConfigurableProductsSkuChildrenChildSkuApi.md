# ConfigurableProductsSkuChildrenChildSkuApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurableProductLinkManagementV1RemoveChildDelete**](ConfigurableProductsSkuChildrenChildSkuApi.md#configurableProductLinkManagementV1RemoveChildDelete) | **DELETE** /V1/configurable-products/{sku}/children/{childSku} | configurable-products/{sku}/children/{childSku} |


<a id="configurableProductLinkManagementV1RemoveChildDelete"></a>
# **configurableProductLinkManagementV1RemoveChildDelete**
> Boolean configurableProductLinkManagementV1RemoveChildDelete(sku, childSku)

configurable-products/{sku}/children/{childSku}

Remove configurable product option

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsSkuChildrenChildSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsSkuChildrenChildSkuApi apiInstance = new ConfigurableProductsSkuChildrenChildSkuApi(defaultClient);
    String sku = "sku_example"; // String | 
    String childSku = "childSku_example"; // String | 
    try {
      Boolean result = apiInstance.configurableProductLinkManagementV1RemoveChildDelete(sku, childSku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsSkuChildrenChildSkuApi#configurableProductLinkManagementV1RemoveChildDelete");
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
| **childSku** | **String**|  | |

### Return type

**Boolean**

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

