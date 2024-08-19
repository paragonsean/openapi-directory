# VictorOps.PersonalPagingPolicyValuesApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1PoliciesTypesContactsGet**](PersonalPagingPolicyValuesApi.md#apiPublicV1PoliciesTypesContactsGet) | **GET** /api-public/v1/policies/types/contacts | Get the available contact types
[**apiPublicV1PoliciesTypesNotificationsGet**](PersonalPagingPolicyValuesApi.md#apiPublicV1PoliciesTypesNotificationsGet) | **GET** /api-public/v1/policies/types/notifications | Get the available notification types
[**apiPublicV1PoliciesTypesTimeoutsGet**](PersonalPagingPolicyValuesApi.md#apiPublicV1PoliciesTypesTimeoutsGet) | **GET** /api-public/v1/policies/types/timeouts | Get the available timeout values



## apiPublicV1PoliciesTypesContactsGet

> ApiPublicV1PoliciesTypesContactsGet200Response apiPublicV1PoliciesTypesContactsGet(xVOApiId, xVOApiKey)

Get the available contact types

Get the available contact types  description: \&quot;Email Address\&quot;, type: \&quot;email\&quot; description: \&quot;Phone Number\&quot;, type: \&quot;phone\&quot;  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPolicyValuesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1PoliciesTypesContactsGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1PoliciesTypesContactsGet200Response**](ApiPublicV1PoliciesTypesContactsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1PoliciesTypesNotificationsGet

> ApiPublicV1PoliciesTypesNotificationsGet200Response apiPublicV1PoliciesTypesNotificationsGet(xVOApiId, xVOApiKey)

Get the available notification types

Get the available notification types  description: \&quot;Send a push notification to all my devices\&quot;, type: \&quot;push\&quot; description: \&quot;Send an email to an email address\&quot;, type: \&quot;email\&quot; description: \&quot;Send an SMS to a phone number\&quot;, type: \&quot;sms\&quot; description: \&quot;Make a phone call to a phone number\&quot;, type: \&quot;phone\&quot;  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPolicyValuesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1PoliciesTypesNotificationsGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1PoliciesTypesNotificationsGet200Response**](ApiPublicV1PoliciesTypesNotificationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1PoliciesTypesTimeoutsGet

> ApiPublicV1PoliciesTypesTimeoutsGet200Response apiPublicV1PoliciesTypesTimeoutsGet(xVOApiId, xVOApiKey)

Get the available timeout values

Get the available timeout values  description: \&quot;If still unacked after 1 minute\&quot;, type: 1 description: \&quot;If still unacked after 5 minutes\&quot;, type: 5 description: \&quot;If still unacked after 10 minutes\&quot;, type: 10 description: \&quot;If still unacked after 15 minutes\&quot;, type: 15 description: \&quot;If still unacked after 20 minutes\&quot;, type: 20 description: \&quot;If still unacked after 25 minutes\&quot;, type: 25 description: \&quot;If still unacked after 30 minutes\&quot;, type: 30 description: \&quot;If still unacked after 45 minutes\&quot;, type: 45 description: \&quot;If still unacked after 60 minutes\&quot;, type: 60  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPolicyValuesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1PoliciesTypesTimeoutsGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1PoliciesTypesTimeoutsGet200Response**](ApiPublicV1PoliciesTypesTimeoutsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

