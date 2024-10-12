# CategoriesIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCategoryRepositoryV1SavePut**](CategoriesIdApi.md#catalogCategoryRepositoryV1SavePut) | **PUT** /V1/categories/{id} | categories/{id} |


<a id="catalogCategoryRepositoryV1SavePut"></a>
# **catalogCategoryRepositoryV1SavePut**
> CatalogDataCategoryInterface catalogCategoryRepositoryV1SavePut(id, catalogCategoryRepositoryV1SavePostRequest)

categories/{id}

Create category service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesIdApi apiInstance = new CategoriesIdApi(defaultClient);
    String id = "id_example"; // String | 
    CatalogCategoryRepositoryV1SavePostRequest catalogCategoryRepositoryV1SavePostRequest = new CatalogCategoryRepositoryV1SavePostRequest(); // CatalogCategoryRepositoryV1SavePostRequest | 
    try {
      CatalogDataCategoryInterface result = apiInstance.catalogCategoryRepositoryV1SavePut(id, catalogCategoryRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesIdApi#catalogCategoryRepositoryV1SavePut");
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
| **id** | **String**|  | |
| **catalogCategoryRepositoryV1SavePostRequest** | [**CatalogCategoryRepositoryV1SavePostRequest**](CatalogCategoryRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CatalogDataCategoryInterface**](CatalogDataCategoryInterface.md)

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

