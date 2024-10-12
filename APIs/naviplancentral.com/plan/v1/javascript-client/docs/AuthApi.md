# NaviPlanApi.AuthApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authLoginByModel**](AuthApi.md#authLoginByModel) | **POST** /api/auth/Login | Start a session with the DomainProviders user store
[**authLogout**](AuthApi.md#authLogout) | **POST** /api/auth/Logout | 
[**authPasswordRequirements**](AuthApi.md#authPasswordRequirements) | **GET** /api/auth/LoginConfiguration | Gets the login rules
[**authResumeSession**](AuthApi.md#authResumeSession) | **POST** /api/auth/ResumeSession | Validate and extend the duration of a session



## authLoginByModel

> PublicSessionInfoModel authLoginByModel(model)

Start a session with the DomainProviders user store

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.AuthApi();
let model = new NaviPlanApi.LoginModel(); // LoginModel | DomainProvider username and password
apiInstance.authLoginByModel(model, (error, data, response) => {
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
 **model** | [**LoginModel**](LoginModel.md)| DomainProvider username and password | 

### Return type

[**PublicSessionInfoModel**](PublicSessionInfoModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## authLogout

> authLogout()



### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.AuthApi();
apiInstance.authLogout((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## authPasswordRequirements

> authPasswordRequirements()

Gets the login rules

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.AuthApi();
apiInstance.authPasswordRequirements((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## authResumeSession

> PublicSessionInfoModel authResumeSession()

Validate and extend the duration of a session

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.AuthApi();
apiInstance.authResumeSession((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicSessionInfoModel**](PublicSessionInfoModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

