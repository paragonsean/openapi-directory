# ProductsAttributeSetsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogAttributeSetManagementV1CreatePost**](ProductsAttributeSetsApi.md#catalogAttributeSetManagementV1CreatePost) | **POST** /V1/products/attribute-sets | products/attribute-sets |


<a id="catalogAttributeSetManagementV1CreatePost"></a>
# **catalogAttributeSetManagementV1CreatePost**
> EavDataAttributeSetInterface catalogAttributeSetManagementV1CreatePost(catalogAttributeSetManagementV1CreatePostRequest)

products/attribute-sets

Create attribute set from data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsApi apiInstance = new ProductsAttributeSetsApi(defaultClient);
    CatalogAttributeSetManagementV1CreatePostRequest catalogAttributeSetManagementV1CreatePostRequest = new CatalogAttributeSetManagementV1CreatePostRequest(); // CatalogAttributeSetManagementV1CreatePostRequest | 
    try {
      EavDataAttributeSetInterface result = apiInstance.catalogAttributeSetManagementV1CreatePost(catalogAttributeSetManagementV1CreatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsApi#catalogAttributeSetManagementV1CreatePost");
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
| **catalogAttributeSetManagementV1CreatePostRequest** | [**CatalogAttributeSetManagementV1CreatePostRequest**](CatalogAttributeSetManagementV1CreatePostRequest.md)|  | [optional] |

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

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

