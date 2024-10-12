# ConfigurableProductsSkuOptionsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurableProductOptionRepositoryV1SavePost**](ConfigurableProductsSkuOptionsApi.md#configurableProductOptionRepositoryV1SavePost) | **POST** /V1/configurable-products/{sku}/options | configurable-products/{sku}/options |


<a id="configurableProductOptionRepositoryV1SavePost"></a>
# **configurableProductOptionRepositoryV1SavePost**
> Integer configurableProductOptionRepositoryV1SavePost(sku, configurableProductOptionRepositoryV1SavePostRequest)

configurable-products/{sku}/options

Save option

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsSkuOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsSkuOptionsApi apiInstance = new ConfigurableProductsSkuOptionsApi(defaultClient);
    String sku = "sku_example"; // String | 
    ConfigurableProductOptionRepositoryV1SavePostRequest configurableProductOptionRepositoryV1SavePostRequest = new ConfigurableProductOptionRepositoryV1SavePostRequest(); // ConfigurableProductOptionRepositoryV1SavePostRequest | 
    try {
      Integer result = apiInstance.configurableProductOptionRepositoryV1SavePost(sku, configurableProductOptionRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsSkuOptionsApi#configurableProductOptionRepositoryV1SavePost");
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
| **configurableProductOptionRepositoryV1SavePostRequest** | [**ConfigurableProductOptionRepositoryV1SavePostRequest**](ConfigurableProductOptionRepositoryV1SavePostRequest.md)|  | [optional] |

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

