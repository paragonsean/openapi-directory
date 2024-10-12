# TurbineLabsApi.ClusterApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusterClusterKeyDelete**](ClusterApi.md#clusterClusterKeyDelete) | **DELETE** /cluster/{clusterKey} | delete cluster
[**clusterClusterKeyGet**](ClusterApi.md#clusterClusterKeyGet) | **GET** /cluster/{clusterKey} | get cluster
[**clusterClusterKeyInstancesInstanceIdentifierDelete**](ClusterApi.md#clusterClusterKeyInstancesInstanceIdentifierDelete) | **DELETE** /cluster/{clusterKey}/instances/{instanceIdentifier} | remove instance
[**clusterClusterKeyInstancesPost**](ClusterApi.md#clusterClusterKeyInstancesPost) | **POST** /cluster/{clusterKey}/instances | add instance
[**clusterClusterKeyPut**](ClusterApi.md#clusterClusterKeyPut) | **PUT** /cluster/{clusterKey} | modify cluster
[**clusterGet**](ClusterApi.md#clusterGet) | **GET** /cluster | get clusters
[**clusterPost**](ClusterApi.md#clusterPost) | **POST** /cluster | create cluster



## clusterClusterKeyDelete

> Object clusterClusterKeyDelete(clusterKey, checksum)

delete cluster

Delete an existing cluster

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ClusterApi();
let clusterKey = "7ef80556-60bb-46bd-4cec-f4e2533aa75c"; // String | the cluster key
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the cluster to be deleted
apiInstance.clusterClusterKeyDelete(clusterKey, checksum, (error, data, response) => {
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
 **clusterKey** | **String**| the cluster key | 
 **checksum** | **String**| the current checksum of the cluster to be deleted | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterClusterKeyGet

> ClusterResult clusterClusterKeyGet(clusterKey)

get cluster

Get details for an existing cluster

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ClusterApi();
let clusterKey = "7ef80556-60bb-46bd-4cec-f4e2533aa75c"; // String | the cluster key
apiInstance.clusterClusterKeyGet(clusterKey, (error, data, response) => {
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
 **clusterKey** | **String**| the cluster key | 

### Return type

[**ClusterResult**](ClusterResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterClusterKeyInstancesInstanceIdentifierDelete

> Object clusterClusterKeyInstancesInstanceIdentifierDelete(checksum, clusterKey, instanceIdentifier)

remove instance

Remove an instance from a cluster

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ClusterApi();
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the instance to be deleted
let clusterKey = "7ef80556-60bb-46bd-4cec-f4e2533aa75c"; // String | the cluster to remove an instance from
let instanceIdentifier = "foo-1.useast.test.com:8080"; // String | the instance to remove, identified as <host>:<port>
apiInstance.clusterClusterKeyInstancesInstanceIdentifierDelete(checksum, clusterKey, instanceIdentifier, (error, data, response) => {
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
 **checksum** | **String**| the current checksum of the instance to be deleted | 
 **clusterKey** | **String**| the cluster to remove an instance from | 
 **instanceIdentifier** | **String**| the instance to remove, identified as &lt;host&gt;:&lt;port&gt; | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterClusterKeyInstancesPost

> InstanceResult clusterClusterKeyInstancesPost(clusterKey, instance)

add instance

Add a new instance to a cluster

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ClusterApi();
let clusterKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the cluster to add the instance to
let instance = new TurbineLabsApi.Instance(); // Instance | the instance to add
apiInstance.clusterClusterKeyInstancesPost(clusterKey, instance, (error, data, response) => {
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
 **clusterKey** | **String**| the cluster to add the instance to | 
 **instance** | [**Instance**](Instance.md)| the instance to add | 

### Return type

[**InstanceResult**](InstanceResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clusterClusterKeyPut

> ClusterResult clusterClusterKeyPut(clusterKey, cluster)

modify cluster

Modify an existing cluster

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ClusterApi();
let clusterKey = "5074fe62-821e-4034-55bd-b9caa09af2a1"; // String | the cluster key
let cluster = new TurbineLabsApi.Cluster(); // Cluster | the cluster to modify
apiInstance.clusterClusterKeyPut(clusterKey, cluster, (error, data, response) => {
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
 **clusterKey** | **String**| the cluster key | 
 **cluster** | [**Cluster**](Cluster.md)| the cluster to modify | 

### Return type

[**ClusterResult**](ClusterResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clusterGet

> MultiClusterResult clusterGet(opts)

get clusters

Get a list of clusters

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ClusterApi();
let opts = {
  'filters': "filters_example" // String | A JSON encoded array of ClusterFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ClusterFilter will be included. 
};
apiInstance.clusterGet(opts, (error, data, response) => {
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
 **filters** | **String**| A JSON encoded array of ClusterFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ClusterFilter will be included.  | [optional] 

### Return type

[**MultiClusterResult**](MultiClusterResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterPost

> ClusterResult clusterPost(cluster)

create cluster

Create a new cluster

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ClusterApi();
let cluster = new TurbineLabsApi.ClusterCreate(); // ClusterCreate | the cluster to create
apiInstance.clusterPost(cluster, (error, data, response) => {
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
 **cluster** | [**ClusterCreate**](ClusterCreate.md)| the cluster to create | 

### Return type

[**ClusterResult**](ClusterResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

