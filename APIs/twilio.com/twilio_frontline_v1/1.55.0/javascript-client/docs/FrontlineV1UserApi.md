# TwilioFrontline.FrontlineV1UserApi

All URIs are relative to *https://frontline-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchUser**](FrontlineV1UserApi.md#fetchUser) | **GET** /v1/Users/{Sid} | 
[**updateUser**](FrontlineV1UserApi.md#updateUser) | **POST** /v1/Users/{Sid} | 



## fetchUser

> FrontlineV1User fetchUser(sid)



Fetch a frontline user

### Example

```javascript
import TwilioFrontline from 'twilio_frontline';
let defaultClient = TwilioFrontline.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFrontline.FrontlineV1UserApi();
let sid = "sid_example"; // String | The SID of the User resource to fetch. This value can be either the `sid` or the `identity` of the User resource to fetch.
apiInstance.fetchUser(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch. | 

### Return type

[**FrontlineV1User**](FrontlineV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUser

> FrontlineV1User updateUser(sid, opts)



Update an existing frontline user

### Example

```javascript
import TwilioFrontline from 'twilio_frontline';
let defaultClient = TwilioFrontline.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFrontline.FrontlineV1UserApi();
let sid = "sid_example"; // String | The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
let opts = {
  'avatar': "avatar_example", // String | The avatar URL which will be shown in Frontline application.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the User.
  'isAvailable': true, // Boolean | Whether the User is available for new conversations. Set to `false` to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).
  'state': "state_example" // UserEnumStateType | 
};
apiInstance.updateUser(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update. | 
 **avatar** | **String**| The avatar URL which will be shown in Frontline application. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the User. | [optional] 
 **isAvailable** | **Boolean**| Whether the User is available for new conversations. Set to &#x60;false&#x60; to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing). | [optional] 
 **state** | **UserEnumStateType**|  | [optional] 

### Return type

[**FrontlineV1User**](FrontlineV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

