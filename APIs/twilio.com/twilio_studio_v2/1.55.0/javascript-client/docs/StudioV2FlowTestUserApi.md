# TwilioStudio.StudioV2FlowTestUserApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTestUser**](StudioV2FlowTestUserApi.md#fetchTestUser) | **GET** /v2/Flows/{Sid}/TestUsers | 
[**updateTestUser**](StudioV2FlowTestUserApi.md#updateTestUser) | **POST** /v2/Flows/{Sid}/TestUsers | 



## fetchTestUser

> StudioV2FlowTestUser fetchTestUser(sid)



Fetch flow test users

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowTestUserApi();
let sid = "sid_example"; // String | Unique identifier of the flow.
apiInstance.fetchTestUser(sid, (error, data, response) => {
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
 **sid** | **String**| Unique identifier of the flow. | 

### Return type

[**StudioV2FlowTestUser**](StudioV2FlowTestUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTestUser

> StudioV2FlowTestUser updateTestUser(sid, testUsers)



Update flow test users

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowTestUserApi();
let sid = "sid_example"; // String | Unique identifier of the flow.
let testUsers = ["null"]; // [String] | List of test user identities that can test draft versions of the flow.
apiInstance.updateTestUser(sid, testUsers, (error, data, response) => {
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
 **sid** | **String**| Unique identifier of the flow. | 
 **testUsers** | [**[String]**](String.md)| List of test user identities that can test draft versions of the flow. | 

### Return type

[**StudioV2FlowTestUser**](StudioV2FlowTestUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

