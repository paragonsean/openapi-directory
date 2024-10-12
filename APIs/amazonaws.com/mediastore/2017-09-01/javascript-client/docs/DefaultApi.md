# AwsElementalMediaStore.DefaultApi

All URIs are relative to *http://mediastore.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createContainer**](DefaultApi.md#createContainer) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.CreateContainer | 
[**deleteContainer**](DefaultApi.md#deleteContainer) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.DeleteContainer | 
[**deleteContainerPolicy**](DefaultApi.md#deleteContainerPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.DeleteContainerPolicy | 
[**deleteCorsPolicy**](DefaultApi.md#deleteCorsPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.DeleteCorsPolicy | 
[**deleteLifecyclePolicy**](DefaultApi.md#deleteLifecyclePolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.DeleteLifecyclePolicy | 
[**deleteMetricPolicy**](DefaultApi.md#deleteMetricPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.DeleteMetricPolicy | 
[**describeContainer**](DefaultApi.md#describeContainer) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.DescribeContainer | 
[**getContainerPolicy**](DefaultApi.md#getContainerPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.GetContainerPolicy | 
[**getCorsPolicy**](DefaultApi.md#getCorsPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.GetCorsPolicy | 
[**getLifecyclePolicy**](DefaultApi.md#getLifecyclePolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.GetLifecyclePolicy | 
[**getMetricPolicy**](DefaultApi.md#getMetricPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.GetMetricPolicy | 
[**listContainers**](DefaultApi.md#listContainers) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.ListContainers | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.ListTagsForResource | 
[**putContainerPolicy**](DefaultApi.md#putContainerPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.PutContainerPolicy | 
[**putCorsPolicy**](DefaultApi.md#putCorsPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.PutCorsPolicy | 
[**putLifecyclePolicy**](DefaultApi.md#putLifecyclePolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.PutLifecyclePolicy | 
[**putMetricPolicy**](DefaultApi.md#putMetricPolicy) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.PutMetricPolicy | 
[**startAccessLogging**](DefaultApi.md#startAccessLogging) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.StartAccessLogging | 
[**stopAccessLogging**](DefaultApi.md#stopAccessLogging) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.StopAccessLogging | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;MediaStore_20170901.UntagResource | 



## createContainer

> CreateContainerOutput createContainer(xAmzTarget, createContainerInput, opts)



Creates a storage container to hold objects. A container is similar to a bucket in the Amazon S3 service.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createContainerInput = new AwsElementalMediaStore.CreateContainerInput(); // CreateContainerInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContainer(xAmzTarget, createContainerInput, opts, (error, data, response) => {
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
 **createContainerInput** | [**CreateContainerInput**](CreateContainerInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateContainerOutput**](CreateContainerOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteContainer

> Object deleteContainer(xAmzTarget, deleteContainerInput, opts)



Deletes the specified container. Before you make a &lt;code&gt;DeleteContainer&lt;/code&gt; request, delete any objects in the container or in any folders in the container. You can delete only empty containers. 

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteContainerInput = new AwsElementalMediaStore.DeleteContainerInput(); // DeleteContainerInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContainer(xAmzTarget, deleteContainerInput, opts, (error, data, response) => {
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
 **deleteContainerInput** | [**DeleteContainerInput**](DeleteContainerInput.md)|  | 
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


## deleteContainerPolicy

> Object deleteContainerPolicy(xAmzTarget, deleteContainerPolicyInput, opts)



Deletes the access policy that is associated with the specified container.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteContainerPolicyInput = new AwsElementalMediaStore.DeleteContainerPolicyInput(); // DeleteContainerPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContainerPolicy(xAmzTarget, deleteContainerPolicyInput, opts, (error, data, response) => {
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
 **deleteContainerPolicyInput** | [**DeleteContainerPolicyInput**](DeleteContainerPolicyInput.md)|  | 
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


## deleteCorsPolicy

> Object deleteCorsPolicy(xAmzTarget, deleteCorsPolicyInput, opts)



&lt;p&gt;Deletes the cross-origin resource sharing (CORS) configuration information that is set for the container.&lt;/p&gt; &lt;p&gt;To use this operation, you must have permission to perform the &lt;code&gt;MediaStore:DeleteCorsPolicy&lt;/code&gt; action. The container owner has this permission by default and can grant this permission to others.&lt;/p&gt;

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteCorsPolicyInput = new AwsElementalMediaStore.DeleteCorsPolicyInput(); // DeleteCorsPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCorsPolicy(xAmzTarget, deleteCorsPolicyInput, opts, (error, data, response) => {
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
 **deleteCorsPolicyInput** | [**DeleteCorsPolicyInput**](DeleteCorsPolicyInput.md)|  | 
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


## deleteLifecyclePolicy

> Object deleteLifecyclePolicy(xAmzTarget, deleteLifecyclePolicyInput, opts)



Removes an object lifecycle policy from a container. It takes up to 20 minutes for the change to take effect.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteLifecyclePolicyInput = new AwsElementalMediaStore.DeleteLifecyclePolicyInput(); // DeleteLifecyclePolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLifecyclePolicy(xAmzTarget, deleteLifecyclePolicyInput, opts, (error, data, response) => {
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
 **deleteLifecyclePolicyInput** | [**DeleteLifecyclePolicyInput**](DeleteLifecyclePolicyInput.md)|  | 
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


## deleteMetricPolicy

> Object deleteMetricPolicy(xAmzTarget, deleteMetricPolicyInput, opts)



Deletes the metric policy that is associated with the specified container. If there is no metric policy associated with the container, MediaStore doesn&#39;t send metrics to CloudWatch.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteMetricPolicyInput = new AwsElementalMediaStore.DeleteMetricPolicyInput(); // DeleteMetricPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMetricPolicy(xAmzTarget, deleteMetricPolicyInput, opts, (error, data, response) => {
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
 **deleteMetricPolicyInput** | [**DeleteMetricPolicyInput**](DeleteMetricPolicyInput.md)|  | 
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


## describeContainer

> DescribeContainerOutput describeContainer(xAmzTarget, describeContainerInput, opts)



Retrieves the properties of the requested container. This request is commonly used to retrieve the endpoint of a container. An endpoint is a value assigned by the service when a new container is created. A container&#39;s endpoint does not change after it has been assigned. The &lt;code&gt;DescribeContainer&lt;/code&gt; request returns a single &lt;code&gt;Container&lt;/code&gt; object based on &lt;code&gt;ContainerName&lt;/code&gt;. To return all &lt;code&gt;Container&lt;/code&gt; objects that are associated with a specified AWS account, use &lt;a&gt;ListContainers&lt;/a&gt;.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeContainerInput = new AwsElementalMediaStore.DescribeContainerInput(); // DescribeContainerInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeContainer(xAmzTarget, describeContainerInput, opts, (error, data, response) => {
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
 **describeContainerInput** | [**DescribeContainerInput**](DescribeContainerInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeContainerOutput**](DescribeContainerOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getContainerPolicy

> GetContainerPolicyOutput getContainerPolicy(xAmzTarget, getContainerPolicyInput, opts)



Retrieves the access policy for the specified container. For information about the data that is included in an access policy, see the &lt;a href&#x3D;\&quot;https://aws.amazon.com/documentation/iam/\&quot;&gt;AWS Identity and Access Management User Guide&lt;/a&gt;.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getContainerPolicyInput = new AwsElementalMediaStore.GetContainerPolicyInput(); // GetContainerPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContainerPolicy(xAmzTarget, getContainerPolicyInput, opts, (error, data, response) => {
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
 **getContainerPolicyInput** | [**GetContainerPolicyInput**](GetContainerPolicyInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContainerPolicyOutput**](GetContainerPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCorsPolicy

> GetCorsPolicyOutput getCorsPolicy(xAmzTarget, getCorsPolicyInput, opts)



&lt;p&gt;Returns the cross-origin resource sharing (CORS) configuration information that is set for the container.&lt;/p&gt; &lt;p&gt;To use this operation, you must have permission to perform the &lt;code&gt;MediaStore:GetCorsPolicy&lt;/code&gt; action. By default, the container owner has this permission and can grant it to others.&lt;/p&gt;

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getCorsPolicyInput = new AwsElementalMediaStore.GetCorsPolicyInput(); // GetCorsPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCorsPolicy(xAmzTarget, getCorsPolicyInput, opts, (error, data, response) => {
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
 **getCorsPolicyInput** | [**GetCorsPolicyInput**](GetCorsPolicyInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCorsPolicyOutput**](GetCorsPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLifecyclePolicy

> GetLifecyclePolicyOutput getLifecyclePolicy(xAmzTarget, getLifecyclePolicyInput, opts)



Retrieves the object lifecycle policy that is assigned to a container.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getLifecyclePolicyInput = new AwsElementalMediaStore.GetLifecyclePolicyInput(); // GetLifecyclePolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLifecyclePolicy(xAmzTarget, getLifecyclePolicyInput, opts, (error, data, response) => {
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
 **getLifecyclePolicyInput** | [**GetLifecyclePolicyInput**](GetLifecyclePolicyInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLifecyclePolicyOutput**](GetLifecyclePolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMetricPolicy

> GetMetricPolicyOutput getMetricPolicy(xAmzTarget, getMetricPolicyInput, opts)



Returns the metric policy for the specified container. 

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getMetricPolicyInput = new AwsElementalMediaStore.GetMetricPolicyInput(); // GetMetricPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMetricPolicy(xAmzTarget, getMetricPolicyInput, opts, (error, data, response) => {
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
 **getMetricPolicyInput** | [**GetMetricPolicyInput**](GetMetricPolicyInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMetricPolicyOutput**](GetMetricPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listContainers

> ListContainersOutput listContainers(xAmzTarget, listContainersInput, opts)



&lt;p&gt;Lists the properties of all containers in AWS Elemental MediaStore. &lt;/p&gt; &lt;p&gt;You can query to receive all the containers in one response. Or you can include the &lt;code&gt;MaxResults&lt;/code&gt; parameter to receive a limited number of containers in each response. In this case, the response includes a token. To get the next set of containers, send the command again, this time with the &lt;code&gt;NextToken&lt;/code&gt; parameter (with the returned token as its value). The next set of responses appears, with a token if there are still more containers to receive. &lt;/p&gt; &lt;p&gt;See also &lt;a&gt;DescribeContainer&lt;/a&gt;, which gets the properties of one container. &lt;/p&gt;

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listContainersInput = new AwsElementalMediaStore.ListContainersInput(); // ListContainersInput | 
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
apiInstance.listContainers(xAmzTarget, listContainersInput, opts, (error, data, response) => {
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
 **listContainersInput** | [**ListContainersInput**](ListContainersInput.md)|  | 
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

[**ListContainersOutput**](ListContainersOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(xAmzTarget, listTagsForResourceInput, opts)



Returns a list of the tags assigned to the specified container. 

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceInput = new AwsElementalMediaStore.ListTagsForResourceInput(); // ListTagsForResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceInput, opts, (error, data, response) => {
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
 **listTagsForResourceInput** | [**ListTagsForResourceInput**](ListTagsForResourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putContainerPolicy

> Object putContainerPolicy(xAmzTarget, putContainerPolicyInput, opts)



&lt;p&gt;Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the &lt;a href&#x3D;\&quot;https://aws.amazon.com/documentation/iam/\&quot;&gt;AWS Identity and Access Management User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For this release of the REST API, you can create only one policy for a container. If you enter &lt;code&gt;PutContainerPolicy&lt;/code&gt; twice, the second command modifies the existing policy. &lt;/p&gt;

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putContainerPolicyInput = new AwsElementalMediaStore.PutContainerPolicyInput(); // PutContainerPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putContainerPolicy(xAmzTarget, putContainerPolicyInput, opts, (error, data, response) => {
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
 **putContainerPolicyInput** | [**PutContainerPolicyInput**](PutContainerPolicyInput.md)|  | 
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


## putCorsPolicy

> Object putCorsPolicy(xAmzTarget, putCorsPolicyInput, opts)



&lt;p&gt;Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser&#39;s XMLHttpRequest capability.&lt;/p&gt; &lt;p&gt;To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.&lt;/p&gt; &lt;p&gt;To learn more about CORS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html\&quot;&gt;Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putCorsPolicyInput = new AwsElementalMediaStore.PutCorsPolicyInput(); // PutCorsPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putCorsPolicy(xAmzTarget, putCorsPolicyInput, opts, (error, data, response) => {
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
 **putCorsPolicyInput** | [**PutCorsPolicyInput**](PutCorsPolicyInput.md)|  | 
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


## putLifecyclePolicy

> Object putLifecyclePolicy(xAmzTarget, putLifecyclePolicyInput, opts)



&lt;p&gt;Writes an object lifecycle policy to a container. If the container already has an object lifecycle policy, the service replaces the existing policy with the new policy. It takes up to 20 minutes for the change to take effect.&lt;/p&gt; &lt;p&gt;For information about how to construct an object lifecycle policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-components.html\&quot;&gt;Components of an Object Lifecycle Policy&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putLifecyclePolicyInput = new AwsElementalMediaStore.PutLifecyclePolicyInput(); // PutLifecyclePolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putLifecyclePolicy(xAmzTarget, putLifecyclePolicyInput, opts, (error, data, response) => {
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
 **putLifecyclePolicyInput** | [**PutLifecyclePolicyInput**](PutLifecyclePolicyInput.md)|  | 
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


## putMetricPolicy

> Object putMetricPolicy(xAmzTarget, putMetricPolicyInput, opts)



The metric policy that you want to add to the container. A metric policy allows AWS Elemental MediaStore to send metrics to Amazon CloudWatch. It takes up to 20 minutes for the new policy to take effect.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putMetricPolicyInput = new AwsElementalMediaStore.PutMetricPolicyInput(); // PutMetricPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putMetricPolicy(xAmzTarget, putMetricPolicyInput, opts, (error, data, response) => {
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
 **putMetricPolicyInput** | [**PutMetricPolicyInput**](PutMetricPolicyInput.md)|  | 
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


## startAccessLogging

> Object startAccessLogging(xAmzTarget, startAccessLoggingInput, opts)



Starts access logging on the specified container. When you enable access logging on a container, MediaStore delivers access logs for objects stored in that container to Amazon CloudWatch Logs.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startAccessLoggingInput = new AwsElementalMediaStore.StartAccessLoggingInput(); // StartAccessLoggingInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startAccessLogging(xAmzTarget, startAccessLoggingInput, opts, (error, data, response) => {
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
 **startAccessLoggingInput** | [**StartAccessLoggingInput**](StartAccessLoggingInput.md)|  | 
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


## stopAccessLogging

> Object stopAccessLogging(xAmzTarget, stopAccessLoggingInput, opts)



Stops access logging on the specified container. When you stop access logging on a container, MediaStore stops sending access logs to Amazon CloudWatch Logs. These access logs are not saved and are not retrievable.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopAccessLoggingInput = new AwsElementalMediaStore.StopAccessLoggingInput(); // StopAccessLoggingInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopAccessLogging(xAmzTarget, stopAccessLoggingInput, opts, (error, data, response) => {
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
 **stopAccessLoggingInput** | [**StopAccessLoggingInput**](StopAccessLoggingInput.md)|  | 
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


## tagResource

> Object tagResource(xAmzTarget, tagResourceInput, opts)



Adds tags to the specified AWS Elemental MediaStore container. Tags are key:value pairs that you can associate with AWS resources. For example, the tag key might be \&quot;customer\&quot; and the tag value might be \&quot;companyA.\&quot; You can specify one or more tags to add to each container. You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html\&quot;&gt;Tagging Resources in MediaStore&lt;/a&gt;.

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceInput = new AwsElementalMediaStore.TagResourceInput(); // TagResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceInput, opts, (error, data, response) => {
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
 **tagResourceInput** | [**TagResourceInput**](TagResourceInput.md)|  | 
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

> Object untagResource(xAmzTarget, untagResourceInput, opts)



Removes tags from the specified container. You can specify one or more tags to remove. 

### Example

```javascript
import AwsElementalMediaStore from 'aws_elemental_media_store';
let defaultClient = AwsElementalMediaStore.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStore.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceInput = new AwsElementalMediaStore.UntagResourceInput(); // UntagResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceInput, opts, (error, data, response) => {
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
 **untagResourceInput** | [**UntagResourceInput**](UntagResourceInput.md)|  | 
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

