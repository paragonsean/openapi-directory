# GraphHopperDirectionsApi.ClusterAPIApi

All URIs are relative to *https://graphhopper.com/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asyncClusteringProblem**](ClusterAPIApi.md#asyncClusteringProblem) | **POST** /cluster/calculate | Batch Cluster Endpoint
[**getClusterSolution**](ClusterAPIApi.md#getClusterSolution) | **GET** /cluster/solution/{jobId} | GET Batch Solution Endpoint
[**solveClusteringProblem**](ClusterAPIApi.md#solveClusteringProblem) | **POST** /cluster | POST Cluster Endpoint



## asyncClusteringProblem

> JobId asyncClusteringProblem(clusterRequest)

Batch Cluster Endpoint

 Prefer the [synchronous endpoint](#operation/solveClusteringProblem) and use this Batch Cluster endpoint for long running problems only. The work flow is asynchronous:  - send a POST request towards &#x60;https://graphhopper.com/api/1/cluster/calculate?key&#x3D;&lt;your_key&gt;&#x60; and fetch the job_id. - poll the solution every 500ms until it gives &#x60;status&#x3D;finished&#x60;. Do this with a GET request   towards &#x60;https://graphhopper.com/api/1/cluster/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt;&#x60;. 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.ClusterAPIApi();
let clusterRequest = new GraphHopperDirectionsApi.ClusterRequest(); // ClusterRequest | Request object that contains the problem to be solved
apiInstance.asyncClusteringProblem(clusterRequest, (error, data, response) => {
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
 **clusterRequest** | [**ClusterRequest**](ClusterRequest.md)| Request object that contains the problem to be solved | 

### Return type

[**JobId**](JobId.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getClusterSolution

> ClusterResponse getClusterSolution(jobId)

GET Batch Solution Endpoint

This endpoint returns the solution of the clustering problems submitted to the [Batch Cluster endpoint](#operation/asyncClusteringProblem). You can fetch it with the job_id, you have been sent. 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.ClusterAPIApi();
let jobId = "jobId_example"; // String | Request solution with jobId
apiInstance.getClusterSolution(jobId, (error, data, response) => {
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
 **jobId** | **String**| Request solution with jobId | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## solveClusteringProblem

> ClusterResponse solveClusteringProblem(clusterRequest)

POST Cluster Endpoint

 The Cluster endpoint is used with a POST request towards &#x60;https://graphhopper.com/api/1/cluster?key&#x3D;&lt;your_key&gt;&#x60;. The solution will be provided in the JSON response. Please note that for problems that take longer than 10 seconds a bad request error is returned. In this case please use the asynchronous [Batch Cluster Endpoint](#operation/asyncClusteringProblem) instead. 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.ClusterAPIApi();
let clusterRequest = new GraphHopperDirectionsApi.ClusterRequest(); // ClusterRequest | Request object that contains the problem to be solved
apiInstance.solveClusteringProblem(clusterRequest, (error, data, response) => {
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
 **clusterRequest** | [**ClusterRequest**](ClusterRequest.md)| Request object that contains the problem to be solved | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

