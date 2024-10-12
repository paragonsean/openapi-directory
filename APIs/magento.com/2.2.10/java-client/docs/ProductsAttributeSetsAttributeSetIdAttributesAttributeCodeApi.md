# ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeManagementV1UnassignDelete**](ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi.md#catalogProductAttributeManagementV1UnassignDelete) | **DELETE** /V1/products/attribute-sets/{attributeSetId}/attributes/{attributeCode} | products/attribute-sets/{attributeSetId}/attributes/{attributeCode} |


<a id="catalogProductAttributeManagementV1UnassignDelete"></a>
# **catalogProductAttributeManagementV1UnassignDelete**
> Boolean catalogProductAttributeManagementV1UnassignDelete(attributeSetId, attributeCode)

products/attribute-sets/{attributeSetId}/attributes/{attributeCode}

Remove attribute from attribute set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi apiInstance = new ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi(defaultClient);
    String attributeSetId = "attributeSetId_example"; // String | 
    String attributeCode = "attributeCode_example"; // String | 
    try {
      Boolean result = apiInstance.catalogProductAttributeManagementV1UnassignDelete(attributeSetId, attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi#catalogProductAttributeManagementV1UnassignDelete");
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
| **attributeCode** | **String**|  | |

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

