# GraphHopperDirectionsApi.MatrixAPIApi

All URIs are relative to *https://graphhopper.com/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculateMatrix**](MatrixAPIApi.md#calculateMatrix) | **POST** /matrix/calculate | Batch Matrix Endpoint
[**getMatrix**](MatrixAPIApi.md#getMatrix) | **GET** /matrix | GET Matrix Endpoint
[**getMatrixSolution**](MatrixAPIApi.md#getMatrixSolution) | **GET** /matrix/solution/{jobId} | GET Batch Matrix Endpoint
[**postMatrix**](MatrixAPIApi.md#postMatrix) | **POST** /matrix | POST Matrix Endpoint



## calculateMatrix

> JobId calculateMatrix(opts)

Batch Matrix Endpoint

Prefer the [synchronous endpoint](#operation/postMatrix) and use this Batch endpoint for long running problems only.  The Batch Matrix endpoint allows using matrices with more locations and works asynchronously - similar to the [Batch Route Optimization endpoint](#operation/asyncVRP):  * Create a HTTP POST request against &#x60;/matrix/calculate&#x60; and add the key in the URL: &#x60;/matrix/calculate?key&#x3D;[YOUR_KEY]&#x60;. This will give you the &#x60;job_id&#x60; from the response json like &#x60;{ \&quot;job_id\&quot;: \&quot;7ac65787-fb99-4e02-a832-2c3010c70097\&quot; }&#x60;  * Poll via HTTP GET requests every 500ms against &#x60;/matrix/solution/[job_id]&#x60;  Here are some full examples via curl: &#x60;&#x60;&#x60;bash $ curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/matrix/calculate?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;points\&quot;:[[13.29895,52.48696],[13.370876,52.489575],[13.439026,52.511206]]}&#39; {\&quot;job_id\&quot;:\&quot;7ac65787-fb99-4e02-a832-2c3010c70097\&quot;} &#x60;&#x60;&#x60;  Pick the returned &#x60;job_id&#x60; and use it in the next GET requests: &#x60;&#x60;&#x60;bash $ curl -X GET \&quot;https://graphhopper.com/api/1/matrix/solution/7ac65787-fb99-4e02-a832-2c3010c70097?key&#x3D;[YOUR_KEY]\&quot; {\&quot;status\&quot;:\&quot;waiting\&quot;} &#x60;&#x60;&#x60;  When the calculation is finished (&#x60;status:finished&#x60;) the JSON response will contain the full matrix JSON under &#x60;solution&#x60;: &#x60;&#x60;&#x60;bash $ curl -X GET \&quot;https://graphhopper.com/api/1/matrix/solution/7ac65787-fb99-4e02-a832-2c3010c70097?key&#x3D;[YOUR_KEY]\&quot; {\&quot;solution\&quot;:{\&quot;weights\&quot;:[[0.0,470.453,945.414],[503.793,0.0,580.871],[970.49,569.511,0.0]],\&quot;info\&quot;:{\&quot;copyrights\&quot;:[\&quot;GraphHopper\&quot;,\&quot;OpenStreetMap contributors\&quot;]}},\&quot;status\&quot;:\&quot;finished\&quot;} &#x60;&#x60;&#x60;  Please note that if an error occured while calculation the JSON will not have a status but contain directly the error message e.g.: &#x60;&#x60;&#x60;json {\&quot;message\&quot;:\&quot;Cannot find from_points: 1\&quot;} &#x60;&#x60;&#x60; And the optional &#x60;hints&#x60; array. 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.MatrixAPIApi();
let opts = {
  'postMatrixRequest': new GraphHopperDirectionsApi.PostMatrixRequest() // PostMatrixRequest | 
};
apiInstance.calculateMatrix(opts, (error, data, response) => {
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
 **postMatrixRequest** | [**PostMatrixRequest**](PostMatrixRequest.md)|  | [optional] 

### Return type

[**JobId**](JobId.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMatrix

> MatrixResponse getMatrix(opts)

GET Matrix Endpoint

With this Matrix Endpoint you submit the points and parameters via URL parameters and is the most convenient as it works out-of-the-box in the browser. If possible you should prefer using the [POST Matrix Endpoint](#operation/postMatrix) that avoids problems with many locations and can also gzip the **request**. (Note, that all endpoints return gzipped responses). 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.MatrixAPIApi();
let opts = {
  'point': ["null"], // [String] | Specify multiple points in `latitude,longitude` for which the weight-, route-, time- or distance-matrix should be calculated. In this case the starts are identical to the destinations. If there are N points, then NxN entries will be calculated. The order of the point parameter is important. Specify at least three points. Cannot be used together with from_point or to_point.
  'fromPoint': ["null"], // [String] | The starting points for the routes in `latitude,longitude`. E.g. if you want to calculate the three routes A-&gt;1, A-&gt;2, A-&gt;3 then you have one from_point parameter and three to_point parameters.
  'toPoint': ["null"], // [String] | The destination points for the routes in `latitude,longitude`.
  'pointHint': ["null"], // [String] | Optional parameter. Specifies a hint for each `point` parameter to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.
  'fromPointHint': ["null"], // [String] | For the from_point parameter. See point_hint
  'toPointHint': ["null"], // [String] | For the to_point parameter. See point_hint
  'snapPrevention': ["null"], // [String] | Optional parameter to avoid snapping to a certain road class or road environment. Current supported values `motorway`, `trunk`, `ferry`, `tunnel`, `bridge` and `ford`. Multiple values are specified like `snap_prevention=ferry&snap_prevention=motorway` 
  'curbside': ["null"], // [String] | Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.
  'fromCurbside': ["null"], // [String] | Curbside setting for the from_point parameter. See curbside.
  'toCurbside': ["null"], // [String] | Curbside setting for the to_point parameter. See curbside.
  'outArray': ["null"], // [String] | Specifies which arrays should be included in the response. Specify one or more of the following options 'weights', 'times', 'distances'. To specify more than one array use e.g. out_array=times&out_array=distances. The units of the entries of distances are meters, of times are seconds and of weights is arbitrary and it can differ for different vehicles or versions of this API.
  'vehicle': new GraphHopperDirectionsApi.VehicleProfileId(), // VehicleProfileId | The vehicle profile for which the matrix should be calculated.
  'failFast': true, // Boolean | Specifies whether or not the matrix calculation should return with an error as soon as possible in case some points cannot be found or some points are not connected. If set to `false` the time/weight/distance matrix will be calculated for all valid points and contain the `null` value for all entries that could not be calculated. The `hint` field of the response will also contain additional information about what went wrong (see its documentation).
  'turnCosts': false // Boolean | Specifies if turn restrictions should be considered. Enabling this option increases the matrix computation time. Only supported for motor vehicles and OpenStreetMap.
};
apiInstance.getMatrix(opts, (error, data, response) => {
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
 **point** | [**[String]**](String.md)| Specify multiple points in &#x60;latitude,longitude&#x60; for which the weight-, route-, time- or distance-matrix should be calculated. In this case the starts are identical to the destinations. If there are N points, then NxN entries will be calculated. The order of the point parameter is important. Specify at least three points. Cannot be used together with from_point or to_point. | [optional] 
 **fromPoint** | [**[String]**](String.md)| The starting points for the routes in &#x60;latitude,longitude&#x60;. E.g. if you want to calculate the three routes A-&amp;gt;1, A-&amp;gt;2, A-&amp;gt;3 then you have one from_point parameter and three to_point parameters. | [optional] 
 **toPoint** | [**[String]**](String.md)| The destination points for the routes in &#x60;latitude,longitude&#x60;. | [optional] 
 **pointHint** | [**[String]**](String.md)| Optional parameter. Specifies a hint for each &#x60;point&#x60; parameter to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up. | [optional] 
 **fromPointHint** | [**[String]**](String.md)| For the from_point parameter. See point_hint | [optional] 
 **toPointHint** | [**[String]**](String.md)| For the to_point parameter. See point_hint | [optional] 
 **snapPrevention** | [**[String]**](String.md)| Optional parameter to avoid snapping to a certain road class or road environment. Current supported values &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60;. Multiple values are specified like &#x60;snap_prevention&#x3D;ferry&amp;snap_prevention&#x3D;motorway&#x60;  | [optional] 
 **curbside** | [**[String]**](String.md)| Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap. | [optional] 
 **fromCurbside** | [**[String]**](String.md)| Curbside setting for the from_point parameter. See curbside. | [optional] 
 **toCurbside** | [**[String]**](String.md)| Curbside setting for the to_point parameter. See curbside. | [optional] 
 **outArray** | [**[String]**](String.md)| Specifies which arrays should be included in the response. Specify one or more of the following options &#39;weights&#39;, &#39;times&#39;, &#39;distances&#39;. To specify more than one array use e.g. out_array&#x3D;times&amp;out_array&#x3D;distances. The units of the entries of distances are meters, of times are seconds and of weights is arbitrary and it can differ for different vehicles or versions of this API. | [optional] 
 **vehicle** | [**VehicleProfileId**](.md)| The vehicle profile for which the matrix should be calculated. | [optional] 
 **failFast** | **Boolean**| Specifies whether or not the matrix calculation should return with an error as soon as possible in case some points cannot be found or some points are not connected. If set to &#x60;false&#x60; the time/weight/distance matrix will be calculated for all valid points and contain the &#x60;null&#x60; value for all entries that could not be calculated. The &#x60;hint&#x60; field of the response will also contain additional information about what went wrong (see its documentation). | [optional] [default to true]
 **turnCosts** | **Boolean**| Specifies if turn restrictions should be considered. Enabling this option increases the matrix computation time. Only supported for motor vehicles and OpenStreetMap. | [optional] [default to false]

### Return type

[**MatrixResponse**](MatrixResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMatrixSolution

> MatrixResponse getMatrixSolution(jobId)

GET Batch Matrix Endpoint

This endpoint returns the solution of a JSON submitted to the Batch Matrix endpoint. You can fetch it with the job_id, you have been sent. 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.MatrixAPIApi();
let jobId = "jobId_example"; // String | Request solution with jobId
apiInstance.getMatrixSolution(jobId, (error, data, response) => {
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

[**MatrixResponse**](MatrixResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postMatrix

> MatrixResponse postMatrix(opts)

POST Matrix Endpoint

 The [GET endpoint](#operation/getMatrix) has an URL length limitation, which hurts for many locations per request. In those cases use this POST endpoint with a JSON as input. The only parameter in the URL will be the key. Both request scenarios are identical except that all singular parameter names are named as their plural for a POST request. The effected parameters are: &#x60;points&#x60;, &#x60;from_points&#x60;, &#x60;to_points&#x60;, and &#x60;out_arrays&#x60;. For the remaining parameters please refer to the [guide of the GET endpoint](#operation/getMatrix).  **Please note that in contrast to GET endpoint the points have to be specified as &#x60;[longitude, latitude]&#x60; array (in that order, similar to [GeoJson](http://geojson.org/geojson-spec.html#examples))**.  For example the query &#x60;point&#x3D;10,11&amp;point&#x3D;20,22&amp;vehicle&#x3D;car&#x60; will be converted to the following JSON: &#x60;&#x60;&#x60;json { \&quot;points\&quot;: [[11,10], [22,20]], \&quot;vehicle\&quot;: \&quot;car\&quot; } &#x60;&#x60;&#x60;  A complete curl Example: &#x60;&#x60;&#x60;bash curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/matrix?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;elevation\&quot;:false,\&quot;out_arrays\&quot;:[\&quot;weights\&quot;, \&quot;times\&quot;],\&quot;from_points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697],[-0.171833,51.521241],[-0.211487,51.473685]],\&quot;to_points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697],[-0.171833,51.521241],[-0.211487,51.473685]],\&quot;vehicle\&quot;:\&quot;car\&quot;}&#39; &#x60;&#x60;&#x60; 

### Example

```javascript
import GraphHopperDirectionsApi from 'graph_hopper_directions_api';
let defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GraphHopperDirectionsApi.MatrixAPIApi();
let opts = {
  'postMatrixRequest': new GraphHopperDirectionsApi.PostMatrixRequest() // PostMatrixRequest | 
};
apiInstance.postMatrix(opts, (error, data, response) => {
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
 **postMatrixRequest** | [**PostMatrixRequest**](PostMatrixRequest.md)|  | [optional] 

### Return type

[**MatrixResponse**](MatrixResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

