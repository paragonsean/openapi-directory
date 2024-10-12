# CategoriesCategoryIdMoveApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCategoryManagementV1MovePut**](CategoriesCategoryIdMoveApi.md#catalogCategoryManagementV1MovePut) | **PUT** /V1/categories/{categoryId}/move | categories/{categoryId}/move |


<a id="catalogCategoryManagementV1MovePut"></a>
# **catalogCategoryManagementV1MovePut**
> Boolean catalogCategoryManagementV1MovePut(categoryId, catalogCategoryManagementV1MovePutRequest)

categories/{categoryId}/move

Move category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesCategoryIdMoveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesCategoryIdMoveApi apiInstance = new CategoriesCategoryIdMoveApi(defaultClient);
    Integer categoryId = 56; // Integer | 
    CatalogCategoryManagementV1MovePutRequest catalogCategoryManagementV1MovePutRequest = new CatalogCategoryManagementV1MovePutRequest(); // CatalogCategoryManagementV1MovePutRequest | 
    try {
      Boolean result = apiInstance.catalogCategoryManagementV1MovePut(categoryId, catalogCategoryManagementV1MovePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesCategoryIdMoveApi#catalogCategoryManagementV1MovePut");
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
| **categoryId** | **Integer**|  | |
| **catalogCategoryManagementV1MovePutRequest** | [**CatalogCategoryManagementV1MovePutRequest**](CatalogCategoryManagementV1MovePutRequest.md)|  | [optional] |

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

