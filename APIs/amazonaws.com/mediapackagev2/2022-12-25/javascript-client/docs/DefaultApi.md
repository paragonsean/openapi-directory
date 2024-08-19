# AwsElementalMediaPackageV2.DefaultApi

All URIs are relative to *http://mediapackagev2.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChannel**](DefaultApi.md#createChannel) | **POST** /channelGroup/{ChannelGroupName}/channel | 
[**createChannelGroup**](DefaultApi.md#createChannelGroup) | **POST** /channelGroup | 
[**createOriginEndpoint**](DefaultApi.md#createOriginEndpoint) | **POST** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/originEndpoint | 
[**deleteChannel**](DefaultApi.md#deleteChannel) | **DELETE** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/ | 
[**deleteChannelGroup**](DefaultApi.md#deleteChannelGroup) | **DELETE** /channelGroup/{ChannelGroupName} | 
[**deleteChannelPolicy**](DefaultApi.md#deleteChannelPolicy) | **DELETE** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/policy | 
[**deleteOriginEndpoint**](DefaultApi.md#deleteOriginEndpoint) | **DELETE** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/originEndpoint/{OriginEndpointName} | 
[**deleteOriginEndpointPolicy**](DefaultApi.md#deleteOriginEndpointPolicy) | **DELETE** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/originEndpoint/{OriginEndpointName}/policy | 
[**getChannel**](DefaultApi.md#getChannel) | **GET** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/ | 
[**getChannelGroup**](DefaultApi.md#getChannelGroup) | **GET** /channelGroup/{ChannelGroupName} | 
[**getChannelPolicy**](DefaultApi.md#getChannelPolicy) | **GET** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/policy | 
[**getOriginEndpoint**](DefaultApi.md#getOriginEndpoint) | **GET** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/originEndpoint/{OriginEndpointName} | 
[**getOriginEndpointPolicy**](DefaultApi.md#getOriginEndpointPolicy) | **GET** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/originEndpoint/{OriginEndpointName}/policy | 
[**listChannelGroups**](DefaultApi.md#listChannelGroups) | **GET** /channelGroup | 
[**listChannels**](DefaultApi.md#listChannels) | **GET** /channelGroup/{ChannelGroupName}/channel | 
[**listOriginEndpoints**](DefaultApi.md#listOriginEndpoints) | **GET** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/originEndpoint | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**putChannelPolicy**](DefaultApi.md#putChannelPolicy) | **PUT** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/policy | 
[**putOriginEndpointPolicy**](DefaultApi.md#putOriginEndpointPolicy) | **POST** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/originEndpoint/{OriginEndpointName}/policy | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateChannel**](DefaultApi.md#updateChannel) | **PUT** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/ | 
[**updateChannelGroup**](DefaultApi.md#updateChannelGroup) | **PUT** /channelGroup/{ChannelGroupName} | 
[**updateOriginEndpoint**](DefaultApi.md#updateOriginEndpoint) | **PUT** /channelGroup/{ChannelGroupName}/channel/{ChannelName}/originEndpoint/{OriginEndpointName} | 



## createChannel

> CreateChannelResponse createChannel(channelGroupName, createChannelRequest, opts)



Create a channel to start receiving content streams. The channel represents the input to MediaPackage for incoming live content from an encoder such as AWS Elemental MediaLive. The channel receives content, and after packaging it, outputs it through an origin endpoint to downstream devices (such as video players or CDNs) that request the content. You can create only one channel with each request. We recommend that you spread out channels between channel groups, such as putting redundant channels in the same AWS Region in different channel groups.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let createChannelRequest = new AwsElementalMediaPackageV2.CreateChannelRequest(); // CreateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | A unique, case-sensitive token that you provide to ensure the idempotency of the request.
};
apiInstance.createChannel(channelGroupName, createChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **createChannelRequest** | [**CreateChannelRequest**](CreateChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| A unique, case-sensitive token that you provide to ensure the idempotency of the request. | [optional] 

### Return type

[**CreateChannelResponse**](CreateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelGroup

> CreateChannelGroupResponse createChannelGroup(createChannelGroupRequest, opts)



Create a channel group to group your channels and origin endpoints. A channel group is the top-level resource that consists of channels and origin endpoints that are associated with it and that provides predictable URLs for stream delivery. All channels and origin endpoints within the channel group are guaranteed to share the DNS. You can create only one channel group with each request. 

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let createChannelGroupRequest = new AwsElementalMediaPackageV2.CreateChannelGroupRequest(); // CreateChannelGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | A unique, case-sensitive token that you provide to ensure the idempotency of the request.
};
apiInstance.createChannelGroup(createChannelGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createChannelGroupRequest** | [**CreateChannelGroupRequest**](CreateChannelGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| A unique, case-sensitive token that you provide to ensure the idempotency of the request. | [optional] 

### Return type

[**CreateChannelGroupResponse**](CreateChannelGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOriginEndpoint

> CreateOriginEndpointResponse createOriginEndpoint(channelGroupName, channelName, createOriginEndpointRequest, opts)



The endpoint is attached to a channel, and represents the output of the live content. You can associate multiple endpoints to a single channel. Each endpoint gives players and downstream CDNs (such as Amazon CloudFront) access to the content for playback. Content can&#39;t be served from a channel until it has an endpoint. You can create only one endpoint with each request. 

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let createOriginEndpointRequest = new AwsElementalMediaPackageV2.CreateOriginEndpointRequest(); // CreateOriginEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmznClientToken': "xAmznClientToken_example" // String | A unique, case-sensitive token that you provide to ensure the idempotency of the request.
};
apiInstance.createOriginEndpoint(channelGroupName, channelName, createOriginEndpointRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **createOriginEndpointRequest** | [**CreateOriginEndpointRequest**](CreateOriginEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmznClientToken** | **String**| A unique, case-sensitive token that you provide to ensure the idempotency of the request. | [optional] 

### Return type

[**CreateOriginEndpointResponse**](CreateOriginEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteChannel

> Object deleteChannel(channelGroupName, channelName, opts)



Delete a channel to stop AWS Elemental MediaPackage from receiving further content. You must delete the channel&#39;s origin endpoints before you can delete the channel.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannel(channelGroupName, channelName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. | 
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


## deleteChannelGroup

> Object deleteChannelGroup(channelGroupName, opts)



Delete a channel group. You must delete the channel group&#39;s channels and origin endpoints before you can delete the channel group. If you delete a channel group, you&#39;ll lose access to the egress domain and will have to create a new channel group to replace it.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannelGroup(channelGroupName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
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


## deleteChannelPolicy

> Object deleteChannelPolicy(channelGroupName, channelName, opts)



Delete a channel policy.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannelPolicy(channelGroupName, channelName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. | 
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


## deleteOriginEndpoint

> Object deleteOriginEndpoint(channelGroupName, channelName, originEndpointName, opts)



Origin endpoints can serve content until they&#39;re deleted. Delete the endpoint if it should no longer respond to playback requests. You must delete all endpoints from a channel before you can delete the channel.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let originEndpointName = "originEndpointName_example"; // String | The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteOriginEndpoint(channelGroupName, channelName, originEndpointName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **originEndpointName** | **String**| The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.  | 
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


## deleteOriginEndpointPolicy

> Object deleteOriginEndpointPolicy(channelGroupName, channelName, originEndpointName, opts)



Delete an origin endpoint policy.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let originEndpointName = "originEndpointName_example"; // String | The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteOriginEndpointPolicy(channelGroupName, channelName, originEndpointName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **originEndpointName** | **String**| The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.  | 
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


## getChannel

> GetChannelResponse getChannel(channelGroupName, channelName, opts)



Retrieves the specified channel that&#39;s configured in AWS Elemental MediaPackage, including the origin endpoints that are associated with it.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getChannel(channelGroupName, channelName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetChannelResponse**](GetChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelGroup

> GetChannelGroupResponse getChannelGroup(channelGroupName, opts)



Retrieves the specified channel group that&#39;s configured in AWS Elemental MediaPackage, including the channels and origin endpoints that are associated with it.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getChannelGroup(channelGroupName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetChannelGroupResponse**](GetChannelGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelPolicy

> GetChannelPolicyResponse getChannelPolicy(channelGroupName, channelName, opts)



Retrieves the specified channel policy that&#39;s configured in AWS Elemental MediaPackage. With policies, you can specify who has access to AWS resources and what actions they can perform on those resources.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getChannelPolicy(channelGroupName, channelName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetChannelPolicyResponse**](GetChannelPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOriginEndpoint

> GetOriginEndpointResponse getOriginEndpoint(channelGroupName, channelName, originEndpointName, opts)



Retrieves the specified origin endpoint that&#39;s configured in AWS Elemental MediaPackage to obtain its playback URL and to view the packaging settings that it&#39;s currently using.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let originEndpointName = "originEndpointName_example"; // String | The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOriginEndpoint(channelGroupName, channelName, originEndpointName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **originEndpointName** | **String**| The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOriginEndpointResponse**](GetOriginEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOriginEndpointPolicy

> GetOriginEndpointPolicyResponse getOriginEndpointPolicy(channelGroupName, channelName, originEndpointName, opts)



Retrieves the specified origin endpoint policy that&#39;s configured in AWS Elemental MediaPackage.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let originEndpointName = "originEndpointName_example"; // String | The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOriginEndpointPolicy(channelGroupName, channelName, originEndpointName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **originEndpointName** | **String**| The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOriginEndpointPolicyResponse**](GetOriginEndpointPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelGroups

> ListChannelGroupsResponse listChannelGroups(opts)



Retrieves all channel groups that are configured in AWS Elemental MediaPackage, including the channels and origin endpoints that are associated with it.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in the response.
  'nextToken': "nextToken_example", // String | The pagination token from the GET list request. Use the token to fetch the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelGroups(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**| The maximum number of results to return in the response. | [optional] 
 **nextToken** | **String**| The pagination token from the GET list request. Use the token to fetch the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelGroupsResponse**](ListChannelGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannels

> ListChannelsResponse listChannels(channelGroupName, opts)



Retrieves all channels in a specific channel group that are configured in AWS Elemental MediaPackage, including the origin endpoints that are associated with it.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in the response.
  'nextToken': "nextToken_example", // String | The pagination token from the GET list request. Use the token to fetch the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannels(channelGroupName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in the response. | [optional] 
 **nextToken** | **String**| The pagination token from the GET list request. Use the token to fetch the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOriginEndpoints

> ListOriginEndpointsResponse listOriginEndpoints(channelGroupName, channelName, opts)



Retrieves all origin endpoints in a specific channel that are configured in AWS Elemental MediaPackage.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in the response.
  'nextToken': "nextToken_example", // String | The pagination token from the GET list request. Use the token to fetch the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listOriginEndpoints(channelGroupName, channelName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in the response. | [optional] 
 **nextToken** | **String**| The pagination token from the GET list request. Use the token to fetch the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListOriginEndpointsResponse**](ListOriginEndpointsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags assigned to a resource.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the CloudWatch resource that you want to view tags for.
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
 **resourceArn** | **String**| The ARN of the CloudWatch resource that you want to view tags for. | 
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


## putChannelPolicy

> Object putChannelPolicy(channelGroupName, channelName, putChannelPolicyRequest, opts)



Attaches an IAM policy to the specified channel. With policies, you can specify who has access to AWS resources and what actions they can perform on those resources. You can attach only one policy with each request.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let putChannelPolicyRequest = new AwsElementalMediaPackageV2.PutChannelPolicyRequest(); // PutChannelPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putChannelPolicy(channelGroupName, channelName, putChannelPolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **putChannelPolicyRequest** | [**PutChannelPolicyRequest**](PutChannelPolicyRequest.md)|  | 
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


## putOriginEndpointPolicy

> Object putOriginEndpointPolicy(channelGroupName, channelName, originEndpointName, putOriginEndpointPolicyRequest, opts)



Attaches an IAM policy to the specified origin endpoint. You can attach only one policy with each request.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let originEndpointName = "originEndpointName_example"; // String | The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
let putOriginEndpointPolicyRequest = new AwsElementalMediaPackageV2.PutOriginEndpointPolicyRequest(); // PutOriginEndpointPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putOriginEndpointPolicy(channelGroupName, channelName, originEndpointName, putOriginEndpointPolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **originEndpointName** | **String**| The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.  | 
 **putOriginEndpointPolicyRequest** | [**PutOriginEndpointPolicyRequest**](PutOriginEndpointPolicyRequest.md)|  | 
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

> tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Assigns one of more tags (key-value pairs) to the specified MediaPackage resource.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values. You can use the TagResource operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt;

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the MediaPackage resource that you're adding tags to.
let tagResourceRequest = new AwsElementalMediaPackageV2.TagResourceRequest(); // TagResourceRequest | 
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
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The ARN of the MediaPackage resource that you&#39;re adding tags to. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
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


## untagResource

> untagResource(resourceArn, tagKeys, opts)



Removes one or more tags from the specified resource.

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the MediaPackage resource that you're removing tags from.
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
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The ARN of the MediaPackage resource that you&#39;re removing tags from. | 
 **tagKeys** | [**[String]**](String.md)| The list of tag keys to remove from the resource. | 
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


## updateChannel

> UpdateChannelResponse updateChannel(channelGroupName, channelName, updateChannelRequest, opts)



&lt;p&gt;Update the specified channel. You can edit if MediaPackage sends ingest or egress access logs to the CloudWatch log group, if content will be encrypted, the description on a channel, and your channel&#39;s policy settings. You can&#39;t edit the name of the channel or CloudFront distribution details.&lt;/p&gt; &lt;p&gt;Any edits you make that impact the video output may not be reflected for a few minutes.&lt;/p&gt;

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let updateChannelRequest = new AwsElementalMediaPackageV2.UpdateChannelRequest(); // UpdateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannel(channelGroupName, channelName, updateChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **updateChannelRequest** | [**UpdateChannelRequest**](UpdateChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChannelResponse**](UpdateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelGroup

> UpdateChannelGroupResponse updateChannelGroup(channelGroupName, updateChannelGroupRequest, opts)



&lt;p&gt;Update the specified channel group. You can edit the description on a channel group for easier identification later from the AWS Elemental MediaPackage console. You can&#39;t edit the name of the channel group.&lt;/p&gt; &lt;p&gt;Any edits you make that impact the video output may not be reflected for a few minutes.&lt;/p&gt;

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let updateChannelGroupRequest = new AwsElementalMediaPackageV2.UpdateChannelGroupRequest(); // UpdateChannelGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannelGroup(channelGroupName, updateChannelGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **updateChannelGroupRequest** | [**UpdateChannelGroupRequest**](UpdateChannelGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChannelGroupResponse**](UpdateChannelGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOriginEndpoint

> UpdateOriginEndpointResponse updateOriginEndpoint(channelGroupName, channelName, originEndpointName, updateOriginEndpointRequest, opts)



&lt;p&gt;Update the specified origin endpoint. Edit the packaging preferences on an endpoint to optimize the viewing experience. You can&#39;t edit the name of the endpoint.&lt;/p&gt; &lt;p&gt;Any edits you make that impact the video output may not be reflected for a few minutes.&lt;/p&gt;

### Example

```javascript
import AwsElementalMediaPackageV2 from 'aws_elemental_media_package_v2';
let defaultClient = AwsElementalMediaPackageV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaPackageV2.DefaultApi();
let channelGroupName = "channelGroupName_example"; // String | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
let channelName = "channelName_example"; // String | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
let originEndpointName = "originEndpointName_example"; // String | The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
let updateOriginEndpointRequest = new AwsElementalMediaPackageV2.UpdateOriginEndpointRequest(); // UpdateOriginEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateOriginEndpoint(channelGroupName, channelName, originEndpointName, updateOriginEndpointRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelGroupName** | **String**| The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. | 
 **channelName** | **String**| The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.  | 
 **originEndpointName** | **String**| The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.  | 
 **updateOriginEndpointRequest** | [**UpdateOriginEndpointRequest**](UpdateOriginEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateOriginEndpointResponse**](UpdateOriginEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

