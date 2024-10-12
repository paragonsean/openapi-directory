# ProductsMediaTypesAttributeSetNameApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductMediaAttributeManagementV1GetListGet**](ProductsMediaTypesAttributeSetNameApi.md#catalogProductMediaAttributeManagementV1GetListGet) | **GET** /V1/products/media/types/{attributeSetName} | products/media/types/{attributeSetName} |


<a id="catalogProductMediaAttributeManagementV1GetListGet"></a>
# **catalogProductMediaAttributeManagementV1GetListGet**
> List&lt;CatalogDataProductAttributeInterface&gt; catalogProductMediaAttributeManagementV1GetListGet(attributeSetName)

products/media/types/{attributeSetName}

Retrieve the list of media attributes (fronted input type is media_image) assigned to the given attribute set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsMediaTypesAttributeSetNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsMediaTypesAttributeSetNameApi apiInstance = new ProductsMediaTypesAttributeSetNameApi(defaultClient);
    String attributeSetName = "attributeSetName_example"; // String | 
    try {
      List<CatalogDataProductAttributeInterface> result = apiInstance.catalogProductMediaAttributeManagementV1GetListGet(attributeSetName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsMediaTypesAttributeSetNameApi#catalogProductMediaAttributeManagementV1GetListGet");
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
| **attributeSetName** | **String**|  | |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

