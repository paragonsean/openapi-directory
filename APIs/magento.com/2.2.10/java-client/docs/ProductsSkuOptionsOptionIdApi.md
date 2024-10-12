# ProductsSkuOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete**](ProductsSkuOptionsOptionIdApi.md#catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete) | **DELETE** /V1/products/{sku}/options/{optionId} | products/{sku}/options/{optionId} |
| [**catalogProductCustomOptionRepositoryV1GetGet**](ProductsSkuOptionsOptionIdApi.md#catalogProductCustomOptionRepositoryV1GetGet) | **GET** /V1/products/{sku}/options/{optionId} | products/{sku}/options/{optionId} |


<a id="catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete"></a>
# **catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete**
> Boolean catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete(sku, optionId)

products/{sku}/options/{optionId}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuOptionsOptionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuOptionsOptionIdApi apiInstance = new ProductsSkuOptionsOptionIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer optionId = 56; // Integer | 
    try {
      Boolean result = apiInstance.catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete(sku, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuOptionsOptionIdApi#catalogProductCustomOptionRepositoryV1DeleteByIdentifierDelete");
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
| **optionId** | **Integer**|  | |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="catalogProductCustomOptionRepositoryV1GetGet"></a>
# **catalogProductCustomOptionRepositoryV1GetGet**
> CatalogDataProductCustomOptionInterface catalogProductCustomOptionRepositoryV1GetGet(sku, optionId)

products/{sku}/options/{optionId}

Get custom option for a specific product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuOptionsOptionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuOptionsOptionIdApi apiInstance = new ProductsSkuOptionsOptionIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer optionId = 56; // Integer | 
    try {
      CatalogDataProductCustomOptionInterface result = apiInstance.catalogProductCustomOptionRepositoryV1GetGet(sku, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuOptionsOptionIdApi#catalogProductCustomOptionRepositoryV1GetGet");
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
| **optionId** | **Integer**|  | |

### Return type

[**CatalogDataProductCustomOptionInterface**](CatalogDataProductCustomOptionInterface.md)

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

