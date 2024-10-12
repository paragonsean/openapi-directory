# ServiceFabricClientApis.MeshServiceReplicasApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meshServiceReplicaGet**](MeshServiceReplicasApi.md#meshServiceReplicaGet) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/Replicas/{replicaName} | Gets the given replica of the service of an application.
[**meshServiceReplicaList**](MeshServiceReplicasApi.md#meshServiceReplicaList) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/Replicas | Lists all the replicas of a service.



## meshServiceReplicaGet

> ServiceReplicaDescription meshServiceReplicaGet(apiVersion, applicationResourceName, serviceResourceName, replicaName)

Gets the given replica of the service of an application.

Gets the information about the service replica with the given name. The information include the description and other properties of the service replica.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshServiceReplicasApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
let serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
let replicaName = "replicaName_example"; // String | Service Fabric replica name.
apiInstance.meshServiceReplicaGet(apiVersion, applicationResourceName, serviceResourceName, replicaName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **applicationResourceName** | **String**| The identity of the application. | 
 **serviceResourceName** | **String**| The identity of the service. | 
 **replicaName** | **String**| Service Fabric replica name. | 

### Return type

[**ServiceReplicaDescription**](ServiceReplicaDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshServiceReplicaList

> PagedServiceReplicaDescriptionList meshServiceReplicaList(apiVersion, applicationResourceName, serviceResourceName)

Lists all the replicas of a service.

Gets the information about all replicas of a service. The information include the description and other properties of the service replica.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshServiceReplicasApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
let serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
apiInstance.meshServiceReplicaList(apiVersion, applicationResourceName, serviceResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **applicationResourceName** | **String**| The identity of the application. | 
 **serviceResourceName** | **String**| The identity of the service. | 

### Return type

[**PagedServiceReplicaDescriptionList**](PagedServiceReplicaDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

