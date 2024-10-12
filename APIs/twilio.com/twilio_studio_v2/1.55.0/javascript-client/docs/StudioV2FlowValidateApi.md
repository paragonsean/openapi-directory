# TwilioStudio.StudioV2FlowValidateApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateFlowValidate**](StudioV2FlowValidateApi.md#updateFlowValidate) | **POST** /v2/Flows/Validate | 



## updateFlowValidate

> StudioV2FlowValidate updateFlowValidate(definition, friendlyName, status, opts)



Validate flow JSON definition

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV2FlowValidateApi();
let definition = null; // Object | JSON representation of flow definition.
let friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the Flow.
let status = "status_example"; // FlowValidateEnumStatus | 
let opts = {
  'commitMessage': "commitMessage_example" // String | Description of change made in the revision.
};
apiInstance.updateFlowValidate(definition, friendlyName, status, opts, (error, data, response) => {
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
 **status** | **FlowValidateEnumStatus**|  | 
 **commitMessage** | **String**| Description of change made in the revision. | [optional] 

### Return type

[**StudioV2FlowValidate**](StudioV2FlowValidate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

