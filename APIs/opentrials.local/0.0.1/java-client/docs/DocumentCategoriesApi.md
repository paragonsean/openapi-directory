# DocumentCategoriesApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listDocumentCategories**](DocumentCategoriesApi.md#listDocumentCategories) | **GET** /document_categories |  |


<a id="listDocumentCategories"></a>
# **listDocumentCategories**
> DocumentCategoryList listDocumentCategories()



Returns document categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    DocumentCategoriesApi apiInstance = new DocumentCategoriesApi(defaultClient);
    try {
      DocumentCategoryList result = apiInstance.listDocumentCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentCategoriesApi#listDocumentCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DocumentCategoryList**](DocumentCategoryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

