# GraphHopperDirectionsApi.RouteOptimizationAPIApi

All URIs are relative to *https://graphhopper.com/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asyncVRP**](RouteOptimizationAPIApi.md#asyncVRP) | **POST** /vrp/optimize | POST route optimization problem (batch mode)
[**getSolution**](RouteOptimizationAPIApi.md#getSolution) | **GET** /vrp/solution/{jobId} | GET the solution (batch mode)
[**solveVRP**](RouteOptimizationAPIApi.md#solveVRP) | **POST** /vrp | POST route optimization problem



## asyncVRP

> JobId asyncVRP(request)

POST route optimization problem (batch mode)

 To solve a vehicle routing problem, perform the following steps:  1.) Make a HTTP POST to this URL  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/optimize?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  It returns a job id (job_id).  2.) Take the job id and fetch the solution for the vehicle routing problem from this URL:  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  We recommend to query the solution every 500ms until it returns &#39;status&#x3D;finished&#39;.  **Note**: Since the workflow is a bit more cumbersome and since you lose some time in fetching the solution, you should always prefer the [synchronous endpoint](#operation/solveVRP). You should use the batch mode only for long running problems. 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.RouteOptimizationAPIApi();
let request = new GraphHopperDirectionsApi.Request(); // Request | The request that contains the problem to be solved.
apiInstance.asyncVRP(request, (error, data, response) => {
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
 **request** | [**Request**](Request.md)| The request that contains the problem to be solved. | 

### Return type

[**JobId**](JobId.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSolution

> Response getSolution(jobId)

GET the solution (batch mode)

 Take the job id and fetch the solution for the vehicle routing problem from this URL:  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  You get the job id by sending a vehicle routing problem to the [batch mode URL](#operation/asyncVRP). 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.RouteOptimizationAPIApi();
let jobId = "jobId_example"; // String | Request solution with jobId
apiInstance.getSolution(jobId, (error, data, response) => {
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

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## solveVRP

> Response solveVRP(request)

POST route optimization problem

 To get started with the Route Optimization API, please read the [introduction](#tag/Route-Optimization-API).  To solve a new vehicle routing problem, make a HTTP POST to this URL  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  It returns the solution to this problem in the JSON response.  Please note that this URL is very well suited to solve minor problems. Larger vehicle routing problems, which take longer than 10 seconds to solve, cannot be solved. To solve them, please use the [batch mode URL](#operation/asyncVRP) instead. 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.RouteOptimizationAPIApi();
let request = new GraphHopperDirectionsApi.Request(); // Request | The request that contains the vehicle routing problem to be solved.
apiInstance.solveVRP(request, (error, data, response) => {
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
 **request** | [**Request**](Request.md)| The request that contains the vehicle routing problem to be solved. | 

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

