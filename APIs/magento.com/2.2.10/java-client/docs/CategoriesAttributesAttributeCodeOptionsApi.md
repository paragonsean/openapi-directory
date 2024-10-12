# CategoriesAttributesAttributeCodeOptionsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCategoryAttributeOptionManagementV1GetItemsGet**](CategoriesAttributesAttributeCodeOptionsApi.md#catalogCategoryAttributeOptionManagementV1GetItemsGet) | **GET** /V1/categories/attributes/{attributeCode}/options | categories/attributes/{attributeCode}/options |


<a id="catalogCategoryAttributeOptionManagementV1GetItemsGet"></a>
# **catalogCategoryAttributeOptionManagementV1GetItemsGet**
> List&lt;EavDataAttributeOptionInterface&gt; catalogCategoryAttributeOptionManagementV1GetItemsGet(attributeCode)

categories/attributes/{attributeCode}/options

Retrieve list of attribute options

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesAttributesAttributeCodeOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CategoriesAttributesAttributeCodeOptionsApi apiInstance = new CategoriesAttributesAttributeCodeOptionsApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    try {
      List<EavDataAttributeOptionInterface> result = apiInstance.catalogCategoryAttributeOptionManagementV1GetItemsGet(attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesAttributesAttributeCodeOptionsApi#catalogCategoryAttributeOptionManagementV1GetItemsGet");
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

[**List&lt;EavDataAttributeOptionInterface&gt;**](EavDataAttributeOptionInterface.md)

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

