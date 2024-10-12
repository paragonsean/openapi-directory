# DefaultApi

All URIs are relative to *https://cloudfront.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associateAlias20200531**](DefaultApi.md#associateAlias20200531) | **PUT** /2020-05-31/distribution/{TargetDistributionId}/associate-alias#Alias |  |
| [**copyDistribution20200531**](DefaultApi.md#copyDistribution20200531) | **POST** /2020-05-31/distribution/{PrimaryDistributionId}/copy |  |
| [**createCachePolicy20200531**](DefaultApi.md#createCachePolicy20200531) | **POST** /2020-05-31/cache-policy |  |
| [**createCloudFrontOriginAccessIdentity20200531**](DefaultApi.md#createCloudFrontOriginAccessIdentity20200531) | **POST** /2020-05-31/origin-access-identity/cloudfront |  |
| [**createContinuousDeploymentPolicy20200531**](DefaultApi.md#createContinuousDeploymentPolicy20200531) | **POST** /2020-05-31/continuous-deployment-policy |  |
| [**createDistribution20200531**](DefaultApi.md#createDistribution20200531) | **POST** /2020-05-31/distribution |  |
| [**createDistributionWithTags20200531**](DefaultApi.md#createDistributionWithTags20200531) | **POST** /2020-05-31/distribution#WithTags |  |
| [**createFieldLevelEncryptionConfig20200531**](DefaultApi.md#createFieldLevelEncryptionConfig20200531) | **POST** /2020-05-31/field-level-encryption |  |
| [**createFieldLevelEncryptionProfile20200531**](DefaultApi.md#createFieldLevelEncryptionProfile20200531) | **POST** /2020-05-31/field-level-encryption-profile |  |
| [**createFunction20200531**](DefaultApi.md#createFunction20200531) | **POST** /2020-05-31/function |  |
| [**createInvalidation20200531**](DefaultApi.md#createInvalidation20200531) | **POST** /2020-05-31/distribution/{DistributionId}/invalidation |  |
| [**createKeyGroup20200531**](DefaultApi.md#createKeyGroup20200531) | **POST** /2020-05-31/key-group |  |
| [**createMonitoringSubscription20200531**](DefaultApi.md#createMonitoringSubscription20200531) | **POST** /2020-05-31/distributions/{DistributionId}/monitoring-subscription/ |  |
| [**createOriginAccessControl20200531**](DefaultApi.md#createOriginAccessControl20200531) | **POST** /2020-05-31/origin-access-control |  |
| [**createOriginRequestPolicy20200531**](DefaultApi.md#createOriginRequestPolicy20200531) | **POST** /2020-05-31/origin-request-policy |  |
| [**createPublicKey20200531**](DefaultApi.md#createPublicKey20200531) | **POST** /2020-05-31/public-key |  |
| [**createRealtimeLogConfig20200531**](DefaultApi.md#createRealtimeLogConfig20200531) | **POST** /2020-05-31/realtime-log-config |  |
| [**createResponseHeadersPolicy20200531**](DefaultApi.md#createResponseHeadersPolicy20200531) | **POST** /2020-05-31/response-headers-policy |  |
| [**createStreamingDistribution20200531**](DefaultApi.md#createStreamingDistribution20200531) | **POST** /2020-05-31/streaming-distribution |  |
| [**createStreamingDistributionWithTags20200531**](DefaultApi.md#createStreamingDistributionWithTags20200531) | **POST** /2020-05-31/streaming-distribution#WithTags |  |
| [**deleteCachePolicy20200531**](DefaultApi.md#deleteCachePolicy20200531) | **DELETE** /2020-05-31/cache-policy/{Id} |  |
| [**deleteCloudFrontOriginAccessIdentity20200531**](DefaultApi.md#deleteCloudFrontOriginAccessIdentity20200531) | **DELETE** /2020-05-31/origin-access-identity/cloudfront/{Id} |  |
| [**deleteContinuousDeploymentPolicy20200531**](DefaultApi.md#deleteContinuousDeploymentPolicy20200531) | **DELETE** /2020-05-31/continuous-deployment-policy/{Id} |  |
| [**deleteDistribution20200531**](DefaultApi.md#deleteDistribution20200531) | **DELETE** /2020-05-31/distribution/{Id} |  |
| [**deleteFieldLevelEncryptionConfig20200531**](DefaultApi.md#deleteFieldLevelEncryptionConfig20200531) | **DELETE** /2020-05-31/field-level-encryption/{Id} |  |
| [**deleteFieldLevelEncryptionProfile20200531**](DefaultApi.md#deleteFieldLevelEncryptionProfile20200531) | **DELETE** /2020-05-31/field-level-encryption-profile/{Id} |  |
| [**deleteFunction20200531**](DefaultApi.md#deleteFunction20200531) | **DELETE** /2020-05-31/function/{Name}#If-Match |  |
| [**deleteKeyGroup20200531**](DefaultApi.md#deleteKeyGroup20200531) | **DELETE** /2020-05-31/key-group/{Id} |  |
| [**deleteMonitoringSubscription20200531**](DefaultApi.md#deleteMonitoringSubscription20200531) | **DELETE** /2020-05-31/distributions/{DistributionId}/monitoring-subscription/ |  |
| [**deleteOriginAccessControl20200531**](DefaultApi.md#deleteOriginAccessControl20200531) | **DELETE** /2020-05-31/origin-access-control/{Id} |  |
| [**deleteOriginRequestPolicy20200531**](DefaultApi.md#deleteOriginRequestPolicy20200531) | **DELETE** /2020-05-31/origin-request-policy/{Id} |  |
| [**deletePublicKey20200531**](DefaultApi.md#deletePublicKey20200531) | **DELETE** /2020-05-31/public-key/{Id} |  |
| [**deleteRealtimeLogConfig20200531**](DefaultApi.md#deleteRealtimeLogConfig20200531) | **POST** /2020-05-31/delete-realtime-log-config/ |  |
| [**deleteResponseHeadersPolicy20200531**](DefaultApi.md#deleteResponseHeadersPolicy20200531) | **DELETE** /2020-05-31/response-headers-policy/{Id} |  |
| [**deleteStreamingDistribution20200531**](DefaultApi.md#deleteStreamingDistribution20200531) | **DELETE** /2020-05-31/streaming-distribution/{Id} |  |
| [**describeFunction20200531**](DefaultApi.md#describeFunction20200531) | **GET** /2020-05-31/function/{Name}/describe |  |
| [**getCachePolicy20200531**](DefaultApi.md#getCachePolicy20200531) | **GET** /2020-05-31/cache-policy/{Id} |  |
| [**getCachePolicyConfig20200531**](DefaultApi.md#getCachePolicyConfig20200531) | **GET** /2020-05-31/cache-policy/{Id}/config |  |
| [**getCloudFrontOriginAccessIdentity20200531**](DefaultApi.md#getCloudFrontOriginAccessIdentity20200531) | **GET** /2020-05-31/origin-access-identity/cloudfront/{Id} |  |
| [**getCloudFrontOriginAccessIdentityConfig20200531**](DefaultApi.md#getCloudFrontOriginAccessIdentityConfig20200531) | **GET** /2020-05-31/origin-access-identity/cloudfront/{Id}/config |  |
| [**getContinuousDeploymentPolicy20200531**](DefaultApi.md#getContinuousDeploymentPolicy20200531) | **GET** /2020-05-31/continuous-deployment-policy/{Id} |  |
| [**getContinuousDeploymentPolicyConfig20200531**](DefaultApi.md#getContinuousDeploymentPolicyConfig20200531) | **GET** /2020-05-31/continuous-deployment-policy/{Id}/config |  |
| [**getDistribution20200531**](DefaultApi.md#getDistribution20200531) | **GET** /2020-05-31/distribution/{Id} |  |
| [**getDistributionConfig20200531**](DefaultApi.md#getDistributionConfig20200531) | **GET** /2020-05-31/distribution/{Id}/config |  |
| [**getFieldLevelEncryption20200531**](DefaultApi.md#getFieldLevelEncryption20200531) | **GET** /2020-05-31/field-level-encryption/{Id} |  |
| [**getFieldLevelEncryptionConfig20200531**](DefaultApi.md#getFieldLevelEncryptionConfig20200531) | **GET** /2020-05-31/field-level-encryption/{Id}/config |  |
| [**getFieldLevelEncryptionProfile20200531**](DefaultApi.md#getFieldLevelEncryptionProfile20200531) | **GET** /2020-05-31/field-level-encryption-profile/{Id} |  |
| [**getFieldLevelEncryptionProfileConfig20200531**](DefaultApi.md#getFieldLevelEncryptionProfileConfig20200531) | **GET** /2020-05-31/field-level-encryption-profile/{Id}/config |  |
| [**getFunction20200531**](DefaultApi.md#getFunction20200531) | **GET** /2020-05-31/function/{Name} |  |
| [**getInvalidation20200531**](DefaultApi.md#getInvalidation20200531) | **GET** /2020-05-31/distribution/{DistributionId}/invalidation/{Id} |  |
| [**getKeyGroup20200531**](DefaultApi.md#getKeyGroup20200531) | **GET** /2020-05-31/key-group/{Id} |  |
| [**getKeyGroupConfig20200531**](DefaultApi.md#getKeyGroupConfig20200531) | **GET** /2020-05-31/key-group/{Id}/config |  |
| [**getMonitoringSubscription20200531**](DefaultApi.md#getMonitoringSubscription20200531) | **GET** /2020-05-31/distributions/{DistributionId}/monitoring-subscription/ |  |
| [**getOriginAccessControl20200531**](DefaultApi.md#getOriginAccessControl20200531) | **GET** /2020-05-31/origin-access-control/{Id} |  |
| [**getOriginAccessControlConfig20200531**](DefaultApi.md#getOriginAccessControlConfig20200531) | **GET** /2020-05-31/origin-access-control/{Id}/config |  |
| [**getOriginRequestPolicy20200531**](DefaultApi.md#getOriginRequestPolicy20200531) | **GET** /2020-05-31/origin-request-policy/{Id} |  |
| [**getOriginRequestPolicyConfig20200531**](DefaultApi.md#getOriginRequestPolicyConfig20200531) | **GET** /2020-05-31/origin-request-policy/{Id}/config |  |
| [**getPublicKey20200531**](DefaultApi.md#getPublicKey20200531) | **GET** /2020-05-31/public-key/{Id} |  |
| [**getPublicKeyConfig20200531**](DefaultApi.md#getPublicKeyConfig20200531) | **GET** /2020-05-31/public-key/{Id}/config |  |
| [**getRealtimeLogConfig20200531**](DefaultApi.md#getRealtimeLogConfig20200531) | **POST** /2020-05-31/get-realtime-log-config/ |  |
| [**getResponseHeadersPolicy20200531**](DefaultApi.md#getResponseHeadersPolicy20200531) | **GET** /2020-05-31/response-headers-policy/{Id} |  |
| [**getResponseHeadersPolicyConfig20200531**](DefaultApi.md#getResponseHeadersPolicyConfig20200531) | **GET** /2020-05-31/response-headers-policy/{Id}/config |  |
| [**getStreamingDistribution20200531**](DefaultApi.md#getStreamingDistribution20200531) | **GET** /2020-05-31/streaming-distribution/{Id} |  |
| [**getStreamingDistributionConfig20200531**](DefaultApi.md#getStreamingDistributionConfig20200531) | **GET** /2020-05-31/streaming-distribution/{Id}/config |  |
| [**listCachePolicies20200531**](DefaultApi.md#listCachePolicies20200531) | **GET** /2020-05-31/cache-policy |  |
| [**listCloudFrontOriginAccessIdentities20200531**](DefaultApi.md#listCloudFrontOriginAccessIdentities20200531) | **GET** /2020-05-31/origin-access-identity/cloudfront |  |
| [**listConflictingAliases20200531**](DefaultApi.md#listConflictingAliases20200531) | **GET** /2020-05-31/conflicting-alias#DistributionId&amp;Alias |  |
| [**listContinuousDeploymentPolicies20200531**](DefaultApi.md#listContinuousDeploymentPolicies20200531) | **GET** /2020-05-31/continuous-deployment-policy |  |
| [**listDistributions20200531**](DefaultApi.md#listDistributions20200531) | **GET** /2020-05-31/distribution |  |
| [**listDistributionsByCachePolicyId20200531**](DefaultApi.md#listDistributionsByCachePolicyId20200531) | **GET** /2020-05-31/distributionsByCachePolicyId/{CachePolicyId} |  |
| [**listDistributionsByKeyGroup20200531**](DefaultApi.md#listDistributionsByKeyGroup20200531) | **GET** /2020-05-31/distributionsByKeyGroupId/{KeyGroupId} |  |
| [**listDistributionsByOriginRequestPolicyId20200531**](DefaultApi.md#listDistributionsByOriginRequestPolicyId20200531) | **GET** /2020-05-31/distributionsByOriginRequestPolicyId/{OriginRequestPolicyId} |  |
| [**listDistributionsByRealtimeLogConfig20200531**](DefaultApi.md#listDistributionsByRealtimeLogConfig20200531) | **POST** /2020-05-31/distributionsByRealtimeLogConfig/ |  |
| [**listDistributionsByResponseHeadersPolicyId20200531**](DefaultApi.md#listDistributionsByResponseHeadersPolicyId20200531) | **GET** /2020-05-31/distributionsByResponseHeadersPolicyId/{ResponseHeadersPolicyId} |  |
| [**listDistributionsByWebACLId20200531**](DefaultApi.md#listDistributionsByWebACLId20200531) | **GET** /2020-05-31/distributionsByWebACLId/{WebACLId} |  |
| [**listFieldLevelEncryptionConfigs20200531**](DefaultApi.md#listFieldLevelEncryptionConfigs20200531) | **GET** /2020-05-31/field-level-encryption |  |
| [**listFieldLevelEncryptionProfiles20200531**](DefaultApi.md#listFieldLevelEncryptionProfiles20200531) | **GET** /2020-05-31/field-level-encryption-profile |  |
| [**listFunctions20200531**](DefaultApi.md#listFunctions20200531) | **GET** /2020-05-31/function |  |
| [**listInvalidations20200531**](DefaultApi.md#listInvalidations20200531) | **GET** /2020-05-31/distribution/{DistributionId}/invalidation |  |
| [**listKeyGroups20200531**](DefaultApi.md#listKeyGroups20200531) | **GET** /2020-05-31/key-group |  |
| [**listOriginAccessControls20200531**](DefaultApi.md#listOriginAccessControls20200531) | **GET** /2020-05-31/origin-access-control |  |
| [**listOriginRequestPolicies20200531**](DefaultApi.md#listOriginRequestPolicies20200531) | **GET** /2020-05-31/origin-request-policy |  |
| [**listPublicKeys20200531**](DefaultApi.md#listPublicKeys20200531) | **GET** /2020-05-31/public-key |  |
| [**listRealtimeLogConfigs20200531**](DefaultApi.md#listRealtimeLogConfigs20200531) | **GET** /2020-05-31/realtime-log-config |  |
| [**listResponseHeadersPolicies20200531**](DefaultApi.md#listResponseHeadersPolicies20200531) | **GET** /2020-05-31/response-headers-policy |  |
| [**listStreamingDistributions20200531**](DefaultApi.md#listStreamingDistributions20200531) | **GET** /2020-05-31/streaming-distribution |  |
| [**listTagsForResource20200531**](DefaultApi.md#listTagsForResource20200531) | **GET** /2020-05-31/tagging#Resource |  |
| [**publishFunction20200531**](DefaultApi.md#publishFunction20200531) | **POST** /2020-05-31/function/{Name}/publish#If-Match |  |
| [**tagResource20200531**](DefaultApi.md#tagResource20200531) | **POST** /2020-05-31/tagging#Operation&#x3D;Tag&amp;Resource |  |
| [**testFunction20200531**](DefaultApi.md#testFunction20200531) | **POST** /2020-05-31/function/{Name}/test#If-Match |  |
| [**untagResource20200531**](DefaultApi.md#untagResource20200531) | **POST** /2020-05-31/tagging#Operation&#x3D;Untag&amp;Resource |  |
| [**updateCachePolicy20200531**](DefaultApi.md#updateCachePolicy20200531) | **PUT** /2020-05-31/cache-policy/{Id} |  |
| [**updateCloudFrontOriginAccessIdentity20200531**](DefaultApi.md#updateCloudFrontOriginAccessIdentity20200531) | **PUT** /2020-05-31/origin-access-identity/cloudfront/{Id}/config |  |
| [**updateContinuousDeploymentPolicy20200531**](DefaultApi.md#updateContinuousDeploymentPolicy20200531) | **PUT** /2020-05-31/continuous-deployment-policy/{Id} |  |
| [**updateDistribution20200531**](DefaultApi.md#updateDistribution20200531) | **PUT** /2020-05-31/distribution/{Id}/config |  |
| [**updateDistributionWithStagingConfig20200531**](DefaultApi.md#updateDistributionWithStagingConfig20200531) | **PUT** /2020-05-31/distribution/{Id}/promote-staging-config |  |
| [**updateFieldLevelEncryptionConfig20200531**](DefaultApi.md#updateFieldLevelEncryptionConfig20200531) | **PUT** /2020-05-31/field-level-encryption/{Id}/config |  |
| [**updateFieldLevelEncryptionProfile20200531**](DefaultApi.md#updateFieldLevelEncryptionProfile20200531) | **PUT** /2020-05-31/field-level-encryption-profile/{Id}/config |  |
| [**updateFunction20200531**](DefaultApi.md#updateFunction20200531) | **PUT** /2020-05-31/function/{Name}#If-Match |  |
| [**updateKeyGroup20200531**](DefaultApi.md#updateKeyGroup20200531) | **PUT** /2020-05-31/key-group/{Id} |  |
| [**updateOriginAccessControl20200531**](DefaultApi.md#updateOriginAccessControl20200531) | **PUT** /2020-05-31/origin-access-control/{Id}/config |  |
| [**updateOriginRequestPolicy20200531**](DefaultApi.md#updateOriginRequestPolicy20200531) | **PUT** /2020-05-31/origin-request-policy/{Id} |  |
| [**updatePublicKey20200531**](DefaultApi.md#updatePublicKey20200531) | **PUT** /2020-05-31/public-key/{Id}/config |  |
| [**updateRealtimeLogConfig20200531**](DefaultApi.md#updateRealtimeLogConfig20200531) | **PUT** /2020-05-31/realtime-log-config/ |  |
| [**updateResponseHeadersPolicy20200531**](DefaultApi.md#updateResponseHeadersPolicy20200531) | **PUT** /2020-05-31/response-headers-policy/{Id} |  |
| [**updateStreamingDistribution20200531**](DefaultApi.md#updateStreamingDistribution20200531) | **PUT** /2020-05-31/streaming-distribution/{Id}/config |  |


<a id="associateAlias20200531"></a>
# **associateAlias20200531**
> associateAlias20200531(targetDistributionId, alias, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Associates an alias (also known as a CNAME or an alternate domain name) with a CloudFront distribution.&lt;/p&gt; &lt;p&gt;With this operation you can move an alias that&#39;s already in use on a CloudFront distribution to a different distribution in one step. This prevents the downtime that could occur if you first remove the alias from one distribution and then separately add the alias to another distribution.&lt;/p&gt; &lt;p&gt;To use this operation to associate an alias with a distribution, you provide the alias and the ID of the target distribution for the alias. For more information, including how to set up the target distribution, prerequisites that you must complete, and other restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\&quot;&gt;Moving an alternate domain name to a different distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String targetDistributionId = "targetDistributionId_example"; // String | The ID of the distribution that you're associating the alias with.
    String alias = "alias_example"; // String | The alias (also known as a CNAME) to add to the target distribution.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.associateAlias20200531(targetDistributionId, alias, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateAlias20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **targetDistributionId** | **String**| The ID of the distribution that you&#39;re associating the alias with. | |
| **alias** | **String**| The alias (also known as a CNAME) to add to the target distribution. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | NoSuchDistribution |  -  |
| **482** | TooManyDistributionCNAMEs |  -  |
| **483** | IllegalUpdate |  -  |
| **484** | AccessDenied |  -  |

<a id="copyDistribution20200531"></a>
# **copyDistribution20200531**
> CopyDistributionResult copyDistribution20200531(primaryDistributionId, copyDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, staging, ifMatch)



&lt;p&gt;Creates a staging distribution using the configuration of the provided primary distribution. A staging distribution is a copy of an existing distribution (called the primary distribution) that you can use in a continuous deployment workflow.&lt;/p&gt; &lt;p&gt;After you create a staging distribution, you can use &lt;code&gt;UpdateDistribution&lt;/code&gt; to modify the staging distribution&#39;s configuration. Then you can use &lt;code&gt;CreateContinuousDeploymentPolicy&lt;/code&gt; to incrementally move traffic to the staging distribution.&lt;/p&gt; &lt;p&gt;This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html\&quot;&gt;GetDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html\&quot;&gt;CreateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CopyDistribution.html\&quot;&gt;CopyDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String primaryDistributionId = "primaryDistributionId_example"; // String | The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use <code>ListDistributions</code>.
    CopyDistribution20200531Request copyDistribution20200531Request = new CopyDistribution20200531Request(); // CopyDistribution20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean staging = true; // Boolean | The type of distribution that your primary distribution will be copied to. The only valid value is <code>True</code>, indicating that you are copying to a staging distribution.
    String ifMatch = "ifMatch_example"; // String | The version identifier of the primary distribution whose configuration you are copying. This is the <code>ETag</code> value returned in the response to <code>GetDistribution</code> and <code>GetDistributionConfig</code>.
    try {
      CopyDistributionResult result = apiInstance.copyDistribution20200531(primaryDistributionId, copyDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, staging, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#copyDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **primaryDistributionId** | **String**| The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use &lt;code&gt;ListDistributions&lt;/code&gt;. | |
| **copyDistribution20200531Request** | [**CopyDistribution20200531Request**](CopyDistribution20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **staging** | **Boolean**| The type of distribution that your primary distribution will be copied to. The only valid value is &lt;code&gt;True&lt;/code&gt;, indicating that you are copying to a staging distribution. | [optional] |
| **ifMatch** | **String**| The version identifier of the primary distribution whose configuration you are copying. This is the &lt;code&gt;ETag&lt;/code&gt; value returned in the response to &lt;code&gt;GetDistribution&lt;/code&gt; and &lt;code&gt;GetDistributionConfig&lt;/code&gt;. | [optional] |

### Return type

[**CopyDistributionResult**](CopyDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | CNAMEAlreadyExists |  -  |
| **481** | DistributionAlreadyExists |  -  |
| **482** | InvalidOrigin |  -  |
| **483** | InvalidOriginAccessIdentity |  -  |
| **484** | InvalidOriginAccessControl |  -  |
| **485** | InvalidIfMatchVersion |  -  |
| **486** | NoSuchDistribution |  -  |
| **487** | PreconditionFailed |  -  |
| **488** | AccessDenied |  -  |
| **489** | TooManyTrustedSigners |  -  |
| **490** | TrustedSignerDoesNotExist |  -  |
| **491** | InvalidViewerCertificate |  -  |
| **492** | InvalidMinimumProtocolVersion |  -  |
| **493** | MissingBody |  -  |
| **494** | TooManyDistributionCNAMEs |  -  |
| **495** | TooManyDistributions |  -  |
| **496** | InvalidDefaultRootObject |  -  |
| **497** | InvalidRelativePath |  -  |
| **498** | InvalidErrorCode |  -  |
| **499** | InvalidResponseCode |  -  |
| **500** | InvalidArgument |  -  |
| **501** | InvalidRequiredProtocol |  -  |
| **502** | NoSuchOrigin |  -  |
| **503** | TooManyOrigins |  -  |
| **504** | TooManyOriginGroupsPerDistribution |  -  |
| **505** | TooManyCacheBehaviors |  -  |
| **506** | TooManyCookieNamesInWhiteList |  -  |
| **507** | InvalidForwardCookies |  -  |
| **508** | TooManyHeadersInForwardedValues |  -  |
| **509** | InvalidHeadersForS3Origin |  -  |
| **510** | InconsistentQuantities |  -  |
| **511** | TooManyCertificates |  -  |
| **512** | InvalidLocationCode |  -  |
| **513** | InvalidGeoRestrictionParameter |  -  |
| **514** | InvalidProtocolSettings |  -  |
| **515** | InvalidTTLOrder |  -  |
| **516** | InvalidWebACLId |  -  |
| **517** | TooManyOriginCustomHeaders |  -  |
| **518** | TooManyQueryStringParameters |  -  |
| **519** | InvalidQueryStringParameters |  -  |
| **520** | TooManyDistributionsWithLambdaAssociations |  -  |
| **521** | TooManyDistributionsWithSingleFunctionARN |  -  |
| **522** | TooManyLambdaFunctionAssociations |  -  |
| **523** | InvalidLambdaFunctionAssociation |  -  |
| **524** | TooManyDistributionsWithFunctionAssociations |  -  |
| **525** | TooManyFunctionAssociations |  -  |
| **526** | InvalidFunctionAssociation |  -  |
| **527** | InvalidOriginReadTimeout |  -  |
| **528** | InvalidOriginKeepaliveTimeout |  -  |
| **529** | NoSuchFieldLevelEncryptionConfig |  -  |
| **530** | IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior |  -  |
| **531** | TooManyDistributionsAssociatedToFieldLevelEncryptionConfig |  -  |
| **532** | NoSuchCachePolicy |  -  |
| **533** | TooManyDistributionsAssociatedToCachePolicy |  -  |
| **534** | TooManyDistributionsAssociatedToOriginAccessControl |  -  |
| **535** | NoSuchResponseHeadersPolicy |  -  |
| **536** | TooManyDistributionsAssociatedToResponseHeadersPolicy |  -  |
| **537** | NoSuchOriginRequestPolicy |  -  |
| **538** | TooManyDistributionsAssociatedToOriginRequestPolicy |  -  |
| **539** | TooManyDistributionsAssociatedToKeyGroup |  -  |
| **540** | TooManyKeyGroupsAssociatedToDistribution |  -  |
| **541** | TrustedKeyGroupDoesNotExist |  -  |
| **542** | NoSuchRealtimeLogConfig |  -  |
| **543** | RealtimeLogConfigOwnerMismatch |  -  |

<a id="createCachePolicy20200531"></a>
# **createCachePolicy20200531**
> CreateCachePolicyResult createCachePolicy20200531(createCachePolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a cache policy.&lt;/p&gt; &lt;p&gt;After you create a cache policy, you can attach it to one or more cache behaviors. When it&#39;s attached to a cache behavior, the cache policy determines the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The values that CloudFront includes in the &lt;i&gt;cache key&lt;/i&gt;. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can&#39;t find an object in its cache that matches the request&#39;s cache key. If you want to send values to the origin but &lt;i&gt;not&lt;/i&gt; include them in the cache key, use &lt;code&gt;OriginRequestPolicy&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about cache policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html\&quot;&gt;Controlling the cache key&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateCachePolicy20200531Request createCachePolicy20200531Request = new CreateCachePolicy20200531Request(); // CreateCachePolicy20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateCachePolicyResult result = apiInstance.createCachePolicy20200531(createCachePolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createCachePolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCachePolicy20200531Request** | [**CreateCachePolicy20200531Request**](CreateCachePolicy20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateCachePolicyResult**](CreateCachePolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InconsistentQuantities |  -  |
| **482** | InvalidArgument |  -  |
| **483** | CachePolicyAlreadyExists |  -  |
| **484** | TooManyCachePolicies |  -  |
| **485** | TooManyHeadersInCachePolicy |  -  |
| **486** | TooManyCookiesInCachePolicy |  -  |
| **487** | TooManyQueryStringsInCachePolicy |  -  |

<a id="createCloudFrontOriginAccessIdentity20200531"></a>
# **createCloudFrontOriginAccessIdentity20200531**
> CreateCloudFrontOriginAccessIdentityResult createCloudFrontOriginAccessIdentity20200531(createCloudFrontOriginAccessIdentity20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a new origin access identity. If you&#39;re using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving Private Content through CloudFront&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateCloudFrontOriginAccessIdentity20200531Request createCloudFrontOriginAccessIdentity20200531Request = new CreateCloudFrontOriginAccessIdentity20200531Request(); // CreateCloudFrontOriginAccessIdentity20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateCloudFrontOriginAccessIdentityResult result = apiInstance.createCloudFrontOriginAccessIdentity20200531(createCloudFrontOriginAccessIdentity20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createCloudFrontOriginAccessIdentity20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCloudFrontOriginAccessIdentity20200531Request** | [**CreateCloudFrontOriginAccessIdentity20200531Request**](CreateCloudFrontOriginAccessIdentity20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateCloudFrontOriginAccessIdentityResult**](CreateCloudFrontOriginAccessIdentityResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | CloudFrontOriginAccessIdentityAlreadyExists |  -  |
| **481** | MissingBody |  -  |
| **482** | TooManyCloudFrontOriginAccessIdentities |  -  |
| **483** | InvalidArgument |  -  |
| **484** | InconsistentQuantities |  -  |

<a id="createContinuousDeploymentPolicy20200531"></a>
# **createContinuousDeploymentPolicy20200531**
> CreateContinuousDeploymentPolicyResult createContinuousDeploymentPolicy20200531(createContinuousDeploymentPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a continuous deployment policy that distributes traffic for a custom domain name to two different CloudFront distributions.&lt;/p&gt; &lt;p&gt;To use a continuous deployment policy, first use &lt;code&gt;CopyDistribution&lt;/code&gt; to create a staging distribution, then use &lt;code&gt;UpdateDistribution&lt;/code&gt; to modify the staging distribution&#39;s configuration.&lt;/p&gt; &lt;p&gt;After you create and update a staging distribution, you can use a continuous deployment policy to incrementally move traffic to the staging distribution. This workflow enables you to test changes to a distribution&#39;s configuration before moving all of your domain&#39;s production traffic to the new configuration.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateContinuousDeploymentPolicy20200531Request createContinuousDeploymentPolicy20200531Request = new CreateContinuousDeploymentPolicy20200531Request(); // CreateContinuousDeploymentPolicy20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateContinuousDeploymentPolicyResult result = apiInstance.createContinuousDeploymentPolicy20200531(createContinuousDeploymentPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createContinuousDeploymentPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createContinuousDeploymentPolicy20200531Request** | [**CreateContinuousDeploymentPolicy20200531Request**](CreateContinuousDeploymentPolicy20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateContinuousDeploymentPolicyResult**](CreateContinuousDeploymentPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidArgument |  -  |
| **482** | InconsistentQuantities |  -  |
| **483** | ContinuousDeploymentPolicyAlreadyExists |  -  |
| **484** | TooManyContinuousDeploymentPolicies |  -  |
| **485** | StagingDistributionInUse |  -  |

<a id="createDistribution20200531"></a>
# **createDistribution20200531**
> CreateDistributionResult createDistribution20200531(createDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a CloudFront distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateDistribution20200531Request createDistribution20200531Request = new CreateDistribution20200531Request(); // CreateDistribution20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDistributionResult result = apiInstance.createDistribution20200531(createDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createDistribution20200531Request** | [**CreateDistribution20200531Request**](CreateDistribution20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateDistributionResult**](CreateDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | CNAMEAlreadyExists |  -  |
| **481** | DistributionAlreadyExists |  -  |
| **482** | InvalidOrigin |  -  |
| **483** | InvalidOriginAccessIdentity |  -  |
| **484** | InvalidOriginAccessControl |  -  |
| **485** | IllegalOriginAccessConfiguration |  -  |
| **486** | TooManyDistributionsAssociatedToOriginAccessControl |  -  |
| **487** | AccessDenied |  -  |
| **488** | TooManyTrustedSigners |  -  |
| **489** | TrustedSignerDoesNotExist |  -  |
| **490** | InvalidViewerCertificate |  -  |
| **491** | InvalidMinimumProtocolVersion |  -  |
| **492** | MissingBody |  -  |
| **493** | TooManyDistributionCNAMEs |  -  |
| **494** | TooManyDistributions |  -  |
| **495** | InvalidDefaultRootObject |  -  |
| **496** | InvalidRelativePath |  -  |
| **497** | InvalidErrorCode |  -  |
| **498** | InvalidResponseCode |  -  |
| **499** | InvalidArgument |  -  |
| **500** | InvalidRequiredProtocol |  -  |
| **501** | NoSuchOrigin |  -  |
| **502** | TooManyOrigins |  -  |
| **503** | TooManyOriginGroupsPerDistribution |  -  |
| **504** | TooManyCacheBehaviors |  -  |
| **505** | TooManyCookieNamesInWhiteList |  -  |
| **506** | InvalidForwardCookies |  -  |
| **507** | TooManyHeadersInForwardedValues |  -  |
| **508** | InvalidHeadersForS3Origin |  -  |
| **509** | InconsistentQuantities |  -  |
| **510** | TooManyCertificates |  -  |
| **511** | InvalidLocationCode |  -  |
| **512** | InvalidGeoRestrictionParameter |  -  |
| **513** | InvalidProtocolSettings |  -  |
| **514** | InvalidTTLOrder |  -  |
| **515** | InvalidWebACLId |  -  |
| **516** | TooManyOriginCustomHeaders |  -  |
| **517** | TooManyQueryStringParameters |  -  |
| **518** | InvalidQueryStringParameters |  -  |
| **519** | TooManyDistributionsWithLambdaAssociations |  -  |
| **520** | TooManyDistributionsWithSingleFunctionARN |  -  |
| **521** | TooManyLambdaFunctionAssociations |  -  |
| **522** | InvalidLambdaFunctionAssociation |  -  |
| **523** | TooManyDistributionsWithFunctionAssociations |  -  |
| **524** | TooManyFunctionAssociations |  -  |
| **525** | InvalidFunctionAssociation |  -  |
| **526** | InvalidOriginReadTimeout |  -  |
| **527** | InvalidOriginKeepaliveTimeout |  -  |
| **528** | NoSuchFieldLevelEncryptionConfig |  -  |
| **529** | IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior |  -  |
| **530** | TooManyDistributionsAssociatedToFieldLevelEncryptionConfig |  -  |
| **531** | NoSuchCachePolicy |  -  |
| **532** | TooManyDistributionsAssociatedToCachePolicy |  -  |
| **533** | NoSuchResponseHeadersPolicy |  -  |
| **534** | TooManyDistributionsAssociatedToResponseHeadersPolicy |  -  |
| **535** | NoSuchOriginRequestPolicy |  -  |
| **536** | TooManyDistributionsAssociatedToOriginRequestPolicy |  -  |
| **537** | TooManyDistributionsAssociatedToKeyGroup |  -  |
| **538** | TooManyKeyGroupsAssociatedToDistribution |  -  |
| **539** | TrustedKeyGroupDoesNotExist |  -  |
| **540** | NoSuchRealtimeLogConfig |  -  |
| **541** | RealtimeLogConfigOwnerMismatch |  -  |
| **542** | ContinuousDeploymentPolicyInUse |  -  |
| **543** | NoSuchContinuousDeploymentPolicy |  -  |
| **544** | InvalidDomainNameForOriginAccessControl |  -  |

<a id="createDistributionWithTags20200531"></a>
# **createDistributionWithTags20200531**
> CreateDistributionWithTagsResult createDistributionWithTags20200531(withTags, createDistributionWithTags20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Create a new distribution with tags. This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html\&quot;&gt;CreateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean withTags = true; // Boolean | 
    CreateDistributionWithTags20200531Request createDistributionWithTags20200531Request = new CreateDistributionWithTags20200531Request(); // CreateDistributionWithTags20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDistributionWithTagsResult result = apiInstance.createDistributionWithTags20200531(withTags, createDistributionWithTags20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDistributionWithTags20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **withTags** | **Boolean**|  | |
| **createDistributionWithTags20200531Request** | [**CreateDistributionWithTags20200531Request**](CreateDistributionWithTags20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateDistributionWithTagsResult**](CreateDistributionWithTagsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | CNAMEAlreadyExists |  -  |
| **481** | DistributionAlreadyExists |  -  |
| **482** | InvalidOrigin |  -  |
| **483** | InvalidOriginAccessIdentity |  -  |
| **484** | InvalidOriginAccessControl |  -  |
| **485** | IllegalOriginAccessConfiguration |  -  |
| **486** | AccessDenied |  -  |
| **487** | TooManyTrustedSigners |  -  |
| **488** | TrustedSignerDoesNotExist |  -  |
| **489** | InvalidViewerCertificate |  -  |
| **490** | InvalidMinimumProtocolVersion |  -  |
| **491** | MissingBody |  -  |
| **492** | TooManyDistributionCNAMEs |  -  |
| **493** | TooManyDistributions |  -  |
| **494** | InvalidDefaultRootObject |  -  |
| **495** | InvalidRelativePath |  -  |
| **496** | InvalidErrorCode |  -  |
| **497** | InvalidResponseCode |  -  |
| **498** | InvalidArgument |  -  |
| **499** | InvalidRequiredProtocol |  -  |
| **500** | NoSuchOrigin |  -  |
| **501** | TooManyOrigins |  -  |
| **502** | TooManyOriginGroupsPerDistribution |  -  |
| **503** | TooManyCacheBehaviors |  -  |
| **504** | TooManyCookieNamesInWhiteList |  -  |
| **505** | InvalidForwardCookies |  -  |
| **506** | TooManyHeadersInForwardedValues |  -  |
| **507** | InvalidHeadersForS3Origin |  -  |
| **508** | InconsistentQuantities |  -  |
| **509** | TooManyCertificates |  -  |
| **510** | InvalidLocationCode |  -  |
| **511** | InvalidGeoRestrictionParameter |  -  |
| **512** | InvalidProtocolSettings |  -  |
| **513** | InvalidTTLOrder |  -  |
| **514** | InvalidWebACLId |  -  |
| **515** | TooManyOriginCustomHeaders |  -  |
| **516** | InvalidTagging |  -  |
| **517** | TooManyQueryStringParameters |  -  |
| **518** | InvalidQueryStringParameters |  -  |
| **519** | TooManyDistributionsWithLambdaAssociations |  -  |
| **520** | TooManyDistributionsWithSingleFunctionARN |  -  |
| **521** | TooManyLambdaFunctionAssociations |  -  |
| **522** | InvalidLambdaFunctionAssociation |  -  |
| **523** | TooManyDistributionsWithFunctionAssociations |  -  |
| **524** | TooManyFunctionAssociations |  -  |
| **525** | InvalidFunctionAssociation |  -  |
| **526** | InvalidOriginReadTimeout |  -  |
| **527** | InvalidOriginKeepaliveTimeout |  -  |
| **528** | NoSuchFieldLevelEncryptionConfig |  -  |
| **529** | IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior |  -  |
| **530** | TooManyDistributionsAssociatedToFieldLevelEncryptionConfig |  -  |
| **531** | NoSuchCachePolicy |  -  |
| **532** | TooManyDistributionsAssociatedToCachePolicy |  -  |
| **533** | TooManyDistributionsAssociatedToOriginAccessControl |  -  |
| **534** | NoSuchResponseHeadersPolicy |  -  |
| **535** | TooManyDistributionsAssociatedToResponseHeadersPolicy |  -  |
| **536** | NoSuchOriginRequestPolicy |  -  |
| **537** | TooManyDistributionsAssociatedToOriginRequestPolicy |  -  |
| **538** | TooManyDistributionsAssociatedToKeyGroup |  -  |
| **539** | TooManyKeyGroupsAssociatedToDistribution |  -  |
| **540** | TrustedKeyGroupDoesNotExist |  -  |
| **541** | NoSuchRealtimeLogConfig |  -  |
| **542** | RealtimeLogConfigOwnerMismatch |  -  |
| **543** | ContinuousDeploymentPolicyInUse |  -  |
| **544** | NoSuchContinuousDeploymentPolicy |  -  |
| **545** | InvalidDomainNameForOriginAccessControl |  -  |

<a id="createFieldLevelEncryptionConfig20200531"></a>
# **createFieldLevelEncryptionConfig20200531**
> CreateFieldLevelEncryptionConfigResult createFieldLevelEncryptionConfig20200531(createFieldLevelEncryptionConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Create a new field-level encryption configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateFieldLevelEncryptionConfig20200531Request createFieldLevelEncryptionConfig20200531Request = new CreateFieldLevelEncryptionConfig20200531Request(); // CreateFieldLevelEncryptionConfig20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateFieldLevelEncryptionConfigResult result = apiInstance.createFieldLevelEncryptionConfig20200531(createFieldLevelEncryptionConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createFieldLevelEncryptionConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createFieldLevelEncryptionConfig20200531Request** | [**CreateFieldLevelEncryptionConfig20200531Request**](CreateFieldLevelEncryptionConfig20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateFieldLevelEncryptionConfigResult**](CreateFieldLevelEncryptionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InconsistentQuantities |  -  |
| **481** | InvalidArgument |  -  |
| **482** | NoSuchFieldLevelEncryptionProfile |  -  |
| **483** | FieldLevelEncryptionConfigAlreadyExists |  -  |
| **484** | TooManyFieldLevelEncryptionConfigs |  -  |
| **485** | TooManyFieldLevelEncryptionQueryArgProfiles |  -  |
| **486** | TooManyFieldLevelEncryptionContentTypeProfiles |  -  |
| **487** | QueryArgProfileEmpty |  -  |

<a id="createFieldLevelEncryptionProfile20200531"></a>
# **createFieldLevelEncryptionProfile20200531**
> CreateFieldLevelEncryptionProfileResult createFieldLevelEncryptionProfile20200531(createFieldLevelEncryptionProfile20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Create a field-level encryption profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateFieldLevelEncryptionProfile20200531Request createFieldLevelEncryptionProfile20200531Request = new CreateFieldLevelEncryptionProfile20200531Request(); // CreateFieldLevelEncryptionProfile20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateFieldLevelEncryptionProfileResult result = apiInstance.createFieldLevelEncryptionProfile20200531(createFieldLevelEncryptionProfile20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createFieldLevelEncryptionProfile20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createFieldLevelEncryptionProfile20200531Request** | [**CreateFieldLevelEncryptionProfile20200531Request**](CreateFieldLevelEncryptionProfile20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateFieldLevelEncryptionProfileResult**](CreateFieldLevelEncryptionProfileResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InconsistentQuantities |  -  |
| **481** | InvalidArgument |  -  |
| **482** | NoSuchPublicKey |  -  |
| **483** | FieldLevelEncryptionProfileAlreadyExists |  -  |
| **484** | FieldLevelEncryptionProfileSizeExceeded |  -  |
| **485** | TooManyFieldLevelEncryptionProfiles |  -  |
| **486** | TooManyFieldLevelEncryptionEncryptionEntities |  -  |
| **487** | TooManyFieldLevelEncryptionFieldPatterns |  -  |

<a id="createFunction20200531"></a>
# **createFunction20200531**
> CreateFunctionResult createFunction20200531(createFunction20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a CloudFront function.&lt;/p&gt; &lt;p&gt;To create a function, you provide the function code and some configuration information about the function. The response contains an Amazon Resource Name (ARN) that uniquely identifies the function.&lt;/p&gt; &lt;p&gt;When you create a function, it&#39;s in the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage. In this stage, you can test the function with &lt;code&gt;TestFunction&lt;/code&gt;, and update it with &lt;code&gt;UpdateFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When you&#39;re ready to use your function with a CloudFront distribution, use &lt;code&gt;PublishFunction&lt;/code&gt; to copy the function from the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage to &lt;code&gt;LIVE&lt;/code&gt;. When it&#39;s live, you can attach the function to a distribution&#39;s cache behavior, using the function&#39;s ARN.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateFunction20200531Request createFunction20200531Request = new CreateFunction20200531Request(); // CreateFunction20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateFunctionResult result = apiInstance.createFunction20200531(createFunction20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createFunction20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createFunction20200531Request** | [**CreateFunction20200531Request**](CreateFunction20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateFunctionResult**](CreateFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | TooManyFunctions |  -  |
| **481** | FunctionAlreadyExists |  -  |
| **482** | FunctionSizeLimitExceeded |  -  |
| **483** | InvalidArgument |  -  |
| **484** | UnsupportedOperation |  -  |

<a id="createInvalidation20200531"></a>
# **createInvalidation20200531**
> CreateInvalidationResult createInvalidation20200531(distributionId, createInvalidation20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Create a new invalidation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String distributionId = "distributionId_example"; // String | The distribution's id.
    CreateInvalidation20200531Request createInvalidation20200531Request = new CreateInvalidation20200531Request(); // CreateInvalidation20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateInvalidationResult result = apiInstance.createInvalidation20200531(distributionId, createInvalidation20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createInvalidation20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionId** | **String**| The distribution&#39;s id. | |
| **createInvalidation20200531Request** | [**CreateInvalidation20200531Request**](CreateInvalidation20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateInvalidationResult**](CreateInvalidationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | MissingBody |  -  |
| **482** | InvalidArgument |  -  |
| **483** | NoSuchDistribution |  -  |
| **484** | BatchTooLarge |  -  |
| **485** | TooManyInvalidationsInProgress |  -  |
| **486** | InconsistentQuantities |  -  |

<a id="createKeyGroup20200531"></a>
# **createKeyGroup20200531**
> CreateKeyGroupResult createKeyGroup20200531(createKeyGroup20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a key group that you can use with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;CloudFront signed URLs and signed cookies&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To create a key group, you must specify at least one public key for the key group. After you create a key group, you can reference it from one or more cache behaviors. When you reference a key group in a cache behavior, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving private content&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateKeyGroup20200531Request createKeyGroup20200531Request = new CreateKeyGroup20200531Request(); // CreateKeyGroup20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateKeyGroupResult result = apiInstance.createKeyGroup20200531(createKeyGroup20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createKeyGroup20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createKeyGroup20200531Request** | [**CreateKeyGroup20200531Request**](CreateKeyGroup20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateKeyGroupResult**](CreateKeyGroupResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | KeyGroupAlreadyExists |  -  |
| **482** | TooManyKeyGroups |  -  |
| **483** | TooManyPublicKeysInKeyGroup |  -  |

<a id="createMonitoringSubscription20200531"></a>
# **createMonitoringSubscription20200531**
> CreateMonitoringSubscriptionResult createMonitoringSubscription20200531(distributionId, createMonitoringSubscription20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Enables additional CloudWatch metrics for the specified CloudFront distribution. The additional metrics incur an additional cost.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html#monitoring-console.distributions-additional\&quot;&gt;Viewing additional CloudFront distribution metrics&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String distributionId = "distributionId_example"; // String | The ID of the distribution that you are enabling metrics for.
    CreateMonitoringSubscription20200531Request createMonitoringSubscription20200531Request = new CreateMonitoringSubscription20200531Request(); // CreateMonitoringSubscription20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateMonitoringSubscriptionResult result = apiInstance.createMonitoringSubscription20200531(distributionId, createMonitoringSubscription20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createMonitoringSubscription20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionId** | **String**| The ID of the distribution that you are enabling metrics for. | |
| **createMonitoringSubscription20200531Request** | [**CreateMonitoringSubscription20200531Request**](CreateMonitoringSubscription20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateMonitoringSubscriptionResult**](CreateMonitoringSubscriptionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchDistribution |  -  |
| **482** | MonitoringSubscriptionAlreadyExists |  -  |
| **483** | UnsupportedOperation |  -  |

<a id="createOriginAccessControl20200531"></a>
# **createOriginAccessControl20200531**
> CreateOriginAccessControlResult createOriginAccessControl20200531(createOriginAccessControl20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new origin access control in CloudFront. After you create an origin access control, you can add it to an origin in a CloudFront distribution so that CloudFront sends authenticated (signed) requests to the origin.&lt;/p&gt; &lt;p&gt;This makes it possible to block public access to the origin, allowing viewers (users) to access the origin&#39;s content only through CloudFront.&lt;/p&gt; &lt;p&gt;For more information about using a CloudFront origin access control, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html\&quot;&gt;Restricting access to an Amazon Web Services origin&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateOriginAccessControl20200531Request createOriginAccessControl20200531Request = new CreateOriginAccessControl20200531Request(); // CreateOriginAccessControl20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateOriginAccessControlResult result = apiInstance.createOriginAccessControl20200531(createOriginAccessControl20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createOriginAccessControl20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createOriginAccessControl20200531Request** | [**CreateOriginAccessControl20200531Request**](CreateOriginAccessControl20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateOriginAccessControlResult**](CreateOriginAccessControlResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | OriginAccessControlAlreadyExists |  -  |
| **481** | TooManyOriginAccessControls |  -  |
| **482** | InvalidArgument |  -  |

<a id="createOriginRequestPolicy20200531"></a>
# **createOriginRequestPolicy20200531**
> CreateOriginRequestPolicyResult createOriginRequestPolicy20200531(createOriginRequestPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an origin request policy.&lt;/p&gt; &lt;p&gt;After you create an origin request policy, you can attach it to one or more cache behaviors. When it&#39;s attached to a cache behavior, the origin request policy determines the values that CloudFront includes in requests that it sends to the origin. Each request that CloudFront sends to the origin includes the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The request body and the URL path (without the domain name) from the viewer request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The headers that CloudFront automatically includes in every origin request, including &lt;code&gt;Host&lt;/code&gt;, &lt;code&gt;User-Agent&lt;/code&gt;, and &lt;code&gt;X-Amz-Cf-Id&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All HTTP headers, cookies, and URL query strings that are specified in the cache policy or the origin request policy. These can include items from the viewer request and, in the case of headers, additional ones that are added by CloudFront.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;CloudFront sends a request when it can&#39;t find a valid object in its cache that matches the request. If you want to send values to the origin and also include them in the cache key, use &lt;code&gt;CachePolicy&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about origin request policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html\&quot;&gt;Controlling origin requests&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateOriginRequestPolicy20200531Request createOriginRequestPolicy20200531Request = new CreateOriginRequestPolicy20200531Request(); // CreateOriginRequestPolicy20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateOriginRequestPolicyResult result = apiInstance.createOriginRequestPolicy20200531(createOriginRequestPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createOriginRequestPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createOriginRequestPolicy20200531Request** | [**CreateOriginRequestPolicy20200531Request**](CreateOriginRequestPolicy20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateOriginRequestPolicyResult**](CreateOriginRequestPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InconsistentQuantities |  -  |
| **482** | InvalidArgument |  -  |
| **483** | OriginRequestPolicyAlreadyExists |  -  |
| **484** | TooManyOriginRequestPolicies |  -  |
| **485** | TooManyHeadersInOriginRequestPolicy |  -  |
| **486** | TooManyCookiesInOriginRequestPolicy |  -  |
| **487** | TooManyQueryStringsInOriginRequestPolicy |  -  |

<a id="createPublicKey20200531"></a>
# **createPublicKey20200531**
> CreatePublicKeyResult createPublicKey20200531(createPublicKey20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Uploads a public key to CloudFront that you can use with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;signed URLs and signed cookies&lt;/a&gt;, or with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html\&quot;&gt;field-level encryption&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreatePublicKey20200531Request createPublicKey20200531Request = new CreatePublicKey20200531Request(); // CreatePublicKey20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreatePublicKeyResult result = apiInstance.createPublicKey20200531(createPublicKey20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createPublicKey20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createPublicKey20200531Request** | [**CreatePublicKey20200531Request**](CreatePublicKey20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreatePublicKeyResult**](CreatePublicKeyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | PublicKeyAlreadyExists |  -  |
| **481** | InvalidArgument |  -  |
| **482** | TooManyPublicKeys |  -  |

<a id="createRealtimeLogConfig20200531"></a>
# **createRealtimeLogConfig20200531**
> CreateRealtimeLogConfigResult createRealtimeLogConfig20200531(createRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a real-time log configuration.&lt;/p&gt; &lt;p&gt;After you create a real-time log configuration, you can attach it to one or more cache behaviors to send real-time log data to the specified Amazon Kinesis data stream.&lt;/p&gt; &lt;p&gt;For more information about real-time log configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html\&quot;&gt;Real-time logs&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateRealtimeLogConfig20200531Request createRealtimeLogConfig20200531Request = new CreateRealtimeLogConfig20200531Request(); // CreateRealtimeLogConfig20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateRealtimeLogConfigResult result = apiInstance.createRealtimeLogConfig20200531(createRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createRealtimeLogConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createRealtimeLogConfig20200531Request** | [**CreateRealtimeLogConfig20200531Request**](CreateRealtimeLogConfig20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateRealtimeLogConfigResult**](CreateRealtimeLogConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | RealtimeLogConfigAlreadyExists |  -  |
| **481** | TooManyRealtimeLogConfigs |  -  |
| **482** | InvalidArgument |  -  |
| **483** | AccessDenied |  -  |

<a id="createResponseHeadersPolicy20200531"></a>
# **createResponseHeadersPolicy20200531**
> CreateResponseHeadersPolicyResult createResponseHeadersPolicy20200531(createResponseHeadersPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a response headers policy.&lt;/p&gt; &lt;p&gt;A response headers policy contains information about a set of HTTP headers. To create a response headers policy, you provide some metadata about the policy and a set of configurations that specify the headers.&lt;/p&gt; &lt;p&gt;After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it&#39;s attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html\&quot;&gt;Adding or removing HTTP headers in CloudFront responses&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateResponseHeadersPolicy20200531Request createResponseHeadersPolicy20200531Request = new CreateResponseHeadersPolicy20200531Request(); // CreateResponseHeadersPolicy20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateResponseHeadersPolicyResult result = apiInstance.createResponseHeadersPolicy20200531(createResponseHeadersPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createResponseHeadersPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createResponseHeadersPolicy20200531Request** | [**CreateResponseHeadersPolicy20200531Request**](CreateResponseHeadersPolicy20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateResponseHeadersPolicyResult**](CreateResponseHeadersPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InconsistentQuantities |  -  |
| **482** | InvalidArgument |  -  |
| **483** | ResponseHeadersPolicyAlreadyExists |  -  |
| **484** | TooManyResponseHeadersPolicies |  -  |
| **485** | TooManyCustomHeadersInResponseHeadersPolicy |  -  |
| **486** | TooLongCSPInResponseHeadersPolicy |  -  |
| **487** | TooManyRemoveHeadersInResponseHeadersPolicy |  -  |

<a id="createStreamingDistribution20200531"></a>
# **createStreamingDistribution20200531**
> CreateStreamingDistributionResult createStreamingDistribution20200531(createStreamingDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/ann.jspa?annID&#x3D;7356\&quot;&gt;read the announcement&lt;/a&gt; on the Amazon CloudFront discussion forum.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateStreamingDistribution20200531Request createStreamingDistribution20200531Request = new CreateStreamingDistribution20200531Request(); // CreateStreamingDistribution20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateStreamingDistributionResult result = apiInstance.createStreamingDistribution20200531(createStreamingDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createStreamingDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createStreamingDistribution20200531Request** | [**CreateStreamingDistribution20200531Request**](CreateStreamingDistribution20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateStreamingDistributionResult**](CreateStreamingDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | CNAMEAlreadyExists |  -  |
| **481** | StreamingDistributionAlreadyExists |  -  |
| **482** | InvalidOrigin |  -  |
| **483** | InvalidOriginAccessIdentity |  -  |
| **484** | InvalidOriginAccessControl |  -  |
| **485** | AccessDenied |  -  |
| **486** | TooManyTrustedSigners |  -  |
| **487** | TrustedSignerDoesNotExist |  -  |
| **488** | MissingBody |  -  |
| **489** | TooManyStreamingDistributionCNAMEs |  -  |
| **490** | TooManyStreamingDistributions |  -  |
| **491** | InvalidArgument |  -  |
| **492** | InconsistentQuantities |  -  |

<a id="createStreamingDistributionWithTags20200531"></a>
# **createStreamingDistributionWithTags20200531**
> CreateStreamingDistributionWithTagsResult createStreamingDistributionWithTags20200531(withTags, createStreamingDistributionWithTags20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/ann.jspa?annID&#x3D;7356\&quot;&gt;read the announcement&lt;/a&gt; on the Amazon CloudFront discussion forum.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean withTags = true; // Boolean | 
    CreateStreamingDistributionWithTags20200531Request createStreamingDistributionWithTags20200531Request = new CreateStreamingDistributionWithTags20200531Request(); // CreateStreamingDistributionWithTags20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateStreamingDistributionWithTagsResult result = apiInstance.createStreamingDistributionWithTags20200531(withTags, createStreamingDistributionWithTags20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createStreamingDistributionWithTags20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **withTags** | **Boolean**|  | |
| **createStreamingDistributionWithTags20200531Request** | [**CreateStreamingDistributionWithTags20200531Request**](CreateStreamingDistributionWithTags20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateStreamingDistributionWithTagsResult**](CreateStreamingDistributionWithTagsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | CNAMEAlreadyExists |  -  |
| **481** | StreamingDistributionAlreadyExists |  -  |
| **482** | InvalidOrigin |  -  |
| **483** | InvalidOriginAccessIdentity |  -  |
| **484** | InvalidOriginAccessControl |  -  |
| **485** | AccessDenied |  -  |
| **486** | TooManyTrustedSigners |  -  |
| **487** | TrustedSignerDoesNotExist |  -  |
| **488** | MissingBody |  -  |
| **489** | TooManyStreamingDistributionCNAMEs |  -  |
| **490** | TooManyStreamingDistributions |  -  |
| **491** | InvalidArgument |  -  |
| **492** | InconsistentQuantities |  -  |
| **493** | InvalidTagging |  -  |

<a id="deleteCachePolicy20200531"></a>
# **deleteCachePolicy20200531**
> deleteCachePolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Deletes a cache policy.&lt;/p&gt; &lt;p&gt;You cannot delete a cache policy if it&#39;s attached to a cache behavior. First update your distributions to remove the cache policy from all cache behaviors, then delete the cache policy.&lt;/p&gt; &lt;p&gt;To delete a cache policy, you must provide the policy&#39;s identifier and version. To get these values, you can use &lt;code&gt;ListCachePolicies&lt;/code&gt; or &lt;code&gt;GetCachePolicy&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier for the cache policy that you are deleting. To get the identifier, you can use <code>ListCachePolicies</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The version of the cache policy that you are deleting. The version is the cache policy's <code>ETag</code> value, which you can get using <code>ListCachePolicies</code>, <code>GetCachePolicy</code>, or <code>GetCachePolicyConfig</code>.
    try {
      apiInstance.deleteCachePolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteCachePolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier for the cache policy that you are deleting. To get the identifier, you can use &lt;code&gt;ListCachePolicies&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The version of the cache policy that you are deleting. The version is the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListCachePolicies&lt;/code&gt;, &lt;code&gt;GetCachePolicy&lt;/code&gt;, or &lt;code&gt;GetCachePolicyConfig&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchCachePolicy |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | IllegalDelete |  -  |
| **485** | CachePolicyInUse |  -  |

<a id="deleteCloudFrontOriginAccessIdentity20200531"></a>
# **deleteCloudFrontOriginAccessIdentity20200531**
> deleteCloudFrontOriginAccessIdentity20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Delete an origin access identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The origin access identity's ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header you received from a previous <code>GET</code> or <code>PUT</code> request. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      apiInstance.deleteCloudFrontOriginAccessIdentity20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteCloudFrontOriginAccessIdentity20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The origin access identity&#39;s ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header you received from a previous &lt;code&gt;GET&lt;/code&gt; or &lt;code&gt;PUT&lt;/code&gt; request. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchCloudFrontOriginAccessIdentity |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | CloudFrontOriginAccessIdentityInUse |  -  |

<a id="deleteContinuousDeploymentPolicy20200531"></a>
# **deleteContinuousDeploymentPolicy20200531**
> deleteContinuousDeploymentPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Deletes a continuous deployment policy.&lt;/p&gt; &lt;p&gt;You cannot delete a continuous deployment policy that&#39;s attached to a primary distribution. First update your distribution to remove the continuous deployment policy, then you can delete the policy.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the continuous deployment policy that you are deleting.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the continuous deployment policy that you are deleting.
    try {
      apiInstance.deleteContinuousDeploymentPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteContinuousDeploymentPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the continuous deployment policy that you are deleting. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the continuous deployment policy that you are deleting. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InvalidIfMatchVersion |  -  |
| **481** | InvalidArgument |  -  |
| **482** | AccessDenied |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | ContinuousDeploymentPolicyInUse |  -  |
| **485** | NoSuchContinuousDeploymentPolicy |  -  |

<a id="deleteDistribution20200531"></a>
# **deleteDistribution20200531**
> deleteDistribution20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Delete a distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The distribution ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when you disabled the distribution. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      apiInstance.deleteDistribution20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The distribution ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when you disabled the distribution. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | DistributionNotDisabled |  -  |
| **482** | InvalidIfMatchVersion |  -  |
| **483** | NoSuchDistribution |  -  |
| **484** | PreconditionFailed |  -  |

<a id="deleteFieldLevelEncryptionConfig20200531"></a>
# **deleteFieldLevelEncryptionConfig20200531**
> deleteFieldLevelEncryptionConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Remove a field-level encryption configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the configuration you want to delete from CloudFront.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the configuration identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      apiInstance.deleteFieldLevelEncryptionConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteFieldLevelEncryptionConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the configuration you want to delete from CloudFront. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the configuration identity to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchFieldLevelEncryptionConfig |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | FieldLevelEncryptionConfigInUse |  -  |

<a id="deleteFieldLevelEncryptionProfile20200531"></a>
# **deleteFieldLevelEncryptionProfile20200531**
> deleteFieldLevelEncryptionProfile20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Remove a field-level encryption profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Request the ID of the profile you want to delete from CloudFront.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the profile to delete. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      apiInstance.deleteFieldLevelEncryptionProfile20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteFieldLevelEncryptionProfile20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Request the ID of the profile you want to delete from CloudFront. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the profile to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchFieldLevelEncryptionProfile |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | FieldLevelEncryptionProfileInUse |  -  |

<a id="deleteFunction20200531"></a>
# **deleteFunction20200531**
> deleteFunction20200531(name, ifMatch, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a CloudFront function.&lt;/p&gt; &lt;p&gt;You cannot delete a function if it&#39;s associated with a cache behavior. First, update your distributions to remove the function association from all cache behaviors, then delete the function.&lt;/p&gt; &lt;p&gt;To delete a function, you must provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value). To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the function that you are deleting.
    String ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the function that you are deleting, which you can get using <code>DescribeFunction</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteFunction20200531(name, ifMatch, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteFunction20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the function that you are deleting. | |
| **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are deleting, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InvalidIfMatchVersion |  -  |
| **481** | NoSuchFunctionExists |  -  |
| **482** | FunctionInUse |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | UnsupportedOperation |  -  |

<a id="deleteKeyGroup20200531"></a>
# **deleteKeyGroup20200531**
> deleteKeyGroup20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Deletes a key group.&lt;/p&gt; &lt;p&gt;You cannot delete a key group that is referenced in a cache behavior. First update your distributions to remove the key group from all cache behaviors, then delete the key group.&lt;/p&gt; &lt;p&gt;To delete a key group, you must provide the key group&#39;s identifier and version. To get these values, use &lt;code&gt;ListKeyGroups&lt;/code&gt; followed by &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the key group that you are deleting. To get the identifier, use <code>ListKeyGroups</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The version of the key group that you are deleting. The version is the key group's <code>ETag</code> value. To get the <code>ETag</code>, use <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.
    try {
      apiInstance.deleteKeyGroup20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteKeyGroup20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the key group that you are deleting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The version of the key group that you are deleting. The version is the key group&#39;s &lt;code&gt;ETag&lt;/code&gt; value. To get the &lt;code&gt;ETag&lt;/code&gt;, use &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InvalidIfMatchVersion |  -  |
| **481** | NoSuchResource |  -  |
| **482** | PreconditionFailed |  -  |
| **483** | ResourceInUse |  -  |

<a id="deleteMonitoringSubscription20200531"></a>
# **deleteMonitoringSubscription20200531**
> Object deleteMonitoringSubscription20200531(distributionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disables additional CloudWatch metrics for the specified CloudFront distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String distributionId = "distributionId_example"; // String | The ID of the distribution that you are disabling metrics for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteMonitoringSubscription20200531(distributionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteMonitoringSubscription20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionId** | **String**| The ID of the distribution that you are disabling metrics for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchDistribution |  -  |
| **482** | NoSuchMonitoringSubscription |  -  |
| **483** | UnsupportedOperation |  -  |

<a id="deleteOriginAccessControl20200531"></a>
# **deleteOriginAccessControl20200531**
> deleteOriginAccessControl20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Deletes a CloudFront origin access control.&lt;/p&gt; &lt;p&gt;You cannot delete an origin access control if it&#39;s in use. First, update all distributions to remove the origin access control from all origins, then delete the origin access control.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the origin access control that you are deleting.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the origin access control that you are deleting.
    try {
      apiInstance.deleteOriginAccessControl20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteOriginAccessControl20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier of the origin access control that you are deleting. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the origin access control that you are deleting. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchOriginAccessControl |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | OriginAccessControlInUse |  -  |

<a id="deleteOriginRequestPolicy20200531"></a>
# **deleteOriginRequestPolicy20200531**
> deleteOriginRequestPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Deletes an origin request policy.&lt;/p&gt; &lt;p&gt;You cannot delete an origin request policy if it&#39;s attached to any cache behaviors. First update your distributions to remove the origin request policy from all cache behaviors, then delete the origin request policy.&lt;/p&gt; &lt;p&gt;To delete an origin request policy, you must provide the policy&#39;s identifier and version. To get the identifier, you can use &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt; or &lt;code&gt;GetOriginRequestPolicy&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use <code>ListOriginRequestPolicies</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The version of the origin request policy that you are deleting. The version is the origin request policy's <code>ETag</code> value, which you can get using <code>ListOriginRequestPolicies</code>, <code>GetOriginRequestPolicy</code>, or <code>GetOriginRequestPolicyConfig</code>.
    try {
      apiInstance.deleteOriginRequestPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteOriginRequestPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The version of the origin request policy that you are deleting. The version is the origin request policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;, &lt;code&gt;GetOriginRequestPolicy&lt;/code&gt;, or &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchOriginRequestPolicy |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | IllegalDelete |  -  |
| **485** | OriginRequestPolicyInUse |  -  |

<a id="deletePublicKey20200531"></a>
# **deletePublicKey20200531**
> deletePublicKey20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Remove a public key you previously added to CloudFront.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the public key you want to remove from CloudFront.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the public key identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      apiInstance.deletePublicKey20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePublicKey20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the public key you want to remove from CloudFront. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the public key identity to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | PublicKeyInUse |  -  |
| **482** | InvalidIfMatchVersion |  -  |
| **483** | NoSuchPublicKey |  -  |
| **484** | PreconditionFailed |  -  |

<a id="deleteRealtimeLogConfig20200531"></a>
# **deleteRealtimeLogConfig20200531**
> deleteRealtimeLogConfig20200531(deleteRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a real-time log configuration.&lt;/p&gt; &lt;p&gt;You cannot delete a real-time log configuration if it&#39;s attached to a cache behavior. First update your distributions to remove the real-time log configuration from all cache behaviors, then delete the real-time log configuration.&lt;/p&gt; &lt;p&gt;To delete a real-time log configuration, you can provide the configuration&#39;s name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to delete.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    DeleteRealtimeLogConfig20200531Request deleteRealtimeLogConfig20200531Request = new DeleteRealtimeLogConfig20200531Request(); // DeleteRealtimeLogConfig20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteRealtimeLogConfig20200531(deleteRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRealtimeLogConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **deleteRealtimeLogConfig20200531Request** | [**DeleteRealtimeLogConfig20200531Request**](DeleteRealtimeLogConfig20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | NoSuchRealtimeLogConfig |  -  |
| **481** | RealtimeLogConfigInUse |  -  |
| **482** | InvalidArgument |  -  |
| **483** | AccessDenied |  -  |

<a id="deleteResponseHeadersPolicy20200531"></a>
# **deleteResponseHeadersPolicy20200531**
> deleteResponseHeadersPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Deletes a response headers policy.&lt;/p&gt; &lt;p&gt;You cannot delete a response headers policy if it&#39;s attached to a cache behavior. First update your distributions to remove the response headers policy from all cache behaviors, then delete the response headers policy.&lt;/p&gt; &lt;p&gt;To delete a response headers policy, you must provide the policy&#39;s identifier and version. To get these values, you can use &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt; or &lt;code&gt;GetResponseHeadersPolicy&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | <p>The identifier for the response headers policy that you are deleting.</p> <p>To get the identifier, you can use <code>ListResponseHeadersPolicies</code>.</p>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | <p>The version of the response headers policy that you are deleting.</p> <p>The version is the response headers policy's <code>ETag</code> value, which you can get using <code>ListResponseHeadersPolicies</code>, <code>GetResponseHeadersPolicy</code>, or <code>GetResponseHeadersPolicyConfig</code>.</p>
    try {
      apiInstance.deleteResponseHeadersPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteResponseHeadersPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| &lt;p&gt;The identifier for the response headers policy that you are deleting.&lt;/p&gt; &lt;p&gt;To get the identifier, you can use &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt; | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| &lt;p&gt;The version of the response headers policy that you are deleting.&lt;/p&gt; &lt;p&gt;The version is the response headers policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;, &lt;code&gt;GetResponseHeadersPolicy&lt;/code&gt;, or &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt;.&lt;/p&gt; | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchResponseHeadersPolicy |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | IllegalDelete |  -  |
| **485** | ResponseHeadersPolicyInUse |  -  |

<a id="deleteStreamingDistribution20200531"></a>
# **deleteStreamingDistribution20200531**
> deleteStreamingDistribution20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To delete an RTMP distribution using the CloudFront API&lt;/b&gt;:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Disable the RTMP distribution.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to get the current configuration and the &lt;code&gt;Etag&lt;/code&gt; header for the distribution. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to change the value of &lt;code&gt;Enabled&lt;/code&gt; to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to confirm that the distribution was successfully disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request. Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to your &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request to confirm that the distribution was successfully deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For information about deleting a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html\&quot;&gt;Deleting a Distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The distribution ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when you disabled the streaming distribution. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      apiInstance.deleteStreamingDistribution20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteStreamingDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The distribution ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when you disabled the streaming distribution. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | StreamingDistributionNotDisabled |  -  |
| **482** | InvalidIfMatchVersion |  -  |
| **483** | NoSuchStreamingDistribution |  -  |
| **484** | PreconditionFailed |  -  |

<a id="describeFunction20200531"></a>
# **describeFunction20200531**
> DescribeFunctionResult describeFunction20200531(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, stage)



&lt;p&gt;Gets configuration information and metadata about a CloudFront function, but not the function&#39;s code. To get a function&#39;s code, use &lt;code&gt;GetFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get configuration information and metadata about a function, you must provide the function&#39;s name and stage. To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the function that you are getting information about.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String stage = "DEVELOPMENT"; // String | The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.
    try {
      DescribeFunctionResult result = apiInstance.describeFunction20200531(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, stage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeFunction20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the function that you are getting information about. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **stage** | **String**| The function&#39;s stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;. | [optional] [enum: DEVELOPMENT, LIVE] |

### Return type

[**DescribeFunctionResult**](DescribeFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchFunctionExists |  -  |
| **481** | UnsupportedOperation |  -  |

<a id="getCachePolicy20200531"></a>
# **getCachePolicy20200531**
> GetCachePolicyResult getCachePolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets a cache policy, including the following metadata:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The policy&#39;s identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The date and time when the policy was last modified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To get a cache policy, you must provide the policy&#39;s identifier. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetCachePolicyResult result = apiInstance.getCachePolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCachePolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier for the cache policy. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetCachePolicyResult**](GetCachePolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchCachePolicy |  -  |

<a id="getCachePolicyConfig20200531"></a>
# **getCachePolicyConfig20200531**
> GetCachePolicyConfigResult getCachePolicyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets a cache policy configuration.&lt;/p&gt; &lt;p&gt;To get a cache policy configuration, you must provide the policy&#39;s identifier. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetCachePolicyConfigResult result = apiInstance.getCachePolicyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCachePolicyConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier for the cache policy. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetCachePolicyConfigResult**](GetCachePolicyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchCachePolicy |  -  |

<a id="getCloudFrontOriginAccessIdentity20200531"></a>
# **getCloudFrontOriginAccessIdentity20200531**
> GetCloudFrontOriginAccessIdentityResult getCloudFrontOriginAccessIdentity20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the information about an origin access identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identity's ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetCloudFrontOriginAccessIdentityResult result = apiInstance.getCloudFrontOriginAccessIdentity20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCloudFrontOriginAccessIdentity20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identity&#39;s ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetCloudFrontOriginAccessIdentityResult**](GetCloudFrontOriginAccessIdentityResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchCloudFrontOriginAccessIdentity |  -  |
| **481** | AccessDenied |  -  |

<a id="getCloudFrontOriginAccessIdentityConfig20200531"></a>
# **getCloudFrontOriginAccessIdentityConfig20200531**
> GetCloudFrontOriginAccessIdentityConfigResult getCloudFrontOriginAccessIdentityConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the configuration information about an origin access identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identity's ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetCloudFrontOriginAccessIdentityConfigResult result = apiInstance.getCloudFrontOriginAccessIdentityConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCloudFrontOriginAccessIdentityConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identity&#39;s ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetCloudFrontOriginAccessIdentityConfigResult**](GetCloudFrontOriginAccessIdentityConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchCloudFrontOriginAccessIdentity |  -  |
| **481** | AccessDenied |  -  |

<a id="getContinuousDeploymentPolicy20200531"></a>
# **getContinuousDeploymentPolicy20200531**
> GetContinuousDeploymentPolicyResult getContinuousDeploymentPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a continuous deployment policy, including metadata (the policy&#39;s identifier and the date and time when the policy was last modified).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the continuous deployment policy that you are getting.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetContinuousDeploymentPolicyResult result = apiInstance.getContinuousDeploymentPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getContinuousDeploymentPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the continuous deployment policy that you are getting. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetContinuousDeploymentPolicyResult**](GetContinuousDeploymentPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchContinuousDeploymentPolicy |  -  |

<a id="getContinuousDeploymentPolicyConfig20200531"></a>
# **getContinuousDeploymentPolicyConfig20200531**
> GetContinuousDeploymentPolicyConfigResult getContinuousDeploymentPolicyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets configuration information about a continuous deployment policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the continuous deployment policy whose configuration you are getting.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetContinuousDeploymentPolicyConfigResult result = apiInstance.getContinuousDeploymentPolicyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getContinuousDeploymentPolicyConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the continuous deployment policy whose configuration you are getting. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetContinuousDeploymentPolicyConfigResult**](GetContinuousDeploymentPolicyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchContinuousDeploymentPolicy |  -  |

<a id="getDistribution20200531"></a>
# **getDistribution20200531**
> GetDistributionResult getDistribution20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the information about a distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The distribution's ID. If the ID is empty, an empty distribution configuration is returned.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDistributionResult result = apiInstance.getDistribution20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The distribution&#39;s ID. If the ID is empty, an empty distribution configuration is returned. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDistributionResult**](GetDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchDistribution |  -  |
| **481** | AccessDenied |  -  |

<a id="getDistributionConfig20200531"></a>
# **getDistributionConfig20200531**
> GetDistributionConfigResult getDistributionConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the configuration information about a distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The distribution's ID. If the ID is empty, an empty distribution configuration is returned.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDistributionConfigResult result = apiInstance.getDistributionConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDistributionConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The distribution&#39;s ID. If the ID is empty, an empty distribution configuration is returned. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDistributionConfigResult**](GetDistributionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchDistribution |  -  |
| **481** | AccessDenied |  -  |

<a id="getFieldLevelEncryption20200531"></a>
# **getFieldLevelEncryption20200531**
> GetFieldLevelEncryptionResult getFieldLevelEncryption20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the field-level encryption configuration information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Request the ID for the field-level encryption configuration information.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetFieldLevelEncryptionResult result = apiInstance.getFieldLevelEncryption20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldLevelEncryption20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Request the ID for the field-level encryption configuration information. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetFieldLevelEncryptionResult**](GetFieldLevelEncryptionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchFieldLevelEncryptionConfig |  -  |

<a id="getFieldLevelEncryptionConfig20200531"></a>
# **getFieldLevelEncryptionConfig20200531**
> GetFieldLevelEncryptionConfigResult getFieldLevelEncryptionConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the field-level encryption configuration information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Request the ID for the field-level encryption configuration information.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetFieldLevelEncryptionConfigResult result = apiInstance.getFieldLevelEncryptionConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldLevelEncryptionConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Request the ID for the field-level encryption configuration information. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetFieldLevelEncryptionConfigResult**](GetFieldLevelEncryptionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchFieldLevelEncryptionConfig |  -  |

<a id="getFieldLevelEncryptionProfile20200531"></a>
# **getFieldLevelEncryptionProfile20200531**
> GetFieldLevelEncryptionProfileResult getFieldLevelEncryptionProfile20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the field-level encryption profile information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Get the ID for the field-level encryption profile information.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetFieldLevelEncryptionProfileResult result = apiInstance.getFieldLevelEncryptionProfile20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldLevelEncryptionProfile20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Get the ID for the field-level encryption profile information. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetFieldLevelEncryptionProfileResult**](GetFieldLevelEncryptionProfileResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchFieldLevelEncryptionProfile |  -  |

<a id="getFieldLevelEncryptionProfileConfig20200531"></a>
# **getFieldLevelEncryptionProfileConfig20200531**
> GetFieldLevelEncryptionProfileConfigResult getFieldLevelEncryptionProfileConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the field-level encryption profile configuration information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Get the ID for the field-level encryption profile configuration information.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetFieldLevelEncryptionProfileConfigResult result = apiInstance.getFieldLevelEncryptionProfileConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldLevelEncryptionProfileConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Get the ID for the field-level encryption profile configuration information. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetFieldLevelEncryptionProfileConfigResult**](GetFieldLevelEncryptionProfileConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchFieldLevelEncryptionProfile |  -  |

<a id="getFunction20200531"></a>
# **getFunction20200531**
> GetFunctionResult getFunction20200531(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, stage)



&lt;p&gt;Gets the code of a CloudFront function. To get configuration information and metadata about a function, use &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get a function&#39;s code, you must provide the function&#39;s name and stage. To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the function whose code you are getting.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String stage = "DEVELOPMENT"; // String | The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.
    try {
      GetFunctionResult result = apiInstance.getFunction20200531(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, stage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFunction20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the function whose code you are getting. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **stage** | **String**| The function&#39;s stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;. | [optional] [enum: DEVELOPMENT, LIVE] |

### Return type

[**GetFunctionResult**](GetFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchFunctionExists |  -  |
| **481** | UnsupportedOperation |  -  |

<a id="getInvalidation20200531"></a>
# **getInvalidation20200531**
> GetInvalidationResult getInvalidation20200531(distributionId, id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the information about an invalidation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String distributionId = "distributionId_example"; // String | The distribution's ID.
    String id = "id_example"; // String | The identifier for the invalidation request, for example, <code>IDFDVBD632BHDS5</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetInvalidationResult result = apiInstance.getInvalidation20200531(distributionId, id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getInvalidation20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionId** | **String**| The distribution&#39;s ID. | |
| **id** | **String**| The identifier for the invalidation request, for example, &lt;code&gt;IDFDVBD632BHDS5&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetInvalidationResult**](GetInvalidationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchInvalidation |  -  |
| **481** | NoSuchDistribution |  -  |
| **482** | AccessDenied |  -  |

<a id="getKeyGroup20200531"></a>
# **getKeyGroup20200531**
> GetKeyGroupResult getKeyGroup20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets a key group, including the date and time when the key group was last modified.&lt;/p&gt; &lt;p&gt;To get a key group, you must provide the key group&#39;s identifier. If the key group is referenced in a distribution&#39;s cache behavior, you can get the key group&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the key group is not referenced in a cache behavior, you can get the identifier using &lt;code&gt;ListKeyGroups&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the key group that you are getting. To get the identifier, use <code>ListKeyGroups</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetKeyGroupResult result = apiInstance.getKeyGroup20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getKeyGroup20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the key group that you are getting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetKeyGroupResult**](GetKeyGroupResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchResource |  -  |

<a id="getKeyGroupConfig20200531"></a>
# **getKeyGroupConfig20200531**
> GetKeyGroupConfigResult getKeyGroupConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets a key group configuration.&lt;/p&gt; &lt;p&gt;To get a key group configuration, you must provide the key group&#39;s identifier. If the key group is referenced in a distribution&#39;s cache behavior, you can get the key group&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the key group is not referenced in a cache behavior, you can get the identifier using &lt;code&gt;ListKeyGroups&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the key group whose configuration you are getting. To get the identifier, use <code>ListKeyGroups</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetKeyGroupConfigResult result = apiInstance.getKeyGroupConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getKeyGroupConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the key group whose configuration you are getting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetKeyGroupConfigResult**](GetKeyGroupConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchResource |  -  |

<a id="getMonitoringSubscription20200531"></a>
# **getMonitoringSubscription20200531**
> GetMonitoringSubscriptionResult getMonitoringSubscription20200531(distributionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets information about whether additional CloudWatch metrics are enabled for the specified CloudFront distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String distributionId = "distributionId_example"; // String | The ID of the distribution that you are getting metrics information for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetMonitoringSubscriptionResult result = apiInstance.getMonitoringSubscription20200531(distributionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMonitoringSubscription20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionId** | **String**| The ID of the distribution that you are getting metrics information for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetMonitoringSubscriptionResult**](GetMonitoringSubscriptionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchDistribution |  -  |
| **482** | NoSuchMonitoringSubscription |  -  |
| **483** | UnsupportedOperation |  -  |

<a id="getOriginAccessControl20200531"></a>
# **getOriginAccessControl20200531**
> GetOriginAccessControlResult getOriginAccessControl20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a CloudFront origin access control, including its unique identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the origin access control.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetOriginAccessControlResult result = apiInstance.getOriginAccessControl20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOriginAccessControl20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier of the origin access control. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetOriginAccessControlResult**](GetOriginAccessControlResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchOriginAccessControl |  -  |
| **481** | AccessDenied |  -  |

<a id="getOriginAccessControlConfig20200531"></a>
# **getOriginAccessControlConfig20200531**
> GetOriginAccessControlConfigResult getOriginAccessControlConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a CloudFront origin access control configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the origin access control.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetOriginAccessControlConfigResult result = apiInstance.getOriginAccessControlConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOriginAccessControlConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier of the origin access control. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetOriginAccessControlConfigResult**](GetOriginAccessControlConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchOriginAccessControl |  -  |
| **481** | AccessDenied |  -  |

<a id="getOriginRequestPolicy20200531"></a>
# **getOriginRequestPolicy20200531**
> GetOriginRequestPolicyResult getOriginRequestPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets an origin request policy, including the following metadata:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The policy&#39;s identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The date and time when the policy was last modified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To get an origin request policy, you must provide the policy&#39;s identifier. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetOriginRequestPolicyResult result = apiInstance.getOriginRequestPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOriginRequestPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier for the origin request policy. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetOriginRequestPolicyResult**](GetOriginRequestPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchOriginRequestPolicy |  -  |

<a id="getOriginRequestPolicyConfig20200531"></a>
# **getOriginRequestPolicyConfig20200531**
> GetOriginRequestPolicyConfigResult getOriginRequestPolicyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets an origin request policy configuration.&lt;/p&gt; &lt;p&gt;To get an origin request policy configuration, you must provide the policy&#39;s identifier. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetOriginRequestPolicyConfigResult result = apiInstance.getOriginRequestPolicyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOriginRequestPolicyConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier for the origin request policy. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetOriginRequestPolicyConfigResult**](GetOriginRequestPolicyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchOriginRequestPolicy |  -  |

<a id="getPublicKey20200531"></a>
# **getPublicKey20200531**
> GetPublicKeyResult getPublicKey20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a public key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the public key you are getting.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetPublicKeyResult result = apiInstance.getPublicKey20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPublicKey20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the public key you are getting. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetPublicKeyResult**](GetPublicKeyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchPublicKey |  -  |

<a id="getPublicKeyConfig20200531"></a>
# **getPublicKeyConfig20200531**
> GetPublicKeyConfigResult getPublicKeyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a public key configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the public key whose configuration you are getting.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetPublicKeyConfigResult result = apiInstance.getPublicKeyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPublicKeyConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the public key whose configuration you are getting. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetPublicKeyConfigResult**](GetPublicKeyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchPublicKey |  -  |

<a id="getRealtimeLogConfig20200531"></a>
# **getRealtimeLogConfig20200531**
> GetRealtimeLogConfigResult getRealtimeLogConfig20200531(getRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets a real-time log configuration.&lt;/p&gt; &lt;p&gt;To get a real-time log configuration, you can provide the configuration&#39;s name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to get.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    GetRealtimeLogConfig20200531Request getRealtimeLogConfig20200531Request = new GetRealtimeLogConfig20200531Request(); // GetRealtimeLogConfig20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetRealtimeLogConfigResult result = apiInstance.getRealtimeLogConfig20200531(getRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRealtimeLogConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **getRealtimeLogConfig20200531Request** | [**GetRealtimeLogConfig20200531Request**](GetRealtimeLogConfig20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetRealtimeLogConfigResult**](GetRealtimeLogConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchRealtimeLogConfig |  -  |
| **481** | InvalidArgument |  -  |
| **482** | AccessDenied |  -  |

<a id="getResponseHeadersPolicy20200531"></a>
# **getResponseHeadersPolicy20200531**
> GetResponseHeadersPolicyResult getResponseHeadersPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets a response headers policy, including metadata (the policy&#39;s identifier and the date and time when the policy was last modified).&lt;/p&gt; &lt;p&gt;To get a response headers policy, you must provide the policy&#39;s identifier. If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | <p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetResponseHeadersPolicyResult result = apiInstance.getResponseHeadersPolicy20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getResponseHeadersPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| &lt;p&gt;The identifier for the response headers policy.&lt;/p&gt; &lt;p&gt;If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt; | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetResponseHeadersPolicyResult**](GetResponseHeadersPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchResponseHeadersPolicy |  -  |

<a id="getResponseHeadersPolicyConfig20200531"></a>
# **getResponseHeadersPolicyConfig20200531**
> GetResponseHeadersPolicyConfigResult getResponseHeadersPolicyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets a response headers policy configuration.&lt;/p&gt; &lt;p&gt;To get a response headers policy configuration, you must provide the policy&#39;s identifier. If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | <p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetResponseHeadersPolicyConfigResult result = apiInstance.getResponseHeadersPolicyConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getResponseHeadersPolicyConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| &lt;p&gt;The identifier for the response headers policy.&lt;/p&gt; &lt;p&gt;If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt; | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetResponseHeadersPolicyConfigResult**](GetResponseHeadersPolicyConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchResponseHeadersPolicy |  -  |

<a id="getStreamingDistribution20200531"></a>
# **getStreamingDistribution20200531**
> GetStreamingDistributionResult getStreamingDistribution20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets information about a specified RTMP distribution, including the distribution configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The streaming distribution's ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetStreamingDistributionResult result = apiInstance.getStreamingDistribution20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStreamingDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The streaming distribution&#39;s ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetStreamingDistributionResult**](GetStreamingDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchStreamingDistribution |  -  |
| **481** | AccessDenied |  -  |

<a id="getStreamingDistributionConfig20200531"></a>
# **getStreamingDistributionConfig20200531**
> GetStreamingDistributionConfigResult getStreamingDistributionConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the configuration information about a streaming distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The streaming distribution's ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetStreamingDistributionConfigResult result = apiInstance.getStreamingDistributionConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStreamingDistributionConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The streaming distribution&#39;s ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetStreamingDistributionConfigResult**](GetStreamingDistributionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchStreamingDistribution |  -  |
| **481** | AccessDenied |  -  |

<a id="listCachePolicies20200531"></a>
# **listCachePolicies20200531**
> ListCachePoliciesResult listCachePolicies20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, marker, maxItems)



&lt;p&gt;Gets a list of cache policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String type = "managed"; // String | <p>A filter to return only the specified kinds of cache policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of cache policies that you want in the response.
    try {
      ListCachePoliciesResult result = apiInstance.listCachePolicies20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCachePolicies20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **type** | **String**| &lt;p&gt;A filter to return only the specified kinds of cache policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Returns only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Returns only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] [enum: managed, custom] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of cache policies that you want in the response. | [optional] |

### Return type

[**ListCachePoliciesResult**](ListCachePoliciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchCachePolicy |  -  |
| **482** | InvalidArgument |  -  |

<a id="listCloudFrontOriginAccessIdentities20200531"></a>
# **listCloudFrontOriginAccessIdentities20200531**
> ListCloudFrontOriginAccessIdentitiesResult listCloudFrontOriginAccessIdentities20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



Lists origin access identities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page).
    String maxItems = "maxItems_example"; // String | The maximum number of origin access identities you want in the response body.
    try {
      ListCloudFrontOriginAccessIdentitiesResult result = apiInstance.listCloudFrontOriginAccessIdentities20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCloudFrontOriginAccessIdentities20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last identity on that page). | [optional] |
| **maxItems** | **String**| The maximum number of origin access identities you want in the response body. | [optional] |

### Return type

[**ListCloudFrontOriginAccessIdentitiesResult**](ListCloudFrontOriginAccessIdentitiesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listConflictingAliases20200531"></a>
# **listConflictingAliases20200531**
> ListConflictingAliasesResult listConflictingAliases20200531(distributionId, alias, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



&lt;p&gt;Gets a list of aliases (also called CNAMEs or alternate domain names) that conflict or overlap with the provided alias, and the associated CloudFront distributions and Amazon Web Services accounts for each conflicting alias. In the returned list, the distribution and account IDs are partially hidden, which allows you to identify the distributions and accounts that you own, but helps to protect the information of ones that you don&#39;t own.&lt;/p&gt; &lt;p&gt;Use this operation to find aliases that are in use in CloudFront that conflict or overlap with the provided alias. For example, if you provide &lt;code&gt;www.example.com&lt;/code&gt; as input, the returned list can include &lt;code&gt;www.example.com&lt;/code&gt; and the overlapping wildcard alternate domain name (&lt;code&gt;*.example.com&lt;/code&gt;), if they exist. If you provide &lt;code&gt;*.example.com&lt;/code&gt; as input, the returned list can include &lt;code&gt;*.example.com&lt;/code&gt; and any alternate domain names covered by that wildcard (for example, &lt;code&gt;www.example.com&lt;/code&gt;, &lt;code&gt;test.example.com&lt;/code&gt;, &lt;code&gt;dev.example.com&lt;/code&gt;, and so on), if they exist.&lt;/p&gt; &lt;p&gt;To list conflicting aliases, you provide the alias to search and the ID of a distribution in your account that has an attached SSL/TLS certificate that includes the provided alias. For more information, including how to set up the distribution and certificate, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\&quot;&gt;Moving an alternate domain name to a different distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String distributionId = "distributionId_example"; // String | The ID of a distribution in your account that has an attached SSL/TLS certificate that includes the provided alias.
    String alias = "alias_example"; // String | The alias (also called a CNAME) to search for conflicting aliases.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    Integer maxItems = 56; // Integer | The maximum number of conflicting aliases that you want in the response.
    try {
      ListConflictingAliasesResult result = apiInstance.listConflictingAliases20200531(distributionId, alias, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listConflictingAliases20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionId** | **String**| The ID of a distribution in your account that has an attached SSL/TLS certificate that includes the provided alias. | |
| **alias** | **String**| The alias (also called a CNAME) to search for conflicting aliases. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **Integer**| The maximum number of conflicting aliases that you want in the response. | [optional] |

### Return type

[**ListConflictingAliasesResult**](ListConflictingAliasesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | NoSuchDistribution |  -  |

<a id="listContinuousDeploymentPolicies20200531"></a>
# **listContinuousDeploymentPolicies20200531**
> ListContinuousDeploymentPoliciesResult listContinuousDeploymentPolicies20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



&lt;p&gt;Gets a list of the continuous deployment policies in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of continuous deployment policies that you want returned in the response.
    try {
      ListContinuousDeploymentPoliciesResult result = apiInstance.listContinuousDeploymentPolicies20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listContinuousDeploymentPolicies20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of continuous deployment policies that you want returned in the response. | [optional] |

### Return type

[**ListContinuousDeploymentPoliciesResult**](ListContinuousDeploymentPoliciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | AccessDenied |  -  |
| **482** | NoSuchContinuousDeploymentPolicy |  -  |

<a id="listDistributions20200531"></a>
# **listDistributions20200531**
> ListDistributionsResult listDistributions20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



List CloudFront distributions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last distribution on that page).
    String maxItems = "maxItems_example"; // String | The maximum number of distributions you want in the response body.
    try {
      ListDistributionsResult result = apiInstance.listDistributions20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributions20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last distribution on that page). | [optional] |
| **maxItems** | **String**| The maximum number of distributions you want in the response body. | [optional] |

### Return type

[**ListDistributionsResult**](ListDistributionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listDistributionsByCachePolicyId20200531"></a>
# **listDistributionsByCachePolicyId20200531**
> ListDistributionsByCachePolicyIdResult listDistributionsByCachePolicyId20200531(cachePolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



&lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified cache policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cachePolicyId = "cachePolicyId_example"; // String | The ID of the cache policy whose associated distribution IDs you want to list.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of distribution IDs that you want in the response.
    try {
      ListDistributionsByCachePolicyIdResult result = apiInstance.listDistributionsByCachePolicyId20200531(cachePolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributionsByCachePolicyId20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **cachePolicyId** | **String**| The ID of the cache policy whose associated distribution IDs you want to list. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of distribution IDs that you want in the response. | [optional] |

### Return type

[**ListDistributionsByCachePolicyIdResult**](ListDistributionsByCachePolicyIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchCachePolicy |  -  |
| **481** | InvalidArgument |  -  |
| **482** | AccessDenied |  -  |

<a id="listDistributionsByKeyGroup20200531"></a>
# **listDistributionsByKeyGroup20200531**
> ListDistributionsByKeyGroupResult listDistributionsByKeyGroup20200531(keyGroupId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



&lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that references the specified key group.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String keyGroupId = "keyGroupId_example"; // String | The ID of the key group whose associated distribution IDs you are listing.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of distribution IDs that you want in the response.
    try {
      ListDistributionsByKeyGroupResult result = apiInstance.listDistributionsByKeyGroup20200531(keyGroupId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributionsByKeyGroup20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyGroupId** | **String**| The ID of the key group whose associated distribution IDs you are listing. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of distribution IDs that you want in the response. | [optional] |

### Return type

[**ListDistributionsByKeyGroupResult**](ListDistributionsByKeyGroupResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchResource |  -  |
| **481** | InvalidArgument |  -  |

<a id="listDistributionsByOriginRequestPolicyId20200531"></a>
# **listDistributionsByOriginRequestPolicyId20200531**
> ListDistributionsByOriginRequestPolicyIdResult listDistributionsByOriginRequestPolicyId20200531(originRequestPolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



&lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified origin request policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String originRequestPolicyId = "originRequestPolicyId_example"; // String | The ID of the origin request policy whose associated distribution IDs you want to list.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of distribution IDs that you want in the response.
    try {
      ListDistributionsByOriginRequestPolicyIdResult result = apiInstance.listDistributionsByOriginRequestPolicyId20200531(originRequestPolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributionsByOriginRequestPolicyId20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **originRequestPolicyId** | **String**| The ID of the origin request policy whose associated distribution IDs you want to list. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of distribution IDs that you want in the response. | [optional] |

### Return type

[**ListDistributionsByOriginRequestPolicyIdResult**](ListDistributionsByOriginRequestPolicyIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchOriginRequestPolicy |  -  |
| **481** | InvalidArgument |  -  |
| **482** | AccessDenied |  -  |

<a id="listDistributionsByRealtimeLogConfig20200531"></a>
# **listDistributionsByRealtimeLogConfig20200531**
> ListDistributionsByRealtimeLogConfigResult listDistributionsByRealtimeLogConfig20200531(listDistributionsByRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets a list of distributions that have a cache behavior that&#39;s associated with the specified real-time log configuration.&lt;/p&gt; &lt;p&gt;You can specify the real-time log configuration by its name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to list distributions for.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListDistributionsByRealtimeLogConfig20200531Request listDistributionsByRealtimeLogConfig20200531Request = new ListDistributionsByRealtimeLogConfig20200531Request(); // ListDistributionsByRealtimeLogConfig20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListDistributionsByRealtimeLogConfigResult result = apiInstance.listDistributionsByRealtimeLogConfig20200531(listDistributionsByRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributionsByRealtimeLogConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **listDistributionsByRealtimeLogConfig20200531Request** | [**ListDistributionsByRealtimeLogConfig20200531Request**](ListDistributionsByRealtimeLogConfig20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListDistributionsByRealtimeLogConfigResult**](ListDistributionsByRealtimeLogConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listDistributionsByResponseHeadersPolicyId20200531"></a>
# **listDistributionsByResponseHeadersPolicyId20200531**
> ListDistributionsByResponseHeadersPolicyIdResult listDistributionsByResponseHeadersPolicyId20200531(responseHeadersPolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



&lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified response headers policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String responseHeadersPolicyId = "responseHeadersPolicyId_example"; // String | The ID of the response headers policy whose associated distribution IDs you want to list.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of distribution IDs that you want to get in the response.
    try {
      ListDistributionsByResponseHeadersPolicyIdResult result = apiInstance.listDistributionsByResponseHeadersPolicyId20200531(responseHeadersPolicyId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributionsByResponseHeadersPolicyId20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **responseHeadersPolicyId** | **String**| The ID of the response headers policy whose associated distribution IDs you want to list. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of distribution IDs that you want to get in the response. | [optional] |

### Return type

[**ListDistributionsByResponseHeadersPolicyIdResult**](ListDistributionsByResponseHeadersPolicyIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchResponseHeadersPolicy |  -  |
| **481** | InvalidArgument |  -  |
| **482** | AccessDenied |  -  |

<a id="listDistributionsByWebACLId20200531"></a>
# **listDistributionsByWebACLId20200531**
> ListDistributionsByWebACLIdResult listDistributionsByWebACLId20200531(webACLId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



List the distributions that are associated with a specified WAF web ACL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String webACLId = "webACLId_example"; // String | The ID of the WAF web ACL that you want to list the associated distributions. If you specify \"null\" for the ID, the request returns a list of the distributions that aren't associated with a web ACL.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use <code>Marker</code> and <code>MaxItems</code> to control pagination of results. If you have more than <code>MaxItems</code> distributions that satisfy the request, the response includes a <code>NextMarker</code> element. To get the next page of results, submit another request. For the value of <code>Marker</code>, specify the value of <code>NextMarker</code> from the last response. (For the first request, omit <code>Marker</code>.)
    String maxItems = "maxItems_example"; // String | The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.
    try {
      ListDistributionsByWebACLIdResult result = apiInstance.listDistributionsByWebACLId20200531(webACLId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributionsByWebACLId20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webACLId** | **String**| The ID of the WAF web ACL that you want to list the associated distributions. If you specify \&quot;null\&quot; for the ID, the request returns a list of the distributions that aren&#39;t associated with a web ACL. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use &lt;code&gt;Marker&lt;/code&gt; and &lt;code&gt;MaxItems&lt;/code&gt; to control pagination of results. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; distributions that satisfy the request, the response includes a &lt;code&gt;NextMarker&lt;/code&gt; element. To get the next page of results, submit another request. For the value of &lt;code&gt;Marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the last response. (For the first request, omit &lt;code&gt;Marker&lt;/code&gt;.) | [optional] |
| **maxItems** | **String**| The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100. | [optional] |

### Return type

[**ListDistributionsByWebACLIdResult**](ListDistributionsByWebACLIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | InvalidWebACLId |  -  |

<a id="listFieldLevelEncryptionConfigs20200531"></a>
# **listFieldLevelEncryptionConfigs20200531**
> ListFieldLevelEncryptionConfigsResult listFieldLevelEncryptionConfigs20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



List all field-level encryption configurations that have been created in CloudFront for this account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last configuration on that page).
    String maxItems = "maxItems_example"; // String | The maximum number of field-level encryption configurations you want in the response body.
    try {
      ListFieldLevelEncryptionConfigsResult result = apiInstance.listFieldLevelEncryptionConfigs20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFieldLevelEncryptionConfigs20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last configuration on that page). | [optional] |
| **maxItems** | **String**| The maximum number of field-level encryption configurations you want in the response body. | [optional] |

### Return type

[**ListFieldLevelEncryptionConfigsResult**](ListFieldLevelEncryptionConfigsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listFieldLevelEncryptionProfiles20200531"></a>
# **listFieldLevelEncryptionProfiles20200531**
> ListFieldLevelEncryptionProfilesResult listFieldLevelEncryptionProfiles20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



Request a list of field-level encryption profiles that have been created in CloudFront for this account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last profile on that page).
    String maxItems = "maxItems_example"; // String | The maximum number of field-level encryption profiles you want in the response body. 
    try {
      ListFieldLevelEncryptionProfilesResult result = apiInstance.listFieldLevelEncryptionProfiles20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFieldLevelEncryptionProfiles20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last profile on that page). | [optional] |
| **maxItems** | **String**| The maximum number of field-level encryption profiles you want in the response body.  | [optional] |

### Return type

[**ListFieldLevelEncryptionProfilesResult**](ListFieldLevelEncryptionProfilesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listFunctions20200531"></a>
# **listFunctions20200531**
> ListFunctionsResult listFunctions20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems, stage)



&lt;p&gt;Gets a list of all CloudFront functions in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the functions that are in the specified stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of functions that you want in the response.
    String stage = "DEVELOPMENT"; // String | An optional filter to return only the functions that are in the specified stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.
    try {
      ListFunctionsResult result = apiInstance.listFunctions20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems, stage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFunctions20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of functions that you want in the response. | [optional] |
| **stage** | **String**| An optional filter to return only the functions that are in the specified stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;. | [optional] [enum: DEVELOPMENT, LIVE] |

### Return type

[**ListFunctionsResult**](ListFunctionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | UnsupportedOperation |  -  |

<a id="listInvalidations20200531"></a>
# **listInvalidations20200531**
> ListInvalidationsResult listInvalidations20200531(distributionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



Lists invalidation batches.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String distributionId = "distributionId_example"; // String | The distribution's ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.
    String maxItems = "maxItems_example"; // String | The maximum number of invalidation batches that you want in the response body.
    try {
      ListInvalidationsResult result = apiInstance.listInvalidations20200531(distributionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listInvalidations20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionId** | **String**| The distribution&#39;s ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. This value is the same as the ID of the last invalidation batch on that page. | [optional] |
| **maxItems** | **String**| The maximum number of invalidation batches that you want in the response body. | [optional] |

### Return type

[**ListInvalidationsResult**](ListInvalidationsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | NoSuchDistribution |  -  |
| **482** | AccessDenied |  -  |

<a id="listKeyGroups20200531"></a>
# **listKeyGroups20200531**
> ListKeyGroupsResult listKeyGroups20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



&lt;p&gt;Gets a list of key groups.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of key groups. The response includes key groups in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of key groups that you want in the response.
    try {
      ListKeyGroupsResult result = apiInstance.listKeyGroups20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listKeyGroups20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of key groups. The response includes key groups in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of key groups that you want in the response. | [optional] |

### Return type

[**ListKeyGroupsResult**](ListKeyGroupsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listOriginAccessControls20200531"></a>
# **listOriginAccessControls20200531**
> ListOriginAccessControlsResult listOriginAccessControls20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



&lt;p&gt;Gets the list of CloudFront origin access controls in this Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send another request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the next request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of origin access controls that you want in the response.
    try {
      ListOriginAccessControlsResult result = apiInstance.listOriginAccessControls20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listOriginAccessControls20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of origin access controls that you want in the response. | [optional] |

### Return type

[**ListOriginAccessControlsResult**](ListOriginAccessControlsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listOriginRequestPolicies20200531"></a>
# **listOriginRequestPolicies20200531**
> ListOriginRequestPoliciesResult listOriginRequestPolicies20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, marker, maxItems)



&lt;p&gt;Gets a list of origin request policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String type = "managed"; // String | <p>A filter to return only the specified kinds of origin request policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of origin request policies. The response includes origin request policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of origin request policies that you want in the response.
    try {
      ListOriginRequestPoliciesResult result = apiInstance.listOriginRequestPolicies20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listOriginRequestPolicies20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **type** | **String**| &lt;p&gt;A filter to return only the specified kinds of origin request policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Returns only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Returns only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] [enum: managed, custom] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of origin request policies. The response includes origin request policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of origin request policies that you want in the response. | [optional] |

### Return type

[**ListOriginRequestPoliciesResult**](ListOriginRequestPoliciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchOriginRequestPolicy |  -  |
| **482** | InvalidArgument |  -  |

<a id="listPublicKeys20200531"></a>
# **listPublicKeys20200531**
> ListPublicKeysResult listPublicKeys20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



List all public keys that have been added to CloudFront for this account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last public key on that page).
    String maxItems = "maxItems_example"; // String | The maximum number of public keys you want in the response body.
    try {
      ListPublicKeysResult result = apiInstance.listPublicKeys20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPublicKeys20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last public key on that page). | [optional] |
| **maxItems** | **String**| The maximum number of public keys you want in the response body. | [optional] |

### Return type

[**ListPublicKeysResult**](ListPublicKeysResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listRealtimeLogConfigs20200531"></a>
# **listRealtimeLogConfigs20200531**
> ListRealtimeLogConfigsResult listRealtimeLogConfigs20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxItems, marker)



&lt;p&gt;Gets a list of real-time log configurations.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxItems = "maxItems_example"; // String | The maximum number of real-time log configurations that you want in the response.
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    try {
      ListRealtimeLogConfigsResult result = apiInstance.listRealtimeLogConfigs20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxItems, marker);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRealtimeLogConfigs20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxItems** | **String**| The maximum number of real-time log configurations that you want in the response. | [optional] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |

### Return type

[**ListRealtimeLogConfigsResult**](ListRealtimeLogConfigsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | AccessDenied |  -  |
| **482** | NoSuchRealtimeLogConfig |  -  |

<a id="listResponseHeadersPolicies20200531"></a>
# **listResponseHeadersPolicies20200531**
> ListResponseHeadersPoliciesResult listResponseHeadersPolicies20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, marker, maxItems)



&lt;p&gt;Gets a list of response headers policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to get only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String type = "managed"; // String | <p>A filter to get only the specified kind of response headers policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Gets only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Gets only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
    String marker = "marker_example"; // String | Use this field when paginating results to indicate where to begin in your list of response headers policies. The response includes response headers policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.
    String maxItems = "maxItems_example"; // String | The maximum number of response headers policies that you want to get in the response.
    try {
      ListResponseHeadersPoliciesResult result = apiInstance.listResponseHeadersPolicies20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listResponseHeadersPolicies20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **type** | **String**| &lt;p&gt;A filter to get only the specified kind of response headers policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Gets only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Gets only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] [enum: managed, custom] |
| **marker** | **String**| Use this field when paginating results to indicate where to begin in your list of response headers policies. The response includes response headers policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. | [optional] |
| **maxItems** | **String**| The maximum number of response headers policies that you want to get in the response. | [optional] |

### Return type

[**ListResponseHeadersPoliciesResult**](ListResponseHeadersPoliciesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | NoSuchResponseHeadersPolicy |  -  |
| **482** | InvalidArgument |  -  |

<a id="listStreamingDistributions20200531"></a>
# **listStreamingDistributions20200531**
> ListStreamingDistributionsResult listStreamingDistributions20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



List streaming distributions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String marker = "marker_example"; // String | The value that you provided for the <code>Marker</code> request parameter.
    String maxItems = "maxItems_example"; // String | The value that you provided for the <code>MaxItems</code> request parameter.
    try {
      ListStreamingDistributionsResult result = apiInstance.listStreamingDistributions20200531(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listStreamingDistributions20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| The value that you provided for the &lt;code&gt;Marker&lt;/code&gt; request parameter. | [optional] |
| **maxItems** | **String**| The value that you provided for the &lt;code&gt;MaxItems&lt;/code&gt; request parameter. | [optional] |

### Return type

[**ListStreamingDistributionsResult**](ListStreamingDistributionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |

<a id="listTagsForResource20200531"></a>
# **listTagsForResource20200531**
> ListTagsForResourceResult listTagsForResource20200531(resource, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



List tags for a CloudFront resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resource = "resource_example"; // String | An ARN of a CloudFront resource.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResult result = apiInstance.listTagsForResource20200531(resource, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource** | **String**| An ARN of a CloudFront resource. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResult**](ListTagsForResourceResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidArgument |  -  |
| **482** | InvalidTagging |  -  |
| **483** | NoSuchResource |  -  |

<a id="publishFunction20200531"></a>
# **publishFunction20200531**
> PublishFunctionResult publishFunction20200531(name, ifMatch, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Publishes a CloudFront function by copying the function code from the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage to &lt;code&gt;LIVE&lt;/code&gt;. This automatically updates all cache behaviors that are using this function to use the newly published copy in the &lt;code&gt;LIVE&lt;/code&gt; stage.&lt;/p&gt; &lt;p&gt;When a function is published to the &lt;code&gt;LIVE&lt;/code&gt; stage, you can attach the function to a distribution&#39;s cache behavior, using the function&#39;s Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;To publish a function, you must provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value). To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the function that you are publishing.
    String ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the function that you are publishing, which you can get using <code>DescribeFunction</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PublishFunctionResult result = apiInstance.publishFunction20200531(name, ifMatch, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishFunction20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the function that you are publishing. | |
| **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are publishing, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PublishFunctionResult**](PublishFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchFunctionExists |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | UnsupportedOperation |  -  |

<a id="tagResource20200531"></a>
# **tagResource20200531**
> tagResource20200531(resource, operation, tagResource20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Add tags to a CloudFront resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resource = "resource_example"; // String | An ARN of a CloudFront resource.
    String operation = "Tag"; // String | 
    TagResource20200531Request tagResource20200531Request = new TagResource20200531Request(); // TagResource20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.tagResource20200531(resource, operation, tagResource20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource** | **String**| An ARN of a CloudFront resource. | |
| **operation** | **String**|  | [enum: Tag] |
| **tagResource20200531Request** | [**TagResource20200531Request**](TagResource20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidArgument |  -  |
| **482** | InvalidTagging |  -  |
| **483** | NoSuchResource |  -  |

<a id="testFunction20200531"></a>
# **testFunction20200531**
> TestFunctionResult testFunction20200531(name, ifMatch, testFunction20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Tests a CloudFront function.&lt;/p&gt; &lt;p&gt;To test a function, you provide an &lt;i&gt;event object&lt;/i&gt; that represents an HTTP request or response that your CloudFront distribution could receive in production. CloudFront runs the function, passing it the event object that you provided, and returns the function&#39;s result (the modified event object) in the response. The response also contains function logs and error messages, if any exist. For more information about testing functions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function\&quot;&gt;Testing functions&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To test a function, you provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value) along with the event object. To get the function&#39;s name and version, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the function that you are testing.
    String ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the function that you are testing, which you can get using <code>DescribeFunction</code>.
    TestFunction20200531Request testFunction20200531Request = new TestFunction20200531Request(); // TestFunction20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      TestFunctionResult result = apiInstance.testFunction20200531(name, ifMatch, testFunction20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#testFunction20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the function that you are testing. | |
| **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are testing, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;. | |
| **testFunction20200531Request** | [**TestFunction20200531Request**](TestFunction20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**TestFunctionResult**](TestFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchFunctionExists |  -  |
| **483** | TestFunctionFailed |  -  |
| **484** | UnsupportedOperation |  -  |

<a id="untagResource20200531"></a>
# **untagResource20200531**
> untagResource20200531(resource, operation, untagResource20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Remove tags from a CloudFront resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resource = "resource_example"; // String | An ARN of a CloudFront resource.
    String operation = "Untag"; // String | 
    UntagResource20200531Request untagResource20200531Request = new UntagResource20200531Request(); // UntagResource20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.untagResource20200531(resource, operation, untagResource20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource** | **String**| An ARN of a CloudFront resource. | |
| **operation** | **String**|  | [enum: Untag] |
| **untagResource20200531Request** | [**UntagResource20200531Request**](UntagResource20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | InvalidArgument |  -  |
| **482** | InvalidTagging |  -  |
| **483** | NoSuchResource |  -  |

<a id="updateCachePolicy20200531"></a>
# **updateCachePolicy20200531**
> UpdateCachePolicyResult updateCachePolicy20200531(id, createCachePolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Updates a cache policy configuration.&lt;/p&gt; &lt;p&gt;When you update a cache policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a cache policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetCachePolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the cache policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateCachePolicy&lt;/code&gt; by providing the entire cache policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behavior's <code>CachePolicyId</code> field in the response to <code>GetDistributionConfig</code>.
    CreateCachePolicy20200531Request createCachePolicy20200531Request = new CreateCachePolicy20200531Request(); // CreateCachePolicy20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The version of the cache policy that you are updating. The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetCachePolicyConfig</code>.
    try {
      UpdateCachePolicyResult result = apiInstance.updateCachePolicy20200531(id, createCachePolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateCachePolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behavior&#39;s &lt;code&gt;CachePolicyId&lt;/code&gt; field in the response to &lt;code&gt;GetDistributionConfig&lt;/code&gt;. | |
| **createCachePolicy20200531Request** | [**CreateCachePolicy20200531Request**](CreateCachePolicy20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The version of the cache policy that you are updating. The version is returned in the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetCachePolicyConfig&lt;/code&gt;. | [optional] |

### Return type

[**UpdateCachePolicyResult**](UpdateCachePolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | IllegalUpdate |  -  |
| **482** | InconsistentQuantities |  -  |
| **483** | InvalidArgument |  -  |
| **484** | InvalidIfMatchVersion |  -  |
| **485** | NoSuchCachePolicy |  -  |
| **486** | PreconditionFailed |  -  |
| **487** | CachePolicyAlreadyExists |  -  |
| **488** | TooManyHeadersInCachePolicy |  -  |
| **489** | TooManyCookiesInCachePolicy |  -  |
| **490** | TooManyQueryStringsInCachePolicy |  -  |

<a id="updateCloudFrontOriginAccessIdentity20200531"></a>
# **updateCloudFrontOriginAccessIdentity20200531**
> UpdateCloudFrontOriginAccessIdentityResult updateCloudFrontOriginAccessIdentity20200531(id, createCloudFrontOriginAccessIdentity20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Update an origin access identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identity's id.
    CreateCloudFrontOriginAccessIdentity20200531Request createCloudFrontOriginAccessIdentity20200531Request = new CreateCloudFrontOriginAccessIdentity20200531Request(); // CreateCloudFrontOriginAccessIdentity20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the identity's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateCloudFrontOriginAccessIdentityResult result = apiInstance.updateCloudFrontOriginAccessIdentity20200531(id, createCloudFrontOriginAccessIdentity20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateCloudFrontOriginAccessIdentity20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identity&#39;s id. | |
| **createCloudFrontOriginAccessIdentity20200531Request** | [**CreateCloudFrontOriginAccessIdentity20200531Request**](CreateCloudFrontOriginAccessIdentity20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the identity&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

[**UpdateCloudFrontOriginAccessIdentityResult**](UpdateCloudFrontOriginAccessIdentityResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | IllegalUpdate |  -  |
| **482** | InvalidIfMatchVersion |  -  |
| **483** | MissingBody |  -  |
| **484** | NoSuchCloudFrontOriginAccessIdentity |  -  |
| **485** | PreconditionFailed |  -  |
| **486** | InvalidArgument |  -  |
| **487** | InconsistentQuantities |  -  |

<a id="updateContinuousDeploymentPolicy20200531"></a>
# **updateContinuousDeploymentPolicy20200531**
> UpdateContinuousDeploymentPolicyResult updateContinuousDeploymentPolicy20200531(id, createContinuousDeploymentPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Updates a continuous deployment policy. You can update a continuous deployment policy to enable or disable it, to change the percentage of traffic that it sends to the staging distribution, or to change the staging distribution that it sends traffic to.&lt;/p&gt; &lt;p&gt;When you update a continuous deployment policy configuration, all the fields are updated with the values that are provided in the request. You cannot update some fields independent of others. To update a continuous deployment policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetContinuousDeploymentPolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the continuous deployment policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;UpdateContinuousDeploymentPolicy&lt;/code&gt;, providing the entire continuous deployment policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the continuous deployment policy that you are updating.
    CreateContinuousDeploymentPolicy20200531Request createContinuousDeploymentPolicy20200531Request = new CreateContinuousDeploymentPolicy20200531Request(); // CreateContinuousDeploymentPolicy20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the continuous deployment policy that you are updating.
    try {
      UpdateContinuousDeploymentPolicyResult result = apiInstance.updateContinuousDeploymentPolicy20200531(id, createContinuousDeploymentPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateContinuousDeploymentPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the continuous deployment policy that you are updating. | |
| **createContinuousDeploymentPolicy20200531Request** | [**CreateContinuousDeploymentPolicy20200531Request**](CreateContinuousDeploymentPolicy20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the continuous deployment policy that you are updating. | [optional] |

### Return type

[**UpdateContinuousDeploymentPolicyResult**](UpdateContinuousDeploymentPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidIfMatchVersion |  -  |
| **481** | InvalidArgument |  -  |
| **482** | AccessDenied |  -  |
| **483** | InconsistentQuantities |  -  |
| **484** | PreconditionFailed |  -  |
| **485** | StagingDistributionInUse |  -  |
| **486** | NoSuchContinuousDeploymentPolicy |  -  |

<a id="updateDistribution20200531"></a>
# **updateDistribution20200531**
> UpdateDistributionResult updateDistribution20200531(id, createDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Updates the configuration for a CloudFront distribution.&lt;/p&gt; &lt;p&gt;The update process includes getting the current distribution configuration, updating it to make your changes, and then submitting an &lt;code&gt;UpdateDistribution&lt;/code&gt; request to make the updates.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To update a web distribution using the CloudFront API&lt;/b&gt; &lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetDistributionConfig&lt;/code&gt; to get the current configuration, including the version identifier (&lt;code&gt;ETag&lt;/code&gt;).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the distribution configuration that was returned in the response. Note the following important requirements and restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must rename the &lt;code&gt;ETag&lt;/code&gt; field to &lt;code&gt;IfMatch&lt;/code&gt;, leaving the value unchanged. (Set the value of &lt;code&gt;IfMatch&lt;/code&gt; to the value of &lt;code&gt;ETag&lt;/code&gt;, then remove the &lt;code&gt;ETag&lt;/code&gt; field.)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t change the value of &lt;code&gt;CallerReference&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateDistribution&lt;/code&gt; request, providing the distribution configuration. The new configuration replaces the existing configuration. The values that you specify in an &lt;code&gt;UpdateDistribution&lt;/code&gt; request are not merged into your existing configuration. Make sure to include all fields: the ones that you modified and also the ones that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The distribution's id.
    CreateDistribution20200531Request createDistribution20200531Request = new CreateDistribution20200531Request(); // CreateDistribution20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateDistributionResult result = apiInstance.updateDistribution20200531(id, createDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The distribution&#39;s id. | |
| **createDistribution20200531Request** | [**CreateDistribution20200531Request**](CreateDistribution20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the distribution&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

[**UpdateDistributionResult**](UpdateDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | CNAMEAlreadyExists |  -  |
| **482** | IllegalUpdate |  -  |
| **483** | InvalidIfMatchVersion |  -  |
| **484** | MissingBody |  -  |
| **485** | NoSuchDistribution |  -  |
| **486** | PreconditionFailed |  -  |
| **487** | TooManyDistributionCNAMEs |  -  |
| **488** | InvalidDefaultRootObject |  -  |
| **489** | InvalidRelativePath |  -  |
| **490** | InvalidErrorCode |  -  |
| **491** | InvalidResponseCode |  -  |
| **492** | InvalidArgument |  -  |
| **493** | InvalidOriginAccessIdentity |  -  |
| **494** | InvalidOriginAccessControl |  -  |
| **495** | TooManyTrustedSigners |  -  |
| **496** | TrustedSignerDoesNotExist |  -  |
| **497** | InvalidViewerCertificate |  -  |
| **498** | InvalidMinimumProtocolVersion |  -  |
| **499** | InvalidRequiredProtocol |  -  |
| **500** | NoSuchOrigin |  -  |
| **501** | TooManyOrigins |  -  |
| **502** | TooManyOriginGroupsPerDistribution |  -  |
| **503** | TooManyCacheBehaviors |  -  |
| **504** | TooManyCookieNamesInWhiteList |  -  |
| **505** | InvalidForwardCookies |  -  |
| **506** | TooManyHeadersInForwardedValues |  -  |
| **507** | InvalidHeadersForS3Origin |  -  |
| **508** | InconsistentQuantities |  -  |
| **509** | TooManyCertificates |  -  |
| **510** | InvalidLocationCode |  -  |
| **511** | InvalidGeoRestrictionParameter |  -  |
| **512** | InvalidTTLOrder |  -  |
| **513** | InvalidWebACLId |  -  |
| **514** | TooManyOriginCustomHeaders |  -  |
| **515** | TooManyQueryStringParameters |  -  |
| **516** | InvalidQueryStringParameters |  -  |
| **517** | TooManyDistributionsWithLambdaAssociations |  -  |
| **518** | TooManyDistributionsWithSingleFunctionARN |  -  |
| **519** | TooManyLambdaFunctionAssociations |  -  |
| **520** | InvalidLambdaFunctionAssociation |  -  |
| **521** | TooManyDistributionsWithFunctionAssociations |  -  |
| **522** | TooManyFunctionAssociations |  -  |
| **523** | InvalidFunctionAssociation |  -  |
| **524** | InvalidOriginReadTimeout |  -  |
| **525** | InvalidOriginKeepaliveTimeout |  -  |
| **526** | NoSuchFieldLevelEncryptionConfig |  -  |
| **527** | IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior |  -  |
| **528** | TooManyDistributionsAssociatedToFieldLevelEncryptionConfig |  -  |
| **529** | NoSuchCachePolicy |  -  |
| **530** | TooManyDistributionsAssociatedToCachePolicy |  -  |
| **531** | TooManyDistributionsAssociatedToOriginAccessControl |  -  |
| **532** | NoSuchResponseHeadersPolicy |  -  |
| **533** | TooManyDistributionsAssociatedToResponseHeadersPolicy |  -  |
| **534** | NoSuchOriginRequestPolicy |  -  |
| **535** | TooManyDistributionsAssociatedToOriginRequestPolicy |  -  |
| **536** | TooManyDistributionsAssociatedToKeyGroup |  -  |
| **537** | TooManyKeyGroupsAssociatedToDistribution |  -  |
| **538** | TrustedKeyGroupDoesNotExist |  -  |
| **539** | NoSuchRealtimeLogConfig |  -  |
| **540** | RealtimeLogConfigOwnerMismatch |  -  |
| **541** | ContinuousDeploymentPolicyInUse |  -  |
| **542** | NoSuchContinuousDeploymentPolicy |  -  |
| **543** | StagingDistributionInUse |  -  |
| **544** | IllegalOriginAccessConfiguration |  -  |
| **545** | InvalidDomainNameForOriginAccessControl |  -  |

<a id="updateDistributionWithStagingConfig20200531"></a>
# **updateDistributionWithStagingConfig20200531**
> UpdateDistributionWithStagingConfigResult updateDistributionWithStagingConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, stagingDistributionId, ifMatch)



&lt;p&gt;Copies the staging distribution&#39;s configuration to its corresponding primary distribution. The primary distribution retains its &lt;code&gt;Aliases&lt;/code&gt; (also known as alternate domain names or CNAMEs) and &lt;code&gt;ContinuousDeploymentPolicyId&lt;/code&gt; value, but otherwise its configuration is overwritten to match the staging distribution.&lt;/p&gt; &lt;p&gt;You can use this operation in a continuous deployment workflow after you have tested configuration changes on the staging distribution. After using a continuous deployment policy to move a portion of your domain name&#39;s traffic to the staging distribution and verifying that it works as intended, you can use this operation to copy the staging distribution&#39;s configuration to the primary distribution. This action will disable the continuous deployment policy and move your domain&#39;s traffic back to the primary distribution.&lt;/p&gt; &lt;p&gt;This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html\&quot;&gt;GetDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html\&quot;&gt;UpdateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the primary distribution to which you are copying a staging distribution's configuration.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String stagingDistributionId = "stagingDistributionId_example"; // String | The identifier of the staging distribution whose configuration you are copying to the primary distribution.
    String ifMatch = "ifMatch_example"; // String | <p>The current versions (<code>ETag</code> values) of both primary and staging distributions. Provide these in the following format:</p> <p> <code>&lt;primary ETag&gt;, &lt;staging ETag&gt;</code> </p>
    try {
      UpdateDistributionWithStagingConfigResult result = apiInstance.updateDistributionWithStagingConfig20200531(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, stagingDistributionId, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDistributionWithStagingConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the primary distribution to which you are copying a staging distribution&#39;s configuration. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **stagingDistributionId** | **String**| The identifier of the staging distribution whose configuration you are copying to the primary distribution. | [optional] |
| **ifMatch** | **String**| &lt;p&gt;The current versions (&lt;code&gt;ETag&lt;/code&gt; values) of both primary and staging distributions. Provide these in the following format:&lt;/p&gt; &lt;p&gt; &lt;code&gt;&amp;lt;primary ETag&amp;gt;, &amp;lt;staging ETag&amp;gt;&lt;/code&gt; &lt;/p&gt; | [optional] |

### Return type

[**UpdateDistributionWithStagingConfigResult**](UpdateDistributionWithStagingConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | CNAMEAlreadyExists |  -  |
| **482** | IllegalUpdate |  -  |
| **483** | InvalidIfMatchVersion |  -  |
| **484** | MissingBody |  -  |
| **485** | NoSuchDistribution |  -  |
| **486** | PreconditionFailed |  -  |
| **487** | TooManyDistributionCNAMEs |  -  |
| **488** | InvalidDefaultRootObject |  -  |
| **489** | InvalidRelativePath |  -  |
| **490** | InvalidErrorCode |  -  |
| **491** | InvalidResponseCode |  -  |
| **492** | InvalidArgument |  -  |
| **493** | InvalidOriginAccessIdentity |  -  |
| **494** | InvalidOriginAccessControl |  -  |
| **495** | TooManyTrustedSigners |  -  |
| **496** | TrustedSignerDoesNotExist |  -  |
| **497** | InvalidViewerCertificate |  -  |
| **498** | InvalidMinimumProtocolVersion |  -  |
| **499** | InvalidRequiredProtocol |  -  |
| **500** | NoSuchOrigin |  -  |
| **501** | TooManyOrigins |  -  |
| **502** | TooManyOriginGroupsPerDistribution |  -  |
| **503** | TooManyCacheBehaviors |  -  |
| **504** | TooManyCookieNamesInWhiteList |  -  |
| **505** | InvalidForwardCookies |  -  |
| **506** | TooManyHeadersInForwardedValues |  -  |
| **507** | InvalidHeadersForS3Origin |  -  |
| **508** | InconsistentQuantities |  -  |
| **509** | TooManyCertificates |  -  |
| **510** | InvalidLocationCode |  -  |
| **511** | InvalidGeoRestrictionParameter |  -  |
| **512** | InvalidTTLOrder |  -  |
| **513** | InvalidWebACLId |  -  |
| **514** | TooManyOriginCustomHeaders |  -  |
| **515** | TooManyQueryStringParameters |  -  |
| **516** | InvalidQueryStringParameters |  -  |
| **517** | TooManyDistributionsWithLambdaAssociations |  -  |
| **518** | TooManyDistributionsWithSingleFunctionARN |  -  |
| **519** | TooManyLambdaFunctionAssociations |  -  |
| **520** | InvalidLambdaFunctionAssociation |  -  |
| **521** | TooManyDistributionsWithFunctionAssociations |  -  |
| **522** | TooManyFunctionAssociations |  -  |
| **523** | InvalidFunctionAssociation |  -  |
| **524** | InvalidOriginReadTimeout |  -  |
| **525** | InvalidOriginKeepaliveTimeout |  -  |
| **526** | NoSuchFieldLevelEncryptionConfig |  -  |
| **527** | IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior |  -  |
| **528** | TooManyDistributionsAssociatedToFieldLevelEncryptionConfig |  -  |
| **529** | NoSuchCachePolicy |  -  |
| **530** | TooManyDistributionsAssociatedToCachePolicy |  -  |
| **531** | TooManyDistributionsAssociatedToOriginAccessControl |  -  |
| **532** | NoSuchResponseHeadersPolicy |  -  |
| **533** | TooManyDistributionsAssociatedToResponseHeadersPolicy |  -  |
| **534** | NoSuchOriginRequestPolicy |  -  |
| **535** | TooManyDistributionsAssociatedToOriginRequestPolicy |  -  |
| **536** | TooManyDistributionsAssociatedToKeyGroup |  -  |
| **537** | TooManyKeyGroupsAssociatedToDistribution |  -  |
| **538** | TrustedKeyGroupDoesNotExist |  -  |
| **539** | NoSuchRealtimeLogConfig |  -  |
| **540** | RealtimeLogConfigOwnerMismatch |  -  |

<a id="updateFieldLevelEncryptionConfig20200531"></a>
# **updateFieldLevelEncryptionConfig20200531**
> UpdateFieldLevelEncryptionConfigResult updateFieldLevelEncryptionConfig20200531(id, createFieldLevelEncryptionConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Update a field-level encryption configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the configuration you want to update.
    CreateFieldLevelEncryptionConfig20200531Request createFieldLevelEncryptionConfig20200531Request = new CreateFieldLevelEncryptionConfig20200531Request(); // CreateFieldLevelEncryptionConfig20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the configuration identity to update. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateFieldLevelEncryptionConfigResult result = apiInstance.updateFieldLevelEncryptionConfig20200531(id, createFieldLevelEncryptionConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateFieldLevelEncryptionConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the configuration you want to update. | |
| **createFieldLevelEncryptionConfig20200531Request** | [**CreateFieldLevelEncryptionConfig20200531Request**](CreateFieldLevelEncryptionConfig20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the configuration identity to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

[**UpdateFieldLevelEncryptionConfigResult**](UpdateFieldLevelEncryptionConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | IllegalUpdate |  -  |
| **482** | InconsistentQuantities |  -  |
| **483** | InvalidArgument |  -  |
| **484** | InvalidIfMatchVersion |  -  |
| **485** | NoSuchFieldLevelEncryptionProfile |  -  |
| **486** | NoSuchFieldLevelEncryptionConfig |  -  |
| **487** | PreconditionFailed |  -  |
| **488** | TooManyFieldLevelEncryptionQueryArgProfiles |  -  |
| **489** | TooManyFieldLevelEncryptionContentTypeProfiles |  -  |
| **490** | QueryArgProfileEmpty |  -  |

<a id="updateFieldLevelEncryptionProfile20200531"></a>
# **updateFieldLevelEncryptionProfile20200531**
> UpdateFieldLevelEncryptionProfileResult updateFieldLevelEncryptionProfile20200531(id, createFieldLevelEncryptionProfile20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Update a field-level encryption profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the field-level encryption profile request.
    CreateFieldLevelEncryptionProfile20200531Request createFieldLevelEncryptionProfile20200531Request = new CreateFieldLevelEncryptionProfile20200531Request(); // CreateFieldLevelEncryptionProfile20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the profile identity to update. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateFieldLevelEncryptionProfileResult result = apiInstance.updateFieldLevelEncryptionProfile20200531(id, createFieldLevelEncryptionProfile20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateFieldLevelEncryptionProfile20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The ID of the field-level encryption profile request. | |
| **createFieldLevelEncryptionProfile20200531Request** | [**CreateFieldLevelEncryptionProfile20200531Request**](CreateFieldLevelEncryptionProfile20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the profile identity to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

[**UpdateFieldLevelEncryptionProfileResult**](UpdateFieldLevelEncryptionProfileResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | FieldLevelEncryptionProfileAlreadyExists |  -  |
| **482** | IllegalUpdate |  -  |
| **483** | InconsistentQuantities |  -  |
| **484** | InvalidArgument |  -  |
| **485** | InvalidIfMatchVersion |  -  |
| **486** | NoSuchPublicKey |  -  |
| **487** | NoSuchFieldLevelEncryptionProfile |  -  |
| **488** | PreconditionFailed |  -  |
| **489** | FieldLevelEncryptionProfileSizeExceeded |  -  |
| **490** | TooManyFieldLevelEncryptionEncryptionEntities |  -  |
| **491** | TooManyFieldLevelEncryptionFieldPatterns |  -  |

<a id="updateFunction20200531"></a>
# **updateFunction20200531**
> UpdateFunctionResult updateFunction20200531(name, ifMatch, updateFunction20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates a CloudFront function.&lt;/p&gt; &lt;p&gt;You can update a function&#39;s code or the comment that describes the function. You cannot update a function&#39;s name.&lt;/p&gt; &lt;p&gt;To update a function, you provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value) along with the updated function code. To get the name and version, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the function that you are updating.
    String ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the function that you are updating, which you can get using <code>DescribeFunction</code>.
    UpdateFunction20200531Request updateFunction20200531Request = new UpdateFunction20200531Request(); // UpdateFunction20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateFunctionResult result = apiInstance.updateFunction20200531(name, ifMatch, updateFunction20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateFunction20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the function that you are updating. | |
| **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are updating, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;. | |
| **updateFunction20200531Request** | [**UpdateFunction20200531Request**](UpdateFunction20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateFunctionResult**](UpdateFunctionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgument |  -  |
| **481** | InvalidIfMatchVersion |  -  |
| **482** | NoSuchFunctionExists |  -  |
| **483** | PreconditionFailed |  -  |
| **484** | FunctionSizeLimitExceeded |  -  |
| **485** | UnsupportedOperation |  -  |

<a id="updateKeyGroup20200531"></a>
# **updateKeyGroup20200531**
> UpdateKeyGroupResult updateKeyGroup20200531(id, createKeyGroup20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Updates a key group.&lt;/p&gt; &lt;p&gt;When you update a key group, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a key group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Get the current key group with &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the key group that you want to update. For example, add or remove public key IDs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateKeyGroup&lt;/code&gt; with the entire key group object, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the key group that you are updating.
    CreateKeyGroup20200531Request createKeyGroup20200531Request = new CreateKeyGroup20200531Request(); // CreateKeyGroup20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The version of the key group that you are updating. The version is the key group's <code>ETag</code> value.
    try {
      UpdateKeyGroupResult result = apiInstance.updateKeyGroup20200531(id, createKeyGroup20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateKeyGroup20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the key group that you are updating. | |
| **createKeyGroup20200531Request** | [**CreateKeyGroup20200531Request**](CreateKeyGroup20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The version of the key group that you are updating. The version is the key group&#39;s &lt;code&gt;ETag&lt;/code&gt; value. | [optional] |

### Return type

[**UpdateKeyGroupResult**](UpdateKeyGroupResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidIfMatchVersion |  -  |
| **481** | NoSuchResource |  -  |
| **482** | PreconditionFailed |  -  |
| **483** | KeyGroupAlreadyExists |  -  |
| **484** | InvalidArgument |  -  |
| **485** | TooManyPublicKeysInKeyGroup |  -  |

<a id="updateOriginAccessControl20200531"></a>
# **updateOriginAccessControl20200531**
> UpdateOriginAccessControlResult updateOriginAccessControl20200531(id, createOriginAccessControl20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Updates a CloudFront origin access control.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the origin access control that you are updating.
    CreateOriginAccessControl20200531Request createOriginAccessControl20200531Request = new CreateOriginAccessControl20200531Request(); // CreateOriginAccessControl20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The current version (<code>ETag</code> value) of the origin access control that you are updating.
    try {
      UpdateOriginAccessControlResult result = apiInstance.updateOriginAccessControl20200531(id, createOriginAccessControl20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateOriginAccessControl20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier of the origin access control that you are updating. | |
| **createOriginAccessControl20200531Request** | [**CreateOriginAccessControl20200531Request**](CreateOriginAccessControl20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the origin access control that you are updating. | [optional] |

### Return type

[**UpdateOriginAccessControlResult**](UpdateOriginAccessControlResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | IllegalUpdate |  -  |
| **482** | InvalidIfMatchVersion |  -  |
| **483** | OriginAccessControlAlreadyExists |  -  |
| **484** | NoSuchOriginAccessControl |  -  |
| **485** | PreconditionFailed |  -  |
| **486** | InvalidArgument |  -  |

<a id="updateOriginRequestPolicy20200531"></a>
# **updateOriginRequestPolicy20200531**
> UpdateOriginRequestPolicyResult updateOriginRequestPolicy20200531(id, createOriginRequestPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Updates an origin request policy configuration.&lt;/p&gt; &lt;p&gt;When you update an origin request policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update an origin request policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the origin request policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateOriginRequestPolicy&lt;/code&gt; by providing the entire origin request policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behavior's <code>OriginRequestPolicyId</code> field in the response to <code>GetDistributionConfig</code>.
    CreateOriginRequestPolicy20200531Request createOriginRequestPolicy20200531Request = new CreateOriginRequestPolicy20200531Request(); // CreateOriginRequestPolicy20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The version of the origin request policy that you are updating. The version is returned in the origin request policy's <code>ETag</code> field in the response to <code>GetOriginRequestPolicyConfig</code>.
    try {
      UpdateOriginRequestPolicyResult result = apiInstance.updateOriginRequestPolicy20200531(id, createOriginRequestPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateOriginRequestPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behavior&#39;s &lt;code&gt;OriginRequestPolicyId&lt;/code&gt; field in the response to &lt;code&gt;GetDistributionConfig&lt;/code&gt;. | |
| **createOriginRequestPolicy20200531Request** | [**CreateOriginRequestPolicy20200531Request**](CreateOriginRequestPolicy20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The version of the origin request policy that you are updating. The version is returned in the origin request policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt;. | [optional] |

### Return type

[**UpdateOriginRequestPolicyResult**](UpdateOriginRequestPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | IllegalUpdate |  -  |
| **482** | InconsistentQuantities |  -  |
| **483** | InvalidArgument |  -  |
| **484** | InvalidIfMatchVersion |  -  |
| **485** | NoSuchOriginRequestPolicy |  -  |
| **486** | PreconditionFailed |  -  |
| **487** | OriginRequestPolicyAlreadyExists |  -  |
| **488** | TooManyHeadersInOriginRequestPolicy |  -  |
| **489** | TooManyCookiesInOriginRequestPolicy |  -  |
| **490** | TooManyQueryStringsInOriginRequestPolicy |  -  |

<a id="updatePublicKey20200531"></a>
# **updatePublicKey20200531**
> UpdatePublicKeyResult updatePublicKey20200531(id, createPublicKey20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Update public key information. Note that the only value you can change is the comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier of the public key that you are updating.
    CreatePublicKey20200531Request createPublicKey20200531Request = new CreatePublicKey20200531Request(); // CreatePublicKey20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the public key to update. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdatePublicKeyResult result = apiInstance.updatePublicKey20200531(id, createPublicKey20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePublicKey20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier of the public key that you are updating. | |
| **createPublicKey20200531Request** | [**CreatePublicKey20200531Request**](CreatePublicKey20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the public key to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

[**UpdatePublicKeyResult**](UpdatePublicKeyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | CannotChangeImmutablePublicKeyFields |  -  |
| **482** | InvalidArgument |  -  |
| **483** | InvalidIfMatchVersion |  -  |
| **484** | IllegalUpdate |  -  |
| **485** | NoSuchPublicKey |  -  |
| **486** | PreconditionFailed |  -  |

<a id="updateRealtimeLogConfig20200531"></a>
# **updateRealtimeLogConfig20200531**
> UpdateRealtimeLogConfigResult updateRealtimeLogConfig20200531(updateRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates a real-time log configuration.&lt;/p&gt; &lt;p&gt;When you update a real-time log configuration, all the parameters are updated with the values provided in the request. You cannot update some parameters independent of others. To update a real-time log configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;GetRealtimeLogConfig&lt;/code&gt; to get the current real-time log configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the parameters in the real-time log configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call this API (&lt;code&gt;UpdateRealtimeLogConfig&lt;/code&gt;) by providing the entire real-time log configuration, including the parameters that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;You cannot update a real-time log configuration&#39;s &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;ARN&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UpdateRealtimeLogConfig20200531Request updateRealtimeLogConfig20200531Request = new UpdateRealtimeLogConfig20200531Request(); // UpdateRealtimeLogConfig20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateRealtimeLogConfigResult result = apiInstance.updateRealtimeLogConfig20200531(updateRealtimeLogConfig20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateRealtimeLogConfig20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **updateRealtimeLogConfig20200531Request** | [**UpdateRealtimeLogConfig20200531Request**](UpdateRealtimeLogConfig20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateRealtimeLogConfigResult**](UpdateRealtimeLogConfigResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchRealtimeLogConfig |  -  |
| **481** | InvalidArgument |  -  |
| **482** | AccessDenied |  -  |

<a id="updateResponseHeadersPolicy20200531"></a>
# **updateResponseHeadersPolicy20200531**
> UpdateResponseHeadersPolicyResult updateResponseHeadersPolicy20200531(id, createResponseHeadersPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Updates a response headers policy.&lt;/p&gt; &lt;p&gt;When you update a response headers policy, the entire policy is replaced. You cannot update some policy fields independent of others. To update a response headers policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt; to get the current policy&#39;s configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Modify the fields in the response headers policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateResponseHeadersPolicy&lt;/code&gt;, providing the entire response headers policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The identifier for the response headers policy that you are updating.
    CreateResponseHeadersPolicy20200531Request createResponseHeadersPolicy20200531Request = new CreateResponseHeadersPolicy20200531Request(); // CreateResponseHeadersPolicy20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | <p>The version of the response headers policy that you are updating.</p> <p>The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetResponseHeadersPolicyConfig</code>.</p>
    try {
      UpdateResponseHeadersPolicyResult result = apiInstance.updateResponseHeadersPolicy20200531(id, createResponseHeadersPolicy20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateResponseHeadersPolicy20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The identifier for the response headers policy that you are updating. | |
| **createResponseHeadersPolicy20200531Request** | [**CreateResponseHeadersPolicy20200531Request**](CreateResponseHeadersPolicy20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| &lt;p&gt;The version of the response headers policy that you are updating.&lt;/p&gt; &lt;p&gt;The version is returned in the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt;.&lt;/p&gt; | [optional] |

### Return type

[**UpdateResponseHeadersPolicyResult**](UpdateResponseHeadersPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | IllegalUpdate |  -  |
| **482** | InconsistentQuantities |  -  |
| **483** | InvalidArgument |  -  |
| **484** | InvalidIfMatchVersion |  -  |
| **485** | NoSuchResponseHeadersPolicy |  -  |
| **486** | PreconditionFailed |  -  |
| **487** | ResponseHeadersPolicyAlreadyExists |  -  |
| **488** | TooManyCustomHeadersInResponseHeadersPolicy |  -  |
| **489** | TooLongCSPInResponseHeadersPolicy |  -  |
| **490** | TooManyRemoveHeadersInResponseHeadersPolicy |  -  |

<a id="updateStreamingDistribution20200531"></a>
# **updateStreamingDistribution20200531**
> UpdateStreamingDistributionResult updateStreamingDistribution20200531(id, createStreamingDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



Update a streaming distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudfront.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The streaming distribution's id.
    CreateStreamingDistribution20200531Request createStreamingDistribution20200531Request = new CreateStreamingDistribution20200531Request(); // CreateStreamingDistribution20200531Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the streaming distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateStreamingDistributionResult result = apiInstance.updateStreamingDistribution20200531(id, createStreamingDistribution20200531Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateStreamingDistribution20200531");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The streaming distribution&#39;s id. | |
| **createStreamingDistribution20200531Request** | [**CreateStreamingDistribution20200531Request**](CreateStreamingDistribution20200531Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the streaming distribution&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;. | [optional] |

### Return type

[**UpdateStreamingDistributionResult**](UpdateStreamingDistributionResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AccessDenied |  -  |
| **481** | CNAMEAlreadyExists |  -  |
| **482** | IllegalUpdate |  -  |
| **483** | InvalidIfMatchVersion |  -  |
| **484** | MissingBody |  -  |
| **485** | NoSuchStreamingDistribution |  -  |
| **486** | PreconditionFailed |  -  |
| **487** | TooManyStreamingDistributionCNAMEs |  -  |
| **488** | InvalidArgument |  -  |
| **489** | InvalidOriginAccessIdentity |  -  |
| **490** | InvalidOriginAccessControl |  -  |
| **491** | TooManyTrustedSigners |  -  |
| **492** | TrustedSignerDoesNotExist |  -  |
| **493** | InconsistentQuantities |  -  |

