# RubrikRestApi.ReplicationApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disablePerLocationPause**](ReplicationApi.md#disablePerLocationPause) | **POST** /replication/location_pause/disable | Resume replication from specified source clusters
[**enablePerLocationPause**](ReplicationApi.md#enablePerLocationPause) | **POST** /replication/location_pause/enable | Pause replication from specified source clusters



## disablePerLocationPause

> disablePerLocationPause(disablePerLocationPause)

Resume replication from specified source clusters

A single Rubrik cluster can be the replication target for multiple source Rubrik clusters. For each source cluster specified, this resumes replication from that source cluster to the target cluster. This call must be made on the target cluster. 

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

let apiInstance = new RubrikRestApi.ReplicationApi();
let disablePerLocationPause = new RubrikRestApi.DisablePerLocationPause(); // DisablePerLocationPause | A configuration value that specifies which source clusters resume replication. Snapshots taken before or during the replication pause can be skipped. 
apiInstance.disablePerLocationPause(disablePerLocationPause, (error, data, response) => {
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
 **disablePerLocationPause** | [**DisablePerLocationPause**](DisablePerLocationPause.md)| A configuration value that specifies which source clusters resume replication. Snapshots taken before or during the replication pause can be skipped.  | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enablePerLocationPause

> enablePerLocationPause(enablePerLocationPause)

Pause replication from specified source clusters

A single Rubrik cluster can be the replication target for multiple source Rubrik clusters. For each source cluster specified, this pauses replication from that source cluster to the target cluster. This call must be made on the target cluster. 

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

let apiInstance = new RubrikRestApi.ReplicationApi();
let enablePerLocationPause = new RubrikRestApi.EnablePerLocationPause(); // EnablePerLocationPause | A configuration value that specifies which source clusters pause replication. Replication jobs can be canceled immediately or be allowed to finish. 
apiInstance.enablePerLocationPause(enablePerLocationPause, (error, data, response) => {
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
 **enablePerLocationPause** | [**EnablePerLocationPause**](EnablePerLocationPause.md)| A configuration value that specifies which source clusters pause replication. Replication jobs can be canceled immediately or be allowed to finish.  | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

