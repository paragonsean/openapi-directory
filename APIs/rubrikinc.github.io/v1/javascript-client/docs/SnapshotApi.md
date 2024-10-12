# RubrikRestApi.SnapshotApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSnapshotStorageStatsV1**](SnapshotApi.md#getSnapshotStorageStatsV1) | **GET** /snapshot/{id}/storage/stats | Returns storage stats for a snapshot



## getSnapshotStorageStatsV1

> SnapshotStorageStats getSnapshotStorageStatsV1(id)

Returns storage stats for a snapshot

Returns the storage statistics for a snapshot.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.SnapshotApi();
let id = "id_example"; // String | ID assigned to a snapshot object.
apiInstance.getSnapshotStorageStatsV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a snapshot object. | 

### Return type

[**SnapshotStorageStats**](SnapshotStorageStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

