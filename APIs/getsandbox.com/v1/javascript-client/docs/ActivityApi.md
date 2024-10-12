# SandboxApi.ActivityApi

All URIs are relative to *https://getsandbox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSandboxesActivity**](ActivityApi.md#getSandboxesActivity) | **GET** /1/activity/search | searchActivity



## getSandboxesActivity

> [ActivityMessage] getSandboxesActivity(opts)

searchActivity

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.ActivityApi();
let opts = {
  'fromTimestamp': 789, // Number | Timestamp to start search from, epoch time in milliseconds.
  'sourceSandboxes': "sourceSandboxes_example", // String | Comma-separated list of Sandbox names to search.
  'keyword': "keyword_example", // String | A keyword to search activities by, will match any part of the ActivityMessage.
  'allTypes': true, // Boolean | Flag to return all types of activity, defaults to just Requests
  'maxResults': 56 // Number | Maximum number of results to return
};
apiInstance.getSandboxesActivity(opts, (error, data, response) => {
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
 **fromTimestamp** | **Number**| Timestamp to start search from, epoch time in milliseconds. | [optional] 
 **sourceSandboxes** | **String**| Comma-separated list of Sandbox names to search. | [optional] 
 **keyword** | **String**| A keyword to search activities by, will match any part of the ActivityMessage. | [optional] 
 **allTypes** | **Boolean**| Flag to return all types of activity, defaults to just Requests | [optional] 
 **maxResults** | **Number**| Maximum number of results to return | [optional] 

### Return type

[**[ActivityMessage]**](ActivityMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

