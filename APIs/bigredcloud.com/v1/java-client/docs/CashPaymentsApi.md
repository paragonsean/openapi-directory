# CashPaymentsApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cashPaymentsDelete**](CashPaymentsApi.md#cashPaymentsDelete) | **DELETE** /v1/cashPayments/{id} | Removes an existing Cash Payment. |
| [**cashPaymentsGet**](CashPaymentsApi.md#cashPaymentsGet) | **GET** /v1/cashPayments | Returns a list of company&#39;s Cash Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. |
| [**cashPaymentsPost**](CashPaymentsApi.md#cashPaymentsPost) | **POST** /v1/cashPayments | Creates a new Cash Payment. |
| [**cashPaymentsProcessBatch**](CashPaymentsApi.md#cashPaymentsProcessBatch) | **PUT** /v1/cashPayments/batch | Processes a batch of Cash Payments. |
| [**cashPaymentsPut**](CashPaymentsApi.md#cashPaymentsPut) | **PUT** /v1/cashPayments/{id} | Updates an existing Cash Payment. |
| [**v1CashPaymentsIdGet**](CashPaymentsApi.md#v1CashPaymentsIdGet) | **GET** /v1/cashPayments/{id} | Returns information about a single Cash Payment. |


<a id="cashPaymentsDelete"></a>
# **cashPaymentsDelete**
> Object cashPaymentsDelete(id, timestamp)

Removes an existing Cash Payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashPaymentsApi apiInstance = new CashPaymentsApi(defaultClient);
    Long id = 56L; // Long | Id of Cash Receipt to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Cash Receipt to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.cashPaymentsDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashPaymentsApi#cashPaymentsDelete");
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

<a id="cashPaymentsGet"></a>
# **cashPaymentsGet**
> PageResultCashPaymentQueryDto cashPaymentsGet()

Returns a list of company&#39;s Cash Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashPaymentsApi apiInstance = new CashPaymentsApi(defaultClient);
    try {
      PageResultCashPaymentQueryDto result = apiInstance.cashPaymentsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashPaymentsApi#cashPaymentsGet");
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

[**PageResultCashPaymentQueryDto**](PageResultCashPaymentQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="cashPaymentsPost"></a>
# **cashPaymentsPost**
> Object cashPaymentsPost(cashPaymentDto)

Creates a new Cash Payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashPaymentsApi apiInstance = new CashPaymentsApi(defaultClient);
    CashPaymentDto cashPaymentDto = new CashPaymentDto(); // CashPaymentDto | Information of Cash Receipt to create.
    try {
      Object result = apiInstance.cashPaymentsPost(cashPaymentDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashPaymentsApi#cashPaymentsPost");
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
| **cashPaymentDto** | [**CashPaymentDto**](CashPaymentDto.md)| Information of Cash Receipt to create. | |

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

<a id="cashPaymentsProcessBatch"></a>
# **cashPaymentsProcessBatch**
> Object cashPaymentsProcessBatch(batchItemCashPaymentDto)

Processes a batch of Cash Payments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashPaymentsApi apiInstance = new CashPaymentsApi(defaultClient);
    List<BatchItemCashPaymentDto> batchItemCashPaymentDto = Arrays.asList(); // List<BatchItemCashPaymentDto> | Batch of Cash Receipts to process.
    try {
      Object result = apiInstance.cashPaymentsProcessBatch(batchItemCashPaymentDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashPaymentsApi#cashPaymentsProcessBatch");
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
| **batchItemCashPaymentDto** | [**List&lt;BatchItemCashPaymentDto&gt;**](BatchItemCashPaymentDto.md)| Batch of Cash Receipts to process. | |

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

<a id="cashPaymentsPut"></a>
# **cashPaymentsPut**
> Object cashPaymentsPut(id, cashPaymentDto)

Updates an existing Cash Payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashPaymentsApi apiInstance = new CashPaymentsApi(defaultClient);
    Long id = 56L; // Long | Id of Cash Receipt to update.
    CashPaymentDto cashPaymentDto = new CashPaymentDto(); // CashPaymentDto | Information of Cash Receipt to update.
    try {
      Object result = apiInstance.cashPaymentsPut(id, cashPaymentDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashPaymentsApi#cashPaymentsPut");
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
| **cashPaymentDto** | [**CashPaymentDto**](CashPaymentDto.md)| Information of Cash Receipt to update. | |

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

<a id="v1CashPaymentsIdGet"></a>
# **v1CashPaymentsIdGet**
> CashPaymentDto v1CashPaymentsIdGet(id)

Returns information about a single Cash Payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CashPaymentsApi apiInstance = new CashPaymentsApi(defaultClient);
    Long id = 56L; // Long | Id of Cash Receipt to return.
    try {
      CashPaymentDto result = apiInstance.v1CashPaymentsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashPaymentsApi#v1CashPaymentsIdGet");
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

[**CashPaymentDto**](CashPaymentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

