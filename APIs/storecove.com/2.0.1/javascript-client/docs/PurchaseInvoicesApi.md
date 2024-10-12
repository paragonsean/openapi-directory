# StorecoveApi.PurchaseInvoicesApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInvoiceJson**](PurchaseInvoicesApi.md#getInvoiceJson) | **GET** /purchase_invoices/{guid} | Get Purchase invoice data as JSON
[**getInvoiceUbl**](PurchaseInvoicesApi.md#getInvoiceUbl) | **GET** /purchase_invoices/{guid}/{packaging} | Get Purchase invoice data in a selectable format
[**getInvoiceUblVersioned**](PurchaseInvoicesApi.md#getInvoiceUblVersioned) | **GET** /purchase_invoices/{guid}/{packaging}/{package_version} | Get Purchase invoice data as JSON with a Base64-encoded UBL string in the specified version



## getInvoiceJson

> PurchaseInvoice getInvoiceJson(guid, opts)

Get Purchase invoice data as JSON

Get a specific PurchaseInvoice, in JSON format.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.PurchaseInvoicesApi();
let guid = "guid_example"; // String | The guid of the purchase invoice, from the webhook.
let opts = {
  'pmv': "'1.0'" // String | The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower 'g' in 'bankgiro'). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean.
};
apiInstance.getInvoiceJson(guid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| The guid of the purchase invoice, from the webhook. | 
 **pmv** | **String**| The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower &#39;g&#39; in &#39;bankgiro&#39;). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean. | [optional] [default to &#39;1.0&#39;]

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceUbl

> PurchaseInvoiceUbl getInvoiceUbl(guid, packaging, opts)

Get Purchase invoice data in a selectable format

Get a specific PurchaseInvoice.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.PurchaseInvoicesApi();
let guid = "guid_example"; // String | purchase invoice guid
let packaging = "'json'"; // String | How to package the purchase invoice.
let opts = {
  'pmv': "'1.0'" // String | The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower 'g' in 'bankgiro'). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean.
};
apiInstance.getInvoiceUbl(guid, packaging, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| purchase invoice guid | 
 **packaging** | **String**| How to package the purchase invoice. | [default to &#39;json&#39;]
 **pmv** | **String**| The PaymentMeans version. The default (and deprecated) version 1.0 will give BankPaymentMean, DirectDebitPaymentMean, CardPaymentMean, NppPaymentMean, SeBankGiroPaymentMean, SePlusGiroPaymentMean, SgCardPaymentMean, SgGiroPaymentMean, SgPaynowPaymentMean.  Version 2.0 deprecates BankPaymentMean (now CreditTransferPaymentMean), CardPaymentMean (now CreditCardPaymentMean), NppPaymentMean (now AunzNppPayidPaymentMean), SeBankGiroPaymentMean (now SeBankgiroPaymentMean  -- note the lower &#39;g&#39; in &#39;bankgiro&#39;). It also adds OnlinePaymentServicePaymentMean, StandingAgreementPaymentMean, AunzNppPaytoPaymentMean, AunzBpayPaymentMean, AunzPostbillpayPaymentMean, AunzUriPaymentMean. | [optional] [default to &#39;1.0&#39;]

### Return type

[**PurchaseInvoiceUbl**](PurchaseInvoiceUbl.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceUblVersioned

> PurchaseInvoiceUbl getInvoiceUblVersioned(guid, packaging, packageVersion)

Get Purchase invoice data as JSON with a Base64-encoded UBL string in the specified version

Get a specific PurchaseInvoice in UBL format

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.PurchaseInvoicesApi();
let guid = "guid_example"; // String | purchase invoice guid
let packaging = "'ubl'"; // String | How to package the purchase invoice.
let packageVersion = "'si11'"; // String | The version of the package.
apiInstance.getInvoiceUblVersioned(guid, packaging, packageVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| purchase invoice guid | 
 **packaging** | **String**| How to package the purchase invoice. | [default to &#39;ubl&#39;]
 **packageVersion** | **String**| The version of the package. | [default to &#39;si11&#39;]

### Return type

[**PurchaseInvoiceUbl**](PurchaseInvoiceUbl.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

