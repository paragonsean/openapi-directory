# CloudWatchObservabilityAccessManager.DefaultApi

All URIs are relative to *http://oam.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLink**](DefaultApi.md#createLink) | **POST** /CreateLink | 
[**createSink**](DefaultApi.md#createSink) | **POST** /CreateSink | 
[**deleteLink**](DefaultApi.md#deleteLink) | **POST** /DeleteLink | 
[**deleteSink**](DefaultApi.md#deleteSink) | **POST** /DeleteSink | 
[**getLink**](DefaultApi.md#getLink) | **POST** /GetLink | 
[**getSink**](DefaultApi.md#getSink) | **POST** /GetSink | 
[**getSinkPolicy**](DefaultApi.md#getSinkPolicy) | **POST** /GetSinkPolicy | 
[**listAttachedLinks**](DefaultApi.md#listAttachedLinks) | **POST** /ListAttachedLinks | 
[**listLinks**](DefaultApi.md#listLinks) | **POST** /ListLinks | 
[**listSinks**](DefaultApi.md#listSinks) | **POST** /ListSinks | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**putSinkPolicy**](DefaultApi.md#putSinkPolicy) | **POST** /PutSinkPolicy | 
[**tagResource**](DefaultApi.md#tagResource) | **PUT** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateLink**](DefaultApi.md#updateLink) | **POST** /UpdateLink | 



## createLink

> CreateLinkOutput createLink(createLinkRequest, opts)



&lt;p&gt;Creates a link between a source account and a sink that you have created in a monitoring account.&lt;/p&gt; &lt;p&gt;Before you create a link, you must create a sink in the monitoring account and create a sink policy in that account. The sink policy must permit the source account to link to it. You can grant permission to source accounts by granting permission to an entire organization or to individual accounts.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html\&quot;&gt;CreateSink&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html\&quot;&gt;PutSinkPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each monitoring account can be linked to as many as 100,000 source accounts.&lt;/p&gt; &lt;p&gt;Each source account can be linked to as many as five monitoring accounts.&lt;/p&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let createLinkRequest = new CloudWatchObservabilityAccessManager.CreateLinkRequest(); // CreateLinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLink(createLinkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createLinkRequest** | [**CreateLinkRequest**](CreateLinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLinkOutput**](CreateLinkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSink

> CreateSinkOutput createSink(createSinkRequest, opts)



&lt;p&gt;Use this to create a &lt;i&gt;sink&lt;/i&gt; in the current account, so that it can be used as a monitoring account in CloudWatch cross-account observability. A sink is a resource that represents an attachment point in a monitoring account. Source accounts can link to the sink to send observability data.&lt;/p&gt; &lt;p&gt;After you create a sink, you must create a sink policy that allows source accounts to attach to it. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html\&quot;&gt;PutSinkPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each account can contain one sink. If you delete a sink, you can then create a new one in that account.&lt;/p&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let createSinkRequest = new CloudWatchObservabilityAccessManager.CreateSinkRequest(); // CreateSinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSink(createSinkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createSinkRequest** | [**CreateSinkRequest**](CreateSinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSinkOutput**](CreateSinkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLink

> Object deleteLink(deleteLinkRequest, opts)



Deletes a link between a monitoring account sink and a source account. You must run this operation in the source account.

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let deleteLinkRequest = new CloudWatchObservabilityAccessManager.DeleteLinkRequest(); // DeleteLinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLink(deleteLinkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleteLinkRequest** | [**DeleteLinkRequest**](DeleteLinkRequest.md)|  | 
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


## deleteSink

> Object deleteSink(deleteSinkRequest, opts)



Deletes a sink. You must delete all links to a sink before you can delete that sink.

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let deleteSinkRequest = new CloudWatchObservabilityAccessManager.DeleteSinkRequest(); // DeleteSinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSink(deleteSinkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleteSinkRequest** | [**DeleteSinkRequest**](DeleteSinkRequest.md)|  | 
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


## getLink

> GetLinkOutput getLink(getLinkRequest, opts)



&lt;p&gt;Returns complete information about one link.&lt;/p&gt; &lt;p&gt;To use this operation, provide the link ARN. To retrieve a list of link ARNs, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html\&quot;&gt;ListLinks&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let getLinkRequest = new CloudWatchObservabilityAccessManager.GetLinkRequest(); // GetLinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLink(getLinkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **getLinkRequest** | [**GetLinkRequest**](GetLinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLinkOutput**](GetLinkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSink

> GetSinkOutput getSink(getSinkRequest, opts)



&lt;p&gt;Returns complete information about one monitoring account sink.&lt;/p&gt; &lt;p&gt;To use this operation, provide the sink ARN. To retrieve a list of sink ARNs, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html\&quot;&gt;ListSinks&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let getSinkRequest = new CloudWatchObservabilityAccessManager.GetSinkRequest(); // GetSinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSink(getSinkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **getSinkRequest** | [**GetSinkRequest**](GetSinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSinkOutput**](GetSinkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSinkPolicy

> GetSinkPolicyOutput getSinkPolicy(getSinkPolicyRequest, opts)



Returns the current sink policy attached to this sink. The sink policy specifies what accounts can attach to this sink as source accounts, and what types of data they can share.

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let getSinkPolicyRequest = new CloudWatchObservabilityAccessManager.GetSinkPolicyRequest(); // GetSinkPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSinkPolicy(getSinkPolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **getSinkPolicyRequest** | [**GetSinkPolicyRequest**](GetSinkPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSinkPolicyOutput**](GetSinkPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAttachedLinks

> ListAttachedLinksOutput listAttachedLinks(listAttachedLinksRequest, opts)



&lt;p&gt;Returns a list of source account links that are linked to this monitoring account sink.&lt;/p&gt; &lt;p&gt;To use this operation, provide the sink ARN. To retrieve a list of sink ARNs, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html\&quot;&gt;ListSinks&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To find a list of links for one source account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html\&quot;&gt;ListLinks&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let listAttachedLinksRequest = new CloudWatchObservabilityAccessManager.ListAttachedLinksRequest(); // ListAttachedLinksRequest | 
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
apiInstance.listAttachedLinks(listAttachedLinksRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listAttachedLinksRequest** | [**ListAttachedLinksRequest**](ListAttachedLinksRequest.md)|  | 
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

[**ListAttachedLinksOutput**](ListAttachedLinksOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLinks

> ListLinksOutput listLinks(listLinksRequest, opts)



&lt;p&gt;Use this operation in a source account to return a list of links to monitoring account sinks that this source account has.&lt;/p&gt; &lt;p&gt;To find a list of links for one monitoring account sink, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinks.html\&quot;&gt;ListAttachedLinks&lt;/a&gt; from within the monitoring account.&lt;/p&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let listLinksRequest = new CloudWatchObservabilityAccessManager.ListLinksRequest(); // ListLinksRequest | 
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
apiInstance.listLinks(listLinksRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listLinksRequest** | [**ListLinksRequest**](ListLinksRequest.md)|  | 
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

[**ListLinksOutput**](ListLinksOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSinks

> ListSinksOutput listSinks(listSinksRequest, opts)



Use this operation in a monitoring account to return the list of sinks created in that account.

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let listSinksRequest = new CloudWatchObservabilityAccessManager.ListSinksRequest(); // ListSinksRequest | 
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
apiInstance.listSinks(listSinksRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listSinksRequest** | [**ListSinksRequest**](ListSinksRequest.md)|  | 
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

[**ListSinksOutput**](ListSinksOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(resourceArn, opts)



Displays the tags associated with a resource. Both sinks and links support tagging.

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The ARN of the resource that you want to view tags for.</p> <p>The ARN format of a sink is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:sink/<i>sink-id</i> </code> </p> <p>The ARN format of a link is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:link/<i>link-id</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\">CloudWatch Logs resources and operations</a>.</p> <important> <p>Unlike tagging permissions in other Amazon Web Services services, to retrieve the list of tags for links or sinks you must have the <code>oam:RequestTag</code> permission. The <code>aws:ReguestTag</code> permission does not allow you to tag and untag links and sinks.</p> </important>
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
 **resourceArn** | **String**| &lt;p&gt;The ARN of the resource that you want to view tags for.&lt;/p&gt; &lt;p&gt;The ARN format of a sink is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:sink/&lt;i&gt;sink-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a link is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:link/&lt;i&gt;link-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\&quot;&gt;CloudWatch Logs resources and operations&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Unlike tagging permissions in other Amazon Web Services services, to retrieve the list of tags for links or sinks you must have the &lt;code&gt;oam:RequestTag&lt;/code&gt; permission. The &lt;code&gt;aws:ReguestTag&lt;/code&gt; permission does not allow you to tag and untag links and sinks.&lt;/p&gt; &lt;/important&gt; | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## putSinkPolicy

> PutSinkPolicyOutput putSinkPolicy(putSinkPolicyRequest, opts)



&lt;p&gt;Creates or updates the resource policy that grants permissions to source accounts to link to the monitoring account sink. When you create a sink policy, you can grant permissions to all accounts in an organization or to individual accounts.&lt;/p&gt; &lt;p&gt;You can also use a sink policy to limit the types of data that is shared. The three types that you can allow or deny are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Metrics&lt;/b&gt; - Specify with &lt;code&gt;AWS::CloudWatch::Metric&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Log groups&lt;/b&gt; - Specify with &lt;code&gt;AWS::Logs::LogGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Traces&lt;/b&gt; - Specify with &lt;code&gt;AWS::XRay::Trace&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;See the examples in this section to see how to specify permitted source accounts and data types.&lt;/p&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let putSinkPolicyRequest = new CloudWatchObservabilityAccessManager.PutSinkPolicyRequest(); // PutSinkPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putSinkPolicy(putSinkPolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **putSinkPolicyRequest** | [**PutSinkPolicyRequest**](PutSinkPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutSinkPolicyOutput**](PutSinkPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Assigns one or more tags (key-value pairs) to the specified resource. Both sinks and links can be tagged. &lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Unlike tagging permissions in other Amazon Web Services services, to tag or untag links and sinks you must have the &lt;code&gt;oam:ResourceTag&lt;/code&gt; permission. The &lt;code&gt;iam:ResourceTag&lt;/code&gt; permission does not allow you to tag and untag links and sinks.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The ARN of the resource that you're adding tags to.</p> <p>The ARN format of a sink is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:sink/<i>sink-id</i> </code> </p> <p>The ARN format of a link is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:link/<i>link-id</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\">CloudWatch Logs resources and operations</a>.</p>
let tagResourceRequest = new CloudWatchObservabilityAccessManager.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| &lt;p&gt;The ARN of the resource that you&#39;re adding tags to.&lt;/p&gt; &lt;p&gt;The ARN format of a sink is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:sink/&lt;i&gt;sink-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a link is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:link/&lt;i&gt;link-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\&quot;&gt;CloudWatch Logs resources and operations&lt;/a&gt;.&lt;/p&gt; | 
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



&lt;p&gt;Removes one or more tags from the specified resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Unlike tagging permissions in other Amazon Web Services services, to tag or untag links and sinks you must have the &lt;code&gt;oam:ResourceTag&lt;/code&gt; permission. The &lt;code&gt;iam:TagResource&lt;/code&gt; permission does not allow you to tag and untag links and sinks.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let resourceArn = "resourceArn_example"; // String | <p>The ARN of the resource that you're removing tags from.</p> <p>The ARN format of a sink is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:sink/<i>sink-id</i> </code> </p> <p>The ARN format of a link is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:link/<i>link-id</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\">CloudWatch Logs resources and operations</a>.</p>
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
 **resourceArn** | **String**| &lt;p&gt;The ARN of the resource that you&#39;re removing tags from.&lt;/p&gt; &lt;p&gt;The ARN format of a sink is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:sink/&lt;i&gt;sink-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a link is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:link/&lt;i&gt;link-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\&quot;&gt;CloudWatch Logs resources and operations&lt;/a&gt;.&lt;/p&gt; | 
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


## updateLink

> UpdateLinkOutput updateLink(updateLinkRequest, opts)



&lt;p&gt;Use this operation to change what types of data are shared from a source account to its linked monitoring account sink. You can&#39;t change the sink or change the monitoring account with this operation.&lt;/p&gt; &lt;p&gt;To update the list of tags associated with the sink, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import CloudWatchObservabilityAccessManager from 'cloud_watch_observability_access_manager';
let defaultClient = CloudWatchObservabilityAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchObservabilityAccessManager.DefaultApi();
let updateLinkRequest = new CloudWatchObservabilityAccessManager.UpdateLinkRequest(); // UpdateLinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLink(updateLinkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateLinkRequest** | [**UpdateLinkRequest**](UpdateLinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateLinkOutput**](UpdateLinkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

