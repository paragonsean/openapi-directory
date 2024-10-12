# TwilioMicrovisor.MicrovisorV1AppManifestApi

All URIs are relative to *https://microvisor.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAppManifest**](MicrovisorV1AppManifestApi.md#fetchAppManifest) | **GET** /v1/Apps/{AppSid}/Manifest | 



## fetchAppManifest

> MicrovisorV1AppAppManifest fetchAppManifest(appSid)



Retrieve the Manifest for an App.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AppManifestApi();
let appSid = "appSid_example"; // String | A 34-character string that uniquely identifies this App.
apiInstance.fetchAppManifest(appSid, (error, data, response) => {
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
 **appSid** | **String**| A 34-character string that uniquely identifies this App. | 

### Return type

[**MicrovisorV1AppAppManifest**](MicrovisorV1AppAppManifest.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

