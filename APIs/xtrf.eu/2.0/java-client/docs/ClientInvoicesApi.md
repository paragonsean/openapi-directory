# ClientInvoicesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create1**](ClientInvoicesApi.md#create1) | **POST** /accounting/customers/invoices | Creates a new invoice. |
| [**createPayment**](ClientInvoicesApi.md#createPayment) | **POST** /accounting/customers/invoices/{invoiceId}/payments | Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated. |
| [**delete1**](ClientInvoicesApi.md#delete1) | **DELETE** /accounting/customers/invoices/{invoiceId} | Removes a client invoice. |
| [**delete2**](ClientInvoicesApi.md#delete2) | **DELETE** /accounting/customers/payments/{paymentId} | Removes a customer payment. |
| [**downloadDocuments**](ClientInvoicesApi.md#downloadDocuments) | **POST** /accounting/customers/invoices/documents | Generates client invoices&#39; documents. |
| [**duplicate**](ClientInvoicesApi.md#duplicate) | **POST** /accounting/customers/invoices/{invoiceId}/duplicate | Duplicate client invoice. |
| [**duplicateAsProForma**](ClientInvoicesApi.md#duplicateAsProForma) | **POST** /accounting/customers/invoices/{invoiceId}/duplicate/proForma | Duplicate client invoice as pro forma. |
| [**getAll**](ClientInvoicesApi.md#getAll) | **GET** /accounting/customers/invoices | Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date. |
| [**getAllIds**](ClientInvoicesApi.md#getAllIds) | **GET** /accounting/customers/invoices/ids | Returns client invoices&#39; internal identifiers. |
| [**getById**](ClientInvoicesApi.md#getById) | **GET** /accounting/customers/invoices/{invoiceId} | Returns client invoice details. |
| [**getDates**](ClientInvoicesApi.md#getDates) | **GET** /accounting/customers/invoices/{invoiceId}/dates | Returns dates of a given client invoice. |
| [**getDocument**](ClientInvoicesApi.md#getDocument) | **GET** /accounting/customers/invoices/{invoiceId}/document | Generates client invoice document (PDF). |
| [**getPaymentTerms**](ClientInvoicesApi.md#getPaymentTerms) | **GET** /accounting/customers/invoices/{invoiceId}/paymentTerms | Returns payment terms of a given client invoice. |
| [**getPayments**](ClientInvoicesApi.md#getPayments) | **GET** /accounting/customers/invoices/{invoiceId}/payments | Returns all payments for the client invoice. |
| [**sendReminder**](ClientInvoicesApi.md#sendReminder) | **POST** /accounting/customers/invoices/{invoiceId}/sendReminder | Sends reminder. |
| [**sendReminders**](ClientInvoicesApi.md#sendReminders) | **POST** /accounting/customers/invoices/sendReminders | Sends reminders. Returns number of sent e-mails. |


<a id="create1"></a>
# **create1**
> CustomerInvoiceCreateResultDTO create1(customerInvoiceCreateDTO)

Creates a new invoice.

Creates a new invoice from tasks. Tasks are grouped by client and currency, therefore multiple invoices can be created.If any of the tasks cannot be invoiced (ie. it is already invoiced, not invoiceable, not associated with a project) then an error is reported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    CustomerInvoiceCreateDTO customerInvoiceCreateDTO = new CustomerInvoiceCreateDTO(); // CustomerInvoiceCreateDTO | Created new invoice.
    try {
      CustomerInvoiceCreateResultDTO result = apiInstance.create1(customerInvoiceCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#create1");
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
| **customerInvoiceCreateDTO** | [**CustomerInvoiceCreateDTO**](CustomerInvoiceCreateDTO.md)| Created new invoice. | |

### Return type

[**CustomerInvoiceCreateResultDTO**](CustomerInvoiceCreateResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createPayment"></a>
# **createPayment**
> createPayment(invoiceId, paymentDTO)

Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated.

Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    PaymentDTO paymentDTO = new PaymentDTO(); // PaymentDTO | New payment.
    try {
      apiInstance.createPayment(invoiceId, paymentDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#createPayment");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |
| **paymentDTO** | [**PaymentDTO**](PaymentDTO.md)| New payment. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="delete1"></a>
# **delete1**
> delete1(invoiceId)

Removes a client invoice.

Removes a client invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    try {
      apiInstance.delete1(invoiceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#delete1");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="delete2"></a>
# **delete2**
> delete2(paymentId)

Removes a customer payment.

Removes a customer payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long paymentId = 56L; // Long | customer payment's internal identifier
    try {
      apiInstance.delete2(paymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#delete2");
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
| **paymentId** | **Long**| customer payment&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="downloadDocuments"></a>
# **downloadDocuments**
> UrlResultDTO downloadDocuments(downloadDocumentsRequestDTO)

Generates client invoices&#39; documents.

Generates client invoices&#39; documents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    DownloadDocumentsRequestDTO downloadDocumentsRequestDTO = new DownloadDocumentsRequestDTO(); // DownloadDocumentsRequestDTO | Generated client invoices documents.
    try {
      UrlResultDTO result = apiInstance.downloadDocuments(downloadDocumentsRequestDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#downloadDocuments");
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
| **downloadDocumentsRequestDTO** | [**DownloadDocumentsRequestDTO**](DownloadDocumentsRequestDTO.md)| Generated client invoices documents. | |

### Return type

[**UrlResultDTO**](UrlResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="duplicate"></a>
# **duplicate**
> CustomerInvoiceDTO duplicate(invoiceId)

Duplicate client invoice.

Duplicate client invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    try {
      CustomerInvoiceDTO result = apiInstance.duplicate(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#duplicate");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |

### Return type

[**CustomerInvoiceDTO**](CustomerInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="duplicateAsProForma"></a>
# **duplicateAsProForma**
> CustomerInvoiceDTO duplicateAsProForma(invoiceId)

Duplicate client invoice as pro forma.

Duplicate client invoice as pro forma.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    try {
      CustomerInvoiceDTO result = apiInstance.duplicateAsProForma(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#duplicateAsProForma");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |

### Return type

[**CustomerInvoiceDTO**](CustomerInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getAll"></a>
# **getAll**
> List&lt;CustomerInvoiceDTO&gt; getAll(updatedSince)

Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long updatedSince = 56L; // Long | only client invoices modified since this timestamp
    try {
      List<CustomerInvoiceDTO> result = apiInstance.getAll(updatedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#getAll");
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
| **updatedSince** | **Long**| only client invoices modified since this timestamp | [optional] |

### Return type

[**List&lt;CustomerInvoiceDTO&gt;**](CustomerInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | client invoices |  -  |

<a id="getAllIds"></a>
# **getAllIds**
> List&lt;Integer&gt; getAllIds(updatedSince)

Returns client invoices&#39; internal identifiers.

Returns client invoices&#39; internal identifiers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long updatedSince = 56L; // Long | only client invoices modified since this timestamp
    try {
      List<Integer> result = apiInstance.getAllIds(updatedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#getAllIds");
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
| **updatedSince** | **Long**| only client invoices modified since this timestamp | [optional] |

### Return type

**List&lt;Integer&gt;**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | client invoices&#39; internal identifiers |  -  |

<a id="getById"></a>
# **getById**
> CustomerInvoiceDTO getById(invoiceId, embed)

Returns client invoice details.

Returns client invoice details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    String embed = "embed_example"; // String | list of adittional fields which should be embedded in the response (ie. tasks)
    try {
      CustomerInvoiceDTO result = apiInstance.getById(invoiceId, embed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#getById");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |
| **embed** | **String**| list of adittional fields which should be embedded in the response (ie. tasks) | [optional] |

### Return type

[**CustomerInvoiceDTO**](CustomerInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getDates"></a>
# **getDates**
> CustomerInvoiceDatesDTO getDates(invoiceId)

Returns dates of a given client invoice.

Returns dates of a given client invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    try {
      CustomerInvoiceDatesDTO result = apiInstance.getDates(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#getDates");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |

### Return type

[**CustomerInvoiceDatesDTO**](CustomerInvoiceDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getDocument"></a>
# **getDocument**
> UrlResultDTO getDocument(invoiceId)

Generates client invoice document (PDF).

Generates client invoice document (PDF).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    try {
      UrlResultDTO result = apiInstance.getDocument(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#getDocument");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |

### Return type

[**UrlResultDTO**](UrlResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getPaymentTerms"></a>
# **getPaymentTerms**
> PaymentTermsDTO getPaymentTerms(invoiceId)

Returns payment terms of a given client invoice.

Returns payment terms of a given client invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    try {
      PaymentTermsDTO result = apiInstance.getPaymentTerms(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#getPaymentTerms");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |

### Return type

[**PaymentTermsDTO**](PaymentTermsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getPayments"></a>
# **getPayments**
> List&lt;PaymentDTO&gt; getPayments(invoiceId)

Returns all payments for the client invoice.

Returns all payments for the client invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    try {
      List<PaymentDTO> result = apiInstance.getPayments(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#getPayments");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |

### Return type

[**List&lt;PaymentDTO&gt;**](PaymentDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | client invoice&#39;s payments |  -  |

<a id="sendReminder"></a>
# **sendReminder**
> sendReminder(invoiceId)

Sends reminder.

Sends reminder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | client invoice's internal identifier
    try {
      apiInstance.sendReminder(invoiceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#sendReminder");
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
| **invoiceId** | **Long**| client invoice&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="sendReminders"></a>
# **sendReminders**
> SendRemindersResponseDTO sendReminders(sendRemindersRequestDTO)

Sends reminders. Returns number of sent e-mails.

Sends reminders. Returns number of sent e-mails.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ClientInvoicesApi apiInstance = new ClientInvoicesApi(defaultClient);
    SendRemindersRequestDTO sendRemindersRequestDTO = new SendRemindersRequestDTO(); // SendRemindersRequestDTO | Number of sent e-mails.
    try {
      SendRemindersResponseDTO result = apiInstance.sendReminders(sendRemindersRequestDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInvoicesApi#sendReminders");
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
| **sendRemindersRequestDTO** | [**SendRemindersRequestDTO**](SendRemindersRequestDTO.md)| Number of sent e-mails. | |

### Return type

[**SendRemindersResponseDTO**](SendRemindersResponseDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

