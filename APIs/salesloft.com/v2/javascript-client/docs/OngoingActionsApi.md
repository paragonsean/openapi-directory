# SalesLoftPlatform.OngoingActionsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2OngoingActionsJsonPost**](OngoingActionsApi.md#v2OngoingActionsJsonPost) | **POST** /v2/ongoing_actions.json | Create an ongoing action



## v2OngoingActionsJsonPost

> Action v2OngoingActionsJsonPost(opts)

Create an ongoing action

Creates an ongoing action. An ongoing action is an action that is not yet completed, but progress has been made towards the completion. The user should not need to do anything for an ongoing action to be completed. An ongoing action can be later completed by creating an activity.  Ongoing actions are marked as status&#x3D;pending_activity. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.OngoingActionsApi();
let opts = {
  'actionId': 56 // Number | Action that is being marked ongoing. This will validate that the action is still valid before modifying it. Ongoing actions can not be marked ongoing. 
};
apiInstance.v2OngoingActionsJsonPost(opts, (error, data, response) => {
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
 **actionId** | **Number**| Action that is being marked ongoing. This will validate that the action is still valid before modifying it. Ongoing actions can not be marked ongoing.  | [optional] 

### Return type

[**Action**](Action.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

