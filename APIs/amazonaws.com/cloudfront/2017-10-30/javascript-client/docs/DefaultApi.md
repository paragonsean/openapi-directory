# AmazonCloudFront.DefaultApi

All URIs are relative to *https://cloudfront.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCloudFrontOriginAccessIdentity20171030**](DefaultApi.md#createCloudFrontOriginAccessIdentity20171030) | **POST** /2017-10-30/origin-access-identity/cloudfront | 
[**createDistribution20171030**](DefaultApi.md#createDistribution20171030) | **POST** /2017-10-30/distribution | 
[**createDistributionWithTags20171030**](DefaultApi.md#createDistributionWithTags20171030) | **POST** /2017-10-30/distribution#WithTags | 
[**createFieldLevelEncryptionConfig20171030**](DefaultApi.md#createFieldLevelEncryptionConfig20171030) | **POST** /2017-10-30/field-level-encryption | 
[**createFieldLevelEncryptionProfile20171030**](DefaultApi.md#createFieldLevelEncryptionProfile20171030) | **POST** /2017-10-30/field-level-encryption-profile | 
[**createInvalidation20171030**](DefaultApi.md#createInvalidation20171030) | **POST** /2017-10-30/distribution/{DistributionId}/invalidation | 
[**createPublicKey20171030**](DefaultApi.md#createPublicKey20171030) | **POST** /2017-10-30/public-key | 
[**createStreamingDistribution20171030**](DefaultApi.md#createStreamingDistribution20171030) | **POST** /2017-10-30/streaming-distribution | 
[**createStreamingDistributionWithTags20171030**](DefaultApi.md#createStreamingDistributionWithTags20171030) | **POST** /2017-10-30/streaming-distribution#WithTags | 
[**deleteCloudFrontOriginAccessIdentity20171030**](DefaultApi.md#deleteCloudFrontOriginAccessIdentity20171030) | **DELETE** /2017-10-30/origin-access-identity/cloudfront/{Id} | 
[**deleteDistribution20171030**](DefaultApi.md#deleteDistribution20171030) | **DELETE** /2017-10-30/distribution/{Id} | 
[**deleteFieldLevelEncryptionConfig20171030**](DefaultApi.md#deleteFieldLevelEncryptionConfig20171030) | **DELETE** /2017-10-30/field-level-encryption/{Id} | 
[**deleteFieldLevelEncryptionProfile20171030**](DefaultApi.md#deleteFieldLevelEncryptionProfile20171030) | **DELETE** /2017-10-30/field-level-encryption-profile/{Id} | 
[**deletePublicKey20171030**](DefaultApi.md#deletePublicKey20171030) | **DELETE** /2017-10-30/public-key/{Id} | 
[**deleteStreamingDistribution20171030**](DefaultApi.md#deleteStreamingDistribution20171030) | **DELETE** /2017-10-30/streaming-distribution/{Id} | 
[**getCloudFrontOriginAccessIdentity20171030**](DefaultApi.md#getCloudFrontOriginAccessIdentity20171030) | **GET** /2017-10-30/origin-access-identity/cloudfront/{Id} | 
[**getCloudFrontOriginAccessIdentityConfig20171030**](DefaultApi.md#getCloudFrontOriginAccessIdentityConfig20171030) | **GET** /2017-10-30/origin-access-identity/cloudfront/{Id}/config | 
[**getDistribution20171030**](DefaultApi.md#getDistribution20171030) | **GET** /2017-10-30/distribution/{Id} | 
[**getDistributionConfig20171030**](DefaultApi.md#getDistributionConfig20171030) | **GET** /2017-10-30/distribution/{Id}/config | 
[**getFieldLevelEncryption20171030**](DefaultApi.md#getFieldLevelEncryption20171030) | **GET** /2017-10-30/field-level-encryption/{Id} | 
[**getFieldLevelEncryptionConfig20171030**](DefaultApi.md#getFieldLevelEncryptionConfig20171030) | **GET** /2017-10-30/field-level-encryption/{Id}/config | 
[**getFieldLevelEncryptionProfile20171030**](DefaultApi.md#getFieldLevelEncryptionProfile20171030) | **GET** /2017-10-30/field-level-encryption-profile/{Id} | 
[**getFieldLevelEncryptionProfileConfig20171030**](DefaultApi.md#getFieldLevelEncryptionProfileConfig20171030) | **GET** /2017-10-30/field-level-encryption-profile/{Id}/config | 
[**getInvalidation20171030**](DefaultApi.md#getInvalidation20171030) | **GET** /2017-10-30/distribution/{DistributionId}/invalidation/{Id} | 
[**getPublicKey20171030**](DefaultApi.md#getPublicKey20171030) | **GET** /2017-10-30/public-key/{Id} | 
[**getPublicKeyConfig20171030**](DefaultApi.md#getPublicKeyConfig20171030) | **GET** /2017-10-30/public-key/{Id}/config | 
[**getStreamingDistribution20171030**](DefaultApi.md#getStreamingDistribution20171030) | **GET** /2017-10-30/streaming-distribution/{Id} | 
[**getStreamingDistributionConfig20171030**](DefaultApi.md#getStreamingDistributionConfig20171030) | **GET** /2017-10-30/streaming-distribution/{Id}/config | 
[**listCloudFrontOriginAccessIdentities20171030**](DefaultApi.md#listCloudFrontOriginAccessIdentities20171030) | **GET** /2017-10-30/origin-access-identity/cloudfront | 
[**listDistributions20171030**](DefaultApi.md#listDistributions20171030) | **GET** /2017-10-30/distribution | 
[**listDistributionsByWebACLId20171030**](DefaultApi.md#listDistributionsByWebACLId20171030) | **GET** /2017-10-30/distributionsByWebACLId/{WebACLId} | 
[**listFieldLevelEncryptionConfigs20171030**](DefaultApi.md#listFieldLevelEncryptionConfigs20171030) | **GET** /2017-10-30/field-level-encryption | 
[**listFieldLevelEncryptionProfiles20171030**](DefaultApi.md#listFieldLevelEncryptionProfiles20171030) | **GET** /2017-10-30/field-level-encryption-profile | 
[**listInvalidations20171030**](DefaultApi.md#listInvalidations20171030) | **GET** /2017-10-30/distribution/{DistributionId}/invalidation | 
[**listPublicKeys20171030**](DefaultApi.md#listPublicKeys20171030) | **GET** /2017-10-30/public-key | 
[**listStreamingDistributions20171030**](DefaultApi.md#listStreamingDistributions20171030) | **GET** /2017-10-30/streaming-distribution | 
[**listTagsForResource20171030**](DefaultApi.md#listTagsForResource20171030) | **GET** /2017-10-30/tagging#Resource | 
[**tagResource20171030**](DefaultApi.md#tagResource20171030) | **POST** /2017-10-30/tagging#Operation&#x3D;Tag&amp;Resource | 
[**untagResource20171030**](DefaultApi.md#untagResource20171030) | **POST** /2017-10-30/tagging#Operation&#x3D;Untag&amp;Resource | 
[**updateCloudFrontOriginAccessIdentity20171030**](DefaultApi.md#updateCloudFrontOriginAccessIdentity20171030) | **PUT** /2017-10-30/origin-access-identity/cloudfront/{Id}/config | 
[**updateDistribution20171030**](DefaultApi.md#updateDistribution20171030) | **PUT** /2017-10-30/distribution/{Id}/config | 
[**updateFieldLevelEncryptionConfig20171030**](DefaultApi.md#updateFieldLevelEncryptionConfig20171030) | **PUT** /2017-10-30/field-level-encryption/{Id}/config | 
[**updateFieldLevelEncryptionProfile20171030**](DefaultApi.md#updateFieldLevelEncryptionProfile20171030) | **PUT** /2017-10-30/field-level-encryption-profile/{Id}/config | 
[**updatePublicKey20171030**](DefaultApi.md#updatePublicKey20171030) | **PUT** /2017-10-30/public-key/{Id}/config | 
[**updateStreamingDistribution20171030**](DefaultApi.md#updateStreamingDistribution20171030) | **PUT** /2017-10-30/streaming-distribution/{Id}/config | 



## createCloudFrontOriginAccessIdentity20171030

> CreateCloudFrontOriginAccessIdentityResult createCloudFrontOriginAccessIdentity20171030(createCloudFrontOriginAccessIdentity20171030Request, opts)



Creates a new origin access identity. If you&#39;re using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving Private Content through CloudFront&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.

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
let createCloudFrontOriginAccessIdentity20171030Request = new AmazonCloudFront.CreateCloudFrontOriginAccessIdentity20171030Request(); // CreateCloudFrontOriginAccessIdentity20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCloudFrontOriginAccessIdentity20171030(createCloudFrontOriginAccessIdentity20171030Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCloudFrontOriginAccessIdentity20171030Request** | [**CreateCloudFrontOriginAccessIdentity20171030Request**](CreateCloudFrontOriginAccessIdentity20171030Request.md)|  | 
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


## createDistribution20171030

> CreateDistributionResult createDistribution20171030(createDistribution20171030Request, opts)



Creates a new web distribution. Send a &lt;code&gt;POST&lt;/code&gt; request to the &lt;code&gt;/&lt;i&gt;CloudFront API version&lt;/i&gt;/distribution&lt;/code&gt;/&lt;code&gt;distribution ID&lt;/code&gt; resource.

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
let createDistribution20171030Request = new AmazonCloudFront.CreateDistribution20171030Request(); // CreateDistribution20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDistribution20171030(createDistribution20171030Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDistribution20171030Request** | [**CreateDistribution20171030Request**](CreateDistribution20171030Request.md)|  | 
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


## createDistributionWithTags20171030

> CreateDistributionWithTagsResult createDistributionWithTags20171030(withTags, createDistributionWithTags20171030Request, opts)



Create a new distribution with tags.

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
let createDistributionWithTags20171030Request = new AmazonCloudFront.CreateDistributionWithTags20171030Request(); // CreateDistributionWithTags20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDistributionWithTags20171030(withTags, createDistributionWithTags20171030Request, opts, (error, data, response) => {
  if (error) {
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
 **createDistributionWithTags20171030Request** | [**CreateDistributionWithTags20171030Request**](CreateDistributionWithTags20171030Request.md)|  | 
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


## createFieldLevelEncryptionConfig20171030

> CreateFieldLevelEncryptionConfigResult createFieldLevelEncryptionConfig20171030(createFieldLevelEncryptionConfig20171030Request, opts)



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
let createFieldLevelEncryptionConfig20171030Request = new AmazonCloudFront.CreateFieldLevelEncryptionConfig20171030Request(); // CreateFieldLevelEncryptionConfig20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFieldLevelEncryptionConfig20171030(createFieldLevelEncryptionConfig20171030Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createFieldLevelEncryptionConfig20171030Request** | [**CreateFieldLevelEncryptionConfig20171030Request**](CreateFieldLevelEncryptionConfig20171030Request.md)|  | 
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


## createFieldLevelEncryptionProfile20171030

> CreateFieldLevelEncryptionProfileResult createFieldLevelEncryptionProfile20171030(createFieldLevelEncryptionProfile20171030Request, opts)



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
let createFieldLevelEncryptionProfile20171030Request = new AmazonCloudFront.CreateFieldLevelEncryptionProfile20171030Request(); // CreateFieldLevelEncryptionProfile20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFieldLevelEncryptionProfile20171030(createFieldLevelEncryptionProfile20171030Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createFieldLevelEncryptionProfile20171030Request** | [**CreateFieldLevelEncryptionProfile20171030Request**](CreateFieldLevelEncryptionProfile20171030Request.md)|  | 
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


## createInvalidation20171030

> CreateInvalidationResult createInvalidation20171030(distributionId, createInvalidation20171030Request, opts)



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
let createInvalidation20171030Request = new AmazonCloudFront.CreateInvalidation20171030Request(); // CreateInvalidation20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createInvalidation20171030(distributionId, createInvalidation20171030Request, opts, (error, data, response) => {
  if (error) {
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
 **createInvalidation20171030Request** | [**CreateInvalidation20171030Request**](CreateInvalidation20171030Request.md)|  | 
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


## createPublicKey20171030

> CreatePublicKeyResult createPublicKey20171030(createPublicKey20171030Request, opts)



Add a new public key to CloudFront to use, for example, for field-level encryption. You can add a maximum of 10 public keys with one AWS account.

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
let createPublicKey20171030Request = new AmazonCloudFront.CreatePublicKey20171030Request(); // CreatePublicKey20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPublicKey20171030(createPublicKey20171030Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createPublicKey20171030Request** | [**CreatePublicKey20171030Request**](CreatePublicKey20171030Request.md)|  | 
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


## createStreamingDistribution20171030

> CreateStreamingDistributionResult createStreamingDistribution20171030(createStreamingDistribution20171030Request, opts)



&lt;p&gt;Creates a new RMTP distribution. An RTMP distribution is similar to a web distribution, but an RTMP distribution streams media files using the Adobe Real-Time Messaging Protocol (RTMP) instead of serving files using HTTP. &lt;/p&gt; &lt;p&gt;To create a new web distribution, submit a &lt;code&gt;POST&lt;/code&gt; request to the &lt;i&gt;CloudFront API version&lt;/i&gt;/distribution resource. The request body must include a document with a &lt;i&gt;StreamingDistributionConfig&lt;/i&gt; element. The response echoes the &lt;code&gt;StreamingDistributionConfig&lt;/code&gt; element and returns other information about the RTMP distribution.&lt;/p&gt; &lt;p&gt;To get the status of your request, use the &lt;i&gt;GET StreamingDistribution&lt;/i&gt; API action. When the value of &lt;code&gt;Enabled&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt; and the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;, your distribution is ready. A distribution usually deploys in less than 15 minutes.&lt;/p&gt; &lt;p&gt;For more information about web distributions, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-rtmp.html\&quot;&gt;Working with RTMP Distributions&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Beginning with the 2012-05-05 version of the CloudFront API, we made substantial changes to the format of the XML document that you include in the request body when you create or update a web distribution or an RTMP distribution, and when you invalidate objects. With previous versions of the API, we discovered that it was too easy to accidentally delete one or more values for an element that accepts multiple values, for example, CNAMEs and trusted signers. Our changes for the 2012-05-05 release are intended to prevent these accidental deletions and to notify you when there&#39;s a mismatch between the number of values you say you&#39;re specifying in the &lt;code&gt;Quantity&lt;/code&gt; element and the number of values specified.&lt;/p&gt; &lt;/important&gt;

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
let createStreamingDistribution20171030Request = new AmazonCloudFront.CreateStreamingDistribution20171030Request(); // CreateStreamingDistribution20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStreamingDistribution20171030(createStreamingDistribution20171030Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createStreamingDistribution20171030Request** | [**CreateStreamingDistribution20171030Request**](CreateStreamingDistribution20171030Request.md)|  | 
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


## createStreamingDistributionWithTags20171030

> CreateStreamingDistributionWithTagsResult createStreamingDistributionWithTags20171030(withTags, createStreamingDistributionWithTags20171030Request, opts)



Create a new streaming distribution with tags.

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
let createStreamingDistributionWithTags20171030Request = new AmazonCloudFront.CreateStreamingDistributionWithTags20171030Request(); // CreateStreamingDistributionWithTags20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStreamingDistributionWithTags20171030(withTags, createStreamingDistributionWithTags20171030Request, opts, (error, data, response) => {
  if (error) {
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
 **createStreamingDistributionWithTags20171030Request** | [**CreateStreamingDistributionWithTags20171030Request**](CreateStreamingDistributionWithTags20171030Request.md)|  | 
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


## deleteCloudFrontOriginAccessIdentity20171030

> deleteCloudFrontOriginAccessIdentity20171030(id, opts)



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
apiInstance.deleteCloudFrontOriginAccessIdentity20171030(id, opts, (error, data, response) => {
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


## deleteDistribution20171030

> deleteDistribution20171030(id, opts)



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
apiInstance.deleteDistribution20171030(id, opts, (error, data, response) => {
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
 **id** | **String**| The distribution ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **ifMatch** | **String**| The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when you disabled the distribution. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## deleteFieldLevelEncryptionConfig20171030

> deleteFieldLevelEncryptionConfig20171030(id, opts)



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
apiInstance.deleteFieldLevelEncryptionConfig20171030(id, opts, (error, data, response) => {
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


## deleteFieldLevelEncryptionProfile20171030

> deleteFieldLevelEncryptionProfile20171030(id, opts)



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
apiInstance.deleteFieldLevelEncryptionProfile20171030(id, opts, (error, data, response) => {
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


## deletePublicKey20171030

> deletePublicKey20171030(id, opts)



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
apiInstance.deletePublicKey20171030(id, opts, (error, data, response) => {
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


## deleteStreamingDistribution20171030

> deleteStreamingDistribution20171030(id, opts)



&lt;p&gt;Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To delete an RTMP distribution using the CloudFront API&lt;/b&gt;:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Disable the RTMP distribution.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to get the current configuration and the &lt;code&gt;Etag&lt;/code&gt; header for the distribution. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to change the value of &lt;code&gt;Enabled&lt;/code&gt; to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to confirm that the distribution was successfully disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request. Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to your &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request to confirm that the distribution was successfully deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For information about deleting a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html\&quot;&gt;Deleting a Distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
apiInstance.deleteStreamingDistribution20171030(id, opts, (error, data, response) => {
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
 **id** | **String**| The distribution ID.  | 
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


## getCloudFrontOriginAccessIdentity20171030

> GetCloudFrontOriginAccessIdentityResult getCloudFrontOriginAccessIdentity20171030(id, opts)



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
apiInstance.getCloudFrontOriginAccessIdentity20171030(id, opts, (error, data, response) => {
  if (error) {
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


## getCloudFrontOriginAccessIdentityConfig20171030

> GetCloudFrontOriginAccessIdentityConfigResult getCloudFrontOriginAccessIdentityConfig20171030(id, opts)



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
apiInstance.getCloudFrontOriginAccessIdentityConfig20171030(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The identity&#39;s ID.  | 
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


## getDistribution20171030

> GetDistributionResult getDistribution20171030(id, opts)



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
let id = "id_example"; // String | The distribution's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDistribution20171030(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The distribution&#39;s ID. | 
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


## getDistributionConfig20171030

> GetDistributionConfigResult getDistributionConfig20171030(id, opts)



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
let id = "id_example"; // String | The distribution's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDistributionConfig20171030(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The distribution&#39;s ID. | 
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


## getFieldLevelEncryption20171030

> GetFieldLevelEncryptionResult getFieldLevelEncryption20171030(id, opts)



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
apiInstance.getFieldLevelEncryption20171030(id, opts, (error, data, response) => {
  if (error) {
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


## getFieldLevelEncryptionConfig20171030

> GetFieldLevelEncryptionConfigResult getFieldLevelEncryptionConfig20171030(id, opts)



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
apiInstance.getFieldLevelEncryptionConfig20171030(id, opts, (error, data, response) => {
  if (error) {
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


## getFieldLevelEncryptionProfile20171030

> GetFieldLevelEncryptionProfileResult getFieldLevelEncryptionProfile20171030(id, opts)



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
apiInstance.getFieldLevelEncryptionProfile20171030(id, opts, (error, data, response) => {
  if (error) {
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


## getFieldLevelEncryptionProfileConfig20171030

> GetFieldLevelEncryptionProfileConfigResult getFieldLevelEncryptionProfileConfig20171030(id, opts)



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
apiInstance.getFieldLevelEncryptionProfileConfig20171030(id, opts, (error, data, response) => {
  if (error) {
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


## getInvalidation20171030

> GetInvalidationResult getInvalidation20171030(distributionId, id, opts)



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
apiInstance.getInvalidation20171030(distributionId, id, opts, (error, data, response) => {
  if (error) {
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


## getPublicKey20171030

> GetPublicKeyResult getPublicKey20171030(id, opts)



Get the public key information.

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
let id = "id_example"; // String | Request the ID for the public key.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPublicKey20171030(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Request the ID for the public key. | 
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


## getPublicKeyConfig20171030

> GetPublicKeyConfigResult getPublicKeyConfig20171030(id, opts)



Return public key configuration informaation

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
let id = "id_example"; // String | Request the ID for the public key configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPublicKeyConfig20171030(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Request the ID for the public key configuration. | 
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


## getStreamingDistribution20171030

> GetStreamingDistributionResult getStreamingDistribution20171030(id, opts)



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
apiInstance.getStreamingDistribution20171030(id, opts, (error, data, response) => {
  if (error) {
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


## getStreamingDistributionConfig20171030

> GetStreamingDistributionConfigResult getStreamingDistributionConfig20171030(id, opts)



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
apiInstance.getStreamingDistributionConfig20171030(id, opts, (error, data, response) => {
  if (error) {
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


## listCloudFrontOriginAccessIdentities20171030

> ListCloudFrontOriginAccessIdentitiesResult listCloudFrontOriginAccessIdentities20171030(opts)



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
apiInstance.listCloudFrontOriginAccessIdentities20171030(opts, (error, data, response) => {
  if (error) {
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
 **maxItems** | **String**| The maximum number of origin access identities you want in the response body.  | [optional] 

### Return type

[**ListCloudFrontOriginAccessIdentitiesResult**](ListCloudFrontOriginAccessIdentitiesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listDistributions20171030

> ListDistributionsResult listDistributions20171030(opts)



List distributions. 

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
apiInstance.listDistributions20171030(opts, (error, data, response) => {
  if (error) {
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


## listDistributionsByWebACLId20171030

> ListDistributionsByWebACLIdResult listDistributionsByWebACLId20171030(webACLId, opts)



List the distributions that are associated with a specified AWS WAF web ACL. 

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
let webACLId = "webACLId_example"; // String | The ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify \"null\" for the ID, the request returns a list of the distributions that aren't associated with a web ACL. 
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
apiInstance.listDistributionsByWebACLId20171030(webACLId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webACLId** | **String**| The ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify \&quot;null\&quot; for the ID, the request returns a list of the distributions that aren&#39;t associated with a web ACL.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **marker** | **String**| Use &lt;code&gt;Marker&lt;/code&gt; and &lt;code&gt;MaxItems&lt;/code&gt; to control pagination of results. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; distributions that satisfy the request, the response includes a &lt;code&gt;NextMarker&lt;/code&gt; element. To get the next page of results, submit another request. For the value of &lt;code&gt;Marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the last response. (For the first request, omit &lt;code&gt;Marker&lt;/code&gt;.)  | [optional] 
 **maxItems** | **String**| The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100. | [optional] 

### Return type

[**ListDistributionsByWebACLIdResult**](ListDistributionsByWebACLIdResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listFieldLevelEncryptionConfigs20171030

> ListFieldLevelEncryptionConfigsResult listFieldLevelEncryptionConfigs20171030(opts)



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
apiInstance.listFieldLevelEncryptionConfigs20171030(opts, (error, data, response) => {
  if (error) {
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
 **marker** | **String**| Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last configuration on that page).  | [optional] 
 **maxItems** | **String**| The maximum number of field-level encryption configurations you want in the response body.  | [optional] 

### Return type

[**ListFieldLevelEncryptionConfigsResult**](ListFieldLevelEncryptionConfigsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listFieldLevelEncryptionProfiles20171030

> ListFieldLevelEncryptionProfilesResult listFieldLevelEncryptionProfiles20171030(opts)



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
apiInstance.listFieldLevelEncryptionProfiles20171030(opts, (error, data, response) => {
  if (error) {
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
 **marker** | **String**| Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last profile on that page).  | [optional] 
 **maxItems** | **String**| The maximum number of field-level encryption profiles you want in the response body.  | [optional] 

### Return type

[**ListFieldLevelEncryptionProfilesResult**](ListFieldLevelEncryptionProfilesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listInvalidations20171030

> ListInvalidationsResult listInvalidations20171030(distributionId, opts)



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
apiInstance.listInvalidations20171030(distributionId, opts, (error, data, response) => {
  if (error) {
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
 **marker** | **String**| Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. This value is the same as the ID of the last invalidation batch on that page.  | [optional] 
 **maxItems** | **String**| The maximum number of invalidation batches that you want in the response body. | [optional] 

### Return type

[**ListInvalidationsResult**](ListInvalidationsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listPublicKeys20171030

> ListPublicKeysResult listPublicKeys20171030(opts)



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
apiInstance.listPublicKeys20171030(opts, (error, data, response) => {
  if (error) {
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
 **marker** | **String**| Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last public key on that page).  | [optional] 
 **maxItems** | **String**| The maximum number of public keys you want in the response body.  | [optional] 

### Return type

[**ListPublicKeysResult**](ListPublicKeysResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## listStreamingDistributions20171030

> ListStreamingDistributionsResult listStreamingDistributions20171030(opts)



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
apiInstance.listStreamingDistributions20171030(opts, (error, data, response) => {
  if (error) {
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


## listTagsForResource20171030

> ListTagsForResourceResult listTagsForResource20171030(resource, opts)



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
let resource = "resource_example"; // String |  An ARN of a CloudFront resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource20171030(resource, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **String**|  An ARN of a CloudFront resource. | 
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


## tagResource20171030

> tagResource20171030(resource, operation, tagResource20171030Request, opts)



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
let resource = "resource_example"; // String |  An ARN of a CloudFront resource.
let operation = "operation_example"; // String | 
let tagResource20171030Request = new AmazonCloudFront.TagResource20171030Request(); // TagResource20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource20171030(resource, operation, tagResource20171030Request, opts, (error, data, response) => {
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
 **resource** | **String**|  An ARN of a CloudFront resource. | 
 **operation** | **String**|  | 
 **tagResource20171030Request** | [**TagResource20171030Request**](TagResource20171030Request.md)|  | 
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


## untagResource20171030

> untagResource20171030(resource, operation, untagResource20171030Request, opts)



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
let resource = "resource_example"; // String |  An ARN of a CloudFront resource.
let operation = "operation_example"; // String | 
let untagResource20171030Request = new AmazonCloudFront.UntagResource20171030Request(); // UntagResource20171030Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource20171030(resource, operation, untagResource20171030Request, opts, (error, data, response) => {
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
 **resource** | **String**|  An ARN of a CloudFront resource. | 
 **operation** | **String**|  | 
 **untagResource20171030Request** | [**UntagResource20171030Request**](UntagResource20171030Request.md)|  | 
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


## updateCloudFrontOriginAccessIdentity20171030

> UpdateCloudFrontOriginAccessIdentityResult updateCloudFrontOriginAccessIdentity20171030(id, createCloudFrontOriginAccessIdentity20171030Request, opts)



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
let createCloudFrontOriginAccessIdentity20171030Request = new AmazonCloudFront.CreateCloudFrontOriginAccessIdentity20171030Request(); // CreateCloudFrontOriginAccessIdentity20171030Request | 
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
apiInstance.updateCloudFrontOriginAccessIdentity20171030(id, createCloudFrontOriginAccessIdentity20171030Request, opts, (error, data, response) => {
  if (error) {
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
 **createCloudFrontOriginAccessIdentity20171030Request** | [**CreateCloudFrontOriginAccessIdentity20171030Request**](CreateCloudFrontOriginAccessIdentity20171030Request.md)|  | 
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


## updateDistribution20171030

> UpdateDistributionResult updateDistribution20171030(id, createDistribution20171030Request, opts)



&lt;p&gt;Updates the configuration for a web distribution. Perform the following steps.&lt;/p&gt; &lt;p&gt;For information about updating a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.html\&quot;&gt;Creating or Updating a Web Distribution Using the CloudFront Console &lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To update a web distribution using the CloudFront API&lt;/b&gt; &lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;a&gt;GetDistributionConfig&lt;/a&gt; request to get the current configuration and an &lt;code&gt;Etag&lt;/code&gt; header for the distribution.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you update the distribution again, you need to get a new &lt;code&gt;Etag&lt;/code&gt; header.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GetDistributionConfig&lt;/code&gt; request to include the desired changes. You can&#39;t change the value of &lt;code&gt;CallerReference&lt;/code&gt;. If you try to change this value, CloudFront returns an &lt;code&gt;IllegalUpdate&lt;/code&gt; error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The new configuration replaces the existing configuration; the values that you specify in an &lt;code&gt;UpdateDistribution&lt;/code&gt; request are not merged into the existing configuration. When you add, delete, or replace values in an element that allows multiple values (for example, &lt;code&gt;CNAME&lt;/code&gt;), you must specify all of the values that you want to appear in the updated distribution. In addition, you must update the corresponding &lt;code&gt;Quantity&lt;/code&gt; element.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateDistribution&lt;/code&gt; request to update the configuration for your distribution:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;In the request body, include the XML document that you updated in Step 2. The request body must include an XML document with a &lt;code&gt;DistributionConfig&lt;/code&gt; element.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GetDistributionConfig&lt;/code&gt; request in Step 1.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;UpdateDistribution&lt;/code&gt; request to confirm that the configuration was successfully updated.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Optional: Submit a &lt;a&gt;GetDistribution&lt;/a&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Beginning with the 2012-05-05 version of the CloudFront API, we made substantial changes to the format of the XML document that you include in the request body when you create or update a distribution. With previous versions of the API, we discovered that it was too easy to accidentally delete one or more values for an element that accepts multiple values, for example, CNAMEs and trusted signers. Our changes for the 2012-05-05 release are intended to prevent these accidental deletions and to notify you when there&#39;s a mismatch between the number of values you say you&#39;re specifying in the &lt;code&gt;Quantity&lt;/code&gt; element and the number of values you&#39;re actually specifying.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ol&gt;

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
let createDistribution20171030Request = new AmazonCloudFront.CreateDistribution20171030Request(); // CreateDistribution20171030Request | 
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
apiInstance.updateDistribution20171030(id, createDistribution20171030Request, opts, (error, data, response) => {
  if (error) {
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
 **createDistribution20171030Request** | [**CreateDistribution20171030Request**](CreateDistribution20171030Request.md)|  | 
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


## updateFieldLevelEncryptionConfig20171030

> UpdateFieldLevelEncryptionConfigResult updateFieldLevelEncryptionConfig20171030(id, createFieldLevelEncryptionConfig20171030Request, opts)



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
let createFieldLevelEncryptionConfig20171030Request = new AmazonCloudFront.CreateFieldLevelEncryptionConfig20171030Request(); // CreateFieldLevelEncryptionConfig20171030Request | 
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
apiInstance.updateFieldLevelEncryptionConfig20171030(id, createFieldLevelEncryptionConfig20171030Request, opts, (error, data, response) => {
  if (error) {
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
 **createFieldLevelEncryptionConfig20171030Request** | [**CreateFieldLevelEncryptionConfig20171030Request**](CreateFieldLevelEncryptionConfig20171030Request.md)|  | 
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


## updateFieldLevelEncryptionProfile20171030

> UpdateFieldLevelEncryptionProfileResult updateFieldLevelEncryptionProfile20171030(id, createFieldLevelEncryptionProfile20171030Request, opts)



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
let createFieldLevelEncryptionProfile20171030Request = new AmazonCloudFront.CreateFieldLevelEncryptionProfile20171030Request(); // CreateFieldLevelEncryptionProfile20171030Request | 
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
apiInstance.updateFieldLevelEncryptionProfile20171030(id, createFieldLevelEncryptionProfile20171030Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the field-level encryption profile request.  | 
 **createFieldLevelEncryptionProfile20171030Request** | [**CreateFieldLevelEncryptionProfile20171030Request**](CreateFieldLevelEncryptionProfile20171030Request.md)|  | 
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


## updatePublicKey20171030

> UpdatePublicKeyResult updatePublicKey20171030(id, createPublicKey20171030Request, opts)



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
let id = "id_example"; // String | ID of the public key to be updated.
let createPublicKey20171030Request = new AmazonCloudFront.CreatePublicKey20171030Request(); // CreatePublicKey20171030Request | 
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
apiInstance.updatePublicKey20171030(id, createPublicKey20171030Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the public key to be updated. | 
 **createPublicKey20171030Request** | [**CreatePublicKey20171030Request**](CreatePublicKey20171030Request.md)|  | 
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


## updateStreamingDistribution20171030

> UpdateStreamingDistributionResult updateStreamingDistribution20171030(id, createStreamingDistribution20171030Request, opts)



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
let createStreamingDistribution20171030Request = new AmazonCloudFront.CreateStreamingDistribution20171030Request(); // CreateStreamingDistribution20171030Request | 
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
apiInstance.updateStreamingDistribution20171030(id, createStreamingDistribution20171030Request, opts, (error, data, response) => {
  if (error) {
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
 **createStreamingDistribution20171030Request** | [**CreateStreamingDistribution20171030Request**](CreateStreamingDistribution20171030Request.md)|  | 
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

