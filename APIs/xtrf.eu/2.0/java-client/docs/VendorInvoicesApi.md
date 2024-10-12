# VendorInvoicesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create4**](VendorInvoicesApi.md#create4) | **POST** /accounting/providers/invoices | Creates a new invoice. |
| [**createPayment1**](VendorInvoicesApi.md#createPayment1) | **POST** /accounting/providers/invoices/{invoiceId}/payments | Creates a new payment on the vendor account and assigns the payment to the invoice. |
| [**delete6**](VendorInvoicesApi.md#delete6) | **DELETE** /accounting/providers/invoices/{invoiceId} | Removes a provider invoice. |
| [**delete7**](VendorInvoicesApi.md#delete7) | **DELETE** /accounting/providers/payments/{paymentId} | Removes a provider payment. |
| [**getAll2**](VendorInvoicesApi.md#getAll2) | **GET** /accounting/providers/invoices | Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date. |
| [**getAllIds3**](VendorInvoicesApi.md#getAllIds3) | **GET** /accounting/providers/invoices/ids | Returns vendor invoices&#39; internal identifiers. |
| [**getById3**](VendorInvoicesApi.md#getById3) | **GET** /accounting/providers/invoices/{invoiceId} | Returns provider invoice details. |
| [**getDocument1**](VendorInvoicesApi.md#getDocument1) | **GET** /accounting/providers/invoices/{invoiceId}/document | Generates provider invoice document (PDF). |
| [**getPayments1**](VendorInvoicesApi.md#getPayments1) | **GET** /accounting/providers/invoices/{invoiceId}/payments | Returns all payments for the vendor invoice. |
| [**send**](VendorInvoicesApi.md#send) | **POST** /accounting/providers/invoices/{invoiceId}/send | Sends a provider invoice. |
| [**setStatus**](VendorInvoicesApi.md#setStatus) | **POST** /accounting/providers/invoices/{invoiceId}/status | Changes invoice status to given status. |


<a id="create4"></a>
# **create4**
> ProviderInvoiceCreateResultDTO create4(providerInvoiceCreateDTO)

Creates a new invoice.

Creates a new invoice from jobs. Jobs are grouped by provider and currency, therefore multiple invoices can be created.If any of the jobs cannot be invoiced (ie. it is already invoiced) then an error is reported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    ProviderInvoiceCreateDTO providerInvoiceCreateDTO = new ProviderInvoiceCreateDTO(); // ProviderInvoiceCreateDTO | Created new invoice.
    try {
      ProviderInvoiceCreateResultDTO result = apiInstance.create4(providerInvoiceCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#create4");
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
| **providerInvoiceCreateDTO** | [**ProviderInvoiceCreateDTO**](ProviderInvoiceCreateDTO.md)| Created new invoice. | |

### Return type

[**ProviderInvoiceCreateResultDTO**](ProviderInvoiceCreateResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createPayment1"></a>
# **createPayment1**
> createPayment1(invoiceId, paymentDTO)

Creates a new payment on the vendor account and assigns the payment to the invoice.

Creates a new payment on the vendor account and assigns the payment to the invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | vendor invoice's internal identifier
    PaymentDTO paymentDTO = new PaymentDTO(); // PaymentDTO | New payment.
    try {
      apiInstance.createPayment1(invoiceId, paymentDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#createPayment1");
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
| **invoiceId** | **Long**| vendor invoice&#39;s internal identifier | |
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

<a id="delete6"></a>
# **delete6**
> delete6(invoiceId)

Removes a provider invoice.

Removes a provider invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | provider invoice's internal identifier
    try {
      apiInstance.delete6(invoiceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#delete6");
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
| **invoiceId** | **Long**| provider invoice&#39;s internal identifier | |

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

<a id="delete7"></a>
# **delete7**
> delete7(paymentId)

Removes a provider payment.

Removes a provider payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long paymentId = 56L; // Long | provider payment's internal identifier
    try {
      apiInstance.delete7(paymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#delete7");
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
| **paymentId** | **Long**| provider payment&#39;s internal identifier | |

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

<a id="getAll2"></a>
# **getAll2**
> List&lt;ProviderInvoiceDTO&gt; getAll2(updatedSince)

Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long updatedSince = 56L; // Long | only vendor invoices modified since this timestamp
    try {
      List<ProviderInvoiceDTO> result = apiInstance.getAll2(updatedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#getAll2");
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
| **updatedSince** | **Long**| only vendor invoices modified since this timestamp | [optional] |

### Return type

[**List&lt;ProviderInvoiceDTO&gt;**](ProviderInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | vendor invoices |  -  |

<a id="getAllIds3"></a>
# **getAllIds3**
> List&lt;Integer&gt; getAllIds3(updatedSince)

Returns vendor invoices&#39; internal identifiers.

Returns vendor invoices&#39; internal identifiers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long updatedSince = 56L; // Long | only vendor invoices modified since this timestamp
    try {
      List<Integer> result = apiInstance.getAllIds3(updatedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#getAllIds3");
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
| **updatedSince** | **Long**| only vendor invoices modified since this timestamp | [optional] |

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
| **0** | vendor invoices&#39; internal identifiers |  -  |

<a id="getById3"></a>
# **getById3**
> ProviderInvoiceDTO getById3(invoiceId)

Returns provider invoice details.

Returns provider invoice details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | provider invoice's internal identifier
    try {
      ProviderInvoiceDTO result = apiInstance.getById3(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#getById3");
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
| **invoiceId** | **Long**| provider invoice&#39;s internal identifier | |

### Return type

[**ProviderInvoiceDTO**](ProviderInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getDocument1"></a>
# **getDocument1**
> UrlResultDTO getDocument1(invoiceId)

Generates provider invoice document (PDF).

Generates provider invoice document (PDF).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | provider invoice's internal identifier
    try {
      UrlResultDTO result = apiInstance.getDocument1(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#getDocument1");
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
| **invoiceId** | **Long**| provider invoice&#39;s internal identifier | |

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

<a id="getPayments1"></a>
# **getPayments1**
> List&lt;PaymentDTO&gt; getPayments1(invoiceId)

Returns all payments for the vendor invoice.

Returns all payments for the vendor invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | vendor invoice's internal identifier
    try {
      List<PaymentDTO> result = apiInstance.getPayments1(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#getPayments1");
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
| **invoiceId** | **Long**| vendor invoice&#39;s internal identifier | |

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
| **0** | vendor invoice&#39;s payments |  -  |

<a id="send"></a>
# **send**
> send(invoiceId)

Sends a provider invoice.

Sends a provider invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | provider invoice's internal identifier
    try {
      apiInstance.send(invoiceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#send");
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
| **invoiceId** | **Long**| provider invoice&#39;s internal identifier | |

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

<a id="setStatus"></a>
# **setStatus**
> setStatus(invoiceId, statusRequestDTO)

Changes invoice status to given status.

Changes invoice status to given status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    VendorInvoicesApi apiInstance = new VendorInvoicesApi(defaultClient);
    Long invoiceId = 56L; // Long | provider invoice's internal identifier
    StatusRequestDTO statusRequestDTO = new StatusRequestDTO(); // StatusRequestDTO | Changed invoice status to given status.
    try {
      apiInstance.setStatus(invoiceId, statusRequestDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorInvoicesApi#setStatus");
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
| **invoiceId** | **Long**| provider invoice&#39;s internal identifier | |
| **statusRequestDTO** | [**StatusRequestDTO**](StatusRequestDTO.md)| Changed invoice status to given status. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

