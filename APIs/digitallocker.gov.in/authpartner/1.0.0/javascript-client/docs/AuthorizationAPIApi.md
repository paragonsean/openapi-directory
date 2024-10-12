# AuthorizedPartnerApiSpecification.AuthorizationAPIApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceCodeId**](AuthorizationAPIApi.md#getDeviceCodeId) | **POST** /oauth2/1/code | Get Device Code



## getDeviceCodeId

> DeviceAuthorizationCodeResponse getDeviceCodeId(opts)

Get Device Code

The client device calls the DigiLocker API to get the device code by providing the client_id issued to the device OEM and either the username or the mobile number of the user. DigiLocker responds with a device code and then sends an OTP on the mobile number and email address associated with the user’s account. The masked mobile number and email address is also sent in response. The device should use these values to notify the users about the mobile and email address on which the OTP has been sent.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.AuthorizationAPIApi();
let opts = {
  'deviceAuthorizationCode': new AuthorizedPartnerApiSpecification.DeviceAuthorizationCode() // DeviceAuthorizationCode | 
};
apiInstance.getDeviceCodeId(opts, (error, data, response) => {
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
 **deviceAuthorizationCode** | [**DeviceAuthorizationCode**](DeviceAuthorizationCode.md)|  | [optional] 

### Return type

[**DeviceAuthorizationCodeResponse**](DeviceAuthorizationCodeResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

