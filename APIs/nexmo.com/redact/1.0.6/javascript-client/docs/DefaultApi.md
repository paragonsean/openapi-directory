# RedactApi.DefaultApi

All URIs are relative to *https://api.nexmo.com/v1/redact*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redactMessage**](DefaultApi.md#redactMessage) | **POST** /transaction | Redact a specific message



## redactMessage

> redactMessage(redactTransaction)

Redact a specific message



### Example

```javascript
import RedactApi from 'redact_api';
let defaultClient = RedactApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new RedactApi.DefaultApi();
let redactTransaction = new RedactApi.RedactTransaction(); // RedactTransaction | 
apiInstance.redactMessage(redactTransaction, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redactTransaction** | [**RedactTransaction**](RedactTransaction.md)|  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

