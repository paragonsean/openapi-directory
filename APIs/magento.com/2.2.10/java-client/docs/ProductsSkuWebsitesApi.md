# ProductsSkuWebsitesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductWebsiteLinkRepositoryV1SavePost**](ProductsSkuWebsitesApi.md#catalogProductWebsiteLinkRepositoryV1SavePost) | **POST** /V1/products/{sku}/websites | products/{sku}/websites |
| [**catalogProductWebsiteLinkRepositoryV1SavePut**](ProductsSkuWebsitesApi.md#catalogProductWebsiteLinkRepositoryV1SavePut) | **PUT** /V1/products/{sku}/websites | products/{sku}/websites |


<a id="catalogProductWebsiteLinkRepositoryV1SavePost"></a>
# **catalogProductWebsiteLinkRepositoryV1SavePost**
> Boolean catalogProductWebsiteLinkRepositoryV1SavePost(sku, catalogProductWebsiteLinkRepositoryV1SavePutRequest)

products/{sku}/websites

Assign a product to the website

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuWebsitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuWebsitesApi apiInstance = new ProductsSkuWebsitesApi(defaultClient);
    String sku = "sku_example"; // String | 
    CatalogProductWebsiteLinkRepositoryV1SavePutRequest catalogProductWebsiteLinkRepositoryV1SavePutRequest = new CatalogProductWebsiteLinkRepositoryV1SavePutRequest(); // CatalogProductWebsiteLinkRepositoryV1SavePutRequest | 
    try {
      Boolean result = apiInstance.catalogProductWebsiteLinkRepositoryV1SavePost(sku, catalogProductWebsiteLinkRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuWebsitesApi#catalogProductWebsiteLinkRepositoryV1SavePost");
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
| **catalogProductWebsiteLinkRepositoryV1SavePutRequest** | [**CatalogProductWebsiteLinkRepositoryV1SavePutRequest**](CatalogProductWebsiteLinkRepositoryV1SavePutRequest.md)|  | [optional] |

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

<a id="catalogProductWebsiteLinkRepositoryV1SavePut"></a>
# **catalogProductWebsiteLinkRepositoryV1SavePut**
> Boolean catalogProductWebsiteLinkRepositoryV1SavePut(sku, catalogProductWebsiteLinkRepositoryV1SavePutRequest)

products/{sku}/websites

Assign a product to the website

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuWebsitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuWebsitesApi apiInstance = new ProductsSkuWebsitesApi(defaultClient);
    String sku = "sku_example"; // String | 
    CatalogProductWebsiteLinkRepositoryV1SavePutRequest catalogProductWebsiteLinkRepositoryV1SavePutRequest = new CatalogProductWebsiteLinkRepositoryV1SavePutRequest(); // CatalogProductWebsiteLinkRepositoryV1SavePutRequest | 
    try {
      Boolean result = apiInstance.catalogProductWebsiteLinkRepositoryV1SavePut(sku, catalogProductWebsiteLinkRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuWebsitesApi#catalogProductWebsiteLinkRepositoryV1SavePut");
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
| **catalogProductWebsiteLinkRepositoryV1SavePutRequest** | [**CatalogProductWebsiteLinkRepositoryV1SavePutRequest**](CatalogProductWebsiteLinkRepositoryV1SavePutRequest.md)|  | [optional] |

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

