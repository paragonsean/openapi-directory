# CategoriesCategoryIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCategoryRepositoryV1DeleteByIdentifierDelete**](CategoriesCategoryIdApi.md#catalogCategoryRepositoryV1DeleteByIdentifierDelete) | **DELETE** /V1/categories/{categoryId} | categories/{categoryId} |
| [**catalogCategoryRepositoryV1GetGet**](CategoriesCategoryIdApi.md#catalogCategoryRepositoryV1GetGet) | **GET** /V1/categories/{categoryId} | categories/{categoryId} |


<a id="catalogCategoryRepositoryV1DeleteByIdentifierDelete"></a>
# **catalogCategoryRepositoryV1DeleteByIdentifierDelete**
> Boolean catalogCategoryRepositoryV1DeleteByIdentifierDelete(categoryId)

categories/{categoryId}

Delete category by identifier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesCategoryIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesCategoryIdApi apiInstance = new CategoriesCategoryIdApi(defaultClient);
    Integer categoryId = 56; // Integer | 
    try {
      Boolean result = apiInstance.catalogCategoryRepositoryV1DeleteByIdentifierDelete(categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesCategoryIdApi#catalogCategoryRepositoryV1DeleteByIdentifierDelete");
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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="catalogCategoryRepositoryV1GetGet"></a>
# **catalogCategoryRepositoryV1GetGet**
> CatalogDataCategoryInterface catalogCategoryRepositoryV1GetGet(categoryId, storeId)

categories/{categoryId}

Get info about category by category id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesCategoryIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesCategoryIdApi apiInstance = new CategoriesCategoryIdApi(defaultClient);
    Integer categoryId = 56; // Integer | 
    Integer storeId = 56; // Integer | 
    try {
      CatalogDataCategoryInterface result = apiInstance.catalogCategoryRepositoryV1GetGet(categoryId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesCategoryIdApi#catalogCategoryRepositoryV1GetGet");
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
| **storeId** | **Integer**|  | [optional] |

### Return type

[**CatalogDataCategoryInterface**](CatalogDataCategoryInterface.md)

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

