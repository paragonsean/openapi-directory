# SalesRepApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRepDelete**](SalesRepApi.md#salesRepDelete) | **DELETE** /v1/salesReps/{id} | Removes an existing Sale Rep. |
| [**salesRepGet**](SalesRepApi.md#salesRepGet) | **GET** /v1/salesReps | Returns a list of company&#39;s SaleRep.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;. |
| [**salesRepPost**](SalesRepApi.md#salesRepPost) | **POST** /v1/salesReps | Creates a new SaleRep. |
| [**salesRepProcessBatch**](SalesRepApi.md#salesRepProcessBatch) | **PUT** /v1/salesReps/batch | Processes a batch of Sale Rep. |
| [**salesRepPut**](SalesRepApi.md#salesRepPut) | **PUT** /v1/salesReps/{id} | Updates an existing Sale Rep. |
| [**v1SalesRepsIdGet**](SalesRepApi.md#v1SalesRepsIdGet) | **GET** /v1/salesReps/{id} | Returns information about a single SaleRep. |


<a id="salesRepDelete"></a>
# **salesRepDelete**
> Object salesRepDelete(id, timestamp)

Removes an existing Sale Rep.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesRepApi apiInstance = new SalesRepApi(defaultClient);
    Long id = 56L; // Long | Id of Sale Rep to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Sale Rep to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.salesRepDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRepApi#salesRepDelete");
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
| **id** | **Long**| Id of Sale Rep to remove. | |
| **timestamp** | **String**| Timestamp of Sale Rep to remove. Should be encoded in Base64. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesRepGet"></a>
# **salesRepGet**
> PageResultSaleRepsDto salesRepGet()

Returns a list of company&#39;s SaleRep.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesRepApi apiInstance = new SalesRepApi(defaultClient);
    try {
      PageResultSaleRepsDto result = apiInstance.salesRepGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRepApi#salesRepGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PageResultSaleRepsDto**](PageResultSaleRepsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesRepPost"></a>
# **salesRepPost**
> Object salesRepPost(saleRepsDto)

Creates a new SaleRep.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesRepApi apiInstance = new SalesRepApi(defaultClient);
    SaleRepsDto saleRepsDto = new SaleRepsDto(); // SaleRepsDto | Information of Sale Rep to create.
    try {
      Object result = apiInstance.salesRepPost(saleRepsDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRepApi#salesRepPost");
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
| **saleRepsDto** | [**SaleRepsDto**](SaleRepsDto.md)| Information of Sale Rep to create. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesRepProcessBatch"></a>
# **salesRepProcessBatch**
> Object salesRepProcessBatch(batchItemSaleRepsDto)

Processes a batch of Sale Rep.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesRepApi apiInstance = new SalesRepApi(defaultClient);
    List<BatchItemSaleRepsDto> batchItemSaleRepsDto = Arrays.asList(); // List<BatchItemSaleRepsDto> | Batch of Sale Rep to process.
    try {
      Object result = apiInstance.salesRepProcessBatch(batchItemSaleRepsDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRepApi#salesRepProcessBatch");
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
| **batchItemSaleRepsDto** | [**List&lt;BatchItemSaleRepsDto&gt;**](BatchItemSaleRepsDto.md)| Batch of Sale Rep to process. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesRepPut"></a>
# **salesRepPut**
> Object salesRepPut(id, saleRepsDto)

Updates an existing Sale Rep.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesRepApi apiInstance = new SalesRepApi(defaultClient);
    Long id = 56L; // Long | Id of Sale Rep to update.
    SaleRepsDto saleRepsDto = new SaleRepsDto(); // SaleRepsDto | Information of Sale Rep to update.
    try {
      Object result = apiInstance.salesRepPut(id, saleRepsDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRepApi#salesRepPut");
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
| **id** | **Long**| Id of Sale Rep to update. | |
| **saleRepsDto** | [**SaleRepsDto**](SaleRepsDto.md)| Information of Sale Rep to update. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v1SalesRepsIdGet"></a>
# **v1SalesRepsIdGet**
> SaleRepsDto v1SalesRepsIdGet(id)

Returns information about a single SaleRep.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesRepApi apiInstance = new SalesRepApi(defaultClient);
    Long id = 56L; // Long | Id of Sale Rep to return.
    try {
      SaleRepsDto result = apiInstance.v1SalesRepsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRepApi#v1SalesRepsIdGet");
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
| **id** | **Long**| Id of Sale Rep to return. | |

### Return type

[**SaleRepsDto**](SaleRepsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

