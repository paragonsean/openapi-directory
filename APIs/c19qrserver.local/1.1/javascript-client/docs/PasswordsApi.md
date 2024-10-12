# ApiForTheCovid19TrackingQrCodeSigninServer.PasswordsApi

All URIs are relative to *http://c19qrserver.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changePasswordPost**](PasswordsApi.md#changePasswordPost) | **POST** /changePassword | Used for changing your password
[**requestPasswordResetPost**](PasswordsApi.md#requestPasswordResetPost) | **POST** /requestPasswordReset | Used for requesting a password reset code
[**verifyPasswordChangePost**](PasswordsApi.md#verifyPasswordChangePost) | **POST** /verifyPasswordChange | Used for resetting your password when you forgot it



## changePasswordPost

> changePasswordPost(sample)

Used for changing your password

Pass in your old password and your new password

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.PasswordsApi();
let sample = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample(); // Sample | Change Password Payload
apiInstance.changePasswordPost(sample, (error, data, response) => {
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
 **sample** | [**Sample**](Sample.md)| Change Password Payload | 

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## requestPasswordResetPost

> RequestPasswordResetResponse requestPasswordResetPost(sample2)

Used for requesting a password reset code

The admin should run this on behalf of a user who forgot their password.  The API will generate a password reset code which the admin should then provide to the user. The user can use their client to reset their password. Normally the password reset code is mailed to the user, but I didn&#39;t want to do this in this case because I didn&#39;t want to  introduce the complicated dependency of having an SMTP server just for this purpose. Doing it this way makes it easy for people to adopt this  API. 

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.PasswordsApi();
let sample2 = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample2(); // Sample2 | Request Password Reset Payload
apiInstance.requestPasswordResetPost(sample2, (error, data, response) => {
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
 **sample2** | [**Sample2**](Sample2.md)| Request Password Reset Payload | 

### Return type

[**RequestPasswordResetResponse**](RequestPasswordResetResponse.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## verifyPasswordChangePost

> verifyPasswordChangePost(sample4)

Used for resetting your password when you forgot it

Another endpoint will generate a password reset code for you. You should  use the client app to submit the reset code along with the new password to change your password. 

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.PasswordsApi();
let sample4 = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample4(); // Sample4 | Password Reset Payload
apiInstance.verifyPasswordChangePost(sample4, (error, data, response) => {
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
 **sample4** | [**Sample4**](Sample4.md)| Password Reset Payload | 

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

