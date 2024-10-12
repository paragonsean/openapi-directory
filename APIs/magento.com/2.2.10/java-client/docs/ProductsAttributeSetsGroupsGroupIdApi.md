# ProductsAttributeSetsGroupsGroupIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeGroupRepositoryV1DeleteByIdDelete**](ProductsAttributeSetsGroupsGroupIdApi.md#catalogProductAttributeGroupRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/attribute-sets/groups/{groupId} | products/attribute-sets/groups/{groupId} |


<a id="catalogProductAttributeGroupRepositoryV1DeleteByIdDelete"></a>
# **catalogProductAttributeGroupRepositoryV1DeleteByIdDelete**
> Boolean catalogProductAttributeGroupRepositoryV1DeleteByIdDelete(groupId)

products/attribute-sets/groups/{groupId}

Remove attribute group by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsGroupsGroupIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsGroupsGroupIdApi apiInstance = new ProductsAttributeSetsGroupsGroupIdApi(defaultClient);
    Integer groupId = 56; // Integer | 
    try {
      Boolean result = apiInstance.catalogProductAttributeGroupRepositoryV1DeleteByIdDelete(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsGroupsGroupIdApi#catalogProductAttributeGroupRepositoryV1DeleteByIdDelete");
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
| **groupId** | **Integer**|  | |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

