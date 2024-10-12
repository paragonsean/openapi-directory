# ProductsSkuMediaEntryIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeMediaGalleryManagementV1GetGet**](ProductsSkuMediaEntryIdApi.md#catalogProductAttributeMediaGalleryManagementV1GetGet) | **GET** /V1/products/{sku}/media/{entryId} | products/{sku}/media/{entryId} |
| [**catalogProductAttributeMediaGalleryManagementV1RemoveDelete**](ProductsSkuMediaEntryIdApi.md#catalogProductAttributeMediaGalleryManagementV1RemoveDelete) | **DELETE** /V1/products/{sku}/media/{entryId} | products/{sku}/media/{entryId} |
| [**catalogProductAttributeMediaGalleryManagementV1UpdatePut**](ProductsSkuMediaEntryIdApi.md#catalogProductAttributeMediaGalleryManagementV1UpdatePut) | **PUT** /V1/products/{sku}/media/{entryId} | products/{sku}/media/{entryId} |


<a id="catalogProductAttributeMediaGalleryManagementV1GetGet"></a>
# **catalogProductAttributeMediaGalleryManagementV1GetGet**
> CatalogDataProductAttributeMediaGalleryEntryInterface catalogProductAttributeMediaGalleryManagementV1GetGet(sku, entryId)

products/{sku}/media/{entryId}

Return information about gallery entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuMediaEntryIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuMediaEntryIdApi apiInstance = new ProductsSkuMediaEntryIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer entryId = 56; // Integer | 
    try {
      CatalogDataProductAttributeMediaGalleryEntryInterface result = apiInstance.catalogProductAttributeMediaGalleryManagementV1GetGet(sku, entryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuMediaEntryIdApi#catalogProductAttributeMediaGalleryManagementV1GetGet");
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
| **entryId** | **Integer**|  | |

### Return type

[**CatalogDataProductAttributeMediaGalleryEntryInterface**](CatalogDataProductAttributeMediaGalleryEntryInterface.md)

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

<a id="catalogProductAttributeMediaGalleryManagementV1RemoveDelete"></a>
# **catalogProductAttributeMediaGalleryManagementV1RemoveDelete**
> Boolean catalogProductAttributeMediaGalleryManagementV1RemoveDelete(sku, entryId)

products/{sku}/media/{entryId}

Remove gallery entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuMediaEntryIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuMediaEntryIdApi apiInstance = new ProductsSkuMediaEntryIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer entryId = 56; // Integer | 
    try {
      Boolean result = apiInstance.catalogProductAttributeMediaGalleryManagementV1RemoveDelete(sku, entryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuMediaEntryIdApi#catalogProductAttributeMediaGalleryManagementV1RemoveDelete");
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
| **entryId** | **Integer**|  | |

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

<a id="catalogProductAttributeMediaGalleryManagementV1UpdatePut"></a>
# **catalogProductAttributeMediaGalleryManagementV1UpdatePut**
> Boolean catalogProductAttributeMediaGalleryManagementV1UpdatePut(sku, entryId, catalogProductAttributeMediaGalleryManagementV1CreatePostRequest)

products/{sku}/media/{entryId}

Update gallery entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuMediaEntryIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuMediaEntryIdApi apiInstance = new ProductsSkuMediaEntryIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    String entryId = "entryId_example"; // String | 
    CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest catalogProductAttributeMediaGalleryManagementV1CreatePostRequest = new CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest(); // CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest | 
    try {
      Boolean result = apiInstance.catalogProductAttributeMediaGalleryManagementV1UpdatePut(sku, entryId, catalogProductAttributeMediaGalleryManagementV1CreatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuMediaEntryIdApi#catalogProductAttributeMediaGalleryManagementV1UpdatePut");
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
| **entryId** | **String**|  | |
| **catalogProductAttributeMediaGalleryManagementV1CreatePostRequest** | [**CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest**](CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest.md)|  | [optional] |

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

