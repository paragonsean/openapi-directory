# TwilioBulkexports.BulkexportsV1ExportCustomJobApi

All URIs are relative to *https://bulkexports.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createExportCustomJob**](BulkexportsV1ExportCustomJobApi.md#createExportCustomJob) | **POST** /v1/Exports/{ResourceType}/Jobs | 
[**listExportCustomJob**](BulkexportsV1ExportCustomJobApi.md#listExportCustomJob) | **GET** /v1/Exports/{ResourceType}/Jobs | 



## createExportCustomJob

> BulkexportsV1ExportExportCustomJob createExportCustomJob(resourceType, endDay, friendlyName, startDay, opts)





### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1ExportCustomJobApi();
let resourceType = "resourceType_example"; // String | The type of communication – Messages or Calls, Conferences, and Participants
let endDay = "endDay_example"; // String | The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day.
let friendlyName = "friendlyName_example"; // String | The friendly name specified when creating the job
let startDay = "startDay_example"; // String | The start day for the custom export specified as a string in the format of yyyy-mm-dd
let opts = {
  'email': "email_example", // String | The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job's status.
  'webhookMethod': "webhookMethod_example", // String | This is the method used to call the webhook on completion of the job. If this is supplied, `WebhookUrl` must also be supplied.
  'webhookUrl': "webhookUrl_example" // String | The optional webhook url called on completion of the job. If this is supplied, `WebhookMethod` must also be supplied. If you set neither webhook nor email, you will have to check your job's status manually.
};
apiInstance.createExportCustomJob(resourceType, endDay, friendlyName, startDay, opts, (error, data, response) => {
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
 **resourceType** | **String**| The type of communication – Messages or Calls, Conferences, and Participants | 
 **endDay** | **String**| The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day. | 
 **friendlyName** | **String**| The friendly name specified when creating the job | 
 **startDay** | **String**| The start day for the custom export specified as a string in the format of yyyy-mm-dd | 
 **email** | **String**| The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job&#39;s status. | [optional] 
 **webhookMethod** | **String**| This is the method used to call the webhook on completion of the job. If this is supplied, &#x60;WebhookUrl&#x60; must also be supplied. | [optional] 
 **webhookUrl** | **String**| The optional webhook url called on completion of the job. If this is supplied, &#x60;WebhookMethod&#x60; must also be supplied. If you set neither webhook nor email, you will have to check your job&#39;s status manually. | [optional] 

### Return type

[**BulkexportsV1ExportExportCustomJob**](BulkexportsV1ExportExportCustomJob.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## listExportCustomJob

> ListExportCustomJobResponse listExportCustomJob(resourceType, opts)





### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1ExportCustomJobApi();
let resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listExportCustomJob(resourceType, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListExportCustomJobResponse**](ListExportCustomJobResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

