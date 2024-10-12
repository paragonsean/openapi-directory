# TwilioAutopilot.AutopilotV1FieldValueApi

All URIs are relative to *https://autopilot.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFieldValue**](AutopilotV1FieldValueApi.md#createFieldValue) | **POST** /v1/Assistants/{AssistantSid}/FieldTypes/{FieldTypeSid}/FieldValues | 
[**deleteFieldValue**](AutopilotV1FieldValueApi.md#deleteFieldValue) | **DELETE** /v1/Assistants/{AssistantSid}/FieldTypes/{FieldTypeSid}/FieldValues/{Sid} | 
[**fetchFieldValue**](AutopilotV1FieldValueApi.md#fetchFieldValue) | **GET** /v1/Assistants/{AssistantSid}/FieldTypes/{FieldTypeSid}/FieldValues/{Sid} | 
[**listFieldValue**](AutopilotV1FieldValueApi.md#listFieldValue) | **GET** /v1/Assistants/{AssistantSid}/FieldTypes/{FieldTypeSid}/FieldValues | 



## createFieldValue

> AutopilotV1AssistantFieldTypeFieldValue createFieldValue(assistantSid, fieldTypeSid, language, value, opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1FieldValueApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the new resource.
let fieldTypeSid = "fieldTypeSid_example"; // String | The SID of the Field Type associated with the Field Value.
let language = "language_example"; // String | The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
let value = "value_example"; // String | The Field Value data.
let opts = {
  'synonymOf': "synonymOf_example" // String | The string value that indicates which word the field value is a synonym of.
};
apiInstance.createFieldValue(assistantSid, fieldTypeSid, language, value, opts, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the new resource. | 
 **fieldTypeSid** | **String**| The SID of the Field Type associated with the Field Value. | 
 **language** | **String**| The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: &#x60;en-US&#x60; | 
 **value** | **String**| The Field Value data. | 
 **synonymOf** | **String**| The string value that indicates which word the field value is a synonym of. | [optional] 

### Return type

[**AutopilotV1AssistantFieldTypeFieldValue**](AutopilotV1AssistantFieldTypeFieldValue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteFieldValue

> deleteFieldValue(assistantSid, fieldTypeSid, sid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1FieldValueApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to delete.
let fieldTypeSid = "fieldTypeSid_example"; // String | The SID of the Field Type associated with the Field Value to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the FieldValue resource to delete.
apiInstance.deleteFieldValue(assistantSid, fieldTypeSid, sid, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to delete. | 
 **fieldTypeSid** | **String**| The SID of the Field Type associated with the Field Value to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the FieldValue resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchFieldValue

> AutopilotV1AssistantFieldTypeFieldValue fetchFieldValue(assistantSid, fieldTypeSid, sid)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1FieldValueApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resource to fetch.
let fieldTypeSid = "fieldTypeSid_example"; // String | The SID of the Field Type associated with the Field Value to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the FieldValue resource to fetch.
apiInstance.fetchFieldValue(assistantSid, fieldTypeSid, sid, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resource to fetch. | 
 **fieldTypeSid** | **String**| The SID of the Field Type associated with the Field Value to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the FieldValue resource to fetch. | 

### Return type

[**AutopilotV1AssistantFieldTypeFieldValue**](AutopilotV1AssistantFieldTypeFieldValue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFieldValue

> ListFieldValueResponse listFieldValue(assistantSid, fieldTypeSid, opts)





### Example

```javascript
import TwilioAutopilot from 'twilio_autopilot';
let defaultClient = TwilioAutopilot.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAutopilot.AutopilotV1FieldValueApi();
let assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to read.
let fieldTypeSid = "fieldTypeSid_example"; // String | The SID of the Field Type associated with the Field Value to read.
let opts = {
  'language': "language_example", // String | The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listFieldValue(assistantSid, fieldTypeSid, opts, (error, data, response) => {
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
 **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to read. | 
 **fieldTypeSid** | **String**| The SID of the Field Type associated with the Field Value to read. | 
 **language** | **String**| The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: &#x60;en-US&#x60; | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListFieldValueResponse**](ListFieldValueResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

