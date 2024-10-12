# BundleProductsOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductOptionManagementV1SavePut**](BundleProductsOptionsOptionIdApi.md#bundleProductOptionManagementV1SavePut) | **PUT** /V1/bundle-products/options/{optionId} | bundle-products/options/{optionId} |


<a id="bundleProductOptionManagementV1SavePut"></a>
# **bundleProductOptionManagementV1SavePut**
> Integer bundleProductOptionManagementV1SavePut(optionId, bundleProductOptionManagementV1SavePostRequest)

bundle-products/options/{optionId}

Add new option for bundle product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsOptionsOptionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsOptionsOptionIdApi apiInstance = new BundleProductsOptionsOptionIdApi(defaultClient);
    String optionId = "optionId_example"; // String | 
    BundleProductOptionManagementV1SavePostRequest bundleProductOptionManagementV1SavePostRequest = new BundleProductOptionManagementV1SavePostRequest(); // BundleProductOptionManagementV1SavePostRequest | 
    try {
      Integer result = apiInstance.bundleProductOptionManagementV1SavePut(optionId, bundleProductOptionManagementV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsOptionsOptionIdApi#bundleProductOptionManagementV1SavePut");
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
| **optionId** | **String**|  | |
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

