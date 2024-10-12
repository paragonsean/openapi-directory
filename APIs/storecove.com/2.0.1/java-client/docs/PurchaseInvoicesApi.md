# PurchaseInvoicesApi

All URIs are relative to *https://api.storecove.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInvoiceJson**](PurchaseInvoicesApi.md#getInvoiceJson) | **GET** /purchase_invoices/{guid} | Get Purchase invoice data as JSON |
| [**getInvoiceUbl**](PurchaseInvoicesApi.md#getInvoiceUbl) | **GET** /purchase_invoices/{guid}/{packaging} | Get Purchase invoice data in a selectable format |
| [**getInvoiceUblVersioned**](PurchaseInvoicesApi.md#getInvoiceUblVersioned) | **GET** /purchase_invoices/{guid}/{packaging}/{package_version} | Get Purchase invoice data as JSON with a Base64-encoded UBL string in the specified version |


<a id="getInvoiceJson"></a>
# **getInvoiceJson**
> PurchaseInvoice getInvoiceJson(guid, pmv)

Get Purchase invoice data as JSON

Get a specific PurchaseInvoice, in JSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchaseInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PurchaseInvoicesApi apiInstance = new PurchaseInvoicesApi(defaultClient);
    UUID guid = UUID.randomUUID(); // UUID | The guid of the purchase invoice, from the webhook.
    String pmv = "1.0"; // String | The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower 'g' in 'bankgiro'). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean.
    try {
      PurchaseInvoice result = apiInstance.getInvoiceJson(guid, pmv);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchaseInvoicesApi#getInvoiceJson");
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
| **guid** | **UUID**| The guid of the purchase invoice, from the webhook. | |
| **pmv** | **String**| The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower &#39;g&#39; in &#39;bankgiro&#39;). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean. | [optional] [default to 1.0] |

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getInvoiceUbl"></a>
# **getInvoiceUbl**
> PurchaseInvoiceUbl getInvoiceUbl(guid, packaging, pmv)

Get Purchase invoice data in a selectable format

Get a specific PurchaseInvoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchaseInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PurchaseInvoicesApi apiInstance = new PurchaseInvoicesApi(defaultClient);
    UUID guid = UUID.randomUUID(); // UUID | purchase invoice guid
    String packaging = "json"; // String | How to package the purchase invoice.
    String pmv = "1.0"; // String | The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower 'g' in 'bankgiro'). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean.
    try {
      PurchaseInvoiceUbl result = apiInstance.getInvoiceUbl(guid, packaging, pmv);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchaseInvoicesApi#getInvoiceUbl");
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
| **guid** | **UUID**| purchase invoice guid | |
| **packaging** | **String**| How to package the purchase invoice. | [default to json] [enum: json, ubl, original] |
| **pmv** | **String**| The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower &#39;g&#39; in &#39;bankgiro&#39;). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean. | [optional] [default to 1.0] |

### Return type

[**PurchaseInvoiceUbl**](PurchaseInvoiceUbl.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getInvoiceUblVersioned"></a>
# **getInvoiceUblVersioned**
> PurchaseInvoiceUbl getInvoiceUblVersioned(guid, packaging, packageVersion)

Get Purchase invoice data as JSON with a Base64-encoded UBL string in the specified version

Get a specific PurchaseInvoice in UBL format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchaseInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PurchaseInvoicesApi apiInstance = new PurchaseInvoicesApi(defaultClient);
    UUID guid = UUID.randomUUID(); // UUID | purchase invoice guid
    String packaging = "ubl"; // String | How to package the purchase invoice.
    String packageVersion = "si11"; // String | The version of the package.
    try {
      PurchaseInvoiceUbl result = apiInstance.getInvoiceUblVersioned(guid, packaging, packageVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchaseInvoicesApi#getInvoiceUblVersioned");
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
| **guid** | **UUID**| purchase invoice guid | |
| **packaging** | **String**| How to package the purchase invoice. | [default to ubl] [enum: ubl] |
| **packageVersion** | **String**| The version of the package. | [default to si11] [enum: si11, si12, si20, aunz, sg, jp, en16931, original] |

### Return type

[**PurchaseInvoiceUbl**](PurchaseInvoiceUbl.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

