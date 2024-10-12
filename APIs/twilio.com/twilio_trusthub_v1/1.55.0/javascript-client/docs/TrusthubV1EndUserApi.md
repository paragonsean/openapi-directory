# TwilioTrusthub.TrusthubV1EndUserApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEndUser**](TrusthubV1EndUserApi.md#createEndUser) | **POST** /v1/EndUsers | 
[**deleteEndUser**](TrusthubV1EndUserApi.md#deleteEndUser) | **DELETE** /v1/EndUsers/{Sid} | 
[**fetchEndUser**](TrusthubV1EndUserApi.md#fetchEndUser) | **GET** /v1/EndUsers/{Sid} | 
[**listEndUser**](TrusthubV1EndUserApi.md#listEndUser) | **GET** /v1/EndUsers | 
[**updateEndUser**](TrusthubV1EndUserApi.md#updateEndUser) | **POST** /v1/EndUsers/{Sid} | 



## createEndUser

> TrusthubV1EndUser createEndUser(friendlyName, type, opts)



Create a new End User.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1EndUserApi();
let friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
let type = "type_example"; // String | The type of end user of the Bundle resource - can be `individual` or `business`.
let opts = {
  'attributes': null // Object | The set of parameters that are the attributes of the End User resource which are derived End User Types.
};
apiInstance.createEndUser(friendlyName, type, opts, (error, data, response) => {
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
 **friendlyName** | **String**| The string that you assigned to describe the resource. | 
 **type** | **String**| The type of end user of the Bundle resource - can be &#x60;individual&#x60; or &#x60;business&#x60;. | 
 **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the End User resource which are derived End User Types. | [optional] 

### Return type

[**TrusthubV1EndUser**](TrusthubV1EndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteEndUser

> deleteEndUser(sid)



Delete a specific End User.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1EndUserApi();
let sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
apiInstance.deleteEndUser(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string created by Twilio to identify the End User resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchEndUser

> TrusthubV1EndUser fetchEndUser(sid)



Fetch specific End User Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1EndUserApi();
let sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
apiInstance.fetchEndUser(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string created by Twilio to identify the End User resource. | 

### Return type

[**TrusthubV1EndUser**](TrusthubV1EndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEndUser

> ListEndUserResponse listEndUser(opts)



Retrieve a list of all End User for an account.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1EndUserApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEndUser(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListEndUserResponse**](ListEndUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateEndUser

> TrusthubV1EndUser updateEndUser(sid, opts)



Update an existing End User.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1EndUserApi();
let sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
let opts = {
  'attributes': null, // Object | The set of parameters that are the attributes of the End User resource which are derived End User Types.
  'friendlyName': "friendlyName_example" // String | The string that you assigned to describe the resource.
};
apiInstance.updateEndUser(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique string created by Twilio to identify the End User resource. | 
 **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the End User resource which are derived End User Types. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 

### Return type

[**TrusthubV1EndUser**](TrusthubV1EndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

