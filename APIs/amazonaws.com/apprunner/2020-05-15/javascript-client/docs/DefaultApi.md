# AwsAppRunner.DefaultApi

All URIs are relative to *http://apprunner.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateCustomDomain**](DefaultApi.md#associateCustomDomain) | **POST** /#X-Amz-Target&#x3D;AppRunner.AssociateCustomDomain | 
[**createAutoScalingConfiguration**](DefaultApi.md#createAutoScalingConfiguration) | **POST** /#X-Amz-Target&#x3D;AppRunner.CreateAutoScalingConfiguration | 
[**createConnection**](DefaultApi.md#createConnection) | **POST** /#X-Amz-Target&#x3D;AppRunner.CreateConnection | 
[**createObservabilityConfiguration**](DefaultApi.md#createObservabilityConfiguration) | **POST** /#X-Amz-Target&#x3D;AppRunner.CreateObservabilityConfiguration | 
[**createService**](DefaultApi.md#createService) | **POST** /#X-Amz-Target&#x3D;AppRunner.CreateService | 
[**createVpcConnector**](DefaultApi.md#createVpcConnector) | **POST** /#X-Amz-Target&#x3D;AppRunner.CreateVpcConnector | 
[**createVpcIngressConnection**](DefaultApi.md#createVpcIngressConnection) | **POST** /#X-Amz-Target&#x3D;AppRunner.CreateVpcIngressConnection | 
[**deleteAutoScalingConfiguration**](DefaultApi.md#deleteAutoScalingConfiguration) | **POST** /#X-Amz-Target&#x3D;AppRunner.DeleteAutoScalingConfiguration | 
[**deleteConnection**](DefaultApi.md#deleteConnection) | **POST** /#X-Amz-Target&#x3D;AppRunner.DeleteConnection | 
[**deleteObservabilityConfiguration**](DefaultApi.md#deleteObservabilityConfiguration) | **POST** /#X-Amz-Target&#x3D;AppRunner.DeleteObservabilityConfiguration | 
[**deleteService**](DefaultApi.md#deleteService) | **POST** /#X-Amz-Target&#x3D;AppRunner.DeleteService | 
[**deleteVpcConnector**](DefaultApi.md#deleteVpcConnector) | **POST** /#X-Amz-Target&#x3D;AppRunner.DeleteVpcConnector | 
[**deleteVpcIngressConnection**](DefaultApi.md#deleteVpcIngressConnection) | **POST** /#X-Amz-Target&#x3D;AppRunner.DeleteVpcIngressConnection | 
[**describeAutoScalingConfiguration**](DefaultApi.md#describeAutoScalingConfiguration) | **POST** /#X-Amz-Target&#x3D;AppRunner.DescribeAutoScalingConfiguration | 
[**describeCustomDomains**](DefaultApi.md#describeCustomDomains) | **POST** /#X-Amz-Target&#x3D;AppRunner.DescribeCustomDomains | 
[**describeObservabilityConfiguration**](DefaultApi.md#describeObservabilityConfiguration) | **POST** /#X-Amz-Target&#x3D;AppRunner.DescribeObservabilityConfiguration | 
[**describeService**](DefaultApi.md#describeService) | **POST** /#X-Amz-Target&#x3D;AppRunner.DescribeService | 
[**describeVpcConnector**](DefaultApi.md#describeVpcConnector) | **POST** /#X-Amz-Target&#x3D;AppRunner.DescribeVpcConnector | 
[**describeVpcIngressConnection**](DefaultApi.md#describeVpcIngressConnection) | **POST** /#X-Amz-Target&#x3D;AppRunner.DescribeVpcIngressConnection | 
[**disassociateCustomDomain**](DefaultApi.md#disassociateCustomDomain) | **POST** /#X-Amz-Target&#x3D;AppRunner.DisassociateCustomDomain | 
[**listAutoScalingConfigurations**](DefaultApi.md#listAutoScalingConfigurations) | **POST** /#X-Amz-Target&#x3D;AppRunner.ListAutoScalingConfigurations | 
[**listConnections**](DefaultApi.md#listConnections) | **POST** /#X-Amz-Target&#x3D;AppRunner.ListConnections | 
[**listObservabilityConfigurations**](DefaultApi.md#listObservabilityConfigurations) | **POST** /#X-Amz-Target&#x3D;AppRunner.ListObservabilityConfigurations | 
[**listOperations**](DefaultApi.md#listOperations) | **POST** /#X-Amz-Target&#x3D;AppRunner.ListOperations | 
[**listServices**](DefaultApi.md#listServices) | **POST** /#X-Amz-Target&#x3D;AppRunner.ListServices | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;AppRunner.ListTagsForResource | 
[**listVpcConnectors**](DefaultApi.md#listVpcConnectors) | **POST** /#X-Amz-Target&#x3D;AppRunner.ListVpcConnectors | 
[**listVpcIngressConnections**](DefaultApi.md#listVpcIngressConnections) | **POST** /#X-Amz-Target&#x3D;AppRunner.ListVpcIngressConnections | 
[**pauseService**](DefaultApi.md#pauseService) | **POST** /#X-Amz-Target&#x3D;AppRunner.PauseService | 
[**resumeService**](DefaultApi.md#resumeService) | **POST** /#X-Amz-Target&#x3D;AppRunner.ResumeService | 
[**startDeployment**](DefaultApi.md#startDeployment) | **POST** /#X-Amz-Target&#x3D;AppRunner.StartDeployment | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AppRunner.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AppRunner.UntagResource | 
[**updateService**](DefaultApi.md#updateService) | **POST** /#X-Amz-Target&#x3D;AppRunner.UpdateService | 
[**updateVpcIngressConnection**](DefaultApi.md#updateVpcIngressConnection) | **POST** /#X-Amz-Target&#x3D;AppRunner.UpdateVpcIngressConnection | 



## associateCustomDomain

> AssociateCustomDomainResponse associateCustomDomain(xAmzTarget, associateCustomDomainRequest, opts)



&lt;p&gt;Associate your own domain name with the App Runner subdomain URL of your App Runner service.&lt;/p&gt; &lt;p&gt;After you call &lt;code&gt;AssociateCustomDomain&lt;/code&gt; and receive a successful response, use the information in the &lt;a&gt;CustomDomain&lt;/a&gt; record that&#39;s returned to add CNAME records to your Domain Name System (DNS). For each mapped domain name, add a mapping to the target App Runner subdomain and one or more certificate validation records. App Runner then performs DNS validation to verify that you own or control the domain name that you associated. App Runner tracks domain validity in a certificate stored in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide\&quot;&gt;AWS Certificate Manager (ACM)&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let associateCustomDomainRequest = new AwsAppRunner.AssociateCustomDomainRequest(); // AssociateCustomDomainRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateCustomDomain(xAmzTarget, associateCustomDomainRequest, opts, (error, data, response) => {
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
 **associateCustomDomainRequest** | [**AssociateCustomDomainRequest**](AssociateCustomDomainRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateCustomDomainResponse**](AssociateCustomDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAutoScalingConfiguration

> CreateAutoScalingConfigurationResponse createAutoScalingConfiguration(xAmzTarget, createAutoScalingConfigurationRequest, opts)



&lt;p&gt;Create an App Runner automatic scaling configuration resource. App Runner requires this resource when you create or update App Runner services and you require non-default auto scaling settings. You can share an auto scaling configuration across multiple services.&lt;/p&gt; &lt;p&gt;Create multiple revisions of a configuration by calling this action multiple times using the same &lt;code&gt;AutoScalingConfigurationName&lt;/code&gt;. The call returns incremental &lt;code&gt;AutoScalingConfigurationRevision&lt;/code&gt; values. When you create a service and configure an auto scaling configuration resource, the service uses the latest active revision of the auto scaling configuration by default. You can optionally configure the service to use a specific revision.&lt;/p&gt; &lt;p&gt;Configure a higher &lt;code&gt;MinSize&lt;/code&gt; to increase the spread of your App Runner service over more Availability Zones in the Amazon Web Services Region. The tradeoff is a higher minimal cost.&lt;/p&gt; &lt;p&gt;Configure a lower &lt;code&gt;MaxSize&lt;/code&gt; to control your cost. The tradeoff is lower responsiveness during peak demand.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createAutoScalingConfigurationRequest = new AwsAppRunner.CreateAutoScalingConfigurationRequest(); // CreateAutoScalingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAutoScalingConfiguration(xAmzTarget, createAutoScalingConfigurationRequest, opts, (error, data, response) => {
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
 **createAutoScalingConfigurationRequest** | [**CreateAutoScalingConfigurationRequest**](CreateAutoScalingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAutoScalingConfigurationResponse**](CreateAutoScalingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createConnection

> CreateConnectionResponse createConnection(xAmzTarget, createConnectionRequest, opts)



&lt;p&gt;Create an App Runner connection resource. App Runner requires a connection resource when you create App Runner services that access private repositories from certain third-party providers. You can share a connection across multiple services.&lt;/p&gt; &lt;p&gt;A connection resource is needed to access GitHub repositories. GitHub requires a user interface approval process through the App Runner console before you can use the connection.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createConnectionRequest = new AwsAppRunner.CreateConnectionRequest(); // CreateConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConnection(xAmzTarget, createConnectionRequest, opts, (error, data, response) => {
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
 **createConnectionRequest** | [**CreateConnectionRequest**](CreateConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateConnectionResponse**](CreateConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createObservabilityConfiguration

> CreateObservabilityConfigurationResponse createObservabilityConfiguration(xAmzTarget, createObservabilityConfigurationRequest, opts)



&lt;p&gt;Create an App Runner observability configuration resource. App Runner requires this resource when you create or update App Runner services and you want to enable non-default observability features. You can share an observability configuration across multiple services.&lt;/p&gt; &lt;p&gt;Create multiple revisions of a configuration by calling this action multiple times using the same &lt;code&gt;ObservabilityConfigurationName&lt;/code&gt;. The call returns incremental &lt;code&gt;ObservabilityConfigurationRevision&lt;/code&gt; values. When you create a service and configure an observability configuration resource, the service uses the latest active revision of the observability configuration by default. You can optionally configure the service to use a specific revision.&lt;/p&gt; &lt;p&gt;The observability configuration resource is designed to configure multiple features (currently one feature, tracing). This action takes optional parameters that describe the configuration of these features (currently one parameter, &lt;code&gt;TraceConfiguration&lt;/code&gt;). If you don&#39;t specify a feature parameter, App Runner doesn&#39;t enable the feature.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createObservabilityConfigurationRequest = new AwsAppRunner.CreateObservabilityConfigurationRequest(); // CreateObservabilityConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createObservabilityConfiguration(xAmzTarget, createObservabilityConfigurationRequest, opts, (error, data, response) => {
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
 **createObservabilityConfigurationRequest** | [**CreateObservabilityConfigurationRequest**](CreateObservabilityConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateObservabilityConfigurationResponse**](CreateObservabilityConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createService

> CreateServiceResponse createService(xAmzTarget, createServiceRequest, opts)



&lt;p&gt;Create an App Runner service. After the service is created, the action also automatically starts a deployment.&lt;/p&gt; &lt;p&gt;This is an asynchronous operation. On a successful call, you can use the returned &lt;code&gt;OperationId&lt;/code&gt; and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apprunner/latest/api/API_ListOperations.html\&quot;&gt;ListOperations&lt;/a&gt; call to track the operation&#39;s progress.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createServiceRequest = new AwsAppRunner.CreateServiceRequest(); // CreateServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createService(xAmzTarget, createServiceRequest, opts, (error, data, response) => {
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
 **createServiceRequest** | [**CreateServiceRequest**](CreateServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateServiceResponse**](CreateServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVpcConnector

> CreateVpcConnectorResponse createVpcConnector(xAmzTarget, createVpcConnectorRequest, opts)



Create an App Runner VPC connector resource. App Runner requires this resource when you want to associate your App Runner service to a custom Amazon Virtual Private Cloud (Amazon VPC).

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createVpcConnectorRequest = new AwsAppRunner.CreateVpcConnectorRequest(); // CreateVpcConnectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVpcConnector(xAmzTarget, createVpcConnectorRequest, opts, (error, data, response) => {
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
 **createVpcConnectorRequest** | [**CreateVpcConnectorRequest**](CreateVpcConnectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVpcConnectorResponse**](CreateVpcConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVpcIngressConnection

> CreateVpcIngressConnectionResponse createVpcIngressConnection(xAmzTarget, createVpcIngressConnectionRequest, opts)



Create an App Runner VPC Ingress Connection resource. App Runner requires this resource when you want to associate your App Runner service with an Amazon VPC endpoint.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createVpcIngressConnectionRequest = new AwsAppRunner.CreateVpcIngressConnectionRequest(); // CreateVpcIngressConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVpcIngressConnection(xAmzTarget, createVpcIngressConnectionRequest, opts, (error, data, response) => {
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
 **createVpcIngressConnectionRequest** | [**CreateVpcIngressConnectionRequest**](CreateVpcIngressConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVpcIngressConnectionResponse**](CreateVpcIngressConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAutoScalingConfiguration

> DeleteAutoScalingConfigurationResponse deleteAutoScalingConfiguration(xAmzTarget, deleteAutoScalingConfigurationRequest, opts)



Delete an App Runner automatic scaling configuration resource. You can delete a specific revision or the latest active revision. You can&#39;t delete a configuration that&#39;s used by one or more App Runner services.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteAutoScalingConfigurationRequest = new AwsAppRunner.DeleteAutoScalingConfigurationRequest(); // DeleteAutoScalingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAutoScalingConfiguration(xAmzTarget, deleteAutoScalingConfigurationRequest, opts, (error, data, response) => {
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
 **deleteAutoScalingConfigurationRequest** | [**DeleteAutoScalingConfigurationRequest**](DeleteAutoScalingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAutoScalingConfigurationResponse**](DeleteAutoScalingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteConnection

> DeleteConnectionResponse deleteConnection(xAmzTarget, deleteConnectionRequest, opts)



Delete an App Runner connection. You must first ensure that there are no running App Runner services that use this connection. If there are any, the &lt;code&gt;DeleteConnection&lt;/code&gt; action fails.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteConnectionRequest = new AwsAppRunner.DeleteConnectionRequest(); // DeleteConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteConnection(xAmzTarget, deleteConnectionRequest, opts, (error, data, response) => {
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
 **deleteConnectionRequest** | [**DeleteConnectionRequest**](DeleteConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteConnectionResponse**](DeleteConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteObservabilityConfiguration

> DeleteObservabilityConfigurationResponse deleteObservabilityConfiguration(xAmzTarget, deleteObservabilityConfigurationRequest, opts)



Delete an App Runner observability configuration resource. You can delete a specific revision or the latest active revision. You can&#39;t delete a configuration that&#39;s used by one or more App Runner services.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteObservabilityConfigurationRequest = new AwsAppRunner.DeleteObservabilityConfigurationRequest(); // DeleteObservabilityConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteObservabilityConfiguration(xAmzTarget, deleteObservabilityConfigurationRequest, opts, (error, data, response) => {
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
 **deleteObservabilityConfigurationRequest** | [**DeleteObservabilityConfigurationRequest**](DeleteObservabilityConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteObservabilityConfigurationResponse**](DeleteObservabilityConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteService

> DeleteServiceResponse deleteService(xAmzTarget, deleteServiceRequest, opts)



&lt;p&gt;Delete an App Runner service.&lt;/p&gt; &lt;p&gt;This is an asynchronous operation. On a successful call, you can use the returned &lt;code&gt;OperationId&lt;/code&gt; and the &lt;a&gt;ListOperations&lt;/a&gt; call to track the operation&#39;s progress.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Make sure that you don&#39;t have any active VPCIngressConnections associated with the service you want to delete. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteServiceRequest = new AwsAppRunner.DeleteServiceRequest(); // DeleteServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteService(xAmzTarget, deleteServiceRequest, opts, (error, data, response) => {
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
 **deleteServiceRequest** | [**DeleteServiceRequest**](DeleteServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteServiceResponse**](DeleteServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteVpcConnector

> DeleteVpcConnectorResponse deleteVpcConnector(xAmzTarget, deleteVpcConnectorRequest, opts)



Delete an App Runner VPC connector resource. You can&#39;t delete a connector that&#39;s used by one or more App Runner services.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteVpcConnectorRequest = new AwsAppRunner.DeleteVpcConnectorRequest(); // DeleteVpcConnectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVpcConnector(xAmzTarget, deleteVpcConnectorRequest, opts, (error, data, response) => {
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
 **deleteVpcConnectorRequest** | [**DeleteVpcConnectorRequest**](DeleteVpcConnectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVpcConnectorResponse**](DeleteVpcConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteVpcIngressConnection

> DeleteVpcIngressConnectionResponse deleteVpcIngressConnection(xAmzTarget, deleteVpcIngressConnectionRequest, opts)



&lt;p&gt;Delete an App Runner VPC Ingress Connection resource that&#39;s associated with an App Runner service. The VPC Ingress Connection must be in one of the following states to be deleted: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AVAILABLE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FAILED_CREATION&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FAILED_UPDATE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FAILED_DELETION&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteVpcIngressConnectionRequest = new AwsAppRunner.DeleteVpcIngressConnectionRequest(); // DeleteVpcIngressConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVpcIngressConnection(xAmzTarget, deleteVpcIngressConnectionRequest, opts, (error, data, response) => {
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
 **deleteVpcIngressConnectionRequest** | [**DeleteVpcIngressConnectionRequest**](DeleteVpcIngressConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVpcIngressConnectionResponse**](DeleteVpcIngressConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAutoScalingConfiguration

> DescribeAutoScalingConfigurationResponse describeAutoScalingConfiguration(xAmzTarget, describeAutoScalingConfigurationRequest, opts)



Return a full description of an App Runner automatic scaling configuration resource.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAutoScalingConfigurationRequest = new AwsAppRunner.DescribeAutoScalingConfigurationRequest(); // DescribeAutoScalingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAutoScalingConfiguration(xAmzTarget, describeAutoScalingConfigurationRequest, opts, (error, data, response) => {
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
 **describeAutoScalingConfigurationRequest** | [**DescribeAutoScalingConfigurationRequest**](DescribeAutoScalingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAutoScalingConfigurationResponse**](DescribeAutoScalingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeCustomDomains

> DescribeCustomDomainsResponse describeCustomDomains(xAmzTarget, describeCustomDomainsRequest, opts)



Return a description of custom domain names that are associated with an App Runner service.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeCustomDomainsRequest = new AwsAppRunner.DescribeCustomDomainsRequest(); // DescribeCustomDomainsRequest | 
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
apiInstance.describeCustomDomains(xAmzTarget, describeCustomDomainsRequest, opts, (error, data, response) => {
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
 **describeCustomDomainsRequest** | [**DescribeCustomDomainsRequest**](DescribeCustomDomainsRequest.md)|  | 
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

[**DescribeCustomDomainsResponse**](DescribeCustomDomainsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeObservabilityConfiguration

> DescribeObservabilityConfigurationResponse describeObservabilityConfiguration(xAmzTarget, describeObservabilityConfigurationRequest, opts)



Return a full description of an App Runner observability configuration resource.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeObservabilityConfigurationRequest = new AwsAppRunner.DescribeObservabilityConfigurationRequest(); // DescribeObservabilityConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeObservabilityConfiguration(xAmzTarget, describeObservabilityConfigurationRequest, opts, (error, data, response) => {
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
 **describeObservabilityConfigurationRequest** | [**DescribeObservabilityConfigurationRequest**](DescribeObservabilityConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeObservabilityConfigurationResponse**](DescribeObservabilityConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeService

> DescribeServiceResponse describeService(xAmzTarget, describeServiceRequest, opts)



Return a full description of an App Runner service.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeServiceRequest = new AwsAppRunner.DescribeServiceRequest(); // DescribeServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeService(xAmzTarget, describeServiceRequest, opts, (error, data, response) => {
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
 **describeServiceRequest** | [**DescribeServiceRequest**](DescribeServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeServiceResponse**](DescribeServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeVpcConnector

> DescribeVpcConnectorResponse describeVpcConnector(xAmzTarget, describeVpcConnectorRequest, opts)



Return a description of an App Runner VPC connector resource.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeVpcConnectorRequest = new AwsAppRunner.DescribeVpcConnectorRequest(); // DescribeVpcConnectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeVpcConnector(xAmzTarget, describeVpcConnectorRequest, opts, (error, data, response) => {
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
 **describeVpcConnectorRequest** | [**DescribeVpcConnectorRequest**](DescribeVpcConnectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeVpcConnectorResponse**](DescribeVpcConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeVpcIngressConnection

> DescribeVpcIngressConnectionResponse describeVpcIngressConnection(xAmzTarget, describeVpcIngressConnectionRequest, opts)



Return a full description of an App Runner VPC Ingress Connection resource.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeVpcIngressConnectionRequest = new AwsAppRunner.DescribeVpcIngressConnectionRequest(); // DescribeVpcIngressConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeVpcIngressConnection(xAmzTarget, describeVpcIngressConnectionRequest, opts, (error, data, response) => {
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
 **describeVpcIngressConnectionRequest** | [**DescribeVpcIngressConnectionRequest**](DescribeVpcIngressConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeVpcIngressConnectionResponse**](DescribeVpcIngressConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateCustomDomain

> DisassociateCustomDomainResponse disassociateCustomDomain(xAmzTarget, disassociateCustomDomainRequest, opts)



&lt;p&gt;Disassociate a custom domain name from an App Runner service.&lt;/p&gt; &lt;p&gt;Certificates tracking domain validity are associated with a custom domain and are stored in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide\&quot;&gt;AWS Certificate Manager (ACM)&lt;/a&gt;. These certificates aren&#39;t deleted as part of this action. App Runner delays certificate deletion for 30 days after a domain is disassociated from your service.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let disassociateCustomDomainRequest = new AwsAppRunner.DisassociateCustomDomainRequest(); // DisassociateCustomDomainRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateCustomDomain(xAmzTarget, disassociateCustomDomainRequest, opts, (error, data, response) => {
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
 **disassociateCustomDomainRequest** | [**DisassociateCustomDomainRequest**](DisassociateCustomDomainRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateCustomDomainResponse**](DisassociateCustomDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAutoScalingConfigurations

> ListAutoScalingConfigurationsResponse listAutoScalingConfigurations(xAmzTarget, listAutoScalingConfigurationsRequest, opts)



&lt;p&gt;Returns a list of active App Runner automatic scaling configurations in your Amazon Web Services account. You can query the revisions for a specific configuration name or the revisions for all active configurations in your account. You can optionally query only the latest revision of each requested name.&lt;/p&gt; &lt;p&gt;To retrieve a full description of a particular configuration revision, call and provide one of the ARNs returned by &lt;code&gt;ListAutoScalingConfigurations&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAutoScalingConfigurationsRequest = new AwsAppRunner.ListAutoScalingConfigurationsRequest(); // ListAutoScalingConfigurationsRequest | 
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
apiInstance.listAutoScalingConfigurations(xAmzTarget, listAutoScalingConfigurationsRequest, opts, (error, data, response) => {
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
 **listAutoScalingConfigurationsRequest** | [**ListAutoScalingConfigurationsRequest**](ListAutoScalingConfigurationsRequest.md)|  | 
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

[**ListAutoScalingConfigurationsResponse**](ListAutoScalingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listConnections

> ListConnectionsResponse listConnections(xAmzTarget, listConnectionsRequest, opts)



Returns a list of App Runner connections that are associated with your Amazon Web Services account.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listConnectionsRequest = new AwsAppRunner.ListConnectionsRequest(); // ListConnectionsRequest | 
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
apiInstance.listConnections(xAmzTarget, listConnectionsRequest, opts, (error, data, response) => {
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
 **listConnectionsRequest** | [**ListConnectionsRequest**](ListConnectionsRequest.md)|  | 
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

[**ListConnectionsResponse**](ListConnectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listObservabilityConfigurations

> ListObservabilityConfigurationsResponse listObservabilityConfigurations(xAmzTarget, listObservabilityConfigurationsRequest, opts)



&lt;p&gt;Returns a list of active App Runner observability configurations in your Amazon Web Services account. You can query the revisions for a specific configuration name or the revisions for all active configurations in your account. You can optionally query only the latest revision of each requested name.&lt;/p&gt; &lt;p&gt;To retrieve a full description of a particular configuration revision, call and provide one of the ARNs returned by &lt;code&gt;ListObservabilityConfigurations&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listObservabilityConfigurationsRequest = new AwsAppRunner.ListObservabilityConfigurationsRequest(); // ListObservabilityConfigurationsRequest | 
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
apiInstance.listObservabilityConfigurations(xAmzTarget, listObservabilityConfigurationsRequest, opts, (error, data, response) => {
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
 **listObservabilityConfigurationsRequest** | [**ListObservabilityConfigurationsRequest**](ListObservabilityConfigurationsRequest.md)|  | 
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

[**ListObservabilityConfigurationsResponse**](ListObservabilityConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listOperations

> ListOperationsResponse listOperations(xAmzTarget, listOperationsRequest, opts)



&lt;p&gt;Return a list of operations that occurred on an App Runner service.&lt;/p&gt; &lt;p&gt;The resulting list of &lt;a&gt;OperationSummary&lt;/a&gt; objects is sorted in reverse chronological order. The first object on the list represents the last started operation.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listOperationsRequest = new AwsAppRunner.ListOperationsRequest(); // ListOperationsRequest | 
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
apiInstance.listOperations(xAmzTarget, listOperationsRequest, opts, (error, data, response) => {
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
 **listOperationsRequest** | [**ListOperationsRequest**](ListOperationsRequest.md)|  | 
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

[**ListOperationsResponse**](ListOperationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listServices

> ListServicesResponse listServices(xAmzTarget, listServicesRequest, opts)



Returns a list of running App Runner services in your Amazon Web Services account.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listServicesRequest = new AwsAppRunner.ListServicesRequest(); // ListServicesRequest | 
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
apiInstance.listServices(xAmzTarget, listServicesRequest, opts, (error, data, response) => {
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
 **listServicesRequest** | [**ListServicesRequest**](ListServicesRequest.md)|  | 
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

[**ListServicesResponse**](ListServicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



List tags that are associated with for an App Runner resource. The response contains a list of tag key-value pairs.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AwsAppRunner.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
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

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listVpcConnectors

> ListVpcConnectorsResponse listVpcConnectors(xAmzTarget, listVpcConnectorsRequest, opts)



Returns a list of App Runner VPC connectors in your Amazon Web Services account.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listVpcConnectorsRequest = new AwsAppRunner.ListVpcConnectorsRequest(); // ListVpcConnectorsRequest | 
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
apiInstance.listVpcConnectors(xAmzTarget, listVpcConnectorsRequest, opts, (error, data, response) => {
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
 **listVpcConnectorsRequest** | [**ListVpcConnectorsRequest**](ListVpcConnectorsRequest.md)|  | 
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

[**ListVpcConnectorsResponse**](ListVpcConnectorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listVpcIngressConnections

> ListVpcIngressConnectionsResponse listVpcIngressConnections(xAmzTarget, listVpcIngressConnectionsRequest, opts)



Return a list of App Runner VPC Ingress Connections in your Amazon Web Services account.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listVpcIngressConnectionsRequest = new AwsAppRunner.ListVpcIngressConnectionsRequest(); // ListVpcIngressConnectionsRequest | 
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
apiInstance.listVpcIngressConnections(xAmzTarget, listVpcIngressConnectionsRequest, opts, (error, data, response) => {
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
 **listVpcIngressConnectionsRequest** | [**ListVpcIngressConnectionsRequest**](ListVpcIngressConnectionsRequest.md)|  | 
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

[**ListVpcIngressConnectionsResponse**](ListVpcIngressConnectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pauseService

> PauseServiceResponse pauseService(xAmzTarget, pauseServiceRequest, opts)



&lt;p&gt;Pause an active App Runner service. App Runner reduces compute capacity for the service to zero and loses state (for example, ephemeral storage is removed).&lt;/p&gt; &lt;p&gt;This is an asynchronous operation. On a successful call, you can use the returned &lt;code&gt;OperationId&lt;/code&gt; and the &lt;a&gt;ListOperations&lt;/a&gt; call to track the operation&#39;s progress.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let pauseServiceRequest = new AwsAppRunner.PauseServiceRequest(); // PauseServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.pauseService(xAmzTarget, pauseServiceRequest, opts, (error, data, response) => {
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
 **pauseServiceRequest** | [**PauseServiceRequest**](PauseServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PauseServiceResponse**](PauseServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resumeService

> ResumeServiceResponse resumeService(xAmzTarget, resumeServiceRequest, opts)



&lt;p&gt;Resume an active App Runner service. App Runner provisions compute capacity for the service.&lt;/p&gt; &lt;p&gt;This is an asynchronous operation. On a successful call, you can use the returned &lt;code&gt;OperationId&lt;/code&gt; and the &lt;a&gt;ListOperations&lt;/a&gt; call to track the operation&#39;s progress.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let resumeServiceRequest = new AwsAppRunner.ResumeServiceRequest(); // ResumeServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resumeService(xAmzTarget, resumeServiceRequest, opts, (error, data, response) => {
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
 **resumeServiceRequest** | [**ResumeServiceRequest**](ResumeServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ResumeServiceResponse**](ResumeServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startDeployment

> StartDeploymentResponse startDeployment(xAmzTarget, startDeploymentRequest, opts)



&lt;p&gt;Initiate a manual deployment of the latest commit in a source code repository or the latest image in a source image repository to an App Runner service.&lt;/p&gt; &lt;p&gt;For a source code repository, App Runner retrieves the commit and builds a Docker image. For a source image repository, App Runner retrieves the latest Docker image. In both cases, App Runner then deploys the new image to your service and starts a new container instance.&lt;/p&gt; &lt;p&gt;This is an asynchronous operation. On a successful call, you can use the returned &lt;code&gt;OperationId&lt;/code&gt; and the &lt;a&gt;ListOperations&lt;/a&gt; call to track the operation&#39;s progress.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startDeploymentRequest = new AwsAppRunner.StartDeploymentRequest(); // StartDeploymentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startDeployment(xAmzTarget, startDeploymentRequest, opts, (error, data, response) => {
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
 **startDeploymentRequest** | [**StartDeploymentRequest**](StartDeploymentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartDeploymentResponse**](StartDeploymentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Add tags to, or update the tag values of, an App Runner resource. A tag is a key-value pair.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AwsAppRunner.TagResourceRequest(); // TagResourceRequest | 
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


## untagResource

> Object untagResource(xAmzTarget, untagResourceRequest, opts)



Remove tags from an App Runner resource.

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AwsAppRunner.UntagResourceRequest(); // UntagResourceRequest | 
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


## updateService

> UpdateServiceResponse updateService(xAmzTarget, updateServiceRequest, opts)



&lt;p&gt;Update an App Runner service. You can update the source configuration and instance configuration of the service. You can also update the ARN of the auto scaling configuration resource that&#39;s associated with the service. However, you can&#39;t change the name or the encryption configuration of the service. These can be set only when you create the service.&lt;/p&gt; &lt;p&gt;To update the tags applied to your service, use the separate actions &lt;a&gt;TagResource&lt;/a&gt; and &lt;a&gt;UntagResource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This is an asynchronous operation. On a successful call, you can use the returned &lt;code&gt;OperationId&lt;/code&gt; and the &lt;a&gt;ListOperations&lt;/a&gt; call to track the operation&#39;s progress.&lt;/p&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateServiceRequest = new AwsAppRunner.UpdateServiceRequest(); // UpdateServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateService(xAmzTarget, updateServiceRequest, opts, (error, data, response) => {
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
 **updateServiceRequest** | [**UpdateServiceRequest**](UpdateServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateServiceResponse**](UpdateServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVpcIngressConnection

> UpdateVpcIngressConnectionResponse updateVpcIngressConnection(xAmzTarget, updateVpcIngressConnectionRequest, opts)



&lt;p&gt;Update an existing App Runner VPC Ingress Connection resource. The VPC Ingress Connection must be in one of the following states to be updated:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; AVAILABLE &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; FAILED_CREATION &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; FAILED_UPDATE &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsAppRunner from 'aws_app_runner';
let defaultClient = AwsAppRunner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppRunner.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateVpcIngressConnectionRequest = new AwsAppRunner.UpdateVpcIngressConnectionRequest(); // UpdateVpcIngressConnectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVpcIngressConnection(xAmzTarget, updateVpcIngressConnectionRequest, opts, (error, data, response) => {
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
 **updateVpcIngressConnectionRequest** | [**UpdateVpcIngressConnectionRequest**](UpdateVpcIngressConnectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVpcIngressConnectionResponse**](UpdateVpcIngressConnectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

