# SharedCatalogIdAssignCategoriesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogCategoryManagementV1AssignCategoriesPost**](SharedCatalogIdAssignCategoriesApi.md#sharedCatalogCategoryManagementV1AssignCategoriesPost) | **POST** /V1/sharedCatalog/{id}/assignCategories | sharedCatalog/{id}/assignCategories |


<a id="sharedCatalogCategoryManagementV1AssignCategoriesPost"></a>
# **sharedCatalogCategoryManagementV1AssignCategoriesPost**
> Boolean sharedCatalogCategoryManagementV1AssignCategoriesPost(id, sharedCatalogCategoryManagementV1AssignCategoriesPostRequest)

sharedCatalog/{id}/assignCategories

Add categories into the shared catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogIdAssignCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogIdAssignCategoriesApi apiInstance = new SharedCatalogIdAssignCategoriesApi(defaultClient);
    Integer id = 56; // Integer | 
    SharedCatalogCategoryManagementV1AssignCategoriesPostRequest sharedCatalogCategoryManagementV1AssignCategoriesPostRequest = new SharedCatalogCategoryManagementV1AssignCategoriesPostRequest(); // SharedCatalogCategoryManagementV1AssignCategoriesPostRequest | 
    try {
      Boolean result = apiInstance.sharedCatalogCategoryManagementV1AssignCategoriesPost(id, sharedCatalogCategoryManagementV1AssignCategoriesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogIdAssignCategoriesApi#sharedCatalogCategoryManagementV1AssignCategoriesPost");
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
| **sharedCatalogCategoryManagementV1AssignCategoriesPostRequest** | [**SharedCatalogCategoryManagementV1AssignCategoriesPostRequest**](SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.md)|  | [optional] |

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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

