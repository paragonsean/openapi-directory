# ProductsAttributeSetsAttributeSetIdGroupsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeGroupRepositoryV1SavePut**](ProductsAttributeSetsAttributeSetIdGroupsApi.md#catalogProductAttributeGroupRepositoryV1SavePut) | **PUT** /V1/products/attribute-sets/{attributeSetId}/groups | products/attribute-sets/{attributeSetId}/groups |


<a id="catalogProductAttributeGroupRepositoryV1SavePut"></a>
# **catalogProductAttributeGroupRepositoryV1SavePut**
> EavDataAttributeGroupInterface catalogProductAttributeGroupRepositoryV1SavePut(attributeSetId, catalogProductAttributeGroupRepositoryV1SavePostRequest)

products/attribute-sets/{attributeSetId}/groups

Save attribute group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsAttributeSetIdGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsAttributeSetIdGroupsApi apiInstance = new ProductsAttributeSetsAttributeSetIdGroupsApi(defaultClient);
    String attributeSetId = "attributeSetId_example"; // String | 
    CatalogProductAttributeGroupRepositoryV1SavePostRequest catalogProductAttributeGroupRepositoryV1SavePostRequest = new CatalogProductAttributeGroupRepositoryV1SavePostRequest(); // CatalogProductAttributeGroupRepositoryV1SavePostRequest | 
    try {
      EavDataAttributeGroupInterface result = apiInstance.catalogProductAttributeGroupRepositoryV1SavePut(attributeSetId, catalogProductAttributeGroupRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsAttributeSetIdGroupsApi#catalogProductAttributeGroupRepositoryV1SavePut");
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
| **catalogProductAttributeGroupRepositoryV1SavePostRequest** | [**CatalogProductAttributeGroupRepositoryV1SavePostRequest**](CatalogProductAttributeGroupRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**EavDataAttributeGroupInterface**](EavDataAttributeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

