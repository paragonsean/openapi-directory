# ProductsLinksTypesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductLinkTypeListV1GetItemsGet**](ProductsLinksTypesApi.md#catalogProductLinkTypeListV1GetItemsGet) | **GET** /V1/products/links/types | products/links/types |


<a id="catalogProductLinkTypeListV1GetItemsGet"></a>
# **catalogProductLinkTypeListV1GetItemsGet**
> List&lt;CatalogDataProductLinkTypeInterface&gt; catalogProductLinkTypeListV1GetItemsGet()

products/links/types

Retrieve information about available product link types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsLinksTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsLinksTypesApi apiInstance = new ProductsLinksTypesApi(defaultClient);
    try {
      List<CatalogDataProductLinkTypeInterface> result = apiInstance.catalogProductLinkTypeListV1GetItemsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsLinksTypesApi#catalogProductLinkTypeListV1GetItemsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;CatalogDataProductLinkTypeInterface&gt;**](CatalogDataProductLinkTypeInterface.md)

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

