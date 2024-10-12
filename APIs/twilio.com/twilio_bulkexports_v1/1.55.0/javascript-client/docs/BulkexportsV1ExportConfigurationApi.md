# TwilioBulkexports.BulkexportsV1ExportConfigurationApi

All URIs are relative to *https://bulkexports.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchExportConfiguration**](BulkexportsV1ExportConfigurationApi.md#fetchExportConfiguration) | **GET** /v1/Exports/{ResourceType}/Configuration | 
[**updateExportConfiguration**](BulkexportsV1ExportConfigurationApi.md#updateExportConfiguration) | **POST** /v1/Exports/{ResourceType}/Configuration | 



## fetchExportConfiguration

> BulkexportsV1ExportConfiguration fetchExportConfiguration(resourceType)



Fetch a specific Export Configuration.

### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1ExportConfigurationApi();
let resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
apiInstance.fetchExportConfiguration(resourceType, (error, data, response) => {
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

[**BulkexportsV1ExportConfiguration**](BulkexportsV1ExportConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateExportConfiguration

> BulkexportsV1ExportConfiguration updateExportConfiguration(resourceType, opts)



Update a specific Export Configuration.

### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1ExportConfigurationApi();
let resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
let opts = {
  'enabled': true, // Boolean | If true, Twilio will automatically generate every day's file when the day is over.
  'webhookMethod': "webhookMethod_example", // String | Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url
  'webhookUrl': "webhookUrl_example" // String | Stores the URL destination for the method specified in webhook_method.
};
apiInstance.updateExportConfiguration(resourceType, opts, (error, data, response) => {
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
 **enabled** | **Boolean**| If true, Twilio will automatically generate every day&#39;s file when the day is over. | [optional] 
 **webhookMethod** | **String**| Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url | [optional] 
 **webhookUrl** | **String**| Stores the URL destination for the method specified in webhook_method. | [optional] 

### Return type

[**BulkexportsV1ExportConfiguration**](BulkexportsV1ExportConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

