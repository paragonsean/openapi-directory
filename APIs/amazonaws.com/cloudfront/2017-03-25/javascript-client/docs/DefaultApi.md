# AmazonCloudFront.DefaultApi

All URIs are relative to *https://cloudfront.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCloudFrontOriginAccessIdentity20170325**](DefaultApi.md#createCloudFrontOriginAccessIdentity20170325) | **POST** /2017-03-25/origin-access-identity/cloudfront | 
[**createDistribution20170325**](DefaultApi.md#createDistribution20170325) | **POST** /2017-03-25/distribution | 
[**createDistributionWithTags20170325**](DefaultApi.md#createDistributionWithTags20170325) | **POST** /2017-03-25/distribution#WithTags | 
[**createInvalidation20170325**](DefaultApi.md#createInvalidation20170325) | **POST** /2017-03-25/distribution/{DistributionId}/invalidation | 
[**createStreamingDistribution20170325**](DefaultApi.md#createStreamingDistribution20170325) | **POST** /2017-03-25/streaming-distribution | 
[**createStreamingDistributionWithTags20170325**](DefaultApi.md#createStreamingDistributionWithTags20170325) | **POST** /2017-03-25/streaming-distribution#WithTags | 
[**deleteCloudFrontOriginAccessIdentity20170325**](DefaultApi.md#deleteCloudFrontOriginAccessIdentity20170325) | **DELETE** /2017-03-25/origin-access-identity/cloudfront/{Id} | 
[**deleteDistribution20170325**](DefaultApi.md#deleteDistribution20170325) | **DELETE** /2017-03-25/distribution/{Id} | 
[**deleteServiceLinkedRole20170325**](DefaultApi.md#deleteServiceLinkedRole20170325) | **DELETE** /2017-03-25/service-linked-role/{RoleName} | 
[**deleteStreamingDistribution20170325**](DefaultApi.md#deleteStreamingDistribution20170325) | **DELETE** /2017-03-25/streaming-distribution/{Id} | 
[**getCloudFrontOriginAccessIdentity20170325**](DefaultApi.md#getCloudFrontOriginAccessIdentity20170325) | **GET** /2017-03-25/origin-access-identity/cloudfront/{Id} | 
[**getCloudFrontOriginAccessIdentityConfig20170325**](DefaultApi.md#getCloudFrontOriginAccessIdentityConfig20170325) | **GET** /2017-03-25/origin-access-identity/cloudfront/{Id}/config | 
[**getDistribution20170325**](DefaultApi.md#getDistribution20170325) | **GET** /2017-03-25/distribution/{Id} | 
[**getDistributionConfig20170325**](DefaultApi.md#getDistributionConfig20170325) | **GET** /2017-03-25/distribution/{Id}/config | 
[**getInvalidation20170325**](DefaultApi.md#getInvalidation20170325) | **GET** /2017-03-25/distribution/{DistributionId}/invalidation/{Id} | 
[**getStreamingDistribution20170325**](DefaultApi.md#getStreamingDistribution20170325) | **GET** /2017-03-25/streaming-distribution/{Id} | 
[**getStreamingDistributionConfig20170325**](DefaultApi.md#getStreamingDistributionConfig20170325) | **GET** /2017-03-25/streaming-distribution/{Id}/config | 
[**listCloudFrontOriginAccessIdentities20170325**](DefaultApi.md#listCloudFrontOriginAccessIdentities20170325) | **GET** /2017-03-25/origin-access-identity/cloudfront | 
[**listDistributions20170325**](DefaultApi.md#listDistributions20170325) | **GET** /2017-03-25/distribution | 
[**listDistributionsByWebACLId20170325**](DefaultApi.md#listDistributionsByWebACLId20170325) | **GET** /2017-03-25/distributionsByWebACLId/{WebACLId} | 
[**listInvalidations20170325**](DefaultApi.md#listInvalidations20170325) | **GET** /2017-03-25/distribution/{DistributionId}/invalidation | 
[**listStreamingDistributions20170325**](DefaultApi.md#listStreamingDistributions20170325) | **GET** /2017-03-25/streaming-distribution | 
[**listTagsForResource20170325**](DefaultApi.md#listTagsForResource20170325) | **GET** /2017-03-25/tagging#Resource | 
[**tagResource20170325**](DefaultApi.md#tagResource20170325) | **POST** /2017-03-25/tagging#Operation&#x3D;Tag&amp;Resource | 
[**untagResource20170325**](DefaultApi.md#untagResource20170325) | **POST** /2017-03-25/tagging#Operation&#x3D;Untag&amp;Resource | 
[**updateCloudFrontOriginAccessIdentity20170325**](DefaultApi.md#updateCloudFrontOriginAccessIdentity20170325) | **PUT** /2017-03-25/origin-access-identity/cloudfront/{Id}/config | 
[**updateDistribution20170325**](DefaultApi.md#updateDistribution20170325) | **PUT** /2017-03-25/distribution/{Id}/config | 
[**updateStreamingDistribution20170325**](DefaultApi.md#updateStreamingDistribution20170325) | **PUT** /2017-03-25/streaming-distribution/{Id}/config | 



## createCloudFrontOriginAccessIdentity20170325

> CreateCloudFrontOriginAccessIdentityResult createCloudFrontOriginAccessIdentity20170325(createCloudFrontOriginAccessIdentity20170325Request, opts)



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
let createCloudFrontOriginAccessIdentity20170325Request = new AmazonCloudFront.CreateCloudFrontOriginAccessIdentity20170325Request(); // CreateCloudFrontOriginAccessIdentity20170325Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCloudFrontOriginAccessIdentity20170325(createCloudFrontOriginAccessIdentity20170325Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCloudFrontOriginAccessIdentity20170325Request** | [**CreateCloudFrontOriginAccessIdentity20170325Request**](CreateCloudFrontOriginAccessIdentity20170325Request.md)|  | 
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


## createDistribution20170325

> CreateDistributionResult createDistribution20170325(createDistribution20170325Request, opts)



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
let createDistribution20170325Request = new AmazonCloudFront.CreateDistribution20170325Request(); // CreateDistribution20170325Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDistribution20170325(createDistribution20170325Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDistribution20170325Request** | [**CreateDistribution20170325Request**](CreateDistribution20170325Request.md)|  | 
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


## createDistributionWithTags20170325

> CreateDistributionWithTagsResult createDistributionWithTags20170325(withTags, createDistributionWithTags20170325Request, opts)



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
let createDistributionWithTags20170325Request = new AmazonCloudFront.CreateDistributionWithTags20170325Request(); // CreateDistributionWithTags20170325Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDistributionWithTags20170325(withTags, createDistributionWithTags20170325Request, opts, (error, data, response) => {
  if (error) {
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
 **createDistributionWithTags20170325Request** | [**CreateDistributionWithTags20170325Request**](CreateDistributionWithTags20170325Request.md)|  | 
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


## createInvalidation20170325

> CreateInvalidationResult createInvalidation20170325(distributionId, createInvalidation20170325Request, opts)



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
let createInvalidation20170325Request = new AmazonCloudFront.CreateInvalidation20170325Request(); // CreateInvalidation20170325Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createInvalidation20170325(distributionId, createInvalidation20170325Request, opts, (error, data, response) => {
  if (error) {
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
 **createInvalidation20170325Request** | [**CreateInvalidation20170325Request**](CreateInvalidation20170325Request.md)|  | 
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


## createStreamingDistribution20170325

> CreateStreamingDistributionResult createStreamingDistribution20170325(createStreamingDistribution20170325Request, opts)



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
let createStreamingDistribution20170325Request = new AmazonCloudFront.CreateStreamingDistribution20170325Request(); // CreateStreamingDistribution20170325Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStreamingDistribution20170325(createStreamingDistribution20170325Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createStreamingDistribution20170325Request** | [**CreateStreamingDistribution20170325Request**](CreateStreamingDistribution20170325Request.md)|  | 
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


## createStreamingDistributionWithTags20170325

> CreateStreamingDistributionWithTagsResult createStreamingDistributionWithTags20170325(withTags, createStreamingDistributionWithTags20170325Request, opts)



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
let createStreamingDistributionWithTags20170325Request = new AmazonCloudFront.CreateStreamingDistributionWithTags20170325Request(); // CreateStreamingDistributionWithTags20170325Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStreamingDistributionWithTags20170325(withTags, createStreamingDistributionWithTags20170325Request, opts, (error, data, response) => {
  if (error) {
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
 **createStreamingDistributionWithTags20170325Request** | [**CreateStreamingDistributionWithTags20170325Request**](CreateStreamingDistributionWithTags20170325Request.md)|  | 
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


## deleteCloudFrontOriginAccessIdentity20170325

> deleteCloudFrontOriginAccessIdentity20170325(id, opts)



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
apiInstance.deleteCloudFrontOriginAccessIdentity20170325(id, opts, (error, data, response) => {
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


## deleteDistribution20170325

> deleteDistribution20170325(id, opts)



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
apiInstance.deleteDistribution20170325(id, opts, (error, data, response) => {
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


## deleteServiceLinkedRole20170325

> deleteServiceLinkedRole20170325(roleName, opts)





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
let roleName = "roleName_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteServiceLinkedRole20170325(roleName, opts, (error, data, response) => {
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
 **roleName** | **String**|  | 
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


## deleteStreamingDistribution20170325

> deleteStreamingDistribution20170325(id, opts)



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
apiInstance.deleteStreamingDistribution20170325(id, opts, (error, data, response) => {
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


## getCloudFrontOriginAccessIdentity20170325

> GetCloudFrontOriginAccessIdentityResult getCloudFrontOriginAccessIdentity20170325(id, opts)



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
apiInstance.getCloudFrontOriginAccessIdentity20170325(id, opts, (error, data, response) => {
  if (error) {
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


## getCloudFrontOriginAccessIdentityConfig20170325

> GetCloudFrontOriginAccessIdentityConfigResult getCloudFrontOriginAccessIdentityConfig20170325(id, opts)



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
apiInstance.getCloudFrontOriginAccessIdentityConfig20170325(id, opts, (error, data, response) => {
  if (error) {
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


## getDistribution20170325

> GetDistributionResult getDistribution20170325(id, opts)



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
apiInstance.getDistribution20170325(id, opts, (error, data, response) => {
  if (error) {
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


## getDistributionConfig20170325

> GetDistributionConfigResult getDistributionConfig20170325(id, opts)



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
apiInstance.getDistributionConfig20170325(id, opts, (error, data, response) => {
  if (error) {
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


## getInvalidation20170325

> GetInvalidationResult getInvalidation20170325(distributionId, id, opts)



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
apiInstance.getInvalidation20170325(distributionId, id, opts, (error, data, response) => {
  if (error) {
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


## getStreamingDistribution20170325

> GetStreamingDistributionResult getStreamingDistribution20170325(id, opts)



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
apiInstance.getStreamingDistribution20170325(id, opts, (error, data, response) => {
  if (error) {
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


## getStreamingDistributionConfig20170325

> GetStreamingDistributionConfigResult getStreamingDistributionConfig20170325(id, opts)



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
apiInstance.getStreamingDistributionConfig20170325(id, opts, (error, data, response) => {
  if (error) {
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


## listCloudFrontOriginAccessIdentities20170325

> ListCloudFrontOriginAccessIdentitiesResult listCloudFrontOriginAccessIdentities20170325(opts)



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
apiInstance.listCloudFrontOriginAccessIdentities20170325(opts, (error, data, response) => {
  if (error) {
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


## listDistributions20170325

> ListDistributionsResult listDistributions20170325(opts)



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
apiInstance.listDistributions20170325(opts, (error, data, response) => {
  if (error) {
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


## listDistributionsByWebACLId20170325

> ListDistributionsByWebACLIdResult listDistributionsByWebACLId20170325(webACLId, opts)



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
apiInstance.listDistributionsByWebACLId20170325(webACLId, opts, (error, data, response) => {
  if (error) {
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


## listInvalidations20170325

> ListInvalidationsResult listInvalidations20170325(distributionId, opts)



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
apiInstance.listInvalidations20170325(distributionId, opts, (error, data, response) => {
  if (error) {
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


## listStreamingDistributions20170325

> ListStreamingDistributionsResult listStreamingDistributions20170325(opts)



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
apiInstance.listStreamingDistributions20170325(opts, (error, data, response) => {
  if (error) {
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


## listTagsForResource20170325

> ListTagsForResourceResult listTagsForResource20170325(resource, opts)



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
apiInstance.listTagsForResource20170325(resource, opts, (error, data, response) => {
  if (error) {
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


## tagResource20170325

> tagResource20170325(resource, operation, tagResource20170325Request, opts)



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
let tagResource20170325Request = new AmazonCloudFront.TagResource20170325Request(); // TagResource20170325Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource20170325(resource, operation, tagResource20170325Request, opts, (error, data, response) => {
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
 **tagResource20170325Request** | [**TagResource20170325Request**](TagResource20170325Request.md)|  | 
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


## untagResource20170325

> untagResource20170325(resource, operation, untagResource20170325Request, opts)



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
let untagResource20170325Request = new AmazonCloudFront.UntagResource20170325Request(); // UntagResource20170325Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource20170325(resource, operation, untagResource20170325Request, opts, (error, data, response) => {
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
 **untagResource20170325Request** | [**UntagResource20170325Request**](UntagResource20170325Request.md)|  | 
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


## updateCloudFrontOriginAccessIdentity20170325

> UpdateCloudFrontOriginAccessIdentityResult updateCloudFrontOriginAccessIdentity20170325(id, createCloudFrontOriginAccessIdentity20170325Request, opts)



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
let createCloudFrontOriginAccessIdentity20170325Request = new AmazonCloudFront.CreateCloudFrontOriginAccessIdentity20170325Request(); // CreateCloudFrontOriginAccessIdentity20170325Request | 
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
apiInstance.updateCloudFrontOriginAccessIdentity20170325(id, createCloudFrontOriginAccessIdentity20170325Request, opts, (error, data, response) => {
  if (error) {
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
 **createCloudFrontOriginAccessIdentity20170325Request** | [**CreateCloudFrontOriginAccessIdentity20170325Request**](CreateCloudFrontOriginAccessIdentity20170325Request.md)|  | 
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


## updateDistribution20170325

> UpdateDistributionResult updateDistribution20170325(id, createDistribution20170325Request, opts)



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
let createDistribution20170325Request = new AmazonCloudFront.CreateDistribution20170325Request(); // CreateDistribution20170325Request | 
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
apiInstance.updateDistribution20170325(id, createDistribution20170325Request, opts, (error, data, response) => {
  if (error) {
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
 **createDistribution20170325Request** | [**CreateDistribution20170325Request**](CreateDistribution20170325Request.md)|  | 
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


## updateStreamingDistribution20170325

> UpdateStreamingDistributionResult updateStreamingDistribution20170325(id, createStreamingDistribution20170325Request, opts)



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
let createStreamingDistribution20170325Request = new AmazonCloudFront.CreateStreamingDistribution20170325Request(); // CreateStreamingDistribution20170325Request | 
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
apiInstance.updateStreamingDistribution20170325(id, createStreamingDistribution20170325Request, opts, (error, data, response) => {
  if (error) {
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
 **createStreamingDistribution20170325Request** | [**CreateStreamingDistribution20170325Request**](CreateStreamingDistribution20170325Request.md)|  | 
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

