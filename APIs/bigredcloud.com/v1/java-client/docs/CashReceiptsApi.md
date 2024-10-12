# CashReceiptsApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cashReceiptsDelete**](CashReceiptsApi.md#cashReceiptsDelete) | **DELETE** /v1/cashReceipts/{id} | Removes an existing Cash Receipt. |
| [**cashReceiptsGet**](CashReceiptsApi.md#cashReceiptsGet) | **GET** /v1/cashReceipts | Returns a list of company&#39;s Cash Receipts. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. |
| [**cashReceiptsPost**](CashReceiptsApi.md#cashReceiptsPost) | **POST** /v1/cashReceipts | Creates a new Cash Receipt. |
| [**cashReceiptsProcessBatch**](CashReceiptsApi.md#cashReceiptsProcessBatch) | **PUT** /v1/cashReceipts/batch | Processes a batch of Cash Receipts. |
| [**cashReceiptsPut**](CashReceiptsApi.md#cashReceiptsPut) | **PUT** /v1/cashReceipts/{id} | Updates an existing Cash Receipt. |
| [**v1CashReceiptsIdGet**](CashReceiptsApi.md#v1CashReceiptsIdGet) | **GET** /v1/cashReceipts/{id} | Returns information about a single Cash Receipt. |


<a id="cashReceiptsDelete"></a>
# **cashReceiptsDelete**
> Object cashReceiptsDelete(id, timestamp)

Removes an existing Cash Receipt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashReceiptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashReceiptsApi apiInstance = new CashReceiptsApi(defaultClient);
    Long id = 56L; // Long | Id of Cash Receipt to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Cash Receipt to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.cashReceiptsDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashReceiptsApi#cashReceiptsDelete");
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
| **id** | **Long**| Id of Cash Receipt to remove. | |
| **timestamp** | **String**| Timestamp of Cash Receipt to remove. Should be encoded in Base64. | |

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

<a id="cashReceiptsGet"></a>
# **cashReceiptsGet**
> PageResultCashReceiptQueryDto cashReceiptsGet()

Returns a list of company&#39;s Cash Receipts. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashReceiptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashReceiptsApi apiInstance = new CashReceiptsApi(defaultClient);
    try {
      PageResultCashReceiptQueryDto result = apiInstance.cashReceiptsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashReceiptsApi#cashReceiptsGet");
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

[**PageResultCashReceiptQueryDto**](PageResultCashReceiptQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="cashReceiptsPost"></a>
# **cashReceiptsPost**
> Object cashReceiptsPost(cashReceiptDto)

Creates a new Cash Receipt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashReceiptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashReceiptsApi apiInstance = new CashReceiptsApi(defaultClient);
    CashReceiptDto cashReceiptDto = new CashReceiptDto(); // CashReceiptDto | Information of Cash Receipt to create.
    try {
      Object result = apiInstance.cashReceiptsPost(cashReceiptDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashReceiptsApi#cashReceiptsPost");
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
| **cashReceiptDto** | [**CashReceiptDto**](CashReceiptDto.md)| Information of Cash Receipt to create. | |

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

<a id="cashReceiptsProcessBatch"></a>
# **cashReceiptsProcessBatch**
> Object cashReceiptsProcessBatch(batchItemCashReceiptDto)

Processes a batch of Cash Receipts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashReceiptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashReceiptsApi apiInstance = new CashReceiptsApi(defaultClient);
    List<BatchItemCashReceiptDto> batchItemCashReceiptDto = Arrays.asList(); // List<BatchItemCashReceiptDto> | Batch of Cash Receipts to process.
    try {
      Object result = apiInstance.cashReceiptsProcessBatch(batchItemCashReceiptDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashReceiptsApi#cashReceiptsProcessBatch");
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
| **batchItemCashReceiptDto** | [**List&lt;BatchItemCashReceiptDto&gt;**](BatchItemCashReceiptDto.md)| Batch of Cash Receipts to process. | |

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

<a id="cashReceiptsPut"></a>
# **cashReceiptsPut**
> Object cashReceiptsPut(id, cashReceiptDto)

Updates an existing Cash Receipt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashReceiptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashReceiptsApi apiInstance = new CashReceiptsApi(defaultClient);
    Long id = 56L; // Long | Id of Cash Receipt to update.
    CashReceiptDto cashReceiptDto = new CashReceiptDto(); // CashReceiptDto | Information of Cash Receipt to update.
    try {
      Object result = apiInstance.cashReceiptsPut(id, cashReceiptDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashReceiptsApi#cashReceiptsPut");
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
| **id** | **Long**| Id of Cash Receipt to update. | |
| **cashReceiptDto** | [**CashReceiptDto**](CashReceiptDto.md)| Information of Cash Receipt to update. | |

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

<a id="v1CashReceiptsIdGet"></a>
# **v1CashReceiptsIdGet**
> CashReceiptDto v1CashReceiptsIdGet(id)

Returns information about a single Cash Receipt.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashReceiptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashReceiptsApi apiInstance = new CashReceiptsApi(defaultClient);
    Long id = 56L; // Long | Id of Cash Receipt to return.
    try {
      CashReceiptDto result = apiInstance.v1CashReceiptsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashReceiptsApi#v1CashReceiptsIdGet");
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
| **id** | **Long**| Id of Cash Receipt to return. | |

### Return type

[**CashReceiptDto**](CashReceiptDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

