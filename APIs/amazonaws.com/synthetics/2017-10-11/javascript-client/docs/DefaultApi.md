# Synthetics.DefaultApi

All URIs are relative to *http://synthetics.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateResource**](DefaultApi.md#associateResource) | **PATCH** /group/{groupIdentifier}/associate | 
[**createCanary**](DefaultApi.md#createCanary) | **POST** /canary | 
[**createGroup**](DefaultApi.md#createGroup) | **POST** /group | 
[**deleteCanary**](DefaultApi.md#deleteCanary) | **DELETE** /canary/{name} | 
[**deleteGroup**](DefaultApi.md#deleteGroup) | **DELETE** /group/{groupIdentifier} | 
[**describeCanaries**](DefaultApi.md#describeCanaries) | **POST** /canaries | 
[**describeCanariesLastRun**](DefaultApi.md#describeCanariesLastRun) | **POST** /canaries/last-run | 
[**describeRuntimeVersions**](DefaultApi.md#describeRuntimeVersions) | **POST** /runtime-versions | 
[**disassociateResource**](DefaultApi.md#disassociateResource) | **PATCH** /group/{groupIdentifier}/disassociate | 
[**getCanary**](DefaultApi.md#getCanary) | **GET** /canary/{name} | 
[**getCanaryRuns**](DefaultApi.md#getCanaryRuns) | **POST** /canary/{name}/runs | 
[**getGroup**](DefaultApi.md#getGroup) | **GET** /group/{groupIdentifier} | 
[**listAssociatedGroups**](DefaultApi.md#listAssociatedGroups) | **POST** /resource/{resourceArn}/groups | 
[**listGroupResources**](DefaultApi.md#listGroupResources) | **POST** /group/{groupIdentifier}/resources | 
[**listGroups**](DefaultApi.md#listGroups) | **POST** /groups | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**startCanary**](DefaultApi.md#startCanary) | **POST** /canary/{name}/start | 
[**stopCanary**](DefaultApi.md#stopCanary) | **POST** /canary/{name}/stop | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateCanary**](DefaultApi.md#updateCanary) | **PATCH** /canary/{name} | 



## associateResource

> Object associateResource(groupIdentifier, associateResourceRequest, opts)



&lt;p&gt;Associates a canary with a group. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group. &lt;/p&gt; &lt;p&gt;You must run this operation in the Region where the canary exists.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let groupIdentifier = "groupIdentifier_example"; // String | Specifies the group. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.
let associateResourceRequest = new Synthetics.AssociateResourceRequest(); // AssociateResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateResource(groupIdentifier, associateResourceRequest, opts, (error, data, response) => {
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
 **groupIdentifier** | **String**| Specifies the group. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;. | 
 **associateResourceRequest** | [**AssociateResourceRequest**](AssociateResourceRequest.md)|  | 
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


## createCanary

> CreateCanaryResponse createCanary(createCanaryRequest, opts)



&lt;p&gt;Creates a canary. Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once. &lt;/p&gt; &lt;p&gt;Do not use &lt;code&gt;CreateCanary&lt;/code&gt; to modify an existing canary. Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html\&quot;&gt;UpdateCanary&lt;/a&gt; instead.&lt;/p&gt; &lt;p&gt;To create canaries, you must have the &lt;code&gt;CloudWatchSyntheticsFullAccess&lt;/code&gt; policy. If you are creating a new IAM role for the canary, you also need the &lt;code&gt;iam:CreateRole&lt;/code&gt;, &lt;code&gt;iam:CreatePolicy&lt;/code&gt; and &lt;code&gt;iam:AttachRolePolicy&lt;/code&gt; permissions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles\&quot;&gt;Necessary Roles and Permissions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html\&quot;&gt;Security Considerations for Synthetics Canaries&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let createCanaryRequest = new Synthetics.CreateCanaryRequest(); // CreateCanaryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCanary(createCanaryRequest, opts, (error, data, response) => {
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
 **createCanaryRequest** | [**CreateCanaryRequest**](CreateCanaryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCanaryResponse**](CreateCanaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGroup

> CreateGroupResponse createGroup(createGroupRequest, opts)



&lt;p&gt;Creates a group which you can use to associate canaries with each other, including cross-Region canaries. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group. &lt;/p&gt; &lt;p&gt;Groups are global resources. When you create a group, it is replicated across Amazon Web Services Regions, and you can view it and add canaries to it from any Region. Although the group ARN format reflects the Region name where it was created, a group is not constrained to any Region. This means that you can put canaries from multiple Regions into the same group, and then use that group to view and manage all of those canaries in a single view.&lt;/p&gt; &lt;p&gt;Groups are supported in all Regions except the Regions that are disabled by default. For more information about these Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable\&quot;&gt;Enabling a Region&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each group can contain as many as 10 canaries. You can have as many as 20 groups in your account. Any single canary can be a member of up to 10 groups.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let createGroupRequest = new Synthetics.CreateGroupRequest(); // CreateGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createGroup(createGroupRequest, opts, (error, data, response) => {
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
 **createGroupRequest** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateGroupResponse**](CreateGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCanary

> Object deleteCanary(name, opts)



&lt;p&gt;Permanently deletes the specified canary.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;DeleteLambda&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;, CloudWatch Synthetics also deletes the Lambda functions and layers that are used by the canary.&lt;/p&gt; &lt;p&gt;Other resources used and created by the canary are not automatically deleted. After you delete a canary that you do not intend to use again, you should also delete the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The CloudWatch alarms created for this canary. These alarms have a name of &lt;code&gt;Synthetics-SharpDrop-Alarm-&lt;i&gt;MyCanaryName&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon S3 objects and buckets, such as the canary&#39;s artifact location.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IAM roles created for the canary. If they were created in the console, these roles have the name &lt;code&gt; role/service-role/CloudWatchSyntheticsRole-&lt;i&gt;MyCanaryName&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CloudWatch Logs log groups created for the canary. These logs groups have the name &lt;code&gt;/aws/lambda/cwsyn-&lt;i&gt;MyCanaryName&lt;/i&gt; &lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Before you delete a canary, you might want to use &lt;code&gt;GetCanary&lt;/code&gt; to display the information about this canary. Make note of the information returned by this operation so that you can delete these resources after you delete the canary.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let name = "name_example"; // String | The name of the canary that you want to delete. To find the names of your canaries, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'deleteLambda': true // Boolean | <p>Specifies whether to also delete the Lambda functions and layers used by this canary. The default is false.</p> <p>Type: Boolean</p>
};
apiInstance.deleteCanary(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the canary that you want to delete. To find the names of your canaries, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;DescribeCanaries&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **deleteLambda** | **Boolean**| &lt;p&gt;Specifies whether to also delete the Lambda functions and layers used by this canary. The default is false.&lt;/p&gt; &lt;p&gt;Type: Boolean&lt;/p&gt; | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGroup

> Object deleteGroup(groupIdentifier, opts)



&lt;p&gt;Deletes a group. The group doesn&#39;t need to be empty to be deleted. If there are canaries in the group, they are not deleted when you delete the group. &lt;/p&gt; &lt;p&gt;Groups are a global resource that appear in all Regions, but the request to delete a group must be made from its home Region. You can find the home Region of a group within its ARN.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let groupIdentifier = "groupIdentifier_example"; // String | Specifies which group to delete. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteGroup(groupIdentifier, opts, (error, data, response) => {
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
 **groupIdentifier** | **String**| Specifies which group to delete. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;. | 
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


## describeCanaries

> DescribeCanariesResponse describeCanaries(describeCanariesRequest, opts)



&lt;p&gt;This operation returns a list of the canaries in your account, along with full details about each canary.&lt;/p&gt; &lt;p&gt;This operation supports resource-level authorization using an IAM policy and the &lt;code&gt;Names&lt;/code&gt; parameter. If you specify the &lt;code&gt;Names&lt;/code&gt; parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.&lt;/p&gt; &lt;p&gt;You are required to use the &lt;code&gt;Names&lt;/code&gt; parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html\&quot;&gt; Limiting a user to viewing specific canaries&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let describeCanariesRequest = new Synthetics.DescribeCanariesRequest(); // DescribeCanariesRequest | 
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
apiInstance.describeCanaries(describeCanariesRequest, opts, (error, data, response) => {
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
 **describeCanariesRequest** | [**DescribeCanariesRequest**](DescribeCanariesRequest.md)|  | 
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

[**DescribeCanariesResponse**](DescribeCanariesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeCanariesLastRun

> DescribeCanariesLastRunResponse describeCanariesLastRun(describeCanariesLastRunRequest, opts)



&lt;p&gt;Use this operation to see information from the most recent run of each canary that you have created.&lt;/p&gt; &lt;p&gt;This operation supports resource-level authorization using an IAM policy and the &lt;code&gt;Names&lt;/code&gt; parameter. If you specify the &lt;code&gt;Names&lt;/code&gt; parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.&lt;/p&gt; &lt;p&gt;You are required to use the &lt;code&gt;Names&lt;/code&gt; parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html\&quot;&gt; Limiting a user to viewing specific canaries&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let describeCanariesLastRunRequest = new Synthetics.DescribeCanariesLastRunRequest(); // DescribeCanariesLastRunRequest | 
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
apiInstance.describeCanariesLastRun(describeCanariesLastRunRequest, opts, (error, data, response) => {
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
 **describeCanariesLastRunRequest** | [**DescribeCanariesLastRunRequest**](DescribeCanariesLastRunRequest.md)|  | 
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

[**DescribeCanariesLastRunResponse**](DescribeCanariesLastRunResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeRuntimeVersions

> DescribeRuntimeVersionsResponse describeRuntimeVersions(describeRuntimeVersionsRequest, opts)



Returns a list of Synthetics canary runtime versions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\&quot;&gt; Canary Runtime Versions&lt;/a&gt;.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let describeRuntimeVersionsRequest = new Synthetics.DescribeRuntimeVersionsRequest(); // DescribeRuntimeVersionsRequest | 
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
apiInstance.describeRuntimeVersions(describeRuntimeVersionsRequest, opts, (error, data, response) => {
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
 **describeRuntimeVersionsRequest** | [**DescribeRuntimeVersionsRequest**](DescribeRuntimeVersionsRequest.md)|  | 
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

[**DescribeRuntimeVersionsResponse**](DescribeRuntimeVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateResource

> Object disassociateResource(groupIdentifier, disassociateResourceRequest, opts)



Removes a canary from a group. You must run this operation in the Region where the canary exists.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let groupIdentifier = "groupIdentifier_example"; // String | Specifies the group. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.
let disassociateResourceRequest = new Synthetics.DisassociateResourceRequest(); // DisassociateResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateResource(groupIdentifier, disassociateResourceRequest, opts, (error, data, response) => {
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
 **groupIdentifier** | **String**| Specifies the group. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;. | 
 **disassociateResourceRequest** | [**DisassociateResourceRequest**](DisassociateResourceRequest.md)|  | 
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


## getCanary

> GetCanaryResponse getCanary(name, opts)



Retrieves complete information about one canary. You must specify the name of the canary that you want. To get a list of canaries and their names, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;DescribeCanaries&lt;/a&gt;.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let name = "name_example"; // String | The name of the canary that you want details for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCanary(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the canary that you want details for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCanaryResponse**](GetCanaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCanaryRuns

> GetCanaryRunsResponse getCanaryRuns(name, getCanaryRunsRequest, opts)



Retrieves a list of runs for a specified canary.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let name = "name_example"; // String | The name of the canary that you want to see runs for.
let getCanaryRunsRequest = new Synthetics.GetCanaryRunsRequest(); // GetCanaryRunsRequest | 
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
apiInstance.getCanaryRuns(name, getCanaryRunsRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the canary that you want to see runs for. | 
 **getCanaryRunsRequest** | [**GetCanaryRunsRequest**](GetCanaryRunsRequest.md)|  | 
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

[**GetCanaryRunsResponse**](GetCanaryRunsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getGroup

> GetGroupResponse getGroup(groupIdentifier, opts)



Returns information about one group. Groups are a global resource, so you can use this operation from any Region.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let groupIdentifier = "groupIdentifier_example"; // String | Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGroup(groupIdentifier, opts, (error, data, response) => {
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
 **groupIdentifier** | **String**| Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGroupResponse**](GetGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssociatedGroups

> ListAssociatedGroupsResponse listAssociatedGroups(resourceArn, listAssociatedGroupsRequest, opts)



Returns a list of the groups that the specified canary is associated with. The canary that you specify must be in the current Region.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the canary that you want to view groups for.
let listAssociatedGroupsRequest = new Synthetics.ListAssociatedGroupsRequest(); // ListAssociatedGroupsRequest | 
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
apiInstance.listAssociatedGroups(resourceArn, listAssociatedGroupsRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The ARN of the canary that you want to view groups for. | 
 **listAssociatedGroupsRequest** | [**ListAssociatedGroupsRequest**](ListAssociatedGroupsRequest.md)|  | 
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

[**ListAssociatedGroupsResponse**](ListAssociatedGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGroupResources

> ListGroupResourcesResponse listGroupResources(groupIdentifier, listGroupResourcesRequest, opts)



This operation returns a list of the ARNs of the canaries that are associated with the specified group.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let groupIdentifier = "groupIdentifier_example"; // String | Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.
let listGroupResourcesRequest = new Synthetics.ListGroupResourcesRequest(); // ListGroupResourcesRequest | 
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
apiInstance.listGroupResources(groupIdentifier, listGroupResourcesRequest, opts, (error, data, response) => {
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
 **groupIdentifier** | **String**| Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;. | 
 **listGroupResourcesRequest** | [**ListGroupResourcesRequest**](ListGroupResourcesRequest.md)|  | 
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

[**ListGroupResourcesResponse**](ListGroupResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGroups

> ListGroupsResponse listGroups(listGroupsRequest, opts)



Returns a list of all groups in the account, displaying their names, unique IDs, and ARNs. The groups from all Regions are returned.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let listGroupsRequest = new Synthetics.ListGroupsRequest(); // ListGroupsRequest | 
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
apiInstance.listGroups(listGroupsRequest, opts, (error, data, response) => {
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
 **listGroupsRequest** | [**ListGroupsRequest**](ListGroupsRequest.md)|  | 
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

[**ListGroupsResponse**](ListGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Displays the tags associated with a canary or group.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The ARN of the canary or group that you want to view tags for.</p> <p>The ARN format of a canary is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:canary:<i>canary-name</i> </code>.</p> <p>The ARN format of a group is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:group:<i>group-name</i> </code> </p>
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
 **resourceArn** | **String**| &lt;p&gt;The ARN of the canary or group that you want to view tags for.&lt;/p&gt; &lt;p&gt;The ARN format of a canary is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:canary:&lt;i&gt;canary-name&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The ARN format of a group is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:group:&lt;i&gt;group-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; | 
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


## startCanary

> Object startCanary(name, opts)



Use this operation to run a canary that has already been created. The frequency of the canary runs is determined by the value of the canary&#39;s &lt;code&gt;Schedule&lt;/code&gt;. To see a canary&#39;s schedule, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html\&quot;&gt;GetCanary&lt;/a&gt;.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let name = "name_example"; // String | The name of the canary that you want to run. To find canary names, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startCanary(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the canary that you want to run. To find canary names, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;DescribeCanaries&lt;/a&gt;. | 
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


## stopCanary

> Object stopCanary(name, opts)



&lt;p&gt;Stops the canary to prevent all future runs. If the canary is currently running,the run that is in progress completes on its own, publishes metrics, and uploads artifacts, but it is not recorded in Synthetics as a completed run.&lt;/p&gt; &lt;p&gt;You can use &lt;code&gt;StartCanary&lt;/code&gt; to start it running again with the canary’s current schedule at any point in the future. &lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let name = "name_example"; // String | The name of the canary that you want to stop. To find the names of your canaries, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">ListCanaries</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopCanary(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the canary that you want to stop. To find the names of your canaries, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;ListCanaries&lt;/a&gt;. | 
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


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Assigns one or more tags (key-value pairs) to the specified canary or group. &lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a canary or group.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The ARN of the canary or group that you're adding tags to.</p> <p>The ARN format of a canary is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:canary:<i>canary-name</i> </code>.</p> <p>The ARN format of a group is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:group:<i>group-name</i> </code> </p>
let tagResourceRequest = new Synthetics.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| &lt;p&gt;The ARN of the canary or group that you&#39;re adding tags to.&lt;/p&gt; &lt;p&gt;The ARN format of a canary is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:canary:&lt;i&gt;canary-name&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The ARN format of a group is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:group:&lt;i&gt;group-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; | 
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



Removes one or more tags from the specified resource.

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The ARN of the canary or group that you're removing tags from.</p> <p>The ARN format of a canary is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:canary:<i>canary-name</i> </code>.</p> <p>The ARN format of a group is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:group:<i>group-name</i> </code> </p>
let tagKeys = ["null"]; // [String] | The list of tag keys to remove from the resource.
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
 **resourceArn** | **String**| &lt;p&gt;The ARN of the canary or group that you&#39;re removing tags from.&lt;/p&gt; &lt;p&gt;The ARN format of a canary is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:canary:&lt;i&gt;canary-name&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The ARN format of a group is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:group:&lt;i&gt;group-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; | 
 **tagKeys** | [**[String]**](String.md)| The list of tag keys to remove from the resource. | 
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


## updateCanary

> Object updateCanary(name, updateCanaryRequest, opts)



&lt;p&gt;Updates the configuration of a canary that has already been created.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation to update the tags of an existing canary. To change the tags of an existing canary, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import Synthetics from 'synthetics';
let defaultClient = Synthetics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new Synthetics.DefaultApi();
let name = "name_example"; // String | <p>The name of the canary that you want to update. To find the names of your canaries, use <a href=\"https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\">DescribeCanaries</a>.</p> <p>You cannot change the name of a canary that has already been created.</p>
let updateCanaryRequest = new Synthetics.UpdateCanaryRequest(); // UpdateCanaryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateCanary(name, updateCanaryRequest, opts, (error, data, response) => {
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
 **name** | **String**| &lt;p&gt;The name of the canary that you want to update. To find the names of your canaries, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;DescribeCanaries&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You cannot change the name of a canary that has already been created.&lt;/p&gt; | 
 **updateCanaryRequest** | [**UpdateCanaryRequest**](UpdateCanaryRequest.md)|  | 
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

