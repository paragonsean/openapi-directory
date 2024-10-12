# BundleProductsSkuOptionsOptionIdChildrenChildSkuApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductLinkManagementV1RemoveChildDelete**](BundleProductsSkuOptionsOptionIdChildrenChildSkuApi.md#bundleProductLinkManagementV1RemoveChildDelete) | **DELETE** /V1/bundle-products/{sku}/options/{optionId}/children/{childSku} | bundle-products/{sku}/options/{optionId}/children/{childSku} |


<a id="bundleProductLinkManagementV1RemoveChildDelete"></a>
# **bundleProductLinkManagementV1RemoveChildDelete**
> Boolean bundleProductLinkManagementV1RemoveChildDelete(sku, optionId, childSku)

bundle-products/{sku}/options/{optionId}/children/{childSku}

Remove product from Bundle product option

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsSkuOptionsOptionIdChildrenChildSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsSkuOptionsOptionIdChildrenChildSkuApi apiInstance = new BundleProductsSkuOptionsOptionIdChildrenChildSkuApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer optionId = 56; // Integer | 
    String childSku = "childSku_example"; // String | 
    try {
      Boolean result = apiInstance.bundleProductLinkManagementV1RemoveChildDelete(sku, optionId, childSku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsSkuOptionsOptionIdChildrenChildSkuApi#bundleProductLinkManagementV1RemoveChildDelete");
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
| **optionId** | **Integer**|  | |
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

