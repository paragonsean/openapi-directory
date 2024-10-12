# ProductsOptionsTypesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductCustomOptionTypeListV1GetItemsGet**](ProductsOptionsTypesApi.md#catalogProductCustomOptionTypeListV1GetItemsGet) | **GET** /V1/products/options/types | products/options/types |


<a id="catalogProductCustomOptionTypeListV1GetItemsGet"></a>
# **catalogProductCustomOptionTypeListV1GetItemsGet**
> List&lt;CatalogDataProductCustomOptionTypeInterface&gt; catalogProductCustomOptionTypeListV1GetItemsGet()

products/options/types

Get custom option types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsOptionsTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsOptionsTypesApi apiInstance = new ProductsOptionsTypesApi(defaultClient);
    try {
      List<CatalogDataProductCustomOptionTypeInterface> result = apiInstance.catalogProductCustomOptionTypeListV1GetItemsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsOptionsTypesApi#catalogProductCustomOptionTypeListV1GetItemsGet");
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

[**List&lt;CatalogDataProductCustomOptionTypeInterface&gt;**](CatalogDataProductCustomOptionTypeInterface.md)

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

