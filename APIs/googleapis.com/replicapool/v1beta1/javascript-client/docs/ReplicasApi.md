# ReplicaPool.ReplicasApi

All URIs are relative to *https://www.googleapis.com/replicapool/v1beta1/projects*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicapoolReplicasDelete**](ReplicasApi.md#replicapoolReplicasDelete) | **POST** /{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName} | 
[**replicapoolReplicasGet**](ReplicasApi.md#replicapoolReplicasGet) | **GET** /{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName} | 
[**replicapoolReplicasList**](ReplicasApi.md#replicapoolReplicasList) | **GET** /{projectName}/zones/{zone}/pools/{poolName}/replicas | 
[**replicapoolReplicasRestart**](ReplicasApi.md#replicapoolReplicasRestart) | **POST** /{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName}/restart | 



## replicapoolReplicasDelete

> Replica replicapoolReplicasDelete(projectName, zone, poolName, replicaName, opts)



Deletes a replica from the pool.

### Example

```javascript
import ReplicaPool from 'replica_pool';
let defaultClient = ReplicaPool.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ReplicaPool.ReplicasApi();
let projectName = "projectName_example"; // String | The project ID for this request.
let zone = "zone_example"; // String | The zone where the replica lives.
let poolName = "poolName_example"; // String | The replica pool name for this request.
let replicaName = "replicaName_example"; // String | The name of the replica for this request.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'replicasDeleteRequest': new ReplicaPool.ReplicasDeleteRequest() // ReplicasDeleteRequest | 
};
apiInstance.replicapoolReplicasDelete(projectName, zone, poolName, replicaName, opts, (error, data, response) => {
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
 **projectName** | **String**| The project ID for this request. | 
 **zone** | **String**| The zone where the replica lives. | 
 **poolName** | **String**| The replica pool name for this request. | 
 **replicaName** | **String**| The name of the replica for this request. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **replicasDeleteRequest** | [**ReplicasDeleteRequest**](ReplicasDeleteRequest.md)|  | [optional] 

### Return type

[**Replica**](Replica.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## replicapoolReplicasGet

> Replica replicapoolReplicasGet(projectName, zone, poolName, replicaName, opts)



Gets information about a specific replica.

### Example

```javascript
import ReplicaPool from 'replica_pool';
let defaultClient = ReplicaPool.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ReplicaPool.ReplicasApi();
let projectName = "projectName_example"; // String | The project ID for this request.
let zone = "zone_example"; // String | The zone where the replica lives.
let poolName = "poolName_example"; // String | The replica pool name for this request.
let replicaName = "replicaName_example"; // String | The name of the replica for this request.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.replicapoolReplicasGet(projectName, zone, poolName, replicaName, opts, (error, data, response) => {
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
 **projectName** | **String**| The project ID for this request. | 
 **zone** | **String**| The zone where the replica lives. | 
 **poolName** | **String**| The replica pool name for this request. | 
 **replicaName** | **String**| The name of the replica for this request. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**Replica**](Replica.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## replicapoolReplicasList

> ReplicasListResponse replicapoolReplicasList(projectName, zone, poolName, opts)



Lists all replicas in a pool.

### Example

```javascript
import ReplicaPool from 'replica_pool';
let defaultClient = ReplicaPool.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ReplicaPool.ReplicasApi();
let projectName = "projectName_example"; // String | The project ID for this request.
let zone = "zone_example"; // String | The zone where the replica pool lives.
let poolName = "poolName_example"; // String | The replica pool name for this request.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'maxResults': 500, // Number | Maximum count of results to be returned. Acceptable values are 0 to 100, inclusive. (Default: 50)
  'pageToken': "pageToken_example" // String | Set this to the nextPageToken value returned by a previous list request to obtain the next page of results from the previous list request.
};
apiInstance.replicapoolReplicasList(projectName, zone, poolName, opts, (error, data, response) => {
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
 **projectName** | **String**| The project ID for this request. | 
 **zone** | **String**| The zone where the replica pool lives. | 
 **poolName** | **String**| The replica pool name for this request. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **maxResults** | **Number**| Maximum count of results to be returned. Acceptable values are 0 to 100, inclusive. (Default: 50) | [optional] [default to 500]
 **pageToken** | **String**| Set this to the nextPageToken value returned by a previous list request to obtain the next page of results from the previous list request. | [optional] 

### Return type

[**ReplicasListResponse**](ReplicasListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## replicapoolReplicasRestart

> Replica replicapoolReplicasRestart(projectName, zone, poolName, replicaName, opts)



Restarts a replica in a pool.

### Example

```javascript
import ReplicaPool from 'replica_pool';
let defaultClient = ReplicaPool.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ReplicaPool.ReplicasApi();
let projectName = "projectName_example"; // String | The project ID for this request.
let zone = "zone_example"; // String | The zone where the replica lives.
let poolName = "poolName_example"; // String | The replica pool name for this request.
let replicaName = "replicaName_example"; // String | The name of the replica for this request.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.replicapoolReplicasRestart(projectName, zone, poolName, replicaName, opts, (error, data, response) => {
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
 **projectName** | **String**| The project ID for this request. | 
 **zone** | **String**| The zone where the replica lives. | 
 **poolName** | **String**| The replica pool name for this request. | 
 **replicaName** | **String**| The name of the replica for this request. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**Replica**](Replica.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

