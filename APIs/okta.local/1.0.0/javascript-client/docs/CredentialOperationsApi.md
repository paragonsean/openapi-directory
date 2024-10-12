# UsersOktaApi.CredentialOperationsApi

All URIs are relative to *http://okta.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changePassword**](CredentialOperationsApi.md#changePassword) | **POST** /api/v1/users/{userId}/credentials/change_password | Change Password
[**changeRecoveryQuestion**](CredentialOperationsApi.md#changeRecoveryQuestion) | **POST** /api/v1/users/{userId}/credentials/change_recovery_question | Change Recovery Question
[**forgotPasswordOneTimeCode**](CredentialOperationsApi.md#forgotPasswordOneTimeCode) | **POST** /api/v1/users/{userId}/credentials/forgot_password | Forgot Password (One Time Code)
[**setRecoveryCredential**](CredentialOperationsApi.md#setRecoveryCredential) | **PUT** /api/v1/users/{userId} | Set Recovery Credential



## changePassword

> changePassword(userId, opts)

Change Password

Change Password

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.CredentialOperationsApi();
let userId = "userId_example"; // String | 
let opts = {
  'changePasswordRequest': {"newPassword":{"value":"uTVM,TPw55"},"oldPassword":{"value":"{{password}}"}} // ChangePasswordRequest | 
};
apiInstance.changePassword(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **changePasswordRequest** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeRecoveryQuestion

> changeRecoveryQuestion(userId, opts)

Change Recovery Question

Change Recovery Question

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.CredentialOperationsApi();
let userId = "userId_example"; // String | 
let opts = {
  'changeRecoveryQuestionRequest': {"password":{"value":"{{password}}"},"recovery_question":{"answer":"My recovery credentials are updated","question":"What happens when I update my question"}} // ChangeRecoveryQuestionRequest | 
};
apiInstance.changeRecoveryQuestion(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **changeRecoveryQuestionRequest** | [**ChangeRecoveryQuestionRequest**](ChangeRecoveryQuestionRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## forgotPasswordOneTimeCode

> forgotPasswordOneTimeCode(userId, opts)

Forgot Password (One Time Code)

Forgot Password (One Time Code)

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.CredentialOperationsApi();
let userId = "userId_example"; // String | 
let opts = {
  'sendEmail': "false" // String | 
};
apiInstance.forgotPasswordOneTimeCode(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **sendEmail** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## setRecoveryCredential

> setRecoveryCredential(userId, opts)

Set Recovery Credential

Set Recovery Credential

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.CredentialOperationsApi();
let userId = "userId_example"; // String | 
let opts = {
  'setRecoveryCredentialRequest': {"credentials":{"recovery_question":{"answer":"Annie Oakley","question":"Who's a major player in the cowboy scene?"}}} // SetRecoveryCredentialRequest | 
};
apiInstance.setRecoveryCredential(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **setRecoveryCredentialRequest** | [**SetRecoveryCredentialRequest**](SetRecoveryCredentialRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

