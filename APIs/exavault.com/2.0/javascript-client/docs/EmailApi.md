# ExaVault.EmailApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendReferralEmail**](EmailApi.md#sendReferralEmail) | **POST** /email/referral | Send referral email to a given address
[**sendWelcomeEmail**](EmailApi.md#sendWelcomeEmail) | **POST** /email/welcome/{username} | Resend welcome email to specific user



## sendReferralEmail

> EmptyResponse sendReferralEmail(evApiKey, evAccessToken, opts)

Send referral email to a given address

Invite a friend to sign up for a free trial of ExaVault. Send a [referral](/lp/referafriend/) email to an email address. If the recipient signs up for ExaVault, we&#39;ll apply a credit to your account for the referral. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.EmailApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'sendReferralEmailRequestBody': {"emails":["user@example.com"],"message":"I use ExaVault for secure file sending, and so should you. Follow my link to sign up for a trial."} // SendReferralEmailRequestBody | 
};
apiInstance.sendReferralEmail(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **sendReferralEmailRequestBody** | [**SendReferralEmailRequestBody**](SendReferralEmailRequestBody.md)|  | [optional] 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendWelcomeEmail

> EmptyResponse sendWelcomeEmail(evApiKey, evAccessToken, username)

Resend welcome email to specific user

Send a welcome email to a user. The contents of the welcome email can be set by [PATCH /accounts](#operation/updateAccount).

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.EmailApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let username = "exampleuser"; // String | A username to send the welcome email to.
apiInstance.sendWelcomeEmail(evApiKey, evAccessToken, username, (error, data, response) => {
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
 **username** | **String**| A username to send the welcome email to. | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

