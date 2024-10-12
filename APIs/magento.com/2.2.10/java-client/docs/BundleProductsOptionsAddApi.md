# BundleProductsOptionsAddApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductOptionManagementV1SavePost**](BundleProductsOptionsAddApi.md#bundleProductOptionManagementV1SavePost) | **POST** /V1/bundle-products/options/add | bundle-products/options/add |


<a id="bundleProductOptionManagementV1SavePost"></a>
# **bundleProductOptionManagementV1SavePost**
> Integer bundleProductOptionManagementV1SavePost(bundleProductOptionManagementV1SavePostRequest)

bundle-products/options/add

Add new option for bundle product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsOptionsAddApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsOptionsAddApi apiInstance = new BundleProductsOptionsAddApi(defaultClient);
    BundleProductOptionManagementV1SavePostRequest bundleProductOptionManagementV1SavePostRequest = new BundleProductOptionManagementV1SavePostRequest(); // BundleProductOptionManagementV1SavePostRequest | 
    try {
      Integer result = apiInstance.bundleProductOptionManagementV1SavePost(bundleProductOptionManagementV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsOptionsAddApi#bundleProductOptionManagementV1SavePost");
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
| **bundleProductOptionManagementV1SavePostRequest** | [**BundleProductOptionManagementV1SavePostRequest**](BundleProductOptionManagementV1SavePostRequest.md)|  | [optional] |

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

