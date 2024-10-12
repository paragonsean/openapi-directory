# NaviPlanApi.PasswordApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**passwordHasUserSetPassword**](PasswordApi.md#passwordHasUserSetPassword) | **POST** /api/Password/HasUserSetPassword | Determines if the currently logged in user has set their own password
[**passwordPasswordRequirements**](PasswordApi.md#passwordPasswordRequirements) | **GET** /api/Password/PasswordRequirements | Gets the password complexity requirements
[**passwordResetByModel**](PasswordApi.md#passwordResetByModel) | **POST** /api/Password/Reset | Resets the password for the supplied user name
[**passwordSetByModel**](PasswordApi.md#passwordSetByModel) | **POST** /api/Password/Set | Sets the password for the currently logged in user



## passwordHasUserSetPassword

> passwordHasUserSetPassword()

Determines if the currently logged in user has set their own password

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.PasswordApi();
apiInstance.passwordHasUserSetPassword((error, data, response) => {
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


## passwordPasswordRequirements

> passwordPasswordRequirements()

Gets the password complexity requirements

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.PasswordApi();
apiInstance.passwordPasswordRequirements((error, data, response) => {
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


## passwordResetByModel

> passwordResetByModel(model)

Resets the password for the supplied user name

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.PasswordApi();
let model = new NaviPlanApi.ResetPasswordModel(); // ResetPasswordModel | 
apiInstance.passwordResetByModel(model, (error, data, response) => {
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
 **model** | [**ResetPasswordModel**](ResetPasswordModel.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## passwordSetByModel

> passwordSetByModel(model)

Sets the password for the currently logged in user

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.PasswordApi();
let model = new NaviPlanApi.SetPasswordModel(); // SetPasswordModel | 
apiInstance.passwordSetByModel(model, (error, data, response) => {
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
 **model** | [**SetPasswordModel**](SetPasswordModel.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

