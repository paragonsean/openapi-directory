# BundleProductsSkuOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundleProductOptionRepositoryV1DeleteByIdDelete**](BundleProductsSkuOptionsOptionIdApi.md#bundleProductOptionRepositoryV1DeleteByIdDelete) | **DELETE** /V1/bundle-products/{sku}/options/{optionId} | bundle-products/{sku}/options/{optionId} |
| [**bundleProductOptionRepositoryV1GetGet**](BundleProductsSkuOptionsOptionIdApi.md#bundleProductOptionRepositoryV1GetGet) | **GET** /V1/bundle-products/{sku}/options/{optionId} | bundle-products/{sku}/options/{optionId} |


<a id="bundleProductOptionRepositoryV1DeleteByIdDelete"></a>
# **bundleProductOptionRepositoryV1DeleteByIdDelete**
> Boolean bundleProductOptionRepositoryV1DeleteByIdDelete(sku, optionId)

bundle-products/{sku}/options/{optionId}

Remove bundle option

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsSkuOptionsOptionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsSkuOptionsOptionIdApi apiInstance = new BundleProductsSkuOptionsOptionIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer optionId = 56; // Integer | 
    try {
      Boolean result = apiInstance.bundleProductOptionRepositoryV1DeleteByIdDelete(sku, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsSkuOptionsOptionIdApi#bundleProductOptionRepositoryV1DeleteByIdDelete");
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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="bundleProductOptionRepositoryV1GetGet"></a>
# **bundleProductOptionRepositoryV1GetGet**
> BundleDataOptionInterface bundleProductOptionRepositoryV1GetGet(sku, optionId)

bundle-products/{sku}/options/{optionId}

Get option for bundle product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundleProductsSkuOptionsOptionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BundleProductsSkuOptionsOptionIdApi apiInstance = new BundleProductsSkuOptionsOptionIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer optionId = 56; // Integer | 
    try {
      BundleDataOptionInterface result = apiInstance.bundleProductOptionRepositoryV1GetGet(sku, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundleProductsSkuOptionsOptionIdApi#bundleProductOptionRepositoryV1GetGet");
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

[**BundleDataOptionInterface**](BundleDataOptionInterface.md)

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

