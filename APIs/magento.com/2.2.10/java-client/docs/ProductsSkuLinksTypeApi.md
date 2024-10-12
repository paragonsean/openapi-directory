# ProductsSkuLinksTypeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductLinkManagementV1GetLinkedItemsByTypeGet**](ProductsSkuLinksTypeApi.md#catalogProductLinkManagementV1GetLinkedItemsByTypeGet) | **GET** /V1/products/{sku}/links/{type} | products/{sku}/links/{type} |


<a id="catalogProductLinkManagementV1GetLinkedItemsByTypeGet"></a>
# **catalogProductLinkManagementV1GetLinkedItemsByTypeGet**
> List&lt;CatalogDataProductLinkInterface&gt; catalogProductLinkManagementV1GetLinkedItemsByTypeGet(sku, type)

products/{sku}/links/{type}

Provide the list of links for a specific product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuLinksTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuLinksTypeApi apiInstance = new ProductsSkuLinksTypeApi(defaultClient);
    String sku = "sku_example"; // String | 
    String type = "type_example"; // String | 
    try {
      List<CatalogDataProductLinkInterface> result = apiInstance.catalogProductLinkManagementV1GetLinkedItemsByTypeGet(sku, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuLinksTypeApi#catalogProductLinkManagementV1GetLinkedItemsByTypeGet");
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

### Return type

[**List&lt;CatalogDataProductLinkInterface&gt;**](CatalogDataProductLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

