# AwsCloudMap.DefaultApi

All URIs are relative to *http://servicediscovery.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHttpNamespace**](DefaultApi.md#createHttpNamespace) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.CreateHttpNamespace | 
[**createPrivateDnsNamespace**](DefaultApi.md#createPrivateDnsNamespace) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.CreatePrivateDnsNamespace | 
[**createPublicDnsNamespace**](DefaultApi.md#createPublicDnsNamespace) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.CreatePublicDnsNamespace | 
[**createService**](DefaultApi.md#createService) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.CreateService | 
[**deleteNamespace**](DefaultApi.md#deleteNamespace) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.DeleteNamespace | 
[**deleteService**](DefaultApi.md#deleteService) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.DeleteService | 
[**deregisterInstance**](DefaultApi.md#deregisterInstance) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.DeregisterInstance | 
[**discoverInstances**](DefaultApi.md#discoverInstances) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.DiscoverInstances | 
[**getInstance**](DefaultApi.md#getInstance) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.GetInstance | 
[**getInstancesHealthStatus**](DefaultApi.md#getInstancesHealthStatus) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.GetInstancesHealthStatus | 
[**getNamespace**](DefaultApi.md#getNamespace) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.GetNamespace | 
[**getOperation**](DefaultApi.md#getOperation) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.GetOperation | 
[**getService**](DefaultApi.md#getService) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.GetService | 
[**listInstances**](DefaultApi.md#listInstances) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.ListInstances | 
[**listNamespaces**](DefaultApi.md#listNamespaces) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.ListNamespaces | 
[**listOperations**](DefaultApi.md#listOperations) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.ListOperations | 
[**listServices**](DefaultApi.md#listServices) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.ListServices | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.ListTagsForResource | 
[**registerInstance**](DefaultApi.md#registerInstance) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.RegisterInstance | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.UntagResource | 
[**updateHttpNamespace**](DefaultApi.md#updateHttpNamespace) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.UpdateHttpNamespace | 
[**updateInstanceCustomHealthStatus**](DefaultApi.md#updateInstanceCustomHealthStatus) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.UpdateInstanceCustomHealthStatus | 
[**updatePrivateDnsNamespace**](DefaultApi.md#updatePrivateDnsNamespace) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.UpdatePrivateDnsNamespace | 
[**updatePublicDnsNamespace**](DefaultApi.md#updatePublicDnsNamespace) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.UpdatePublicDnsNamespace | 
[**updateService**](DefaultApi.md#updateService) | **POST** /#X-Amz-Target&#x3D;Route53AutoNaming_v20170314.UpdateService | 



## createHttpNamespace

> CreateHttpNamespaceResponse createHttpNamespace(xAmzTarget, createHttpNamespaceRequest, opts)



&lt;p&gt;Creates an HTTP namespace. Service instances registered using an HTTP namespace can be discovered using a &lt;code&gt;DiscoverInstances&lt;/code&gt; request but can&#39;t be discovered using DNS.&lt;/p&gt; &lt;p&gt;For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createHttpNamespaceRequest = new AwsCloudMap.CreateHttpNamespaceRequest(); // CreateHttpNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createHttpNamespace(xAmzTarget, createHttpNamespaceRequest, opts, (error, data, response) => {
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
 **createHttpNamespaceRequest** | [**CreateHttpNamespaceRequest**](CreateHttpNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateHttpNamespaceResponse**](CreateHttpNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPrivateDnsNamespace

> CreatePrivateDnsNamespaceResponse createPrivateDnsNamespace(xAmzTarget, createPrivateDnsNamespaceRequest, opts)



Creates a private namespace based on DNS, which is visible only inside a specified Amazon VPC. The namespace defines your service naming scheme. For example, if you name your namespace &lt;code&gt;example.com&lt;/code&gt; and name your service &lt;code&gt;backend&lt;/code&gt;, the resulting DNS name for the service is &lt;code&gt;backend.example.com&lt;/code&gt;. Service instances that are registered using a private DNS namespace can be discovered using either a &lt;code&gt;DiscoverInstances&lt;/code&gt; request or using DNS. For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createPrivateDnsNamespaceRequest = new AwsCloudMap.CreatePrivateDnsNamespaceRequest(); // CreatePrivateDnsNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPrivateDnsNamespace(xAmzTarget, createPrivateDnsNamespaceRequest, opts, (error, data, response) => {
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
 **createPrivateDnsNamespaceRequest** | [**CreatePrivateDnsNamespaceRequest**](CreatePrivateDnsNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePrivateDnsNamespaceResponse**](CreatePrivateDnsNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPublicDnsNamespace

> CreatePublicDnsNamespaceResponse createPublicDnsNamespace(xAmzTarget, createPublicDnsNamespaceRequest, opts)



&lt;p&gt;Creates a public namespace based on DNS, which is visible on the internet. The namespace defines your service naming scheme. For example, if you name your namespace &lt;code&gt;example.com&lt;/code&gt; and name your service &lt;code&gt;backend&lt;/code&gt;, the resulting DNS name for the service is &lt;code&gt;backend.example.com&lt;/code&gt;. You can discover instances that were registered with a public DNS namespace by using either a &lt;code&gt;DiscoverInstances&lt;/code&gt; request or using DNS. For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The &lt;code&gt;CreatePublicDnsNamespace&lt;/code&gt; API operation is not supported in the Amazon Web Services GovCloud (US) Regions.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createPublicDnsNamespaceRequest = new AwsCloudMap.CreatePublicDnsNamespaceRequest(); // CreatePublicDnsNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPublicDnsNamespace(xAmzTarget, createPublicDnsNamespaceRequest, opts, (error, data, response) => {
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
 **createPublicDnsNamespaceRequest** | [**CreatePublicDnsNamespaceRequest**](CreatePublicDnsNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePublicDnsNamespaceResponse**](CreatePublicDnsNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createService

> CreateServiceResponse createService(xAmzTarget, createServiceRequest, opts)



&lt;p&gt;Creates a service. This action defines the configuration for the following entities:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For public and private DNS namespaces, one of the following combinations of DNS records in Amazon Route 53:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;A&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AAAA&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;A&lt;/code&gt; and &lt;code&gt;AAAA&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SRV&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CNAME&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Optionally, a health check&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After you create the service, you can submit a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html\&quot;&gt;RegisterInstance&lt;/a&gt; request, and Cloud Map uses the values in the configuration to create the specified entities.&lt;/p&gt; &lt;p&gt;For the current quota on the number of instances that you can register using the same namespace and using the same service, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createServiceRequest = new AwsCloudMap.CreateServiceRequest(); // CreateServiceRequest | 
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


## deleteNamespace

> DeleteNamespaceResponse deleteNamespace(xAmzTarget, deleteNamespaceRequest, opts)



Deletes a namespace from the current account. If the namespace still contains one or more services, the request fails.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteNamespaceRequest = new AwsCloudMap.DeleteNamespaceRequest(); // DeleteNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteNamespace(xAmzTarget, deleteNamespaceRequest, opts, (error, data, response) => {
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
 **deleteNamespaceRequest** | [**DeleteNamespaceRequest**](DeleteNamespaceRequest.md)|  | 
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


## deleteService

> Object deleteService(xAmzTarget, deleteServiceRequest, opts)



Deletes a specified service. If the service still contains one or more registered instances, the request fails.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteServiceRequest = new AwsCloudMap.DeleteServiceRequest(); // DeleteServiceRequest | 
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

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deregisterInstance

> DeregisterInstanceResponse deregisterInstance(xAmzTarget, deregisterInstanceRequest, opts)



Deletes the Amazon Route 53 DNS records and health check, if any, that Cloud Map created for the specified instance.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deregisterInstanceRequest = new AwsCloudMap.DeregisterInstanceRequest(); // DeregisterInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deregisterInstance(xAmzTarget, deregisterInstanceRequest, opts, (error, data, response) => {
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
 **deregisterInstanceRequest** | [**DeregisterInstanceRequest**](DeregisterInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeregisterInstanceResponse**](DeregisterInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## discoverInstances

> DiscoverInstancesResponse discoverInstances(xAmzTarget, discoverInstancesRequest, opts)



Discovers registered instances for a specified namespace and service. You can use &lt;code&gt;DiscoverInstances&lt;/code&gt; to discover instances for any type of namespace. For public and private DNS namespaces, you can also use DNS queries to discover instances.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let discoverInstancesRequest = new AwsCloudMap.DiscoverInstancesRequest(); // DiscoverInstancesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.discoverInstances(xAmzTarget, discoverInstancesRequest, opts, (error, data, response) => {
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
 **discoverInstancesRequest** | [**DiscoverInstancesRequest**](DiscoverInstancesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DiscoverInstancesResponse**](DiscoverInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getInstance

> GetInstanceResponse getInstance(xAmzTarget, getInstanceRequest, opts)



Gets information about a specified instance.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getInstanceRequest = new AwsCloudMap.GetInstanceRequest(); // GetInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getInstance(xAmzTarget, getInstanceRequest, opts, (error, data, response) => {
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
 **getInstanceRequest** | [**GetInstanceRequest**](GetInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetInstanceResponse**](GetInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getInstancesHealthStatus

> GetInstancesHealthStatusResponse getInstancesHealthStatus(xAmzTarget, getInstancesHealthStatusRequest, opts)



&lt;p&gt;Gets the current health status (&lt;code&gt;Healthy&lt;/code&gt;, &lt;code&gt;Unhealthy&lt;/code&gt;, or &lt;code&gt;Unknown&lt;/code&gt;) of one or more instances that are associated with a specified service.&lt;/p&gt; &lt;note&gt; &lt;p&gt;There&#39;s a brief delay between when you register an instance and when the health status for the instance is available. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getInstancesHealthStatusRequest = new AwsCloudMap.GetInstancesHealthStatusRequest(); // GetInstancesHealthStatusRequest | 
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
apiInstance.getInstancesHealthStatus(xAmzTarget, getInstancesHealthStatusRequest, opts, (error, data, response) => {
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
 **getInstancesHealthStatusRequest** | [**GetInstancesHealthStatusRequest**](GetInstancesHealthStatusRequest.md)|  | 
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

[**GetInstancesHealthStatusResponse**](GetInstancesHealthStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getNamespace

> GetNamespaceResponse getNamespace(xAmzTarget, getNamespaceRequest, opts)



Gets information about a namespace.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getNamespaceRequest = new AwsCloudMap.GetNamespaceRequest(); // GetNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getNamespace(xAmzTarget, getNamespaceRequest, opts, (error, data, response) => {
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
 **getNamespaceRequest** | [**GetNamespaceRequest**](GetNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetNamespaceResponse**](GetNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOperation

> GetOperationResponse getOperation(xAmzTarget, getOperationRequest, opts)



&lt;p&gt;Gets information about any operation that returns an operation ID in the response, such as a &lt;code&gt;CreateService&lt;/code&gt; request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To get a list of operations that match specified criteria, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html\&quot;&gt;ListOperations&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getOperationRequest = new AwsCloudMap.GetOperationRequest(); // GetOperationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOperation(xAmzTarget, getOperationRequest, opts, (error, data, response) => {
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
 **getOperationRequest** | [**GetOperationRequest**](GetOperationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOperationResponse**](GetOperationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getService

> GetServiceResponse getService(xAmzTarget, getServiceRequest, opts)



Gets the settings for a specified service.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getServiceRequest = new AwsCloudMap.GetServiceRequest(); // GetServiceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getService(xAmzTarget, getServiceRequest, opts, (error, data, response) => {
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
 **getServiceRequest** | [**GetServiceRequest**](GetServiceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceResponse**](GetServiceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listInstances

> ListInstancesResponse listInstances(xAmzTarget, listInstancesRequest, opts)



Lists summary information about the instances that you registered by using a specified service.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listInstancesRequest = new AwsCloudMap.ListInstancesRequest(); // ListInstancesRequest | 
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
apiInstance.listInstances(xAmzTarget, listInstancesRequest, opts, (error, data, response) => {
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
 **listInstancesRequest** | [**ListInstancesRequest**](ListInstancesRequest.md)|  | 
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

[**ListInstancesResponse**](ListInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listNamespaces

> ListNamespacesResponse listNamespaces(xAmzTarget, listNamespacesRequest, opts)



Lists summary information about the namespaces that were created by the current Amazon Web Services account.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listNamespacesRequest = new AwsCloudMap.ListNamespacesRequest(); // ListNamespacesRequest | 
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
apiInstance.listNamespaces(xAmzTarget, listNamespacesRequest, opts, (error, data, response) => {
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
 **listNamespacesRequest** | [**ListNamespacesRequest**](ListNamespacesRequest.md)|  | 
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

[**ListNamespacesResponse**](ListNamespacesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listOperations

> ListOperationsResponse listOperations(xAmzTarget, listOperationsRequest, opts)



Lists operations that match the criteria that you specify.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listOperationsRequest = new AwsCloudMap.ListOperationsRequest(); // ListOperationsRequest | 
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



Lists summary information for all the services that are associated with one or more specified namespaces.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listServicesRequest = new AwsCloudMap.ListServicesRequest(); // ListServicesRequest | 
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



Lists tags for the specified resource.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AwsCloudMap.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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


## registerInstance

> RegisterInstanceResponse registerInstance(xAmzTarget, registerInstanceRequest, opts)



&lt;p&gt;Creates or updates one or more records and, optionally, creates a health check based on the settings in a specified service. When you submit a &lt;code&gt;RegisterInstance&lt;/code&gt; request, the following occurs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For each DNS record that you define in the service that&#39;s specified by &lt;code&gt;ServiceId&lt;/code&gt;, a record is created or updated in the hosted zone that&#39;s associated with the corresponding namespace.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the service includes &lt;code&gt;HealthCheckConfig&lt;/code&gt;, a health check is created based on the settings in the health check configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The health check, if any, is associated with each of the new or updated records.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;One &lt;code&gt;RegisterInstance&lt;/code&gt; request must complete before you can submit another request and specify the same service ID and instance ID.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html\&quot;&gt;CreateService&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When Cloud Map receives a DNS query for the specified DNS name, it returns the applicable value:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If the health check is healthy&lt;/b&gt;: returns all the records&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If the health check is unhealthy&lt;/b&gt;: returns the applicable value for the last healthy instance&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If you didn&#39;t specify a health check configuration&lt;/b&gt;: returns all the records&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For the current quota on the number of instances that you can register using the same namespace and using the same service, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let registerInstanceRequest = new AwsCloudMap.RegisterInstanceRequest(); // RegisterInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerInstance(xAmzTarget, registerInstanceRequest, opts, (error, data, response) => {
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
 **registerInstanceRequest** | [**RegisterInstanceRequest**](RegisterInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegisterInstanceResponse**](RegisterInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Adds one or more tags to the specified resource.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AwsCloudMap.TagResourceRequest(); // TagResourceRequest | 
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



Removes one or more tags from the specified resource.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AwsCloudMap.UntagResourceRequest(); // UntagResourceRequest | 
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


## updateHttpNamespace

> UpdateHttpNamespaceResponse updateHttpNamespace(xAmzTarget, updateHttpNamespaceRequest, opts)



Updates an HTTP namespace.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateHttpNamespaceRequest = new AwsCloudMap.UpdateHttpNamespaceRequest(); // UpdateHttpNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateHttpNamespace(xAmzTarget, updateHttpNamespaceRequest, opts, (error, data, response) => {
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
 **updateHttpNamespaceRequest** | [**UpdateHttpNamespaceRequest**](UpdateHttpNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateHttpNamespaceResponse**](UpdateHttpNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInstanceCustomHealthStatus

> updateInstanceCustomHealthStatus(xAmzTarget, updateInstanceCustomHealthStatusRequest, opts)



&lt;p&gt;Submits a request to change the health status of a custom health check to healthy or unhealthy.&lt;/p&gt; &lt;p&gt;You can use &lt;code&gt;UpdateInstanceCustomHealthStatus&lt;/code&gt; to change the status only for custom health checks, which you define using &lt;code&gt;HealthCheckCustomConfig&lt;/code&gt; when you create a service. You can&#39;t use it to change the status for Route 53 health checks, which you define using &lt;code&gt;HealthCheckConfig&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html\&quot;&gt;HealthCheckCustomConfig&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateInstanceCustomHealthStatusRequest = new AwsCloudMap.UpdateInstanceCustomHealthStatusRequest(); // UpdateInstanceCustomHealthStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateInstanceCustomHealthStatus(xAmzTarget, updateInstanceCustomHealthStatusRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **updateInstanceCustomHealthStatusRequest** | [**UpdateInstanceCustomHealthStatusRequest**](UpdateInstanceCustomHealthStatusRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## updatePrivateDnsNamespace

> UpdatePrivateDnsNamespaceResponse updatePrivateDnsNamespace(xAmzTarget, updatePrivateDnsNamespaceRequest, opts)



Updates a private DNS namespace.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updatePrivateDnsNamespaceRequest = new AwsCloudMap.UpdatePrivateDnsNamespaceRequest(); // UpdatePrivateDnsNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePrivateDnsNamespace(xAmzTarget, updatePrivateDnsNamespaceRequest, opts, (error, data, response) => {
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
 **updatePrivateDnsNamespaceRequest** | [**UpdatePrivateDnsNamespaceRequest**](UpdatePrivateDnsNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePrivateDnsNamespaceResponse**](UpdatePrivateDnsNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePublicDnsNamespace

> UpdatePublicDnsNamespaceResponse updatePublicDnsNamespace(xAmzTarget, updatePublicDnsNamespaceRequest, opts)



Updates a public DNS namespace.

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updatePublicDnsNamespaceRequest = new AwsCloudMap.UpdatePublicDnsNamespaceRequest(); // UpdatePublicDnsNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePublicDnsNamespace(xAmzTarget, updatePublicDnsNamespaceRequest, opts, (error, data, response) => {
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
 **updatePublicDnsNamespaceRequest** | [**UpdatePublicDnsNamespaceRequest**](UpdatePublicDnsNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePublicDnsNamespaceResponse**](UpdatePublicDnsNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateService

> UpdateServiceResponse updateService(xAmzTarget, updateServiceRequest, opts)



&lt;p&gt;Submits a request to perform the following operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Update the TTL setting for existing &lt;code&gt;DnsRecords&lt;/code&gt; configurations&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add, update, or delete &lt;code&gt;HealthCheckConfig&lt;/code&gt; for a specified service&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t add, update, or delete a &lt;code&gt;HealthCheckCustomConfig&lt;/code&gt; configuration.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For public and private DNS namespaces, note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you omit any existing &lt;code&gt;DnsRecords&lt;/code&gt; or &lt;code&gt;HealthCheckConfig&lt;/code&gt; configurations from an &lt;code&gt;UpdateService&lt;/code&gt; request, the configurations are deleted from the service.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you omit an existing &lt;code&gt;HealthCheckCustomConfig&lt;/code&gt; configuration from an &lt;code&gt;UpdateService&lt;/code&gt; request, the configuration isn&#39;t deleted from the service.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When you update settings for a service, Cloud Map also updates the corresponding settings in all the records and health checks that were created by using the specified service.&lt;/p&gt;

### Example

```javascript
import AwsCloudMap from 'aws_cloud_map';
let defaultClient = AwsCloudMap.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCloudMap.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateServiceRequest = new AwsCloudMap.UpdateServiceRequest(); // UpdateServiceRequest | 
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

