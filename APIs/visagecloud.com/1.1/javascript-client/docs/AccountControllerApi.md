# VisageCloud.AccountControllerApi

All URIs are relative to *https://visagecloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changePasswordUsingPOST**](AccountControllerApi.md#changePasswordUsingPOST) | **POST** /rest/v1.1/account/changePassword | Change password for an account using old password
[**getAccountByAccessKeyUsingGET**](AccountControllerApi.md#getAccountByAccessKeyUsingGET) | **GET** /rest/v1.1/account/account | Get account information by accessKey and secretKey
[**getBillingPerAccountUsingGET**](AccountControllerApi.md#getBillingPerAccountUsingGET) | **GET** /rest/v1.1/account/billing | Get billing information by accessKey and secretKey
[**loginWithEmailUsingPOST**](AccountControllerApi.md#loginWithEmailUsingPOST) | **POST** /rest/v1.1/account/login | Get account information including accessKey and secretKey by email and password



## changePasswordUsingPOST

> RestResponse changePasswordUsingPOST(email, oldPassword, newPassword)

Change password for an account using old password

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AccountControllerApi();
let email = "email_example"; // String | email
let oldPassword = "oldPassword_example"; // String | oldPassword
let newPassword = "newPassword_example"; // String | newPassword
apiInstance.changePasswordUsingPOST(email, oldPassword, newPassword, (error, data, response) => {
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
 **email** | **String**| email | 
 **oldPassword** | **String**| oldPassword | 
 **newPassword** | **String**| newPassword | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAccountByAccessKeyUsingGET

> RestResponse getAccountByAccessKeyUsingGET(accessKey, secretKey)

Get account information by accessKey and secretKey

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AccountControllerApi();
let accessKey = "accessKey_example"; // String | accessKey
let secretKey = "secretKey_example"; // String | secretKey
apiInstance.getAccountByAccessKeyUsingGET(accessKey, secretKey, (error, data, response) => {
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
 **accessKey** | **String**| accessKey | 
 **secretKey** | **String**| secretKey | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getBillingPerAccountUsingGET

> RestResponse getBillingPerAccountUsingGET(accessKey, secretKey, opts)

Get billing information by accessKey and secretKey

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AccountControllerApi();
let accessKey = "accessKey_example"; // String | accessKey
let secretKey = "secretKey_example"; // String | secretKey
let opts = {
  'startDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | startDateTime
  'endDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | endDateTime
  'dateTemplate': "dateTemplate_example" // String | dateTemplate
};
apiInstance.getBillingPerAccountUsingGET(accessKey, secretKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| accessKey | 
 **secretKey** | **String**| secretKey | 
 **startDateTime** | **Date**| startDateTime | [optional] 
 **endDateTime** | **Date**| endDateTime | [optional] 
 **dateTemplate** | **String**| dateTemplate | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## loginWithEmailUsingPOST

> RestResponse loginWithEmailUsingPOST(email, password)

Get account information including accessKey and secretKey by email and password

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AccountControllerApi();
let email = "email_example"; // String | email
let password = "password_example"; // String | password
apiInstance.loginWithEmailUsingPOST(email, password, (error, data, response) => {
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
 **email** | **String**| email | 
 **password** | **String**| password | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

