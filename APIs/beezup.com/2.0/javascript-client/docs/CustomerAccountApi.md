# BeezUpMerchantApi.CustomerAccountApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateUserAccount**](CustomerAccountApi.md#activateUserAccount) | **POST** /v2/user/customer/account/activate | Activate the user account
[**changeEmail**](CustomerAccountApi.md#changeEmail) | **POST** /v2/user/customer/account/changeEmail | Change user email
[**changePassword**](CustomerAccountApi.md#changePassword) | **POST** /v2/user/customer/account/changePassword | Change user password
[**getCreditCardInfo**](CustomerAccountApi.md#getCreditCardInfo) | **GET** /v2/user/customer/account/creditCardInfo | Get credit card information
[**getProfilePictureInfo**](CustomerAccountApi.md#getProfilePictureInfo) | **GET** /v2/user/customer/account/profilePictureInfo | Get profile picture information
[**getUserAccountInfo**](CustomerAccountApi.md#getUserAccountInfo) | **GET** /v2/user/customer/account | Get user account information
[**resendEmailActivation**](CustomerAccountApi.md#resendEmailActivation) | **POST** /v2/user/customer/account/resendEmailActivation | Resend email activation
[**saveCompanyInfo**](CustomerAccountApi.md#saveCompanyInfo) | **PUT** /v2/user/customer/account/companyInfo | Change company information
[**saveCreditCardInfo**](CustomerAccountApi.md#saveCreditCardInfo) | **PUT** /v2/user/customer/account/creditCardInfo | Save user credit card info
[**savePersonalInfo**](CustomerAccountApi.md#savePersonalInfo) | **PUT** /v2/user/customer/account/personalInfo | Save user personal information
[**saveProfilePictureInfo**](CustomerAccountApi.md#saveProfilePictureInfo) | **PUT** /v2/user/customer/account/profilePictureInfo | Change user picture information



## activateUserAccount

> activateUserAccount(body)

Activate the user account

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let body = "body_example"; // String | The email activation id received by email.
apiInstance.activateUserAccount(body, (error, data, response) => {
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
 **body** | **String**| The email activation id received by email. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeEmail

> changeEmail(changeEmailRequest)

Change user email

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let changeEmailRequest = new BeezUpMerchantApi.ChangeEmailRequest(); // ChangeEmailRequest | 
apiInstance.changeEmail(changeEmailRequest, (error, data, response) => {
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
 **changeEmailRequest** | [**ChangeEmailRequest**](ChangeEmailRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changePassword

> changePassword(changePasswordRequest)

Change user password

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let changePasswordRequest = new BeezUpMerchantApi.ChangePasswordRequest(); // ChangePasswordRequest | 
apiInstance.changePassword(changePasswordRequest, (error, data, response) => {
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
 **changePasswordRequest** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCreditCardInfo

> CreditCardInfoResponse getCreditCardInfo(opts)

Get credit card information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getCreditCardInfo(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**CreditCardInfoResponse**](CreditCardInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfilePictureInfo

> ProfilePictureInfoResponse getProfilePictureInfo(opts)

Get profile picture information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getProfilePictureInfo(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**ProfilePictureInfoResponse**](ProfilePictureInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserAccountInfo

> AccountInfo getUserAccountInfo(opts)

Get user account information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getUserAccountInfo(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resendEmailActivation

> resendEmailActivation()

Resend email activation

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
apiInstance.resendEmailActivation((error, data, response) => {
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
- **Accept**: application/json


## saveCompanyInfo

> saveCompanyInfo(companyInfo)

Change company information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let companyInfo = new BeezUpMerchantApi.CompanyInfo(); // CompanyInfo | 
apiInstance.saveCompanyInfo(companyInfo, (error, data, response) => {
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
 **companyInfo** | [**CompanyInfo**](CompanyInfo.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveCreditCardInfo

> saveCreditCardInfo(creditCardInfo)

Save user credit card info

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let creditCardInfo = new BeezUpMerchantApi.CreditCardInfo(); // CreditCardInfo | Credit card info
apiInstance.saveCreditCardInfo(creditCardInfo, (error, data, response) => {
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
 **creditCardInfo** | [**CreditCardInfo**](CreditCardInfo.md)| Credit card info | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## savePersonalInfo

> savePersonalInfo(personalInfo)

Save user personal information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let personalInfo = new BeezUpMerchantApi.PersonalInfo(); // PersonalInfo | 
apiInstance.savePersonalInfo(personalInfo, (error, data, response) => {
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
 **personalInfo** | [**PersonalInfo**](PersonalInfo.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveProfilePictureInfo

> saveProfilePictureInfo(profilePictureInfo)

Change user picture information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAccountApi();
let profilePictureInfo = new BeezUpMerchantApi.ProfilePictureInfo(); // ProfilePictureInfo | 
apiInstance.saveProfilePictureInfo(profilePictureInfo, (error, data, response) => {
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
 **profilePictureInfo** | [**ProfilePictureInfo**](ProfilePictureInfo.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

