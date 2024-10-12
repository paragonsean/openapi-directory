# ExaVault.AccountApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccount**](AccountApi.md#getAccount) | **GET** /account | Get account settings
[**updateAccount**](AccountApi.md#updateAccount) | **PATCH** /account | Update account settings



## getAccount

> AccountResponse getAccount(evApiKey, evAccessToken, opts)

Get account settings

Get settings for your account, such as current space usage, webhooks settings, welcome email content and IP address restrictions.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.AccountApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required for the request
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token for the request
let opts = {
  'include': "masterUser" // String | Related records to include in the response. Valid option is **masterUser**
};
apiInstance.getAccount(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required for the request | 
 **evAccessToken** | **String**| Access Token for the request | 
 **include** | **String**| Related records to include in the response. Valid option is **masterUser** | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccount

> AccountResponse updateAccount(evApiKey, evAccessToken, opts)

Update account settings

Update account settings, such as welcome email content, IP address restrictions, webhooks settings and secure password requirements.  **Notes**  - You must have [admin-level access](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to change account settings.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.AccountApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access token required to make the API call.
let opts = {
  'updateAccountRequestBody': {"accountOnboarding":true,"allowedIpRanges":[{"ipEnd":"67.208.64.254","ipStart":"67.208.64.228"}],"brandingSettings":{"companyName":"Example File Transfer","theme":"light"},"complexPasswords":true,"customSignature":"Please consider the planet before printing this email","emailContent":"Greetings, ExampleUser!  Your account is ready for you to start transferring files right now. Here's your link to set up your account [[setpassword]]  Henceforth, you shall be known as [[username]]","emailSubject":"Welcome to the Example Account","externalDomain":"https://example.com/files","quota":{"noticeEnabled":true,"noticeThreshold":90,"transactionsNoticeEnabled":true,"transactionsNoticeThreshold":80},"secureOnly":true,"showReferralLinks":false} // UpdateAccountRequestBody | Update Account Settings
};
apiInstance.updateAccount(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **updateAccountRequestBody** | [**UpdateAccountRequestBody**](UpdateAccountRequestBody.md)| Update Account Settings | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

