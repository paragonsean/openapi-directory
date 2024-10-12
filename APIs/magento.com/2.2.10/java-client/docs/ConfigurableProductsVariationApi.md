# ConfigurableProductsVariationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurableProductConfigurableProductManagementV1GenerateVariationPut**](ConfigurableProductsVariationApi.md#configurableProductConfigurableProductManagementV1GenerateVariationPut) | **PUT** /V1/configurable-products/variation | configurable-products/variation |


<a id="configurableProductConfigurableProductManagementV1GenerateVariationPut"></a>
# **configurableProductConfigurableProductManagementV1GenerateVariationPut**
> List&lt;CatalogDataProductInterface&gt; configurableProductConfigurableProductManagementV1GenerateVariationPut(configurableProductConfigurableProductManagementV1GenerateVariationPutRequest)

configurable-products/variation

Generate variation based on same product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsVariationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsVariationApi apiInstance = new ConfigurableProductsVariationApi(defaultClient);
    ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest configurableProductConfigurableProductManagementV1GenerateVariationPutRequest = new ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest(); // ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest | 
    try {
      List<CatalogDataProductInterface> result = apiInstance.configurableProductConfigurableProductManagementV1GenerateVariationPut(configurableProductConfigurableProductManagementV1GenerateVariationPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsVariationApi#configurableProductConfigurableProductManagementV1GenerateVariationPut");
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
| **configurableProductConfigurableProductManagementV1GenerateVariationPutRequest** | [**ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest**](ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest.md)|  | [optional] |

### Return type

[**List&lt;CatalogDataProductInterface&gt;**](CatalogDataProductInterface.md)

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

