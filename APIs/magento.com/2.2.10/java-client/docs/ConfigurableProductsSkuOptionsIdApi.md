# ConfigurableProductsSkuOptionsIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurableProductOptionRepositoryV1DeleteByIdDelete**](ConfigurableProductsSkuOptionsIdApi.md#configurableProductOptionRepositoryV1DeleteByIdDelete) | **DELETE** /V1/configurable-products/{sku}/options/{id} | configurable-products/{sku}/options/{id} |
| [**configurableProductOptionRepositoryV1GetGet**](ConfigurableProductsSkuOptionsIdApi.md#configurableProductOptionRepositoryV1GetGet) | **GET** /V1/configurable-products/{sku}/options/{id} | configurable-products/{sku}/options/{id} |
| [**configurableProductOptionRepositoryV1SavePut**](ConfigurableProductsSkuOptionsIdApi.md#configurableProductOptionRepositoryV1SavePut) | **PUT** /V1/configurable-products/{sku}/options/{id} | configurable-products/{sku}/options/{id} |


<a id="configurableProductOptionRepositoryV1DeleteByIdDelete"></a>
# **configurableProductOptionRepositoryV1DeleteByIdDelete**
> Boolean configurableProductOptionRepositoryV1DeleteByIdDelete(sku, id)

configurable-products/{sku}/options/{id}

Remove option from configurable product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsSkuOptionsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsSkuOptionsIdApi apiInstance = new ConfigurableProductsSkuOptionsIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer id = 56; // Integer | 
    try {
      Boolean result = apiInstance.configurableProductOptionRepositoryV1DeleteByIdDelete(sku, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsSkuOptionsIdApi#configurableProductOptionRepositoryV1DeleteByIdDelete");
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
| **id** | **Integer**|  | |

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

<a id="configurableProductOptionRepositoryV1GetGet"></a>
# **configurableProductOptionRepositoryV1GetGet**
> ConfigurableProductDataOptionInterface configurableProductOptionRepositoryV1GetGet(sku, id)

configurable-products/{sku}/options/{id}

Get option for configurable product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsSkuOptionsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsSkuOptionsIdApi apiInstance = new ConfigurableProductsSkuOptionsIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer id = 56; // Integer | 
    try {
      ConfigurableProductDataOptionInterface result = apiInstance.configurableProductOptionRepositoryV1GetGet(sku, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsSkuOptionsIdApi#configurableProductOptionRepositoryV1GetGet");
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
| **id** | **Integer**|  | |

### Return type

[**ConfigurableProductDataOptionInterface**](ConfigurableProductDataOptionInterface.md)

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

<a id="configurableProductOptionRepositoryV1SavePut"></a>
# **configurableProductOptionRepositoryV1SavePut**
> Integer configurableProductOptionRepositoryV1SavePut(sku, id, configurableProductOptionRepositoryV1SavePostRequest)

configurable-products/{sku}/options/{id}

Save option

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurableProductsSkuOptionsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ConfigurableProductsSkuOptionsIdApi apiInstance = new ConfigurableProductsSkuOptionsIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    String id = "id_example"; // String | 
    ConfigurableProductOptionRepositoryV1SavePostRequest configurableProductOptionRepositoryV1SavePostRequest = new ConfigurableProductOptionRepositoryV1SavePostRequest(); // ConfigurableProductOptionRepositoryV1SavePostRequest | 
    try {
      Integer result = apiInstance.configurableProductOptionRepositoryV1SavePut(sku, id, configurableProductOptionRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurableProductsSkuOptionsIdApi#configurableProductOptionRepositoryV1SavePut");
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
| **id** | **String**|  | |
| **configurableProductOptionRepositoryV1SavePostRequest** | [**ConfigurableProductOptionRepositoryV1SavePostRequest**](ConfigurableProductOptionRepositoryV1SavePostRequest.md)|  | [optional] |

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

