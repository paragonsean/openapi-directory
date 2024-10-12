# ProductsLinksTypeAttributesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductLinkTypeListV1GetItemAttributesGet**](ProductsLinksTypeAttributesApi.md#catalogProductLinkTypeListV1GetItemAttributesGet) | **GET** /V1/products/links/{type}/attributes | products/links/{type}/attributes |


<a id="catalogProductLinkTypeListV1GetItemAttributesGet"></a>
# **catalogProductLinkTypeListV1GetItemAttributesGet**
> List&lt;CatalogDataProductLinkAttributeInterface&gt; catalogProductLinkTypeListV1GetItemAttributesGet(type)

products/links/{type}/attributes

Provide a list of the product link type attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsLinksTypeAttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsLinksTypeAttributesApi apiInstance = new ProductsLinksTypeAttributesApi(defaultClient);
    String type = "type_example"; // String | 
    try {
      List<CatalogDataProductLinkAttributeInterface> result = apiInstance.catalogProductLinkTypeListV1GetItemAttributesGet(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsLinksTypeAttributesApi#catalogProductLinkTypeListV1GetItemAttributesGet");
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
| **type** | **String**|  | |

### Return type

[**List&lt;CatalogDataProductLinkAttributeInterface&gt;**](CatalogDataProductLinkAttributeInterface.md)

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

