# SharedCatalogIdUnassignProductsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogProductManagementV1UnassignProductsPost**](SharedCatalogIdUnassignProductsApi.md#sharedCatalogProductManagementV1UnassignProductsPost) | **POST** /V1/sharedCatalog/{id}/unassignProducts | sharedCatalog/{id}/unassignProducts |


<a id="sharedCatalogProductManagementV1UnassignProductsPost"></a>
# **sharedCatalogProductManagementV1UnassignProductsPost**
> Boolean sharedCatalogProductManagementV1UnassignProductsPost(id, sharedCatalogProductManagementV1AssignProductsPostRequest)

sharedCatalog/{id}/unassignProducts

Remove the specified products from the shared catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogIdUnassignProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogIdUnassignProductsApi apiInstance = new SharedCatalogIdUnassignProductsApi(defaultClient);
    Integer id = 56; // Integer | 
    SharedCatalogProductManagementV1AssignProductsPostRequest sharedCatalogProductManagementV1AssignProductsPostRequest = new SharedCatalogProductManagementV1AssignProductsPostRequest(); // SharedCatalogProductManagementV1AssignProductsPostRequest | 
    try {
      Boolean result = apiInstance.sharedCatalogProductManagementV1UnassignProductsPost(id, sharedCatalogProductManagementV1AssignProductsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogIdUnassignProductsApi#sharedCatalogProductManagementV1UnassignProductsPost");
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

