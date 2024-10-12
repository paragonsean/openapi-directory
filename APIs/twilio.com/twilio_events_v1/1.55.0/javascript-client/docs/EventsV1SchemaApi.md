# TwilioEvents.EventsV1SchemaApi

All URIs are relative to *https://events.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchSchema**](EventsV1SchemaApi.md#fetchSchema) | **GET** /v1/Schemas/{Id} | 



## fetchSchema

> EventsV1Schema fetchSchema(id)



Fetch a specific schema with its nested versions.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SchemaApi();
let id = "id_example"; // String | The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
apiInstance.fetchSchema(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the schema. Each schema can have multiple versions, that share the same id. | 

### Return type

[**EventsV1Schema**](EventsV1Schema.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

