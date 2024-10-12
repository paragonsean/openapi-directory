# WhatsAppBusinessApi.TwoStepVerificationApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disableTwoStep**](TwoStepVerificationApi.md#disableTwoStep) | **DELETE** /settings/account/two-step | Disable-Two-Step
[**enableTwoStep**](TwoStepVerificationApi.md#enableTwoStep) | **POST** /settings/account/two-step | Enable-Two-Step



## disableTwoStep

> disableTwoStep()

Disable-Two-Step

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.TwoStepVerificationApi();
apiInstance.disableTwoStep((error, data, response) => {
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enableTwoStep

> enableTwoStep(enableTwoStepRequestBody)

Enable-Two-Step

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.TwoStepVerificationApi();
let enableTwoStepRequestBody = {"pin":"<Two-Step Verification PIN>"}; // EnableTwoStepRequestBody | 
apiInstance.enableTwoStep(enableTwoStepRequestBody, (error, data, response) => {
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
 **enableTwoStepRequestBody** | [**EnableTwoStepRequestBody**](EnableTwoStepRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

