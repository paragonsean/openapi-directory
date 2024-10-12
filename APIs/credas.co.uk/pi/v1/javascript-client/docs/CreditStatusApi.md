# CredasApi.CreditStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkCreditStatus**](CreditStatusApi.md#checkCreditStatus) | **POST** /api/credit-status/perform | Check includes identifying bankruptcy, insolvency, CCJ&#39;s or Company Directorship.



## checkCreditStatus

> CredasApiModelsStatusChecksStatusCheck checkCreditStatus(apikey, opts)

Check includes identifying bankruptcy, insolvency, CCJ&#39;s or Company Directorship.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.CreditStatusApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsStatusChecksStatusCheckRequest': new CredasApi.CredasApiModelsStatusChecksStatusCheckRequest() // CredasApiModelsStatusChecksStatusCheckRequest | Object containing data required to perform the check.
};
apiInstance.checkCreditStatus(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsStatusChecksStatusCheckRequest** | [**CredasApiModelsStatusChecksStatusCheckRequest**](CredasApiModelsStatusChecksStatusCheckRequest.md)| Object containing data required to perform the check. | [optional] 

### Return type

[**CredasApiModelsStatusChecksStatusCheck**](CredasApiModelsStatusChecksStatusCheck.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

