# ProductsAttributeSetsGroupsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeGroupRepositoryV1SavePost**](ProductsAttributeSetsGroupsApi.md#catalogProductAttributeGroupRepositoryV1SavePost) | **POST** /V1/products/attribute-sets/groups | products/attribute-sets/groups |


<a id="catalogProductAttributeGroupRepositoryV1SavePost"></a>
# **catalogProductAttributeGroupRepositoryV1SavePost**
> EavDataAttributeGroupInterface catalogProductAttributeGroupRepositoryV1SavePost(catalogProductAttributeGroupRepositoryV1SavePostRequest)

products/attribute-sets/groups

Save attribute group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsGroupsApi apiInstance = new ProductsAttributeSetsGroupsApi(defaultClient);
    CatalogProductAttributeGroupRepositoryV1SavePostRequest catalogProductAttributeGroupRepositoryV1SavePostRequest = new CatalogProductAttributeGroupRepositoryV1SavePostRequest(); // CatalogProductAttributeGroupRepositoryV1SavePostRequest | 
    try {
      EavDataAttributeGroupInterface result = apiInstance.catalogProductAttributeGroupRepositoryV1SavePost(catalogProductAttributeGroupRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsGroupsApi#catalogProductAttributeGroupRepositoryV1SavePost");
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

