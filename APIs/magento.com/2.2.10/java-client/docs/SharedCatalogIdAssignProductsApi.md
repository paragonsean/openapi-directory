# SharedCatalogIdAssignProductsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogProductManagementV1AssignProductsPost**](SharedCatalogIdAssignProductsApi.md#sharedCatalogProductManagementV1AssignProductsPost) | **POST** /V1/sharedCatalog/{id}/assignProducts | sharedCatalog/{id}/assignProducts |


<a id="sharedCatalogProductManagementV1AssignProductsPost"></a>
# **sharedCatalogProductManagementV1AssignProductsPost**
> Boolean sharedCatalogProductManagementV1AssignProductsPost(id, sharedCatalogProductManagementV1AssignProductsPostRequest)

sharedCatalog/{id}/assignProducts

Add products into the shared catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogIdAssignProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogIdAssignProductsApi apiInstance = new SharedCatalogIdAssignProductsApi(defaultClient);
    Integer id = 56; // Integer | 
    SharedCatalogProductManagementV1AssignProductsPostRequest sharedCatalogProductManagementV1AssignProductsPostRequest = new SharedCatalogProductManagementV1AssignProductsPostRequest(); // SharedCatalogProductManagementV1AssignProductsPostRequest | 
    try {
      Boolean result = apiInstance.sharedCatalogProductManagementV1AssignProductsPost(id, sharedCatalogProductManagementV1AssignProductsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogIdAssignProductsApi#sharedCatalogProductManagementV1AssignProductsPost");
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
| **id** | **Integer**|  | |
| **sharedCatalogProductManagementV1AssignProductsPostRequest** | [**SharedCatalogProductManagementV1AssignProductsPostRequest**](SharedCatalogProductManagementV1AssignProductsPostRequest.md)|  | [optional] |

### Return type

**Boolean**

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

