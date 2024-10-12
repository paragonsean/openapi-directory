# TwilioEvents.EventsV1SchemaVersionApi

All URIs are relative to *https://events.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchSchemaVersion**](EventsV1SchemaVersionApi.md#fetchSchemaVersion) | **GET** /v1/Schemas/{Id}/Versions/{SchemaVersion} | 
[**listSchemaVersion**](EventsV1SchemaVersionApi.md#listSchemaVersion) | **GET** /v1/Schemas/{Id}/Versions | 



## fetchSchemaVersion

> EventsV1SchemaSchemaVersion fetchSchemaVersion(id, schemaVersion)



Fetch a specific schema and version.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SchemaVersionApi();
let id = "id_example"; // String | The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
let schemaVersion = 56; // Number | The version of the schema
apiInstance.fetchSchemaVersion(id, schemaVersion, (error, data, response) => {
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
 **schemaVersion** | **Number**| The version of the schema | 

### Return type

[**EventsV1SchemaSchemaVersion**](EventsV1SchemaSchemaVersion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSchemaVersion

> ListSchemaVersionResponse listSchemaVersion(id, opts)



Retrieve a paginated list of versions of the schema.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SchemaVersionApi();
let id = "id_example"; // String | The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSchemaVersion(id, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSchemaVersionResponse**](ListSchemaVersionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

