# TwilioStudio.StudioV2FlowRevisionApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchFlowRevision**](StudioV2FlowRevisionApi.md#fetchFlowRevision) | **GET** /v2/Flows/{Sid}/Revisions/{Revision} | 
[**listFlowRevision**](StudioV2FlowRevisionApi.md#listFlowRevision) | **GET** /v2/Flows/{Sid}/Revisions | 



## fetchFlowRevision

> StudioV2FlowFlowRevision fetchFlowRevision(sid, revision)



Retrieve a specific Flow revision.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowRevisionApi();
let sid = "sid_example"; // String | The SID of the Flow resource to fetch.
let revision = "revision_example"; // String | Specific Revision number or can be `LatestPublished` and `LatestRevision`.
apiInstance.fetchFlowRevision(sid, revision, (error, data, response) => {
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
 **revision** | **String**| Specific Revision number or can be &#x60;LatestPublished&#x60; and &#x60;LatestRevision&#x60;. | 

### Return type

[**StudioV2FlowFlowRevision**](StudioV2FlowFlowRevision.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFlowRevision

> ListFlowRevisionResponse listFlowRevision(sid, opts)



Retrieve a list of all Flows revisions.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowRevisionApi();
let sid = "sid_example"; // String | The SID of the Flow resource to fetch.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listFlowRevision(sid, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListFlowRevisionResponse**](ListFlowRevisionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

