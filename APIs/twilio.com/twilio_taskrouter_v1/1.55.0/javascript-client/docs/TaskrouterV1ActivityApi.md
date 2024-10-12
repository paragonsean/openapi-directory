# TwilioTaskrouter.TaskrouterV1ActivityApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createActivity**](TaskrouterV1ActivityApi.md#createActivity) | **POST** /v1/Workspaces/{WorkspaceSid}/Activities | 
[**deleteActivity**](TaskrouterV1ActivityApi.md#deleteActivity) | **DELETE** /v1/Workspaces/{WorkspaceSid}/Activities/{Sid} | 
[**fetchActivity**](TaskrouterV1ActivityApi.md#fetchActivity) | **GET** /v1/Workspaces/{WorkspaceSid}/Activities/{Sid} | 
[**listActivity**](TaskrouterV1ActivityApi.md#listActivity) | **GET** /v1/Workspaces/{WorkspaceSid}/Activities | 
[**updateActivity**](TaskrouterV1ActivityApi.md#updateActivity) | **POST** /v1/Workspaces/{WorkspaceSid}/Activities/{Sid} | 



## createActivity

> TaskrouterV1WorkspaceActivity createActivity(workspaceSid, friendlyName, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ActivityApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Activity belongs to.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: `on-call`, `break`, and `email`.
let opts = {
  'available': true // Boolean | Whether the Worker should be eligible to receive a Task when it occupies the Activity. A value of `true`, `1`, or `yes` specifies the Activity is available. All other values specify that it is not. The value cannot be changed after the Activity is created.
};
apiInstance.createActivity(workspaceSid, friendlyName, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace that the new Activity belongs to. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: &#x60;on-call&#x60;, &#x60;break&#x60;, and &#x60;email&#x60;. | 
 **available** | **Boolean**| Whether the Worker should be eligible to receive a Task when it occupies the Activity. A value of &#x60;true&#x60;, &#x60;1&#x60;, or &#x60;yes&#x60; specifies the Activity is available. All other values specify that it is not. The value cannot be changed after the Activity is created. | [optional] 

### Return type

[**TaskrouterV1WorkspaceActivity**](TaskrouterV1WorkspaceActivity.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteActivity

> deleteActivity(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ActivityApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Activity resources to delete.
let sid = "sid_example"; // String | The SID of the Activity resource to delete.
apiInstance.deleteActivity(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Activity resources to delete. | 
 **sid** | **String**| The SID of the Activity resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchActivity

> TaskrouterV1WorkspaceActivity fetchActivity(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ActivityApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Activity resources to fetch.
let sid = "sid_example"; // String | The SID of the Activity resource to fetch.
apiInstance.fetchActivity(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Activity resources to fetch. | 
 **sid** | **String**| The SID of the Activity resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceActivity**](TaskrouterV1WorkspaceActivity.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listActivity

> ListActivityResponse listActivity(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ActivityApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Activity resources to read.
let opts = {
  'friendlyName': "friendlyName_example", // String | The `friendly_name` of the Activity resources to read.
  'available': "available_example", // String | Whether return only Activity resources that are available or unavailable. A value of `true` returns only available activities. Values of '1' or `yes` also indicate `true`. All other values represent `false` and return activities that are unavailable.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listActivity(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Activity resources to read. | 
 **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the Activity resources to read. | [optional] 
 **available** | **String**| Whether return only Activity resources that are available or unavailable. A value of &#x60;true&#x60; returns only available activities. Values of &#39;1&#39; or &#x60;yes&#x60; also indicate &#x60;true&#x60;. All other values represent &#x60;false&#x60; and return activities that are unavailable. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListActivityResponse**](ListActivityResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateActivity

> TaskrouterV1WorkspaceActivity updateActivity(workspaceSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ActivityApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Activity resources to update.
let sid = "sid_example"; // String | The SID of the Activity resource to update.
let opts = {
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: `on-call`, `break`, and `email`.
};
apiInstance.updateActivity(workspaceSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Activity resources to update. | 
 **sid** | **String**| The SID of the Activity resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: &#x60;on-call&#x60;, &#x60;break&#x60;, and &#x60;email&#x60;. | [optional] 

### Return type

[**TaskrouterV1WorkspaceActivity**](TaskrouterV1WorkspaceActivity.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

