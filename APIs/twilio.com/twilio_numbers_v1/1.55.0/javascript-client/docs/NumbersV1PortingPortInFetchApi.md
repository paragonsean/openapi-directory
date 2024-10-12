# TwilioNumbers.NumbersV1PortingPortInFetchApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchPortingPortInFetch**](NumbersV1PortingPortInFetchApi.md#fetchPortingPortInFetch) | **GET** /v1/Porting/PortIn/{PortInRequestSid} | 



## fetchPortingPortInFetch

> NumbersV1PortingPortInFetch fetchPortingPortInFetch(portInRequestSid)



Fetch a port in request by SID

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV1PortingPortInFetchApi();
let portInRequestSid = "portInRequestSid_example"; // String | The SID of the Port In request. This is a unique identifier of the port in request.
apiInstance.fetchPortingPortInFetch(portInRequestSid, (error, data, response) => {
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
 **portInRequestSid** | **String**| The SID of the Port In request. This is a unique identifier of the port in request. | 

### Return type

[**NumbersV1PortingPortInFetch**](NumbersV1PortingPortInFetch.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

