# TwilioServerless.ServerlessV1ServiceApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](ServerlessV1ServiceApi.md#createService) | **POST** /v1/Services | 
[**deleteService**](ServerlessV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} | 
[**fetchService**](ServerlessV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} | 
[**listService**](ServerlessV1ServiceApi.md#listService) | **GET** /v1/Services | 
[**updateService**](ServerlessV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} | 



## createService

> ServerlessV1Service createService(friendlyName, uniqueName, opts)



Create a new Service resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1ServiceApi();
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
let uniqueName = "uniqueName_example"; // String | A user-defined string that uniquely identifies the Service resource. It can be used as an alternative to the `sid` in the URL path to address the Service resource. This value must be 50 characters or less in length and be unique.
let opts = {
  'includeCredentials': true, // Boolean | Whether to inject Account credentials into a function invocation context. The default value is `true`.
  'uiEditable': true // Boolean | Whether the Service's properties and subresources can be edited via the UI. The default value is `false`.
};
apiInstance.createService(friendlyName, uniqueName, opts, (error, data, response) => {
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
 **friendlyName** | **String**| A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters. | 
 **uniqueName** | **String**| A user-defined string that uniquely identifies the Service resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the Service resource. This value must be 50 characters or less in length and be unique. | 
 **includeCredentials** | **Boolean**| Whether to inject Account credentials into a function invocation context. The default value is &#x60;true&#x60;. | [optional] 
 **uiEditable** | **Boolean**| Whether the Service&#39;s properties and subresources can be edited via the UI. The default value is &#x60;false&#x60;. | [optional] 

### Return type

[**ServerlessV1Service**](ServerlessV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteService

> deleteService(sid)



Delete a Service resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1ServiceApi();
let sid = "sid_example"; // String | The `sid` or `unique_name` of the Service resource to delete.
apiInstance.deleteService(sid, (error, data, response) => {
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
 **sid** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> ServerlessV1Service fetchService(sid)



Retrieve a specific Service resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1ServiceApi();
let sid = "sid_example"; // String | The `sid` or `unique_name` of the Service resource to fetch.
apiInstance.fetchService(sid, (error, data, response) => {
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
 **sid** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to fetch. | 

### Return type

[**ServerlessV1Service**](ServerlessV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listService

> ListServiceResponse listService(opts)



Retrieve a list of all Services.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1ServiceApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listService(opts, (error, data, response) => {
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

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateService

> ServerlessV1Service updateService(sid, opts)



Update a specific Service resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1ServiceApi();
let sid = "sid_example"; // String | The `sid` or `unique_name` of the Service resource to update.
let opts = {
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
  'includeCredentials': true, // Boolean | Whether to inject Account credentials into a function invocation context.
  'uiEditable': true // Boolean | Whether the Service resource's properties and subresources can be edited via the UI. The default value is `false`.
};
apiInstance.updateService(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters. | [optional] 
 **includeCredentials** | **Boolean**| Whether to inject Account credentials into a function invocation context. | [optional] 
 **uiEditable** | **Boolean**| Whether the Service resource&#39;s properties and subresources can be edited via the UI. The default value is &#x60;false&#x60;. | [optional] 

### Return type

[**ServerlessV1Service**](ServerlessV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

