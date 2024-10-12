# Apacta.ActivitiesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activitiesActivityIdDelete**](ActivitiesApi.md#activitiesActivityIdDelete) | **DELETE** /activities/{activity_id} | Delete an activity
[**activitiesActivityIdPut**](ActivitiesApi.md#activitiesActivityIdPut) | **PUT** /activities/{activity_id} | Edit an activity
[**activitiesBulkDeleteDelete**](ActivitiesApi.md#activitiesBulkDeleteDelete) | **DELETE** /activities/bulkDelete | Bulk delete activities
[**activitiesGet**](ActivitiesApi.md#activitiesGet) | **GET** /activities | Get a list of activities
[**activitiesPost**](ActivitiesApi.md#activitiesPost) | **POST** /activities | Create an activity



## activitiesActivityIdDelete

> EmptySuccessResponse activitiesActivityIdDelete(activityId)

Delete an activity

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ActivitiesApi();
let activityId = "activityId_example"; // String | 
apiInstance.activitiesActivityIdDelete(activityId, (error, data, response) => {
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
 **activityId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activitiesActivityIdPut

> EmptySuccessResponse activitiesActivityIdPut(activityId, activitiesPostRequest)

Edit an activity

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ActivitiesApi();
let activityId = "activityId_example"; // String | 
let activitiesPostRequest = new Apacta.ActivitiesPostRequest(); // ActivitiesPostRequest | 
apiInstance.activitiesActivityIdPut(activityId, activitiesPostRequest, (error, data, response) => {
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
 **activityId** | **String**|  | 
 **activitiesPostRequest** | [**ActivitiesPostRequest**](ActivitiesPostRequest.md)|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activitiesBulkDeleteDelete

> EmptySuccessResponse activitiesBulkDeleteDelete(bulkActionRequestBody)

Bulk delete activities

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ActivitiesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Activities ids
apiInstance.activitiesBulkDeleteDelete(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Activities ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activitiesGet

> ActivitiesGet200Response activitiesGet()

Get a list of activities

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ActivitiesApi();
apiInstance.activitiesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ActivitiesGet200Response**](ActivitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activitiesPost

> EmptySuccessResponse activitiesPost(activitiesPostRequest)

Create an activity

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ActivitiesApi();
let activitiesPostRequest = new Apacta.ActivitiesPostRequest(); // ActivitiesPostRequest | 
apiInstance.activitiesPost(activitiesPostRequest, (error, data, response) => {
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
 **activitiesPostRequest** | [**ActivitiesPostRequest**](ActivitiesPostRequest.md)|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

