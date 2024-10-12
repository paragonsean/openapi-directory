# ExaVault.ActivityApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSessionLogs**](ActivityApi.md#getSessionLogs) | **GET** /activity/session | Get activity logs
[**getWebhookLogs**](ActivityApi.md#getWebhookLogs) | **GET** /activity/webhooks | Get webhook logs



## getSessionLogs

> SessionActivityResponse getSessionLogs(evApiKey, evAccessToken, opts)

Get activity logs

Returns the detailed activity logs for your account. Optional query paramaters will filter the returned results based on a number of options including usernames, activity types, or date ranges.   **NOTE:** Total Results will always return as 0 to avoid quering data you&#39;re not using and stay as performant as possible.     **Operation Types** Session activity is logged with an operation type that is different from what is visible through the [activity log interface in the web file manager](/docs/account/10-activity-logs/00-activity-logs). Consult the table below to compare the two:  | File Manager Value | API Value | Notes | |-----|----|---| | Connect | PASS | | | Disconnect | EXIT | | | Upload | STOR | | | Download | RETR | | | Delete | DELE | | | Create Folder | MKD | | | Rename | RNTO | | | Move | MOVE | | | Copy | COPY | | | Compress | COMPR | | | Extract | EXTRACT | | | Shared Folders | SHARE | | | Send Files | SEND | | | Receive Files | RECV | | | _N/A_ | EDIT\\_SEND | Update send. Not shown in file manager | | Update Share | EDIT\\_SHARE| |  | Update Receive | EDIT\\_RECV | | | Delete Send | DELE\\_SEND | | | Delete Receive | DELE\\_RECV | | | Delete Share | DELE\\_SHARE | | | Create Notification | NOTIFY | | | Update Notification | EDIT\\_NTFY| | | Delete Notification | DELE\\_NTFY | | | Create User | USER | | | Update User | EDIT\\_USER | | | Delete User | DELE\\_USER | | | _N/A_ | DFA | Create direct link. Not shown in file manager | | _N/A_ | EDIT\\_DFA | Update direct link options. Not shown in file manager | | _N/A_ | DELE\\_DFA | Deactivate direct link. Not shown in file manager| 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ActivityApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
let opts = {
  'startDate': new Date("2019-10-18T06:48:40Z"), // Date | Start date of the filter data range
  'endDate': new Date("2019-10-18T06:48:40Z"), // Date | End date of the filter data range
  'ipAddress': "127.0.0.1", // String | Used to filter session logs by ip address.
  'username': "jdoe", // String | Username used for filtering a list
  'path': "/folder*", // String | Path used to filter records
  'type': "EDIT_SHARE", // String | Filter session logs for operation type (see table above for acceptable values)
  'offset': 100, // Number | Offset of the records list
  'limit': 10, // Number | Limit of the records list
  'sort': "-date" // String | Comma separated list sort params
};
apiInstance.getSessionLogs(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key | 
 **evAccessToken** | **String**| Access Token | 
 **startDate** | **Date**| Start date of the filter data range | [optional] 
 **endDate** | **Date**| End date of the filter data range | [optional] 
 **ipAddress** | **String**| Used to filter session logs by ip address. | [optional] 
 **username** | **String**| Username used for filtering a list | [optional] 
 **path** | **String**| Path used to filter records | [optional] 
 **type** | **String**| Filter session logs for operation type (see table above for acceptable values) | [optional] 
 **offset** | **Number**| Offset of the records list | [optional] 
 **limit** | **Number**| Limit of the records list | [optional] 
 **sort** | **String**| Comma separated list sort params | [optional] 

### Return type

[**SessionActivityResponse**](SessionActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebhookLogs

> WebhookActivityResponse getWebhookLogs(evApiKey, evAccessToken, opts)

Get webhook logs

Returns the webhook logs for your account. Use the available query parameters to filter the listing of activity that is returned.  **NOTE:** Total Results will always return as 0 to avoid querying data you&#39;re not using and stay as performant as possible.   **Event Types**  Webhooks are triggered by enabled event types for your account, which are configured on the [developer settings page](/docs/account/09-settings/06-developer-settings). Not all event types may be allowed for your account type. These are the valid options for event types:  - resources.upload - resources.download - resources.delete - resources.createFolder - resources.rename - resources.move - resources.copy - resources.compress - resources.extract - shares.formSubmit 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ActivityApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Earliest date of entries to include in list
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Latest date of entries to include in list
  'endpointUrl': "endpointUrl_example", // String | Webhook listener endpoint
  'event': "resources.upload", // String | Type of activity that triggered the webhook attempt
  'statusCode': 200, // Number | Response code from the webhook endpoint
  'resourcePath': "/folder*", // String | Path of the resource that triggered the webhook attempt
  'username': "exampleuser", // String | Filter by triggering username.
  'offset': 100, // Number | Records to skip before returning results.
  'limit': 10, // Number | Limit of the records list
  'sort': "-date,event" // String | Comma separated list sort params
};
apiInstance.getWebhookLogs(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key | 
 **evAccessToken** | **String**| Access Token | 
 **startDate** | **Date**| Earliest date of entries to include in list | [optional] 
 **endDate** | **Date**| Latest date of entries to include in list | [optional] 
 **endpointUrl** | **String**| Webhook listener endpoint | [optional] 
 **event** | **String**| Type of activity that triggered the webhook attempt | [optional] 
 **statusCode** | **Number**| Response code from the webhook endpoint | [optional] 
 **resourcePath** | **String**| Path of the resource that triggered the webhook attempt | [optional] 
 **username** | **String**| Filter by triggering username. | [optional] 
 **offset** | **Number**| Records to skip before returning results. | [optional] 
 **limit** | **Number**| Limit of the records list | [optional] 
 **sort** | **String**| Comma separated list sort params | [optional] 

### Return type

[**WebhookActivityResponse**](WebhookActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

