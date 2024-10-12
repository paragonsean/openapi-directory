# TwilioNumbers.NumbersV2EndUserApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEndUser**](NumbersV2EndUserApi.md#createEndUser) | **POST** /v2/RegulatoryCompliance/EndUsers | 
[**deleteEndUser**](NumbersV2EndUserApi.md#deleteEndUser) | **DELETE** /v2/RegulatoryCompliance/EndUsers/{Sid} | 
[**fetchEndUser**](NumbersV2EndUserApi.md#fetchEndUser) | **GET** /v2/RegulatoryCompliance/EndUsers/{Sid} | 
[**listEndUser**](NumbersV2EndUserApi.md#listEndUser) | **GET** /v2/RegulatoryCompliance/EndUsers | 
[**updateEndUser**](NumbersV2EndUserApi.md#updateEndUser) | **POST** /v2/RegulatoryCompliance/EndUsers/{Sid} | 



## createEndUser

> NumbersV2RegulatoryComplianceEndUser createEndUser(friendlyName, type, opts)



Create a new End User.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EndUserApi();
let friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
let type = "type_example"; // EndUserEnumType | 
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
 **type** | **EndUserEnumType**|  | 
 **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the End User resource which are derived End User Types. | [optional] 

### Return type

[**NumbersV2RegulatoryComplianceEndUser**](NumbersV2RegulatoryComplianceEndUser.md)

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
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EndUserApi();
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

> NumbersV2RegulatoryComplianceEndUser fetchEndUser(sid)



Fetch specific End User Instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EndUserApi();
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

[**NumbersV2RegulatoryComplianceEndUser**](NumbersV2RegulatoryComplianceEndUser.md)

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
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EndUserApi();
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

> NumbersV2RegulatoryComplianceEndUser updateEndUser(sid, opts)



Update an existing End User.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EndUserApi();
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

[**NumbersV2RegulatoryComplianceEndUser**](NumbersV2RegulatoryComplianceEndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

