# AmazonCloudFront.DefaultApi

All URIs are relative to *https://cloudfront.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateAlias20200531**](DefaultApi.md#associateAlias20200531) | **PUT** /2020-05-31/distribution/{TargetDistributionId}/associate-alias#Alias | 
[**copyDistribution20200531**](DefaultApi.md#copyDistribution20200531) | **POST** /2020-05-31/distribution/{PrimaryDistributionId}/copy | 
[**createCachePolicy20200531**](DefaultApi.md#createCachePolicy20200531) | **POST** /2020-05-31/cache-policy | 
[**createCloudFrontOriginAccessIdentity20200531**](DefaultApi.md#createCloudFrontOriginAccessIdentity20200531) | **POST** /2020-05-31/origin-access-identity/cloudfront | 
[**createContinuousDeploymentPolicy20200531**](DefaultApi.md#createContinuousDeploymentPolicy20200531) | **POST** /2020-05-31/continuous-deployment-policy | 
[**createDistribution20200531**](DefaultApi.md#createDistribution20200531) | **POST** /2020-05-31/distribution | 
[**createDistributionWithTags20200531**](DefaultApi.md#createDistributionWithTags20200531) | **POST** /2020-05-31/distribution#WithTags | 
[**createFieldLevelEncryptionConfig20200531**](DefaultApi.md#createFieldLevelEncryptionConfig20200531) | **POST** /2020-05-31/field-level-encryption | 
[**createFieldLevelEncryptionProfile20200531**](DefaultApi.md#createFieldLevelEncryptionProfile20200531) | **POST** /2020-05-31/field-level-encryption-profile | 
[**createFunction20200531**](DefaultApi.md#createFunction20200531) | **POST** /2020-05-31/function | 
[**createInvalidation20200531**](DefaultApi.md#createInvalidation20200531) | **POST** /2020-05-31/distribution/{DistributionId}/invalidation | 
[**createKeyGroup20200531**](DefaultApi.md#createKeyGroup20200531) | **POST** /2020-05-31/key-group | 
[**createMonitoringSubscription20200531**](DefaultApi.md#createMonitoringSubscription20200531) | **POST** /2020-05-31/distributions/{DistributionId}/monitoring-subscription/ | 
[**createOriginAccessControl20200531**](DefaultApi.md#createOriginAccessControl20200531) | **POST** /2020-05-31/origin-access-control | 
[**createOriginRequestPolicy20200531**](DefaultApi.md#createOriginRequestPolicy20200531) | **POST** /2020-05-31/origin-request-policy | 
[**createPublicKey20200531**](DefaultApi.md#createPublicKey20200531) | **POST** /2020-05-31/public-key | 
[**createRealtimeLogConfig20200531**](DefaultApi.md#createRealtimeLogConfig20200531) | **POST** /2020-05-31/realtime-log-config | 
[**createResponseHeadersPolicy20200531**](DefaultApi.md#createResponseHeadersPolicy20200531) | **POST** /2020-05-31/response-headers-policy | 
[**createStreamingDistribution20200531**](DefaultApi.md#createStreamingDistribution20200531) | **POST** /2020-05-31/streaming-distribution | 
[**createStreamingDistributionWithTags20200531**](DefaultApi.md#createStreamingDistributionWithTags20200531) | **POST** /2020-05-31/streaming-distribution#WithTags | 
[**deleteCachePolicy20200531**](DefaultApi.md#deleteCachePolicy20200531) | **DELETE** /2020-05-31/cache-policy/{Id} | 
[**deleteCloudFrontOriginAccessIdentity20200531**](DefaultApi.md#deleteCloudFrontOriginAccessIdentity20200531) | **DELETE** /2020-05-31/origin-access-identity/cloudfront/{Id} | 
[**deleteContinuousDeploymentPolicy20200531**](DefaultApi.md#deleteContinuousDeploymentPolicy20200531) | **DELETE** /2020-05-31/continuous-deployment-policy/{Id} | 
[**deleteDistribution20200531**](DefaultApi.md#deleteDistribution20200531) | **DELETE** /2020-05-31/distribution/{Id} | 
[**deleteFieldLevelEncryptionConfig20200531**](DefaultApi.md#deleteFieldLevelEncryptionConfig20200531) | **DELETE** /2020-05-31/field-level-encryption/{Id} | 
[**deleteFieldLevelEncryptionProfile20200531**](DefaultApi.md#deleteFieldLevelEncryptionProfile20200531) | **DELETE** /2020-05-31/field-level-encryption-profile/{Id} | 
[**deleteFunction20200531**](DefaultApi.md#deleteFunction20200531) | **DELETE** /2020-05-31/function/{Name}#If-Match | 
[**deleteKeyGroup20200531**](DefaultApi.md#deleteKeyGroup20200531) | **DELETE** /2020-05-31/key-group/{Id} | 
[**deleteMonitoringSubscription20200531**](DefaultApi.md#deleteMonitoringSubscription20200531) | **DELETE** /2020-05-31/distributions/{DistributionId}/monitoring-subscription/ | 
[**deleteOriginAccessControl20200531**](DefaultApi.md#deleteOriginAccessControl20200531) | **DELETE** /2020-05-31/origin-access-control/{Id} | 
[**deleteOriginRequestPolicy20200531**](DefaultApi.md#deleteOriginRequestPolicy20200531) | **DELETE** /2020-05-31/origin-request-policy/{Id} | 
[**deletePublicKey20200531**](DefaultApi.md#deletePublicKey20200531) | **DELETE** /2020-05-31/public-key/{Id} | 
[**deleteRealtimeLogConfig20200531**](DefaultApi.md#deleteRealtimeLogConfig20200531) | **POST** /2020-05-31/delete-realtime-log-config/ | 
[**deleteResponseHeadersPolicy20200531**](DefaultApi.md#deleteResponseHeadersPolicy20200531) | **DELETE** /2020-05-31/response-headers-policy/{Id} | 
[**deleteStreamingDistribution20200531**](DefaultApi.md#deleteStreamingDistribution20200531) | **DELETE** /2020-05-31/streaming-distribution/{Id} | 
[**describeFunction20200531**](DefaultApi.md#describeFunction20200531) | **GET** /2020-05-31/function/{Name}/describe | 
[**getCachePolicy20200531**](DefaultApi.md#getCachePolicy20200531) | **GET** /2020-05-31/cache-policy/{Id} | 
[**getCachePolicyConfig20200531**](DefaultApi.md#getCachePolicyConfig20200531) | **GET** /2020-05-31/cache-policy/{Id}/config | 
[**getCloudFrontOriginAccessIdentity20200531**](DefaultApi.md#getCloudFrontOriginAccessIdentity20200531) | **GET** /2020-05-31/origin-access-identity/cloudfront/{Id} | 
[**getCloudFrontOriginAccessIdentityConfig20200531**](DefaultApi.md#getCloudFrontOriginAccessIdentityConfig20200531) | **GET** /2020-05-31/origin-access-identity/cloudfront/{Id}/config | 
[**getContinuousDeploymentPolicy20200531**](DefaultApi.md#getContinuousDeploymentPolicy20200531) | **GET** /2020-05-31/continuous-deployment-policy/{Id} | 
[**getContinuousDeploymentPolicyConfig20200531**](DefaultApi.md#getContinuousDeploymentPolicyConfig20200531) | **GET** /2020-05-31/continuous-deployment-policy/{Id}/config | 
[**getDistribution20200531**](DefaultApi.md#getDistribution20200531) | **GET** /2020-05-31/distribution/{Id} | 
[**getDistributionConfig20200531**](DefaultApi.md#getDistributionConfig20200531) | **GET** /2020-05-31/distribution/{Id}/config | 
[**getFieldLevelEncryption20200531**](DefaultApi.md#getFieldLevelEncryption20200531) | **GET** /2020-05-31/field-level-encryption/{Id} | 
[**getFieldLevelEncryptionConfig20200531**](DefaultApi.md#getFieldLevelEncryptionConfig20200531) | **GET** /2020-05-31/field-level-encryption/{Id}/config | 
[**getFieldLevelEncryptionProfile20200531**](DefaultApi.md#getFieldLevelEncryptionProfile20200531) | **GET** /2020-05-31/field-level-encryption-profile/{Id} | 
[**getFieldLevelEncryptionProfileConfig20200531**](DefaultApi.md#getFieldLevelEncryptionProfileConfig20200531) | **GET** /2020-05-31/field-level-encryption-profile/{Id}/config | 
[**getFunction20200531**](DefaultApi.md#getFunction20200531) | **GET** /2020-05-31/function/{Name} | 
[**getInvalidation20200531**](DefaultApi.md#getInvalidation20200531) | **GET** /2020-05-31/distribution/{DistributionId}/invalidation/{Id} | 
[**getKeyGroup20200531**](DefaultApi.md#getKeyGroup20200531) | **GET** /2020-05-31/key-group/{Id} | 
[**getKeyGroupConfig20200531**](DefaultApi.md#getKeyGroupConfig20200531) | **GET** /2020-05-31/key-group/{Id}/config | 
[**getMonitoringSubscription20200531**](DefaultApi.md#getMonitoringSubscription20200531) | **GET** /2020-05-31/distributions/{DistributionId}/monitoring-subscription/ | 
[**getOriginAccessControl20200531**](DefaultApi.md#getOriginAccessControl20200531) | **GET** /2020-05-31/origin-access-control/{Id} | 
[**getOriginAccessControlConfig20200531**](DefaultApi.md#getOriginAccessControlConfig20200531) | **GET** /2020-05-31/origin-access-control/{Id}/config | 
[**getOriginRequestPolicy20200531**](DefaultApi.md#getOriginRequestPolicy20200531) | **GET** /2020-05-31/origin-request-policy/{Id} | 
[**getOriginRequestPolicyConfig20200531**](DefaultApi.md#getOriginRequestPolicyConfig20200531) | **GET** /2020-05-31/origin-request-policy/{Id}/config | 
[**getPublicKey20200531**](DefaultApi.md#getPublicKey20200531) | **GET** /2020-05-31/public-key/{Id} | 
[**getPublicKeyConfig20200531**](DefaultApi.md#getPublicKeyConfig20200531) | **GET** /2020-05-31/public-key/{Id}/config | 
[**getRealtimeLogConfig20200531**](DefaultApi.md#getRealtimeLogConfig20200531) | **POST** /2020-05-31/get-realtime-log-config/ | 
[**getResponseHeadersPolicy20200531**](DefaultApi.md#getResponseHeadersPolicy20200531) | **GET** /2020-05-31/response-headers-policy/{Id} | 
[**getResponseHeadersPolicyConfig20200531**](DefaultApi.md#getResponseHeadersPolicyConfig20200531) | **GET** /2020-05-31/response-headers-policy/{Id}/config | 
[**getStreamingDistribution20200531**](DefaultApi.md#getStreamingDistribution20200531) | **GET** /2020-05-31/streaming-distribution/{Id} | 
[**getStreamingDistributionConfig20200531**](DefaultApi.md#getStreamingDistributionConfig20200531) | **GET** /2020-05-31/streaming-distribution/{Id}/config | 
[**listCachePolicies20200531**](DefaultApi.md#listCachePolicies20200531) | **GET** /2020-05-31/cache-policy | 
[**listCloudFrontOriginAccessIdentities20200531**](DefaultApi.md#listCloudFrontOriginAccessIdentities20200531) | **GET** /2020-05-31/origin-access-identity/cloudfront | 
[**listConflictingAliases20200531**](DefaultApi.md#listConflictingAliases20200531) | **GET** /2020-05-31/conflicting-alias#DistributionId&amp;Alias | 
[**listContinuousDeploymentPolicies20200531**](DefaultApi.md#listContinuousDeploymentPolicies20200531) | **GET** /2020-05-31/continuous-deployment-policy | 
[**listDistributions20200531**](DefaultApi.md#listDistributions20200531) | **GET** /2020-05-31/distribution | 
[**listDistributionsByCachePolicyId20200531**](DefaultApi.md#listDistributionsByCachePolicyId20200531) | **GET** /2020-05-31/distributionsByCachePolicyId/{CachePolicyId} | 
[**listDistributionsByKeyGroup20200531**](DefaultApi.md#listDistributionsByKeyGroup20200531) | **GET** /2020-05-31/distributionsByKeyGroupId/{KeyGroupId} | 
[**listDistributionsByOriginRequestPolicyId20200531**](DefaultApi.md#listDistributionsByOriginRequestPolicyId20200531) | **GET** /2020-05-31/distributionsByOriginRequestPolicyId/{OriginRequestPolicyId} | 
[**listDistributionsByRealtimeLogConfig20200531**](DefaultApi.md#listDistributionsByRealtimeLogConfig20200531) | **POST** /2020-05-31/distributionsByRealtimeLogConfig/ | 
[**listDistributionsByResponseHeadersPolicyId20200531**](DefaultApi.md#listDistributionsByResponseHeadersPolicyId20200531) | **GET** /2020-05-31/distributionsByResponseHeadersPolicyId/{ResponseHeadersPolicyId} | 
[**listDistributionsByWebACLId20200531**](DefaultApi.md#listDistributionsByWebACLId20200531) | **GET** /2020-05-31/distributionsByWebACLId/{WebACLId} | 
[**listFieldLevelEncryptionConfigs20200531**](DefaultApi.md#listFieldLevelEncryptionConfigs20200531) | **GET** /2020-05-31/field-level-encryption | 
[**listFieldLevelEncryptionProfiles20200531**](DefaultApi.md#listFieldLevelEncryptionProfiles20200531) | **GET** /2020-05-31/field-level-encryption-profile | 
[**listFunctions20200531**](DefaultApi.md#listFunctions20200531) | **GET** /2020-05-31/function | 
[**listInvalidations20200531**](DefaultApi.md#listInvalidations20200531) | **GET** /2020-05-31/distribution/{DistributionId}/invalidation | 
[**listKeyGroups20200531**](DefaultApi.md#listKeyGroups20200531) | **GET** /2020-05-31/key-group | 
[**listOriginAccessControls20200531**](DefaultApi.md#listOriginAccessControls20200531) | **GET** /2020-05-31/origin-access-control | 
[**listOriginRequestPolicies20200531**](DefaultApi.md#listOriginRequestPolicies20200531) | **GET** /2020-05-31/origin-request-policy | 
[**listPublicKeys20200531**](DefaultApi.md#listPublicKeys20200531) | **GET** /2020-05-31/public-key | 
[**listRealtimeLogConfigs20200531**](DefaultApi.md#listRealtimeLogConfigs20200531) | **GET** /2020-05-31/realtime-log-config | 
[**listResponseHeadersPolicies20200531**](DefaultApi.md#listResponseHeadersPolicies20200531) | **GET** /2020-05-31/response-headers-policy | 
[**listStreamingDistributions20200531**](DefaultApi.md#listStreamingDistributions20200531) | **GET** /2020-05-31/streaming-distribution | 
[**listTagsForResource20200531**](DefaultApi.md#listTagsForResource20200531) | **GET** /2020-05-31/tagging#Resource | 
[**publishFunction20200531**](DefaultApi.md#publishFunction20200531) | **POST** /2020-05-31/function/{Name}/publish#If-Match | 
[**tagResource20200531**](DefaultApi.md#tagResource20200531) | **POST** /2020-05-31/tagging#Operation&#x3D;Tag&amp;Resource | 
[**testFunction20200531**](DefaultApi.md#testFunction20200531) | **POST** /2020-05-31/function/{Name}/test#If-Match | 
[**untagResource20200531**](DefaultApi.md#untagResource20200531) | **POST** /2020-05-31/tagging#Operation&#x3D;Untag&amp;Resource | 
[**updateCachePolicy20200531**](DefaultApi.md#updateCachePolicy20200531) | **PUT** /2020-05-31/cache-policy/{Id} | 
[**updateCloudFrontOriginAccessIdentity20200531**](DefaultApi.md#updateCloudFrontOriginAccessIdentity20200531) | **PUT** /2020-05-31/origin-access-identity/cloudfront/{Id}/config | 
[**updateContinuousDeploymentPolicy20200531**](DefaultApi.md#updateContinuousDeploymentPolicy20200531) | **PUT** /2020-05-31/continuous-deployment-policy/{Id} | 
[**updateDistribution20200531**](DefaultApi.md#updateDistribution20200531) | **PUT** /2020-05-31/distribution/{Id}/config | 
[**updateDistributionWithStagingConfig20200531**](DefaultApi.md#updateDistributionWithStagingConfig20200531) | **PUT** /2020-05-31/distribution/{Id}/promote-staging-config | 
[**updateFieldLevelEncryptionConfig20200531**](DefaultApi.md#updateFieldLevelEncryptionConfig20200531) | **PUT** /2020-05-31/field-level-encryption/{Id}/config | 
[**updateFieldLevelEncryptionProfile20200531**](DefaultApi.md#updateFieldLevelEncryptionProfile20200531) | **PUT** /2020-05-31/field-level-encryption-profile/{Id}/config | 
[**updateFunction20200531**](DefaultApi.md#updateFunction20200531) | **PUT** /2020-05-31/function/{Name}#If-Match | 
[**updateKeyGroup20200531**](DefaultApi.md#updateKeyGroup20200531) | **PUT** /2020-05-31/key-group/{Id} | 
[**updateOriginAccessControl20200531**](DefaultApi.md#updateOriginAccessControl20200531) | **PUT** /2020-05-31/origin-access-control/{Id}/config | 
[**updateOriginRequestPolicy20200531**](DefaultApi.md#updateOriginRequestPolicy20200531) | **PUT** /2020-05-31/origin-request-policy/{Id} | 
[**updatePublicKey20200531**](DefaultApi.md#updatePublicKey20200531) | **PUT** /2020-05-31/public-key/{Id}/config | 
[**updateRealtimeLogConfig20200531**](DefaultApi.md#updateRealtimeLogConfig20200531) | **PUT** /2020-05-31/realtime-log-config/ | 
[**updateResponseHeadersPolicy20200531**](DefaultApi.md#updateResponseHeadersPolicy20200531) | **PUT** /2020-05-31/response-headers-policy/{Id} | 
[**updateStreamingDistribution20200531**](DefaultApi.md#updateStreamingDistribution20200531) | **PUT** /2020-05-31/streaming-distribution/{Id}/config | 



## associateAlias20200531

> associateAlias20200531(targetDistributionId, alias, opts)



&lt;p&gt;Associates an alias (also known as a CNAME or an alternate domain name) with a CloudFront distribution.&lt;/p&gt; &lt;p&gt;With this operation you can move an alias that&#39;s already in use on a CloudFront distribution to a different distribution in one step. This prevents the downtime that could occur if you first remove the alias from one distribution and then separately add the alias to another distribution.&lt;/p&gt; &lt;p&gt;To use this operation to associate an alias with a distribution, you provide the alias and the ID of the target distribution for the alias. For more information, including how to set up the target distribution, prerequisites that you must complete, and other restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\&quot;&gt;Moving an alternate domain name to a different distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let targetDistributionId = "targetDistributionId_example"; // String | The ID of the distribution that you're associating the alias with.
let alias = "alias_example"; // String | The alias (also known as a CNAME) to add to the target distribution.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateAlias20200531(targetDistributionId, alias, opts, (error, data, response) => {
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
 **targetDistributionId** | **String**| The ID of the distribution that you&#39;re associating the alias with. | 
 **alias** | **String**| The alias (also known as a CNAME) to add to the target distribution. | 
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
- **Accept**: text/xml


## copyDistribution20200531

> CopyDistributionResult copyDistribution20200531(primaryDistributionId, copyDistribution20200531Request, opts)



&lt;p&gt;Creates a staging distribution using the configuration of the provided primary distribution. A staging distribution is a copy of an existing distribution (called the primary distribution) that you can use in a continuous deployment workflow.&lt;/p&gt; &lt;p&gt;After you create a staging distribution, you can use &lt;code&gt;UpdateDistribution&lt;/code&gt; to modify the staging distribution&#39;s configuration. Then you can use &lt;code&gt;CreateContinuousDeploymentPolicy&lt;/code&gt; to incrementally move traffic to the staging distribution.&lt;/p&gt; &lt;p&gt;This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html\&quot;&gt;GetDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html\&quot;&gt;CreateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CopyDistribution.html\&quot;&gt;CopyDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let primaryDistributionId = "primaryDistributionId_example"; // String | The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use <code>ListDistributions</code>.
let copyDistribution20200531Request = new AmazonCloudFront.CopyDistribution20200531Request(); // CopyDistribution20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'staging': true, // Boolean | The type of distribution that your primary distribution will be copied to. The only valid value is <code>True</code>, indicating that you are copying to a staging distribution.
  'ifMatch': "ifMatch_example" // String | The version identifier of the primary distribution whose configuration you are copying. This is the <code>ETag</code> value returned in the response to <code>GetDistribution</code> and <code>GetDistributionConfig</code>.
};
apiInstance.copyDistribution20200531(primaryDistributionId, copyDistribution20200531Request, opts, (error, data, response) => {
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
 **primaryDistributionId** | **String**| The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use &lt;code&gt;ListDistributions&lt;/code&gt;. | 
 **copyDistribution20200531Request** | [**CopyDistribution20200531Request**](CopyDistribution20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **staging** | **Boolean**| The type of distribution that your primary distribution will be copied to. The only valid value is &lt;code&gt;True&lt;/code&gt;, indicating that you are copying to a staging distribution. | [optional] 
 **ifMatch** | **String**| The version identifier of the primary distribution whose configuration you are copying. This is the &lt;code&gt;ETag&lt;/code&gt; value returned in the response to &lt;code&gt;GetDistribution&lt;/code&gt; and &lt;code&gt;GetDistributionConfig&lt;/code&gt;. | [optional] 

### Return type

[**CopyDistributionResult**](CopyDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createCachePolicy20200531

> CreateCachePolicyResult createCachePolicy20200531(createCachePolicy20200531Request, opts)



&lt;p&gt;Creates a cache policy.&lt;/p&gt; &lt;p&gt;After you create a cache policy, you can attach it to one or more cache behaviors. When it&#39;s attached to a cache behavior, the cache policy determines the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The values that CloudFront includes in the &lt;i&gt;cache key&lt;/i&gt;. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can&#39;t find an object in its cache that matches the request&#39;s cache key. If you want to send values to the origin but &lt;i&gt;not&lt;/i&gt; include them in the cache key, use &lt;code&gt;OriginRequestPolicy&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about cache policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html\&quot;&gt;Controlling the cache key&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createCachePolicy20200531Request = new AmazonCloudFront.CreateCachePolicy20200531Request(); // CreateCachePolicy20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCachePolicy20200531(createCachePolicy20200531Request, opts, (error, data, response) => {
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
 **createCachePolicy20200531Request** | [**CreateCachePolicy20200531Request**](CreateCachePolicy20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCachePolicyResult**](CreateCachePolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createCloudFrontOriginAccessIdentity20200531

> CreateCloudFrontOriginAccessIdentityResult createCloudFrontOriginAccessIdentity20200531(createCloudFrontOriginAccessIdentity20200531Request, opts)



Creates a new origin access identity. If you&#39;re using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving Private Content through CloudFront&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createCloudFrontOriginAccessIdentity20200531Request = new AmazonCloudFront.CreateCloudFrontOriginAccessIdentity20200531Request(); // CreateCloudFrontOriginAccessIdentity20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCloudFrontOriginAccessIdentity20200531(createCloudFrontOriginAccessIdentity20200531Request, opts, (error, data, response) => {
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
 **createCloudFrontOriginAccessIdentity20200531Request** | [**CreateCloudFrontOriginAccessIdentity20200531Request**](CreateCloudFrontOriginAccessIdentity20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCloudFrontOriginAccessIdentityResult**](CreateCloudFrontOriginAccessIdentityResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createContinuousDeploymentPolicy20200531

> CreateContinuousDeploymentPolicyResult createContinuousDeploymentPolicy20200531(createContinuousDeploymentPolicy20200531Request, opts)



&lt;p&gt;Creates a continuous deployment policy that distributes traffic for a custom domain name to two different CloudFront distributions.&lt;/p&gt; &lt;p&gt;To use a continuous deployment policy, first use &lt;code&gt;CopyDistribution&lt;/code&gt; to create a staging distribution, then use &lt;code&gt;UpdateDistribution&lt;/code&gt; to modify the staging distribution&#39;s configuration.&lt;/p&gt; &lt;p&gt;After you create and update a staging distribution, you can use a continuous deployment policy to incrementally move traffic to the staging distribution. This workflow enables you to test changes to a distribution&#39;s configuration before moving all of your domain&#39;s production traffic to the new configuration.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createContinuousDeploymentPolicy20200531Request = new AmazonCloudFront.CreateContinuousDeploymentPolicy20200531Request(); // CreateContinuousDeploymentPolicy20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContinuousDeploymentPolicy20200531(createContinuousDeploymentPolicy20200531Request, opts, (error, data, response) => {
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
 **createContinuousDeploymentPolicy20200531Request** | [**CreateContinuousDeploymentPolicy20200531Request**](CreateContinuousDeploymentPolicy20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateContinuousDeploymentPolicyResult**](CreateContinuousDeploymentPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createDistribution20200531

> CreateDistributionResult createDistribution20200531(createDistribution20200531Request, opts)



Creates a CloudFront distribution.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createDistribution20200531Request = new AmazonCloudFront.CreateDistribution20200531Request(); // CreateDistribution20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDistribution20200531(createDistribution20200531Request, opts, (error, data, response) => {
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
 **createDistribution20200531Request** | [**CreateDistribution20200531Request**](CreateDistribution20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDistributionResult**](CreateDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createDistributionWithTags20200531

> CreateDistributionWithTagsResult createDistributionWithTags20200531(withTags, createDistributionWithTags20200531Request, opts)



&lt;p&gt;Create a new distribution with tags. This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html\&quot;&gt;CreateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let withTags = true; // Boolean | 
let createDistributionWithTags20200531Request = new AmazonCloudFront.CreateDistributionWithTags20200531Request(); // CreateDistributionWithTags20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDistributionWithTags20200531(withTags, createDistributionWithTags20200531Request, opts, (error, data, response) => {
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
 **withTags** | **Boolean**|  | 
 **createDistributionWithTags20200531Request** | [**CreateDistributionWithTags20200531Request**](CreateDistributionWithTags20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDistributionWithTagsResult**](CreateDistributionWithTagsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createFieldLevelEncryptionConfig20200531

> CreateFieldLevelEncryptionConfigResult createFieldLevelEncryptionConfig20200531(createFieldLevelEncryptionConfig20200531Request, opts)



Create a new field-level encryption configuration.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createFieldLevelEncryptionConfig20200531Request = new AmazonCloudFront.CreateFieldLevelEncryptionConfig20200531Request(); // CreateFieldLevelEncryptionConfig20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFieldLevelEncryptionConfig20200531(createFieldLevelEncryptionConfig20200531Request, opts, (error, data, response) => {
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
 **createFieldLevelEncryptionConfig20200531Request** | [**CreateFieldLevelEncryptionConfig20200531Request**](CreateFieldLevelEncryptionConfig20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateFieldLevelEncryptionConfigResult**](CreateFieldLevelEncryptionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createFieldLevelEncryptionProfile20200531

> CreateFieldLevelEncryptionProfileResult createFieldLevelEncryptionProfile20200531(createFieldLevelEncryptionProfile20200531Request, opts)



Create a field-level encryption profile.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createFieldLevelEncryptionProfile20200531Request = new AmazonCloudFront.CreateFieldLevelEncryptionProfile20200531Request(); // CreateFieldLevelEncryptionProfile20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFieldLevelEncryptionProfile20200531(createFieldLevelEncryptionProfile20200531Request, opts, (error, data, response) => {
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
 **createFieldLevelEncryptionProfile20200531Request** | [**CreateFieldLevelEncryptionProfile20200531Request**](CreateFieldLevelEncryptionProfile20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateFieldLevelEncryptionProfileResult**](CreateFieldLevelEncryptionProfileResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createFunction20200531

> CreateFunctionResult createFunction20200531(createFunction20200531Request, opts)



&lt;p&gt;Creates a CloudFront function.&lt;/p&gt; &lt;p&gt;To create a function, you provide the function code and some configuration information about the function. The response contains an Amazon Resource Name (ARN) that uniquely identifies the function.&lt;/p&gt; &lt;p&gt;When you create a function, it&#39;s in the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage. In this stage, you can test the function with &lt;code&gt;TestFunction&lt;/code&gt;, and update it with &lt;code&gt;UpdateFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When you&#39;re ready to use your function with a CloudFront distribution, use &lt;code&gt;PublishFunction&lt;/code&gt; to copy the function from the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage to &lt;code&gt;LIVE&lt;/code&gt;. When it&#39;s live, you can attach the function to a distribution&#39;s cache behavior, using the function&#39;s ARN.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createFunction20200531Request = new AmazonCloudFront.CreateFunction20200531Request(); // CreateFunction20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFunction20200531(createFunction20200531Request, opts, (error, data, response) => {
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
 **createFunction20200531Request** | [**CreateFunction20200531Request**](CreateFunction20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateFunctionResult**](CreateFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createInvalidation20200531

> CreateInvalidationResult createInvalidation20200531(distributionId, createInvalidation20200531Request, opts)



Create a new invalidation.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let distributionId = "distributionId_example"; // String | The distribution's id.
let createInvalidation20200531Request = new AmazonCloudFront.CreateInvalidation20200531Request(); // CreateInvalidation20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createInvalidation20200531(distributionId, createInvalidation20200531Request, opts, (error, data, response) => {
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
 **distributionId** | **String**| The distribution&#39;s id. | 
 **createInvalidation20200531Request** | [**CreateInvalidation20200531Request**](CreateInvalidation20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateInvalidationResult**](CreateInvalidationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createKeyGroup20200531

> CreateKeyGroupResult createKeyGroup20200531(createKeyGroup20200531Request, opts)



&lt;p&gt;Creates a key group that you can use with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;CloudFront signed URLs and signed cookies&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To create a key group, you must specify at least one public key for the key group. After you create a key group, you can reference it from one or more cache behaviors. When you reference a key group in a cache behavior, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving private content&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createKeyGroup20200531Request = new AmazonCloudFront.CreateKeyGroup20200531Request(); // CreateKeyGroup20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createKeyGroup20200531(createKeyGroup20200531Request, opts, (error, data, response) => {
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
 **createKeyGroup20200531Request** | [**CreateKeyGroup20200531Request**](CreateKeyGroup20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateKeyGroupResult**](CreateKeyGroupResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createMonitoringSubscription20200531

> CreateMonitoringSubscriptionResult createMonitoringSubscription20200531(distributionId, createMonitoringSubscription20200531Request, opts)



&lt;p&gt;Enables additional CloudWatch metrics for the specified CloudFront distribution. The additional metrics incur an additional cost.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html#monitoring-console.distributions-additional\&quot;&gt;Viewing additional CloudFront distribution metrics&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let distributionId = "distributionId_example"; // String | The ID of the distribution that you are enabling metrics for.
let createMonitoringSubscription20200531Request = new AmazonCloudFront.CreateMonitoringSubscription20200531Request(); // CreateMonitoringSubscription20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMonitoringSubscription20200531(distributionId, createMonitoringSubscription20200531Request, opts, (error, data, response) => {
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
 **distributionId** | **String**| The ID of the distribution that you are enabling metrics for. | 
 **createMonitoringSubscription20200531Request** | [**CreateMonitoringSubscription20200531Request**](CreateMonitoringSubscription20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMonitoringSubscriptionResult**](CreateMonitoringSubscriptionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createOriginAccessControl20200531

> CreateOriginAccessControlResult createOriginAccessControl20200531(createOriginAccessControl20200531Request, opts)



&lt;p&gt;Creates a new origin access control in CloudFront. After you create an origin access control, you can add it to an origin in a CloudFront distribution so that CloudFront sends authenticated (signed) requests to the origin.&lt;/p&gt; &lt;p&gt;This makes it possible to block public access to the origin, allowing viewers (users) to access the origin&#39;s content only through CloudFront.&lt;/p&gt; &lt;p&gt;For more information about using a CloudFront origin access control, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html\&quot;&gt;Restricting access to an Amazon Web Services origin&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createOriginAccessControl20200531Request = new AmazonCloudFront.CreateOriginAccessControl20200531Request(); // CreateOriginAccessControl20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createOriginAccessControl20200531(createOriginAccessControl20200531Request, opts, (error, data, response) => {
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
 **createOriginAccessControl20200531Request** | [**CreateOriginAccessControl20200531Request**](CreateOriginAccessControl20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateOriginAccessControlResult**](CreateOriginAccessControlResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createOriginRequestPolicy20200531

> CreateOriginRequestPolicyResult createOriginRequestPolicy20200531(createOriginRequestPolicy20200531Request, opts)



&lt;p&gt;Creates an origin request policy.&lt;/p&gt; &lt;p&gt;After you create an origin request policy, you can attach it to one or more cache behaviors. When it&#39;s attached to a cache behavior, the origin request policy determines the values that CloudFront includes in requests that it sends to the origin. Each request that CloudFront sends to the origin includes the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The request body and the URL path (without the domain name) from the viewer request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The headers that CloudFront automatically includes in every origin request, including &lt;code&gt;Host&lt;/code&gt;, &lt;code&gt;User-Agent&lt;/code&gt;, and &lt;code&gt;X-Amz-Cf-Id&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All HTTP headers, cookies, and URL query strings that are specified in the cache policy or the origin request policy. These can include items from the viewer request and, in the case of headers, additional ones that are added by CloudFront.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;CloudFront sends a request when it can&#39;t find a valid object in its cache that matches the request. If you want to send values to the origin and also include them in the cache key, use &lt;code&gt;CachePolicy&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about origin request policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html\&quot;&gt;Controlling origin requests&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createOriginRequestPolicy20200531Request = new AmazonCloudFront.CreateOriginRequestPolicy20200531Request(); // CreateOriginRequestPolicy20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createOriginRequestPolicy20200531(createOriginRequestPolicy20200531Request, opts, (error, data, response) => {
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
 **createOriginRequestPolicy20200531Request** | [**CreateOriginRequestPolicy20200531Request**](CreateOriginRequestPolicy20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateOriginRequestPolicyResult**](CreateOriginRequestPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createPublicKey20200531

> CreatePublicKeyResult createPublicKey20200531(createPublicKey20200531Request, opts)



Uploads a public key to CloudFront that you can use with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;signed URLs and signed cookies&lt;/a&gt;, or with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html\&quot;&gt;field-level encryption&lt;/a&gt;.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createPublicKey20200531Request = new AmazonCloudFront.CreatePublicKey20200531Request(); // CreatePublicKey20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPublicKey20200531(createPublicKey20200531Request, opts, (error, data, response) => {
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
 **createPublicKey20200531Request** | [**CreatePublicKey20200531Request**](CreatePublicKey20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePublicKeyResult**](CreatePublicKeyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createRealtimeLogConfig20200531

> CreateRealtimeLogConfigResult createRealtimeLogConfig20200531(createRealtimeLogConfig20200531Request, opts)



&lt;p&gt;Creates a real-time log configuration.&lt;/p&gt; &lt;p&gt;After you create a real-time log configuration, you can attach it to one or more cache behaviors to send real-time log data to the specified Amazon Kinesis data stream.&lt;/p&gt; &lt;p&gt;For more information about real-time log configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html\&quot;&gt;Real-time logs&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createRealtimeLogConfig20200531Request = new AmazonCloudFront.CreateRealtimeLogConfig20200531Request(); // CreateRealtimeLogConfig20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRealtimeLogConfig20200531(createRealtimeLogConfig20200531Request, opts, (error, data, response) => {
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
 **createRealtimeLogConfig20200531Request** | [**CreateRealtimeLogConfig20200531Request**](CreateRealtimeLogConfig20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRealtimeLogConfigResult**](CreateRealtimeLogConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createResponseHeadersPolicy20200531

> CreateResponseHeadersPolicyResult createResponseHeadersPolicy20200531(createResponseHeadersPolicy20200531Request, opts)



&lt;p&gt;Creates a response headers policy.&lt;/p&gt; &lt;p&gt;A response headers policy contains information about a set of HTTP headers. To create a response headers policy, you provide some metadata about the policy and a set of configurations that specify the headers.&lt;/p&gt; &lt;p&gt;After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it&#39;s attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html\&quot;&gt;Adding or removing HTTP headers in CloudFront responses&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createResponseHeadersPolicy20200531Request = new AmazonCloudFront.CreateResponseHeadersPolicy20200531Request(); // CreateResponseHeadersPolicy20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createResponseHeadersPolicy20200531(createResponseHeadersPolicy20200531Request, opts, (error, data, response) => {
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
 **createResponseHeadersPolicy20200531Request** | [**CreateResponseHeadersPolicy20200531Request**](CreateResponseHeadersPolicy20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateResponseHeadersPolicyResult**](CreateResponseHeadersPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createStreamingDistribution20200531

> CreateStreamingDistributionResult createStreamingDistribution20200531(createStreamingDistribution20200531Request, opts)



This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/ann.jspa?annID&#x3D;7356\&quot;&gt;read the announcement&lt;/a&gt; on the Amazon CloudFront discussion forum.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let createStreamingDistribution20200531Request = new AmazonCloudFront.CreateStreamingDistribution20200531Request(); // CreateStreamingDistribution20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStreamingDistribution20200531(createStreamingDistribution20200531Request, opts, (error, data, response) => {
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
 **createStreamingDistribution20200531Request** | [**CreateStreamingDistribution20200531Request**](CreateStreamingDistribution20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateStreamingDistributionResult**](CreateStreamingDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## createStreamingDistributionWithTags20200531

> CreateStreamingDistributionWithTagsResult createStreamingDistributionWithTags20200531(withTags, createStreamingDistributionWithTags20200531Request, opts)



This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/ann.jspa?annID&#x3D;7356\&quot;&gt;read the announcement&lt;/a&gt; on the Amazon CloudFront discussion forum.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let withTags = true; // Boolean | 
let createStreamingDistributionWithTags20200531Request = new AmazonCloudFront.CreateStreamingDistributionWithTags20200531Request(); // CreateStreamingDistributionWithTags20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStreamingDistributionWithTags20200531(withTags, createStreamingDistributionWithTags20200531Request, opts, (error, data, response) => {
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
 **withTags** | **Boolean**|  | 
 **createStreamingDistributionWithTags20200531Request** | [**CreateStreamingDistributionWithTags20200531Request**](CreateStreamingDistributionWithTags20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateStreamingDistributionWithTagsResult**](CreateStreamingDistributionWithTagsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## deleteCachePolicy20200531

> deleteCachePolicy20200531(id, opts)



&lt;p&gt;Deletes a cache policy.&lt;/p&gt; &lt;p&gt;You cannot delete a cache policy if it&#39;s attached to a cache behavior. First update your distributions to remove the cache policy from all cache behaviors, then delete the cache policy.&lt;/p&gt; &lt;p&gt;To delete a cache policy, you must provide the policy&#39;s identifier and version. To get these values, you can use &lt;code&gt;ListCachePolicies&lt;/code&gt; or &lt;code&gt;GetCachePolicy&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier for the cache policy that you are deleting. To get the identifier, you can use <code>ListCachePolicies</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The version of the cache policy that you are deleting. The version is the cache policy's <code>ETag</code> value, which you can get using <code>ListCachePolicies</code>, <code>GetCachePolicy</code>, or <code>GetCachePolicyConfig</code>.
};
apiInstance.deleteCachePolicy20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the cache policy that you are deleting. To get the identifier, you can use &lt;code&gt;ListCachePolicies&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The version of the cache policy that you are deleting. The version is the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListCachePolicies&lt;/code&gt;, &lt;code&gt;GetCachePolicy&lt;/code&gt;, or &lt;code&gt;GetCachePolicyConfig&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteCloudFrontOriginAccessIdentity20200531

> deleteCloudFrontOriginAccessIdentity20200531(id, opts)



Delete an origin access identity.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The origin access identity's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header you received from a previous <code>GET</code> or <code>PUT</code> request. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.deleteCloudFrontOriginAccessIdentity20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The origin access identity&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header you received from a previous &lt;code&gt;GET&lt;/code&gt; or &lt;code&gt;PUT&lt;/code&gt; request. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteContinuousDeploymentPolicy20200531

> deleteContinuousDeploymentPolicy20200531(id, opts)



&lt;p&gt;Deletes a continuous deployment policy.&lt;/p&gt; &lt;p&gt;You cannot delete a continuous deployment policy that&#39;s attached to a primary distribution. First update your distribution to remove the continuous deployment policy, then you can delete the policy.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the continuous deployment policy that you are deleting.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The current version (<code>ETag</code> value) of the continuous deployment policy that you are deleting.
};
apiInstance.deleteContinuousDeploymentPolicy20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the continuous deployment policy that you are deleting. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the continuous deployment policy that you are deleting. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteDistribution20200531

> deleteDistribution20200531(id, opts)



Delete a distribution.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The distribution ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when you disabled the distribution. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.deleteDistribution20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The distribution ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when you disabled the distribution. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteFieldLevelEncryptionConfig20200531

> deleteFieldLevelEncryptionConfig20200531(id, opts)



Remove a field-level encryption configuration.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The ID of the configuration you want to delete from CloudFront.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the configuration identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.deleteFieldLevelEncryptionConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the configuration you want to delete from CloudFront. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the configuration identity to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteFieldLevelEncryptionProfile20200531

> deleteFieldLevelEncryptionProfile20200531(id, opts)



Remove a field-level encryption profile.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | Request the ID of the profile you want to delete from CloudFront.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the profile to delete. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.deleteFieldLevelEncryptionProfile20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| Request the ID of the profile you want to delete from CloudFront. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the profile to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteFunction20200531

> deleteFunction20200531(name, ifMatch, opts)



&lt;p&gt;Deletes a CloudFront function.&lt;/p&gt; &lt;p&gt;You cannot delete a function if it&#39;s associated with a cache behavior. First, update your distributions to remove the function association from all cache behaviors, then delete the function.&lt;/p&gt; &lt;p&gt;To delete a function, you must provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value). To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let name = "name_example"; // String | The name of the function that you are deleting.
let ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the function that you are deleting, which you can get using <code>DescribeFunction</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteFunction20200531(name, ifMatch, opts, (error, data, response) => {
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
 **name** | **String**| The name of the function that you are deleting. | 
 **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are deleting, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;. | 
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
- **Accept**: text/xml


## deleteKeyGroup20200531

> deleteKeyGroup20200531(id, opts)



&lt;p&gt;Deletes a key group.&lt;/p&gt; &lt;p&gt;You cannot delete a key group that is referenced in a cache behavior. First update your distributions to remove the key group from all cache behaviors, then delete the key group.&lt;/p&gt; &lt;p&gt;To delete a key group, you must provide the key group&#39;s identifier and version. To get these values, use &lt;code&gt;ListKeyGroups&lt;/code&gt; followed by &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the key group that you are deleting. To get the identifier, use <code>ListKeyGroups</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The version of the key group that you are deleting. The version is the key group's <code>ETag</code> value. To get the <code>ETag</code>, use <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.
};
apiInstance.deleteKeyGroup20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the key group that you are deleting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The version of the key group that you are deleting. The version is the key group&#39;s &lt;code&gt;ETag&lt;/code&gt; value. To get the &lt;code&gt;ETag&lt;/code&gt;, use &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteMonitoringSubscription20200531

> Object deleteMonitoringSubscription20200531(distributionId, opts)



Disables additional CloudWatch metrics for the specified CloudFront distribution.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let distributionId = "distributionId_example"; // String | The ID of the distribution that you are disabling metrics for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMonitoringSubscription20200531(distributionId, opts, (error, data, response) => {
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
 **distributionId** | **String**| The ID of the distribution that you are disabling metrics for. | 
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


## deleteOriginAccessControl20200531

> deleteOriginAccessControl20200531(id, opts)



&lt;p&gt;Deletes a CloudFront origin access control.&lt;/p&gt; &lt;p&gt;You cannot delete an origin access control if it&#39;s in use. First, update all distributions to remove the origin access control from all origins, then delete the origin access control.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier of the origin access control that you are deleting.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The current version (<code>ETag</code> value) of the origin access control that you are deleting.
};
apiInstance.deleteOriginAccessControl20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the origin access control that you are deleting. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the origin access control that you are deleting. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteOriginRequestPolicy20200531

> deleteOriginRequestPolicy20200531(id, opts)



&lt;p&gt;Deletes an origin request policy.&lt;/p&gt; &lt;p&gt;You cannot delete an origin request policy if it&#39;s attached to any cache behaviors. First update your distributions to remove the origin request policy from all cache behaviors, then delete the origin request policy.&lt;/p&gt; &lt;p&gt;To delete an origin request policy, you must provide the policy&#39;s identifier and version. To get the identifier, you can use &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt; or &lt;code&gt;GetOriginRequestPolicy&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use <code>ListOriginRequestPolicies</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The version of the origin request policy that you are deleting. The version is the origin request policy's <code>ETag</code> value, which you can get using <code>ListOriginRequestPolicies</code>, <code>GetOriginRequestPolicy</code>, or <code>GetOriginRequestPolicyConfig</code>.
};
apiInstance.deleteOriginRequestPolicy20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The version of the origin request policy that you are deleting. The version is the origin request policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;, &lt;code&gt;GetOriginRequestPolicy&lt;/code&gt;, or &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deletePublicKey20200531

> deletePublicKey20200531(id, opts)



Remove a public key you previously added to CloudFront.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The ID of the public key you want to remove from CloudFront.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the public key identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.deletePublicKey20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the public key you want to remove from CloudFront. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the public key identity to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteRealtimeLogConfig20200531

> deleteRealtimeLogConfig20200531(deleteRealtimeLogConfig20200531Request, opts)



&lt;p&gt;Deletes a real-time log configuration.&lt;/p&gt; &lt;p&gt;You cannot delete a real-time log configuration if it&#39;s attached to a cache behavior. First update your distributions to remove the real-time log configuration from all cache behaviors, then delete the real-time log configuration.&lt;/p&gt; &lt;p&gt;To delete a real-time log configuration, you can provide the configuration&#39;s name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to delete.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let deleteRealtimeLogConfig20200531Request = new AmazonCloudFront.DeleteRealtimeLogConfig20200531Request(); // DeleteRealtimeLogConfig20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRealtimeLogConfig20200531(deleteRealtimeLogConfig20200531Request, opts, (error, data, response) => {
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
 **deleteRealtimeLogConfig20200531Request** | [**DeleteRealtimeLogConfig20200531Request**](DeleteRealtimeLogConfig20200531Request.md)|  | 
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
- **Accept**: text/xml


## deleteResponseHeadersPolicy20200531

> deleteResponseHeadersPolicy20200531(id, opts)



&lt;p&gt;Deletes a response headers policy.&lt;/p&gt; &lt;p&gt;You cannot delete a response headers policy if it&#39;s attached to a cache behavior. First update your distributions to remove the response headers policy from all cache behaviors, then delete the response headers policy.&lt;/p&gt; &lt;p&gt;To delete a response headers policy, you must provide the policy&#39;s identifier and version. To get these values, you can use &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt; or &lt;code&gt;GetResponseHeadersPolicy&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | <p>The identifier for the response headers policy that you are deleting.</p> <p>To get the identifier, you can use <code>ListResponseHeadersPolicies</code>.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | <p>The version of the response headers policy that you are deleting.</p> <p>The version is the response headers policy's <code>ETag</code> value, which you can get using <code>ListResponseHeadersPolicies</code>, <code>GetResponseHeadersPolicy</code>, or <code>GetResponseHeadersPolicyConfig</code>.</p>
};
apiInstance.deleteResponseHeadersPolicy20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| &lt;p&gt;The identifier for the response headers policy that you are deleting.&lt;/p&gt; &lt;p&gt;To get the identifier, you can use &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| &lt;p&gt;The version of the response headers policy that you are deleting.&lt;/p&gt; &lt;p&gt;The version is the response headers policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;, &lt;code&gt;GetResponseHeadersPolicy&lt;/code&gt;, or &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt;.&lt;/p&gt; | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteStreamingDistribution20200531

> deleteStreamingDistribution20200531(id, opts)



&lt;p&gt;Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To delete an RTMP distribution using the CloudFront API&lt;/b&gt;:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Disable the RTMP distribution.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to get the current configuration and the &lt;code&gt;Etag&lt;/code&gt; header for the distribution. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to change the value of &lt;code&gt;Enabled&lt;/code&gt; to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to confirm that the distribution was successfully disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request. Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to your &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request to confirm that the distribution was successfully deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For information about deleting a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html\&quot;&gt;Deleting a Distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The distribution ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when you disabled the streaming distribution. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.deleteStreamingDistribution20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The distribution ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when you disabled the streaming distribution. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## describeFunction20200531

> DescribeFunctionResult describeFunction20200531(name, opts)



&lt;p&gt;Gets configuration information and metadata about a CloudFront function, but not the function&#39;s code. To get a function&#39;s code, use &lt;code&gt;GetFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get configuration information and metadata about a function, you must provide the function&#39;s name and stage. To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let name = "name_example"; // String | The name of the function that you are getting information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'stage': "stage_example" // String | The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.
};
apiInstance.describeFunction20200531(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the function that you are getting information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **stage** | **String**| The function&#39;s stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;. | [optional] 

### Return type

[**DescribeFunctionResult**](DescribeFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getCachePolicy20200531

> GetCachePolicyResult getCachePolicy20200531(id, opts)



&lt;p&gt;Gets a cache policy, including the following metadata:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The policy&#39;s identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The date and time when the policy was last modified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To get a cache policy, you must provide the policy&#39;s identifier. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCachePolicy20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the cache policy. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCachePolicyResult**](GetCachePolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getCachePolicyConfig20200531

> GetCachePolicyConfigResult getCachePolicyConfig20200531(id, opts)



&lt;p&gt;Gets a cache policy configuration.&lt;/p&gt; &lt;p&gt;To get a cache policy configuration, you must provide the policy&#39;s identifier. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCachePolicyConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the cache policy. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCachePolicyConfigResult**](GetCachePolicyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getCloudFrontOriginAccessIdentity20200531

> GetCloudFrontOriginAccessIdentityResult getCloudFrontOriginAccessIdentity20200531(id, opts)



Get the information about an origin access identity.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identity's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCloudFrontOriginAccessIdentity20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identity&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCloudFrontOriginAccessIdentityResult**](GetCloudFrontOriginAccessIdentityResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getCloudFrontOriginAccessIdentityConfig20200531

> GetCloudFrontOriginAccessIdentityConfigResult getCloudFrontOriginAccessIdentityConfig20200531(id, opts)



Get the configuration information about an origin access identity.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identity's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCloudFrontOriginAccessIdentityConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identity&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCloudFrontOriginAccessIdentityConfigResult**](GetCloudFrontOriginAccessIdentityConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getContinuousDeploymentPolicy20200531

> GetContinuousDeploymentPolicyResult getContinuousDeploymentPolicy20200531(id, opts)



Gets a continuous deployment policy, including metadata (the policy&#39;s identifier and the date and time when the policy was last modified).

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the continuous deployment policy that you are getting.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContinuousDeploymentPolicy20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the continuous deployment policy that you are getting. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContinuousDeploymentPolicyResult**](GetContinuousDeploymentPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getContinuousDeploymentPolicyConfig20200531

> GetContinuousDeploymentPolicyConfigResult getContinuousDeploymentPolicyConfig20200531(id, opts)



Gets configuration information about a continuous deployment policy.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the continuous deployment policy whose configuration you are getting.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContinuousDeploymentPolicyConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the continuous deployment policy whose configuration you are getting. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContinuousDeploymentPolicyConfigResult**](GetContinuousDeploymentPolicyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getDistribution20200531

> GetDistributionResult getDistribution20200531(id, opts)



Get the information about a distribution.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The distribution's ID. If the ID is empty, an empty distribution configuration is returned.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDistribution20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The distribution&#39;s ID. If the ID is empty, an empty distribution configuration is returned. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDistributionResult**](GetDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getDistributionConfig20200531

> GetDistributionConfigResult getDistributionConfig20200531(id, opts)



Get the configuration information about a distribution.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The distribution's ID. If the ID is empty, an empty distribution configuration is returned.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDistributionConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The distribution&#39;s ID. If the ID is empty, an empty distribution configuration is returned. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDistributionConfigResult**](GetDistributionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getFieldLevelEncryption20200531

> GetFieldLevelEncryptionResult getFieldLevelEncryption20200531(id, opts)



Get the field-level encryption configuration information.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | Request the ID for the field-level encryption configuration information.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFieldLevelEncryption20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| Request the ID for the field-level encryption configuration information. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFieldLevelEncryptionResult**](GetFieldLevelEncryptionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getFieldLevelEncryptionConfig20200531

> GetFieldLevelEncryptionConfigResult getFieldLevelEncryptionConfig20200531(id, opts)



Get the field-level encryption configuration information.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | Request the ID for the field-level encryption configuration information.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFieldLevelEncryptionConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| Request the ID for the field-level encryption configuration information. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFieldLevelEncryptionConfigResult**](GetFieldLevelEncryptionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getFieldLevelEncryptionProfile20200531

> GetFieldLevelEncryptionProfileResult getFieldLevelEncryptionProfile20200531(id, opts)



Get the field-level encryption profile information.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | Get the ID for the field-level encryption profile information.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFieldLevelEncryptionProfile20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| Get the ID for the field-level encryption profile information. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFieldLevelEncryptionProfileResult**](GetFieldLevelEncryptionProfileResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getFieldLevelEncryptionProfileConfig20200531

> GetFieldLevelEncryptionProfileConfigResult getFieldLevelEncryptionProfileConfig20200531(id, opts)



Get the field-level encryption profile configuration information.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | Get the ID for the field-level encryption profile configuration information.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFieldLevelEncryptionProfileConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| Get the ID for the field-level encryption profile configuration information. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFieldLevelEncryptionProfileConfigResult**](GetFieldLevelEncryptionProfileConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getFunction20200531

> GetFunctionResult getFunction20200531(name, opts)



&lt;p&gt;Gets the code of a CloudFront function. To get configuration information and metadata about a function, use &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get a function&#39;s code, you must provide the function&#39;s name and stage. To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let name = "name_example"; // String | The name of the function whose code you are getting.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'stage': "stage_example" // String | The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.
};
apiInstance.getFunction20200531(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the function whose code you are getting. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **stage** | **String**| The function&#39;s stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;. | [optional] 

### Return type

[**GetFunctionResult**](GetFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getInvalidation20200531

> GetInvalidationResult getInvalidation20200531(distributionId, id, opts)



Get the information about an invalidation.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let distributionId = "distributionId_example"; // String | The distribution's ID.
let id = "id_example"; // String | The identifier for the invalidation request, for example, <code>IDFDVBD632BHDS5</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getInvalidation20200531(distributionId, id, opts, (error, data, response) => {
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
 **distributionId** | **String**| The distribution&#39;s ID. | 
 **id** | **String**| The identifier for the invalidation request, for example, &lt;code&gt;IDFDVBD632BHDS5&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetInvalidationResult**](GetInvalidationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getKeyGroup20200531

> GetKeyGroupResult getKeyGroup20200531(id, opts)



&lt;p&gt;Gets a key group, including the date and time when the key group was last modified.&lt;/p&gt; &lt;p&gt;To get a key group, you must provide the key group&#39;s identifier. If the key group is referenced in a distribution&#39;s cache behavior, you can get the key group&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the key group is not referenced in a cache behavior, you can get the identifier using &lt;code&gt;ListKeyGroups&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the key group that you are getting. To get the identifier, use <code>ListKeyGroups</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getKeyGroup20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the key group that you are getting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetKeyGroupResult**](GetKeyGroupResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getKeyGroupConfig20200531

> GetKeyGroupConfigResult getKeyGroupConfig20200531(id, opts)



&lt;p&gt;Gets a key group configuration.&lt;/p&gt; &lt;p&gt;To get a key group configuration, you must provide the key group&#39;s identifier. If the key group is referenced in a distribution&#39;s cache behavior, you can get the key group&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the key group is not referenced in a cache behavior, you can get the identifier using &lt;code&gt;ListKeyGroups&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the key group whose configuration you are getting. To get the identifier, use <code>ListKeyGroups</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getKeyGroupConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the key group whose configuration you are getting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetKeyGroupConfigResult**](GetKeyGroupConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getMonitoringSubscription20200531

> GetMonitoringSubscriptionResult getMonitoringSubscription20200531(distributionId, opts)



Gets information about whether additional CloudWatch metrics are enabled for the specified CloudFront distribution.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let distributionId = "distributionId_example"; // String | The ID of the distribution that you are getting metrics information for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMonitoringSubscription20200531(distributionId, opts, (error, data, response) => {
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
 **distributionId** | **String**| The ID of the distribution that you are getting metrics information for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMonitoringSubscriptionResult**](GetMonitoringSubscriptionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getOriginAccessControl20200531

> GetOriginAccessControlResult getOriginAccessControl20200531(id, opts)



Gets a CloudFront origin access control, including its unique identifier.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier of the origin access control.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOriginAccessControl20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the origin access control. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOriginAccessControlResult**](GetOriginAccessControlResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getOriginAccessControlConfig20200531

> GetOriginAccessControlConfigResult getOriginAccessControlConfig20200531(id, opts)



Gets a CloudFront origin access control configuration.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier of the origin access control.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOriginAccessControlConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the origin access control. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOriginAccessControlConfigResult**](GetOriginAccessControlConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getOriginRequestPolicy20200531

> GetOriginRequestPolicyResult getOriginRequestPolicy20200531(id, opts)



&lt;p&gt;Gets an origin request policy, including the following metadata:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The policy&#39;s identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The date and time when the policy was last modified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To get an origin request policy, you must provide the policy&#39;s identifier. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOriginRequestPolicy20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the origin request policy. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOriginRequestPolicyResult**](GetOriginRequestPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getOriginRequestPolicyConfig20200531

> GetOriginRequestPolicyConfigResult getOriginRequestPolicyConfig20200531(id, opts)



&lt;p&gt;Gets an origin request policy configuration.&lt;/p&gt; &lt;p&gt;To get an origin request policy configuration, you must provide the policy&#39;s identifier. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOriginRequestPolicyConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the origin request policy. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOriginRequestPolicyConfigResult**](GetOriginRequestPolicyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getPublicKey20200531

> GetPublicKeyResult getPublicKey20200531(id, opts)



Gets a public key.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the public key you are getting.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPublicKey20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the public key you are getting. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPublicKeyResult**](GetPublicKeyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getPublicKeyConfig20200531

> GetPublicKeyConfigResult getPublicKeyConfig20200531(id, opts)



Gets a public key configuration.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the public key whose configuration you are getting.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPublicKeyConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the public key whose configuration you are getting. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPublicKeyConfigResult**](GetPublicKeyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getRealtimeLogConfig20200531

> GetRealtimeLogConfigResult getRealtimeLogConfig20200531(getRealtimeLogConfig20200531Request, opts)



&lt;p&gt;Gets a real-time log configuration.&lt;/p&gt; &lt;p&gt;To get a real-time log configuration, you can provide the configuration&#39;s name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to get.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let getRealtimeLogConfig20200531Request = new AmazonCloudFront.GetRealtimeLogConfig20200531Request(); // GetRealtimeLogConfig20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRealtimeLogConfig20200531(getRealtimeLogConfig20200531Request, opts, (error, data, response) => {
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
 **getRealtimeLogConfig20200531Request** | [**GetRealtimeLogConfig20200531Request**](GetRealtimeLogConfig20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRealtimeLogConfigResult**](GetRealtimeLogConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## getResponseHeadersPolicy20200531

> GetResponseHeadersPolicyResult getResponseHeadersPolicy20200531(id, opts)



&lt;p&gt;Gets a response headers policy, including metadata (the policy&#39;s identifier and the date and time when the policy was last modified).&lt;/p&gt; &lt;p&gt;To get a response headers policy, you must provide the policy&#39;s identifier. If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | <p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getResponseHeadersPolicy20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| &lt;p&gt;The identifier for the response headers policy.&lt;/p&gt; &lt;p&gt;If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetResponseHeadersPolicyResult**](GetResponseHeadersPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getResponseHeadersPolicyConfig20200531

> GetResponseHeadersPolicyConfigResult getResponseHeadersPolicyConfig20200531(id, opts)



&lt;p&gt;Gets a response headers policy configuration.&lt;/p&gt; &lt;p&gt;To get a response headers policy configuration, you must provide the policy&#39;s identifier. If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | <p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getResponseHeadersPolicyConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| &lt;p&gt;The identifier for the response headers policy.&lt;/p&gt; &lt;p&gt;If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetResponseHeadersPolicyConfigResult**](GetResponseHeadersPolicyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getStreamingDistribution20200531

> GetStreamingDistributionResult getStreamingDistribution20200531(id, opts)



Gets information about a specified RTMP distribution, including the distribution configuration.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The streaming distribution's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStreamingDistribution20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The streaming distribution&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStreamingDistributionResult**](GetStreamingDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getStreamingDistributionConfig20200531

> GetStreamingDistributionConfigResult getStreamingDistributionConfig20200531(id, opts)



Get the configuration information about a streaming distribution.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The streaming distribution's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStreamingDistributionConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The streaming distribution&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStreamingDistributionConfigResult**](GetStreamingDistributionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listCachePolicies20200531

> ListCachePoliciesResult listCachePolicies20200531(opts)



&lt;p&gt;Gets a list of cache policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'type': "type_example", // String | <p>A filter to return only the specified kinds of cache policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of cache policies that you want in the response.
};
apiInstance.listCachePolicies20200531(opts, (error, data, response) => {
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
 **type** | **String**| &lt;p&gt;A filter to return only the specified kinds of cache policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Returns only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Returns only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of cache policies that you want in the response. | [optional] 

### Return type

[**ListCachePoliciesResult**](ListCachePoliciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listCloudFrontOriginAccessIdentities20200531

> ListCloudFrontOriginAccessIdentitiesResult listCloudFrontOriginAccessIdentities20200531(opts)



Lists origin access identities.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page).
  'maxItems': "maxItems_example" // String | The maximum number of origin access identities you want in the response body.
};
apiInstance.listCloudFrontOriginAccessIdentities20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last identity on that page). | [optional] 
 **maxItems** | **String**| The maximum number of origin access identities you want in the response body. | [optional] 

### Return type

[**ListCloudFrontOriginAccessIdentitiesResult**](ListCloudFrontOriginAccessIdentitiesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listConflictingAliases20200531

> ListConflictingAliasesResult listConflictingAliases20200531(distributionId, alias, opts)



&lt;p&gt;Gets a list of aliases (also called CNAMEs or alternate domain names) that conflict or overlap with the provided alias, and the associated CloudFront distributions and Amazon Web Services accounts for each conflicting alias. In the returned list, the distribution and account IDs are partially hidden, which allows you to identify the distributions and accounts that you own, but helps to protect the information of ones that you don&#39;t own.&lt;/p&gt; &lt;p&gt;Use this operation to find aliases that are in use in CloudFront that conflict or overlap with the provided alias. For example, if you provide &lt;code&gt;www.example.com&lt;/code&gt; as input, the returned list can include &lt;code&gt;www.example.com&lt;/code&gt; and the overlapping wildcard alternate domain name (&lt;code&gt;*.example.com&lt;/code&gt;), if they exist. If you provide &lt;code&gt;*.example.com&lt;/code&gt; as input, the returned list can include &lt;code&gt;*.example.com&lt;/code&gt; and any alternate domain names covered by that wildcard (for example, &lt;code&gt;www.example.com&lt;/code&gt;, &lt;code&gt;test.example.com&lt;/code&gt;, &lt;code&gt;dev.example.com&lt;/code&gt;, and so on), if they exist.&lt;/p&gt; &lt;p&gt;To list conflicting aliases, you provide the alias to search and the ID of a distribution in your account that has an attached SSL/TLS certificate that includes the provided alias. For more information, including how to set up the distribution and certificate, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\&quot;&gt;Moving an alternate domain name to a different distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let distributionId = "distributionId_example"; // String | The ID of a distribution in your account that has an attached SSL/TLS certificate that includes the provided alias.
let alias = "alias_example"; // String | The alias (also called a CNAME) to search for conflicting aliases.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': 56 // Number | The maximum number of conflicting aliases that you want in the response.
};
apiInstance.listConflictingAliases20200531(distributionId, alias, opts, (error, data, response) => {
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
 **distributionId** | **String**| The ID of a distribution in your account that has an attached SSL/TLS certificate that includes the provided alias. | 
 **alias** | **String**| The alias (also called a CNAME) to search for conflicting aliases. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **Number**| The maximum number of conflicting aliases that you want in the response. | [optional] 

### Return type

[**ListConflictingAliasesResult**](ListConflictingAliasesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listContinuousDeploymentPolicies20200531

> ListContinuousDeploymentPoliciesResult listContinuousDeploymentPolicies20200531(opts)



&lt;p&gt;Gets a list of the continuous deployment policies in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of continuous deployment policies that you want returned in the response.
};
apiInstance.listContinuousDeploymentPolicies20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of continuous deployment policies that you want returned in the response. | [optional] 

### Return type

[**ListContinuousDeploymentPoliciesResult**](ListContinuousDeploymentPoliciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listDistributions20200531

> ListDistributionsResult listDistributions20200531(opts)



List CloudFront distributions.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last distribution on that page).
  'maxItems': "maxItems_example" // String | The maximum number of distributions you want in the response body.
};
apiInstance.listDistributions20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last distribution on that page). | [optional] 
 **maxItems** | **String**| The maximum number of distributions you want in the response body. | [optional] 

### Return type

[**ListDistributionsResult**](ListDistributionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listDistributionsByCachePolicyId20200531

> ListDistributionsByCachePolicyIdResult listDistributionsByCachePolicyId20200531(cachePolicyId, opts)



&lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified cache policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let cachePolicyId = "cachePolicyId_example"; // String | The ID of the cache policy whose associated distribution IDs you want to list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of distribution IDs that you want in the response.
};
apiInstance.listDistributionsByCachePolicyId20200531(cachePolicyId, opts, (error, data, response) => {
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
 **cachePolicyId** | **String**| The ID of the cache policy whose associated distribution IDs you want to list. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of distribution IDs that you want in the response. | [optional] 

### Return type

[**ListDistributionsByCachePolicyIdResult**](ListDistributionsByCachePolicyIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listDistributionsByKeyGroup20200531

> ListDistributionsByKeyGroupResult listDistributionsByKeyGroup20200531(keyGroupId, opts)



&lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that references the specified key group.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let keyGroupId = "keyGroupId_example"; // String | The ID of the key group whose associated distribution IDs you are listing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of distribution IDs that you want in the response.
};
apiInstance.listDistributionsByKeyGroup20200531(keyGroupId, opts, (error, data, response) => {
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
 **keyGroupId** | **String**| The ID of the key group whose associated distribution IDs you are listing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of distribution IDs that you want in the response. | [optional] 

### Return type

[**ListDistributionsByKeyGroupResult**](ListDistributionsByKeyGroupResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listDistributionsByOriginRequestPolicyId20200531

> ListDistributionsByOriginRequestPolicyIdResult listDistributionsByOriginRequestPolicyId20200531(originRequestPolicyId, opts)



&lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified origin request policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let originRequestPolicyId = "originRequestPolicyId_example"; // String | The ID of the origin request policy whose associated distribution IDs you want to list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of distribution IDs that you want in the response.
};
apiInstance.listDistributionsByOriginRequestPolicyId20200531(originRequestPolicyId, opts, (error, data, response) => {
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
 **originRequestPolicyId** | **String**| The ID of the origin request policy whose associated distribution IDs you want to list. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of distribution IDs that you want in the response. | [optional] 

### Return type

[**ListDistributionsByOriginRequestPolicyIdResult**](ListDistributionsByOriginRequestPolicyIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listDistributionsByRealtimeLogConfig20200531

> ListDistributionsByRealtimeLogConfigResult listDistributionsByRealtimeLogConfig20200531(listDistributionsByRealtimeLogConfig20200531Request, opts)



&lt;p&gt;Gets a list of distributions that have a cache behavior that&#39;s associated with the specified real-time log configuration.&lt;/p&gt; &lt;p&gt;You can specify the real-time log configuration by its name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to list distributions for.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let listDistributionsByRealtimeLogConfig20200531Request = new AmazonCloudFront.ListDistributionsByRealtimeLogConfig20200531Request(); // ListDistributionsByRealtimeLogConfig20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listDistributionsByRealtimeLogConfig20200531(listDistributionsByRealtimeLogConfig20200531Request, opts, (error, data, response) => {
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
 **listDistributionsByRealtimeLogConfig20200531Request** | [**ListDistributionsByRealtimeLogConfig20200531Request**](ListDistributionsByRealtimeLogConfig20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListDistributionsByRealtimeLogConfigResult**](ListDistributionsByRealtimeLogConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## listDistributionsByResponseHeadersPolicyId20200531

> ListDistributionsByResponseHeadersPolicyIdResult listDistributionsByResponseHeadersPolicyId20200531(responseHeadersPolicyId, opts)



&lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified response headers policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let responseHeadersPolicyId = "responseHeadersPolicyId_example"; // String | The ID of the response headers policy whose associated distribution IDs you want to list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of distribution IDs that you want to get in the response.
};
apiInstance.listDistributionsByResponseHeadersPolicyId20200531(responseHeadersPolicyId, opts, (error, data, response) => {
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
 **responseHeadersPolicyId** | **String**| The ID of the response headers policy whose associated distribution IDs you want to list. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of distribution IDs that you want to get in the response. | [optional] 

### Return type

[**ListDistributionsByResponseHeadersPolicyIdResult**](ListDistributionsByResponseHeadersPolicyIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listDistributionsByWebACLId20200531

> ListDistributionsByWebACLIdResult listDistributionsByWebACLId20200531(webACLId, opts)



List the distributions that are associated with a specified WAF web ACL.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let webACLId = "webACLId_example"; // String | The ID of the WAF web ACL that you want to list the associated distributions. If you specify \"null\" for the ID, the request returns a list of the distributions that aren't associated with a web ACL.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use <code>Marker</code> and <code>MaxItems</code> to control pagination of results. If you have more than <code>MaxItems</code> distributions that satisfy the request, the response includes a <code>NextMarker</code> element. To get the next page of results, submit another request. For the value of <code>Marker</code>, specify the value of <code>NextMarker</code> from the last response. (For the first request, omit <code>Marker</code>.)
  'maxItems': "maxItems_example" // String | The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.
};
apiInstance.listDistributionsByWebACLId20200531(webACLId, opts, (error, data, response) => {
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
 **webACLId** | **String**| The ID of the WAF web ACL that you want to list the associated distributions. If you specify \&quot;null\&quot; for the ID, the request returns a list of the distributions that aren&#39;t associated with a web ACL. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Use &lt;code&gt;Marker&lt;/code&gt; and &lt;code&gt;MaxItems&lt;/code&gt; to control pagination of results. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; distributions that satisfy the request, the response includes a &lt;code&gt;NextMarker&lt;/code&gt; element. To get the next page of results, submit another request. For the value of &lt;code&gt;Marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the last response. (For the first request, omit &lt;code&gt;Marker&lt;/code&gt;.) | [optional] 
 **maxItems** | **String**| The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100. | [optional] 

### Return type

[**ListDistributionsByWebACLIdResult**](ListDistributionsByWebACLIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listFieldLevelEncryptionConfigs20200531

> ListFieldLevelEncryptionConfigsResult listFieldLevelEncryptionConfigs20200531(opts)



List all field-level encryption configurations that have been created in CloudFront for this account.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last configuration on that page).
  'maxItems': "maxItems_example" // String | The maximum number of field-level encryption configurations you want in the response body.
};
apiInstance.listFieldLevelEncryptionConfigs20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last configuration on that page). | [optional] 
 **maxItems** | **String**| The maximum number of field-level encryption configurations you want in the response body. | [optional] 

### Return type

[**ListFieldLevelEncryptionConfigsResult**](ListFieldLevelEncryptionConfigsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listFieldLevelEncryptionProfiles20200531

> ListFieldLevelEncryptionProfilesResult listFieldLevelEncryptionProfiles20200531(opts)



Request a list of field-level encryption profiles that have been created in CloudFront for this account.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last profile on that page).
  'maxItems': "maxItems_example" // String | The maximum number of field-level encryption profiles you want in the response body. 
};
apiInstance.listFieldLevelEncryptionProfiles20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last profile on that page). | [optional] 
 **maxItems** | **String**| The maximum number of field-level encryption profiles you want in the response body.  | [optional] 

### Return type

[**ListFieldLevelEncryptionProfilesResult**](ListFieldLevelEncryptionProfilesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listFunctions20200531

> ListFunctionsResult listFunctions20200531(opts)



&lt;p&gt;Gets a list of all CloudFront functions in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the functions that are in the specified stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example", // String | The maximum number of functions that you want in the response.
  'stage': "stage_example" // String | An optional filter to return only the functions that are in the specified stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.
};
apiInstance.listFunctions20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of functions that you want in the response. | [optional] 
 **stage** | **String**| An optional filter to return only the functions that are in the specified stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;. | [optional] 

### Return type

[**ListFunctionsResult**](ListFunctionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listInvalidations20200531

> ListInvalidationsResult listInvalidations20200531(distributionId, opts)



Lists invalidation batches.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let distributionId = "distributionId_example"; // String | The distribution's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.
  'maxItems': "maxItems_example" // String | The maximum number of invalidation batches that you want in the response body.
};
apiInstance.listInvalidations20200531(distributionId, opts, (error, data, response) => {
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
 **distributionId** | **String**| The distribution&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. This value is the same as the ID of the last invalidation batch on that page. | [optional] 
 **maxItems** | **String**| The maximum number of invalidation batches that you want in the response body. | [optional] 

### Return type

[**ListInvalidationsResult**](ListInvalidationsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listKeyGroups20200531

> ListKeyGroupsResult listKeyGroups20200531(opts)



&lt;p&gt;Gets a list of key groups.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of key groups. The response includes key groups in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of key groups that you want in the response.
};
apiInstance.listKeyGroups20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of key groups. The response includes key groups in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of key groups that you want in the response. | [optional] 

### Return type

[**ListKeyGroupsResult**](ListKeyGroupsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listOriginAccessControls20200531

> ListOriginAccessControlsResult listOriginAccessControls20200531(opts)



&lt;p&gt;Gets the list of CloudFront origin access controls in this Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send another request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the next request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of origin access controls that you want in the response.
};
apiInstance.listOriginAccessControls20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of origin access controls that you want in the response. | [optional] 

### Return type

[**ListOriginAccessControlsResult**](ListOriginAccessControlsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listOriginRequestPolicies20200531

> ListOriginRequestPoliciesResult listOriginRequestPolicies20200531(opts)



&lt;p&gt;Gets a list of origin request policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'type': "type_example", // String | <p>A filter to return only the specified kinds of origin request policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of origin request policies. The response includes origin request policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of origin request policies that you want in the response.
};
apiInstance.listOriginRequestPolicies20200531(opts, (error, data, response) => {
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
 **type** | **String**| &lt;p&gt;A filter to return only the specified kinds of origin request policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Returns only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Returns only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of origin request policies. The response includes origin request policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of origin request policies that you want in the response. | [optional] 

### Return type

[**ListOriginRequestPoliciesResult**](ListOriginRequestPoliciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listPublicKeys20200531

> ListPublicKeysResult listPublicKeys20200531(opts)



List all public keys that have been added to CloudFront for this account.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last public key on that page).
  'maxItems': "maxItems_example" // String | The maximum number of public keys you want in the response body.
};
apiInstance.listPublicKeys20200531(opts, (error, data, response) => {
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
 **marker** | **String**| Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last public key on that page). | [optional] 
 **maxItems** | **String**| The maximum number of public keys you want in the response body. | [optional] 

### Return type

[**ListPublicKeysResult**](ListPublicKeysResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listRealtimeLogConfigs20200531

> ListRealtimeLogConfigsResult listRealtimeLogConfigs20200531(opts)



&lt;p&gt;Gets a list of real-time log configurations.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxItems': "maxItems_example", // String | The maximum number of real-time log configurations that you want in the response.
  'marker': "marker_example" // String | Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
};
apiInstance.listRealtimeLogConfigs20200531(opts, (error, data, response) => {
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
 **maxItems** | **String**| The maximum number of real-time log configurations that you want in the response. | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 

### Return type

[**ListRealtimeLogConfigsResult**](ListRealtimeLogConfigsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listResponseHeadersPolicies20200531

> ListResponseHeadersPoliciesResult listResponseHeadersPolicies20200531(opts)



&lt;p&gt;Gets a list of response headers policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to get only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'type': "type_example", // String | <p>A filter to get only the specified kind of response headers policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Gets only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Gets only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
  'marker': "marker_example", // String | Use this field when paginating results to indicate where to begin in your list of response headers policies. The response includes response headers policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
  'maxItems': "maxItems_example" // String | The maximum number of response headers policies that you want to get in the response.
};
apiInstance.listResponseHeadersPolicies20200531(opts, (error, data, response) => {
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
 **type** | **String**| &lt;p&gt;A filter to get only the specified kind of response headers policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Gets only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Gets only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
 **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of response headers policies. The response includes response headers policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] 
 **maxItems** | **String**| The maximum number of response headers policies that you want to get in the response. | [optional] 

### Return type

[**ListResponseHeadersPoliciesResult**](ListResponseHeadersPoliciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listStreamingDistributions20200531

> ListStreamingDistributionsResult listStreamingDistributions20200531(opts)



List streaming distributions.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'marker': "marker_example", // String | The value that you provided for the <code>Marker</code> request parameter.
  'maxItems': "maxItems_example" // String | The value that you provided for the <code>MaxItems</code> request parameter.
};
apiInstance.listStreamingDistributions20200531(opts, (error, data, response) => {
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
 **marker** | **String**| The value that you provided for the &lt;code&gt;Marker&lt;/code&gt; request parameter. | [optional] 
 **maxItems** | **String**| The value that you provided for the &lt;code&gt;MaxItems&lt;/code&gt; request parameter. | [optional] 

### Return type

[**ListStreamingDistributionsResult**](ListStreamingDistributionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listTagsForResource20200531

> ListTagsForResourceResult listTagsForResource20200531(resource, opts)



List tags for a CloudFront resource.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let resource = "resource_example"; // String | An ARN of a CloudFront resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource20200531(resource, opts, (error, data, response) => {
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
 **resource** | **String**| An ARN of a CloudFront resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResult**](ListTagsForResourceResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## publishFunction20200531

> PublishFunctionResult publishFunction20200531(name, ifMatch, opts)



&lt;p&gt;Publishes a CloudFront function by copying the function code from the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage to &lt;code&gt;LIVE&lt;/code&gt;. This automatically updates all cache behaviors that are using this function to use the newly published copy in the &lt;code&gt;LIVE&lt;/code&gt; stage.&lt;/p&gt; &lt;p&gt;When a function is published to the &lt;code&gt;LIVE&lt;/code&gt; stage, you can attach the function to a distribution&#39;s cache behavior, using the function&#39;s Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;To publish a function, you must provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value). To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let name = "name_example"; // String | The name of the function that you are publishing.
let ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the function that you are publishing, which you can get using <code>DescribeFunction</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.publishFunction20200531(name, ifMatch, opts, (error, data, response) => {
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
 **name** | **String**| The name of the function that you are publishing. | 
 **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are publishing, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PublishFunctionResult**](PublishFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## tagResource20200531

> tagResource20200531(resource, operation, tagResource20200531Request, opts)



Add tags to a CloudFront resource.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let resource = "resource_example"; // String | An ARN of a CloudFront resource.
let operation = "operation_example"; // String | 
let tagResource20200531Request = new AmazonCloudFront.TagResource20200531Request(); // TagResource20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource20200531(resource, operation, tagResource20200531Request, opts, (error, data, response) => {
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
 **resource** | **String**| An ARN of a CloudFront resource. | 
 **operation** | **String**|  | 
 **tagResource20200531Request** | [**TagResource20200531Request**](TagResource20200531Request.md)|  | 
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
- **Accept**: text/xml


## testFunction20200531

> TestFunctionResult testFunction20200531(name, ifMatch, testFunction20200531Request, opts)



&lt;p&gt;Tests a CloudFront function.&lt;/p&gt; &lt;p&gt;To test a function, you provide an &lt;i&gt;event object&lt;/i&gt; that represents an HTTP request or response that your CloudFront distribution could receive in production. CloudFront runs the function, passing it the event object that you provided, and returns the function&#39;s result (the modified event object) in the response. The response also contains function logs and error messages, if any exist. For more information about testing functions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function\&quot;&gt;Testing functions&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To test a function, you provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value) along with the event object. To get the function&#39;s name and version, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let name = "name_example"; // String | The name of the function that you are testing.
let ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the function that you are testing, which you can get using <code>DescribeFunction</code>.
let testFunction20200531Request = new AmazonCloudFront.TestFunction20200531Request(); // TestFunction20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.testFunction20200531(name, ifMatch, testFunction20200531Request, opts, (error, data, response) => {
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
 **name** | **String**| The name of the function that you are testing. | 
 **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are testing, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;. | 
 **testFunction20200531Request** | [**TestFunction20200531Request**](TestFunction20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TestFunctionResult**](TestFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## untagResource20200531

> untagResource20200531(resource, operation, untagResource20200531Request, opts)



Remove tags from a CloudFront resource.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let resource = "resource_example"; // String | An ARN of a CloudFront resource.
let operation = "operation_example"; // String | 
let untagResource20200531Request = new AmazonCloudFront.UntagResource20200531Request(); // UntagResource20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource20200531(resource, operation, untagResource20200531Request, opts, (error, data, response) => {
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
 **resource** | **String**| An ARN of a CloudFront resource. | 
 **operation** | **String**|  | 
 **untagResource20200531Request** | [**UntagResource20200531Request**](UntagResource20200531Request.md)|  | 
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
- **Accept**: text/xml


## updateCachePolicy20200531

> UpdateCachePolicyResult updateCachePolicy20200531(id, createCachePolicy20200531Request, opts)



&lt;p&gt;Updates a cache policy configuration.&lt;/p&gt; &lt;p&gt;When you update a cache policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a cache policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetCachePolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the cache policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateCachePolicy&lt;/code&gt; by providing the entire cache policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behavior's <code>CachePolicyId</code> field in the response to <code>GetDistributionConfig</code>.
let createCachePolicy20200531Request = new AmazonCloudFront.CreateCachePolicy20200531Request(); // CreateCachePolicy20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The version of the cache policy that you are updating. The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetCachePolicyConfig</code>.
};
apiInstance.updateCachePolicy20200531(id, createCachePolicy20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behavior&#39;s &lt;code&gt;CachePolicyId&lt;/code&gt; field in the response to &lt;code&gt;GetDistributionConfig&lt;/code&gt;. | 
 **createCachePolicy20200531Request** | [**CreateCachePolicy20200531Request**](CreateCachePolicy20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The version of the cache policy that you are updating. The version is returned in the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetCachePolicyConfig&lt;/code&gt;. | [optional] 

### Return type

[**UpdateCachePolicyResult**](UpdateCachePolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateCloudFrontOriginAccessIdentity20200531

> UpdateCloudFrontOriginAccessIdentityResult updateCloudFrontOriginAccessIdentity20200531(id, createCloudFrontOriginAccessIdentity20200531Request, opts)



Update an origin access identity.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identity's id.
let createCloudFrontOriginAccessIdentity20200531Request = new AmazonCloudFront.CreateCloudFrontOriginAccessIdentity20200531Request(); // CreateCloudFrontOriginAccessIdentity20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the identity's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.updateCloudFrontOriginAccessIdentity20200531(id, createCloudFrontOriginAccessIdentity20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The identity&#39;s id. | 
 **createCloudFrontOriginAccessIdentity20200531Request** | [**CreateCloudFrontOriginAccessIdentity20200531Request**](CreateCloudFrontOriginAccessIdentity20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the identity&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

[**UpdateCloudFrontOriginAccessIdentityResult**](UpdateCloudFrontOriginAccessIdentityResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateContinuousDeploymentPolicy20200531

> UpdateContinuousDeploymentPolicyResult updateContinuousDeploymentPolicy20200531(id, createContinuousDeploymentPolicy20200531Request, opts)



&lt;p&gt;Updates a continuous deployment policy. You can update a continuous deployment policy to enable or disable it, to change the percentage of traffic that it sends to the staging distribution, or to change the staging distribution that it sends traffic to.&lt;/p&gt; &lt;p&gt;When you update a continuous deployment policy configuration, all the fields are updated with the values that are provided in the request. You cannot update some fields independent of others. To update a continuous deployment policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetContinuousDeploymentPolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the continuous deployment policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;UpdateContinuousDeploymentPolicy&lt;/code&gt;, providing the entire continuous deployment policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the continuous deployment policy that you are updating.
let createContinuousDeploymentPolicy20200531Request = new AmazonCloudFront.CreateContinuousDeploymentPolicy20200531Request(); // CreateContinuousDeploymentPolicy20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The current version (<code>ETag</code> value) of the continuous deployment policy that you are updating.
};
apiInstance.updateContinuousDeploymentPolicy20200531(id, createContinuousDeploymentPolicy20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the continuous deployment policy that you are updating. | 
 **createContinuousDeploymentPolicy20200531Request** | [**CreateContinuousDeploymentPolicy20200531Request**](CreateContinuousDeploymentPolicy20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the continuous deployment policy that you are updating. | [optional] 

### Return type

[**UpdateContinuousDeploymentPolicyResult**](UpdateContinuousDeploymentPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateDistribution20200531

> UpdateDistributionResult updateDistribution20200531(id, createDistribution20200531Request, opts)



&lt;p&gt;Updates the configuration for a CloudFront distribution.&lt;/p&gt; &lt;p&gt;The update process includes getting the current distribution configuration, updating it to make your changes, and then submitting an &lt;code&gt;UpdateDistribution&lt;/code&gt; request to make the updates.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To update a web distribution using the CloudFront API&lt;/b&gt; &lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetDistributionConfig&lt;/code&gt; to get the current configuration, including the version identifier (&lt;code&gt;ETag&lt;/code&gt;).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the distribution configuration that was returned in the response. Note the following important requirements and restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must rename the &lt;code&gt;ETag&lt;/code&gt; field to &lt;code&gt;IfMatch&lt;/code&gt;, leaving the value unchanged. (Set the value of &lt;code&gt;IfMatch&lt;/code&gt; to the value of &lt;code&gt;ETag&lt;/code&gt;, then remove the &lt;code&gt;ETag&lt;/code&gt; field.)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t change the value of &lt;code&gt;CallerReference&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateDistribution&lt;/code&gt; request, providing the distribution configuration. The new configuration replaces the existing configuration. The values that you specify in an &lt;code&gt;UpdateDistribution&lt;/code&gt; request are not merged into your existing configuration. Make sure to include all fields: the ones that you modified and also the ones that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The distribution's id.
let createDistribution20200531Request = new AmazonCloudFront.CreateDistribution20200531Request(); // CreateDistribution20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.updateDistribution20200531(id, createDistribution20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The distribution&#39;s id. | 
 **createDistribution20200531Request** | [**CreateDistribution20200531Request**](CreateDistribution20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the distribution&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

[**UpdateDistributionResult**](UpdateDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateDistributionWithStagingConfig20200531

> UpdateDistributionWithStagingConfigResult updateDistributionWithStagingConfig20200531(id, opts)



&lt;p&gt;Copies the staging distribution&#39;s configuration to its corresponding primary distribution. The primary distribution retains its &lt;code&gt;Aliases&lt;/code&gt; (also known as alternate domain names or CNAMEs) and &lt;code&gt;ContinuousDeploymentPolicyId&lt;/code&gt; value, but otherwise its configuration is overwritten to match the staging distribution.&lt;/p&gt; &lt;p&gt;You can use this operation in a continuous deployment workflow after you have tested configuration changes on the staging distribution. After using a continuous deployment policy to move a portion of your domain name&#39;s traffic to the staging distribution and verifying that it works as intended, you can use this operation to copy the staging distribution&#39;s configuration to the primary distribution. This action will disable the continuous deployment policy and move your domain&#39;s traffic back to the primary distribution.&lt;/p&gt; &lt;p&gt;This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html\&quot;&gt;GetDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html\&quot;&gt;UpdateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the primary distribution to which you are copying a staging distribution's configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'stagingDistributionId': "stagingDistributionId_example", // String | The identifier of the staging distribution whose configuration you are copying to the primary distribution.
  'ifMatch': "ifMatch_example" // String | <p>The current versions (<code>ETag</code> values) of both primary and staging distributions. Provide these in the following format:</p> <p> <code>&lt;primary ETag&gt;, &lt;staging ETag&gt;</code> </p>
};
apiInstance.updateDistributionWithStagingConfig20200531(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the primary distribution to which you are copying a staging distribution&#39;s configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **stagingDistributionId** | **String**| The identifier of the staging distribution whose configuration you are copying to the primary distribution. | [optional] 
 **ifMatch** | **String**| &lt;p&gt;The current versions (&lt;code&gt;ETag&lt;/code&gt; values) of both primary and staging distributions. Provide these in the following format:&lt;/p&gt; &lt;p&gt; &lt;code&gt;&amp;lt;primary ETag&amp;gt;, &amp;lt;staging ETag&amp;gt;&lt;/code&gt; &lt;/p&gt; | [optional] 

### Return type

[**UpdateDistributionWithStagingConfigResult**](UpdateDistributionWithStagingConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## updateFieldLevelEncryptionConfig20200531

> UpdateFieldLevelEncryptionConfigResult updateFieldLevelEncryptionConfig20200531(id, createFieldLevelEncryptionConfig20200531Request, opts)



Update a field-level encryption configuration.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The ID of the configuration you want to update.
let createFieldLevelEncryptionConfig20200531Request = new AmazonCloudFront.CreateFieldLevelEncryptionConfig20200531Request(); // CreateFieldLevelEncryptionConfig20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the configuration identity to update. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.updateFieldLevelEncryptionConfig20200531(id, createFieldLevelEncryptionConfig20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the configuration you want to update. | 
 **createFieldLevelEncryptionConfig20200531Request** | [**CreateFieldLevelEncryptionConfig20200531Request**](CreateFieldLevelEncryptionConfig20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the configuration identity to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

[**UpdateFieldLevelEncryptionConfigResult**](UpdateFieldLevelEncryptionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateFieldLevelEncryptionProfile20200531

> UpdateFieldLevelEncryptionProfileResult updateFieldLevelEncryptionProfile20200531(id, createFieldLevelEncryptionProfile20200531Request, opts)



Update a field-level encryption profile.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The ID of the field-level encryption profile request.
let createFieldLevelEncryptionProfile20200531Request = new AmazonCloudFront.CreateFieldLevelEncryptionProfile20200531Request(); // CreateFieldLevelEncryptionProfile20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the profile identity to update. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.updateFieldLevelEncryptionProfile20200531(id, createFieldLevelEncryptionProfile20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the field-level encryption profile request. | 
 **createFieldLevelEncryptionProfile20200531Request** | [**CreateFieldLevelEncryptionProfile20200531Request**](CreateFieldLevelEncryptionProfile20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the profile identity to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

[**UpdateFieldLevelEncryptionProfileResult**](UpdateFieldLevelEncryptionProfileResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateFunction20200531

> UpdateFunctionResult updateFunction20200531(name, ifMatch, updateFunction20200531Request, opts)



&lt;p&gt;Updates a CloudFront function.&lt;/p&gt; &lt;p&gt;You can update a function&#39;s code or the comment that describes the function. You cannot update a function&#39;s name.&lt;/p&gt; &lt;p&gt;To update a function, you provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value) along with the updated function code. To get the name and version, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let name = "name_example"; // String | The name of the function that you are updating.
let ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the function that you are updating, which you can get using <code>DescribeFunction</code>.
let updateFunction20200531Request = new AmazonCloudFront.UpdateFunction20200531Request(); // UpdateFunction20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateFunction20200531(name, ifMatch, updateFunction20200531Request, opts, (error, data, response) => {
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
 **name** | **String**| The name of the function that you are updating. | 
 **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are updating, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;. | 
 **updateFunction20200531Request** | [**UpdateFunction20200531Request**](UpdateFunction20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateFunctionResult**](UpdateFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateKeyGroup20200531

> UpdateKeyGroupResult updateKeyGroup20200531(id, createKeyGroup20200531Request, opts)



&lt;p&gt;Updates a key group.&lt;/p&gt; &lt;p&gt;When you update a key group, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a key group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Get the current key group with &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the key group that you want to update. For example, add or remove public key IDs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateKeyGroup&lt;/code&gt; with the entire key group object, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the key group that you are updating.
let createKeyGroup20200531Request = new AmazonCloudFront.CreateKeyGroup20200531Request(); // CreateKeyGroup20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The version of the key group that you are updating. The version is the key group's <code>ETag</code> value.
};
apiInstance.updateKeyGroup20200531(id, createKeyGroup20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the key group that you are updating. | 
 **createKeyGroup20200531Request** | [**CreateKeyGroup20200531Request**](CreateKeyGroup20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The version of the key group that you are updating. The version is the key group&#39;s &lt;code&gt;ETag&lt;/code&gt; value. | [optional] 

### Return type

[**UpdateKeyGroupResult**](UpdateKeyGroupResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateOriginAccessControl20200531

> UpdateOriginAccessControlResult updateOriginAccessControl20200531(id, createOriginAccessControl20200531Request, opts)



Updates a CloudFront origin access control.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier of the origin access control that you are updating.
let createOriginAccessControl20200531Request = new AmazonCloudFront.CreateOriginAccessControl20200531Request(); // CreateOriginAccessControl20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The current version (<code>ETag</code> value) of the origin access control that you are updating.
};
apiInstance.updateOriginAccessControl20200531(id, createOriginAccessControl20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the origin access control that you are updating. | 
 **createOriginAccessControl20200531Request** | [**CreateOriginAccessControl20200531Request**](CreateOriginAccessControl20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the origin access control that you are updating. | [optional] 

### Return type

[**UpdateOriginAccessControlResult**](UpdateOriginAccessControlResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateOriginRequestPolicy20200531

> UpdateOriginRequestPolicyResult updateOriginRequestPolicy20200531(id, createOriginRequestPolicy20200531Request, opts)



&lt;p&gt;Updates an origin request policy configuration.&lt;/p&gt; &lt;p&gt;When you update an origin request policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update an origin request policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the origin request policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateOriginRequestPolicy&lt;/code&gt; by providing the entire origin request policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behavior's <code>OriginRequestPolicyId</code> field in the response to <code>GetDistributionConfig</code>.
let createOriginRequestPolicy20200531Request = new AmazonCloudFront.CreateOriginRequestPolicy20200531Request(); // CreateOriginRequestPolicy20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The version of the origin request policy that you are updating. The version is returned in the origin request policy's <code>ETag</code> field in the response to <code>GetOriginRequestPolicyConfig</code>.
};
apiInstance.updateOriginRequestPolicy20200531(id, createOriginRequestPolicy20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behavior&#39;s &lt;code&gt;OriginRequestPolicyId&lt;/code&gt; field in the response to &lt;code&gt;GetDistributionConfig&lt;/code&gt;. | 
 **createOriginRequestPolicy20200531Request** | [**CreateOriginRequestPolicy20200531Request**](CreateOriginRequestPolicy20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The version of the origin request policy that you are updating. The version is returned in the origin request policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt;. | [optional] 

### Return type

[**UpdateOriginRequestPolicyResult**](UpdateOriginRequestPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updatePublicKey20200531

> UpdatePublicKeyResult updatePublicKey20200531(id, createPublicKey20200531Request, opts)



Update public key information. Note that the only value you can change is the comment.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier of the public key that you are updating.
let createPublicKey20200531Request = new AmazonCloudFront.CreatePublicKey20200531Request(); // CreatePublicKey20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the public key to update. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.updatePublicKey20200531(id, createPublicKey20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the public key that you are updating. | 
 **createPublicKey20200531Request** | [**CreatePublicKey20200531Request**](CreatePublicKey20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the public key to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

[**UpdatePublicKeyResult**](UpdatePublicKeyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateRealtimeLogConfig20200531

> UpdateRealtimeLogConfigResult updateRealtimeLogConfig20200531(updateRealtimeLogConfig20200531Request, opts)



&lt;p&gt;Updates a real-time log configuration.&lt;/p&gt; &lt;p&gt;When you update a real-time log configuration, all the parameters are updated with the values provided in the request. You cannot update some parameters independent of others. To update a real-time log configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;GetRealtimeLogConfig&lt;/code&gt; to get the current real-time log configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the parameters in the real-time log configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call this API (&lt;code&gt;UpdateRealtimeLogConfig&lt;/code&gt;) by providing the entire real-time log configuration, including the parameters that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;You cannot update a real-time log configuration&#39;s &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;ARN&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let updateRealtimeLogConfig20200531Request = new AmazonCloudFront.UpdateRealtimeLogConfig20200531Request(); // UpdateRealtimeLogConfig20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRealtimeLogConfig20200531(updateRealtimeLogConfig20200531Request, opts, (error, data, response) => {
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
 **updateRealtimeLogConfig20200531Request** | [**UpdateRealtimeLogConfig20200531Request**](UpdateRealtimeLogConfig20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRealtimeLogConfigResult**](UpdateRealtimeLogConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateResponseHeadersPolicy20200531

> UpdateResponseHeadersPolicyResult updateResponseHeadersPolicy20200531(id, createResponseHeadersPolicy20200531Request, opts)



&lt;p&gt;Updates a response headers policy.&lt;/p&gt; &lt;p&gt;When you update a response headers policy, the entire policy is replaced. You cannot update some policy fields independent of others. To update a response headers policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt; to get the current policy&#39;s configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Modify the fields in the response headers policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateResponseHeadersPolicy&lt;/code&gt;, providing the entire response headers policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The identifier for the response headers policy that you are updating.
let createResponseHeadersPolicy20200531Request = new AmazonCloudFront.CreateResponseHeadersPolicy20200531Request(); // CreateResponseHeadersPolicy20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | <p>The version of the response headers policy that you are updating.</p> <p>The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetResponseHeadersPolicyConfig</code>.</p>
};
apiInstance.updateResponseHeadersPolicy20200531(id, createResponseHeadersPolicy20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The identifier for the response headers policy that you are updating. | 
 **createResponseHeadersPolicy20200531Request** | [**CreateResponseHeadersPolicy20200531Request**](CreateResponseHeadersPolicy20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| &lt;p&gt;The version of the response headers policy that you are updating.&lt;/p&gt; &lt;p&gt;The version is returned in the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt;.&lt;/p&gt; | [optional] 

### Return type

[**UpdateResponseHeadersPolicyResult**](UpdateResponseHeadersPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## updateStreamingDistribution20200531

> UpdateStreamingDistributionResult updateStreamingDistribution20200531(id, createStreamingDistribution20200531Request, opts)



Update a streaming distribution.

### Example

```javascript
import AmazonCloudFront from 'amazon_cloud_front';
let defaultClient = AmazonCloudFront.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudFront.DefaultApi();
let id = "id_example"; // String | The streaming distribution's id.
let createStreamingDistribution20200531Request = new AmazonCloudFront.CreateStreamingDistribution20200531Request(); // CreateStreamingDistribution20200531Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'ifMatch': "ifMatch_example" // String | The value of the <code>ETag</code> header that you received when retrieving the streaming distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
};
apiInstance.updateStreamingDistribution20200531(id, createStreamingDistribution20200531Request, opts, (error, data, response) => {
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
 **id** | **String**| The streaming distribution&#39;s id. | 
 **createStreamingDistribution20200531Request** | [**CreateStreamingDistribution20200531Request**](CreateStreamingDistribution20200531Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the streaming distribution&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] 

### Return type

[**UpdateStreamingDistributionResult**](UpdateStreamingDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml

