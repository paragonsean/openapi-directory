# TwilioStudio.StudioV2FlowApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFlow**](StudioV2FlowApi.md#createFlow) | **POST** /v2/Flows | 
[**deleteFlow**](StudioV2FlowApi.md#deleteFlow) | **DELETE** /v2/Flows/{Sid} | 
[**fetchFlow**](StudioV2FlowApi.md#fetchFlow) | **GET** /v2/Flows/{Sid} | 
[**listFlow**](StudioV2FlowApi.md#listFlow) | **GET** /v2/Flows | 
[**updateFlow**](StudioV2FlowApi.md#updateFlow) | **POST** /v2/Flows/{Sid} | 



## createFlow

> StudioV2Flow createFlow(definition, friendlyName, status, opts)



Create a Flow.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowApi();
let definition = null; // Object | JSON representation of flow definition.
let friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the Flow.
let status = "status_example"; // FlowEnumStatus | 
let opts = {
  'commitMessage': "commitMessage_example" // String | Description of change made in the revision.
};
apiInstance.createFlow(definition, friendlyName, status, opts, (error, data, response) => {
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
 **definition** | [**Object**](Object.md)| JSON representation of flow definition. | 
 **friendlyName** | **String**| The string that you assigned to describe the Flow. | 
 **status** | **FlowEnumStatus**|  | 
 **commitMessage** | **String**| Description of change made in the revision. | [optional] 

### Return type

[**StudioV2Flow**](StudioV2Flow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteFlow

> deleteFlow(sid)



Delete a specific Flow.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowApi();
let sid = "sid_example"; // String | The SID of the Flow resource to delete.
apiInstance.deleteFlow(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Flow resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchFlow

> StudioV2Flow fetchFlow(sid)



Retrieve a specific Flow.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowApi();
let sid = "sid_example"; // String | The SID of the Flow resource to fetch.
apiInstance.fetchFlow(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Flow resource to fetch. | 

### Return type

[**StudioV2Flow**](StudioV2Flow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFlow

> ListFlowResponse listFlow(opts)



Retrieve a list of all Flows.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listFlow(opts, (error, data, response) => {
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

[**ListFlowResponse**](ListFlowResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFlow

> StudioV2Flow updateFlow(sid, status, opts)



Update a Flow.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowApi();
let sid = "sid_example"; // String | The SID of the Flow resource to fetch.
let status = "status_example"; // FlowEnumStatus | 
let opts = {
  'commitMessage': "commitMessage_example", // String | Description of change made in the revision.
  'definition': null, // Object | JSON representation of flow definition.
  'friendlyName': "friendlyName_example" // String | The string that you assigned to describe the Flow.
};
apiInstance.updateFlow(sid, status, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the Flow resource to fetch. | 
 **status** | **FlowEnumStatus**|  | 
 **commitMessage** | **String**| Description of change made in the revision. | [optional] 
 **definition** | [**Object**](Object.md)| JSON representation of flow definition. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the Flow. | [optional] 

### Return type

[**StudioV2Flow**](StudioV2Flow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

