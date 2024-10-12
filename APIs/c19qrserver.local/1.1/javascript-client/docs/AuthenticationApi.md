# ApiForTheCovid19TrackingQrCodeSigninServer.AuthenticationApi

All URIs are relative to *http://c19qrserver.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loginPost**](AuthenticationApi.md#loginPost) | **POST** /login | Log in to get an API token
[**logoutPost**](AuthenticationApi.md#logoutPost) | **POST** /logout | Log out



## loginPost

> LoginResponse loginPost(sample1)

Log in to get an API token

Submit your email and password to get an API token

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.AuthenticationApi();
let sample1 = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample1(); // Sample1 | The login payload
apiInstance.loginPost(sample1, (error, data, response) => {
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
 **sample1** | [**Sample1**](Sample1.md)| The login payload | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## logoutPost

> logoutPost()

Log out

Log out by deleting your token off the server.

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.AuthenticationApi();
apiInstance.logoutPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

