# ProductsAttributesTypesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeTypesListV1GetItemsGet**](ProductsAttributesTypesApi.md#catalogProductAttributeTypesListV1GetItemsGet) | **GET** /V1/products/attributes/types | products/attributes/types |


<a id="catalogProductAttributeTypesListV1GetItemsGet"></a>
# **catalogProductAttributeTypesListV1GetItemsGet**
> List&lt;CatalogDataProductAttributeTypeInterface&gt; catalogProductAttributeTypesListV1GetItemsGet()

products/attributes/types

Retrieve list of product attribute types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributesTypesApi apiInstance = new ProductsAttributesTypesApi(defaultClient);
    try {
      List<CatalogDataProductAttributeTypeInterface> result = apiInstance.catalogProductAttributeTypesListV1GetItemsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributesTypesApi#catalogProductAttributeTypesListV1GetItemsGet");
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

[**List&lt;CatalogDataProductAttributeTypeInterface&gt;**](CatalogDataProductAttributeTypeInterface.md)

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

