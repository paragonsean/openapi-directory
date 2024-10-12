# ServiceFabricClientApis.ReplicaApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeployedServiceReplicaDetailInfo**](ReplicaApi.md#getDeployedServiceReplicaDetailInfo) | **GET** /Nodes/{nodeName}/$/GetPartitions/{partitionId}/$/GetReplicas/{replicaId}/$/GetDetail | Gets the details of replica deployed on a Service Fabric node.
[**getDeployedServiceReplicaDetailInfoByPartitionId**](ReplicaApi.md#getDeployedServiceReplicaDetailInfoByPartitionId) | **GET** /Nodes/{nodeName}/$/GetPartitions/{partitionId}/$/GetReplicas | Gets the details of replica deployed on a Service Fabric node.
[**getDeployedServiceReplicaInfoList**](ReplicaApi.md#getDeployedServiceReplicaInfoList) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetReplicas | Gets the list of replicas deployed on a Service Fabric node.
[**getReplicaHealth**](ReplicaApi.md#getReplicaHealth) | **GET** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/GetHealth | Gets the health of a Service Fabric stateful service replica or stateless service instance.
[**getReplicaHealthUsingPolicy**](ReplicaApi.md#getReplicaHealthUsingPolicy) | **POST** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/GetHealth | Gets the health of a Service Fabric stateful service replica or stateless service instance using the specified policy.
[**getReplicaInfo**](ReplicaApi.md#getReplicaInfo) | **GET** /Partitions/{partitionId}/$/GetReplicas/{replicaId} | Gets the information about a replica of a Service Fabric partition.
[**getReplicaInfoList**](ReplicaApi.md#getReplicaInfoList) | **GET** /Partitions/{partitionId}/$/GetReplicas | Gets the information about replicas of a Service Fabric service partition.
[**removeReplica**](ReplicaApi.md#removeReplica) | **POST** /Nodes/{nodeName}/$/GetPartitions/{partitionId}/$/GetReplicas/{replicaId}/$/Delete | Removes a service replica running on a node.
[**reportReplicaHealth**](ReplicaApi.md#reportReplicaHealth) | **POST** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/ReportHealth | Sends a health report on the Service Fabric replica.
[**restartReplica**](ReplicaApi.md#restartReplica) | **POST** /Nodes/{nodeName}/$/GetPartitions/{partitionId}/$/GetReplicas/{replicaId}/$/Restart | Restarts a service replica of a persisted service running on a node.



## getDeployedServiceReplicaDetailInfo

> DeployedServiceReplicaDetailInfo getDeployedServiceReplicaDetailInfo(apiVersion, nodeName, partitionId, replicaId, opts)

Gets the details of replica deployed on a Service Fabric node.

Gets the details of the replica deployed on a Service Fabric node. The information includes service kind, service name, current service operation, current service operation start date time, partition ID, replica/instance ID, reported load, and other information.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nodeName = "nodeName_example"; // String | The name of the node.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let replicaId = "replicaId_example"; // String | The identifier of the replica.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getDeployedServiceReplicaDetailInfo(apiVersion, nodeName, partitionId, replicaId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nodeName** | **String**| The name of the node. | 
 **partitionId** | **String**| The identity of the partition. | 
 **replicaId** | **String**| The identifier of the replica. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**DeployedServiceReplicaDetailInfo**](DeployedServiceReplicaDetailInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployedServiceReplicaDetailInfoByPartitionId

> DeployedServiceReplicaDetailInfo getDeployedServiceReplicaDetailInfoByPartitionId(apiVersion, nodeName, partitionId, opts)

Gets the details of replica deployed on a Service Fabric node.

Gets the details of the replica deployed on a Service Fabric node. The information includes service kind, service name, current service operation, current service operation start date time, partition ID, replica/instance ID, reported load, and other information.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nodeName = "nodeName_example"; // String | The name of the node.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getDeployedServiceReplicaDetailInfoByPartitionId(apiVersion, nodeName, partitionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nodeName** | **String**| The name of the node. | 
 **partitionId** | **String**| The identity of the partition. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**DeployedServiceReplicaDetailInfo**](DeployedServiceReplicaDetailInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployedServiceReplicaInfoList

> [DeployedServiceReplicaInfo] getDeployedServiceReplicaInfoList(apiVersion, nodeName, applicationId, opts)

Gets the list of replicas deployed on a Service Fabric node.

Gets the list containing the information about replicas deployed on a Service Fabric node. The information include partition ID, replica ID, status of the replica, name of the service, name of the service type, and other information. Use PartitionId or ServiceManifestName query parameters to return information about the deployed replicas matching the specified values for those parameters.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nodeName = "nodeName_example"; // String | The name of the node.
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let opts = {
  'partitionId': "partitionId_example", // String | The identity of the partition.
  'serviceManifestName': "serviceManifestName_example", // String | The name of a service manifest registered as part of an application type in a Service Fabric cluster.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getDeployedServiceReplicaInfoList(apiVersion, nodeName, applicationId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nodeName** | **String**| The name of the node. | 
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **partitionId** | **String**| The identity of the partition. | [optional] 
 **serviceManifestName** | **String**| The name of a service manifest registered as part of an application type in a Service Fabric cluster. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**[DeployedServiceReplicaInfo]**](DeployedServiceReplicaInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReplicaHealth

> ReplicaHealth getReplicaHealth(apiVersion, partitionId, replicaId, opts)

Gets the health of a Service Fabric stateful service replica or stateless service instance.

Gets the health of a Service Fabric replica. Use EventsHealthStateFilter to filter the collection of health events reported on the replica based on the health state.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let replicaId = "replicaId_example"; // String | The identifier of the replica.
let opts = {
  'eventsHealthStateFilter': 0, // Number | Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values, obtained using the bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getReplicaHealth(apiVersion, partitionId, replicaId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **partitionId** | **String**| The identity of the partition. | 
 **replicaId** | **String**| The identifier of the replica. | 
 **eventsHealthStateFilter** | **Number**| Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values, obtained using the bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ReplicaHealth**](ReplicaHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReplicaHealthUsingPolicy

> ReplicaHealth getReplicaHealthUsingPolicy(apiVersion, partitionId, replicaId, opts)

Gets the health of a Service Fabric stateful service replica or stateless service instance using the specified policy.

Gets the health of a Service Fabric stateful service replica or stateless service instance. Use EventsHealthStateFilter to filter the collection of health events reported on the cluster based on the health state. Use ApplicationHealthPolicy to optionally override the health policies used to evaluate the health. This API only uses &#39;ConsiderWarningAsError&#39; field of the ApplicationHealthPolicy. The rest of the fields are ignored while evaluating the health of the replica.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let replicaId = "replicaId_example"; // String | The identifier of the replica.
let opts = {
  'eventsHealthStateFilter': 0, // Number | Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values, obtained using the bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'applicationHealthPolicy': new ServiceFabricClientApis.ApplicationHealthPolicy() // ApplicationHealthPolicy | Describes the health policies used to evaluate the health of an application or one of its children. If not present, the health evaluation uses the health policy from application manifest or the default health policy.
};
apiInstance.getReplicaHealthUsingPolicy(apiVersion, partitionId, replicaId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **partitionId** | **String**| The identity of the partition. | 
 **replicaId** | **String**| The identifier of the replica. | 
 **eventsHealthStateFilter** | **Number**| Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values, obtained using the bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md)| Describes the health policies used to evaluate the health of an application or one of its children. If not present, the health evaluation uses the health policy from application manifest or the default health policy. | [optional] 

### Return type

[**ReplicaHealth**](ReplicaHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReplicaInfo

> ReplicaInfo getReplicaInfo(apiVersion, partitionId, replicaId, opts)

Gets the information about a replica of a Service Fabric partition.

The response includes the ID, role, status, health, node name, uptime, and other details about the replica.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let replicaId = "replicaId_example"; // String | The identifier of the replica.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getReplicaInfo(apiVersion, partitionId, replicaId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **partitionId** | **String**| The identity of the partition. | 
 **replicaId** | **String**| The identifier of the replica. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ReplicaInfo**](ReplicaInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReplicaInfoList

> PagedReplicaInfoList getReplicaInfoList(apiVersion, partitionId, opts)

Gets the information about replicas of a Service Fabric service partition.

The GetReplicas endpoint returns information about the replicas of the specified partition. The response includes the ID, role, status, health, node name, uptime, and other details about the replica.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getReplicaInfoList(apiVersion, partitionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **partitionId** | **String**| The identity of the partition. | 
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedReplicaInfoList**](PagedReplicaInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeReplica

> removeReplica(apiVersion, nodeName, partitionId, replicaId, opts)

Removes a service replica running on a node.

This API simulates a Service Fabric replica failure by removing a replica from a Service Fabric cluster. The removal closes the replica, transitions the replica to the role None, and then removes all of the state information of the replica from the cluster. This API tests the replica state removal path, and simulates the report fault permanent path through client APIs. Warning - There are no safety checks performed when this API is used. Incorrect use of this API can lead to data loss for stateful services. In addition, the forceRemove flag impacts all other replicas hosted in the same process.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nodeName = "nodeName_example"; // String | The name of the node.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let replicaId = "replicaId_example"; // String | The identifier of the replica.
let opts = {
  'forceRemove': true, // Boolean | Remove a Service Fabric application or service forcefully without going through the graceful shutdown sequence. This parameter can be used to forcefully delete an application or service for which delete is timing out due to issues in the service code that prevents graceful close of replicas.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.removeReplica(apiVersion, nodeName, partitionId, replicaId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nodeName** | **String**| The name of the node. | 
 **partitionId** | **String**| The identity of the partition. | 
 **replicaId** | **String**| The identifier of the replica. | 
 **forceRemove** | **Boolean**| Remove a Service Fabric application or service forcefully without going through the graceful shutdown sequence. This parameter can be used to forcefully delete an application or service for which delete is timing out due to issues in the service code that prevents graceful close of replicas. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportReplicaHealth

> reportReplicaHealth(apiVersion, partitionId, replicaId, replicaHealthReportServiceKind, healthInformation, opts)

Sends a health report on the Service Fabric replica.

Reports health state of the specified Service Fabric replica. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway Replica, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, run GetReplicaHealth and check that the report appears in the HealthEvents section.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let replicaId = "replicaId_example"; // String | The identifier of the replica.
let replicaHealthReportServiceKind = "'Stateful'"; // String | The kind of service replica (Stateless or Stateful) for which the health is being reported. Following are the possible values.
let healthInformation = new ServiceFabricClientApis.HealthInformation(); // HealthInformation | Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager.
let opts = {
  'immediate': false, // Boolean | A flag that indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from HTTP Gateway to the health store, regardless of the fabric client settings that the HTTP Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the HTTP Gateway is closed or the message doesn't reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the HTTP Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.reportReplicaHealth(apiVersion, partitionId, replicaId, replicaHealthReportServiceKind, healthInformation, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **partitionId** | **String**| The identity of the partition. | 
 **replicaId** | **String**| The identifier of the replica. | 
 **replicaHealthReportServiceKind** | **String**| The kind of service replica (Stateless or Stateful) for which the health is being reported. Following are the possible values. | [default to &#39;Stateful&#39;]
 **healthInformation** | [**HealthInformation**](HealthInformation.md)| Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager. | 
 **immediate** | **Boolean**| A flag that indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from HTTP Gateway to the health store, regardless of the fabric client settings that the HTTP Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the HTTP Gateway is closed or the message doesn&#39;t reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the HTTP Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately. | [optional] [default to false]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restartReplica

> restartReplica(apiVersion, nodeName, partitionId, replicaId, opts)

Restarts a service replica of a persisted service running on a node.

Restarts a service replica of a persisted service running on a node. Warning - There are no safety checks performed when this API is used. Incorrect use of this API can lead to availability loss for stateful services.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ReplicaApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nodeName = "nodeName_example"; // String | The name of the node.
let partitionId = "partitionId_example"; // String | The identity of the partition.
let replicaId = "replicaId_example"; // String | The identifier of the replica.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.restartReplica(apiVersion, nodeName, partitionId, replicaId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nodeName** | **String**| The name of the node. | 
 **partitionId** | **String**| The identity of the partition. | 
 **replicaId** | **String**| The identifier of the replica. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

