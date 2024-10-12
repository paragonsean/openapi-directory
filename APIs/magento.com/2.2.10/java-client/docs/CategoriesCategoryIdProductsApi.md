# CategoriesCategoryIdProductsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCategoryLinkManagementV1GetAssignedProductsGet**](CategoriesCategoryIdProductsApi.md#catalogCategoryLinkManagementV1GetAssignedProductsGet) | **GET** /V1/categories/{categoryId}/products | categories/{categoryId}/products |
| [**catalogCategoryLinkRepositoryV1SavePost**](CategoriesCategoryIdProductsApi.md#catalogCategoryLinkRepositoryV1SavePost) | **POST** /V1/categories/{categoryId}/products | categories/{categoryId}/products |
| [**catalogCategoryLinkRepositoryV1SavePut**](CategoriesCategoryIdProductsApi.md#catalogCategoryLinkRepositoryV1SavePut) | **PUT** /V1/categories/{categoryId}/products | categories/{categoryId}/products |


<a id="catalogCategoryLinkManagementV1GetAssignedProductsGet"></a>
# **catalogCategoryLinkManagementV1GetAssignedProductsGet**
> List&lt;CatalogDataCategoryProductLinkInterface&gt; catalogCategoryLinkManagementV1GetAssignedProductsGet(categoryId)

categories/{categoryId}/products

Get products assigned to category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesCategoryIdProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesCategoryIdProductsApi apiInstance = new CategoriesCategoryIdProductsApi(defaultClient);
    Integer categoryId = 56; // Integer | 
    try {
      List<CatalogDataCategoryProductLinkInterface> result = apiInstance.catalogCategoryLinkManagementV1GetAssignedProductsGet(categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesCategoryIdProductsApi#catalogCategoryLinkManagementV1GetAssignedProductsGet");
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

[**List&lt;CatalogDataCategoryProductLinkInterface&gt;**](CatalogDataCategoryProductLinkInterface.md)

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

<a id="catalogCategoryLinkRepositoryV1SavePost"></a>
# **catalogCategoryLinkRepositoryV1SavePost**
> Boolean catalogCategoryLinkRepositoryV1SavePost(categoryId, catalogCategoryLinkRepositoryV1SavePutRequest)

categories/{categoryId}/products

Assign a product to the required category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesCategoryIdProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesCategoryIdProductsApi apiInstance = new CategoriesCategoryIdProductsApi(defaultClient);
    String categoryId = "categoryId_example"; // String | 
    CatalogCategoryLinkRepositoryV1SavePutRequest catalogCategoryLinkRepositoryV1SavePutRequest = new CatalogCategoryLinkRepositoryV1SavePutRequest(); // CatalogCategoryLinkRepositoryV1SavePutRequest | 
    try {
      Boolean result = apiInstance.catalogCategoryLinkRepositoryV1SavePost(categoryId, catalogCategoryLinkRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesCategoryIdProductsApi#catalogCategoryLinkRepositoryV1SavePost");
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
| **categoryId** | **String**|  | |
| **catalogCategoryLinkRepositoryV1SavePutRequest** | [**CatalogCategoryLinkRepositoryV1SavePutRequest**](CatalogCategoryLinkRepositoryV1SavePutRequest.md)|  | [optional] |

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

<a id="catalogCategoryLinkRepositoryV1SavePut"></a>
# **catalogCategoryLinkRepositoryV1SavePut**
> Boolean catalogCategoryLinkRepositoryV1SavePut(categoryId, catalogCategoryLinkRepositoryV1SavePutRequest)

categories/{categoryId}/products

Assign a product to the required category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesCategoryIdProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesCategoryIdProductsApi apiInstance = new CategoriesCategoryIdProductsApi(defaultClient);
    String categoryId = "categoryId_example"; // String | 
    CatalogCategoryLinkRepositoryV1SavePutRequest catalogCategoryLinkRepositoryV1SavePutRequest = new CatalogCategoryLinkRepositoryV1SavePutRequest(); // CatalogCategoryLinkRepositoryV1SavePutRequest | 
    try {
      Boolean result = apiInstance.catalogCategoryLinkRepositoryV1SavePut(categoryId, catalogCategoryLinkRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesCategoryIdProductsApi#catalogCategoryLinkRepositoryV1SavePut");
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
| **categoryId** | **String**|  | |
| **catalogCategoryLinkRepositoryV1SavePutRequest** | [**CatalogCategoryLinkRepositoryV1SavePutRequest**](CatalogCategoryLinkRepositoryV1SavePutRequest.md)|  | [optional] |

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

