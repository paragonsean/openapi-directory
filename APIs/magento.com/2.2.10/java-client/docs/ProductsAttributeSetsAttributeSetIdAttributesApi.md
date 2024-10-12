# ProductsAttributeSetsAttributeSetIdAttributesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeManagementV1GetAttributesGet**](ProductsAttributeSetsAttributeSetIdAttributesApi.md#catalogProductAttributeManagementV1GetAttributesGet) | **GET** /V1/products/attribute-sets/{attributeSetId}/attributes | products/attribute-sets/{attributeSetId}/attributes |


<a id="catalogProductAttributeManagementV1GetAttributesGet"></a>
# **catalogProductAttributeManagementV1GetAttributesGet**
> List&lt;CatalogDataProductAttributeInterface&gt; catalogProductAttributeManagementV1GetAttributesGet(attributeSetId)

products/attribute-sets/{attributeSetId}/attributes

Retrieve related attributes based on given attribute set ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsAttributeSetIdAttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsAttributeSetIdAttributesApi apiInstance = new ProductsAttributeSetsAttributeSetIdAttributesApi(defaultClient);
    String attributeSetId = "attributeSetId_example"; // String | 
    try {
      List<CatalogDataProductAttributeInterface> result = apiInstance.catalogProductAttributeManagementV1GetAttributesGet(attributeSetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsAttributeSetIdAttributesApi#catalogProductAttributeManagementV1GetAttributesGet");
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
| **attributeSetId** | **String**|  | |

### Return type

[**List&lt;CatalogDataProductAttributeInterface&gt;**](CatalogDataProductAttributeInterface.md)

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

