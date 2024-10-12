# AgcoApi.ActivitiesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activitiesDeleteActivity**](ActivitiesApi.md#activitiesDeleteActivity) | **DELETE** /api/v2/activities/{activityID} | Mark the delete flag for the Activity
[**activitiesGetActivities**](ActivitiesApi.md#activitiesGetActivities) | **GET** /api/v2/activities | Get Activities
[**activitiesGetActivity**](ActivitiesApi.md#activitiesGetActivity) | **GET** /api/v2/activities/{activityID} | Get an Activity by ID
[**activitiesPostActivity**](ActivitiesApi.md#activitiesPostActivity) | **POST** /api/v2/activities | Create an Activity
[**activitiesPutActivity**](ActivitiesApi.md#activitiesPutActivity) | **PUT** /api/v2/activities/{activityID} | Update an Activity



## activitiesDeleteActivity

> activitiesDeleteActivity(activityID)

Mark the delete flag for the Activity

Deletes an Activity. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivitiesApi();
let activityID = 56; // Number | The id of the activity to delete
apiInstance.activitiesDeleteActivity(activityID, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activityID** | **Number**| The id of the activity to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## activitiesGetActivities

> APIPagedResponseBuildSystemSharedDTOActivity activitiesGetActivities(opts)

Get Activities

Gets a collection of Activities. When successful, the response is a PagedResponse of Activities.                If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivitiesApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'isIncludeDeleted': true // Boolean | Does it include deleted activity, or not
};
apiInstance.activitiesGetActivities(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **isIncludeDeleted** | **Boolean**| Does it include deleted activity, or not | [optional] 

### Return type

[**APIPagedResponseBuildSystemSharedDTOActivity**](APIPagedResponseBuildSystemSharedDTOActivity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## activitiesGetActivity

> BuildSystemSharedDTOActivity activitiesGetActivity(activityID, opts)

Get an Activity by ID

Gets an Activity by ID. When successful, the response is the requested Activity.  If unsuccessful,              an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivitiesApi();
let activityID = 56; // Number | The ID of the Activity to get.
let opts = {
  'isIncludeDeleted': true // Boolean | Does it include deleted activity, or not
};
apiInstance.activitiesGetActivity(activityID, opts, (error, data, response) => {
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
 **activityID** | **Number**| The ID of the Activity to get. | 
 **isIncludeDeleted** | **Boolean**| Does it include deleted activity, or not | [optional] 

### Return type

[**BuildSystemSharedDTOActivity**](BuildSystemSharedDTOActivity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## activitiesPostActivity

> Number activitiesPostActivity(buildSystemSharedDTOActivity)

Create an Activity

Creates an Activity.  The body of the POST is the Activity to create.  The ActivityID will be assigned              on creation of the Activity.  When successful, the response is the ActivityID.  If unsuccessful, an               appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivitiesApi();
let buildSystemSharedDTOActivity = new AgcoApi.BuildSystemSharedDTOActivity(); // BuildSystemSharedDTOActivity | The activity to create.  The ActivityID will be assigned on creation of the Activity.
apiInstance.activitiesPostActivity(buildSystemSharedDTOActivity, (error, data, response) => {
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
 **buildSystemSharedDTOActivity** | [**BuildSystemSharedDTOActivity**](BuildSystemSharedDTOActivity.md)| The activity to create.  The ActivityID will be assigned on creation of the Activity. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## activitiesPutActivity

> activitiesPutActivity(activityID, buildSystemSharedDTOActivity)

Update an Activity

Updates an Activity.  The body of the PUT is the updated Activity.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivitiesApi();
let activityID = 56; // Number | The id of the activity to update
let buildSystemSharedDTOActivity = new AgcoApi.BuildSystemSharedDTOActivity(); // BuildSystemSharedDTOActivity | The updated activity
apiInstance.activitiesPutActivity(activityID, buildSystemSharedDTOActivity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activityID** | **Number**| The id of the activity to update | 
 **buildSystemSharedDTOActivity** | [**BuildSystemSharedDTOActivity**](BuildSystemSharedDTOActivity.md)| The updated activity | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

