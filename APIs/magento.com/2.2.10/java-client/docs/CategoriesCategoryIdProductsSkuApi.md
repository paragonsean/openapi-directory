# CategoriesCategoryIdProductsSkuApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCategoryLinkRepositoryV1DeleteByIdsDelete**](CategoriesCategoryIdProductsSkuApi.md#catalogCategoryLinkRepositoryV1DeleteByIdsDelete) | **DELETE** /V1/categories/{categoryId}/products/{sku} | categories/{categoryId}/products/{sku} |


<a id="catalogCategoryLinkRepositoryV1DeleteByIdsDelete"></a>
# **catalogCategoryLinkRepositoryV1DeleteByIdsDelete**
> Boolean catalogCategoryLinkRepositoryV1DeleteByIdsDelete(categoryId, sku)

categories/{categoryId}/products/{sku}

Remove the product assignment from the category by category id and sku

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesCategoryIdProductsSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesCategoryIdProductsSkuApi apiInstance = new CategoriesCategoryIdProductsSkuApi(defaultClient);
    String categoryId = "categoryId_example"; // String | 
    String sku = "sku_example"; // String | 
    try {
      Boolean result = apiInstance.catalogCategoryLinkRepositoryV1DeleteByIdsDelete(categoryId, sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesCategoryIdProductsSkuApi#catalogCategoryLinkRepositoryV1DeleteByIdsDelete");
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
| **sku** | **String**|  | |

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

