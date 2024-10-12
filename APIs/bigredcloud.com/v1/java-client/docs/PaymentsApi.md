# PaymentsApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsDelete**](PaymentsApi.md#paymentsDelete) | **DELETE** /v1/payments/{id} | Removes an existing Payment. |
| [**paymentsGet**](PaymentsApi.md#paymentsGet) | **GET** /v1/payments | Returns a list of company&#39;s Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. |
| [**paymentsPost**](PaymentsApi.md#paymentsPost) | **POST** /v1/payments | Creates a new Payment. |
| [**paymentsProcessBatch**](PaymentsApi.md#paymentsProcessBatch) | **PUT** /v1/payments/batch | Processes a batch of Payments. |
| [**paymentsPut**](PaymentsApi.md#paymentsPut) | **PUT** /v1/payments/{id} | Updates an existing Payment. |
| [**v1PaymentsIdGet**](PaymentsApi.md#v1PaymentsIdGet) | **GET** /v1/payments/{id} | Returns information about a single Payments. |


<a id="paymentsDelete"></a>
# **paymentsDelete**
> Object paymentsDelete(id, timestamp)

Removes an existing Payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Long id = 56L; // Long | Id of Payment to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Payment to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.paymentsDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsDelete");
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
| **id** | **Long**| Id of Payment to remove. | |
| **timestamp** | **String**| Timestamp of Payment to remove. Should be encoded in Base64. | |

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

<a id="paymentsGet"></a>
# **paymentsGet**
> PageResultPaymentQueryDto paymentsGet()

Returns a list of company&#39;s Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      PageResultPaymentQueryDto result = apiInstance.paymentsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsGet");
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

[**PageResultPaymentQueryDto**](PageResultPaymentQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="paymentsPost"></a>
# **paymentsPost**
> Object paymentsPost(paymentDto)

Creates a new Payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    PaymentDto paymentDto = new PaymentDto(); // PaymentDto | Information of Payment to create.
    try {
      Object result = apiInstance.paymentsPost(paymentDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsPost");
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
| **paymentDto** | [**PaymentDto**](PaymentDto.md)| Information of Payment to create. | |

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

<a id="paymentsProcessBatch"></a>
# **paymentsProcessBatch**
> Object paymentsProcessBatch(batchItemPaymentDto)

Processes a batch of Payments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    List<BatchItemPaymentDto> batchItemPaymentDto = Arrays.asList(); // List<BatchItemPaymentDto> | Batch of Payments to process.
    try {
      Object result = apiInstance.paymentsProcessBatch(batchItemPaymentDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsProcessBatch");
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
| **batchItemPaymentDto** | [**List&lt;BatchItemPaymentDto&gt;**](BatchItemPaymentDto.md)| Batch of Payments to process. | |

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

<a id="paymentsPut"></a>
# **paymentsPut**
> Object paymentsPut(id, paymentDto)

Updates an existing Payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Long id = 56L; // Long | Id of Payment to update.
    PaymentDto paymentDto = new PaymentDto(); // PaymentDto | Information of Payment to update.
    try {
      Object result = apiInstance.paymentsPut(id, paymentDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsPut");
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
| **id** | **Long**| Id of Payment to update. | |
| **paymentDto** | [**PaymentDto**](PaymentDto.md)| Information of Payment to update. | |

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

<a id="v1PaymentsIdGet"></a>
# **v1PaymentsIdGet**
> PaymentDto v1PaymentsIdGet(id)

Returns information about a single Payments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    Long id = 56L; // Long | Id of Payment to return.
    try {
      PaymentDto result = apiInstance.v1PaymentsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#v1PaymentsIdGet");
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
| **id** | **Long**| Id of Payment to return. | |

### Return type

[**PaymentDto**](PaymentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

