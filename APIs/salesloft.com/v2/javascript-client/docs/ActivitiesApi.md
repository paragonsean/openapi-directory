# SalesLoftPlatform.ActivitiesApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2ActivitiesJsonPost**](ActivitiesApi.md#v2ActivitiesJsonPost) | **POST** /v2/activities.json | Create an activity



## v2ActivitiesJsonPost

> Activity v2ActivitiesJsonPost(opts)

Create an activity

Creates an activity. An activity will mark the associated action as completed. Currently, only certain action types can have an activity explicitly created for them. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ActivitiesApi();
let opts = {
  'actionId': 56, // Number | Action that is being completed. This will validate that the action is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The action must have a type of 'integration'. 
  'taskId': 56 // Number | Task that is being completed. This will validate that the task is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The task must have a type of 'integration'. 
};
apiInstance.v2ActivitiesJsonPost(opts, (error, data, response) => {
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
 **actionId** | **Number**| Action that is being completed. This will validate that the action is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The action must have a type of &#39;integration&#39;.  | [optional] 
 **taskId** | **Number**| Task that is being completed. This will validate that the task is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The task must have a type of &#39;integration&#39;.  | [optional] 

### Return type

[**Activity**](Activity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

