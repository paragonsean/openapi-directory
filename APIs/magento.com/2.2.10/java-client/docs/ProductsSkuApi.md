# ProductsSkuApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductRepositoryV1DeleteByIdDelete**](ProductsSkuApi.md#catalogProductRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/{sku} | products/{sku} |
| [**catalogProductRepositoryV1GetGet**](ProductsSkuApi.md#catalogProductRepositoryV1GetGet) | **GET** /V1/products/{sku} | products/{sku} |
| [**catalogProductRepositoryV1SavePut**](ProductsSkuApi.md#catalogProductRepositoryV1SavePut) | **PUT** /V1/products/{sku} | products/{sku} |


<a id="catalogProductRepositoryV1DeleteByIdDelete"></a>
# **catalogProductRepositoryV1DeleteByIdDelete**
> Boolean catalogProductRepositoryV1DeleteByIdDelete(sku)

products/{sku}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuApi apiInstance = new ProductsSkuApi(defaultClient);
    String sku = "sku_example"; // String | 
    try {
      Boolean result = apiInstance.catalogProductRepositoryV1DeleteByIdDelete(sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuApi#catalogProductRepositoryV1DeleteByIdDelete");
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

<a id="catalogProductRepositoryV1GetGet"></a>
# **catalogProductRepositoryV1GetGet**
> CatalogDataProductInterface catalogProductRepositoryV1GetGet(sku, editMode, storeId, forceReload)

products/{sku}

Get info about product by product SKU

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuApi apiInstance = new ProductsSkuApi(defaultClient);
    String sku = "sku_example"; // String | 
    Boolean editMode = true; // Boolean | 
    Integer storeId = 56; // Integer | 
    Boolean forceReload = true; // Boolean | 
    try {
      CatalogDataProductInterface result = apiInstance.catalogProductRepositoryV1GetGet(sku, editMode, storeId, forceReload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuApi#catalogProductRepositoryV1GetGet");
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
| **editMode** | **Boolean**|  | [optional] |
| **storeId** | **Integer**|  | [optional] |
| **forceReload** | **Boolean**|  | [optional] |

### Return type

[**CatalogDataProductInterface**](CatalogDataProductInterface.md)

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

<a id="catalogProductRepositoryV1SavePut"></a>
# **catalogProductRepositoryV1SavePut**
> CatalogDataProductInterface catalogProductRepositoryV1SavePut(sku, catalogProductRepositoryV1SavePostRequest)

products/{sku}

Create product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuApi apiInstance = new ProductsSkuApi(defaultClient);
    String sku = "sku_example"; // String | 
    CatalogProductRepositoryV1SavePostRequest catalogProductRepositoryV1SavePostRequest = new CatalogProductRepositoryV1SavePostRequest(); // CatalogProductRepositoryV1SavePostRequest | 
    try {
      CatalogDataProductInterface result = apiInstance.catalogProductRepositoryV1SavePut(sku, catalogProductRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuApi#catalogProductRepositoryV1SavePut");
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
| **catalogProductRepositoryV1SavePostRequest** | [**CatalogProductRepositoryV1SavePostRequest**](CatalogProductRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CatalogDataProductInterface**](CatalogDataProductInterface.md)

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

