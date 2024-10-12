# ProductsSkuLinksTypeLinkedProductSkuApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductLinkRepositoryV1DeleteByIdDelete**](ProductsSkuLinksTypeLinkedProductSkuApi.md#catalogProductLinkRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/{sku}/links/{type}/{linkedProductSku} | products/{sku}/links/{type}/{linkedProductSku} |


<a id="catalogProductLinkRepositoryV1DeleteByIdDelete"></a>
# **catalogProductLinkRepositoryV1DeleteByIdDelete**
> Boolean catalogProductLinkRepositoryV1DeleteByIdDelete(sku, type, linkedProductSku)

products/{sku}/links/{type}/{linkedProductSku}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuLinksTypeLinkedProductSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuLinksTypeLinkedProductSkuApi apiInstance = new ProductsSkuLinksTypeLinkedProductSkuApi(defaultClient);
    String sku = "sku_example"; // String | 
    String type = "type_example"; // String | 
    String linkedProductSku = "linkedProductSku_example"; // String | 
    try {
      Boolean result = apiInstance.catalogProductLinkRepositoryV1DeleteByIdDelete(sku, type, linkedProductSku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuLinksTypeLinkedProductSkuApi#catalogProductLinkRepositoryV1DeleteByIdDelete");
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
| **type** | **String**|  | |
| **linkedProductSku** | **String**|  | |

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

