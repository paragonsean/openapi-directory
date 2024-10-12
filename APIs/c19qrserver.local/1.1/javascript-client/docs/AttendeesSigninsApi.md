# ApiForTheCovid19TrackingQrCodeSigninServer.AttendeesSigninsApi

All URIs are relative to *http://c19qrserver.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signinPost**](AttendeesSigninsApi.md#signinPost) | **POST** /signin | 
[**signinSigninIdDelete**](AttendeesSigninsApi.md#signinSigninIdDelete) | **DELETE** /signin/{signinId} | Delete a signin record
[**signinSigninIdGet**](AttendeesSigninsApi.md#signinSigninIdGet) | **GET** /signin/{signinId} | Retrieve the information associated with a signin record
[**signinSigninIdPut**](AttendeesSigninsApi.md#signinSigninIdPut) | **PUT** /signin/{signinId} | Update a signin record
[**signinsGet**](AttendeesSigninsApi.md#signinsGet) | **GET** /signins | Get signin info



## signinPost

> SigninResponse signinPost(opts)



Create a new signin record

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.AttendeesSigninsApi();
let opts = {
  'signin': new ApiForTheCovid19TrackingQrCodeSigninServer.Signin() // Signin | 
};
apiInstance.signinPost(opts, (error, data, response) => {
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
 **signin** | [**Signin**](Signin.md)|  | [optional] 

### Return type

[**SigninResponse**](SigninResponse.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signinSigninIdDelete

> signinSigninIdDelete(signinId)

Delete a signin record

Delete a signin record       

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.AttendeesSigninsApi();
let signinId = 1; // Number | The ID of the signin record to be deleted.
apiInstance.signinSigninIdDelete(signinId, (error, data, response) => {
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
 **signinId** | **Number**| The ID of the signin record to be deleted. | 

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signinSigninIdGet

> Signin signinSigninIdGet(signinId)

Retrieve the information associated with a signin record

Retrieve the information associated with a signin record 

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.AttendeesSigninsApi();
let signinId = 1; // Number | The ID of the signin record to be retrieved.
apiInstance.signinSigninIdGet(signinId, (error, data, response) => {
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
 **signinId** | **Number**| The ID of the signin record to be retrieved. | 

### Return type

[**Signin**](Signin.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signinSigninIdPut

> UserRecord signinSigninIdPut(signinId, opts)

Update a signin record

Update a signin record 

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.AttendeesSigninsApi();
let signinId = 1; // Number | The ID of the signin record to be retrieved.
let opts = {
  'signin': new ApiForTheCovid19TrackingQrCodeSigninServer.Signin() // Signin | 
};
apiInstance.signinSigninIdPut(signinId, opts, (error, data, response) => {
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
 **signinId** | **Number**| The ID of the signin record to be retrieved. | 
 **signin** | [**Signin**](Signin.md)|  | [optional] 

### Return type

[**UserRecord**](UserRecord.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signinsGet

> [Signin] signinsGet(opts)

Get signin info

Returns a list of signin objects sorted by signin ID descending.

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.AttendeesSigninsApi();
let opts = {
  'lessThan': 56, // Number | Return signins with IDs less than this value.
  'returnCount': 100 // Number | Return this many objects
};
apiInstance.signinsGet(opts, (error, data, response) => {
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
 **lessThan** | **Number**| Return signins with IDs less than this value. | [optional] 
 **returnCount** | **Number**| Return this many objects | [optional] [default to 100]

### Return type

[**[Signin]**](Signin.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

