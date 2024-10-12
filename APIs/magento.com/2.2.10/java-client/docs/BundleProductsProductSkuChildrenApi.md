# BundleProductsProductSkuChildrenApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductLinkManagementV1GetChildrenGet**](BundleProductsProductSkuChildrenApi.md#bundleProductLinkManagementV1GetChildrenGet) | **GET** /V1/bundle-products/{productSku}/children | bundle-products/{productSku}/children |


<a id="bundleProductLinkManagementV1GetChildrenGet"></a>
# **bundleProductLinkManagementV1GetChildrenGet**
> List&lt;BundleDataLinkInterface&gt; bundleProductLinkManagementV1GetChildrenGet(productSku, optionId)

bundle-products/{productSku}/children

Get all children for Bundle product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsProductSkuChildrenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsProductSkuChildrenApi apiInstance = new BundleProductsProductSkuChildrenApi(defaultClient);
    String productSku = "productSku_example"; // String | 
    Integer optionId = 56; // Integer | 
    try {
      List<BundleDataLinkInterface> result = apiInstance.bundleProductLinkManagementV1GetChildrenGet(productSku, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsProductSkuChildrenApi#bundleProductLinkManagementV1GetChildrenGet");
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
| **productSku** | **String**|  | |
| **optionId** | **Integer**|  | [optional] |

### Return type

[**List&lt;BundleDataLinkInterface&gt;**](BundleDataLinkInterface.md)

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

