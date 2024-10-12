# ServiceFabricClientApis.CodePackageApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeployedCodePackageInfoList**](CodePackageApi.md#getDeployedCodePackageInfoList) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetCodePackages | Gets the list of code packages deployed on a Service Fabric node.
[**restartDeployedCodePackage**](CodePackageApi.md#restartDeployedCodePackage) | **POST** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetCodePackages/$/Restart | Restarts a code package deployed on a Service Fabric node in a cluster.



## getDeployedCodePackageInfoList

> [DeployedCodePackageInfo] getDeployedCodePackageInfoList(apiVersion, nodeName, applicationId, opts)

Gets the list of code packages deployed on a Service Fabric node.

Gets the list of code packages deployed on a Service Fabric node for the given application.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.CodePackageApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let nodeName = "nodeName_example"; // String | The name of the node.
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let opts = {
  'serviceManifestName': "serviceManifestName_example", // String | The name of a service manifest registered as part of an application type in a Service Fabric cluster.
  'codePackageName': "codePackageName_example", // String | The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getDeployedCodePackageInfoList(apiVersion, nodeName, applicationId, opts, (error, data, response) => {
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
 **serviceManifestName** | **String**| The name of a service manifest registered as part of an application type in a Service Fabric cluster. | [optional] 
 **codePackageName** | **String**| The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**[DeployedCodePackageInfo]**](DeployedCodePackageInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restartDeployedCodePackage

> restartDeployedCodePackage(apiVersion, nodeName, applicationId, restartDeployedCodePackageDescription, opts)

Restarts a code package deployed on a Service Fabric node in a cluster.

Restarts a code package deployed on a Service Fabric node in a cluster. This aborts the code package process, which will restart all the user service replicas hosted in that process.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.CodePackageApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let nodeName = "nodeName_example"; // String | The name of the node.
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let restartDeployedCodePackageDescription = new ServiceFabricClientApis.RestartDeployedCodePackageDescription(); // RestartDeployedCodePackageDescription | Describes the deployed code package on Service Fabric node to restart.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.restartDeployedCodePackage(apiVersion, nodeName, applicationId, restartDeployedCodePackageDescription, opts, (error, data, response) => {
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
 **nodeName** | **String**| The name of the node. | 
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **restartDeployedCodePackageDescription** | [**RestartDeployedCodePackageDescription**](RestartDeployedCodePackageDescription.md)| Describes the deployed code package on Service Fabric node to restart. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

