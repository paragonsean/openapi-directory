# EmailApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**emailSendEmailStatement**](EmailApi.md#emailSendEmailStatement) | **POST** /v1/email/sendEmailStatement | Sends a Statement email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address. |
| [**emailSendQuote**](EmailApi.md#emailSendQuote) | **POST** /v1/email/sendQuote | Sends a Quote email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address. |
| [**emailSendSalesInvoice**](EmailApi.md#emailSendSalesInvoice) | **POST** /v1/email/sendSalesInvoice | Sends a Sales Invoice email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Sales Invoice Customer&#39;s address. |


<a id="emailSendEmailStatement"></a>
# **emailSendEmailStatement**
> Object emailSendEmailStatement(emailStatementDto)

Sends a Statement email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    EmailApi apiInstance = new EmailApi(defaultClient);
    EmailStatementDto emailStatementDto = new EmailStatementDto(); // EmailStatementDto | 
    try {
      Object result = apiInstance.emailSendEmailStatement(emailStatementDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#emailSendEmailStatement");
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
| **emailStatementDto** | [**EmailStatementDto**](EmailStatementDto.md)|  | |

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

<a id="emailSendQuote"></a>
# **emailSendQuote**
> Object emailSendQuote(emailQuoteDto)

Sends a Quote email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    EmailApi apiInstance = new EmailApi(defaultClient);
    EmailQuoteDto emailQuoteDto = new EmailQuoteDto(); // EmailQuoteDto | 
    try {
      Object result = apiInstance.emailSendQuote(emailQuoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#emailSendQuote");
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
| **emailQuoteDto** | [**EmailQuoteDto**](EmailQuoteDto.md)|  | |

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

<a id="emailSendSalesInvoice"></a>
# **emailSendSalesInvoice**
> Object emailSendSalesInvoice(salesInvoiceEmailInfoDto)

Sends a Sales Invoice email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Sales Invoice Customer&#39;s address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    EmailApi apiInstance = new EmailApi(defaultClient);
    SalesInvoiceEmailInfoDto salesInvoiceEmailInfoDto = new SalesInvoiceEmailInfoDto(); // SalesInvoiceEmailInfoDto | 
    try {
      Object result = apiInstance.emailSendSalesInvoice(salesInvoiceEmailInfoDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#emailSendSalesInvoice");
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
| **salesInvoiceEmailInfoDto** | [**SalesInvoiceEmailInfoDto**](SalesInvoiceEmailInfoDto.md)|  | |

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

