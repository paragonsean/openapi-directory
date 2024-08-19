# AwsS3Control.DefaultApi

All URIs are relative to *http://s3-control.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccessPoint**](DefaultApi.md#createAccessPoint) | **PUT** /v20180820/accesspoint/{name}#x-amz-account-id | 
[**createAccessPointForObjectLambda**](DefaultApi.md#createAccessPointForObjectLambda) | **PUT** /v20180820/accesspointforobjectlambda/{name}#x-amz-account-id | 
[**createBucket**](DefaultApi.md#createBucket) | **PUT** /v20180820/bucket/{name} | 
[**createJob**](DefaultApi.md#createJob) | **POST** /v20180820/jobs#x-amz-account-id | 
[**createMultiRegionAccessPoint**](DefaultApi.md#createMultiRegionAccessPoint) | **POST** /v20180820/async-requests/mrap/create#x-amz-account-id | 
[**deleteAccessPoint**](DefaultApi.md#deleteAccessPoint) | **DELETE** /v20180820/accesspoint/{name}#x-amz-account-id | 
[**deleteAccessPointForObjectLambda**](DefaultApi.md#deleteAccessPointForObjectLambda) | **DELETE** /v20180820/accesspointforobjectlambda/{name}#x-amz-account-id | 
[**deleteAccessPointPolicy**](DefaultApi.md#deleteAccessPointPolicy) | **DELETE** /v20180820/accesspoint/{name}/policy#x-amz-account-id | 
[**deleteAccessPointPolicyForObjectLambda**](DefaultApi.md#deleteAccessPointPolicyForObjectLambda) | **DELETE** /v20180820/accesspointforobjectlambda/{name}/policy#x-amz-account-id | 
[**deleteBucket**](DefaultApi.md#deleteBucket) | **DELETE** /v20180820/bucket/{name}#x-amz-account-id | 
[**deleteBucketLifecycleConfiguration**](DefaultApi.md#deleteBucketLifecycleConfiguration) | **DELETE** /v20180820/bucket/{name}/lifecycleconfiguration#x-amz-account-id | 
[**deleteBucketPolicy**](DefaultApi.md#deleteBucketPolicy) | **DELETE** /v20180820/bucket/{name}/policy#x-amz-account-id | 
[**deleteBucketReplication**](DefaultApi.md#deleteBucketReplication) | **DELETE** /v20180820/bucket/{name}/replication#x-amz-account-id | 
[**deleteBucketTagging**](DefaultApi.md#deleteBucketTagging) | **DELETE** /v20180820/bucket/{name}/tagging#x-amz-account-id | 
[**deleteJobTagging**](DefaultApi.md#deleteJobTagging) | **DELETE** /v20180820/jobs/{id}/tagging#x-amz-account-id | 
[**deleteMultiRegionAccessPoint**](DefaultApi.md#deleteMultiRegionAccessPoint) | **POST** /v20180820/async-requests/mrap/delete#x-amz-account-id | 
[**deletePublicAccessBlock**](DefaultApi.md#deletePublicAccessBlock) | **DELETE** /v20180820/configuration/publicAccessBlock#x-amz-account-id | 
[**deleteStorageLensConfiguration**](DefaultApi.md#deleteStorageLensConfiguration) | **DELETE** /v20180820/storagelens/{storagelensid}#x-amz-account-id | 
[**deleteStorageLensConfigurationTagging**](DefaultApi.md#deleteStorageLensConfigurationTagging) | **DELETE** /v20180820/storagelens/{storagelensid}/tagging#x-amz-account-id | 
[**describeJob**](DefaultApi.md#describeJob) | **GET** /v20180820/jobs/{id}#x-amz-account-id | 
[**describeMultiRegionAccessPointOperation**](DefaultApi.md#describeMultiRegionAccessPointOperation) | **GET** /v20180820/async-requests/mrap/{request_token}#x-amz-account-id | 
[**getAccessPoint**](DefaultApi.md#getAccessPoint) | **GET** /v20180820/accesspoint/{name}#x-amz-account-id | 
[**getAccessPointConfigurationForObjectLambda**](DefaultApi.md#getAccessPointConfigurationForObjectLambda) | **GET** /v20180820/accesspointforobjectlambda/{name}/configuration#x-amz-account-id | 
[**getAccessPointForObjectLambda**](DefaultApi.md#getAccessPointForObjectLambda) | **GET** /v20180820/accesspointforobjectlambda/{name}#x-amz-account-id | 
[**getAccessPointPolicy**](DefaultApi.md#getAccessPointPolicy) | **GET** /v20180820/accesspoint/{name}/policy#x-amz-account-id | 
[**getAccessPointPolicyForObjectLambda**](DefaultApi.md#getAccessPointPolicyForObjectLambda) | **GET** /v20180820/accesspointforobjectlambda/{name}/policy#x-amz-account-id | 
[**getAccessPointPolicyStatus**](DefaultApi.md#getAccessPointPolicyStatus) | **GET** /v20180820/accesspoint/{name}/policyStatus#x-amz-account-id | 
[**getAccessPointPolicyStatusForObjectLambda**](DefaultApi.md#getAccessPointPolicyStatusForObjectLambda) | **GET** /v20180820/accesspointforobjectlambda/{name}/policyStatus#x-amz-account-id | 
[**getBucket**](DefaultApi.md#getBucket) | **GET** /v20180820/bucket/{name}#x-amz-account-id | 
[**getBucketLifecycleConfiguration**](DefaultApi.md#getBucketLifecycleConfiguration) | **GET** /v20180820/bucket/{name}/lifecycleconfiguration#x-amz-account-id | 
[**getBucketPolicy**](DefaultApi.md#getBucketPolicy) | **GET** /v20180820/bucket/{name}/policy#x-amz-account-id | 
[**getBucketReplication**](DefaultApi.md#getBucketReplication) | **GET** /v20180820/bucket/{name}/replication#x-amz-account-id | 
[**getBucketTagging**](DefaultApi.md#getBucketTagging) | **GET** /v20180820/bucket/{name}/tagging#x-amz-account-id | 
[**getBucketVersioning**](DefaultApi.md#getBucketVersioning) | **GET** /v20180820/bucket/{name}/versioning#x-amz-account-id | 
[**getJobTagging**](DefaultApi.md#getJobTagging) | **GET** /v20180820/jobs/{id}/tagging#x-amz-account-id | 
[**getMultiRegionAccessPoint**](DefaultApi.md#getMultiRegionAccessPoint) | **GET** /v20180820/mrap/instances/{name}#x-amz-account-id | 
[**getMultiRegionAccessPointPolicy**](DefaultApi.md#getMultiRegionAccessPointPolicy) | **GET** /v20180820/mrap/instances/{name}/policy#x-amz-account-id | 
[**getMultiRegionAccessPointPolicyStatus**](DefaultApi.md#getMultiRegionAccessPointPolicyStatus) | **GET** /v20180820/mrap/instances/{name}/policystatus#x-amz-account-id | 
[**getMultiRegionAccessPointRoutes**](DefaultApi.md#getMultiRegionAccessPointRoutes) | **GET** /v20180820/mrap/instances/{mrap}/routes#x-amz-account-id | 
[**getPublicAccessBlock**](DefaultApi.md#getPublicAccessBlock) | **GET** /v20180820/configuration/publicAccessBlock#x-amz-account-id | 
[**getStorageLensConfiguration**](DefaultApi.md#getStorageLensConfiguration) | **GET** /v20180820/storagelens/{storagelensid}#x-amz-account-id | 
[**getStorageLensConfigurationTagging**](DefaultApi.md#getStorageLensConfigurationTagging) | **GET** /v20180820/storagelens/{storagelensid}/tagging#x-amz-account-id | 
[**listAccessPoints**](DefaultApi.md#listAccessPoints) | **GET** /v20180820/accesspoint#x-amz-account-id | 
[**listAccessPointsForObjectLambda**](DefaultApi.md#listAccessPointsForObjectLambda) | **GET** /v20180820/accesspointforobjectlambda#x-amz-account-id | 
[**listJobs**](DefaultApi.md#listJobs) | **GET** /v20180820/jobs#x-amz-account-id | 
[**listMultiRegionAccessPoints**](DefaultApi.md#listMultiRegionAccessPoints) | **GET** /v20180820/mrap/instances#x-amz-account-id | 
[**listRegionalBuckets**](DefaultApi.md#listRegionalBuckets) | **GET** /v20180820/bucket#x-amz-account-id | 
[**listStorageLensConfigurations**](DefaultApi.md#listStorageLensConfigurations) | **GET** /v20180820/storagelens#x-amz-account-id | 
[**putAccessPointConfigurationForObjectLambda**](DefaultApi.md#putAccessPointConfigurationForObjectLambda) | **PUT** /v20180820/accesspointforobjectlambda/{name}/configuration#x-amz-account-id | 
[**putAccessPointPolicy**](DefaultApi.md#putAccessPointPolicy) | **PUT** /v20180820/accesspoint/{name}/policy#x-amz-account-id | 
[**putAccessPointPolicyForObjectLambda**](DefaultApi.md#putAccessPointPolicyForObjectLambda) | **PUT** /v20180820/accesspointforobjectlambda/{name}/policy#x-amz-account-id | 
[**putBucketLifecycleConfiguration**](DefaultApi.md#putBucketLifecycleConfiguration) | **PUT** /v20180820/bucket/{name}/lifecycleconfiguration#x-amz-account-id | 
[**putBucketPolicy**](DefaultApi.md#putBucketPolicy) | **PUT** /v20180820/bucket/{name}/policy#x-amz-account-id | 
[**putBucketReplication**](DefaultApi.md#putBucketReplication) | **PUT** /v20180820/bucket/{name}/replication#x-amz-account-id | 
[**putBucketTagging**](DefaultApi.md#putBucketTagging) | **PUT** /v20180820/bucket/{name}/tagging#x-amz-account-id | 
[**putBucketVersioning**](DefaultApi.md#putBucketVersioning) | **PUT** /v20180820/bucket/{name}/versioning#x-amz-account-id | 
[**putJobTagging**](DefaultApi.md#putJobTagging) | **PUT** /v20180820/jobs/{id}/tagging#x-amz-account-id | 
[**putMultiRegionAccessPointPolicy**](DefaultApi.md#putMultiRegionAccessPointPolicy) | **POST** /v20180820/async-requests/mrap/put-policy#x-amz-account-id | 
[**putPublicAccessBlock**](DefaultApi.md#putPublicAccessBlock) | **PUT** /v20180820/configuration/publicAccessBlock#x-amz-account-id | 
[**putStorageLensConfiguration**](DefaultApi.md#putStorageLensConfiguration) | **PUT** /v20180820/storagelens/{storagelensid}#x-amz-account-id | 
[**putStorageLensConfigurationTagging**](DefaultApi.md#putStorageLensConfigurationTagging) | **PUT** /v20180820/storagelens/{storagelensid}/tagging#x-amz-account-id | 
[**submitMultiRegionAccessPointRoutes**](DefaultApi.md#submitMultiRegionAccessPointRoutes) | **PATCH** /v20180820/mrap/instances/{mrap}/routes#x-amz-account-id | 
[**updateJobPriority**](DefaultApi.md#updateJobPriority) | **POST** /v20180820/jobs/{id}/priority#x-amz-account-id&amp;priority | 
[**updateJobStatus**](DefaultApi.md#updateJobStatus) | **POST** /v20180820/jobs/{id}/status#x-amz-account-id&amp;requestedJobStatus | 



## createAccessPoint

> CreateAccessPointResult createAccessPoint(xAmzAccountId, name, createAccessPointRequest, opts)



&lt;p&gt;Creates an access point and associates it with the specified bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html\&quot;&gt;Managing Data Access with Amazon S3 Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt; &lt;note&gt; &lt;p&gt;S3 on Outposts only supports VPC-style access points. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt; Accessing Amazon S3 on Outposts using virtual private cloud (VPC) only access points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html#API_control_CreateAccessPoint_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;The following actions are related to &lt;code&gt;CreateAccessPoint&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html\&quot;&gt;GetAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html\&quot;&gt;DeleteAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html\&quot;&gt;ListAccessPoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the account that owns the specified access point.
let name = "name_example"; // String | The name you want to assign to this access point.
let createAccessPointRequest = new AwsS3Control.CreateAccessPointRequest(); // CreateAccessPointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAccessPoint(xAmzAccountId, name, createAccessPointRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the account that owns the specified access point. | 
 **name** | **String**| The name you want to assign to this access point. | 
 **createAccessPointRequest** | [**CreateAccessPointRequest**](CreateAccessPointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAccessPointResult**](CreateAccessPointResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createAccessPointForObjectLambda

> CreateAccessPointForObjectLambdaResult createAccessPointForObjectLambda(xAmzAccountId, name, createAccessPointForObjectLambdaRequest, opts)



&lt;p&gt;Creates an Object Lambda Access Point. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html\&quot;&gt;Transforming objects with Object Lambda Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;CreateAccessPointForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html\&quot;&gt;DeleteAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html\&quot;&gt;GetAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html\&quot;&gt;ListAccessPointsForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for owner of the specified Object Lambda Access Point.
let name = "name_example"; // String | The name you want to assign to this Object Lambda Access Point.
let createAccessPointForObjectLambdaRequest = new AwsS3Control.CreateAccessPointForObjectLambdaRequest(); // CreateAccessPointForObjectLambdaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAccessPointForObjectLambda(xAmzAccountId, name, createAccessPointForObjectLambdaRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for owner of the specified Object Lambda Access Point. | 
 **name** | **String**| The name you want to assign to this Object Lambda Access Point. | 
 **createAccessPointForObjectLambdaRequest** | [**CreateAccessPointForObjectLambdaRequest**](CreateAccessPointForObjectLambdaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAccessPointForObjectLambdaResult**](CreateAccessPointForObjectLambdaResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createBucket

> CreateBucketResult createBucket(name, createBucketRequest, opts)



&lt;note&gt; &lt;p&gt;This action creates an Amazon S3 on Outposts bucket. To create an S3 bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html\&quot;&gt;Create Bucket&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a new Outposts bucket. By creating the bucket, you become the bucket owner. To create an Outposts bucket, you must have S3 on Outposts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Not every string is an acceptable bucket name. For information on bucket naming restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules\&quot;&gt;Working with Amazon S3 Buckets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;S3 on Outposts buckets support:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Tags&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;LifecycleConfigurations for deleting expired objects&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For a complete list of restrictions and Amazon S3 feature limitations on S3 on Outposts, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OnOutpostsRestrictionsLimitations.html\&quot;&gt; Amazon S3 on Outposts Restrictions and Limitations&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and &lt;code&gt;x-amz-outpost-id&lt;/code&gt; in your API request, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html#API_control_CreateBucket_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;CreateBucket&lt;/code&gt; for Amazon S3 on Outposts:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html\&quot;&gt;PutObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html\&quot;&gt;GetBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html\&quot;&gt;DeleteBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html\&quot;&gt;CreateAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html\&quot;&gt;PutAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let name = "name_example"; // String | The name of the bucket.
let createBucketRequest = new AwsS3Control.CreateBucketRequest(); // CreateBucketRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzAcl': "xAmzAcl_example", // String | <p>The canned ACL to apply to the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
  'xAmzGrantFullControl': "xAmzGrantFullControl_example", // String | <p>Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
  'xAmzGrantRead': "xAmzGrantRead_example", // String | <p>Allows grantee to list the objects in the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
  'xAmzGrantReadAcp': "xAmzGrantReadAcp_example", // String | <p>Allows grantee to read the bucket ACL.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
  'xAmzGrantWrite': "xAmzGrantWrite_example", // String | <p>Allows grantee to create, overwrite, and delete any object in the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
  'xAmzGrantWriteAcp': "xAmzGrantWriteAcp_example", // String | <p>Allows grantee to write the ACL for the applicable bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
  'xAmzBucketObjectLockEnabled': true, // Boolean | <p>Specifies whether you want S3 Object Lock to be enabled for the new bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
  'xAmzOutpostId': "xAmzOutpostId_example" // String | <p>The ID of the Outposts where the bucket is being created.</p> <note> <p>This ID is required by Amazon S3 on Outposts buckets.</p> </note>
};
apiInstance.createBucket(name, createBucketRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bucket. | 
 **createBucketRequest** | [**CreateBucketRequest**](CreateBucketRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzAcl** | **String**| &lt;p&gt;The canned ACL to apply to the bucket.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is not supported by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **xAmzGrantFullControl** | **String**| &lt;p&gt;Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is not supported by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **xAmzGrantRead** | **String**| &lt;p&gt;Allows grantee to list the objects in the bucket.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is not supported by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **xAmzGrantReadAcp** | **String**| &lt;p&gt;Allows grantee to read the bucket ACL.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is not supported by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **xAmzGrantWrite** | **String**| &lt;p&gt;Allows grantee to create, overwrite, and delete any object in the bucket.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is not supported by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **xAmzGrantWriteAcp** | **String**| &lt;p&gt;Allows grantee to write the ACL for the applicable bucket.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is not supported by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **xAmzBucketObjectLockEnabled** | **Boolean**| &lt;p&gt;Specifies whether you want S3 Object Lock to be enabled for the new bucket.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is not supported by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **xAmzOutpostId** | **String**| &lt;p&gt;The ID of the Outposts where the bucket is being created.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This ID is required by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 

### Return type

[**CreateBucketResult**](CreateBucketResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createJob

> CreateJobResult createJob(xAmzAccountId, createJobRequest, opts)



&lt;p&gt;You can use S3 Batch Operations to perform large-scale batch actions on Amazon S3 objects. Batch Operations can run a single action on lists of Amazon S3 objects that you specify. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html\&quot;&gt;S3 Batch Operations&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This action creates a S3 Batch Operations job.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html\&quot;&gt;DescribeJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html\&quot;&gt;ListJobs&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html\&quot;&gt;UpdateJobPriority&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html\&quot;&gt;UpdateJobStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobOperation.html\&quot;&gt;JobOperation&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID that creates the job.
let createJobRequest = new AwsS3Control.CreateJobRequest(); // CreateJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createJob(xAmzAccountId, createJobRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID that creates the job. | 
 **createJobRequest** | [**CreateJobRequest**](CreateJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateJobResult**](CreateJobResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createMultiRegionAccessPoint

> CreateMultiRegionAccessPointResult createMultiRegionAccessPoint(xAmzAccountId, createMultiRegionAccessPointRequest, opts)



&lt;p&gt;Creates a Multi-Region Access Point and associates it with the specified buckets. For more information about creating Multi-Region Access Points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html\&quot;&gt;Creating Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around managing Multi-Region Access Points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This request is asynchronous, meaning that you might receive a response before the command has completed. When this request provides a response, it provides a token that you can use to monitor the status of the request with &lt;code&gt;DescribeMultiRegionAccessPointOperation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;CreateMultiRegionAccessPoint&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html\&quot;&gt;DeleteMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html\&quot;&gt;DescribeMultiRegionAccessPointOperation&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html\&quot;&gt;GetMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html\&quot;&gt;ListMultiRegionAccessPoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point. The owner of the Multi-Region Access Point also must own the underlying buckets.
let createMultiRegionAccessPointRequest = new AwsS3Control.CreateMultiRegionAccessPointRequest(); // CreateMultiRegionAccessPointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMultiRegionAccessPoint(xAmzAccountId, createMultiRegionAccessPointRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. The owner of the Multi-Region Access Point also must own the underlying buckets. | 
 **createMultiRegionAccessPointRequest** | [**CreateMultiRegionAccessPointRequest**](CreateMultiRegionAccessPointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMultiRegionAccessPointResult**](CreateMultiRegionAccessPointResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## deleteAccessPoint

> deleteAccessPoint(xAmzAccountId, name, opts)



&lt;p&gt;Deletes the specified access point.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html#API_control_DeleteAccessPoint_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;DeleteAccessPoint&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html\&quot;&gt;CreateAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html\&quot;&gt;GetAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html\&quot;&gt;ListAccessPoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the account that owns the specified access point.
let name = "name_example"; // String | <p>The name of the access point you want to delete.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/accesspoint/&lt;my-accesspoint-name&gt;</code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccessPoint(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the account that owns the specified access point. | 
 **name** | **String**| &lt;p&gt;The name of the access point you want to delete.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/accesspoint/&amp;lt;my-accesspoint-name&amp;gt;&lt;/code&gt;. For example, to access the access point &lt;code&gt;reports-ap&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
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
- **Accept**: Not defined


## deleteAccessPointForObjectLambda

> deleteAccessPointForObjectLambda(xAmzAccountId, name, opts)



&lt;p&gt;Deletes the specified Object Lambda Access Point.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;DeleteAccessPointForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html\&quot;&gt;CreateAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html\&quot;&gt;GetAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html\&quot;&gt;ListAccessPointsForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let name = "name_example"; // String | The name of the access point you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccessPointForObjectLambda(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **name** | **String**| The name of the access point you want to delete. | 
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
- **Accept**: Not defined


## deleteAccessPointPolicy

> deleteAccessPointPolicy(xAmzAccountId, name, opts)



&lt;p&gt;Deletes the access point policy for the specified access point.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html#API_control_DeleteAccessPointPolicy_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;DeleteAccessPointPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html\&quot;&gt;PutAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html\&quot;&gt;GetAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified access point.
let name = "name_example"; // String | <p>The name of the access point whose policy you want to delete.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/accesspoint/&lt;my-accesspoint-name&gt;</code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccessPointPolicy(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified access point. | 
 **name** | **String**| &lt;p&gt;The name of the access point whose policy you want to delete.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/accesspoint/&amp;lt;my-accesspoint-name&amp;gt;&lt;/code&gt;. For example, to access the access point &lt;code&gt;reports-ap&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
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
- **Accept**: Not defined


## deleteAccessPointPolicyForObjectLambda

> deleteAccessPointPolicyForObjectLambda(xAmzAccountId, name, opts)



&lt;p&gt;Removes the resource policy for an Object Lambda Access Point.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;DeleteAccessPointPolicyForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html\&quot;&gt;GetAccessPointPolicyForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html\&quot;&gt;PutAccessPointPolicyForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let name = "name_example"; // String | The name of the Object Lambda Access Point you want to delete the policy for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccessPointPolicyForObjectLambda(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **name** | **String**| The name of the Object Lambda Access Point you want to delete the policy for. | 
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
- **Accept**: Not defined


## deleteBucket

> deleteBucket(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This action deletes an Amazon S3 on Outposts bucket. To delete an S3 bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html\&quot;&gt;DeleteBucket&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes the Amazon S3 on Outposts bucket. All objects (including all object versions and delete markers) in the bucket must be deleted before the bucket itself can be deleted. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html#API_control_DeleteBucket_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Related Resources&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html\&quot;&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html\&quot;&gt;GetBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html\&quot;&gt;DeleteObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID that owns the Outposts bucket.
let name = "name_example"; // String | <p>Specifies the bucket being deleted.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBucket(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID that owns the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;Specifies the bucket being deleted.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
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
- **Accept**: Not defined


## deleteBucketLifecycleConfiguration

> deleteBucketLifecycleConfiguration(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This action deletes an Amazon S3 on Outposts bucket&#39;s lifecycle configuration. To delete an S3 bucket&#39;s lifecycle configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html\&quot;&gt;DeleteBucketLifecycle&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes the lifecycle configuration from the specified Outposts bucket. Amazon S3 on Outposts removes all the lifecycle configuration rules in the lifecycle subresource associated with the bucket. Your objects never expire, and Amazon S3 on Outposts no longer automatically deletes any objects on the basis of rules contained in the deleted lifecycle configuration. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3-outposts:DeleteLifecycleConfiguration&lt;/code&gt; action. By default, the bucket owner has this permission and the Outposts bucket owner can grant this permission to others.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketLifecycleConfiguration.html#API_control_DeleteBucketLifecycleConfiguration_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;For more information about object expiration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#intro-lifecycle-rules-actions\&quot;&gt;Elements to Describe Lifecycle Actions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html\&quot;&gt;PutBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html\&quot;&gt;GetBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the lifecycle configuration to delete.
let name = "name_example"; // String | <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBucketLifecycleConfiguration(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID of the lifecycle configuration to delete. | 
 **name** | **String**| &lt;p&gt;Specifies the bucket.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
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
- **Accept**: Not defined


## deleteBucketPolicy

> deleteBucketPolicy(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This action deletes an Amazon S3 on Outposts bucket policy. To delete an S3 bucket policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html\&quot;&gt;DeleteBucketPolicy&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;This implementation of the DELETE action uses the policy subresource to delete the policy of a specified Amazon S3 on Outposts bucket. If you are using an identity other than the root user of the Amazon Web Services account that owns the bucket, the calling identity must have the &lt;code&gt;s3-outposts:DeleteBucketPolicy&lt;/code&gt; permissions on the specified Outposts bucket and belong to the bucket owner&#39;s account to use this action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t have &lt;code&gt;DeleteBucketPolicy&lt;/code&gt; permissions, Amazon S3 returns a &lt;code&gt;403 Access Denied&lt;/code&gt; error. If you have the correct permissions, but you&#39;re not using an identity that belongs to the bucket owner&#39;s account, Amazon S3 returns a &lt;code&gt;405 Method Not Allowed&lt;/code&gt; error. &lt;/p&gt; &lt;important&gt; &lt;p&gt;As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this action, even if the policy explicitly denies the root user the ability to perform this action.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about bucket policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html\&quot;&gt;Using Bucket Policies and User Policies&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html#API_control_DeleteBucketPolicy_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;DeleteBucketPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html\&quot;&gt;GetBucketPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html\&quot;&gt;PutBucketPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the Outposts bucket.
let name = "name_example"; // String | <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBucketPolicy(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;Specifies the bucket.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
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
- **Accept**: Not defined


## deleteBucketReplication

> deleteBucketReplication(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This operation deletes an Amazon S3 on Outposts bucket&#39;s replication configuration. To delete an S3 bucket&#39;s replication configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketReplication.html\&quot;&gt;DeleteBucketReplication&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes the replication configuration from the specified S3 on Outposts bucket.&lt;/p&gt; &lt;p&gt;To use this operation, you must have permissions to perform the &lt;code&gt;s3-outposts:PutReplicationConfiguration&lt;/code&gt; action. The Outposts bucket owner has this permission by default and can grant it to others. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsIAM.html\&quot;&gt;Setting up IAM with S3 on Outposts&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsBucketPolicy.html\&quot;&gt;Managing access to S3 on Outposts buckets&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It can take a while to propagate &lt;code&gt;PUT&lt;/code&gt; or &lt;code&gt;DELETE&lt;/code&gt; requests for a replication configuration to all S3 on Outposts systems. Therefore, the replication configuration that&#39;s returned by a &lt;code&gt;GET&lt;/code&gt; request soon after a &lt;code&gt;PUT&lt;/code&gt; or &lt;code&gt;DELETE&lt;/code&gt; request might return a more recent result than what&#39;s on the Outpost. If an Outpost is offline, the delay in updating the replication configuration on that Outpost can be significant.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketReplication.html#API_control_DeleteBucketReplication_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;For information about S3 replication on Outposts configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html\&quot;&gt;Replicating objects for S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;DeleteBucketReplication&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html\&quot;&gt;PutBucketReplication&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html\&quot;&gt;GetBucketReplication&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket to delete the replication configuration for.
let name = "name_example"; // String | <p>Specifies the S3 on Outposts bucket to delete the replication configuration for.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBucketReplication(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket to delete the replication configuration for. | 
 **name** | **String**| &lt;p&gt;Specifies the S3 on Outposts bucket to delete the replication configuration for.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
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
- **Accept**: Not defined


## deleteBucketTagging

> deleteBucketTagging(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This action deletes an Amazon S3 on Outposts bucket&#39;s tags. To delete an S3 bucket tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html\&quot;&gt;DeleteBucketTagging&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes the tags from the Outposts bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;PutBucketTagging&lt;/code&gt; action. By default, the bucket owner has this permission and can grant this permission to others. &lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketTagging.html#API_control_DeleteBucketTagging_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;DeleteBucketTagging&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html\&quot;&gt;GetBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketTagging.html\&quot;&gt;PutBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket tag set to be removed.
let name = "name_example"; // String | <p>The bucket ARN that has the tag set to be removed.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBucketTagging(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket tag set to be removed. | 
 **name** | **String**| &lt;p&gt;The bucket ARN that has the tag set to be removed.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
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
- **Accept**: Not defined


## deleteJobTagging

> Object deleteJobTagging(xAmzAccountId, id, opts)



&lt;p&gt;Removes the entire tag set from the specified S3 Batch Operations job. To use the &lt;code&gt;DeleteJobTagging&lt;/code&gt; operation, you must have permission to perform the &lt;code&gt;s3:DeleteJobTagging&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags\&quot;&gt;Controlling access and labeling jobs using tags&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html\&quot;&gt;CreateJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html\&quot;&gt;GetJobTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html\&quot;&gt;PutJobTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID associated with the S3 Batch Operations job.
let id = "id_example"; // String | The ID for the S3 Batch Operations job whose tags you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteJobTagging(xAmzAccountId, id, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID associated with the S3 Batch Operations job. | 
 **id** | **String**| The ID for the S3 Batch Operations job whose tags you want to delete. | 
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
- **Accept**: text/xml


## deleteMultiRegionAccessPoint

> DeleteMultiRegionAccessPointResult deleteMultiRegionAccessPoint(xAmzAccountId, deleteMultiRegionAccessPointRequest, opts)



&lt;p&gt;Deletes a Multi-Region Access Point. This action does not delete the buckets associated with the Multi-Region Access Point, only the Multi-Region Access Point itself.&lt;/p&gt; &lt;p&gt;This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around managing Multi-Region Access Points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This request is asynchronous, meaning that you might receive a response before the command has completed. When this request provides a response, it provides a token that you can use to monitor the status of the request with &lt;code&gt;DescribeMultiRegionAccessPointOperation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;DeleteMultiRegionAccessPoint&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html\&quot;&gt;CreateMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html\&quot;&gt;DescribeMultiRegionAccessPointOperation&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html\&quot;&gt;GetMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html\&quot;&gt;ListMultiRegionAccessPoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let deleteMultiRegionAccessPointRequest = new AwsS3Control.DeleteMultiRegionAccessPointRequest(); // DeleteMultiRegionAccessPointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMultiRegionAccessPoint(xAmzAccountId, deleteMultiRegionAccessPointRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **deleteMultiRegionAccessPointRequest** | [**DeleteMultiRegionAccessPointRequest**](DeleteMultiRegionAccessPointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteMultiRegionAccessPointResult**](DeleteMultiRegionAccessPointResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## deletePublicAccessBlock

> deletePublicAccessBlock(xAmzAccountId, opts)



&lt;p&gt;Removes the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for an Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html\&quot;&gt; Using Amazon S3 block public access&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html\&quot;&gt;GetPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html\&quot;&gt;PutPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to remove.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePublicAccessBlock(xAmzAccountId, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the Amazon Web Services account whose &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration you want to remove. | 
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
- **Accept**: Not defined


## deleteStorageLensConfiguration

> deleteStorageLensConfiguration(storagelensid, xAmzAccountId, opts)



&lt;p&gt;Deletes the Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html\&quot;&gt;Assessing your storage activity and usage with Amazon S3 Storage Lens &lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3:DeleteStorageLensConfiguration&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html\&quot;&gt;Setting permissions to use Amazon S3 Storage Lens&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let storagelensid = "storagelensid_example"; // String | The ID of the S3 Storage Lens configuration.
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the requester.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStorageLensConfiguration(storagelensid, xAmzAccountId, opts, (error, data, response) => {
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
 **storagelensid** | **String**| The ID of the S3 Storage Lens configuration. | 
 **xAmzAccountId** | **String**| The account ID of the requester. | 
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
- **Accept**: Not defined


## deleteStorageLensConfigurationTagging

> Object deleteStorageLensConfigurationTagging(storagelensid, xAmzAccountId, opts)



&lt;p&gt;Deletes the Amazon S3 Storage Lens configuration tags. For more information about S3 Storage Lens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html\&quot;&gt;Assessing your storage activity and usage with Amazon S3 Storage Lens &lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3:DeleteStorageLensConfigurationTagging&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html\&quot;&gt;Setting permissions to use Amazon S3 Storage Lens&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let storagelensid = "storagelensid_example"; // String | The ID of the S3 Storage Lens configuration.
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the requester.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStorageLensConfigurationTagging(storagelensid, xAmzAccountId, opts, (error, data, response) => {
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
 **storagelensid** | **String**| The ID of the S3 Storage Lens configuration. | 
 **xAmzAccountId** | **String**| The account ID of the requester. | 
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
- **Accept**: text/xml


## describeJob

> DescribeJobResult describeJob(xAmzAccountId, id, opts)



&lt;p&gt;Retrieves the configuration parameters and status for a Batch Operations job. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html\&quot;&gt;S3 Batch Operations&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html\&quot;&gt;CreateJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html\&quot;&gt;ListJobs&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html\&quot;&gt;UpdateJobPriority&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html\&quot;&gt;UpdateJobStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID associated with the S3 Batch Operations job.
let id = "id_example"; // String | The ID for the job whose information you want to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeJob(xAmzAccountId, id, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID associated with the S3 Batch Operations job. | 
 **id** | **String**| The ID for the job whose information you want to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeJobResult**](DescribeJobResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## describeMultiRegionAccessPointOperation

> DescribeMultiRegionAccessPointOperationResult describeMultiRegionAccessPointOperation(xAmzAccountId, requestToken, opts)



&lt;p&gt;Retrieves the status of an asynchronous request to manage a Multi-Region Access Point. For more information about managing Multi-Region Access Points and how asynchronous requests work, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetMultiRegionAccessPoint&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html\&quot;&gt;CreateMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html\&quot;&gt;DeleteMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html\&quot;&gt;GetMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html\&quot;&gt;ListMultiRegionAccessPoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let requestToken = "requestToken_example"; // String | The request token associated with the request you want to know about. This request token is returned as part of the response when you make an asynchronous request. You provide this token to query about the status of the asynchronous action.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeMultiRegionAccessPointOperation(xAmzAccountId, requestToken, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **requestToken** | **String**| The request token associated with the request you want to know about. This request token is returned as part of the response when you make an asynchronous request. You provide this token to query about the status of the asynchronous action. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeMultiRegionAccessPointOperationResult**](DescribeMultiRegionAccessPointOperationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getAccessPoint

> GetAccessPointResult getAccessPoint(xAmzAccountId, name, opts)



&lt;p&gt;Returns configuration information about the specified access point.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html#API_control_GetAccessPoint_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetAccessPoint&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html\&quot;&gt;CreateAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html\&quot;&gt;DeleteAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html\&quot;&gt;ListAccessPoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the account that owns the specified access point.
let name = "name_example"; // String | <p>The name of the access point whose configuration information you want to retrieve.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/accesspoint/&lt;my-accesspoint-name&gt;</code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessPoint(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the account that owns the specified access point. | 
 **name** | **String**| &lt;p&gt;The name of the access point whose configuration information you want to retrieve.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/accesspoint/&amp;lt;my-accesspoint-name&amp;gt;&lt;/code&gt;. For example, to access the access point &lt;code&gt;reports-ap&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessPointResult**](GetAccessPointResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getAccessPointConfigurationForObjectLambda

> GetAccessPointConfigurationForObjectLambdaResult getAccessPointConfigurationForObjectLambda(xAmzAccountId, name, opts)



&lt;p&gt;Returns configuration for an Object Lambda Access Point.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetAccessPointConfigurationForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointConfigurationForObjectLambda.html\&quot;&gt;PutAccessPointConfigurationForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let name = "name_example"; // String | The name of the Object Lambda Access Point you want to return the configuration for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessPointConfigurationForObjectLambda(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **name** | **String**| The name of the Object Lambda Access Point you want to return the configuration for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessPointConfigurationForObjectLambdaResult**](GetAccessPointConfigurationForObjectLambdaResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getAccessPointForObjectLambda

> GetAccessPointForObjectLambdaResult getAccessPointForObjectLambda(xAmzAccountId, name, opts)



&lt;p&gt;Returns configuration information about the specified Object Lambda Access Point&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetAccessPointForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html\&quot;&gt;CreateAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html\&quot;&gt;DeleteAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html\&quot;&gt;ListAccessPointsForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let name = "name_example"; // String | The name of the Object Lambda Access Point.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessPointForObjectLambda(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **name** | **String**| The name of the Object Lambda Access Point. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessPointForObjectLambdaResult**](GetAccessPointForObjectLambdaResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getAccessPointPolicy

> GetAccessPointPolicyResult getAccessPointPolicy(xAmzAccountId, name, opts)



&lt;p&gt;Returns the access point policy associated with the specified access point.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetAccessPointPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html\&quot;&gt;PutAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html\&quot;&gt;DeleteAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified access point.
let name = "name_example"; // String | <p>The name of the access point whose policy you want to retrieve.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/accesspoint/&lt;my-accesspoint-name&gt;</code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessPointPolicy(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified access point. | 
 **name** | **String**| &lt;p&gt;The name of the access point whose policy you want to retrieve.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/accesspoint/&amp;lt;my-accesspoint-name&amp;gt;&lt;/code&gt;. For example, to access the access point &lt;code&gt;reports-ap&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessPointPolicyResult**](GetAccessPointPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getAccessPointPolicyForObjectLambda

> GetAccessPointPolicyForObjectLambdaResult getAccessPointPolicyForObjectLambda(xAmzAccountId, name, opts)



&lt;p&gt;Returns the resource policy for an Object Lambda Access Point.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetAccessPointPolicyForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html\&quot;&gt;DeleteAccessPointPolicyForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html\&quot;&gt;PutAccessPointPolicyForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let name = "name_example"; // String | The name of the Object Lambda Access Point.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessPointPolicyForObjectLambda(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **name** | **String**| The name of the Object Lambda Access Point. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessPointPolicyForObjectLambdaResult**](GetAccessPointPolicyForObjectLambdaResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getAccessPointPolicyStatus

> GetAccessPointPolicyStatusResult getAccessPointPolicyStatus(xAmzAccountId, name, opts)



Indicates whether the specified access point currently has a policy that allows public access. For more information about public access through access points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html\&quot;&gt;Managing Data Access with Amazon S3 access points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified access point.
let name = "name_example"; // String | The name of the access point whose policy status you want to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessPointPolicyStatus(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified access point. | 
 **name** | **String**| The name of the access point whose policy status you want to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessPointPolicyStatusResult**](GetAccessPointPolicyStatusResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getAccessPointPolicyStatusForObjectLambda

> GetAccessPointPolicyStatusForObjectLambdaResult getAccessPointPolicyStatusForObjectLambda(xAmzAccountId, name, opts)



Returns the status of the resource policy associated with an Object Lambda Access Point.

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let name = "name_example"; // String | The name of the Object Lambda Access Point.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessPointPolicyStatusForObjectLambda(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **name** | **String**| The name of the Object Lambda Access Point. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessPointPolicyStatusForObjectLambdaResult**](GetAccessPointPolicyStatusForObjectLambdaResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getBucket

> GetBucketResult getBucket(xAmzAccountId, name, opts)



&lt;p&gt;Gets an Amazon S3 on Outposts bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt; Using Amazon S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you are using an identity other than the root user of the Amazon Web Services account that owns the Outposts bucket, the calling identity must have the &lt;code&gt;s3-outposts:GetBucket&lt;/code&gt; permissions on the specified Outposts bucket and belong to the Outposts bucket owner&#39;s account in order to use this action. Only users from Outposts bucket owner account with the right permissions can perform actions on an Outposts bucket. &lt;/p&gt; &lt;p&gt; If you don&#39;t have &lt;code&gt;s3-outposts:GetBucket&lt;/code&gt; permissions or you&#39;re not using an identity that belongs to the bucket owner&#39;s account, Amazon S3 returns a &lt;code&gt;403 Access Denied&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetBucket&lt;/code&gt; for Amazon S3 on Outposts:&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html#API_control_GetBucket_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html\&quot;&gt;PutObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html\&quot;&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html\&quot;&gt;DeleteBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBucket(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;Specifies the bucket.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBucketResult**](GetBucketResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getBucketLifecycleConfiguration

> GetBucketLifecycleConfigurationResult getBucketLifecycleConfiguration(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This action gets an Amazon S3 on Outposts bucket&#39;s lifecycle configuration. To get an S3 bucket&#39;s lifecycle configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html\&quot;&gt;GetBucketLifecycleConfiguration&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the lifecycle configuration information set on the Outposts bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; and for information about lifecycle configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html\&quot;&gt; Object Lifecycle Management&lt;/a&gt; in &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3-outposts:GetLifecycleConfiguration&lt;/code&gt; action. The Outposts bucket owner has this permission, by default. The bucket owner can grant this permission to others. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources\&quot;&gt;Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html\&quot;&gt;Managing Access Permissions to Your Amazon S3 Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html#API_control_GetBucketLifecycleConfiguration_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetBucketLifecycleConfiguration&lt;/code&gt; has the following special error:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;NoSuchLifecycleConfiguration&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: The lifecycle configuration does not exist.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;HTTP Status Code: 404 Not Found&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;SOAP Fault Code Prefix: Client&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetBucketLifecycleConfiguration&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html\&quot;&gt;PutBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketLifecycleConfiguration.html\&quot;&gt;DeleteBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | <p>The Amazon Resource Name (ARN) of the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBucketLifecycleConfiguration(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;The Amazon Resource Name (ARN) of the bucket.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBucketLifecycleConfigurationResult**](GetBucketLifecycleConfigurationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getBucketPolicy

> GetBucketPolicyResult getBucketPolicy(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This action gets a bucket policy for an Amazon S3 on Outposts bucket. To get a policy for an S3 bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html\&quot;&gt;GetBucketPolicy&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the policy of a specified Outposts bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you are using an identity other than the root user of the Amazon Web Services account that owns the bucket, the calling identity must have the &lt;code&gt;GetBucketPolicy&lt;/code&gt; permissions on the specified bucket and belong to the bucket owner&#39;s account in order to use this action.&lt;/p&gt; &lt;p&gt;Only users from Outposts bucket owner account with the right permissions can perform actions on an Outposts bucket. If you don&#39;t have &lt;code&gt;s3-outposts:GetBucketPolicy&lt;/code&gt; permissions or you&#39;re not using an identity that belongs to the bucket owner&#39;s account, Amazon S3 returns a &lt;code&gt;403 Access Denied&lt;/code&gt; error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this action, even if the policy explicitly denies the root user the ability to perform this action.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about bucket policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html\&quot;&gt;Using Bucket Policies and User Policies&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html#API_control_GetBucketPolicy_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetBucketPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html\&quot;&gt;GetObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html\&quot;&gt;PutBucketPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html\&quot;&gt;DeleteBucketPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBucketPolicy(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;Specifies the bucket.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBucketPolicyResult**](GetBucketPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getBucketReplication

> GetBucketReplicationResult getBucketReplication(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This operation gets an Amazon S3 on Outposts bucket&#39;s replication configuration. To get an S3 bucket&#39;s replication configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html\&quot;&gt;GetBucketReplication&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the replication configuration of an S3 on Outposts bucket. For more information about S3 on Outposts, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. For information about S3 replication on Outposts configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html\&quot;&gt;Replicating objects for S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It can take a while to propagate &lt;code&gt;PUT&lt;/code&gt; or &lt;code&gt;DELETE&lt;/code&gt; requests for a replication configuration to all S3 on Outposts systems. Therefore, the replication configuration that&#39;s returned by a &lt;code&gt;GET&lt;/code&gt; request soon after a &lt;code&gt;PUT&lt;/code&gt; or &lt;code&gt;DELETE&lt;/code&gt; request might return a more recent result than what&#39;s on the Outpost. If an Outpost is offline, the delay in updating the replication configuration on that Outpost can be significant.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This action requires permissions for the &lt;code&gt;s3-outposts:GetReplicationConfiguration&lt;/code&gt; action. The Outposts bucket owner has this permission by default and can grant it to others. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsIAM.html\&quot;&gt;Setting up IAM with S3 on Outposts&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsBucketPolicy.html\&quot;&gt;Managing access to S3 on Outposts bucket&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html#API_control_GetBucketReplication_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;If you include the &lt;code&gt;Filter&lt;/code&gt; element in a replication configuration, you must also include the &lt;code&gt;DeleteMarkerReplication&lt;/code&gt;, &lt;code&gt;Status&lt;/code&gt;, and &lt;code&gt;Priority&lt;/code&gt; elements. The response also returns those elements.&lt;/p&gt; &lt;p&gt;For information about S3 on Outposts replication failure reasons, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-replication-eventbridge.html#outposts-replication-failure-codes\&quot;&gt;Replication failure reasons&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketReplication&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html\&quot;&gt;PutBucketReplication&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketReplication.html\&quot;&gt;DeleteBucketReplication&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | <p>Specifies the bucket to get the replication information for.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBucketReplication(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;Specifies the bucket to get the replication information for.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBucketReplicationResult**](GetBucketReplicationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getBucketTagging

> GetBucketTaggingResult getBucketTagging(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This action gets an Amazon S3 on Outposts bucket&#39;s tags. To get an S3 bucket tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html\&quot;&gt;GetBucketTagging&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the tag set associated with the Outposts bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;GetBucketTagging&lt;/code&gt; action. By default, the bucket owner has this permission and can grant this permission to others.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetBucketTagging&lt;/code&gt; has the following special error:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;NoSuchTagSetError&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: There is no tag set associated with the bucket.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html#API_control_GetBucketTagging_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetBucketTagging&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketTagging.html\&quot;&gt;PutBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketTagging.html\&quot;&gt;DeleteBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBucketTagging(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;Specifies the bucket.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBucketTaggingResult**](GetBucketTaggingResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getBucketVersioning

> GetBucketVersioningResult getBucketVersioning(xAmzAccountId, name, opts)



&lt;note&gt; &lt;p&gt;This operation returns the versioning state for S3 on Outposts buckets only. To return the versioning state for an S3 bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html\&quot;&gt;GetBucketVersioning&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the versioning state for an S3 on Outposts bucket. With S3 Versioning, you can save multiple distinct copies of your objects and recover from unintended user actions and application failures.&lt;/p&gt; &lt;p&gt;If you&#39;ve never set versioning on your bucket, it has no versioning state. In that case, the &lt;code&gt;GetBucketVersioning&lt;/code&gt; request does not return a versioning state value.&lt;/p&gt; &lt;p&gt;For more information about versioning, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html\&quot;&gt;Versioning&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html#API_control_GetBucketVersioning_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketVersioning&lt;/code&gt; for S3 on Outposts.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketVersioning.html\&quot;&gt;PutBucketVersioning&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html\&quot;&gt;PutBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html\&quot;&gt;GetBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the S3 on Outposts bucket.
let name = "name_example"; // String | The S3 on Outposts bucket to return the versioning state for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBucketVersioning(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the S3 on Outposts bucket. | 
 **name** | **String**| The S3 on Outposts bucket to return the versioning state for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBucketVersioningResult**](GetBucketVersioningResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getJobTagging

> GetJobTaggingResult getJobTagging(xAmzAccountId, id, opts)



&lt;p&gt;Returns the tags on an S3 Batch Operations job. To use the &lt;code&gt;GetJobTagging&lt;/code&gt; operation, you must have permission to perform the &lt;code&gt;s3:GetJobTagging&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags\&quot;&gt;Controlling access and labeling jobs using tags&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html\&quot;&gt;CreateJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html\&quot;&gt;PutJobTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html\&quot;&gt;DeleteJobTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID associated with the S3 Batch Operations job.
let id = "id_example"; // String | The ID for the S3 Batch Operations job whose tags you want to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getJobTagging(xAmzAccountId, id, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID associated with the S3 Batch Operations job. | 
 **id** | **String**| The ID for the S3 Batch Operations job whose tags you want to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetJobTaggingResult**](GetJobTaggingResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getMultiRegionAccessPoint

> GetMultiRegionAccessPointResult getMultiRegionAccessPoint(xAmzAccountId, name, opts)



&lt;p&gt;Returns configuration information about the specified Multi-Region Access Point.&lt;/p&gt; &lt;p&gt;This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around managing Multi-Region Access Points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetMultiRegionAccessPoint&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html\&quot;&gt;CreateMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html\&quot;&gt;DeleteMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html\&quot;&gt;DescribeMultiRegionAccessPointOperation&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html\&quot;&gt;ListMultiRegionAccessPoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let name = "name_example"; // String | The name of the Multi-Region Access Point whose configuration information you want to receive. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming\">Managing Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMultiRegionAccessPoint(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **name** | **String**| The name of the Multi-Region Access Point whose configuration information you want to receive. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMultiRegionAccessPointResult**](GetMultiRegionAccessPointResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getMultiRegionAccessPointPolicy

> GetMultiRegionAccessPointPolicyResult getMultiRegionAccessPointPolicy(xAmzAccountId, name, opts)



&lt;p&gt;Returns the access control policy of the specified Multi-Region Access Point.&lt;/p&gt; &lt;p&gt;This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around managing Multi-Region Access Points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetMultiRegionAccessPointPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html\&quot;&gt;GetMultiRegionAccessPointPolicyStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html\&quot;&gt;PutMultiRegionAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let name = "name_example"; // String | Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming\">Managing Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMultiRegionAccessPointPolicy(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **name** | **String**| Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMultiRegionAccessPointPolicyResult**](GetMultiRegionAccessPointPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getMultiRegionAccessPointPolicyStatus

> GetMultiRegionAccessPointPolicyStatusResult getMultiRegionAccessPointPolicyStatus(xAmzAccountId, name, opts)



&lt;p&gt;Indicates whether the specified Multi-Region Access Point has an access control policy that allows public access.&lt;/p&gt; &lt;p&gt;This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around managing Multi-Region Access Points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;GetMultiRegionAccessPointPolicyStatus&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html\&quot;&gt;GetMultiRegionAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html\&quot;&gt;PutMultiRegionAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let name = "name_example"; // String | Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming\">Managing Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMultiRegionAccessPointPolicyStatus(xAmzAccountId, name, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **name** | **String**| Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMultiRegionAccessPointPolicyStatusResult**](GetMultiRegionAccessPointPolicyStatusResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getMultiRegionAccessPointRoutes

> GetMultiRegionAccessPointRoutesResult getMultiRegionAccessPointRoutes(xAmzAccountId, mrap, opts)



&lt;p&gt;Returns the routing configuration for a Multi-Region Access Point, indicating which Regions are active or passive.&lt;/p&gt; &lt;p&gt;To obtain routing control changes and failover requests, use the Amazon S3 failover control infrastructure endpoints in these five Amazon Web Services Regions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;us-east-1&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;us-west-2&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ap-southeast-2&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ap-northeast-1&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;eu-west-1&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;Your Amazon S3 bucket does not need to be in these five Regions.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let mrap = "mrap_example"; // String | The Multi-Region Access Point ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMultiRegionAccessPointRoutes(xAmzAccountId, mrap, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **mrap** | **String**| The Multi-Region Access Point ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMultiRegionAccessPointRoutesResult**](GetMultiRegionAccessPointRoutesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getPublicAccessBlock

> GetPublicAccessBlockOutput getPublicAccessBlock(xAmzAccountId, opts)



&lt;p&gt;Retrieves the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for an Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html\&quot;&gt; Using Amazon S3 block public access&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeletePublicAccessBlock.html\&quot;&gt;DeletePublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html\&quot;&gt;PutPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPublicAccessBlock(xAmzAccountId, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the Amazon Web Services account whose &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration you want to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPublicAccessBlockOutput**](GetPublicAccessBlockOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getStorageLensConfiguration

> GetStorageLensConfigurationResult getStorageLensConfiguration(storagelensid, xAmzAccountId, opts)



&lt;p&gt;Gets the Amazon S3 Storage Lens configuration. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html\&quot;&gt;Assessing your storage activity and usage with Amazon S3 Storage Lens &lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. For a complete list of S3 Storage Lens metrics, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html\&quot;&gt;S3 Storage Lens metrics glossary&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3:GetStorageLensConfiguration&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html\&quot;&gt;Setting permissions to use Amazon S3 Storage Lens&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let storagelensid = "storagelensid_example"; // String | The ID of the Amazon S3 Storage Lens configuration.
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the requester.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStorageLensConfiguration(storagelensid, xAmzAccountId, opts, (error, data, response) => {
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
 **storagelensid** | **String**| The ID of the Amazon S3 Storage Lens configuration. | 
 **xAmzAccountId** | **String**| The account ID of the requester. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStorageLensConfigurationResult**](GetStorageLensConfigurationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getStorageLensConfigurationTagging

> GetStorageLensConfigurationTaggingResult getStorageLensConfigurationTagging(storagelensid, xAmzAccountId, opts)



&lt;p&gt;Gets the tags of Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html\&quot;&gt;Assessing your storage activity and usage with Amazon S3 Storage Lens &lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3:GetStorageLensConfigurationTagging&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html\&quot;&gt;Setting permissions to use Amazon S3 Storage Lens&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let storagelensid = "storagelensid_example"; // String | The ID of the Amazon S3 Storage Lens configuration.
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the requester.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStorageLensConfigurationTagging(storagelensid, xAmzAccountId, opts, (error, data, response) => {
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
 **storagelensid** | **String**| The ID of the Amazon S3 Storage Lens configuration. | 
 **xAmzAccountId** | **String**| The account ID of the requester. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStorageLensConfigurationTaggingResult**](GetStorageLensConfigurationTaggingResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listAccessPoints

> ListAccessPointsResult listAccessPoints(xAmzAccountId, opts)



&lt;p&gt;Returns a list of the access points that are owned by the current account that&#39;s associated with the specified bucket. You can retrieve up to 1000 access points per call. If the specified bucket has more than 1,000 access points (or the number specified in &lt;code&gt;maxResults&lt;/code&gt;, whichever is less), the response will include a continuation token that you can use to list the additional access points.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html#API_control_GetAccessPoint_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;ListAccessPoints&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html\&quot;&gt;CreateAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html\&quot;&gt;DeleteAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html\&quot;&gt;GetAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the account that owns the specified access points.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'bucket': "bucket_example", // String | <p>The name of the bucket whose associated access points you want to list.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
  'nextToken': "nextToken_example", // String | A continuation token. If a previous call to <code>ListAccessPoints</code> returned a continuation token in the <code>NextToken</code> field, then providing that value here causes Amazon S3 to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of access points that you want to include in the list. If the specified bucket has more than this number of access points, then the response will include a continuation token in the <code>NextToken</code> field that you can use to retrieve the next page of access points.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAccessPoints(xAmzAccountId, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the account that owns the specified access points. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **bucket** | **String**| &lt;p&gt;The name of the bucket whose associated access points you want to list.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| A continuation token. If a previous call to &lt;code&gt;ListAccessPoints&lt;/code&gt; returned a continuation token in the &lt;code&gt;NextToken&lt;/code&gt; field, then providing that value here causes Amazon S3 to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of access points that you want to include in the list. If the specified bucket has more than this number of access points, then the response will include a continuation token in the &lt;code&gt;NextToken&lt;/code&gt; field that you can use to retrieve the next page of access points. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAccessPointsResult**](ListAccessPointsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listAccessPointsForObjectLambda

> ListAccessPointsForObjectLambdaResult listAccessPointsForObjectLambda(xAmzAccountId, opts)



&lt;p&gt;Returns some or all (up to 1,000) access points associated with the Object Lambda Access Point per call. If there are more access points than what can be returned in one call, the response will include a continuation token that you can use to list the additional access points.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;ListAccessPointsForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html\&quot;&gt;CreateAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html\&quot;&gt;DeleteAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html\&quot;&gt;GetAccessPointForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | If the list has more access points than can be returned in one call to this API, this field contains a continuation token that you can provide in subsequent calls to this API to retrieve additional access points.
  'maxResults': 56, // Number | The maximum number of access points that you want to include in the list. The response may contain fewer access points but will never contain more. If there are more than this number of access points, then the response will include a continuation token in the <code>NextToken</code> field that you can use to retrieve the next page of access points.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAccessPointsForObjectLambda(xAmzAccountId, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| If the list has more access points than can be returned in one call to this API, this field contains a continuation token that you can provide in subsequent calls to this API to retrieve additional access points. | [optional] 
 **maxResults** | **Number**| The maximum number of access points that you want to include in the list. The response may contain fewer access points but will never contain more. If there are more than this number of access points, then the response will include a continuation token in the &lt;code&gt;NextToken&lt;/code&gt; field that you can use to retrieve the next page of access points. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAccessPointsForObjectLambdaResult**](ListAccessPointsForObjectLambdaResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listJobs

> ListJobsResult listJobs(xAmzAccountId, opts)



&lt;p&gt;Lists current S3 Batch Operations jobs and jobs that have ended within the last 30 days for the Amazon Web Services account making the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html\&quot;&gt;S3 Batch Operations&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;p/&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html\&quot;&gt;CreateJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html\&quot;&gt;DescribeJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html\&quot;&gt;UpdateJobPriority&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html\&quot;&gt;UpdateJobStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID associated with the S3 Batch Operations job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'jobStatuses': [new AwsS3Control.JobStatus()], // [JobStatus] | The <code>List Jobs</code> request returns jobs that match the statuses listed in this element.
  'nextToken': "nextToken_example", // String | A pagination token to request the next page of results. Use the token that Amazon S3 returned in the <code>NextToken</code> element of the <code>ListJobsResult</code> from the previous <code>List Jobs</code> request.
  'maxResults': 56, // Number | The maximum number of jobs that Amazon S3 will include in the <code>List Jobs</code> response. If there are more jobs than this number, the response will include a pagination token in the <code>NextToken</code> field to enable you to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listJobs(xAmzAccountId, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID associated with the S3 Batch Operations job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **jobStatuses** | [**[JobStatus]**](JobStatus.md)| The &lt;code&gt;List Jobs&lt;/code&gt; request returns jobs that match the statuses listed in this element. | [optional] 
 **nextToken** | **String**| A pagination token to request the next page of results. Use the token that Amazon S3 returned in the &lt;code&gt;NextToken&lt;/code&gt; element of the &lt;code&gt;ListJobsResult&lt;/code&gt; from the previous &lt;code&gt;List Jobs&lt;/code&gt; request. | [optional] 
 **maxResults** | **Number**| The maximum number of jobs that Amazon S3 will include in the &lt;code&gt;List Jobs&lt;/code&gt; response. If there are more jobs than this number, the response will include a pagination token in the &lt;code&gt;NextToken&lt;/code&gt; field to enable you to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListJobsResult**](ListJobsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listMultiRegionAccessPoints

> ListMultiRegionAccessPointsResult listMultiRegionAccessPoints(xAmzAccountId, opts)



&lt;p&gt;Returns a list of the Multi-Region Access Points currently associated with the specified Amazon Web Services account. Each call can return up to 100 Multi-Region Access Points, the maximum number of Multi-Region Access Points that can be associated with a single account.&lt;/p&gt; &lt;p&gt;This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around managing Multi-Region Access Points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;ListMultiRegionAccessPoint&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html\&quot;&gt;CreateMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html\&quot;&gt;DeleteMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html\&quot;&gt;DescribeMultiRegionAccessPointOperation&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html\&quot;&gt;GetMultiRegionAccessPoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | Not currently used. Do not use this parameter.
  'maxResults': 56, // Number | Not currently used. Do not use this parameter.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMultiRegionAccessPoints(xAmzAccountId, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Not currently used. Do not use this parameter. | [optional] 
 **maxResults** | **Number**| Not currently used. Do not use this parameter. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMultiRegionAccessPointsResult**](ListMultiRegionAccessPointsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listRegionalBuckets

> ListRegionalBucketsResult listRegionalBuckets(xAmzAccountId, opts)



&lt;p&gt;Returns a list of all Outposts buckets in an Outpost that are owned by the authenticated sender of the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and &lt;code&gt;x-amz-outpost-id&lt;/code&gt; in your request, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListRegionalBuckets.html#API_control_ListRegionalBuckets_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | <p/>
  'maxResults': 56, // Number | <p/>
  'xAmzOutpostId': "xAmzOutpostId_example", // String | <p>The ID of the Outposts resource.</p> <note> <p>This ID is required by Amazon S3 on Outposts buckets.</p> </note>
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRegionalBuckets(xAmzAccountId, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| &lt;p/&gt; | [optional] 
 **maxResults** | **Number**| &lt;p/&gt; | [optional] 
 **xAmzOutpostId** | **String**| &lt;p&gt;The ID of the Outposts resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This ID is required by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRegionalBucketsResult**](ListRegionalBucketsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listStorageLensConfigurations

> ListStorageLensConfigurationsResult listStorageLensConfigurations(xAmzAccountId, opts)



&lt;p&gt;Gets a list of Amazon S3 Storage Lens configurations. For more information about S3 Storage Lens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html\&quot;&gt;Assessing your storage activity and usage with Amazon S3 Storage Lens &lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3:ListStorageLensConfigurations&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html\&quot;&gt;Setting permissions to use Amazon S3 Storage Lens&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the requester.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token to request the next page of results.
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listStorageLensConfigurations(xAmzAccountId, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID of the requester. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A pagination token to request the next page of results. | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListStorageLensConfigurationsResult**](ListStorageLensConfigurationsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## putAccessPointConfigurationForObjectLambda

> putAccessPointConfigurationForObjectLambda(xAmzAccountId, name, createAccessPointForObjectLambdaRequest, opts)



&lt;p&gt;Replaces configuration for an Object Lambda Access Point.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;PutAccessPointConfigurationForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointConfigurationForObjectLambda.html\&quot;&gt;GetAccessPointConfigurationForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let name = "name_example"; // String | The name of the Object Lambda Access Point.
let createAccessPointForObjectLambdaRequest = new AwsS3Control.CreateAccessPointForObjectLambdaRequest(); // CreateAccessPointForObjectLambdaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccessPointConfigurationForObjectLambda(xAmzAccountId, name, createAccessPointForObjectLambdaRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **name** | **String**| The name of the Object Lambda Access Point. | 
 **createAccessPointForObjectLambdaRequest** | [**CreateAccessPointForObjectLambdaRequest**](CreateAccessPointForObjectLambdaRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: Not defined


## putAccessPointPolicy

> putAccessPointPolicy(xAmzAccountId, name, putAccessPointPolicyRequest, opts)



&lt;p&gt;Associates an access policy with the specified access point. Each access point can have only one policy, so a request made to this API replaces any existing policy associated with the specified access point.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html#API_control_PutAccessPointPolicy_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;PutAccessPointPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html\&quot;&gt;GetAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html\&quot;&gt;DeleteAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for owner of the bucket associated with the specified access point.
let name = "name_example"; // String | <p>The name of the access point that you want to associate with the specified policy.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/accesspoint/&lt;my-accesspoint-name&gt;</code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>
let putAccessPointPolicyRequest = new AwsS3Control.PutAccessPointPolicyRequest(); // PutAccessPointPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccessPointPolicy(xAmzAccountId, name, putAccessPointPolicyRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for owner of the bucket associated with the specified access point. | 
 **name** | **String**| &lt;p&gt;The name of the access point that you want to associate with the specified policy.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/accesspoint/&amp;lt;my-accesspoint-name&amp;gt;&lt;/code&gt;. For example, to access the access point &lt;code&gt;reports-ap&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **putAccessPointPolicyRequest** | [**PutAccessPointPolicyRequest**](PutAccessPointPolicyRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: Not defined


## putAccessPointPolicyForObjectLambda

> putAccessPointPolicyForObjectLambda(xAmzAccountId, name, putAccessPointPolicyForObjectLambdaRequest, opts)



&lt;p&gt;Creates or replaces resource policy for an Object Lambda Access Point. For an example policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-create.html#olap-create-cli\&quot;&gt;Creating Object Lambda Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;PutAccessPointPolicyForObjectLambda&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html\&quot;&gt;DeleteAccessPointPolicyForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html\&quot;&gt;GetAccessPointPolicyForObjectLambda&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the account that owns the specified Object Lambda Access Point.
let name = "name_example"; // String | The name of the Object Lambda Access Point.
let putAccessPointPolicyForObjectLambdaRequest = new AwsS3Control.PutAccessPointPolicyForObjectLambdaRequest(); // PutAccessPointPolicyForObjectLambdaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccessPointPolicyForObjectLambda(xAmzAccountId, name, putAccessPointPolicyForObjectLambdaRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the account that owns the specified Object Lambda Access Point. | 
 **name** | **String**| The name of the Object Lambda Access Point. | 
 **putAccessPointPolicyForObjectLambdaRequest** | [**PutAccessPointPolicyForObjectLambdaRequest**](PutAccessPointPolicyForObjectLambdaRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: Not defined


## putBucketLifecycleConfiguration

> putBucketLifecycleConfiguration(xAmzAccountId, name, putBucketLifecycleConfigurationRequest, opts)



&lt;note&gt; &lt;p&gt;This action puts a lifecycle configuration to an Amazon S3 on Outposts bucket. To put a lifecycle configuration to an S3 bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html\&quot;&gt;PutBucketLifecycleConfiguration&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a new lifecycle configuration for the S3 on Outposts bucket or replaces an existing lifecycle configuration. Outposts buckets only support lifecycle configurations that delete/expire objects after a certain period of time and abort incomplete multipart uploads.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html#API_control_PutBucketLifecycleConfiguration_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;PutBucketLifecycleConfiguration&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html\&quot;&gt;GetBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketLifecycleConfiguration.html\&quot;&gt;DeleteBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | The name of the bucket for which to set the configuration.
let putBucketLifecycleConfigurationRequest = new AwsS3Control.PutBucketLifecycleConfigurationRequest(); // PutBucketLifecycleConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putBucketLifecycleConfiguration(xAmzAccountId, name, putBucketLifecycleConfigurationRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| The name of the bucket for which to set the configuration. | 
 **putBucketLifecycleConfigurationRequest** | [**PutBucketLifecycleConfigurationRequest**](PutBucketLifecycleConfigurationRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: Not defined


## putBucketPolicy

> putBucketPolicy(xAmzAccountId, name, putBucketPolicyRequest, opts)



&lt;note&gt; &lt;p&gt;This action puts a bucket policy to an Amazon S3 on Outposts bucket. To put a policy on an S3 bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html\&quot;&gt;PutBucketPolicy&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Applies an Amazon S3 bucket policy to an Outposts bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you are using an identity other than the root user of the Amazon Web Services account that owns the Outposts bucket, the calling identity must have the &lt;code&gt;PutBucketPolicy&lt;/code&gt; permissions on the specified Outposts bucket and belong to the bucket owner&#39;s account in order to use this action.&lt;/p&gt; &lt;p&gt;If you don&#39;t have &lt;code&gt;PutBucketPolicy&lt;/code&gt; permissions, Amazon S3 returns a &lt;code&gt;403 Access Denied&lt;/code&gt; error. If you have the correct permissions, but you&#39;re not using an identity that belongs to the bucket owner&#39;s account, Amazon S3 returns a &lt;code&gt;405 Method Not Allowed&lt;/code&gt; error.&lt;/p&gt; &lt;important&gt; &lt;p&gt; As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this action, even if the policy explicitly denies the root user the ability to perform this action. &lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about bucket policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html\&quot;&gt;Using Bucket Policies and User Policies&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html#API_control_PutBucketPolicy_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;PutBucketPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html\&quot;&gt;GetBucketPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html\&quot;&gt;DeleteBucketPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let putBucketPolicyRequest = new AwsS3Control.PutBucketPolicyRequest(); // PutBucketPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConfirmRemoveSelfBucketAccess': true // Boolean | <p>Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
};
apiInstance.putBucketPolicy(xAmzAccountId, name, putBucketPolicyRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;Specifies the bucket.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **putBucketPolicyRequest** | [**PutBucketPolicyRequest**](PutBucketPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConfirmRemoveSelfBucketAccess** | **Boolean**| &lt;p&gt;Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is not supported by Amazon S3 on Outposts buckets.&lt;/p&gt; &lt;/note&gt; | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: Not defined


## putBucketReplication

> putBucketReplication(xAmzAccountId, name, putBucketReplicationRequest, opts)



&lt;note&gt; &lt;p&gt;This action creates an Amazon S3 on Outposts bucket&#39;s replication configuration. To create an S3 bucket&#39;s replication configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html\&quot;&gt;PutBucketReplication&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a replication configuration or replaces an existing one. For information about S3 replication on Outposts configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html\&quot;&gt;Replicating objects for S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It can take a while to propagate &lt;code&gt;PUT&lt;/code&gt; or &lt;code&gt;DELETE&lt;/code&gt; requests for a replication configuration to all S3 on Outposts systems. Therefore, the replication configuration that&#39;s returned by a &lt;code&gt;GET&lt;/code&gt; request soon after a &lt;code&gt;PUT&lt;/code&gt; or &lt;code&gt;DELETE&lt;/code&gt; request might return a more recent result than what&#39;s on the Outpost. If an Outpost is offline, the delay in updating the replication configuration on that Outpost can be significant.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Specify the replication configuration in the request body. In the replication configuration, you provide the following information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The name of the destination bucket or buckets where you want S3 on Outposts to replicate objects&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Identity and Access Management (IAM) role that S3 on Outposts can assume to replicate objects on your behalf&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Other relevant information, such as replication rules&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;A replication configuration must include at least one rule and can contain a maximum of 100. Each rule identifies a subset of objects to replicate by filtering the objects in the source Outposts bucket. To choose additional subsets of objects to replicate, add a rule for each subset.&lt;/p&gt; &lt;p&gt;To specify a subset of the objects in the source Outposts bucket to apply a replication rule to, add the &lt;code&gt;Filter&lt;/code&gt; element as a child of the &lt;code&gt;Rule&lt;/code&gt; element. You can filter objects based on an object key prefix, one or more object tags, or both. When you add the &lt;code&gt;Filter&lt;/code&gt; element in the configuration, you must also add the following elements: &lt;code&gt;DeleteMarkerReplication&lt;/code&gt;, &lt;code&gt;Status&lt;/code&gt;, and &lt;code&gt;Priority&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Using &lt;code&gt;PutBucketReplication&lt;/code&gt; on Outposts requires that both the source and destination buckets must have versioning enabled. For information about enabling versioning on a bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsManagingVersioning.html\&quot;&gt;Managing S3 Versioning for your S3 on Outposts bucket&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For information about S3 on Outposts replication failure reasons, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-replication-eventbridge.html#outposts-replication-failure-codes\&quot;&gt;Replication failure reasons&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Handling Replication of Encrypted Objects&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Outposts buckets are encrypted at all times. All the objects in the source Outposts bucket are encrypted and can be replicated. Also, all the replicas in the destination Outposts bucket are encrypted with the same encryption key as the objects in the source Outposts bucket.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To create a &lt;code&gt;PutBucketReplication&lt;/code&gt; request, you must have &lt;code&gt;s3-outposts:PutReplicationConfiguration&lt;/code&gt; permissions for the bucket. The Outposts bucket owner has this permission by default and can grant it to others. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsIAM.html\&quot;&gt;Setting up IAM with S3 on Outposts&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsBucketPolicy.html\&quot;&gt;Managing access to S3 on Outposts buckets&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;To perform this operation, the user or role must also have the &lt;code&gt;iam:CreateRole&lt;/code&gt; and &lt;code&gt;iam:PassRole&lt;/code&gt; permissions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html\&quot;&gt;Granting a user permissions to pass a role to an Amazon Web Services service&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html#API_control_PutBucketReplication_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;PutBucketReplication&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html\&quot;&gt;GetBucketReplication&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketReplication.html\&quot;&gt;DeleteBucketReplication&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | <p>Specifies the S3 on Outposts bucket to set the configuration for.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let putBucketReplicationRequest = new AwsS3Control.PutBucketReplicationRequest(); // PutBucketReplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putBucketReplication(xAmzAccountId, name, putBucketReplicationRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;Specifies the S3 on Outposts bucket to set the configuration for.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **putBucketReplicationRequest** | [**PutBucketReplicationRequest**](PutBucketReplicationRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: Not defined


## putBucketTagging

> putBucketTagging(xAmzAccountId, name, putBucketTaggingRequest, opts)



&lt;note&gt; &lt;p&gt;This action puts tags on an Amazon S3 on Outposts bucket. To put tags on an S3 bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html\&quot;&gt;PutBucketTagging&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sets the tags for an S3 on Outposts bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html\&quot;&gt;Using Amazon S3 on Outposts&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Use tags to organize your Amazon Web Services bill to reflect your own cost structure. To do this, sign up to get your Amazon Web Services account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Cost allocation and tagging&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Within a bucket, if you add a tag that has the same key as an existing tag, the new value overwrites the old value. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html\&quot;&gt; Using cost allocation in Amazon S3 bucket tags&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To use this action, you must have permissions to perform the &lt;code&gt;s3-outposts:PutBucketTagging&lt;/code&gt; action. The Outposts bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources\&quot;&gt; Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html\&quot;&gt;Managing access permissions to your Amazon S3 resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutBucketTagging&lt;/code&gt; has the following special errors:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;InvalidTagError&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: The tag provided was not a valid tag. This error can occur if the tag did not pass input validation. For information about tag restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html\&quot;&gt; User-Defined Tag Restrictions&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tag-restrictions.html\&quot;&gt; Amazon Web Services-Generated Cost Allocation Tag Restrictions&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;MalformedXMLError&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: The XML provided does not match the schema.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;OperationAbortedError &lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: A conflicting conditional action is currently in progress against this resource. Try again.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;InternalError&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: The service was unable to apply the provided tag to the bucket.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketTagging.html#API_control_PutBucketTagging_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;PutBucketTagging&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html\&quot;&gt;GetBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketTagging.html\&quot;&gt;DeleteBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the Outposts bucket.
let name = "name_example"; // String | <p>The Amazon Resource Name (ARN) of the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:&lt;Region&gt;:&lt;account-id&gt;:outpost/&lt;outpost-id&gt;/bucket/&lt;my-bucket-name&gt;</code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
let putBucketTaggingRequest = new AwsS3Control.PutBucketTaggingRequest(); // PutBucketTaggingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putBucketTagging(xAmzAccountId, name, putBucketTaggingRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the Outposts bucket. | 
 **name** | **String**| &lt;p&gt;The Amazon Resource Name (ARN) of the bucket.&lt;/p&gt; &lt;p&gt;For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.&lt;/p&gt; &lt;p&gt;For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format &lt;code&gt;arn:aws:s3-outposts:&amp;lt;Region&amp;gt;:&amp;lt;account-id&amp;gt;:outpost/&amp;lt;outpost-id&amp;gt;/bucket/&amp;lt;my-bucket-name&amp;gt;&lt;/code&gt;. For example, to access the bucket &lt;code&gt;reports&lt;/code&gt; through Outpost &lt;code&gt;my-outpost&lt;/code&gt; owned by account &lt;code&gt;123456789012&lt;/code&gt; in Region &lt;code&gt;us-west-2&lt;/code&gt;, use the URL encoding of &lt;code&gt;arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports&lt;/code&gt;. The value must be URL encoded. &lt;/p&gt; | 
 **putBucketTaggingRequest** | [**PutBucketTaggingRequest**](PutBucketTaggingRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: Not defined


## putBucketVersioning

> putBucketVersioning(xAmzAccountId, name, putBucketVersioningRequest, opts)



&lt;note&gt; &lt;p&gt;This operation sets the versioning state for S3 on Outposts buckets only. To set the versioning state for an S3 bucket, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html\&quot;&gt;PutBucketVersioning&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sets the versioning state for an S3 on Outposts bucket. With S3 Versioning, you can save multiple distinct copies of your objects and recover from unintended user actions and application failures.&lt;/p&gt; &lt;p&gt;You can set the versioning state to one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Enabled&lt;/b&gt; - Enables versioning for the objects in the bucket. All objects added to the bucket receive a unique version ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Suspended&lt;/b&gt; - Suspends versioning for the objects in the bucket. All objects added to the bucket receive the version ID &lt;code&gt;null&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you&#39;ve never set versioning on your bucket, it has no versioning state. In that case, a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html\&quot;&gt; GetBucketVersioning&lt;/a&gt; request does not return a versioning state value.&lt;/p&gt; &lt;p&gt;When you enable S3 Versioning, for each object in your bucket, you have a current version and zero or more noncurrent versions. You can configure your bucket S3 Lifecycle rules to expire noncurrent versions after a specified time period. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsLifecycleManaging.html\&quot;&gt; Creating and managing a lifecycle configuration for your S3 on Outposts bucket&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you have an object expiration lifecycle configuration in your non-versioned bucket and you want to maintain the same permanent delete behavior when you enable versioning, you must add a noncurrent expiration policy. The noncurrent expiration lifecycle configuration will manage the deletes of the noncurrent object versions in the version-enabled bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html\&quot;&gt;Versioning&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;All Amazon S3 on Outposts REST API requests for this action require an additional parameter of &lt;code&gt;x-amz-outpost-id&lt;/code&gt; to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of &lt;code&gt;s3-control&lt;/code&gt;. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the &lt;code&gt;x-amz-outpost-id&lt;/code&gt; derived by using the access point ARN, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketVersioning.html#API_control_PutBucketVersioning_Examples\&quot;&gt;Examples&lt;/a&gt; section.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;PutBucketVersioning&lt;/code&gt; for S3 on Outposts.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html\&quot;&gt;GetBucketVersioning&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html\&quot;&gt;PutBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html\&quot;&gt;GetBucketLifecycleConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID of the S3 on Outposts bucket.
let name = "name_example"; // String | The S3 on Outposts bucket to set the versioning state for.
let putBucketVersioningRequest = new AwsS3Control.PutBucketVersioningRequest(); // PutBucketVersioningRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzMfa': "xAmzMfa_example" // String | The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.
};
apiInstance.putBucketVersioning(xAmzAccountId, name, putBucketVersioningRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID of the S3 on Outposts bucket. | 
 **name** | **String**| The S3 on Outposts bucket to set the versioning state for. | 
 **putBucketVersioningRequest** | [**PutBucketVersioningRequest**](PutBucketVersioningRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzMfa** | **String**| The concatenation of the authentication device&#39;s serial number, a space, and the value that is displayed on your authentication device. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: Not defined


## putJobTagging

> Object putJobTagging(xAmzAccountId, id, putJobTaggingRequest, opts)



&lt;p&gt;Sets the supplied tag-set on an S3 Batch Operations job.&lt;/p&gt; &lt;p&gt;A tag is a key-value pair. You can associate S3 Batch Operations tags with any job by sending a PUT request against the tagging subresource that is associated with the job. To modify the existing tag set, you can either replace the existing tag set entirely, or make changes within the existing tag set by retrieving the existing tag set using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html\&quot;&gt;GetJobTagging&lt;/a&gt;, modify that tag set, and use this action to replace the tag set with the one you modified. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags\&quot;&gt;Controlling access and labeling jobs using tags&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p/&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you send this request with an empty tag set, Amazon S3 deletes the existing tag set on the Batch Operations job. If you use this method, you are charged for a Tier 1 Request (PUT). For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/s3/pricing/\&quot;&gt;Amazon S3 pricing&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For deleting existing tags for your Batch Operations job, a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html\&quot;&gt;DeleteJobTagging&lt;/a&gt; request is preferred because it achieves the same result without incurring charges.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A few things to consider about using tags:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon S3 limits the maximum number of tags to 50 tags per job.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can associate up to 50 tags with a job as long as they have unique tag keys.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A tag key can be up to 128 Unicode characters in length, and tag values can be up to 256 Unicode characters in length.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The key and values are case sensitive.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For tagging-related restrictions related to characters and encodings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html\&quot;&gt;User-Defined Tag Restrictions&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p/&gt; &lt;p&gt;To use the &lt;code&gt;PutJobTagging&lt;/code&gt; operation, you must have permission to perform the &lt;code&gt;s3:PutJobTagging&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html\&quot;&gt;CreateJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html\&quot;&gt;GetJobTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html\&quot;&gt;DeleteJobTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID associated with the S3 Batch Operations job.
let id = "id_example"; // String | The ID for the S3 Batch Operations job whose tags you want to replace.
let putJobTaggingRequest = new AwsS3Control.PutJobTaggingRequest(); // PutJobTaggingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putJobTagging(xAmzAccountId, id, putJobTaggingRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID associated with the S3 Batch Operations job. | 
 **id** | **String**| The ID for the S3 Batch Operations job whose tags you want to replace. | 
 **putJobTaggingRequest** | [**PutJobTaggingRequest**](PutJobTaggingRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: text/xml


## putMultiRegionAccessPointPolicy

> PutMultiRegionAccessPointPolicyResult putMultiRegionAccessPointPolicy(xAmzAccountId, putMultiRegionAccessPointPolicyRequest, opts)



&lt;p&gt;Associates an access control policy with the specified Multi-Region Access Point. Each Multi-Region Access Point can have only one policy, so a request made to this action replaces any existing policy that is associated with the specified Multi-Region Access Point.&lt;/p&gt; &lt;p&gt;This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around managing Multi-Region Access Points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html\&quot;&gt;Managing Multi-Region Access Points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following actions are related to &lt;code&gt;PutMultiRegionAccessPointPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html\&quot;&gt;GetMultiRegionAccessPointPolicy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html\&quot;&gt;GetMultiRegionAccessPointPolicyStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let putMultiRegionAccessPointPolicyRequest = new AwsS3Control.PutMultiRegionAccessPointPolicyRequest(); // PutMultiRegionAccessPointPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putMultiRegionAccessPointPolicy(xAmzAccountId, putMultiRegionAccessPointPolicyRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **putMultiRegionAccessPointPolicyRequest** | [**PutMultiRegionAccessPointPolicyRequest**](PutMultiRegionAccessPointPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutMultiRegionAccessPointPolicyResult**](PutMultiRegionAccessPointPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## putPublicAccessBlock

> putPublicAccessBlock(xAmzAccountId, putPublicAccessBlockRequest, opts)



&lt;p&gt;Creates or modifies the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for an Amazon Web Services account. For this operation, users must have the &lt;code&gt;s3:PutAccountPublicAccessBlock&lt;/code&gt; permission. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html\&quot;&gt; Using Amazon S3 block public access&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html\&quot;&gt;GetPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeletePublicAccessBlock.html\&quot;&gt;DeletePublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to set.
let putPublicAccessBlockRequest = new AwsS3Control.PutPublicAccessBlockRequest(); // PutPublicAccessBlockRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putPublicAccessBlock(xAmzAccountId, putPublicAccessBlockRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The account ID for the Amazon Web Services account whose &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration you want to set. | 
 **putPublicAccessBlockRequest** | [**PutPublicAccessBlockRequest**](PutPublicAccessBlockRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: Not defined


## putStorageLensConfiguration

> putStorageLensConfiguration(storagelensid, xAmzAccountId, putStorageLensConfigurationRequest, opts)



&lt;p&gt;Puts an Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html\&quot;&gt;Working with Amazon S3 Storage Lens&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. For a complete list of S3 Storage Lens metrics, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html\&quot;&gt;S3 Storage Lens metrics glossary&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3:PutStorageLensConfiguration&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html\&quot;&gt;Setting permissions to use Amazon S3 Storage Lens&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let storagelensid = "storagelensid_example"; // String | The ID of the S3 Storage Lens configuration.
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the requester.
let putStorageLensConfigurationRequest = new AwsS3Control.PutStorageLensConfigurationRequest(); // PutStorageLensConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putStorageLensConfiguration(storagelensid, xAmzAccountId, putStorageLensConfigurationRequest, opts, (error, data, response) => {
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
 **storagelensid** | **String**| The ID of the S3 Storage Lens configuration. | 
 **xAmzAccountId** | **String**| The account ID of the requester. | 
 **putStorageLensConfigurationRequest** | [**PutStorageLensConfigurationRequest**](PutStorageLensConfigurationRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: Not defined


## putStorageLensConfigurationTagging

> Object putStorageLensConfigurationTagging(storagelensid, xAmzAccountId, putStorageLensConfigurationTaggingRequest, opts)



&lt;p&gt;Put or replace tags on an existing Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html\&quot;&gt;Assessing your storage activity and usage with Amazon S3 Storage Lens &lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this action, you must have permission to perform the &lt;code&gt;s3:PutStorageLensConfigurationTagging&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html\&quot;&gt;Setting permissions to use Amazon S3 Storage Lens&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let storagelensid = "storagelensid_example"; // String | The ID of the S3 Storage Lens configuration.
let xAmzAccountId = "xAmzAccountId_example"; // String | The account ID of the requester.
let putStorageLensConfigurationTaggingRequest = new AwsS3Control.PutStorageLensConfigurationTaggingRequest(); // PutStorageLensConfigurationTaggingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putStorageLensConfigurationTagging(storagelensid, xAmzAccountId, putStorageLensConfigurationTaggingRequest, opts, (error, data, response) => {
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
 **storagelensid** | **String**| The ID of the S3 Storage Lens configuration. | 
 **xAmzAccountId** | **String**| The account ID of the requester. | 
 **putStorageLensConfigurationTaggingRequest** | [**PutStorageLensConfigurationTaggingRequest**](PutStorageLensConfigurationTaggingRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: text/xml


## submitMultiRegionAccessPointRoutes

> Object submitMultiRegionAccessPointRoutes(xAmzAccountId, mrap, submitMultiRegionAccessPointRoutesRequest, opts)



&lt;p&gt;Submits an updated route configuration for a Multi-Region Access Point. This API operation updates the routing status for the specified Regions from active to passive, or from passive to active. A value of &lt;code&gt;0&lt;/code&gt; indicates a passive status, which means that traffic won&#39;t be routed to the specified Region. A value of &lt;code&gt;100&lt;/code&gt; indicates an active status, which means that traffic will be routed to the specified Region. At least one Region must be active at all times.&lt;/p&gt; &lt;p&gt;When the routing configuration is changed, any in-progress operations (uploads, copies, deletes, and so on) to formerly active Regions will continue to run to their final completion state (success or failure). The routing configurations of any Regions that aren’t specified remain unchanged.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Updated routing configurations might not be immediately applied. It can take up to 2 minutes for your changes to take effect.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To submit routing control changes and failover requests, use the Amazon S3 failover control infrastructure endpoints in these five Amazon Web Services Regions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;us-east-1&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;us-west-2&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ap-southeast-2&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ap-northeast-1&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;eu-west-1&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;Your Amazon S3 bucket does not need to be in these five Regions.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID for the owner of the Multi-Region Access Point.
let mrap = "mrap_example"; // String | The Multi-Region Access Point ARN.
let submitMultiRegionAccessPointRoutesRequest = new AwsS3Control.SubmitMultiRegionAccessPointRoutesRequest(); // SubmitMultiRegionAccessPointRoutesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.submitMultiRegionAccessPointRoutes(xAmzAccountId, mrap, submitMultiRegionAccessPointRoutesRequest, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID for the owner of the Multi-Region Access Point. | 
 **mrap** | **String**| The Multi-Region Access Point ARN. | 
 **submitMultiRegionAccessPointRoutesRequest** | [**SubmitMultiRegionAccessPointRoutesRequest**](SubmitMultiRegionAccessPointRoutesRequest.md)|  | 
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

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateJobPriority

> UpdateJobPriorityResult updateJobPriority(xAmzAccountId, id, priority, opts)



&lt;p&gt;Updates an existing S3 Batch Operations job&#39;s priority. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html\&quot;&gt;S3 Batch Operations&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html\&quot;&gt;CreateJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html\&quot;&gt;ListJobs&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html\&quot;&gt;DescribeJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html\&quot;&gt;UpdateJobStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID associated with the S3 Batch Operations job.
let id = "id_example"; // String | The ID for the job whose priority you want to update.
let priority = 56; // Number | The priority you want to assign to this job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateJobPriority(xAmzAccountId, id, priority, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID associated with the S3 Batch Operations job. | 
 **id** | **String**| The ID for the job whose priority you want to update. | 
 **priority** | **Number**| The priority you want to assign to this job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateJobPriorityResult**](UpdateJobPriorityResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## updateJobStatus

> UpdateJobStatusResult updateJobStatus(xAmzAccountId, id, requestedJobStatus, opts)



&lt;p&gt;Updates the status for the specified job. Use this action to confirm that you want to run a job or to cancel an existing job. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html\&quot;&gt;S3 Batch Operations&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html\&quot;&gt;CreateJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html\&quot;&gt;ListJobs&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html\&quot;&gt;DescribeJob&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html\&quot;&gt;UpdateJobStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsS3Control from 'aws_s3_control';
let defaultClient = AwsS3Control.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsS3Control.DefaultApi();
let xAmzAccountId = "xAmzAccountId_example"; // String | The Amazon Web Services account ID associated with the S3 Batch Operations job.
let id = "id_example"; // String | The ID of the job whose status you want to update.
let requestedJobStatus = "requestedJobStatus_example"; // String | The status that you want to move the specified job to.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'statusUpdateReason': "statusUpdateReason_example" // String | A description of the reason why you want to change the specified job's status. This field can be any string up to the maximum length.
};
apiInstance.updateJobStatus(xAmzAccountId, id, requestedJobStatus, opts, (error, data, response) => {
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
 **xAmzAccountId** | **String**| The Amazon Web Services account ID associated with the S3 Batch Operations job. | 
 **id** | **String**| The ID of the job whose status you want to update. | 
 **requestedJobStatus** | **String**| The status that you want to move the specified job to. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **statusUpdateReason** | **String**| A description of the reason why you want to change the specified job&#39;s status. This field can be any string up to the maximum length. | [optional] 

### Return type

[**UpdateJobStatusResult**](UpdateJobStatusResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml

