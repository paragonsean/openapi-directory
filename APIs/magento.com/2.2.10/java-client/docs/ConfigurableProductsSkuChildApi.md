# ConfigurableProductsSkuChildApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurableProductLinkManagementV1AddChildPost**](ConfigurableProductsSkuChildApi.md#configurableProductLinkManagementV1AddChildPost) | **POST** /V1/configurable-products/{sku}/child | configurable-products/{sku}/child |


<a id="configurableProductLinkManagementV1AddChildPost"></a>
# **configurableProductLinkManagementV1AddChildPost**
> Boolean configurableProductLinkManagementV1AddChildPost(sku, configurableProductLinkManagementV1AddChildPostRequest)

configurable-products/{sku}/child



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsSkuChildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsSkuChildApi apiInstance = new ConfigurableProductsSkuChildApi(defaultClient);
    String sku = "sku_example"; // String | 
    ConfigurableProductLinkManagementV1AddChildPostRequest configurableProductLinkManagementV1AddChildPostRequest = new ConfigurableProductLinkManagementV1AddChildPostRequest(); // ConfigurableProductLinkManagementV1AddChildPostRequest | 
    try {
      Boolean result = apiInstance.configurableProductLinkManagementV1AddChildPost(sku, configurableProductLinkManagementV1AddChildPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsSkuChildApi#configurableProductLinkManagementV1AddChildPost");
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
| **configurableProductLinkManagementV1AddChildPostRequest** | [**ConfigurableProductLinkManagementV1AddChildPostRequest**](ConfigurableProductLinkManagementV1AddChildPostRequest.md)|  | [optional] |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

