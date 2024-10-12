# PurchasesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**purchasesDelete**](PurchasesApi.md#purchasesDelete) | **DELETE** /v1/purchases/{id} | Removes an existing Purchase. |
| [**purchasesGet**](PurchasesApi.md#purchasesGet) | **GET** /v1/purchases | Returns a list of company&#39;s Purchases. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. |
| [**purchasesPost**](PurchasesApi.md#purchasesPost) | **POST** /v1/purchases | Creates a new Purchase. |
| [**purchasesProcessBatch**](PurchasesApi.md#purchasesProcessBatch) | **PUT** /v1/purchases/batch | Processes a batch of Purchases. |
| [**purchasesPut**](PurchasesApi.md#purchasesPut) | **PUT** /v1/purchases/{id} | Updates an existing Purchase. |
| [**v1PurchasesIdGet**](PurchasesApi.md#v1PurchasesIdGet) | **GET** /v1/purchases/{id} | Returns information about a single Purchases. |


<a id="purchasesDelete"></a>
# **purchasesDelete**
> Object purchasesDelete(id, timestamp)

Removes an existing Purchase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    Long id = 56L; // Long | Id of Purchase to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Purchase to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.purchasesDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#purchasesDelete");
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
| **id** | **Long**| Id of Purchase to remove. | |
| **timestamp** | **String**| Timestamp of Purchase to remove. Should be encoded in Base64. | |

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

<a id="purchasesGet"></a>
# **purchasesGet**
> PageResultPurchaseQueryDto purchasesGet()

Returns a list of company&#39;s Purchases. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    try {
      PageResultPurchaseQueryDto result = apiInstance.purchasesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#purchasesGet");
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

[**PageResultPurchaseQueryDto**](PageResultPurchaseQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="purchasesPost"></a>
# **purchasesPost**
> Object purchasesPost(purchaseDto)

Creates a new Purchase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    PurchaseDto purchaseDto = new PurchaseDto(); // PurchaseDto | Information of Purchase to create.
    try {
      Object result = apiInstance.purchasesPost(purchaseDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#purchasesPost");
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
| **purchaseDto** | [**PurchaseDto**](PurchaseDto.md)| Information of Purchase to create. | |

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

<a id="purchasesProcessBatch"></a>
# **purchasesProcessBatch**
> Object purchasesProcessBatch(batchItemPurchaseDto)

Processes a batch of Purchases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    List<BatchItemPurchaseDto> batchItemPurchaseDto = Arrays.asList(); // List<BatchItemPurchaseDto> | Batch of Purchases to process.
    try {
      Object result = apiInstance.purchasesProcessBatch(batchItemPurchaseDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#purchasesProcessBatch");
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
| **batchItemPurchaseDto** | [**List&lt;BatchItemPurchaseDto&gt;**](BatchItemPurchaseDto.md)| Batch of Purchases to process. | |

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

<a id="purchasesPut"></a>
# **purchasesPut**
> Object purchasesPut(id, purchaseDto)

Updates an existing Purchase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    Long id = 56L; // Long | Id of Purchase to update.
    PurchaseDto purchaseDto = new PurchaseDto(); // PurchaseDto | Information of Purchase to update.
    try {
      Object result = apiInstance.purchasesPut(id, purchaseDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#purchasesPut");
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
| **id** | **Long**| Id of Purchase to update. | |
| **purchaseDto** | [**PurchaseDto**](PurchaseDto.md)| Information of Purchase to update. | |

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

<a id="v1PurchasesIdGet"></a>
# **v1PurchasesIdGet**
> PurchaseDto v1PurchasesIdGet(id)

Returns information about a single Purchases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    Long id = 56L; // Long | Id of Purchase to return.
    try {
      PurchaseDto result = apiInstance.v1PurchasesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#v1PurchasesIdGet");
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
| **id** | **Long**| Id of Purchase to return. | |

### Return type

[**PurchaseDto**](PurchaseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

