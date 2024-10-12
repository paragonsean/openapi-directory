# ServiceFabricClientApis.ChaosApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChaosReport**](ChaosApi.md#getChaosReport) | **GET** /Tools/Chaos/$/Report | Gets the next segment of the Chaos report based on the passed-in continuation token or the passed-in time-range.
[**startChaos**](ChaosApi.md#startChaos) | **POST** /Tools/Chaos/$/Start | Starts Chaos in the cluster.
[**stopChaos**](ChaosApi.md#stopChaos) | **POST** /Tools/Chaos/$/Stop | Stops Chaos in the cluster if it is already running, otherwise it does nothing.



## getChaosReport

> ChaosReport getChaosReport(apiVersion, opts)

Gets the next segment of the Chaos report based on the passed-in continuation token or the passed-in time-range.

You can either specify the ContinuationToken to get the next segment of the Chaos report or you can specify the time-range through StartTimeUtc and EndTimeUtc, but you cannot specify both the ContinuationToken and the time-range in the same call. When there are more than 100 Chaos events, the Chaos report is returned in segments where a segment contains no more than 100 Chaos events. 

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ChaosApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'startTimeUtc': "startTimeUtc_example", // String | The count of ticks representing the start time of the time range for which a Chaos report is to be generated. Please consult [DateTime.Ticks Property](https://msdn.microsoft.com/en-us/library/system.datetime.ticks%28v=vs.110%29) for details about tick.
  'endTimeUtc': "endTimeUtc_example", // String | The count of ticks representing the end time of the time range for which a Chaos report is to be generated. Please consult [DateTime.Ticks Property](https://msdn.microsoft.com/en-us/library/system.datetime.ticks%28v=vs.110%29) for details about tick.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getChaosReport(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **startTimeUtc** | **String**| The count of ticks representing the start time of the time range for which a Chaos report is to be generated. Please consult [DateTime.Ticks Property](https://msdn.microsoft.com/en-us/library/system.datetime.ticks%28v&#x3D;vs.110%29) for details about tick. | [optional] 
 **endTimeUtc** | **String**| The count of ticks representing the end time of the time range for which a Chaos report is to be generated. Please consult [DateTime.Ticks Property](https://msdn.microsoft.com/en-us/library/system.datetime.ticks%28v&#x3D;vs.110%29) for details about tick. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ChaosReport**](ChaosReport.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startChaos

> startChaos(apiVersion, chaosParameters, opts)

Starts Chaos in the cluster.

If Chaos is not already running in the cluster, it starts Chaos with the passed in Chaos parameters. If Chaos is already running when this call is made, the call fails with the error code FABRIC_E_CHAOS_ALREADY_RUNNING. Please refer to the article [Induce controlled Chaos in Service Fabric clusters](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-controlled-chaos) for more details. 

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ChaosApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let chaosParameters = new ServiceFabricClientApis.ChaosParameters(); // ChaosParameters | Describes all the parameters to configure a Chaos run.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.startChaos(apiVersion, chaosParameters, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **chaosParameters** | [**ChaosParameters**](ChaosParameters.md)| Describes all the parameters to configure a Chaos run. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopChaos

> stopChaos(apiVersion, opts)

Stops Chaos in the cluster if it is already running, otherwise it does nothing.

Stops Chaos from scheduling further faults; but, the in-flight faults are not affected.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ChaosApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.stopChaos(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

