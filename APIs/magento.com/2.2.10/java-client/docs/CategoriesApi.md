# CategoriesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCategoryManagementV1GetTreeGet**](CategoriesApi.md#catalogCategoryManagementV1GetTreeGet) | **GET** /V1/categories | categories |
| [**catalogCategoryRepositoryV1SavePost**](CategoriesApi.md#catalogCategoryRepositoryV1SavePost) | **POST** /V1/categories | categories |


<a id="catalogCategoryManagementV1GetTreeGet"></a>
# **catalogCategoryManagementV1GetTreeGet**
> CatalogDataCategoryTreeInterface catalogCategoryManagementV1GetTreeGet(rootCategoryId, depth)

categories

Retrieve list of categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    Integer rootCategoryId = 56; // Integer | 
    Integer depth = 56; // Integer | 
    try {
      CatalogDataCategoryTreeInterface result = apiInstance.catalogCategoryManagementV1GetTreeGet(rootCategoryId, depth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#catalogCategoryManagementV1GetTreeGet");
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
| **rootCategoryId** | **Integer**|  | [optional] |
| **depth** | **Integer**|  | [optional] |

### Return type

[**CatalogDataCategoryTreeInterface**](CatalogDataCategoryTreeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="catalogCategoryRepositoryV1SavePost"></a>
# **catalogCategoryRepositoryV1SavePost**
> CatalogDataCategoryInterface catalogCategoryRepositoryV1SavePost(catalogCategoryRepositoryV1SavePostRequest)

categories

Create category service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    CatalogCategoryRepositoryV1SavePostRequest catalogCategoryRepositoryV1SavePostRequest = new CatalogCategoryRepositoryV1SavePostRequest(); // CatalogCategoryRepositoryV1SavePostRequest | 
    try {
      CatalogDataCategoryInterface result = apiInstance.catalogCategoryRepositoryV1SavePost(catalogCategoryRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#catalogCategoryRepositoryV1SavePost");
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

