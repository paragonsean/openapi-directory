# InvoicesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelInvoice**](InvoicesApi.md#cancelInvoice) | **DELETE** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId} | Cancel Invoice |
| [**changeInvoice**](InvoicesApi.md#changeInvoice) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId} | Change Invoice |
| [**markaninvoiceasPaid**](InvoicesApi.md#markaninvoiceasPaid) | **POST** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId}/payments | Mark an invoice as Paid |
| [**postponeaninvoice**](InvoicesApi.md#postponeaninvoice) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId}/postponement | Postpone an invoice |
| [**retrieveInvoicebyId**](InvoicesApi.md#retrieveInvoicebyId) | **GET** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId} | Retrieve Invoice by Id |
| [**searchallinvoices**](InvoicesApi.md#searchallinvoices) | **GET** /api/creditcontrol/invoices | Search all invoices |
| [**searchallinvoicesofaAccount**](InvoicesApi.md#searchallinvoicesofaAccount) | **GET** /api/creditcontrol/accounts/{creditAccountId}/invoices | Retrieve invoice by creditAccountId |


<a id="cancelInvoice"></a>
# **cancelInvoice**
> Object cancelInvoice(contentType, accept, creditAccountId, invoiceId)

Cancel Invoice

Changes invoice&#39;s status from ancells invoice by specified Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String invoiceId = "insert identifier here"; // String | 
    try {
      Object result = apiInstance.cancelInvoice(contentType, accept, creditAccountId, invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#cancelInvoice");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **invoiceId** | **String**|  | [default to insert identifier here] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="changeInvoice"></a>
# **changeInvoice**
> Object changeInvoice(creditAccountId, invoiceId, accept, contentType, changeInvoiceRequest1, friendlyId)

Change Invoice

Updates invoice&#39;s attributes &#x60;status&#x60;, &#x60;paymentLink&#x60; and &#x60;observation&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String invoiceId = "insert identifier here"; // String | 
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    ChangeInvoiceRequest1 changeInvoiceRequest1 = new ChangeInvoiceRequest1(); // ChangeInvoiceRequest1 | 
    String friendlyId = "insert identifier here"; // String | Invoice's identification
    try {
      Object result = apiInstance.changeInvoice(creditAccountId, invoiceId, accept, contentType, changeInvoiceRequest1, friendlyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#changeInvoice");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **invoiceId** | **String**|  | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **changeInvoiceRequest1** | [**ChangeInvoiceRequest1**](ChangeInvoiceRequest1.md)|  | |
| **friendlyId** | **String**| Invoice&#39;s identification | [optional] [default to insert identifier here] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="markaninvoiceasPaid"></a>
# **markaninvoiceasPaid**
> String markaninvoiceasPaid(creditAccountId, invoiceId, accept, contentType, markaninvoiceasPaidRequest1)

Mark an invoice as Paid

Pay an invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String creditAccountId = "isert indentifier here"; // String | Credit account's identification
    String invoiceId = "insert identifier here"; // String | 
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    MarkaninvoiceasPaidRequest1 markaninvoiceasPaidRequest1 = new MarkaninvoiceasPaidRequest1(); // MarkaninvoiceasPaidRequest1 | 
    try {
      String result = apiInstance.markaninvoiceasPaid(creditAccountId, invoiceId, accept, contentType, markaninvoiceasPaidRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#markaninvoiceasPaid");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to isert indentifier here] |
| **invoiceId** | **String**|  | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **markaninvoiceasPaidRequest1** | [**MarkaninvoiceasPaidRequest1**](MarkaninvoiceasPaidRequest1.md)|  | |

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="postponeaninvoice"></a>
# **postponeaninvoice**
> Object postponeaninvoice(creditAccountId, invoiceId, accept, contentType, postponeaninvoiceRequest1)

Postpone an invoice

Postpone an invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String creditAccountId = "creditAccountId_example"; // String | Credit account's identification
    String invoiceId = "invoiceId_example"; // String | 
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    PostponeaninvoiceRequest1 postponeaninvoiceRequest1 = new PostponeaninvoiceRequest1(); // PostponeaninvoiceRequest1 | 
    try {
      Object result = apiInstance.postponeaninvoice(creditAccountId, invoiceId, accept, contentType, postponeaninvoiceRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#postponeaninvoice");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | |
| **invoiceId** | **String**|  | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **postponeaninvoiceRequest1** | [**PostponeaninvoiceRequest1**](PostponeaninvoiceRequest1.md)|  | |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="retrieveInvoicebyId"></a>
# **retrieveInvoicebyId**
> Retrievedinvoice1 retrieveInvoicebyId(contentType, accept, creditAccountId, invoiceId)

Retrieve Invoice by Id

Returns associated data for the specified Invoice Id, like status  and value, for example.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String invoiceId = "insert identifier here"; // String | 
    try {
      Retrievedinvoice1 result = apiInstance.retrieveInvoicebyId(contentType, accept, creditAccountId, invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#retrieveInvoicebyId");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **invoiceId** | **String**|  | [default to insert identifier here] |

### Return type

[**Retrievedinvoice1**](Retrievedinvoice1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="searchallinvoices"></a>
# **searchallinvoices**
> Paidinvoices1 searchallinvoices(contentType, accept, from, to, createdDateFrom, createdDateTo, value, status, friendlyId, creditAccountId)

Search all invoices

Returns all invoices according to the informed query params in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String from = ""; // String | 
    String to = ""; // String | 
    String createdDateFrom = ""; // String | 
    String createdDateTo = ""; // String | 
    BigDecimal value = new BigDecimal(78); // BigDecimal | Invoice's value. It must be completed with a decimal value.
    String status = "Paid"; // String | Invoice's status. It must be completed with \"Paid\", \"Cancelled\" or \"Open\" value.
    String friendlyId = "insert identifier here"; // String | Invoice's identifier
    String creditAccountId = "B75F0"; // String | Credit account's identifier
    try {
      Paidinvoices1 result = apiInstance.searchallinvoices(contentType, accept, from, to, createdDateFrom, createdDateTo, value, status, friendlyId, creditAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#searchallinvoices");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **from** | **String**|  | [optional] [default to ] |
| **to** | **String**|  | [optional] [default to ] |
| **createdDateFrom** | **String**|  | [optional] |
| **createdDateTo** | **String**|  | [optional] |
| **value** | **BigDecimal**| Invoice&#39;s value. It must be completed with a decimal value. | [optional] |
| **status** | **String**| Invoice&#39;s status. It must be completed with \&quot;Paid\&quot;, \&quot;Cancelled\&quot; or \&quot;Open\&quot; value. | [optional] [default to Paid] |
| **friendlyId** | **String**| Invoice&#39;s identifier | [optional] [default to insert identifier here] |
| **creditAccountId** | **String**| Credit account&#39;s identifier | [optional] [default to B75F0] |

### Return type

[**Paidinvoices1**](Paidinvoices1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="searchallinvoicesofaAccount"></a>
# **searchallinvoicesofaAccount**
> Getinvoicesfromacheckingaccount1 searchallinvoicesofaAccount(contentType, accept, creditAccountId)

Retrieve invoice by creditAccountId

Returns associated invoices by specified creditAccountId, the param that identifies a client in VTEX&#39;s system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String creditAccountId = "insert identifier here"; // String | 
    try {
      Getinvoicesfromacheckingaccount1 result = apiInstance.searchallinvoicesofaAccount(contentType, accept, creditAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#searchallinvoicesofaAccount");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **creditAccountId** | **String**|  | [default to insert identifier here] |

### Return type

[**Getinvoicesfromacheckingaccount1**](Getinvoicesfromacheckingaccount1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

