# JellyfinApi.ActivityLogApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLogEntries**](ActivityLogApi.md#getLogEntries) | **GET** /System/ActivityLog/Entries | Gets activity log entries.



## getLogEntries

> ActivityLogEntryQueryResult getLogEntries(opts)

Gets activity log entries.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ActivityLogApi();
let opts = {
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'minDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum date. Format = ISO.
  'hasUserId': true // Boolean | Optional. Filter log entries if it has user id, or not.
};
apiInstance.getLogEntries(opts, (error, data, response) => {
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
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **minDate** | **Date**| Optional. The minimum date. Format &#x3D; ISO. | [optional] 
 **hasUserId** | **Boolean**| Optional. Filter log entries if it has user id, or not. | [optional] 

### Return type

[**ActivityLogEntryQueryResult**](ActivityLogEntryQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

