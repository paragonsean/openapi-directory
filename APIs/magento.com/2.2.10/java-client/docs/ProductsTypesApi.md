# ProductsTypesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductTypeListV1GetProductTypesGet**](ProductsTypesApi.md#catalogProductTypeListV1GetProductTypesGet) | **GET** /V1/products/types | products/types |


<a id="catalogProductTypeListV1GetProductTypesGet"></a>
# **catalogProductTypeListV1GetProductTypesGet**
> List&lt;CatalogDataProductTypeInterface&gt; catalogProductTypeListV1GetProductTypesGet()

products/types

Retrieve available product types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsTypesApi apiInstance = new ProductsTypesApi(defaultClient);
    try {
      List<CatalogDataProductTypeInterface> result = apiInstance.catalogProductTypeListV1GetProductTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsTypesApi#catalogProductTypeListV1GetProductTypesGet");
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

[**List&lt;CatalogDataProductTypeInterface&gt;**](CatalogDataProductTypeInterface.md)

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

