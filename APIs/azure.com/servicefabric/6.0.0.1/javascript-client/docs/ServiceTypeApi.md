# ServiceFabricClientApis.ServiceTypeApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeployedServiceTypeInfoByName**](ServiceTypeApi.md#getDeployedServiceTypeInfoByName) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServiceTypes/{serviceTypeName} | Gets the information about a specified service type of the application deployed on a node in a Service Fabric cluster.
[**getDeployedServiceTypeInfoList**](ServiceTypeApi.md#getDeployedServiceTypeInfoList) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServiceTypes | Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster.
[**getServiceManifest**](ServiceTypeApi.md#getServiceManifest) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetServiceManifest | Gets the manifest describing a service type.
[**getServiceTypeInfoList**](ServiceTypeApi.md#getServiceTypeInfoList) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetServiceTypes | Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster.



## getDeployedServiceTypeInfoByName

> [DeployedServiceTypeInfo] getDeployedServiceTypeInfoByName(apiVersion, nodeName, applicationId, serviceTypeName, opts)

Gets the information about a specified service type of the application deployed on a node in a Service Fabric cluster.

Gets the list containing the information about a specific service type from the applications deployed on a node in a Service Fabric cluster. The response includes the name of the service type, its registration status, the code package that registered it and activation id of the service package. Each entry represents one activation of a service type, differentiated by the activation id.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ServiceTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let nodeName = "nodeName_example"; // String | The name of the node.
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let serviceTypeName = "serviceTypeName_example"; // String | Specifies the name of a Service Fabric service type.
let opts = {
  'serviceManifestName': "serviceManifestName_example", // String | The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getDeployedServiceTypeInfoByName(apiVersion, nodeName, applicationId, serviceTypeName, opts, (error, data, response) => {
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
 **nodeName** | **String**| The name of the node. | 
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **serviceTypeName** | **String**| Specifies the name of a Service Fabric service type. | 
 **serviceManifestName** | **String**| The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**[DeployedServiceTypeInfo]**](DeployedServiceTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployedServiceTypeInfoList

> [DeployedServiceTypeInfo] getDeployedServiceTypeInfoList(apiVersion, nodeName, applicationId, opts)

Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster.

Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster. The response includes the name of the service type, its registration status, the code package that registered it and activation id of the service package.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ServiceTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let nodeName = "nodeName_example"; // String | The name of the node.
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let opts = {
  'serviceManifestName': "serviceManifestName_example", // String | The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getDeployedServiceTypeInfoList(apiVersion, nodeName, applicationId, opts, (error, data, response) => {
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
 **nodeName** | **String**| The name of the node. | 
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **serviceManifestName** | **String**| The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**[DeployedServiceTypeInfo]**](DeployedServiceTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceManifest

> ServiceTypeManifest getServiceManifest(apiVersion, applicationTypeName, applicationTypeVersion, serviceManifestName, opts)

Gets the manifest describing a service type.

Gets the manifest describing a service type. The response contains the service manifest XML as a string.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ServiceTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
let applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type.
let serviceManifestName = "serviceManifestName_example"; // String | The name of a service manifest registered as part of an application type in a Service Fabric cluster.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getServiceManifest(apiVersion, applicationTypeName, applicationTypeVersion, serviceManifestName, opts, (error, data, response) => {
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
 **applicationTypeName** | **String**| The name of the application type. | 
 **applicationTypeVersion** | **String**| The version of the application type. | 
 **serviceManifestName** | **String**| The name of a service manifest registered as part of an application type in a Service Fabric cluster. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ServiceTypeManifest**](ServiceTypeManifest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceTypeInfoList

> [ServiceTypeInfo] getServiceTypeInfoList(apiVersion, applicationTypeName, applicationTypeVersion, opts)

Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster.

Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster. The response includes the name of the service type, the name and version of the service manifest the type is defined in, kind (stateless or stateless) of the service type and other information about it.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ServiceTypeApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
let applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getServiceTypeInfoList(apiVersion, applicationTypeName, applicationTypeVersion, opts, (error, data, response) => {
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
 **applicationTypeName** | **String**| The name of the application type. | 
 **applicationTypeVersion** | **String**| The version of the application type. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**[ServiceTypeInfo]**](ServiceTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

