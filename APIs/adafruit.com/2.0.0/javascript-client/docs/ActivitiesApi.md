# AdafruitIoRestApi.ActivitiesApi

All URIs are relative to *https://io.adafruit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allActivities**](ActivitiesApi.md#allActivities) | **GET** /{username}/activities | All activities for current user
[**destroyActivities**](ActivitiesApi.md#destroyActivities) | **DELETE** /{username}/activities | All activities for current user
[**getActivity**](ActivitiesApi.md#getActivity) | **GET** /{username}/activities/{type} | Get activities by type for current user



## allActivities

> [Activity] allActivities(username, opts)

All activities for current user

The Activities endpoint returns information about the user&#39;s activities.

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.ActivitiesApi();
let username = "username_example"; // String | a valid username string
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start time for filtering, returns records created after given time.
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End time for filtering, returns records created before give time.
  'limit': 56 // Number | Limit the number of records returned.
};
apiInstance.allActivities(username, opts, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **startTime** | **Date**| Start time for filtering, returns records created after given time. | [optional] 
 **endTime** | **Date**| End time for filtering, returns records created before give time. | [optional] 
 **limit** | **Number**| Limit the number of records returned. | [optional] 

### Return type

[**[Activity]**](Activity.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## destroyActivities

> destroyActivities(username)

All activities for current user

Delete all your activities.

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.ActivitiesApi();
let username = "username_example"; // String | a valid username string
apiInstance.destroyActivities(username, (error, data, response) => {
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
 **username** | **String**| a valid username string | 

### Return type

null (empty response body)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getActivity

> [Activity] getActivity(username, type, opts)

Get activities by type for current user

The Activities endpoint returns information about the user&#39;s activities.

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.ActivitiesApi();
let username = "username_example"; // String | a valid username string
let type = "type_example"; // String | 
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start time for filtering, returns records created after given time.
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End time for filtering, returns records created before give time.
  'limit': 56 // Number | Limit the number of records returned.
};
apiInstance.getActivity(username, type, opts, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **type** | **String**|  | 
 **startTime** | **Date**| Start time for filtering, returns records created after given time. | [optional] 
 **endTime** | **Date**| End time for filtering, returns records created before give time. | [optional] 
 **limit** | **Number**| Limit the number of records returned. | [optional] 

### Return type

[**[Activity]**](Activity.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

