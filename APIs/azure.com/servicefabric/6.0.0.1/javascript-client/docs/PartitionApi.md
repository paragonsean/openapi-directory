# ServiceFabricClientApis.PartitionApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPartitionHealth**](PartitionApi.md#getPartitionHealth) | **GET** /Partitions/{partitionId}/$/GetHealth | Gets the health of the specified Service Fabric partition.
[**getPartitionHealthUsingPolicy**](PartitionApi.md#getPartitionHealthUsingPolicy) | **POST** /Partitions/{partitionId}/$/GetHealth | Gets the health of the specified Service Fabric partition, by using the specified health policy.
[**getPartitionInfo**](PartitionApi.md#getPartitionInfo) | **GET** /Partitions/{partitionId} | Gets the information about a Service Fabric partition.
[**getPartitionInfoList**](PartitionApi.md#getPartitionInfoList) | **GET** /Services/{serviceId}/$/GetPartitions | Gets the list of partitions of a Service Fabric service.
[**getPartitionLoadInformation**](PartitionApi.md#getPartitionLoadInformation) | **GET** /Partitions/{partitionId}/$/GetLoadInformation | Gets the load of the specified Service Fabric partition.
[**getServiceNameInfo**](PartitionApi.md#getServiceNameInfo) | **GET** /Partitions/{partitionId}/$/GetServiceName | Gets the name of the Service Fabric service for a partition.
[**recoverAllPartitions**](PartitionApi.md#recoverAllPartitions) | **POST** /$/RecoverAllPartitions | Indicates to the Service Fabric cluster that it should attempt to recover any services (including system services) which are currently stuck in quorum loss.
[**recoverPartition**](PartitionApi.md#recoverPartition) | **POST** /Partitions/{partitionId}/$/Recover | Indicates to the Service Fabric cluster that it should attempt to recover a specific partition which is currently stuck in quorum loss.
[**recoverServicePartitions**](PartitionApi.md#recoverServicePartitions) | **POST** /Services/$/{serviceId}/$/GetPartitions/$/Recover | Indicates to the Service Fabric cluster that it should attempt to recover the specified service which is currently stuck in quorum loss.
[**recoverSystemPartitions**](PartitionApi.md#recoverSystemPartitions) | **POST** /$/RecoverSystemPartitions | Indicates to the Service Fabric cluster that it should attempt to recover the system services which are currently stuck in quorum loss.
[**reportPartitionHealth**](PartitionApi.md#reportPartitionHealth) | **POST** /Partitions/{partitionId}/$/ReportHealth | Sends a health report on the Service Fabric partition.
[**resetPartitionLoad**](PartitionApi.md#resetPartitionLoad) | **POST** /Partitions/{partitionId}/$/ResetLoad | Resets the current load of a Service Fabric partition.



## getPartitionHealth

> PartitionHealth getPartitionHealth(apiVersion, partitionId, opts)

Gets the health of the specified Service Fabric partition.

Gets the health information of the specified partition. Use EventsHealthStateFilter to filter the collection of health events reported on the service based on the health state. Use ReplicasHealthStateFilter to filter the collection of ReplicaHealthState objects on the partition. If you specify a partition that does not exist in the health store, this cmdlet returns an error. 

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let partitionId = "partitionId_example"; // String | The identity of the partition.
let opts = {
  'eventsHealthStateFilter': 0, // Number | Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
  'replicasHealthStateFilter': 0, // Number | Allows filtering the collection of ReplicaHealthState objects on the partition. The value can be obtained from members or bitwise operations on members of HealthStateFilter. Only replicas that match the filter will be returned. All replicas will be used to evaluate the aggregated health state. If not specified, all entries will be returned.The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) will be returned. The possible values for this parameter include integer value of one of the following health states.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
  'excludeHealthStatistics': false, // Boolean | Indicates whether the health statistics should be returned as part of the query result. False by default. The statistics show the number of children entities in health state Ok, Warning, and Error. 
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPartitionHealth(apiVersion, partitionId, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **eventsHealthStateFilter** | **Number**| Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.  | [optional] [default to 0]
 **replicasHealthStateFilter** | **Number**| Allows filtering the collection of ReplicaHealthState objects on the partition. The value can be obtained from members or bitwise operations on members of HealthStateFilter. Only replicas that match the filter will be returned. All replicas will be used to evaluate the aggregated health state. If not specified, all entries will be returned.The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) will be returned. The possible values for this parameter include integer value of one of the following health states.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.  | [optional] [default to 0]
 **excludeHealthStatistics** | **Boolean**| Indicates whether the health statistics should be returned as part of the query result. False by default. The statistics show the number of children entities in health state Ok, Warning, and Error.  | [optional] [default to false]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PartitionHealth**](PartitionHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionHealthUsingPolicy

> PartitionHealth getPartitionHealthUsingPolicy(apiVersion, partitionId, opts)

Gets the health of the specified Service Fabric partition, by using the specified health policy.

Gets the health information of the specified partition. If the application health policy is specified, the health evaluation uses it to get the aggregated health state. If the policy is not specified, the health evaluation uses the application health policy defined in the application manifest, or the default health policy, if no policy is defined in the manifest. Use EventsHealthStateFilter to filter the collection of health events reported on the partition based on the health state. Use ReplicasHealthStateFilter to filter the collection of ReplicaHealthState objects on the partition. Use ApplicationHealthPolicy in the POST body to override the health policies used to evaluate the health. If you specify a partition that does not exist in the health store, this cmdlet returns an error. 

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let partitionId = "partitionId_example"; // String | The identity of the partition.
let opts = {
  'eventsHealthStateFilter': 0, // Number | Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
  'replicasHealthStateFilter': 0, // Number | Allows filtering the collection of ReplicaHealthState objects on the partition. The value can be obtained from members or bitwise operations on members of HealthStateFilter. Only replicas that match the filter will be returned. All replicas will be used to evaluate the aggregated health state. If not specified, all entries will be returned.The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) will be returned. The possible values for this parameter include integer value of one of the following health states.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
  'excludeHealthStatistics': false, // Boolean | Indicates whether the health statistics should be returned as part of the query result. False by default. The statistics show the number of children entities in health state Ok, Warning, and Error. 
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'applicationHealthPolicy': new ServiceFabricClientApis.ApplicationHealthPolicy() // ApplicationHealthPolicy | Describes the health policies used to evaluate the health of an application or one of its children. If not present, the health evaluation uses the health policy from application manifest or the default health policy. 
};
apiInstance.getPartitionHealthUsingPolicy(apiVersion, partitionId, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **eventsHealthStateFilter** | **Number**| Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.  | [optional] [default to 0]
 **replicasHealthStateFilter** | **Number**| Allows filtering the collection of ReplicaHealthState objects on the partition. The value can be obtained from members or bitwise operations on members of HealthStateFilter. Only replicas that match the filter will be returned. All replicas will be used to evaluate the aggregated health state. If not specified, all entries will be returned.The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) will be returned. The possible values for this parameter include integer value of one of the following health states.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.  | [optional] [default to 0]
 **excludeHealthStatistics** | **Boolean**| Indicates whether the health statistics should be returned as part of the query result. False by default. The statistics show the number of children entities in health state Ok, Warning, and Error.  | [optional] [default to false]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md)| Describes the health policies used to evaluate the health of an application or one of its children. If not present, the health evaluation uses the health policy from application manifest or the default health policy.  | [optional] 

### Return type

[**PartitionHealth**](PartitionHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionInfo

> ServicePartitionInfo getPartitionInfo(apiVersion, partitionId, opts)

Gets the information about a Service Fabric partition.

The Partitions endpoint returns information about the specified partition. The response include the partition id, partitioning scheme information, keys supported by the partition, status, health and other details about the partition.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let partitionId = "partitionId_example"; // String | The identity of the partition.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPartitionInfo(apiVersion, partitionId, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ServicePartitionInfo**](ServicePartitionInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionInfoList

> PagedServicePartitionInfoList getPartitionInfoList(apiVersion, serviceId, opts)

Gets the list of partitions of a Service Fabric service.

Gets the list of partitions of a Service Fabric service. The response include the partition id, partitioning scheme information, keys supported by the partition, status, health and other details about the partition.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let serviceId = "serviceId_example"; // String | The identity of the service. This is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric://myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPartitionInfoList(apiVersion, serviceId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The identity of the service. This is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric://myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedServicePartitionInfoList**](PagedServicePartitionInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionLoadInformation

> PartitionLoadInformation getPartitionLoadInformation(apiVersion, partitionId, opts)

Gets the load of the specified Service Fabric partition.

Returns information about the specified partition. The response includes a list of load information. Each information includes load metric name, value and last reported time in UTC. 

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let partitionId = "partitionId_example"; // String | The identity of the partition.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPartitionLoadInformation(apiVersion, partitionId, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PartitionLoadInformation**](PartitionLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceNameInfo

> ServiceNameInfo getServiceNameInfo(apiVersion, partitionId, opts)

Gets the name of the Service Fabric service for a partition.

The GetServiceName endpoint returns the name of the service for the specified partition.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let partitionId = "partitionId_example"; // String | The identity of the partition.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getServiceNameInfo(apiVersion, partitionId, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ServiceNameInfo**](ServiceNameInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoverAllPartitions

> recoverAllPartitions(apiVersion, opts)

Indicates to the Service Fabric cluster that it should attempt to recover any services (including system services) which are currently stuck in quorum loss.

Indicates to the Service Fabric cluster that it should attempt to recover any services (including system services) which are currently stuck in quorum loss. This operation should only be performed if it is known that the replicas that are down cannot be recovered. Incorrect use of this API can cause potential data loss.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.recoverAllPartitions(apiVersion, opts, (error, data, response) => {
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


## recoverPartition

> recoverPartition(partitionId, apiVersion, opts)

Indicates to the Service Fabric cluster that it should attempt to recover a specific partition which is currently stuck in quorum loss.

Indicates to the Service Fabric cluster that it should attempt to recover a specific partition which is currently stuck in quorum loss. This operation should only be performed if it is known that the replicas that are down cannot be recovered. Incorrect use of this API can cause potential data loss.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.recoverPartition(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoverServicePartitions

> recoverServicePartitions(serviceId, apiVersion, opts)

Indicates to the Service Fabric cluster that it should attempt to recover the specified service which is currently stuck in quorum loss.

Indicates to the Service Fabric cluster that it should attempt to recover the specified service which is currently stuck in quorum loss. This operation should only be performed if it is known that the replicas that are down cannot be recovered. Incorrect use of this API can cause potential data loss.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let serviceId = "serviceId_example"; // String | The identity of the service. This is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric://myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.recoverServicePartitions(serviceId, apiVersion, opts, (error, data, response) => {
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
 **serviceId** | **String**| The identity of the service. This is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric://myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoverSystemPartitions

> recoverSystemPartitions(apiVersion, opts)

Indicates to the Service Fabric cluster that it should attempt to recover the system services which are currently stuck in quorum loss.

Indicates to the Service Fabric cluster that it should attempt to recover the system services which are currently stuck in quorum loss. This operation should only be performed if it is known that the replicas that are down cannot be recovered. Incorrect use of this API can cause potential data loss.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.recoverSystemPartitions(apiVersion, opts, (error, data, response) => {
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


## reportPartitionHealth

> reportPartitionHealth(apiVersion, partitionId, healthInformation, opts)

Sends a health report on the Service Fabric partition.

Reports health state of the specified Service Fabric partition. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway Partition, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, run GetPartitionHealth and check that the report appears in the HealthEvents section. 

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let partitionId = "partitionId_example"; // String | The identity of the partition.
let healthInformation = new ServiceFabricClientApis.HealthInformation(); // HealthInformation | Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager.
let opts = {
  'immediate': false, // Boolean | A flag which indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from Http Gateway to the health store, regardless of the fabric client settings that the Http Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the Http Gateway is closed or the message doesn't reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the Http Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately. 
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.reportPartitionHealth(apiVersion, partitionId, healthInformation, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **healthInformation** | [**HealthInformation**](HealthInformation.md)| Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager. | 
 **immediate** | **Boolean**| A flag which indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from Http Gateway to the health store, regardless of the fabric client settings that the Http Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the Http Gateway is closed or the message doesn&#39;t reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the Http Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately.  | [optional] [default to false]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetPartitionLoad

> resetPartitionLoad(partitionId, apiVersion, opts)

Resets the current load of a Service Fabric partition.

Resets the current load of a Service Fabric partition to the default load for the service.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PartitionApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.resetPartitionLoad(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

