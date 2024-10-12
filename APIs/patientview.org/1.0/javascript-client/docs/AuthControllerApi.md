# PatientView.AuthControllerApi

All URIs are relative to *https://www.patientview.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBasicUserInformation**](AuthControllerApi.md#getBasicUserInformation) | **GET** /auth/{token}/basicuserinformation | Get Basic User Information
[**logIn**](AuthControllerApi.md#logIn) | **POST** /auth/login | Log In
[**logOut**](AuthControllerApi.md#logOut) | **DELETE** /auth/logout/{token} | Log Out



## getBasicUserInformation

> User getBasicUserInformation(token)

Get Basic User Information

Once logged in and have a token, get basic user information including group role membership

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.AuthControllerApi();
let token = "token_example"; // String | token
apiInstance.getBasicUserInformation(token, (error, data, response) => {
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
 **token** | **String**| token | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## logIn

> UserToken logIn(opts)

Log In

Authenticate using username and password, returns token, which must be added to X-Auth-Token in header of all future requests

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.AuthControllerApi();
let opts = {
  'credentials': new PatientView.Credentials() // Credentials | credentials
};
apiInstance.logIn(opts, (error, data, response) => {
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
 **credentials** | [**Credentials**](Credentials.md)| credentials | [optional] 

### Return type

[**UserToken**](UserToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## logOut

> logOut(token)

Log Out

Log Out

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.AuthControllerApi();
let token = "token_example"; // String | token
apiInstance.logOut(token, (error, data, response) => {
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
 **token** | **String**| token | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

