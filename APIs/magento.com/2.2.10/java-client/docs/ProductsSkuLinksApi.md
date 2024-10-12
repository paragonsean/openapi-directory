# ProductsSkuLinksApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductLinkManagementV1SetProductLinksPost**](ProductsSkuLinksApi.md#catalogProductLinkManagementV1SetProductLinksPost) | **POST** /V1/products/{sku}/links | products/{sku}/links |
| [**catalogProductLinkRepositoryV1SavePut**](ProductsSkuLinksApi.md#catalogProductLinkRepositoryV1SavePut) | **PUT** /V1/products/{sku}/links | products/{sku}/links |


<a id="catalogProductLinkManagementV1SetProductLinksPost"></a>
# **catalogProductLinkManagementV1SetProductLinksPost**
> Boolean catalogProductLinkManagementV1SetProductLinksPost(sku, catalogProductLinkManagementV1SetProductLinksPostRequest)

products/{sku}/links

Assign a product link to another product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuLinksApi apiInstance = new ProductsSkuLinksApi(defaultClient);
    String sku = "sku_example"; // String | 
    CatalogProductLinkManagementV1SetProductLinksPostRequest catalogProductLinkManagementV1SetProductLinksPostRequest = new CatalogProductLinkManagementV1SetProductLinksPostRequest(); // CatalogProductLinkManagementV1SetProductLinksPostRequest | 
    try {
      Boolean result = apiInstance.catalogProductLinkManagementV1SetProductLinksPost(sku, catalogProductLinkManagementV1SetProductLinksPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuLinksApi#catalogProductLinkManagementV1SetProductLinksPost");
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
| **catalogProductLinkManagementV1SetProductLinksPostRequest** | [**CatalogProductLinkManagementV1SetProductLinksPostRequest**](CatalogProductLinkManagementV1SetProductLinksPostRequest.md)|  | [optional] |

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

<a id="catalogProductLinkRepositoryV1SavePut"></a>
# **catalogProductLinkRepositoryV1SavePut**
> Boolean catalogProductLinkRepositoryV1SavePut(sku, catalogProductLinkRepositoryV1SavePutRequest)

products/{sku}/links

Save product link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuLinksApi apiInstance = new ProductsSkuLinksApi(defaultClient);
    String sku = "sku_example"; // String | 
    CatalogProductLinkRepositoryV1SavePutRequest catalogProductLinkRepositoryV1SavePutRequest = new CatalogProductLinkRepositoryV1SavePutRequest(); // CatalogProductLinkRepositoryV1SavePutRequest | 
    try {
      Boolean result = apiInstance.catalogProductLinkRepositoryV1SavePut(sku, catalogProductLinkRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuLinksApi#catalogProductLinkRepositoryV1SavePut");
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
| **catalogProductLinkRepositoryV1SavePutRequest** | [**CatalogProductLinkRepositoryV1SavePutRequest**](CatalogProductLinkRepositoryV1SavePutRequest.md)|  | [optional] |

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

