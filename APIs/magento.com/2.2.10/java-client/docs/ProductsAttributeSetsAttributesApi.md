# ProductsAttributeSetsAttributesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeManagementV1AssignPost**](ProductsAttributeSetsAttributesApi.md#catalogProductAttributeManagementV1AssignPost) | **POST** /V1/products/attribute-sets/attributes | products/attribute-sets/attributes |


<a id="catalogProductAttributeManagementV1AssignPost"></a>
# **catalogProductAttributeManagementV1AssignPost**
> Integer catalogProductAttributeManagementV1AssignPost(catalogProductAttributeManagementV1AssignPostRequest)

products/attribute-sets/attributes

Assign attribute to attribute set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsAttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsAttributesApi apiInstance = new ProductsAttributeSetsAttributesApi(defaultClient);
    CatalogProductAttributeManagementV1AssignPostRequest catalogProductAttributeManagementV1AssignPostRequest = new CatalogProductAttributeManagementV1AssignPostRequest(); // CatalogProductAttributeManagementV1AssignPostRequest | 
    try {
      Integer result = apiInstance.catalogProductAttributeManagementV1AssignPost(catalogProductAttributeManagementV1AssignPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsAttributesApi#catalogProductAttributeManagementV1AssignPost");
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
| **catalogProductAttributeManagementV1AssignPostRequest** | [**CatalogProductAttributeManagementV1AssignPostRequest**](CatalogProductAttributeManagementV1AssignPostRequest.md)|  | [optional] |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

