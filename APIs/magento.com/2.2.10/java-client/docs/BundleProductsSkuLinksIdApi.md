# BundleProductsSkuLinksIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductLinkManagementV1SaveChildPut**](BundleProductsSkuLinksIdApi.md#bundleProductLinkManagementV1SaveChildPut) | **PUT** /V1/bundle-products/{sku}/links/{id} | bundle-products/{sku}/links/{id} |


<a id="bundleProductLinkManagementV1SaveChildPut"></a>
# **bundleProductLinkManagementV1SaveChildPut**
> Boolean bundleProductLinkManagementV1SaveChildPut(sku, id, bundleProductLinkManagementV1SaveChildPutRequest)

bundle-products/{sku}/links/{id}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsSkuLinksIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsSkuLinksIdApi apiInstance = new BundleProductsSkuLinksIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    String id = "id_example"; // String | 
    BundleProductLinkManagementV1SaveChildPutRequest bundleProductLinkManagementV1SaveChildPutRequest = new BundleProductLinkManagementV1SaveChildPutRequest(); // BundleProductLinkManagementV1SaveChildPutRequest | 
    try {
      Boolean result = apiInstance.bundleProductLinkManagementV1SaveChildPut(sku, id, bundleProductLinkManagementV1SaveChildPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsSkuLinksIdApi#bundleProductLinkManagementV1SaveChildPut");
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
| **id** | **String**|  | |
| **bundleProductLinkManagementV1SaveChildPutRequest** | [**BundleProductLinkManagementV1SaveChildPutRequest**](BundleProductLinkManagementV1SaveChildPutRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

