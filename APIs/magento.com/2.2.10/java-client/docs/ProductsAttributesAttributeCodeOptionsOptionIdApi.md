# ProductsAttributesAttributeCodeOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeOptionManagementV1DeleteDelete**](ProductsAttributesAttributeCodeOptionsOptionIdApi.md#catalogProductAttributeOptionManagementV1DeleteDelete) | **DELETE** /V1/products/attributes/{attributeCode}/options/{optionId} | products/attributes/{attributeCode}/options/{optionId} |


<a id="catalogProductAttributeOptionManagementV1DeleteDelete"></a>
# **catalogProductAttributeOptionManagementV1DeleteDelete**
> Boolean catalogProductAttributeOptionManagementV1DeleteDelete(attributeCode, optionId)

products/attributes/{attributeCode}/options/{optionId}

Delete option from attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributesAttributeCodeOptionsOptionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributesAttributeCodeOptionsOptionIdApi apiInstance = new ProductsAttributesAttributeCodeOptionsOptionIdApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    String optionId = "optionId_example"; // String | 
    try {
      Boolean result = apiInstance.catalogProductAttributeOptionManagementV1DeleteDelete(attributeCode, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributesAttributeCodeOptionsOptionIdApi#catalogProductAttributeOptionManagementV1DeleteDelete");
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
| **attributeCode** | **String**|  | |
| **optionId** | **String**|  | |

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

