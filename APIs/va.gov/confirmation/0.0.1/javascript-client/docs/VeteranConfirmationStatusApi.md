# VeteranConfirmation.VeteranConfirmationStatusApi

All URIs are relative to *https://sandbox-api.va.gov/services/veteran_confirmation/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVeteranStatus**](VeteranConfirmationStatusApi.md#getVeteranStatus) | **POST** /status | Get confirmation about an individual&#39;s Veteran status according to the VA



## getVeteranStatus

> VeteranStatusConfirmation getVeteranStatus(veteranStatusRequest)

Get confirmation about an individual&#39;s Veteran status according to the VA

### Example

```javascript
import VeteranConfirmation from 'veteran_confirmation';
let defaultClient = VeteranConfirmation.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VeteranConfirmation.VeteranConfirmationStatusApi();
let veteranStatusRequest = new VeteranConfirmation.VeteranStatusRequest(); // VeteranStatusRequest | 
apiInstance.getVeteranStatus(veteranStatusRequest, (error, data, response) => {
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
 **veteranStatusRequest** | [**VeteranStatusRequest**](VeteranStatusRequest.md)|  | 

### Return type

[**VeteranStatusConfirmation**](VeteranStatusConfirmation.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

