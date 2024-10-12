# AwsIoTGreengrassV2.DefaultApi

All URIs are relative to *http://greengrass.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateServiceRoleToAccount**](DefaultApi.md#associateServiceRoleToAccount) | **PUT** /greengrass/servicerole | 
[**batchAssociateClientDeviceWithCoreDevice**](DefaultApi.md#batchAssociateClientDeviceWithCoreDevice) | **POST** /greengrass/v2/coreDevices/{coreDeviceThingName}/associateClientDevices | 
[**batchDisassociateClientDeviceFromCoreDevice**](DefaultApi.md#batchDisassociateClientDeviceFromCoreDevice) | **POST** /greengrass/v2/coreDevices/{coreDeviceThingName}/disassociateClientDevices | 
[**cancelDeployment**](DefaultApi.md#cancelDeployment) | **POST** /greengrass/v2/deployments/{deploymentId}/cancel | 
[**createComponentVersion**](DefaultApi.md#createComponentVersion) | **POST** /greengrass/v2/createComponentVersion | 
[**createDeployment**](DefaultApi.md#createDeployment) | **POST** /greengrass/v2/deployments | 
[**deleteComponent**](DefaultApi.md#deleteComponent) | **DELETE** /greengrass/v2/components/{arn} | 
[**deleteCoreDevice**](DefaultApi.md#deleteCoreDevice) | **DELETE** /greengrass/v2/coreDevices/{coreDeviceThingName} | 
[**deleteDeployment**](DefaultApi.md#deleteDeployment) | **DELETE** /greengrass/v2/deployments/{deploymentId} | 
[**describeComponent**](DefaultApi.md#describeComponent) | **GET** /greengrass/v2/components/{arn}/metadata | 
[**disassociateServiceRoleFromAccount**](DefaultApi.md#disassociateServiceRoleFromAccount) | **DELETE** /greengrass/servicerole | 
[**getComponent**](DefaultApi.md#getComponent) | **GET** /greengrass/v2/components/{arn} | 
[**getComponentVersionArtifact**](DefaultApi.md#getComponentVersionArtifact) | **GET** /greengrass/v2/components/{arn}/artifacts/{artifactName} | 
[**getConnectivityInfo**](DefaultApi.md#getConnectivityInfo) | **GET** /greengrass/things/{thingName}/connectivityInfo | 
[**getCoreDevice**](DefaultApi.md#getCoreDevice) | **GET** /greengrass/v2/coreDevices/{coreDeviceThingName} | 
[**getDeployment**](DefaultApi.md#getDeployment) | **GET** /greengrass/v2/deployments/{deploymentId} | 
[**getServiceRoleForAccount**](DefaultApi.md#getServiceRoleForAccount) | **GET** /greengrass/servicerole | 
[**listClientDevicesAssociatedWithCoreDevice**](DefaultApi.md#listClientDevicesAssociatedWithCoreDevice) | **GET** /greengrass/v2/coreDevices/{coreDeviceThingName}/associatedClientDevices | 
[**listComponentVersions**](DefaultApi.md#listComponentVersions) | **GET** /greengrass/v2/components/{arn}/versions | 
[**listComponents**](DefaultApi.md#listComponents) | **GET** /greengrass/v2/components | 
[**listCoreDevices**](DefaultApi.md#listCoreDevices) | **GET** /greengrass/v2/coreDevices | 
[**listDeployments**](DefaultApi.md#listDeployments) | **GET** /greengrass/v2/deployments | 
[**listEffectiveDeployments**](DefaultApi.md#listEffectiveDeployments) | **GET** /greengrass/v2/coreDevices/{coreDeviceThingName}/effectiveDeployments | 
[**listInstalledComponents**](DefaultApi.md#listInstalledComponents) | **GET** /greengrass/v2/coreDevices/{coreDeviceThingName}/installedComponents | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**resolveComponentCandidates**](DefaultApi.md#resolveComponentCandidates) | **POST** /greengrass/v2/resolveComponentCandidates | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateConnectivityInfo**](DefaultApi.md#updateConnectivityInfo) | **PUT** /greengrass/things/{thingName}/connectivityInfo | 



## associateServiceRoleToAccount

> AssociateServiceRoleToAccountResponse associateServiceRoleToAccount(associateServiceRoleToAccountRequest, opts)



Associates a Greengrass service role with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. IoT Greengrass uses this role to verify the identity of client devices and manage core device connectivity information. The role must include the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/iam/home#/policies/arn:awsiam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy\&quot;&gt;AWSGreengrassResourceAccessRolePolicy&lt;/a&gt; managed policy or a custom policy that defines equivalent permissions for the IoT Greengrass features that you use. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html\&quot;&gt;Greengrass service role&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let associateServiceRoleToAccountRequest = new AwsIoTGreengrassV2.AssociateServiceRoleToAccountRequest(); // AssociateServiceRoleToAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateServiceRoleToAccount(associateServiceRoleToAccountRequest, opts, (error, data, response) => {
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
 **associateServiceRoleToAccountRequest** | [**AssociateServiceRoleToAccountRequest**](AssociateServiceRoleToAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateServiceRoleToAccountResponse**](AssociateServiceRoleToAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchAssociateClientDeviceWithCoreDevice

> BatchAssociateClientDeviceWithCoreDeviceResponse batchAssociateClientDeviceWithCoreDevice(coreDeviceThingName, batchAssociateClientDeviceWithCoreDeviceRequest, opts)



&lt;p&gt;Associates a list of client devices with a core device. Use this API operation to specify which client devices can discover a core device through cloud discovery. With cloud discovery, client devices connect to IoT Greengrass to retrieve associated core devices&#39; connectivity information and certificates. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-cloud-discovery.html\&quot;&gt;Configure cloud discovery&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Client devices are local IoT devices that connect to and communicate with an IoT Greengrass core device over MQTT. You can connect client devices to a core device to sync MQTT messages and data to Amazon Web Services IoT Core and interact with client devices in Greengrass components. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/interact-with-local-iot-devices.html\&quot;&gt;Interact with local IoT devices&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let coreDeviceThingName = "coreDeviceThingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let batchAssociateClientDeviceWithCoreDeviceRequest = new AwsIoTGreengrassV2.BatchAssociateClientDeviceWithCoreDeviceRequest(); // BatchAssociateClientDeviceWithCoreDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchAssociateClientDeviceWithCoreDevice(coreDeviceThingName, batchAssociateClientDeviceWithCoreDeviceRequest, opts, (error, data, response) => {
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
 **coreDeviceThingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **batchAssociateClientDeviceWithCoreDeviceRequest** | [**BatchAssociateClientDeviceWithCoreDeviceRequest**](BatchAssociateClientDeviceWithCoreDeviceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchAssociateClientDeviceWithCoreDeviceResponse**](BatchAssociateClientDeviceWithCoreDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDisassociateClientDeviceFromCoreDevice

> BatchDisassociateClientDeviceFromCoreDeviceResponse batchDisassociateClientDeviceFromCoreDevice(coreDeviceThingName, batchDisassociateClientDeviceFromCoreDeviceRequest, opts)



Disassociates a list of client devices from a core device. After you disassociate a client device from a core device, the client device won&#39;t be able to use cloud discovery to retrieve the core device&#39;s connectivity information and certificates.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let coreDeviceThingName = "coreDeviceThingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let batchDisassociateClientDeviceFromCoreDeviceRequest = new AwsIoTGreengrassV2.BatchDisassociateClientDeviceFromCoreDeviceRequest(); // BatchDisassociateClientDeviceFromCoreDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDisassociateClientDeviceFromCoreDevice(coreDeviceThingName, batchDisassociateClientDeviceFromCoreDeviceRequest, opts, (error, data, response) => {
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
 **coreDeviceThingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **batchDisassociateClientDeviceFromCoreDeviceRequest** | [**BatchDisassociateClientDeviceFromCoreDeviceRequest**](BatchDisassociateClientDeviceFromCoreDeviceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDisassociateClientDeviceFromCoreDeviceResponse**](BatchDisassociateClientDeviceFromCoreDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelDeployment

> CancelDeploymentResponse cancelDeployment(deploymentId, opts)



Cancels a deployment. This operation cancels the deployment for devices that haven&#39;t yet received it. If a device already received the deployment, this operation doesn&#39;t change anything for that device.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let deploymentId = "deploymentId_example"; // String | The ID of the deployment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelDeployment(deploymentId, opts, (error, data, response) => {
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
 **deploymentId** | **String**| The ID of the deployment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CancelDeploymentResponse**](CancelDeploymentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createComponentVersion

> CreateComponentVersionResponse createComponentVersion(createComponentVersionRequest, opts)



&lt;p&gt;Creates a component. Components are software that run on Greengrass core devices. After you develop and test a component on your core device, you can use this operation to upload your component to IoT Greengrass. Then, you can deploy the component to other core devices.&lt;/p&gt; &lt;p&gt;You can use this operation to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Create components from recipes&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Create a component from a recipe, which is a file that defines the component&#39;s metadata, parameters, dependencies, lifecycle, artifacts, and platform capability. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html\&quot;&gt;IoT Greengrass component recipe reference&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To create a component from a recipe, specify &lt;code&gt;inlineRecipe&lt;/code&gt; when you call this operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Create components from Lambda functions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Create a component from an Lambda function that runs on IoT Greengrass. This creates a recipe and artifacts from the Lambda function&#39;s deployment package. You can use this operation to migrate Lambda functions from IoT Greengrass V1 to IoT Greengrass V2.&lt;/p&gt; &lt;p&gt;This function only accepts Lambda functions that use the following runtimes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Python 2.7 – &lt;code&gt;python2.7&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Python 3.7 – &lt;code&gt;python3.7&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Python 3.8 – &lt;code&gt;python3.8&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Python 3.9 – &lt;code&gt;python3.9&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Java 8 – &lt;code&gt;java8&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Java 11 – &lt;code&gt;java11&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Node.js 10 – &lt;code&gt;nodejs10.x&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Node.js 12 – &lt;code&gt;nodejs12.x&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Node.js 14 – &lt;code&gt;nodejs14.x&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To create a component from a Lambda function, specify &lt;code&gt;lambdaFunction&lt;/code&gt; when you call this operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IoT Greengrass currently supports Lambda functions on only Linux core devices.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let createComponentVersionRequest = new AwsIoTGreengrassV2.CreateComponentVersionRequest(); // CreateComponentVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createComponentVersion(createComponentVersionRequest, opts, (error, data, response) => {
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
 **createComponentVersionRequest** | [**CreateComponentVersionRequest**](CreateComponentVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateComponentVersionResponse**](CreateComponentVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDeployment

> CreateDeploymentResponse createDeployment(createDeploymentRequest, opts)



&lt;p&gt;Creates a continuous deployment for a target, which is a Greengrass core device or group of core devices. When you add a new core device to a group of core devices that has a deployment, IoT Greengrass deploys that group&#39;s deployment to the new device.&lt;/p&gt; &lt;p&gt;You can define one deployment for each target. When you create a new deployment for a target that has an existing deployment, you replace the previous deployment. IoT Greengrass applies the new deployment to the target devices.&lt;/p&gt; &lt;p&gt;Every deployment has a revision number that indicates how many deployment revisions you define for a target. Use this operation to create a new revision of an existing deployment.&lt;/p&gt; &lt;p&gt;For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html\&quot;&gt;Create deployments&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let createDeploymentRequest = new AwsIoTGreengrassV2.CreateDeploymentRequest(); // CreateDeploymentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDeployment(createDeploymentRequest, opts, (error, data, response) => {
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
 **createDeploymentRequest** | [**CreateDeploymentRequest**](CreateDeploymentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDeploymentResponse**](CreateDeploymentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteComponent

> deleteComponent(arn, opts)



&lt;p&gt;Deletes a version of a component from IoT Greengrass.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation deletes the component&#39;s recipe and artifacts. As a result, deployments that refer to this component version will fail. If you have deployments that use this component version, you can remove the component from the deployment or update the deployment to use a valid version.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let arn = "arn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteComponent(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component version. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCoreDevice

> deleteCoreDevice(coreDeviceThingName, opts)



Deletes a Greengrass core device, which is an IoT thing. This operation removes the core device from the list of core devices. This operation doesn&#39;t delete the IoT thing. For more information about how to delete the IoT thing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThing.html\&quot;&gt;DeleteThing&lt;/a&gt; in the &lt;i&gt;IoT API Reference&lt;/i&gt;.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let coreDeviceThingName = "coreDeviceThingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCoreDevice(coreDeviceThingName, opts, (error, data, response) => {
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
 **coreDeviceThingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDeployment

> deleteDeployment(deploymentId, opts)



&lt;p&gt;Deletes a deployment. To delete an active deployment, you must first cancel it. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_CancelDeployment.html\&quot;&gt;CancelDeployment&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deleting a deployment doesn&#39;t affect core devices that run that deployment, because core devices store the deployment&#39;s configuration on the device. Additionally, core devices can roll back to a previous deployment that has been deleted.&lt;/p&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let deploymentId = "deploymentId_example"; // String | The ID of the deployment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDeployment(deploymentId, opts, (error, data, response) => {
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
 **deploymentId** | **String**| The ID of the deployment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeComponent

> DescribeComponentResponse describeComponent(arn, opts)



Retrieves metadata for a version of a component.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let arn = "arn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeComponent(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component version. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeComponentResponse**](DescribeComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateServiceRoleFromAccount

> DisassociateServiceRoleFromAccountResponse disassociateServiceRoleFromAccount(opts)



Disassociates the Greengrass service role from IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. Without a service role, IoT Greengrass can&#39;t verify the identity of client devices or manage core device connectivity information. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html\&quot;&gt;Greengrass service role&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateServiceRoleFromAccount(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateServiceRoleFromAccountResponse**](DisassociateServiceRoleFromAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComponent

> GetComponentResponse getComponent(arn, opts)



Gets the recipe for a version of a component.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let arn = "arn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'recipeOutputFormat': "recipeOutputFormat_example" // String | The format of the recipe.
};
apiInstance.getComponent(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component version. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **recipeOutputFormat** | **String**| The format of the recipe. | [optional] 

### Return type

[**GetComponentResponse**](GetComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComponentVersionArtifact

> GetComponentVersionArtifactResponse getComponentVersionArtifact(arn, artifactName, opts)



Gets the pre-signed URL to download a public or a Lambda component artifact. Core devices call this operation to identify the URL that they can use to download an artifact to install.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let arn = "arn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version. Specify the ARN of a public or a Lambda component version.
let artifactName = "artifactName_example"; // String | <p>The name of the artifact.</p> <p>You can use the <a href=\"https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html\">GetComponent</a> operation to download the component recipe, which includes the URI of the artifact. The artifact name is the section of the URI after the scheme. For example, in the artifact URI <code>greengrass:SomeArtifact.zip</code>, the artifact name is <code>SomeArtifact.zip</code>.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getComponentVersionArtifact(arn, artifactName, opts, (error, data, response) => {
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
 **arn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component version. Specify the ARN of a public or a Lambda component version. | 
 **artifactName** | **String**| &lt;p&gt;The name of the artifact.&lt;/p&gt; &lt;p&gt;You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html\&quot;&gt;GetComponent&lt;/a&gt; operation to download the component recipe, which includes the URI of the artifact. The artifact name is the section of the URI after the scheme. For example, in the artifact URI &lt;code&gt;greengrass:SomeArtifact.zip&lt;/code&gt;, the artifact name is &lt;code&gt;SomeArtifact.zip&lt;/code&gt;.&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetComponentVersionArtifactResponse**](GetComponentVersionArtifactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConnectivityInfo

> GetConnectivityInfoResponse getConnectivityInfo(thingName, opts)



&lt;p&gt;Retrieves connectivity information for a Greengrass core device.&lt;/p&gt; &lt;p&gt;Connectivity information includes endpoints and ports where client devices can connect to an MQTT broker on the core device. When a client device calls the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-discover-api.html\&quot;&gt;IoT Greengrass discovery API&lt;/a&gt;, IoT Greengrass returns connectivity information for all of the core devices where the client device can connect. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/connect-client-devices.html\&quot;&gt;Connect client devices to core devices&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let thingName = "thingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConnectivityInfo(thingName, opts, (error, data, response) => {
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
 **thingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetConnectivityInfoResponse**](GetConnectivityInfoResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCoreDevice

> GetCoreDeviceResponse getCoreDevice(coreDeviceThingName, opts)



&lt;p&gt;Retrieves metadata for a Greengrass core device.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn&#39;t running on the device, or if device isn&#39;t connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.&lt;/p&gt; &lt;p&gt;Core devices send status updates at the following times:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When the IoT Greengrass Core software starts&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the core device receives a deployment from the Amazon Web Services Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the status of any component on the core device becomes &lt;code&gt;BROKEN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;At a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss\&quot;&gt;regular interval that you can configure&lt;/a&gt;, which defaults to 24 hours&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let coreDeviceThingName = "coreDeviceThingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCoreDevice(coreDeviceThingName, opts, (error, data, response) => {
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
 **coreDeviceThingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCoreDeviceResponse**](GetCoreDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeployment

> GetDeploymentResponse getDeployment(deploymentId, opts)



Gets a deployment. Deployments define the components that run on Greengrass core devices.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let deploymentId = "deploymentId_example"; // String | The ID of the deployment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeployment(deploymentId, opts, (error, data, response) => {
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
 **deploymentId** | **String**| The ID of the deployment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDeploymentResponse**](GetDeploymentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceRoleForAccount

> GetServiceRoleForAccountResponse getServiceRoleForAccount(opts)



Gets the service role associated with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. IoT Greengrass uses this role to verify the identity of client devices and manage core device connectivity information. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html\&quot;&gt;Greengrass service role&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServiceRoleForAccount(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceRoleForAccountResponse**](GetServiceRoleForAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listClientDevicesAssociatedWithCoreDevice

> ListClientDevicesAssociatedWithCoreDeviceResponse listClientDevicesAssociatedWithCoreDevice(coreDeviceThingName, opts)



Retrieves a paginated list of client devices that are associated with a core device.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let coreDeviceThingName = "coreDeviceThingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to be returned per paginated request.
  'nextToken': "nextToken_example" // String | The token to be used for the next set of paginated results.
};
apiInstance.listClientDevicesAssociatedWithCoreDevice(coreDeviceThingName, opts, (error, data, response) => {
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
 **coreDeviceThingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per paginated request. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 

### Return type

[**ListClientDevicesAssociatedWithCoreDeviceResponse**](ListClientDevicesAssociatedWithCoreDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listComponentVersions

> ListComponentVersionsResponse listComponentVersions(arn, opts)



Retrieves a paginated list of all versions for a component. Greater versions are listed first.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let arn = "arn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to be returned per paginated request.
  'nextToken': "nextToken_example" // String | The token to be used for the next set of paginated results.
};
apiInstance.listComponentVersions(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the component. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per paginated request. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 

### Return type

[**ListComponentVersionsResponse**](ListComponentVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listComponents

> ListComponentsResponse listComponents(opts)



Retrieves a paginated list of component summaries. This list includes components that you have permission to view.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'scope': "scope_example", // String | <p>The scope of the components to list.</p> <p>Default: <code>PRIVATE</code> </p>
  'maxResults': 56, // Number | The maximum number of results to be returned per paginated request.
  'nextToken': "nextToken_example" // String | The token to be used for the next set of paginated results.
};
apiInstance.listComponents(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **scope** | **String**| &lt;p&gt;The scope of the components to list.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;PRIVATE&lt;/code&gt; &lt;/p&gt; | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per paginated request. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 

### Return type

[**ListComponentsResponse**](ListComponentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCoreDevices

> ListCoreDevicesResponse listCoreDevices(opts)



&lt;p&gt;Retrieves a paginated list of Greengrass core devices.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn&#39;t running on the device, or if device isn&#39;t connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.&lt;/p&gt; &lt;p&gt;Core devices send status updates at the following times:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When the IoT Greengrass Core software starts&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the core device receives a deployment from the Amazon Web Services Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the status of any component on the core device becomes &lt;code&gt;BROKEN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;At a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss\&quot;&gt;regular interval that you can configure&lt;/a&gt;, which defaults to 24 hours&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'thingGroupArn': "thingGroupArn_example", // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the IoT thing group by which to filter. If you specify this parameter, the list includes only core devices that have successfully deployed a deployment that targets the thing group. When you remove a core device from a thing group, the list continues to include that core device.
  'status': "status_example", // String | <p>The core device status by which to filter. If you specify this parameter, the list includes only core devices that have this status. Choose one of the following options:</p> <ul> <li> <p> <code>HEALTHY</code> – The IoT Greengrass Core software and all components run on the core device without issue.</p> </li> <li> <p> <code>UNHEALTHY</code> – The IoT Greengrass Core software or a component is in a failed state on the core device.</p> </li> </ul>
  'maxResults': 56, // Number | The maximum number of results to be returned per paginated request.
  'nextToken': "nextToken_example" // String | The token to be used for the next set of paginated results.
};
apiInstance.listCoreDevices(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **thingGroupArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the IoT thing group by which to filter. If you specify this parameter, the list includes only core devices that have successfully deployed a deployment that targets the thing group. When you remove a core device from a thing group, the list continues to include that core device. | [optional] 
 **status** | **String**| &lt;p&gt;The core device status by which to filter. If you specify this parameter, the list includes only core devices that have this status. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HEALTHY&lt;/code&gt; – The IoT Greengrass Core software and all components run on the core device without issue.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UNHEALTHY&lt;/code&gt; – The IoT Greengrass Core software or a component is in a failed state on the core device.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per paginated request. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 

### Return type

[**ListCoreDevicesResponse**](ListCoreDevicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeployments

> ListDeploymentsResponse listDeployments(opts)



Retrieves a paginated list of deployments.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'targetArn': "targetArn_example", // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the target IoT thing or thing group.
  'historyFilter': "historyFilter_example", // String | <p>The filter for the list of deployments. Choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all deployments.</p> </li> <li> <p> <code>LATEST_ONLY</code> – The list includes only the latest revision of each deployment.</p> </li> </ul> <p>Default: <code>LATEST_ONLY</code> </p>
  'parentTargetArn': "parentTargetArn_example", // String | The parent deployment's target <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> within a subdeployment.
  'maxResults': 56, // Number | The maximum number of results to be returned per paginated request.
  'nextToken': "nextToken_example" // String | The token to be used for the next set of paginated results.
};
apiInstance.listDeployments(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **targetArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the target IoT thing or thing group. | [optional] 
 **historyFilter** | **String**| &lt;p&gt;The filter for the list of deployments. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all deployments.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LATEST_ONLY&lt;/code&gt; – The list includes only the latest revision of each deployment.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;LATEST_ONLY&lt;/code&gt; &lt;/p&gt; | [optional] 
 **parentTargetArn** | **String**| The parent deployment&#39;s target &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; within a subdeployment. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per paginated request. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 

### Return type

[**ListDeploymentsResponse**](ListDeploymentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEffectiveDeployments

> ListEffectiveDeploymentsResponse listEffectiveDeployments(coreDeviceThingName, opts)



Retrieves a paginated list of deployment jobs that IoT Greengrass sends to Greengrass core devices.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let coreDeviceThingName = "coreDeviceThingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to be returned per paginated request.
  'nextToken': "nextToken_example" // String | The token to be used for the next set of paginated results.
};
apiInstance.listEffectiveDeployments(coreDeviceThingName, opts, (error, data, response) => {
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
 **coreDeviceThingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per paginated request. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 

### Return type

[**ListEffectiveDeploymentsResponse**](ListEffectiveDeploymentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInstalledComponents

> ListInstalledComponentsResponse listInstalledComponents(coreDeviceThingName, opts)



&lt;p&gt;Retrieves a paginated list of the components that a Greengrass core device runs. By default, this list doesn&#39;t include components that are deployed as dependencies of other components. To include dependencies in the response, set the &lt;code&gt;topologyFilter&lt;/code&gt; parameter to &lt;code&gt;ALL&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn&#39;t running on the device, or if device isn&#39;t connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.&lt;/p&gt; &lt;p&gt;Core devices send status updates at the following times:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When the IoT Greengrass Core software starts&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the core device receives a deployment from the Amazon Web Services Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the status of any component on the core device becomes &lt;code&gt;BROKEN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;At a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss\&quot;&gt;regular interval that you can configure&lt;/a&gt;, which defaults to 24 hours&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let coreDeviceThingName = "coreDeviceThingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to be returned per paginated request.
  'nextToken': "nextToken_example", // String | The token to be used for the next set of paginated results.
  'topologyFilter': "topologyFilter_example" // String | <p>The filter for the list of components. Choose from the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all components installed on the core device.</p> </li> <li> <p> <code>ROOT</code> – The list includes only <i>root</i> components, which are components that you specify in a deployment. When you choose this option, the list doesn't include components that the core device installs as dependencies of other components.</p> </li> </ul> <p>Default: <code>ROOT</code> </p>
};
apiInstance.listInstalledComponents(coreDeviceThingName, opts, (error, data, response) => {
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
 **coreDeviceThingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per paginated request. | [optional] 
 **nextToken** | **String**| The token to be used for the next set of paginated results. | [optional] 
 **topologyFilter** | **String**| &lt;p&gt;The filter for the list of components. Choose from the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all components installed on the core device.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ROOT&lt;/code&gt; – The list includes only &lt;i&gt;root&lt;/i&gt; components, which are components that you specify in a deployment. When you choose this option, the list doesn&#39;t include components that the core device installs as dependencies of other components.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;ROOT&lt;/code&gt; &lt;/p&gt; | [optional] 

### Return type

[**ListInstalledComponentsResponse**](ListInstalledComponentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Retrieves the list of tags for an IoT Greengrass resource.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resolveComponentCandidates

> ResolveComponentCandidatesResponse resolveComponentCandidates(resolveComponentCandidatesRequest, opts)



&lt;p&gt;Retrieves a list of components that meet the component, version, and platform requirements of a deployment. Greengrass core devices call this operation when they receive a deployment to identify the components to install.&lt;/p&gt; &lt;p&gt;This operation identifies components that meet all dependency requirements for a deployment. If the requirements conflict, then this operation returns an error and the deployment fails. For example, this occurs if component &lt;code&gt;A&lt;/code&gt; requires version &lt;code&gt;&amp;gt;2.0.0&lt;/code&gt; and component &lt;code&gt;B&lt;/code&gt; requires version &lt;code&gt;&amp;lt;2.0.0&lt;/code&gt; of a component dependency.&lt;/p&gt; &lt;p&gt;When you specify the component candidates to resolve, IoT Greengrass compares each component&#39;s digest from the core device with the component&#39;s digest in the Amazon Web Services Cloud. If the digests don&#39;t match, then IoT Greengrass specifies to use the version from the Amazon Web Services Cloud.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To use this operation, you must use the data plane API endpoint and authenticate with an IoT device certificate. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/greengrass.html\&quot;&gt;IoT Greengrass endpoints and quotas&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let resolveComponentCandidatesRequest = new AwsIoTGreengrassV2.ResolveComponentCandidatesRequest(); // ResolveComponentCandidatesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resolveComponentCandidates(resolveComponentCandidatesRequest, opts, (error, data, response) => {
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
 **resolveComponentCandidatesRequest** | [**ResolveComponentCandidatesRequest**](ResolveComponentCandidatesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ResolveComponentCandidatesResponse**](ResolveComponentCandidatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds tags to an IoT Greengrass resource. If a tag already exists for the resource, this operation updates the tag&#39;s value.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to tag.
let tagResourceRequest = new AwsIoTGreengrassV2.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to tag. | 
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


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Removes a tag from an IoT Greengrass resource.

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to untag.
let tagKeys = ["null"]; // [String] | A list of keys for tags to remove from the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to untag. | 
 **tagKeys** | [**[String]**](String.md)| A list of keys for tags to remove from the resource. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConnectivityInfo

> UpdateConnectivityInfoResponse updateConnectivityInfo(thingName, updateConnectivityInfoRequest, opts)



&lt;p&gt;Updates connectivity information for a Greengrass core device.&lt;/p&gt; &lt;p&gt;Connectivity information includes endpoints and ports where client devices can connect to an MQTT broker on the core device. When a client device calls the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-discover-api.html\&quot;&gt;IoT Greengrass discovery API&lt;/a&gt;, IoT Greengrass returns connectivity information for all of the core devices where the client device can connect. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/connect-client-devices.html\&quot;&gt;Connect client devices to core devices&lt;/a&gt; in the &lt;i&gt;IoT Greengrass Version 2 Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTGreengrassV2 from 'aws_io_t_greengrass_v2';
let defaultClient = AwsIoTGreengrassV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTGreengrassV2.DefaultApi();
let thingName = "thingName_example"; // String | The name of the core device. This is also the name of the IoT thing.
let updateConnectivityInfoRequest = new AwsIoTGreengrassV2.UpdateConnectivityInfoRequest(); // UpdateConnectivityInfoRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConnectivityInfo(thingName, updateConnectivityInfoRequest, opts, (error, data, response) => {
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
 **thingName** | **String**| The name of the core device. This is also the name of the IoT thing. | 
 **updateConnectivityInfoRequest** | [**UpdateConnectivityInfoRequest**](UpdateConnectivityInfoRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateConnectivityInfoResponse**](UpdateConnectivityInfoResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

