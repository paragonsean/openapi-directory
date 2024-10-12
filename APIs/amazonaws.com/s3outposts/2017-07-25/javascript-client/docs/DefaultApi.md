# AmazonS3OnOutposts.DefaultApi

All URIs are relative to *http://s3-outposts.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEndpoint**](DefaultApi.md#createEndpoint) | **POST** /S3Outposts/CreateEndpoint | 
[**deleteEndpoint**](DefaultApi.md#deleteEndpoint) | **DELETE** /S3Outposts/DeleteEndpoint#endpointId&amp;outpostId | 
[**listEndpoints**](DefaultApi.md#listEndpoints) | **GET** /S3Outposts/ListEndpoints | 
[**listOutpostsWithS3**](DefaultApi.md#listOutpostsWithS3) | **GET** /S3Outposts/ListOutpostsWithS3 | 
[**listSharedEndpoints**](DefaultApi.md#listSharedEndpoints) | **GET** /S3Outposts/ListSharedEndpoints#outpostId | 



## createEndpoint

> CreateEndpointResult createEndpoint(createEndpointRequest, opts)



&lt;p&gt;Creates an endpoint and associates it with the specified Outpost.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It can take up to 5 minutes for this action to finish.&lt;/p&gt; &lt;/note&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html\&quot;&gt;DeleteEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html\&quot;&gt;ListEndpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonS3OnOutposts from 'amazon_s3_on_outposts';
let defaultClient = AmazonS3OnOutposts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonS3OnOutposts.DefaultApi();
let createEndpointRequest = new AmazonS3OnOutposts.CreateEndpointRequest(); // CreateEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEndpoint(createEndpointRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createEndpointRequest** | [**CreateEndpointRequest**](CreateEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateEndpointResult**](CreateEndpointResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEndpoint

> deleteEndpoint(endpointId, outpostId, opts)



&lt;p&gt;Deletes an endpoint.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It can take up to 5 minutes for this action to finish.&lt;/p&gt; &lt;/note&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html\&quot;&gt;CreateEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html\&quot;&gt;ListEndpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonS3OnOutposts from 'amazon_s3_on_outposts';
let defaultClient = AmazonS3OnOutposts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonS3OnOutposts.DefaultApi();
let endpointId = "endpointId_example"; // String | The ID of the endpoint.
let outpostId = "outpostId_example"; // String | The ID of the Outposts. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEndpoint(endpointId, outpostId, opts, (error, data, response) => {
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
 **endpointId** | **String**| The ID of the endpoint. | 
 **outpostId** | **String**| The ID of the Outposts.  | 
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
- **Accept**: application/json


## listEndpoints

> ListEndpointsResult listEndpoints(opts)



&lt;p&gt;Lists endpoints associated with the specified Outpost. &lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html\&quot;&gt;CreateEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html\&quot;&gt;DeleteEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonS3OnOutposts from 'amazon_s3_on_outposts';
let defaultClient = AmazonS3OnOutposts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonS3OnOutposts.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | If a previous response from this operation included a <code>NextToken</code> value, provide that value here to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of endpoints that will be returned in the response.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listEndpoints(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| If a previous response from this operation included a &lt;code&gt;NextToken&lt;/code&gt; value, provide that value here to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of endpoints that will be returned in the response. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListEndpointsResult**](ListEndpointsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOutpostsWithS3

> ListOutpostsWithS3Result listOutpostsWithS3(opts)



Lists the Outposts with S3 on Outposts capacity for your Amazon Web Services account. Includes S3 on Outposts that you have access to as the Outposts owner, or as a shared user from Resource Access Manager (RAM). 

### Example

```javascript
import AmazonS3OnOutposts from 'amazon_s3_on_outposts';
let defaultClient = AmazonS3OnOutposts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonS3OnOutposts.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | When you can get additional results from the <code>ListOutpostsWithS3</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional Outposts.
  'maxResults': 56, // Number | The maximum number of Outposts to return. The limit is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listOutpostsWithS3(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| When you can get additional results from the &lt;code&gt;ListOutpostsWithS3&lt;/code&gt; call, a &lt;code&gt;NextToken&lt;/code&gt; parameter is returned in the output. You can then pass in a subsequent command to the &lt;code&gt;NextToken&lt;/code&gt; parameter to continue listing additional Outposts. | [optional] 
 **maxResults** | **Number**| The maximum number of Outposts to return. The limit is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListOutpostsWithS3Result**](ListOutpostsWithS3Result.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSharedEndpoints

> ListSharedEndpointsResult listSharedEndpoints(outpostId, opts)



&lt;p&gt;Lists all endpoints associated with an Outpost that has been shared by Amazon Web Services Resource Access Manager (RAM).&lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html\&quot;&gt;CreateEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html\&quot;&gt;DeleteEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonS3OnOutposts from 'amazon_s3_on_outposts';
let defaultClient = AmazonS3OnOutposts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonS3OnOutposts.DefaultApi();
let outpostId = "outpostId_example"; // String | The ID of the Amazon Web Services Outpost.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | If a previous response from this operation included a <code>NextToken</code> value, you can provide that value here to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of endpoints that will be returned in the response.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listSharedEndpoints(outpostId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outpostId** | **String**| The ID of the Amazon Web Services Outpost. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| If a previous response from this operation included a &lt;code&gt;NextToken&lt;/code&gt; value, you can provide that value here to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of endpoints that will be returned in the response. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListSharedEndpointsResult**](ListSharedEndpointsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

