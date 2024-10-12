# ProductsAttributesAttributeCodeOptionsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeOptionManagementV1AddPost**](ProductsAttributesAttributeCodeOptionsApi.md#catalogProductAttributeOptionManagementV1AddPost) | **POST** /V1/products/attributes/{attributeCode}/options | products/attributes/{attributeCode}/options |
| [**catalogProductAttributeOptionManagementV1GetItemsGet**](ProductsAttributesAttributeCodeOptionsApi.md#catalogProductAttributeOptionManagementV1GetItemsGet) | **GET** /V1/products/attributes/{attributeCode}/options | products/attributes/{attributeCode}/options |


<a id="catalogProductAttributeOptionManagementV1AddPost"></a>
# **catalogProductAttributeOptionManagementV1AddPost**
> Boolean catalogProductAttributeOptionManagementV1AddPost(attributeCode, catalogProductAttributeOptionManagementV1AddPostRequest)

products/attributes/{attributeCode}/options

Add option to attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributesAttributeCodeOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributesAttributeCodeOptionsApi apiInstance = new ProductsAttributesAttributeCodeOptionsApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    CatalogProductAttributeOptionManagementV1AddPostRequest catalogProductAttributeOptionManagementV1AddPostRequest = new CatalogProductAttributeOptionManagementV1AddPostRequest(); // CatalogProductAttributeOptionManagementV1AddPostRequest | 
    try {
      Boolean result = apiInstance.catalogProductAttributeOptionManagementV1AddPost(attributeCode, catalogProductAttributeOptionManagementV1AddPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributesAttributeCodeOptionsApi#catalogProductAttributeOptionManagementV1AddPost");
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
| **catalogProductAttributeOptionManagementV1AddPostRequest** | [**CatalogProductAttributeOptionManagementV1AddPostRequest**](CatalogProductAttributeOptionManagementV1AddPostRequest.md)|  | [optional] |

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

<a id="catalogProductAttributeOptionManagementV1GetItemsGet"></a>
# **catalogProductAttributeOptionManagementV1GetItemsGet**
> List&lt;EavDataAttributeOptionInterface&gt; catalogProductAttributeOptionManagementV1GetItemsGet(attributeCode)

products/attributes/{attributeCode}/options

Retrieve list of attribute options

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributesAttributeCodeOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributesAttributeCodeOptionsApi apiInstance = new ProductsAttributesAttributeCodeOptionsApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    try {
      List<EavDataAttributeOptionInterface> result = apiInstance.catalogProductAttributeOptionManagementV1GetItemsGet(attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributesAttributeCodeOptionsApi#catalogProductAttributeOptionManagementV1GetItemsGet");
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

