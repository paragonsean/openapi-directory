# TwilioFlex.FlexV1FlexFlowApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFlexFlow**](FlexV1FlexFlowApi.md#createFlexFlow) | **POST** /v1/FlexFlows | 
[**deleteFlexFlow**](FlexV1FlexFlowApi.md#deleteFlexFlow) | **DELETE** /v1/FlexFlows/{Sid} | 
[**fetchFlexFlow**](FlexV1FlexFlowApi.md#fetchFlexFlow) | **GET** /v1/FlexFlows/{Sid} | 
[**listFlexFlow**](FlexV1FlexFlowApi.md#listFlexFlow) | **GET** /v1/FlexFlows | 
[**updateFlexFlow**](FlexV1FlexFlowApi.md#updateFlexFlow) | **POST** /v1/FlexFlows/{Sid} | 



## createFlexFlow

> FlexV1FlexFlow createFlexFlow(channelType, chatServiceSid, friendlyName, opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1FlexFlowApi();
let channelType = "channelType_example"; // FlexFlowEnumChannelType | 
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the chat service.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Flex Flow resource.
let opts = {
  'contactIdentity': "contactIdentity_example", // String | The channel contact's Identity.
  'enabled': true, // Boolean | Whether the new Flex Flow is enabled.
  'integrationChannel': "integrationChannel_example", // String | The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for the Task that will be created. Applicable and required when `integrationType` is `task`. The default value is `default`.
  'integrationCreationOnMessage': true, // Boolean | In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
  'integrationFlowSid': "integrationFlowSid_example", // String | The SID of the Studio Flow. Required when `integrationType` is `studio`.
  'integrationPriority': 56, // Number | The Task priority of a new Task. The default priority is 0. Optional when `integrationType` is `task`, not applicable otherwise.
  'integrationRetryCount': 56, // Number | The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when `integrationType` is `studio` or `external`, not applicable otherwise.
  'integrationTimeout': 56, // Number | The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when `integrationType` is `task`, not applicable otherwise.
  'integrationUrl': "integrationUrl_example", // String | The URL of the external webhook. Required when `integrationType` is `external`.
  'integrationWorkflowSid': "integrationWorkflowSid_example", // String | The Workflow SID for a new Task. Required when `integrationType` is `task`.
  'integrationWorkspaceSid': "integrationWorkspaceSid_example", // String | The Workspace SID for a new Task. Required when `integrationType` is `task`.
  'integrationType': "integrationType_example", // FlexFlowEnumIntegrationType | 
  'janitorEnabled': true, // Boolean | When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to `false`.
  'longLived': true // Boolean | When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to `false`.
};
apiInstance.createFlexFlow(channelType, chatServiceSid, friendlyName, opts, (error, data, response) => {
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
 **channelType** | **FlexFlowEnumChannelType**|  | 
 **chatServiceSid** | **String**| The SID of the chat service. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Flex Flow resource. | 
 **contactIdentity** | **String**| The channel contact&#39;s Identity. | [optional] 
 **enabled** | **Boolean**| Whether the new Flex Flow is enabled. | [optional] 
 **integrationChannel** | **String**| The Task Channel SID (TCXXXX) or unique name (e.g., &#x60;sms&#x60;) to use for the Task that will be created. Applicable and required when &#x60;integrationType&#x60; is &#x60;task&#x60;. The default value is &#x60;default&#x60;. | [optional] 
 **integrationCreationOnMessage** | **Boolean**| In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging. | [optional] 
 **integrationFlowSid** | **String**| The SID of the Studio Flow. Required when &#x60;integrationType&#x60; is &#x60;studio&#x60;. | [optional] 
 **integrationPriority** | **Number**| The Task priority of a new Task. The default priority is 0. Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise. | [optional] 
 **integrationRetryCount** | **Number**| The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when &#x60;integrationType&#x60; is &#x60;studio&#x60; or &#x60;external&#x60;, not applicable otherwise. | [optional] 
 **integrationTimeout** | **Number**| The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise. | [optional] 
 **integrationUrl** | **String**| The URL of the external webhook. Required when &#x60;integrationType&#x60; is &#x60;external&#x60;. | [optional] 
 **integrationWorkflowSid** | **String**| The Workflow SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;. | [optional] 
 **integrationWorkspaceSid** | **String**| The Workspace SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;. | [optional] 
 **integrationType** | **FlexFlowEnumIntegrationType**|  | [optional] 
 **janitorEnabled** | **Boolean**| When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to &#x60;false&#x60;. | [optional] 
 **longLived** | **Boolean**| When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to &#x60;false&#x60;. | [optional] 

### Return type

[**FlexV1FlexFlow**](FlexV1FlexFlow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteFlexFlow

> deleteFlexFlow(sid)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1FlexFlowApi();
let sid = "sid_example"; // String | The SID of the Flex Flow resource to delete.
apiInstance.deleteFlexFlow(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Flex Flow resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchFlexFlow

> FlexV1FlexFlow fetchFlexFlow(sid)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1FlexFlowApi();
let sid = "sid_example"; // String | The SID of the Flex Flow resource to fetch.
apiInstance.fetchFlexFlow(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Flex Flow resource to fetch. | 

### Return type

[**FlexV1FlexFlow**](FlexV1FlexFlow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFlexFlow

> ListFlexFlowResponse listFlexFlow(opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1FlexFlowApi();
let opts = {
  'friendlyName': "friendlyName_example", // String | The `friendly_name` of the Flex Flow resources to read.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listFlexFlow(opts, (error, data, response) => {
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
 **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the Flex Flow resources to read. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListFlexFlowResponse**](ListFlexFlowResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFlexFlow

> FlexV1FlexFlow updateFlexFlow(sid, opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1FlexFlowApi();
let sid = "sid_example"; // String | The SID of the Flex Flow resource to update.
let opts = {
  'channelType': "channelType_example", // FlexFlowEnumChannelType | 
  'chatServiceSid': "chatServiceSid_example", // String | The SID of the chat service.
  'contactIdentity': "contactIdentity_example", // String | The channel contact's Identity.
  'enabled': true, // Boolean | Whether the new Flex Flow is enabled.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the Flex Flow resource.
  'integrationChannel': "integrationChannel_example", // String | The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for the Task that will be created. Applicable and required when `integrationType` is `task`. The default value is `default`.
  'integrationCreationOnMessage': true, // Boolean | In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
  'integrationFlowSid': "integrationFlowSid_example", // String | The SID of the Studio Flow. Required when `integrationType` is `studio`.
  'integrationPriority': 56, // Number | The Task priority of a new Task. The default priority is 0. Optional when `integrationType` is `task`, not applicable otherwise.
  'integrationRetryCount': 56, // Number | The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when `integrationType` is `studio` or `external`, not applicable otherwise.
  'integrationTimeout': 56, // Number | The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when `integrationType` is `task`, not applicable otherwise.
  'integrationUrl': "integrationUrl_example", // String | The URL of the external webhook. Required when `integrationType` is `external`.
  'integrationWorkflowSid': "integrationWorkflowSid_example", // String | The Workflow SID for a new Task. Required when `integrationType` is `task`.
  'integrationWorkspaceSid': "integrationWorkspaceSid_example", // String | The Workspace SID for a new Task. Required when `integrationType` is `task`.
  'integrationType': "integrationType_example", // FlexFlowEnumIntegrationType | 
  'janitorEnabled': true, // Boolean | When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to `false`.
  'longLived': true // Boolean | When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to `false`.
};
apiInstance.updateFlexFlow(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the Flex Flow resource to update. | 
 **channelType** | **FlexFlowEnumChannelType**|  | [optional] 
 **chatServiceSid** | **String**| The SID of the chat service. | [optional] 
 **contactIdentity** | **String**| The channel contact&#39;s Identity. | [optional] 
 **enabled** | **Boolean**| Whether the new Flex Flow is enabled. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the Flex Flow resource. | [optional] 
 **integrationChannel** | **String**| The Task Channel SID (TCXXXX) or unique name (e.g., &#x60;sms&#x60;) to use for the Task that will be created. Applicable and required when &#x60;integrationType&#x60; is &#x60;task&#x60;. The default value is &#x60;default&#x60;. | [optional] 
 **integrationCreationOnMessage** | **Boolean**| In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging. | [optional] 
 **integrationFlowSid** | **String**| The SID of the Studio Flow. Required when &#x60;integrationType&#x60; is &#x60;studio&#x60;. | [optional] 
 **integrationPriority** | **Number**| The Task priority of a new Task. The default priority is 0. Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise. | [optional] 
 **integrationRetryCount** | **Number**| The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when &#x60;integrationType&#x60; is &#x60;studio&#x60; or &#x60;external&#x60;, not applicable otherwise. | [optional] 
 **integrationTimeout** | **Number**| The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise. | [optional] 
 **integrationUrl** | **String**| The URL of the external webhook. Required when &#x60;integrationType&#x60; is &#x60;external&#x60;. | [optional] 
 **integrationWorkflowSid** | **String**| The Workflow SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;. | [optional] 
 **integrationWorkspaceSid** | **String**| The Workspace SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;. | [optional] 
 **integrationType** | **FlexFlowEnumIntegrationType**|  | [optional] 
 **janitorEnabled** | **Boolean**| When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to &#x60;false&#x60;. | [optional] 
 **longLived** | **Boolean**| When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to &#x60;false&#x60;. | [optional] 

### Return type

[**FlexV1FlexFlow**](FlexV1FlexFlow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

