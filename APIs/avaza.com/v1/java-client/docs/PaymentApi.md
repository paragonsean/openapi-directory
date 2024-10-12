# PaymentApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentGet**](PaymentApi.md#paymentGet) | **GET** /api/Payment | Gets list of Payments |
| [**paymentGetByID**](PaymentApi.md#paymentGetByID) | **GET** /api/Payment/{id} | Gets Payment by Payment Transaction ID |
| [**paymentPost**](PaymentApi.md#paymentPost) | **POST** /api/Payment | Create new Payment and optionally assign payment allocations to Invoices |


<a id="paymentGet"></a>
# **paymentGet**
> PaymentList paymentGet(invoiceTransactionID, updatedAfter, pageSize, pageNumber)

Gets list of Payments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentApi apiInstance = new PaymentApi(defaultClient);
    Long invoiceTransactionID = 56L; // Long | Filter for Payments that have at least one allocation against a given Invoice Transaction ID
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Filter for Payments updated after a given date
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    try {
      PaymentList result = apiInstance.paymentGet(invoiceTransactionID, updatedAfter, pageSize, pageNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentApi#paymentGet");
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
| **invoiceTransactionID** | **Long**| Filter for Payments that have at least one allocation against a given Invoice Transaction ID | [optional] |
| **updatedAfter** | **OffsetDateTime**| Filter for Payments updated after a given date | [optional] |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |

### Return type

[**PaymentList**](PaymentList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="paymentGetByID"></a>
# **paymentGetByID**
> Payment paymentGetByID(id)

Gets Payment by Payment Transaction ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentApi apiInstance = new PaymentApi(defaultClient);
    Long id = 56L; // Long | Invoice Transaction ID Number
    try {
      Payment result = apiInstance.paymentGetByID(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentApi#paymentGetByID");
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
| **id** | **Long**| Invoice Transaction ID Number | |

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="paymentPost"></a>
# **paymentPost**
> Payment paymentPost(model)

Create new Payment and optionally assign payment allocations to Invoices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentApi apiInstance = new PaymentApi(defaultClient);
    NewPayment model = new NewPayment(); // NewPayment | 
    try {
      Payment result = apiInstance.paymentPost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentApi#paymentPost");
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
| **model** | [**NewPayment**](NewPayment.md)|  | |

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

