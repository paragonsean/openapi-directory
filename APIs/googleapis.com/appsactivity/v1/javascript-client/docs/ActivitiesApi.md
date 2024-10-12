# DriveActivityApi.ActivitiesApi

All URIs are relative to *https://www.googleapis.com/appsactivity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsactivityActivitiesList**](ActivitiesApi.md#appsactivityActivitiesList) | **GET** /activities | 



## appsactivityActivitiesList

> ListActivitiesResponse appsactivityActivitiesList(opts)



Returns a list of activities visible to the current logged in user. Visible activities are determined by the visibility settings of the object that was acted on, e.g. Drive files a user can see. An activity is a record of past events. Multiple events may be merged if they are similar. A request is scoped to activities from a given Google service using the source parameter.

### Example

```javascript
import DriveActivityApi from 'drive_activity_api';
let defaultClient = DriveActivityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DriveActivityApi.ActivitiesApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'driveAncestorId': "driveAncestorId_example", // String | Identifies the Drive folder containing the items for which to return activities.
  'driveFileId': "driveFileId_example", // String | Identifies the Drive item to return activities for.
  'groupingStrategy': "groupingStrategy_example", // String | Indicates the strategy to use when grouping singleEvents items in the associated combinedEvent object.
  'pageSize': 56, // Number | The maximum number of events to return on a page. The response includes a continuation token if there are more events.
  'pageToken': "pageToken_example", // String | A token to retrieve a specific page of results.
  'source': "source_example", // String | The Google service from which to return activities. Possible values of source are:  - drive.google.com
  'userId': "userId_example" // String | The ID used for ACL checks (does not filter the resulting event list by the assigned value). Use the special value me to indicate the currently authenticated user.
};
apiInstance.appsactivityActivitiesList(opts, (error, data, response) => {
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
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **driveAncestorId** | **String**| Identifies the Drive folder containing the items for which to return activities. | [optional] 
 **driveFileId** | **String**| Identifies the Drive item to return activities for. | [optional] 
 **groupingStrategy** | **String**| Indicates the strategy to use when grouping singleEvents items in the associated combinedEvent object. | [optional] 
 **pageSize** | **Number**| The maximum number of events to return on a page. The response includes a continuation token if there are more events. | [optional] 
 **pageToken** | **String**| A token to retrieve a specific page of results. | [optional] 
 **source** | **String**| The Google service from which to return activities. Possible values of source are:  - drive.google.com | [optional] 
 **userId** | **String**| The ID used for ACL checks (does not filter the resulting event list by the assigned value). Use the special value me to indicate the currently authenticated user. | [optional] 

### Return type

[**ListActivitiesResponse**](ListActivitiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

