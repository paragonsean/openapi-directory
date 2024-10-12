# AwsIoTThingsGraph.DefaultApi

All URIs are relative to *http://iotthingsgraph.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateEntityToThing**](DefaultApi.md#associateEntityToThing) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.AssociateEntityToThing | 
[**createFlowTemplate**](DefaultApi.md#createFlowTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.CreateFlowTemplate | 
[**createSystemInstance**](DefaultApi.md#createSystemInstance) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.CreateSystemInstance | 
[**createSystemTemplate**](DefaultApi.md#createSystemTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.CreateSystemTemplate | 
[**deleteFlowTemplate**](DefaultApi.md#deleteFlowTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DeleteFlowTemplate | 
[**deleteNamespace**](DefaultApi.md#deleteNamespace) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DeleteNamespace | 
[**deleteSystemInstance**](DefaultApi.md#deleteSystemInstance) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DeleteSystemInstance | 
[**deleteSystemTemplate**](DefaultApi.md#deleteSystemTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DeleteSystemTemplate | 
[**deploySystemInstance**](DefaultApi.md#deploySystemInstance) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DeploySystemInstance | 
[**deprecateFlowTemplate**](DefaultApi.md#deprecateFlowTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DeprecateFlowTemplate | 
[**deprecateSystemTemplate**](DefaultApi.md#deprecateSystemTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DeprecateSystemTemplate | 
[**describeNamespace**](DefaultApi.md#describeNamespace) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DescribeNamespace | 
[**dissociateEntityFromThing**](DefaultApi.md#dissociateEntityFromThing) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.DissociateEntityFromThing | 
[**getEntities**](DefaultApi.md#getEntities) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.GetEntities | 
[**getFlowTemplate**](DefaultApi.md#getFlowTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.GetFlowTemplate | 
[**getFlowTemplateRevisions**](DefaultApi.md#getFlowTemplateRevisions) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.GetFlowTemplateRevisions | 
[**getNamespaceDeletionStatus**](DefaultApi.md#getNamespaceDeletionStatus) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.GetNamespaceDeletionStatus | 
[**getSystemInstance**](DefaultApi.md#getSystemInstance) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.GetSystemInstance | 
[**getSystemTemplate**](DefaultApi.md#getSystemTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.GetSystemTemplate | 
[**getSystemTemplateRevisions**](DefaultApi.md#getSystemTemplateRevisions) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.GetSystemTemplateRevisions | 
[**getUploadStatus**](DefaultApi.md#getUploadStatus) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.GetUploadStatus | 
[**listFlowExecutionMessages**](DefaultApi.md#listFlowExecutionMessages) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.ListFlowExecutionMessages | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.ListTagsForResource | 
[**searchEntities**](DefaultApi.md#searchEntities) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.SearchEntities | 
[**searchFlowExecutions**](DefaultApi.md#searchFlowExecutions) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.SearchFlowExecutions | 
[**searchFlowTemplates**](DefaultApi.md#searchFlowTemplates) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.SearchFlowTemplates | 
[**searchSystemInstances**](DefaultApi.md#searchSystemInstances) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.SearchSystemInstances | 
[**searchSystemTemplates**](DefaultApi.md#searchSystemTemplates) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.SearchSystemTemplates | 
[**searchThings**](DefaultApi.md#searchThings) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.SearchThings | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.TagResource | 
[**undeploySystemInstance**](DefaultApi.md#undeploySystemInstance) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.UndeploySystemInstance | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.UntagResource | 
[**updateFlowTemplate**](DefaultApi.md#updateFlowTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.UpdateFlowTemplate | 
[**updateSystemTemplate**](DefaultApi.md#updateSystemTemplate) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.UpdateSystemTemplate | 
[**uploadEntityDefinitions**](DefaultApi.md#uploadEntityDefinitions) | **POST** /#X-Amz-Target&#x3D;IotThingsGraphFrontEndService.UploadEntityDefinitions | 



## associateEntityToThing

> Object associateEntityToThing(xAmzTarget, associateEntityToThingRequest, opts)



&lt;p&gt;Associates a device with a concrete thing that is in the user&#39;s registry.&lt;/p&gt; &lt;p&gt;A thing can be associated with only one device at a time. If you associate a thing with a new device id, its previous association will be removed.&lt;/p&gt;

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let associateEntityToThingRequest = new AwsIoTThingsGraph.AssociateEntityToThingRequest(); // AssociateEntityToThingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateEntityToThing(xAmzTarget, associateEntityToThingRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **associateEntityToThingRequest** | [**AssociateEntityToThingRequest**](AssociateEntityToThingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFlowTemplate

> CreateFlowTemplateResponse createFlowTemplate(xAmzTarget, createFlowTemplateRequest, opts)



Creates a workflow template. Workflows can be created only in the user&#39;s namespace. (The public namespace contains only entities.) The workflow can contain only entities in the specified namespace. The workflow is validated against the entities in the latest version of the user&#39;s namespace unless another namespace version is specified in the request.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createFlowTemplateRequest = new AwsIoTThingsGraph.CreateFlowTemplateRequest(); // CreateFlowTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFlowTemplate(xAmzTarget, createFlowTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **createFlowTemplateRequest** | [**CreateFlowTemplateRequest**](CreateFlowTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateFlowTemplateResponse**](CreateFlowTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSystemInstance

> CreateSystemInstanceResponse createSystemInstance(xAmzTarget, createSystemInstanceRequest, opts)



&lt;p&gt;Creates a system instance. &lt;/p&gt; &lt;p&gt;This action validates the system instance, prepares the deployment-related resources. For Greengrass deployments, it updates the Greengrass group that is specified by the &lt;code&gt;greengrassGroupName&lt;/code&gt; parameter. It also adds a file to the S3 bucket specified by the &lt;code&gt;s3BucketName&lt;/code&gt; parameter. You need to call &lt;code&gt;DeploySystemInstance&lt;/code&gt; after running this action.&lt;/p&gt; &lt;p&gt;For Greengrass deployments, since this action modifies and adds resources to a Greengrass group and an S3 bucket on the caller&#39;s behalf, the calling identity must have write permissions to both the specified Greengrass group and S3 bucket. Otherwise, the call will fail with an authorization error.&lt;/p&gt; &lt;p&gt;For cloud deployments, this action requires a &lt;code&gt;flowActionsRoleArn&lt;/code&gt; value. This is an IAM role that has permissions to access AWS services, such as AWS Lambda and AWS IoT, that the flow uses when it executes.&lt;/p&gt; &lt;p&gt;If the definition document doesn&#39;t specify a version of the user&#39;s namespace, the latest version will be used by default.&lt;/p&gt;

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createSystemInstanceRequest = new AwsIoTThingsGraph.CreateSystemInstanceRequest(); // CreateSystemInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSystemInstance(xAmzTarget, createSystemInstanceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **createSystemInstanceRequest** | [**CreateSystemInstanceRequest**](CreateSystemInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSystemInstanceResponse**](CreateSystemInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSystemTemplate

> CreateSystemTemplateResponse createSystemTemplate(xAmzTarget, createSystemTemplateRequest, opts)



Creates a system. The system is validated against the entities in the latest version of the user&#39;s namespace unless another namespace version is specified in the request.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createSystemTemplateRequest = new AwsIoTThingsGraph.CreateSystemTemplateRequest(); // CreateSystemTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSystemTemplate(xAmzTarget, createSystemTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **createSystemTemplateRequest** | [**CreateSystemTemplateRequest**](CreateSystemTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSystemTemplateResponse**](CreateSystemTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteFlowTemplate

> Object deleteFlowTemplate(xAmzTarget, deleteFlowTemplateRequest, opts)



Deletes a workflow. Any new system or deployment that contains this workflow will fail to update or deploy. Existing deployments that contain the workflow will continue to run (since they use a snapshot of the workflow taken at the time of deployment).

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteFlowTemplateRequest = new AwsIoTThingsGraph.DeleteFlowTemplateRequest(); // DeleteFlowTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteFlowTemplate(xAmzTarget, deleteFlowTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteFlowTemplateRequest** | [**DeleteFlowTemplateRequest**](DeleteFlowTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNamespace

> DeleteNamespaceResponse deleteNamespace(xAmzTarget, body, opts)



Deletes the specified namespace. This action deletes all of the entities in the namespace. Delete the systems and flows that use entities in the namespace before performing this action. This action takes no request parameters.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteNamespace(xAmzTarget, body, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteNamespaceResponse**](DeleteNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSystemInstance

> Object deleteSystemInstance(xAmzTarget, deleteSystemInstanceRequest, opts)



&lt;p&gt;Deletes a system instance. Only system instances that have never been deployed, or that have been undeployed can be deleted.&lt;/p&gt; &lt;p&gt;Users can create a new system instance that has the same ID as a deleted system instance.&lt;/p&gt;

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteSystemInstanceRequest = new AwsIoTThingsGraph.DeleteSystemInstanceRequest(); // DeleteSystemInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSystemInstance(xAmzTarget, deleteSystemInstanceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteSystemInstanceRequest** | [**DeleteSystemInstanceRequest**](DeleteSystemInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSystemTemplate

> Object deleteSystemTemplate(xAmzTarget, deleteSystemTemplateRequest, opts)



Deletes a system. New deployments can&#39;t contain the system after its deletion. Existing deployments that contain the system will continue to work because they use a snapshot of the system that is taken when it is deployed.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteSystemTemplateRequest = new AwsIoTThingsGraph.DeleteSystemTemplateRequest(); // DeleteSystemTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSystemTemplate(xAmzTarget, deleteSystemTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteSystemTemplateRequest** | [**DeleteSystemTemplateRequest**](DeleteSystemTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploySystemInstance

> DeploySystemInstanceResponse deploySystemInstance(xAmzTarget, deploySystemInstanceRequest, opts)



&lt;p&gt; &lt;b&gt;Greengrass and Cloud Deployments&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Deploys the system instance to the target specified in &lt;code&gt;CreateSystemInstance&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Greengrass Deployments&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If the system or any workflows and entities have been updated before this action is called, then the deployment will create a new Amazon Simple Storage Service resource file and then deploy it.&lt;/p&gt; &lt;p&gt;Since this action creates a Greengrass deployment on the caller&#39;s behalf, the calling identity must have write permissions to the specified Greengrass group. Otherwise, the call will fail with an authorization error.&lt;/p&gt; &lt;p&gt;For information about the artifacts that get added to your Greengrass core device when you use this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-greengrass.html\&quot;&gt;AWS IoT Things Graph and AWS IoT Greengrass&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deploySystemInstanceRequest = new AwsIoTThingsGraph.DeploySystemInstanceRequest(); // DeploySystemInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deploySystemInstance(xAmzTarget, deploySystemInstanceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deploySystemInstanceRequest** | [**DeploySystemInstanceRequest**](DeploySystemInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeploySystemInstanceResponse**](DeploySystemInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deprecateFlowTemplate

> Object deprecateFlowTemplate(xAmzTarget, deprecateFlowTemplateRequest, opts)



Deprecates the specified workflow. This action marks the workflow for deletion. Deprecated flows can&#39;t be deployed, but existing deployments will continue to run.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deprecateFlowTemplateRequest = new AwsIoTThingsGraph.DeprecateFlowTemplateRequest(); // DeprecateFlowTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deprecateFlowTemplate(xAmzTarget, deprecateFlowTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deprecateFlowTemplateRequest** | [**DeprecateFlowTemplateRequest**](DeprecateFlowTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deprecateSystemTemplate

> Object deprecateSystemTemplate(xAmzTarget, deprecateSystemTemplateRequest, opts)



Deprecates the specified system.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deprecateSystemTemplateRequest = new AwsIoTThingsGraph.DeprecateSystemTemplateRequest(); // DeprecateSystemTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deprecateSystemTemplate(xAmzTarget, deprecateSystemTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deprecateSystemTemplateRequest** | [**DeprecateSystemTemplateRequest**](DeprecateSystemTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeNamespace

> DescribeNamespaceResponse describeNamespace(xAmzTarget, describeNamespaceRequest, opts)



Gets the latest version of the user&#39;s namespace and the public version that it is tracking.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeNamespaceRequest = new AwsIoTThingsGraph.DescribeNamespaceRequest(); // DescribeNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeNamespace(xAmzTarget, describeNamespaceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **describeNamespaceRequest** | [**DescribeNamespaceRequest**](DescribeNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeNamespaceResponse**](DescribeNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dissociateEntityFromThing

> Object dissociateEntityFromThing(xAmzTarget, dissociateEntityFromThingRequest, opts)



Dissociates a device entity from a concrete thing. The action takes only the type of the entity that you need to dissociate because only one entity of a particular type can be associated with a thing.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let dissociateEntityFromThingRequest = new AwsIoTThingsGraph.DissociateEntityFromThingRequest(); // DissociateEntityFromThingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.dissociateEntityFromThing(xAmzTarget, dissociateEntityFromThingRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **dissociateEntityFromThingRequest** | [**DissociateEntityFromThingRequest**](DissociateEntityFromThingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getEntities

> GetEntitiesResponse getEntities(xAmzTarget, getEntitiesRequest, opts)



&lt;p&gt;Gets definitions of the specified entities. Uses the latest version of the user&#39;s namespace by default. This API returns the following TDM entities.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Properties&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;States&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Events&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Actions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Capabilities&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Mappings&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Devices&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device Models&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Services&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This action doesn&#39;t return definitions for systems, flows, and deployments.&lt;/p&gt;

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getEntitiesRequest = new AwsIoTThingsGraph.GetEntitiesRequest(); // GetEntitiesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEntities(xAmzTarget, getEntitiesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getEntitiesRequest** | [**GetEntitiesRequest**](GetEntitiesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEntitiesResponse**](GetEntitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getFlowTemplate

> GetFlowTemplateResponse getFlowTemplate(xAmzTarget, getFlowTemplateRequest, opts)



Gets the latest version of the &lt;code&gt;DefinitionDocument&lt;/code&gt; and &lt;code&gt;FlowTemplateSummary&lt;/code&gt; for the specified workflow.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getFlowTemplateRequest = new AwsIoTThingsGraph.GetFlowTemplateRequest(); // GetFlowTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFlowTemplate(xAmzTarget, getFlowTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getFlowTemplateRequest** | [**GetFlowTemplateRequest**](GetFlowTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFlowTemplateResponse**](GetFlowTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getFlowTemplateRevisions

> GetFlowTemplateRevisionsResponse getFlowTemplateRevisions(xAmzTarget, getFlowTemplateRevisionsRequest, opts)



Gets revisions of the specified workflow. Only the last 100 revisions are stored. If the workflow has been deprecated, this action will return revisions that occurred before the deprecation. This action won&#39;t work for workflows that have been deleted.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getFlowTemplateRevisionsRequest = new AwsIoTThingsGraph.GetFlowTemplateRevisionsRequest(); // GetFlowTemplateRevisionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getFlowTemplateRevisions(xAmzTarget, getFlowTemplateRevisionsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getFlowTemplateRevisionsRequest** | [**GetFlowTemplateRevisionsRequest**](GetFlowTemplateRevisionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetFlowTemplateRevisionsResponse**](GetFlowTemplateRevisionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getNamespaceDeletionStatus

> GetNamespaceDeletionStatusResponse getNamespaceDeletionStatus(xAmzTarget, body, opts)



Gets the status of a namespace deletion task.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getNamespaceDeletionStatus(xAmzTarget, body, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetNamespaceDeletionStatusResponse**](GetNamespaceDeletionStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSystemInstance

> GetSystemInstanceResponse getSystemInstance(xAmzTarget, getSystemInstanceRequest, opts)



Gets a system instance.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getSystemInstanceRequest = new AwsIoTThingsGraph.GetSystemInstanceRequest(); // GetSystemInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSystemInstance(xAmzTarget, getSystemInstanceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getSystemInstanceRequest** | [**GetSystemInstanceRequest**](GetSystemInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSystemInstanceResponse**](GetSystemInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSystemTemplate

> GetSystemTemplateResponse getSystemTemplate(xAmzTarget, getSystemTemplateRequest, opts)



Gets a system.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getSystemTemplateRequest = new AwsIoTThingsGraph.GetSystemTemplateRequest(); // GetSystemTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSystemTemplate(xAmzTarget, getSystemTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getSystemTemplateRequest** | [**GetSystemTemplateRequest**](GetSystemTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSystemTemplateResponse**](GetSystemTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSystemTemplateRevisions

> GetSystemTemplateRevisionsResponse getSystemTemplateRevisions(xAmzTarget, getSystemTemplateRevisionsRequest, opts)



Gets revisions made to the specified system template. Only the previous 100 revisions are stored. If the system has been deprecated, this action will return the revisions that occurred before its deprecation. This action won&#39;t work with systems that have been deleted.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getSystemTemplateRevisionsRequest = new AwsIoTThingsGraph.GetSystemTemplateRevisionsRequest(); // GetSystemTemplateRevisionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getSystemTemplateRevisions(xAmzTarget, getSystemTemplateRevisionsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getSystemTemplateRevisionsRequest** | [**GetSystemTemplateRevisionsRequest**](GetSystemTemplateRevisionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetSystemTemplateRevisionsResponse**](GetSystemTemplateRevisionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getUploadStatus

> GetUploadStatusResponse getUploadStatus(xAmzTarget, getUploadStatusRequest, opts)



Gets the status of the specified upload.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getUploadStatusRequest = new AwsIoTThingsGraph.GetUploadStatusRequest(); // GetUploadStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUploadStatus(xAmzTarget, getUploadStatusRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getUploadStatusRequest** | [**GetUploadStatusRequest**](GetUploadStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetUploadStatusResponse**](GetUploadStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listFlowExecutionMessages

> ListFlowExecutionMessagesResponse listFlowExecutionMessages(xAmzTarget, listFlowExecutionMessagesRequest, opts)



Returns a list of objects that contain information about events in a flow execution.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listFlowExecutionMessagesRequest = new AwsIoTThingsGraph.ListFlowExecutionMessagesRequest(); // ListFlowExecutionMessagesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listFlowExecutionMessages(xAmzTarget, listFlowExecutionMessagesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listFlowExecutionMessagesRequest** | [**ListFlowExecutionMessagesRequest**](ListFlowExecutionMessagesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListFlowExecutionMessagesResponse**](ListFlowExecutionMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Lists all tags on an AWS IoT Things Graph resource.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AwsIoTThingsGraph.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchEntities

> SearchEntitiesResponse searchEntities(xAmzTarget, searchEntitiesRequest, opts)



Searches for entities of the specified type. You can search for entities in your namespace and the public namespace that you&#39;re tracking.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let searchEntitiesRequest = new AwsIoTThingsGraph.SearchEntitiesRequest(); // SearchEntitiesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchEntities(xAmzTarget, searchEntitiesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **searchEntitiesRequest** | [**SearchEntitiesRequest**](SearchEntitiesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchEntitiesResponse**](SearchEntitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchFlowExecutions

> SearchFlowExecutionsResponse searchFlowExecutions(xAmzTarget, searchFlowExecutionsRequest, opts)



Searches for AWS IoT Things Graph workflow execution instances.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let searchFlowExecutionsRequest = new AwsIoTThingsGraph.SearchFlowExecutionsRequest(); // SearchFlowExecutionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchFlowExecutions(xAmzTarget, searchFlowExecutionsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **searchFlowExecutionsRequest** | [**SearchFlowExecutionsRequest**](SearchFlowExecutionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchFlowExecutionsResponse**](SearchFlowExecutionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchFlowTemplates

> SearchFlowTemplatesResponse searchFlowTemplates(xAmzTarget, searchFlowTemplatesRequest, opts)



Searches for summary information about workflows.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let searchFlowTemplatesRequest = new AwsIoTThingsGraph.SearchFlowTemplatesRequest(); // SearchFlowTemplatesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchFlowTemplates(xAmzTarget, searchFlowTemplatesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **searchFlowTemplatesRequest** | [**SearchFlowTemplatesRequest**](SearchFlowTemplatesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchFlowTemplatesResponse**](SearchFlowTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchSystemInstances

> SearchSystemInstancesResponse searchSystemInstances(xAmzTarget, searchSystemInstancesRequest, opts)



Searches for system instances in the user&#39;s account.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let searchSystemInstancesRequest = new AwsIoTThingsGraph.SearchSystemInstancesRequest(); // SearchSystemInstancesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchSystemInstances(xAmzTarget, searchSystemInstancesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **searchSystemInstancesRequest** | [**SearchSystemInstancesRequest**](SearchSystemInstancesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchSystemInstancesResponse**](SearchSystemInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchSystemTemplates

> SearchSystemTemplatesResponse searchSystemTemplates(xAmzTarget, searchSystemTemplatesRequest, opts)



Searches for summary information about systems in the user&#39;s account. You can filter by the ID of a workflow to return only systems that use the specified workflow.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let searchSystemTemplatesRequest = new AwsIoTThingsGraph.SearchSystemTemplatesRequest(); // SearchSystemTemplatesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchSystemTemplates(xAmzTarget, searchSystemTemplatesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **searchSystemTemplatesRequest** | [**SearchSystemTemplatesRequest**](SearchSystemTemplatesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchSystemTemplatesResponse**](SearchSystemTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchThings

> SearchThingsResponse searchThings(xAmzTarget, searchThingsRequest, opts)



&lt;p&gt;Searches for things associated with the specified entity. You can search by both device and device model.&lt;/p&gt; &lt;p&gt;For example, if two different devices, camera1 and camera2, implement the camera device model, the user can associate thing1 to camera1 and thing2 to camera2. &lt;code&gt;SearchThings(camera2)&lt;/code&gt; will return only thing2, but &lt;code&gt;SearchThings(camera)&lt;/code&gt; will return both thing1 and thing2.&lt;/p&gt; &lt;p&gt;This action searches for exact matches and doesn&#39;t perform partial text matching.&lt;/p&gt;

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let searchThingsRequest = new AwsIoTThingsGraph.SearchThingsRequest(); // SearchThingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchThings(xAmzTarget, searchThingsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **searchThingsRequest** | [**SearchThingsRequest**](SearchThingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchThingsResponse**](SearchThingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Creates a tag for the specified resource.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AwsIoTThingsGraph.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## undeploySystemInstance

> UndeploySystemInstanceResponse undeploySystemInstance(xAmzTarget, undeploySystemInstanceRequest, opts)



Removes a system instance from its target (Cloud or Greengrass).

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let undeploySystemInstanceRequest = new AwsIoTThingsGraph.UndeploySystemInstanceRequest(); // UndeploySystemInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.undeploySystemInstance(xAmzTarget, undeploySystemInstanceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **undeploySystemInstanceRequest** | [**UndeploySystemInstanceRequest**](UndeploySystemInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UndeploySystemInstanceResponse**](UndeploySystemInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(xAmzTarget, untagResourceRequest, opts)



Removes a tag from the specified resource.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AwsIoTThingsGraph.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateFlowTemplate

> UpdateFlowTemplateResponse updateFlowTemplate(xAmzTarget, updateFlowTemplateRequest, opts)



Updates the specified workflow. All deployed systems and system instances that use the workflow will see the changes in the flow when it is redeployed. If you don&#39;t want this behavior, copy the workflow (creating a new workflow with a different ID), and update the copy. The workflow can contain only entities in the specified namespace. 

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateFlowTemplateRequest = new AwsIoTThingsGraph.UpdateFlowTemplateRequest(); // UpdateFlowTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateFlowTemplate(xAmzTarget, updateFlowTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **updateFlowTemplateRequest** | [**UpdateFlowTemplateRequest**](UpdateFlowTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateFlowTemplateResponse**](UpdateFlowTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSystemTemplate

> UpdateSystemTemplateResponse updateSystemTemplate(xAmzTarget, updateSystemTemplateRequest, opts)



Updates the specified system. You don&#39;t need to run this action after updating a workflow. Any deployment that uses the system will see the changes in the system when it is redeployed.

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateSystemTemplateRequest = new AwsIoTThingsGraph.UpdateSystemTemplateRequest(); // UpdateSystemTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSystemTemplate(xAmzTarget, updateSystemTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **updateSystemTemplateRequest** | [**UpdateSystemTemplateRequest**](UpdateSystemTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSystemTemplateResponse**](UpdateSystemTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadEntityDefinitions

> UploadEntityDefinitionsResponse uploadEntityDefinitions(xAmzTarget, uploadEntityDefinitionsRequest, opts)



&lt;p&gt;Asynchronously uploads one or more entity definitions to the user&#39;s namespace. The &lt;code&gt;document&lt;/code&gt; parameter is required if &lt;code&gt;syncWithPublicNamespace&lt;/code&gt; and &lt;code&gt;deleteExistingEntites&lt;/code&gt; are false. If the &lt;code&gt;syncWithPublicNamespace&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt;, the user&#39;s namespace will synchronize with the latest version of the public namespace. If &lt;code&gt;deprecateExistingEntities&lt;/code&gt; is set to true, all entities in the latest version will be deleted before the new &lt;code&gt;DefinitionDocument&lt;/code&gt; is uploaded.&lt;/p&gt; &lt;p&gt;When a user uploads entity definitions for the first time, the service creates a new namespace for the user. The new namespace tracks the public namespace. Currently users can have only one namespace. The namespace version increments whenever a user uploads entity definitions that are backwards-incompatible and whenever a user sets the &lt;code&gt;syncWithPublicNamespace&lt;/code&gt; parameter or the &lt;code&gt;deprecateExistingEntities&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The IDs for all of the entities should be in URN format. Each entity must be in the user&#39;s namespace. Users can&#39;t create entities in the public namespace, but entity definitions can refer to entities in the public namespace.&lt;/p&gt; &lt;p&gt;Valid entities are &lt;code&gt;Device&lt;/code&gt;, &lt;code&gt;DeviceModel&lt;/code&gt;, &lt;code&gt;Service&lt;/code&gt;, &lt;code&gt;Capability&lt;/code&gt;, &lt;code&gt;State&lt;/code&gt;, &lt;code&gt;Action&lt;/code&gt;, &lt;code&gt;Event&lt;/code&gt;, &lt;code&gt;Property&lt;/code&gt;, &lt;code&gt;Mapping&lt;/code&gt;, &lt;code&gt;Enum&lt;/code&gt;. &lt;/p&gt;

### Example

```javascript
import AwsIoTThingsGraph from 'aws_io_t_things_graph';
let defaultClient = AwsIoTThingsGraph.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTThingsGraph.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let uploadEntityDefinitionsRequest = new AwsIoTThingsGraph.UploadEntityDefinitionsRequest(); // UploadEntityDefinitionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.uploadEntityDefinitions(xAmzTarget, uploadEntityDefinitionsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **uploadEntityDefinitionsRequest** | [**UploadEntityDefinitionsRequest**](UploadEntityDefinitionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UploadEntityDefinitionsResponse**](UploadEntityDefinitionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

