# TwilioBulkexports.BulkexportsV1ExportApi

All URIs are relative to *https://bulkexports.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchExport**](BulkexportsV1ExportApi.md#fetchExport) | **GET** /v1/Exports/{ResourceType} | 



## fetchExport

> BulkexportsV1Export fetchExport(resourceType)



Fetch a specific Export.

### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1ExportApi();
let resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
apiInstance.fetchExport(resourceType, (error, data, response) => {
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
 **resourceType** | **String**| The type of communication – Messages, Calls, Conferences, and Participants | 

### Return type

[**BulkexportsV1Export**](BulkexportsV1Export.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

