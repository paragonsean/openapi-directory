# ServiceFabricClientApis.ApplicationResourceApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApplicationResource**](ApplicationResourceApi.md#createApplicationResource) | **PUT** /Resources/Applications/{applicationResourceName} | Creates or updates an application resource.
[**deleteApplicationResource**](ApplicationResourceApi.md#deleteApplicationResource) | **DELETE** /Resources/Applications/{applicationResourceName} | Deletes the specified application.
[**getApplicationResource**](ApplicationResourceApi.md#getApplicationResource) | **GET** /Resources/Applications/{applicationResourceName} | Gets the application with the given name.
[**getReplica**](ApplicationResourceApi.md#getReplica) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/Replicas/{replicaName} | Gets a specific replica of a given service in an application resource.
[**getReplicas**](ApplicationResourceApi.md#getReplicas) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/replicas | Gets replicas of a given service in an application resource.
[**getService**](ApplicationResourceApi.md#getService) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName} | Gets the description of the specified service in an application resource.
[**getServices**](ApplicationResourceApi.md#getServices) | **GET** /Resources/Applications/{applicationResourceName}/Services | Gets all the services in the application resource.



## createApplicationResource

> createApplicationResource(apiVersion, applicationResourceName, applicationResourceDescription)

Creates or updates an application resource.

Creates an application with the specified name and description. If an application with the same name already exists, then its description are updated to the one indicated in this request.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
let applicationResourceDescription = new ServiceFabricClientApis.ApplicationResourceDescription(); // ApplicationResourceDescription | Description for creating an application resource.
apiInstance.createApplicationResource(apiVersion, applicationResourceName, applicationResourceDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **applicationResourceName** | **String**| Service Fabric application resource name. | 
 **applicationResourceDescription** | [**ApplicationResourceDescription**](ApplicationResourceDescription.md)| Description for creating an application resource. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteApplicationResource

> deleteApplicationResource(apiVersion, applicationResourceName)

Deletes the specified application.

Deletes the application identified by the name.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
apiInstance.deleteApplicationResource(apiVersion, applicationResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **applicationResourceName** | **String**| Service Fabric application resource name. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationResource

> ApplicationResourceDescription getApplicationResource(apiVersion, applicationResourceName)

Gets the application with the given name.

Gets the application with the given name. This includes the information about the application&#39;s services and other runtime information.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
apiInstance.getApplicationResource(apiVersion, applicationResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **applicationResourceName** | **String**| Service Fabric application resource name. | 

### Return type

[**ApplicationResourceDescription**](ApplicationResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReplica

> ServiceResourceReplicaDescription getReplica(apiVersion, applicationResourceName, serviceResourceName, replicaName)

Gets a specific replica of a given service in an application resource.

Gets the information about the specified replica of a given service of an application. The information includes the runtime properties of the replica instance.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
let serviceResourceName = "serviceResourceName_example"; // String | Service Fabric service resource name.
let replicaName = "replicaName_example"; // String | Service Fabric replica name.
apiInstance.getReplica(apiVersion, applicationResourceName, serviceResourceName, replicaName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **applicationResourceName** | **String**| Service Fabric application resource name. | 
 **serviceResourceName** | **String**| Service Fabric service resource name. | 
 **replicaName** | **String**| Service Fabric replica name. | 

### Return type

[**ServiceResourceReplicaDescription**](ServiceResourceReplicaDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReplicas

> PagedServiceResourceReplicaDescriptionList getReplicas(apiVersion, applicationResourceName, serviceResourceName)

Gets replicas of a given service in an application resource.

Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
let serviceResourceName = "serviceResourceName_example"; // String | Service Fabric service resource name.
apiInstance.getReplicas(apiVersion, applicationResourceName, serviceResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **applicationResourceName** | **String**| Service Fabric application resource name. | 
 **serviceResourceName** | **String**| Service Fabric service resource name. | 

### Return type

[**PagedServiceResourceReplicaDescriptionList**](PagedServiceResourceReplicaDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getService

> ServiceResourceDescription getService(apiVersion, applicationResourceName, serviceResourceName)

Gets the description of the specified service in an application resource.

Gets the description of the service resource.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
let serviceResourceName = "serviceResourceName_example"; // String | Service Fabric service resource name.
apiInstance.getService(apiVersion, applicationResourceName, serviceResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **applicationResourceName** | **String**| Service Fabric application resource name. | 
 **serviceResourceName** | **String**| Service Fabric service resource name. | 

### Return type

[**ServiceResourceDescription**](ServiceResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServices

> PagedServiceResourceDescriptionList getServices(apiVersion, applicationResourceName)

Gets all the services in the application resource.

The operation returns the service descriptions of all the services in the application resource. 

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ApplicationResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
apiInstance.getServices(apiVersion, applicationResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **applicationResourceName** | **String**| Service Fabric application resource name. | 

### Return type

[**PagedServiceResourceDescriptionList**](PagedServiceResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

