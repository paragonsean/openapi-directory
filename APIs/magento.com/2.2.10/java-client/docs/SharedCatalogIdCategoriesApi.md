# SharedCatalogIdCategoriesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogCategoryManagementV1GetCategoriesGet**](SharedCatalogIdCategoriesApi.md#sharedCatalogCategoryManagementV1GetCategoriesGet) | **GET** /V1/sharedCatalog/{id}/categories | sharedCatalog/{id}/categories |


<a id="sharedCatalogCategoryManagementV1GetCategoriesGet"></a>
# **sharedCatalogCategoryManagementV1GetCategoriesGet**
> List&lt;Integer&gt; sharedCatalogCategoryManagementV1GetCategoriesGet(id)

sharedCatalog/{id}/categories

Return the list of categories in the selected shared catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogIdCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogIdCategoriesApi apiInstance = new SharedCatalogIdCategoriesApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      List<Integer> result = apiInstance.sharedCatalogCategoryManagementV1GetCategoriesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogIdCategoriesApi#sharedCatalogCategoryManagementV1GetCategoriesGet");
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

### Return type

**List&lt;Integer&gt;**

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

