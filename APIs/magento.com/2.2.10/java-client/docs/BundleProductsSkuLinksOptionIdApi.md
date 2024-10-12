# BundleProductsSkuLinksOptionIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductLinkManagementV1AddChildByProductSkuPost**](BundleProductsSkuLinksOptionIdApi.md#bundleProductLinkManagementV1AddChildByProductSkuPost) | **POST** /V1/bundle-products/{sku}/links/{optionId} | bundle-products/{sku}/links/{optionId} |


<a id="bundleProductLinkManagementV1AddChildByProductSkuPost"></a>
# **bundleProductLinkManagementV1AddChildByProductSkuPost**
> Integer bundleProductLinkManagementV1AddChildByProductSkuPost(sku, optionId, bundleProductLinkManagementV1SaveChildPutRequest)

bundle-products/{sku}/links/{optionId}

Add child product to specified Bundle option by product sku

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsSkuLinksOptionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsSkuLinksOptionIdApi apiInstance = new BundleProductsSkuLinksOptionIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer optionId = 56; // Integer | 
    BundleProductLinkManagementV1SaveChildPutRequest bundleProductLinkManagementV1SaveChildPutRequest = new BundleProductLinkManagementV1SaveChildPutRequest(); // BundleProductLinkManagementV1SaveChildPutRequest | 
    try {
      Integer result = apiInstance.bundleProductLinkManagementV1AddChildByProductSkuPost(sku, optionId, bundleProductLinkManagementV1SaveChildPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsSkuLinksOptionIdApi#bundleProductLinkManagementV1AddChildByProductSkuPost");
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
| **bundleProductLinkManagementV1SaveChildPutRequest** | [**BundleProductLinkManagementV1SaveChildPutRequest**](BundleProductLinkManagementV1SaveChildPutRequest.md)|  | [optional] |

### Return type

**Integer**

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

