# TwilioStudio.StudioV1EngagementApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEngagement**](StudioV1EngagementApi.md#createEngagement) | **POST** /v1/Flows/{FlowSid}/Engagements | 
[**deleteEngagement**](StudioV1EngagementApi.md#deleteEngagement) | **DELETE** /v1/Flows/{FlowSid}/Engagements/{Sid} | 
[**fetchEngagement**](StudioV1EngagementApi.md#fetchEngagement) | **GET** /v1/Flows/{FlowSid}/Engagements/{Sid} | 
[**listEngagement**](StudioV1EngagementApi.md#listEngagement) | **GET** /v1/Flows/{FlowSid}/Engagements | 



## createEngagement

> StudioV1FlowEngagement createEngagement(flowSid, from, to, opts)



Triggers a new Engagement for the Flow

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1EngagementApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow.
let from = "from_example"; // String | The Twilio phone number to send messages or initiate calls from during the Flow Engagement. Available as variable `{{flow.channel.address}}`
let to = "to_example"; // String | The Contact phone number to start a Studio Flow Engagement, available as variable `{{contact.channel.address}}`.
let opts = {
  'parameters': null // Object | A JSON string we will add to your flow's context and that you can access as variables inside your flow. For example, if you pass in `Parameters={'name':'Zeke'}` then inside a widget you can reference the variable `{{flow.data.name}}` which will return the string 'Zeke'. Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode your JSON string.
};
apiInstance.createEngagement(flowSid, from, to, opts, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow. | 
 **from** | **String**| The Twilio phone number to send messages or initiate calls from during the Flow Engagement. Available as variable &#x60;{{flow.channel.address}}&#x60; | 
 **to** | **String**| The Contact phone number to start a Studio Flow Engagement, available as variable &#x60;{{contact.channel.address}}&#x60;. | 
 **parameters** | [**Object**](Object.md)| A JSON string we will add to your flow&#39;s context and that you can access as variables inside your flow. For example, if you pass in &#x60;Parameters&#x3D;{&#39;name&#39;:&#39;Zeke&#39;}&#x60; then inside a widget you can reference the variable &#x60;{{flow.data.name}}&#x60; which will return the string &#39;Zeke&#39;. Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode your JSON string. | [optional] 

### Return type

[**StudioV1FlowEngagement**](StudioV1FlowEngagement.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteEngagement

> deleteEngagement(flowSid, sid)



Delete this Engagement and all Steps relating to it.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1EngagementApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow to delete Engagements from.
let sid = "sid_example"; // String | The SID of the Engagement resource to delete.
apiInstance.deleteEngagement(flowSid, sid, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow to delete Engagements from. | 
 **sid** | **String**| The SID of the Engagement resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchEngagement

> StudioV1FlowEngagement fetchEngagement(flowSid, sid)



Retrieve an Engagement

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1EngagementApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow.
let sid = "sid_example"; // String | The SID of the Engagement resource to fetch.
apiInstance.fetchEngagement(flowSid, sid, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow. | 
 **sid** | **String**| The SID of the Engagement resource to fetch. | 

### Return type

[**StudioV1FlowEngagement**](StudioV1FlowEngagement.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEngagement

> ListEngagementResponse listEngagement(flowSid, opts)



Retrieve a list of all Engagements for the Flow.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1EngagementApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow to read Engagements from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEngagement(flowSid, opts, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow to read Engagements from. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListEngagementResponse**](ListEngagementResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

