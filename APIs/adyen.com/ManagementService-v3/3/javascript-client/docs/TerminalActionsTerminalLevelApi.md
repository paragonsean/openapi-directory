# ManagementApi.TerminalActionsTerminalLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postTerminalsScheduleActions**](TerminalActionsTerminalLevelApi.md#postTerminalsScheduleActions) | **POST** /terminals/scheduleActions | Create a terminal action



## postTerminalsScheduleActions

> ScheduleTerminalActionsResponse postTerminalsScheduleActions(opts)

Create a terminal action

Schedules a [terminal action](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) by specifying the action and the terminals that the action must be applied to.   The following restrictions apply: * You can schedule only one action at a time. For example, to install a new app version and remove an old app version, you have to make two API requests.  * The maximum number of terminals in a request is **100**. For example, to apply an action to 250 terminals, you have to divide the terminals over three API requests.  * If there is an error with one or more terminal IDs in the request, the action is scheduled for none of the terminals. You need to fix the error and try again.   To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalActionsTerminalLevelApi();
let opts = {
  'scheduleTerminalActionsRequest': new ManagementApi.ScheduleTerminalActionsRequest() // ScheduleTerminalActionsRequest | 
};
apiInstance.postTerminalsScheduleActions(opts, (error, data, response) => {
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
 **scheduleTerminalActionsRequest** | [**ScheduleTerminalActionsRequest**](ScheduleTerminalActionsRequest.md)|  | [optional] 

### Return type

[**ScheduleTerminalActionsResponse**](ScheduleTerminalActionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

