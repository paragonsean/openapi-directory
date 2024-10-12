# ProductsSkuMediaApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeMediaGalleryManagementV1CreatePost**](ProductsSkuMediaApi.md#catalogProductAttributeMediaGalleryManagementV1CreatePost) | **POST** /V1/products/{sku}/media | products/{sku}/media |
| [**catalogProductAttributeMediaGalleryManagementV1GetListGet**](ProductsSkuMediaApi.md#catalogProductAttributeMediaGalleryManagementV1GetListGet) | **GET** /V1/products/{sku}/media | products/{sku}/media |


<a id="catalogProductAttributeMediaGalleryManagementV1CreatePost"></a>
# **catalogProductAttributeMediaGalleryManagementV1CreatePost**
> Integer catalogProductAttributeMediaGalleryManagementV1CreatePost(sku, catalogProductAttributeMediaGalleryManagementV1CreatePostRequest)

products/{sku}/media

Create new gallery entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuMediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuMediaApi apiInstance = new ProductsSkuMediaApi(defaultClient);
    String sku = "sku_example"; // String | 
    CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest catalogProductAttributeMediaGalleryManagementV1CreatePostRequest = new CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest(); // CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest | 
    try {
      Integer result = apiInstance.catalogProductAttributeMediaGalleryManagementV1CreatePost(sku, catalogProductAttributeMediaGalleryManagementV1CreatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuMediaApi#catalogProductAttributeMediaGalleryManagementV1CreatePost");
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
| **sku** | **String**|  | |
| **catalogProductAttributeMediaGalleryManagementV1CreatePostRequest** | [**CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest**](CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest.md)|  | [optional] |

### Return type

**Integer**

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

<a id="catalogProductAttributeMediaGalleryManagementV1GetListGet"></a>
# **catalogProductAttributeMediaGalleryManagementV1GetListGet**
> List&lt;CatalogDataProductAttributeMediaGalleryEntryInterface&gt; catalogProductAttributeMediaGalleryManagementV1GetListGet(sku)

products/{sku}/media

Retrieve the list of gallery entries associated with given product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuMediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuMediaApi apiInstance = new ProductsSkuMediaApi(defaultClient);
    String sku = "sku_example"; // String | 
    try {
      List<CatalogDataProductAttributeMediaGalleryEntryInterface> result = apiInstance.catalogProductAttributeMediaGalleryManagementV1GetListGet(sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuMediaApi#catalogProductAttributeMediaGalleryManagementV1GetListGet");
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
| **sku** | **String**|  | |

### Return type

[**List&lt;CatalogDataProductAttributeMediaGalleryEntryInterface&gt;**](CatalogDataProductAttributeMediaGalleryEntryInterface.md)

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

