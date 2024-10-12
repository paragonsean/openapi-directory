# DefaultApi

All URIs are relative to *https://cloudfront.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCloudFrontOriginAccessIdentity20171030**](DefaultApi.md#createCloudFrontOriginAccessIdentity20171030) | **POST** /2017-10-30/origin-access-identity/cloudfront |  |
| [**createDistribution20171030**](DefaultApi.md#createDistribution20171030) | **POST** /2017-10-30/distribution |  |
| [**createDistributionWithTags20171030**](DefaultApi.md#createDistributionWithTags20171030) | **POST** /2017-10-30/distribution#WithTags |  |
| [**createFieldLevelEncryptionConfig20171030**](DefaultApi.md#createFieldLevelEncryptionConfig20171030) | **POST** /2017-10-30/field-level-encryption |  |
| [**createFieldLevelEncryptionProfile20171030**](DefaultApi.md#createFieldLevelEncryptionProfile20171030) | **POST** /2017-10-30/field-level-encryption-profile |  |
| [**createInvalidation20171030**](DefaultApi.md#createInvalidation20171030) | **POST** /2017-10-30/distribution/{DistributionId}/invalidation |  |
| [**createPublicKey20171030**](DefaultApi.md#createPublicKey20171030) | **POST** /2017-10-30/public-key |  |
| [**createStreamingDistribution20171030**](DefaultApi.md#createStreamingDistribution20171030) | **POST** /2017-10-30/streaming-distribution |  |
| [**createStreamingDistributionWithTags20171030**](DefaultApi.md#createStreamingDistributionWithTags20171030) | **POST** /2017-10-30/streaming-distribution#WithTags |  |
| [**deleteCloudFrontOriginAccessIdentity20171030**](DefaultApi.md#deleteCloudFrontOriginAccessIdentity20171030) | **DELETE** /2017-10-30/origin-access-identity/cloudfront/{Id} |  |
| [**deleteDistribution20171030**](DefaultApi.md#deleteDistribution20171030) | **DELETE** /2017-10-30/distribution/{Id} |  |
| [**deleteFieldLevelEncryptionConfig20171030**](DefaultApi.md#deleteFieldLevelEncryptionConfig20171030) | **DELETE** /2017-10-30/field-level-encryption/{Id} |  |
| [**deleteFieldLevelEncryptionProfile20171030**](DefaultApi.md#deleteFieldLevelEncryptionProfile20171030) | **DELETE** /2017-10-30/field-level-encryption-profile/{Id} |  |
| [**deletePublicKey20171030**](DefaultApi.md#deletePublicKey20171030) | **DELETE** /2017-10-30/public-key/{Id} |  |
| [**deleteStreamingDistribution20171030**](DefaultApi.md#deleteStreamingDistribution20171030) | **DELETE** /2017-10-30/streaming-distribution/{Id} |  |
| [**getCloudFrontOriginAccessIdentity20171030**](DefaultApi.md#getCloudFrontOriginAccessIdentity20171030) | **GET** /2017-10-30/origin-access-identity/cloudfront/{Id} |  |
| [**getCloudFrontOriginAccessIdentityConfig20171030**](DefaultApi.md#getCloudFrontOriginAccessIdentityConfig20171030) | **GET** /2017-10-30/origin-access-identity/cloudfront/{Id}/config |  |
| [**getDistribution20171030**](DefaultApi.md#getDistribution20171030) | **GET** /2017-10-30/distribution/{Id} |  |
| [**getDistributionConfig20171030**](DefaultApi.md#getDistributionConfig20171030) | **GET** /2017-10-30/distribution/{Id}/config |  |
| [**getFieldLevelEncryption20171030**](DefaultApi.md#getFieldLevelEncryption20171030) | **GET** /2017-10-30/field-level-encryption/{Id} |  |
| [**getFieldLevelEncryptionConfig20171030**](DefaultApi.md#getFieldLevelEncryptionConfig20171030) | **GET** /2017-10-30/field-level-encryption/{Id}/config |  |
| [**getFieldLevelEncryptionProfile20171030**](DefaultApi.md#getFieldLevelEncryptionProfile20171030) | **GET** /2017-10-30/field-level-encryption-profile/{Id} |  |
| [**getFieldLevelEncryptionProfileConfig20171030**](DefaultApi.md#getFieldLevelEncryptionProfileConfig20171030) | **GET** /2017-10-30/field-level-encryption-profile/{Id}/config |  |
| [**getInvalidation20171030**](DefaultApi.md#getInvalidation20171030) | **GET** /2017-10-30/distribution/{DistributionId}/invalidation/{Id} |  |
| [**getPublicKey20171030**](DefaultApi.md#getPublicKey20171030) | **GET** /2017-10-30/public-key/{Id} |  |
| [**getPublicKeyConfig20171030**](DefaultApi.md#getPublicKeyConfig20171030) | **GET** /2017-10-30/public-key/{Id}/config |  |
| [**getStreamingDistribution20171030**](DefaultApi.md#getStreamingDistribution20171030) | **GET** /2017-10-30/streaming-distribution/{Id} |  |
| [**getStreamingDistributionConfig20171030**](DefaultApi.md#getStreamingDistributionConfig20171030) | **GET** /2017-10-30/streaming-distribution/{Id}/config |  |
| [**listCloudFrontOriginAccessIdentities20171030**](DefaultApi.md#listCloudFrontOriginAccessIdentities20171030) | **GET** /2017-10-30/origin-access-identity/cloudfront |  |
| [**listDistributions20171030**](DefaultApi.md#listDistributions20171030) | **GET** /2017-10-30/distribution |  |
| [**listDistributionsByWebACLId20171030**](DefaultApi.md#listDistributionsByWebACLId20171030) | **GET** /2017-10-30/distributionsByWebACLId/{WebACLId} |  |
| [**listFieldLevelEncryptionConfigs20171030**](DefaultApi.md#listFieldLevelEncryptionConfigs20171030) | **GET** /2017-10-30/field-level-encryption |  |
| [**listFieldLevelEncryptionProfiles20171030**](DefaultApi.md#listFieldLevelEncryptionProfiles20171030) | **GET** /2017-10-30/field-level-encryption-profile |  |
| [**listInvalidations20171030**](DefaultApi.md#listInvalidations20171030) | **GET** /2017-10-30/distribution/{DistributionId}/invalidation |  |
| [**listPublicKeys20171030**](DefaultApi.md#listPublicKeys20171030) | **GET** /2017-10-30/public-key |  |
| [**listStreamingDistributions20171030**](DefaultApi.md#listStreamingDistributions20171030) | **GET** /2017-10-30/streaming-distribution |  |
| [**listTagsForResource20171030**](DefaultApi.md#listTagsForResource20171030) | **GET** /2017-10-30/tagging#Resource |  |
| [**tagResource20171030**](DefaultApi.md#tagResource20171030) | **POST** /2017-10-30/tagging#Operation&#x3D;Tag&amp;Resource |  |
| [**untagResource20171030**](DefaultApi.md#untagResource20171030) | **POST** /2017-10-30/tagging#Operation&#x3D;Untag&amp;Resource |  |
| [**updateCloudFrontOriginAccessIdentity20171030**](DefaultApi.md#updateCloudFrontOriginAccessIdentity20171030) | **PUT** /2017-10-30/origin-access-identity/cloudfront/{Id}/config |  |
| [**updateDistribution20171030**](DefaultApi.md#updateDistribution20171030) | **PUT** /2017-10-30/distribution/{Id}/config |  |
| [**updateFieldLevelEncryptionConfig20171030**](DefaultApi.md#updateFieldLevelEncryptionConfig20171030) | **PUT** /2017-10-30/field-level-encryption/{Id}/config |  |
| [**updateFieldLevelEncryptionProfile20171030**](DefaultApi.md#updateFieldLevelEncryptionProfile20171030) | **PUT** /2017-10-30/field-level-encryption-profile/{Id}/config |  |
| [**updatePublicKey20171030**](DefaultApi.md#updatePublicKey20171030) | **PUT** /2017-10-30/public-key/{Id}/config |  |
| [**updateStreamingDistribution20171030**](DefaultApi.md#updateStreamingDistribution20171030) | **PUT** /2017-10-30/streaming-distribution/{Id}/config |  |


<a id="createCloudFrontOriginAccessIdentity20171030"></a>
# **createCloudFrontOriginAccessIdentity20171030**
> CreateCloudFrontOriginAccessIdentityResult createCloudFrontOriginAccessIdentity20171030(createCloudFrontOriginAccessIdentity20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a new origin access identity. If you&#39;re using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving Private Content through CloudFront&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.

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
    CreateCloudFrontOriginAccessIdentity20171030Request createCloudFrontOriginAccessIdentity20171030Request = new CreateCloudFrontOriginAccessIdentity20171030Request(); // CreateCloudFrontOriginAccessIdentity20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateCloudFrontOriginAccessIdentityResult result = apiInstance.createCloudFrontOriginAccessIdentity20171030(createCloudFrontOriginAccessIdentity20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createCloudFrontOriginAccessIdentity20171030");
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
| **createCloudFrontOriginAccessIdentity20171030Request** | [**CreateCloudFrontOriginAccessIdentity20171030Request**](CreateCloudFrontOriginAccessIdentity20171030Request.md)|  | |
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

<a id="createDistribution20171030"></a>
# **createDistribution20171030**
> CreateDistributionResult createDistribution20171030(createDistribution20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a new web distribution. Send a &lt;code&gt;POST&lt;/code&gt; request to the &lt;code&gt;/&lt;i&gt;CloudFront API version&lt;/i&gt;/distribution&lt;/code&gt;/&lt;code&gt;distribution ID&lt;/code&gt; resource.

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
    CreateDistribution20171030Request createDistribution20171030Request = new CreateDistribution20171030Request(); // CreateDistribution20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDistributionResult result = apiInstance.createDistribution20171030(createDistribution20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDistribution20171030");
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
| **createDistribution20171030Request** | [**CreateDistribution20171030Request**](CreateDistribution20171030Request.md)|  | |
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
| **484** | AccessDenied |  -  |
| **485** | TooManyTrustedSigners |  -  |
| **486** | TrustedSignerDoesNotExist |  -  |
| **487** | InvalidViewerCertificate |  -  |
| **488** | InvalidMinimumProtocolVersion |  -  |
| **489** | MissingBody |  -  |
| **490** | TooManyDistributionCNAMEs |  -  |
| **491** | TooManyDistributions |  -  |
| **492** | InvalidDefaultRootObject |  -  |
| **493** | InvalidRelativePath |  -  |
| **494** | InvalidErrorCode |  -  |
| **495** | InvalidResponseCode |  -  |
| **496** | InvalidArgument |  -  |
| **497** | InvalidRequiredProtocol |  -  |
| **498** | NoSuchOrigin |  -  |
| **499** | TooManyOrigins |  -  |
| **500** | TooManyCacheBehaviors |  -  |
| **501** | TooManyCookieNamesInWhiteList |  -  |
| **502** | InvalidForwardCookies |  -  |
| **503** | TooManyHeadersInForwardedValues |  -  |
| **504** | InvalidHeadersForS3Origin |  -  |
| **505** | InconsistentQuantities |  -  |
| **506** | TooManyCertificates |  -  |
| **507** | InvalidLocationCode |  -  |
| **508** | InvalidGeoRestrictionParameter |  -  |
| **509** | InvalidProtocolSettings |  -  |
| **510** | InvalidTTLOrder |  -  |
| **511** | InvalidWebACLId |  -  |
| **512** | TooManyOriginCustomHeaders |  -  |
| **513** | TooManyQueryStringParameters |  -  |
| **514** | InvalidQueryStringParameters |  -  |
| **515** | TooManyDistributionsWithLambdaAssociations |  -  |
| **516** | TooManyLambdaFunctionAssociations |  -  |
| **517** | InvalidLambdaFunctionAssociation |  -  |
| **518** | InvalidOriginReadTimeout |  -  |
| **519** | InvalidOriginKeepaliveTimeout |  -  |
| **520** | NoSuchFieldLevelEncryptionConfig |  -  |
| **521** | IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior |  -  |
| **522** | TooManyDistributionsAssociatedToFieldLevelEncryptionConfig |  -  |

<a id="createDistributionWithTags20171030"></a>
# **createDistributionWithTags20171030**
> CreateDistributionWithTagsResult createDistributionWithTags20171030(withTags, createDistributionWithTags20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Create a new distribution with tags.

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
    CreateDistributionWithTags20171030Request createDistributionWithTags20171030Request = new CreateDistributionWithTags20171030Request(); // CreateDistributionWithTags20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateDistributionWithTagsResult result = apiInstance.createDistributionWithTags20171030(withTags, createDistributionWithTags20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDistributionWithTags20171030");
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
| **createDistributionWithTags20171030Request** | [**CreateDistributionWithTags20171030Request**](CreateDistributionWithTags20171030Request.md)|  | |
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
| **484** | AccessDenied |  -  |
| **485** | TooManyTrustedSigners |  -  |
| **486** | TrustedSignerDoesNotExist |  -  |
| **487** | InvalidViewerCertificate |  -  |
| **488** | InvalidMinimumProtocolVersion |  -  |
| **489** | MissingBody |  -  |
| **490** | TooManyDistributionCNAMEs |  -  |
| **491** | TooManyDistributions |  -  |
| **492** | InvalidDefaultRootObject |  -  |
| **493** | InvalidRelativePath |  -  |
| **494** | InvalidErrorCode |  -  |
| **495** | InvalidResponseCode |  -  |
| **496** | InvalidArgument |  -  |
| **497** | InvalidRequiredProtocol |  -  |
| **498** | NoSuchOrigin |  -  |
| **499** | TooManyOrigins |  -  |
| **500** | TooManyCacheBehaviors |  -  |
| **501** | TooManyCookieNamesInWhiteList |  -  |
| **502** | InvalidForwardCookies |  -  |
| **503** | TooManyHeadersInForwardedValues |  -  |
| **504** | InvalidHeadersForS3Origin |  -  |
| **505** | InconsistentQuantities |  -  |
| **506** | TooManyCertificates |  -  |
| **507** | InvalidLocationCode |  -  |
| **508** | InvalidGeoRestrictionParameter |  -  |
| **509** | InvalidProtocolSettings |  -  |
| **510** | InvalidTTLOrder |  -  |
| **511** | InvalidWebACLId |  -  |
| **512** | TooManyOriginCustomHeaders |  -  |
| **513** | InvalidTagging |  -  |
| **514** | TooManyQueryStringParameters |  -  |
| **515** | InvalidQueryStringParameters |  -  |
| **516** | TooManyDistributionsWithLambdaAssociations |  -  |
| **517** | TooManyLambdaFunctionAssociations |  -  |
| **518** | InvalidLambdaFunctionAssociation |  -  |
| **519** | InvalidOriginReadTimeout |  -  |
| **520** | InvalidOriginKeepaliveTimeout |  -  |
| **521** | NoSuchFieldLevelEncryptionConfig |  -  |
| **522** | IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior |  -  |
| **523** | TooManyDistributionsAssociatedToFieldLevelEncryptionConfig |  -  |

<a id="createFieldLevelEncryptionConfig20171030"></a>
# **createFieldLevelEncryptionConfig20171030**
> CreateFieldLevelEncryptionConfigResult createFieldLevelEncryptionConfig20171030(createFieldLevelEncryptionConfig20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    CreateFieldLevelEncryptionConfig20171030Request createFieldLevelEncryptionConfig20171030Request = new CreateFieldLevelEncryptionConfig20171030Request(); // CreateFieldLevelEncryptionConfig20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateFieldLevelEncryptionConfigResult result = apiInstance.createFieldLevelEncryptionConfig20171030(createFieldLevelEncryptionConfig20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createFieldLevelEncryptionConfig20171030");
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
| **createFieldLevelEncryptionConfig20171030Request** | [**CreateFieldLevelEncryptionConfig20171030Request**](CreateFieldLevelEncryptionConfig20171030Request.md)|  | |
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

<a id="createFieldLevelEncryptionProfile20171030"></a>
# **createFieldLevelEncryptionProfile20171030**
> CreateFieldLevelEncryptionProfileResult createFieldLevelEncryptionProfile20171030(createFieldLevelEncryptionProfile20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    CreateFieldLevelEncryptionProfile20171030Request createFieldLevelEncryptionProfile20171030Request = new CreateFieldLevelEncryptionProfile20171030Request(); // CreateFieldLevelEncryptionProfile20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateFieldLevelEncryptionProfileResult result = apiInstance.createFieldLevelEncryptionProfile20171030(createFieldLevelEncryptionProfile20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createFieldLevelEncryptionProfile20171030");
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
| **createFieldLevelEncryptionProfile20171030Request** | [**CreateFieldLevelEncryptionProfile20171030Request**](CreateFieldLevelEncryptionProfile20171030Request.md)|  | |
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

<a id="createInvalidation20171030"></a>
# **createInvalidation20171030**
> CreateInvalidationResult createInvalidation20171030(distributionId, createInvalidation20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    CreateInvalidation20171030Request createInvalidation20171030Request = new CreateInvalidation20171030Request(); // CreateInvalidation20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateInvalidationResult result = apiInstance.createInvalidation20171030(distributionId, createInvalidation20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createInvalidation20171030");
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
| **createInvalidation20171030Request** | [**CreateInvalidation20171030Request**](CreateInvalidation20171030Request.md)|  | |
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

<a id="createPublicKey20171030"></a>
# **createPublicKey20171030**
> CreatePublicKeyResult createPublicKey20171030(createPublicKey20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Add a new public key to CloudFront to use, for example, for field-level encryption. You can add a maximum of 10 public keys with one AWS account.

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
    CreatePublicKey20171030Request createPublicKey20171030Request = new CreatePublicKey20171030Request(); // CreatePublicKey20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreatePublicKeyResult result = apiInstance.createPublicKey20171030(createPublicKey20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createPublicKey20171030");
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
| **createPublicKey20171030Request** | [**CreatePublicKey20171030Request**](CreatePublicKey20171030Request.md)|  | |
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

<a id="createStreamingDistribution20171030"></a>
# **createStreamingDistribution20171030**
> CreateStreamingDistributionResult createStreamingDistribution20171030(createStreamingDistribution20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new RMTP distribution. An RTMP distribution is similar to a web distribution, but an RTMP distribution streams media files using the Adobe Real-Time Messaging Protocol (RTMP) instead of serving files using HTTP. &lt;/p&gt; &lt;p&gt;To create a new web distribution, submit a &lt;code&gt;POST&lt;/code&gt; request to the &lt;i&gt;CloudFront API version&lt;/i&gt;/distribution resource. The request body must include a document with a &lt;i&gt;StreamingDistributionConfig&lt;/i&gt; element. The response echoes the &lt;code&gt;StreamingDistributionConfig&lt;/code&gt; element and returns other information about the RTMP distribution.&lt;/p&gt; &lt;p&gt;To get the status of your request, use the &lt;i&gt;GET StreamingDistribution&lt;/i&gt; API action. When the value of &lt;code&gt;Enabled&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt; and the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;, your distribution is ready. A distribution usually deploys in less than 15 minutes.&lt;/p&gt; &lt;p&gt;For more information about web distributions, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-rtmp.html\&quot;&gt;Working with RTMP Distributions&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Beginning with the 2012-05-05 version of the CloudFront API, we made substantial changes to the format of the XML document that you include in the request body when you create or update a web distribution or an RTMP distribution, and when you invalidate objects. With previous versions of the API, we discovered that it was too easy to accidentally delete one or more values for an element that accepts multiple values, for example, CNAMEs and trusted signers. Our changes for the 2012-05-05 release are intended to prevent these accidental deletions and to notify you when there&#39;s a mismatch between the number of values you say you&#39;re specifying in the &lt;code&gt;Quantity&lt;/code&gt; element and the number of values specified.&lt;/p&gt; &lt;/important&gt;

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
    CreateStreamingDistribution20171030Request createStreamingDistribution20171030Request = new CreateStreamingDistribution20171030Request(); // CreateStreamingDistribution20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateStreamingDistributionResult result = apiInstance.createStreamingDistribution20171030(createStreamingDistribution20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createStreamingDistribution20171030");
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
| **createStreamingDistribution20171030Request** | [**CreateStreamingDistribution20171030Request**](CreateStreamingDistribution20171030Request.md)|  | |
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
| **484** | AccessDenied |  -  |
| **485** | TooManyTrustedSigners |  -  |
| **486** | TrustedSignerDoesNotExist |  -  |
| **487** | MissingBody |  -  |
| **488** | TooManyStreamingDistributionCNAMEs |  -  |
| **489** | TooManyStreamingDistributions |  -  |
| **490** | InvalidArgument |  -  |
| **491** | InconsistentQuantities |  -  |

<a id="createStreamingDistributionWithTags20171030"></a>
# **createStreamingDistributionWithTags20171030**
> CreateStreamingDistributionWithTagsResult createStreamingDistributionWithTags20171030(withTags, createStreamingDistributionWithTags20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Create a new streaming distribution with tags.

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
    CreateStreamingDistributionWithTags20171030Request createStreamingDistributionWithTags20171030Request = new CreateStreamingDistributionWithTags20171030Request(); // CreateStreamingDistributionWithTags20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateStreamingDistributionWithTagsResult result = apiInstance.createStreamingDistributionWithTags20171030(withTags, createStreamingDistributionWithTags20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createStreamingDistributionWithTags20171030");
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
| **createStreamingDistributionWithTags20171030Request** | [**CreateStreamingDistributionWithTags20171030Request**](CreateStreamingDistributionWithTags20171030Request.md)|  | |
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
| **484** | AccessDenied |  -  |
| **485** | TooManyTrustedSigners |  -  |
| **486** | TrustedSignerDoesNotExist |  -  |
| **487** | MissingBody |  -  |
| **488** | TooManyStreamingDistributionCNAMEs |  -  |
| **489** | TooManyStreamingDistributions |  -  |
| **490** | InvalidArgument |  -  |
| **491** | InconsistentQuantities |  -  |
| **492** | InvalidTagging |  -  |

<a id="deleteCloudFrontOriginAccessIdentity20171030"></a>
# **deleteCloudFrontOriginAccessIdentity20171030**
> deleteCloudFrontOriginAccessIdentity20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
      apiInstance.deleteCloudFrontOriginAccessIdentity20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteCloudFrontOriginAccessIdentity20171030");
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

<a id="deleteDistribution20171030"></a>
# **deleteDistribution20171030**
> deleteDistribution20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
      apiInstance.deleteDistribution20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDistribution20171030");
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
| **id** | **String**| The distribution ID.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when you disabled the distribution. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.  | [optional] |

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

<a id="deleteFieldLevelEncryptionConfig20171030"></a>
# **deleteFieldLevelEncryptionConfig20171030**
> deleteFieldLevelEncryptionConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
      apiInstance.deleteFieldLevelEncryptionConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteFieldLevelEncryptionConfig20171030");
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

<a id="deleteFieldLevelEncryptionProfile20171030"></a>
# **deleteFieldLevelEncryptionProfile20171030**
> deleteFieldLevelEncryptionProfile20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
      apiInstance.deleteFieldLevelEncryptionProfile20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteFieldLevelEncryptionProfile20171030");
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

<a id="deletePublicKey20171030"></a>
# **deletePublicKey20171030**
> deletePublicKey20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
      apiInstance.deletePublicKey20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePublicKey20171030");
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

<a id="deleteStreamingDistribution20171030"></a>
# **deleteStreamingDistribution20171030**
> deleteStreamingDistribution20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To delete an RTMP distribution using the CloudFront API&lt;/b&gt;:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Disable the RTMP distribution.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to get the current configuration and the &lt;code&gt;Etag&lt;/code&gt; header for the distribution. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to change the value of &lt;code&gt;Enabled&lt;/code&gt; to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to confirm that the distribution was successfully disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request. Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to your &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request to confirm that the distribution was successfully deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For information about deleting a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html\&quot;&gt;Deleting a Distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
      apiInstance.deleteStreamingDistribution20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteStreamingDistribution20171030");
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
| **id** | **String**| The distribution ID.  | |
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

<a id="getCloudFrontOriginAccessIdentity20171030"></a>
# **getCloudFrontOriginAccessIdentity20171030**
> GetCloudFrontOriginAccessIdentityResult getCloudFrontOriginAccessIdentity20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetCloudFrontOriginAccessIdentityResult result = apiInstance.getCloudFrontOriginAccessIdentity20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCloudFrontOriginAccessIdentity20171030");
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

<a id="getCloudFrontOriginAccessIdentityConfig20171030"></a>
# **getCloudFrontOriginAccessIdentityConfig20171030**
> GetCloudFrontOriginAccessIdentityConfigResult getCloudFrontOriginAccessIdentityConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetCloudFrontOriginAccessIdentityConfigResult result = apiInstance.getCloudFrontOriginAccessIdentityConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCloudFrontOriginAccessIdentityConfig20171030");
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
| **id** | **String**| The identity&#39;s ID.  | |
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

<a id="getDistribution20171030"></a>
# **getDistribution20171030**
> GetDistributionResult getDistribution20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    String id = "id_example"; // String | The distribution's ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDistributionResult result = apiInstance.getDistribution20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDistribution20171030");
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
| **id** | **String**| The distribution&#39;s ID. | |
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

<a id="getDistributionConfig20171030"></a>
# **getDistributionConfig20171030**
> GetDistributionConfigResult getDistributionConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    String id = "id_example"; // String | The distribution's ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDistributionConfigResult result = apiInstance.getDistributionConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDistributionConfig20171030");
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
| **id** | **String**| The distribution&#39;s ID. | |
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

<a id="getFieldLevelEncryption20171030"></a>
# **getFieldLevelEncryption20171030**
> GetFieldLevelEncryptionResult getFieldLevelEncryption20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetFieldLevelEncryptionResult result = apiInstance.getFieldLevelEncryption20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldLevelEncryption20171030");
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

<a id="getFieldLevelEncryptionConfig20171030"></a>
# **getFieldLevelEncryptionConfig20171030**
> GetFieldLevelEncryptionConfigResult getFieldLevelEncryptionConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetFieldLevelEncryptionConfigResult result = apiInstance.getFieldLevelEncryptionConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldLevelEncryptionConfig20171030");
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

<a id="getFieldLevelEncryptionProfile20171030"></a>
# **getFieldLevelEncryptionProfile20171030**
> GetFieldLevelEncryptionProfileResult getFieldLevelEncryptionProfile20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetFieldLevelEncryptionProfileResult result = apiInstance.getFieldLevelEncryptionProfile20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldLevelEncryptionProfile20171030");
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

<a id="getFieldLevelEncryptionProfileConfig20171030"></a>
# **getFieldLevelEncryptionProfileConfig20171030**
> GetFieldLevelEncryptionProfileConfigResult getFieldLevelEncryptionProfileConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetFieldLevelEncryptionProfileConfigResult result = apiInstance.getFieldLevelEncryptionProfileConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldLevelEncryptionProfileConfig20171030");
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

<a id="getInvalidation20171030"></a>
# **getInvalidation20171030**
> GetInvalidationResult getInvalidation20171030(distributionId, id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetInvalidationResult result = apiInstance.getInvalidation20171030(distributionId, id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getInvalidation20171030");
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

<a id="getPublicKey20171030"></a>
# **getPublicKey20171030**
> GetPublicKeyResult getPublicKey20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the public key information.

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
    String id = "id_example"; // String | Request the ID for the public key.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetPublicKeyResult result = apiInstance.getPublicKey20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPublicKey20171030");
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
| **id** | **String**| Request the ID for the public key. | |
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

<a id="getPublicKeyConfig20171030"></a>
# **getPublicKeyConfig20171030**
> GetPublicKeyConfigResult getPublicKeyConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Return public key configuration informaation

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
    String id = "id_example"; // String | Request the ID for the public key configuration.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetPublicKeyConfigResult result = apiInstance.getPublicKeyConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPublicKeyConfig20171030");
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
| **id** | **String**| Request the ID for the public key configuration. | |
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

<a id="getStreamingDistribution20171030"></a>
# **getStreamingDistribution20171030**
> GetStreamingDistributionResult getStreamingDistribution20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetStreamingDistributionResult result = apiInstance.getStreamingDistribution20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStreamingDistribution20171030");
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

<a id="getStreamingDistributionConfig20171030"></a>
# **getStreamingDistributionConfig20171030**
> GetStreamingDistributionConfigResult getStreamingDistributionConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
      GetStreamingDistributionConfigResult result = apiInstance.getStreamingDistributionConfig20171030(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStreamingDistributionConfig20171030");
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

<a id="listCloudFrontOriginAccessIdentities20171030"></a>
# **listCloudFrontOriginAccessIdentities20171030**
> ListCloudFrontOriginAccessIdentitiesResult listCloudFrontOriginAccessIdentities20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



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
      ListCloudFrontOriginAccessIdentitiesResult result = apiInstance.listCloudFrontOriginAccessIdentities20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCloudFrontOriginAccessIdentities20171030");
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
| **maxItems** | **String**| The maximum number of origin access identities you want in the response body.  | [optional] |

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

<a id="listDistributions20171030"></a>
# **listDistributions20171030**
> ListDistributionsResult listDistributions20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



List distributions. 

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
      ListDistributionsResult result = apiInstance.listDistributions20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributions20171030");
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

<a id="listDistributionsByWebACLId20171030"></a>
# **listDistributionsByWebACLId20171030**
> ListDistributionsByWebACLIdResult listDistributionsByWebACLId20171030(webACLId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



List the distributions that are associated with a specified AWS WAF web ACL. 

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
    String webACLId = "webACLId_example"; // String | The ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify \"null\" for the ID, the request returns a list of the distributions that aren't associated with a web ACL. 
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
      ListDistributionsByWebACLIdResult result = apiInstance.listDistributionsByWebACLId20171030(webACLId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistributionsByWebACLId20171030");
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
| **webACLId** | **String**| The ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify \&quot;null\&quot; for the ID, the request returns a list of the distributions that aren&#39;t associated with a web ACL.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **marker** | **String**| Use &lt;code&gt;Marker&lt;/code&gt; and &lt;code&gt;MaxItems&lt;/code&gt; to control pagination of results. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; distributions that satisfy the request, the response includes a &lt;code&gt;NextMarker&lt;/code&gt; element. To get the next page of results, submit another request. For the value of &lt;code&gt;Marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the last response. (For the first request, omit &lt;code&gt;Marker&lt;/code&gt;.)  | [optional] |
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

<a id="listFieldLevelEncryptionConfigs20171030"></a>
# **listFieldLevelEncryptionConfigs20171030**
> ListFieldLevelEncryptionConfigsResult listFieldLevelEncryptionConfigs20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



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
      ListFieldLevelEncryptionConfigsResult result = apiInstance.listFieldLevelEncryptionConfigs20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFieldLevelEncryptionConfigs20171030");
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
| **marker** | **String**| Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last configuration on that page).  | [optional] |
| **maxItems** | **String**| The maximum number of field-level encryption configurations you want in the response body.  | [optional] |

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

<a id="listFieldLevelEncryptionProfiles20171030"></a>
# **listFieldLevelEncryptionProfiles20171030**
> ListFieldLevelEncryptionProfilesResult listFieldLevelEncryptionProfiles20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



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
      ListFieldLevelEncryptionProfilesResult result = apiInstance.listFieldLevelEncryptionProfiles20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFieldLevelEncryptionProfiles20171030");
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
| **marker** | **String**| Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last profile on that page).  | [optional] |
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

<a id="listInvalidations20171030"></a>
# **listInvalidations20171030**
> ListInvalidationsResult listInvalidations20171030(distributionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



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
      ListInvalidationsResult result = apiInstance.listInvalidations20171030(distributionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listInvalidations20171030");
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
| **marker** | **String**| Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. This value is the same as the ID of the last invalidation batch on that page.  | [optional] |
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

<a id="listPublicKeys20171030"></a>
# **listPublicKeys20171030**
> ListPublicKeysResult listPublicKeys20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



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
      ListPublicKeysResult result = apiInstance.listPublicKeys20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPublicKeys20171030");
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
| **marker** | **String**| Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last public key on that page).  | [optional] |
| **maxItems** | **String**| The maximum number of public keys you want in the response body.  | [optional] |

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

<a id="listStreamingDistributions20171030"></a>
# **listStreamingDistributions20171030**
> ListStreamingDistributionsResult listStreamingDistributions20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems)



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
      ListStreamingDistributionsResult result = apiInstance.listStreamingDistributions20171030(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listStreamingDistributions20171030");
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

<a id="listTagsForResource20171030"></a>
# **listTagsForResource20171030**
> ListTagsForResourceResult listTagsForResource20171030(resource, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    String resource = "resource_example"; // String |  An ARN of a CloudFront resource.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResult result = apiInstance.listTagsForResource20171030(resource, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource20171030");
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
| **resource** | **String**|  An ARN of a CloudFront resource. | |
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

<a id="tagResource20171030"></a>
# **tagResource20171030**
> tagResource20171030(resource, operation, tagResource20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    String resource = "resource_example"; // String |  An ARN of a CloudFront resource.
    String operation = "Tag"; // String | 
    TagResource20171030Request tagResource20171030Request = new TagResource20171030Request(); // TagResource20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.tagResource20171030(resource, operation, tagResource20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource20171030");
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
| **resource** | **String**|  An ARN of a CloudFront resource. | |
| **operation** | **String**|  | [enum: Tag] |
| **tagResource20171030Request** | [**TagResource20171030Request**](TagResource20171030Request.md)|  | |
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

<a id="untagResource20171030"></a>
# **untagResource20171030**
> untagResource20171030(resource, operation, untagResource20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    String resource = "resource_example"; // String |  An ARN of a CloudFront resource.
    String operation = "Untag"; // String | 
    UntagResource20171030Request untagResource20171030Request = new UntagResource20171030Request(); // UntagResource20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.untagResource20171030(resource, operation, untagResource20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource20171030");
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
| **resource** | **String**|  An ARN of a CloudFront resource. | |
| **operation** | **String**|  | [enum: Untag] |
| **untagResource20171030Request** | [**UntagResource20171030Request**](UntagResource20171030Request.md)|  | |
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

<a id="updateCloudFrontOriginAccessIdentity20171030"></a>
# **updateCloudFrontOriginAccessIdentity20171030**
> UpdateCloudFrontOriginAccessIdentityResult updateCloudFrontOriginAccessIdentity20171030(id, createCloudFrontOriginAccessIdentity20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
    CreateCloudFrontOriginAccessIdentity20171030Request createCloudFrontOriginAccessIdentity20171030Request = new CreateCloudFrontOriginAccessIdentity20171030Request(); // CreateCloudFrontOriginAccessIdentity20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the identity's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateCloudFrontOriginAccessIdentityResult result = apiInstance.updateCloudFrontOriginAccessIdentity20171030(id, createCloudFrontOriginAccessIdentity20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateCloudFrontOriginAccessIdentity20171030");
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
| **createCloudFrontOriginAccessIdentity20171030Request** | [**CreateCloudFrontOriginAccessIdentity20171030Request**](CreateCloudFrontOriginAccessIdentity20171030Request.md)|  | |
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

<a id="updateDistribution20171030"></a>
# **updateDistribution20171030**
> UpdateDistributionResult updateDistribution20171030(id, createDistribution20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



&lt;p&gt;Updates the configuration for a web distribution. Perform the following steps.&lt;/p&gt; &lt;p&gt;For information about updating a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.html\&quot;&gt;Creating or Updating a Web Distribution Using the CloudFront Console &lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To update a web distribution using the CloudFront API&lt;/b&gt; &lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;a&gt;GetDistributionConfig&lt;/a&gt; request to get the current configuration and an &lt;code&gt;Etag&lt;/code&gt; header for the distribution.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you update the distribution again, you need to get a new &lt;code&gt;Etag&lt;/code&gt; header.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GetDistributionConfig&lt;/code&gt; request to include the desired changes. You can&#39;t change the value of &lt;code&gt;CallerReference&lt;/code&gt;. If you try to change this value, CloudFront returns an &lt;code&gt;IllegalUpdate&lt;/code&gt; error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The new configuration replaces the existing configuration; the values that you specify in an &lt;code&gt;UpdateDistribution&lt;/code&gt; request are not merged into the existing configuration. When you add, delete, or replace values in an element that allows multiple values (for example, &lt;code&gt;CNAME&lt;/code&gt;), you must specify all of the values that you want to appear in the updated distribution. In addition, you must update the corresponding &lt;code&gt;Quantity&lt;/code&gt; element.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateDistribution&lt;/code&gt; request to update the configuration for your distribution:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;In the request body, include the XML document that you updated in Step 2. The request body must include an XML document with a &lt;code&gt;DistributionConfig&lt;/code&gt; element.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GetDistributionConfig&lt;/code&gt; request in Step 1.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;UpdateDistribution&lt;/code&gt; request to confirm that the configuration was successfully updated.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Optional: Submit a &lt;a&gt;GetDistribution&lt;/a&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Beginning with the 2012-05-05 version of the CloudFront API, we made substantial changes to the format of the XML document that you include in the request body when you create or update a distribution. With previous versions of the API, we discovered that it was too easy to accidentally delete one or more values for an element that accepts multiple values, for example, CNAMEs and trusted signers. Our changes for the 2012-05-05 release are intended to prevent these accidental deletions and to notify you when there&#39;s a mismatch between the number of values you say you&#39;re specifying in the &lt;code&gt;Quantity&lt;/code&gt; element and the number of values you&#39;re actually specifying.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ol&gt;

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
    CreateDistribution20171030Request createDistribution20171030Request = new CreateDistribution20171030Request(); // CreateDistribution20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateDistributionResult result = apiInstance.updateDistribution20171030(id, createDistribution20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDistribution20171030");
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
| **createDistribution20171030Request** | [**CreateDistribution20171030Request**](CreateDistribution20171030Request.md)|  | |
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
| **494** | TooManyTrustedSigners |  -  |
| **495** | TrustedSignerDoesNotExist |  -  |
| **496** | InvalidViewerCertificate |  -  |
| **497** | InvalidMinimumProtocolVersion |  -  |
| **498** | InvalidRequiredProtocol |  -  |
| **499** | NoSuchOrigin |  -  |
| **500** | TooManyOrigins |  -  |
| **501** | TooManyCacheBehaviors |  -  |
| **502** | TooManyCookieNamesInWhiteList |  -  |
| **503** | InvalidForwardCookies |  -  |
| **504** | TooManyHeadersInForwardedValues |  -  |
| **505** | InvalidHeadersForS3Origin |  -  |
| **506** | InconsistentQuantities |  -  |
| **507** | TooManyCertificates |  -  |
| **508** | InvalidLocationCode |  -  |
| **509** | InvalidGeoRestrictionParameter |  -  |
| **510** | InvalidTTLOrder |  -  |
| **511** | InvalidWebACLId |  -  |
| **512** | TooManyOriginCustomHeaders |  -  |
| **513** | TooManyQueryStringParameters |  -  |
| **514** | InvalidQueryStringParameters |  -  |
| **515** | TooManyDistributionsWithLambdaAssociations |  -  |
| **516** | TooManyLambdaFunctionAssociations |  -  |
| **517** | InvalidLambdaFunctionAssociation |  -  |
| **518** | InvalidOriginReadTimeout |  -  |
| **519** | InvalidOriginKeepaliveTimeout |  -  |
| **520** | NoSuchFieldLevelEncryptionConfig |  -  |
| **521** | IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior |  -  |
| **522** | TooManyDistributionsAssociatedToFieldLevelEncryptionConfig |  -  |

<a id="updateFieldLevelEncryptionConfig20171030"></a>
# **updateFieldLevelEncryptionConfig20171030**
> UpdateFieldLevelEncryptionConfigResult updateFieldLevelEncryptionConfig20171030(id, createFieldLevelEncryptionConfig20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
    CreateFieldLevelEncryptionConfig20171030Request createFieldLevelEncryptionConfig20171030Request = new CreateFieldLevelEncryptionConfig20171030Request(); // CreateFieldLevelEncryptionConfig20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the configuration identity to update. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateFieldLevelEncryptionConfigResult result = apiInstance.updateFieldLevelEncryptionConfig20171030(id, createFieldLevelEncryptionConfig20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateFieldLevelEncryptionConfig20171030");
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
| **createFieldLevelEncryptionConfig20171030Request** | [**CreateFieldLevelEncryptionConfig20171030Request**](CreateFieldLevelEncryptionConfig20171030Request.md)|  | |
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

<a id="updateFieldLevelEncryptionProfile20171030"></a>
# **updateFieldLevelEncryptionProfile20171030**
> UpdateFieldLevelEncryptionProfileResult updateFieldLevelEncryptionProfile20171030(id, createFieldLevelEncryptionProfile20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
    CreateFieldLevelEncryptionProfile20171030Request createFieldLevelEncryptionProfile20171030Request = new CreateFieldLevelEncryptionProfile20171030Request(); // CreateFieldLevelEncryptionProfile20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the profile identity to update. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateFieldLevelEncryptionProfileResult result = apiInstance.updateFieldLevelEncryptionProfile20171030(id, createFieldLevelEncryptionProfile20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateFieldLevelEncryptionProfile20171030");
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
| **id** | **String**| The ID of the field-level encryption profile request.  | |
| **createFieldLevelEncryptionProfile20171030Request** | [**CreateFieldLevelEncryptionProfile20171030Request**](CreateFieldLevelEncryptionProfile20171030Request.md)|  | |
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

<a id="updatePublicKey20171030"></a>
# **updatePublicKey20171030**
> UpdatePublicKeyResult updatePublicKey20171030(id, createPublicKey20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
    String id = "id_example"; // String | ID of the public key to be updated.
    CreatePublicKey20171030Request createPublicKey20171030Request = new CreatePublicKey20171030Request(); // CreatePublicKey20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the public key to update. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdatePublicKeyResult result = apiInstance.updatePublicKey20171030(id, createPublicKey20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePublicKey20171030");
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
| **id** | **String**| ID of the public key to be updated. | |
| **createPublicKey20171030Request** | [**CreatePublicKey20171030Request**](CreatePublicKey20171030Request.md)|  | |
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

<a id="updateStreamingDistribution20171030"></a>
# **updateStreamingDistribution20171030**
> UpdateStreamingDistributionResult updateStreamingDistribution20171030(id, createStreamingDistribution20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch)



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
    CreateStreamingDistribution20171030Request createStreamingDistribution20171030Request = new CreateStreamingDistribution20171030Request(); // CreateStreamingDistribution20171030Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The value of the <code>ETag</code> header that you received when retrieving the streaming distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.
    try {
      UpdateStreamingDistributionResult result = apiInstance.updateStreamingDistribution20171030(id, createStreamingDistribution20171030Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateStreamingDistribution20171030");
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
| **createStreamingDistribution20171030Request** | [**CreateStreamingDistribution20171030Request**](CreateStreamingDistribution20171030Request.md)|  | |
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
| **490** | TooManyTrustedSigners |  -  |
| **491** | TrustedSignerDoesNotExist |  -  |
| **492** | InconsistentQuantities |  -  |

