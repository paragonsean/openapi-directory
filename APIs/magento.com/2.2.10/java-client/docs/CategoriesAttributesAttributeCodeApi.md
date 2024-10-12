# CategoriesAttributesAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCategoryAttributeRepositoryV1GetGet**](CategoriesAttributesAttributeCodeApi.md#catalogCategoryAttributeRepositoryV1GetGet) | **GET** /V1/categories/attributes/{attributeCode} | categories/attributes/{attributeCode} |


<a id="catalogCategoryAttributeRepositoryV1GetGet"></a>
# **catalogCategoryAttributeRepositoryV1GetGet**
> CatalogDataCategoryAttributeInterface catalogCategoryAttributeRepositoryV1GetGet(attributeCode)

categories/attributes/{attributeCode}

Retrieve specific attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesAttributesAttributeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesAttributesAttributeCodeApi apiInstance = new CategoriesAttributesAttributeCodeApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    try {
      CatalogDataCategoryAttributeInterface result = apiInstance.catalogCategoryAttributeRepositoryV1GetGet(attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesAttributesAttributeCodeApi#catalogCategoryAttributeRepositoryV1GetGet");
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
| **attributeCode** | **String**|  | |

### Return type

[**CatalogDataCategoryAttributeInterface**](CatalogDataCategoryAttributeInterface.md)

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

