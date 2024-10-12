# ServiceFabricClientApis.EventsStoreApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApplicationEventList**](EventsStoreApi.md#getApplicationEventList) | **GET** /EventsStore/Applications/{applicationId}/$/Events | Gets an Application-related events.
[**getApplicationsEventList**](EventsStoreApi.md#getApplicationsEventList) | **GET** /EventsStore/Applications/Events | Gets all Applications-related events.
[**getClusterEventList**](EventsStoreApi.md#getClusterEventList) | **GET** /EventsStore/Cluster/Events | Gets all Cluster-related events.
[**getContainersEventList**](EventsStoreApi.md#getContainersEventList) | **GET** /EventsStore/Containers/Events | Gets all Containers-related events.
[**getCorrelatedEventList**](EventsStoreApi.md#getCorrelatedEventList) | **GET** /EventsStore/CorrelatedEvents/{eventInstanceId}/$/Events | Gets all correlated events for a given event.
[**getNodeEventList**](EventsStoreApi.md#getNodeEventList) | **GET** /EventsStore/Nodes/{nodeName}/$/Events | Gets a Node-related events.
[**getNodesEventList**](EventsStoreApi.md#getNodesEventList) | **GET** /EventsStore/Nodes/Events | Gets all Nodes-related Events.
[**getPartitionEventList**](EventsStoreApi.md#getPartitionEventList) | **GET** /EventsStore/Partitions/{partitionId}/$/Events | Gets a Partition-related events.
[**getPartitionReplicaEventList**](EventsStoreApi.md#getPartitionReplicaEventList) | **GET** /EventsStore/Partitions/{partitionId}/$/Replicas/{replicaId}/$/Events | Gets a Partition Replica-related events.
[**getPartitionReplicasEventList**](EventsStoreApi.md#getPartitionReplicasEventList) | **GET** /EventsStore/Partitions/{partitionId}/$/Replicas/Events | Gets all Replicas-related events for a Partition.
[**getPartitionsEventList**](EventsStoreApi.md#getPartitionsEventList) | **GET** /EventsStore/Partitions/Events | Gets all Partitions-related events.
[**getServiceEventList**](EventsStoreApi.md#getServiceEventList) | **GET** /EventsStore/Services/{serviceId}/$/Events | Gets a Service-related events.
[**getServicesEventList**](EventsStoreApi.md#getServicesEventList) | **GET** /EventsStore/Services/Events | Gets all Services-related events.



## getApplicationEventList

> [ApplicationEvent] getApplicationEventList(apiVersion, applicationId, startTimeUtc, endTimeUtc, opts)

Gets an Application-related events.

The response is list of ApplicationEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getApplicationEventList(apiVersion, applicationId, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[ApplicationEvent]**](ApplicationEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationsEventList

> [ApplicationEvent] getApplicationsEventList(apiVersion, startTimeUtc, endTimeUtc, opts)

Gets all Applications-related events.

The response is list of ApplicationEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getApplicationsEventList(apiVersion, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[ApplicationEvent]**](ApplicationEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClusterEventList

> [ClusterEvent] getClusterEventList(apiVersion, startTimeUtc, endTimeUtc, opts)

Gets all Cluster-related events.

The response is list of ClusterEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getClusterEventList(apiVersion, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[ClusterEvent]**](ClusterEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContainersEventList

> [ContainerInstanceEvent] getContainersEventList(apiVersion, startTimeUtc, endTimeUtc, opts)

Gets all Containers-related events.

The response is list of ContainerInstanceEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getContainersEventList(apiVersion, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[ContainerInstanceEvent]**](ContainerInstanceEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCorrelatedEventList

> [FabricEvent] getCorrelatedEventList(apiVersion, eventInstanceId, opts)

Gets all correlated events for a given event.

The response is list of FabricEvents.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let eventInstanceId = "eventInstanceId_example"; // String | The EventInstanceId.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getCorrelatedEventList(apiVersion, eventInstanceId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **eventInstanceId** | **String**| The EventInstanceId. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**[FabricEvent]**](FabricEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeEventList

> [NodeEvent] getNodeEventList(apiVersion, nodeName, startTimeUtc, endTimeUtc, opts)

Gets a Node-related events.

The response is list of NodeEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let nodeName = "nodeName_example"; // String | The name of the node.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getNodeEventList(apiVersion, nodeName, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **nodeName** | **String**| The name of the node. | 
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[NodeEvent]**](NodeEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodesEventList

> [NodeEvent] getNodesEventList(apiVersion, startTimeUtc, endTimeUtc, opts)

Gets all Nodes-related Events.

The response is list of NodeEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getNodesEventList(apiVersion, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[NodeEvent]**](NodeEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionEventList

> [PartitionEvent] getPartitionEventList(apiVersion, partitionId, startTimeUtc, endTimeUtc, opts)

Gets a Partition-related events.

The response is list of PartitionEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getPartitionEventList(apiVersion, partitionId, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **partitionId** | **String**| The identity of the partition. | 
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[PartitionEvent]**](PartitionEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionReplicaEventList

> [ReplicaEvent] getPartitionReplicaEventList(apiVersion, partitionId, replicaId, startTimeUtc, endTimeUtc, opts)

Gets a Partition Replica-related events.

The response is list of ReplicaEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let replicaId = "replicaId_example"; // String | The identifier of the replica.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getPartitionReplicaEventList(apiVersion, partitionId, replicaId, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **partitionId** | **String**| The identity of the partition. | 
 **replicaId** | **String**| The identifier of the replica. | 
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[ReplicaEvent]**](ReplicaEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionReplicasEventList

> [ReplicaEvent] getPartitionReplicasEventList(apiVersion, partitionId, startTimeUtc, endTimeUtc, opts)

Gets all Replicas-related events for a Partition.

The response is list of ReplicaEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getPartitionReplicasEventList(apiVersion, partitionId, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **partitionId** | **String**| The identity of the partition. | 
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[ReplicaEvent]**](ReplicaEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionsEventList

> [PartitionEvent] getPartitionsEventList(apiVersion, startTimeUtc, endTimeUtc, opts)

Gets all Partitions-related events.

The response is list of PartitionEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getPartitionsEventList(apiVersion, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[PartitionEvent]**](PartitionEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceEventList

> [ServiceEvent] getServiceEventList(apiVersion, serviceId, startTimeUtc, endTimeUtc, opts)

Gets a Service-related events.

The response is list of ServiceEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getServiceEventList(apiVersion, serviceId, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[ServiceEvent]**](ServiceEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServicesEventList

> [ServiceEvent] getServicesEventList(apiVersion, startTimeUtc, endTimeUtc, opts)

Gets all Services-related events.

The response is list of ServiceEvent objects.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.EventsStoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'eventsTypesFilter': "eventsTypesFilter_example", // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
  'excludeAnalysisEvents': true, // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
  'skipCorrelationLookup': true // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
};
apiInstance.getServicesEventList(apiVersion, startTimeUtc, endTimeUtc, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] 
 **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] 
 **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] 

### Return type

[**[ServiceEvent]**](ServiceEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

