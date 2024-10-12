# AwsResourceExplorer.DefaultApi

All URIs are relative to *http://resource-explorer-2.us-east-1.api.aws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateDefaultView**](DefaultApi.md#associateDefaultView) | **POST** /AssociateDefaultView | 
[**batchGetView**](DefaultApi.md#batchGetView) | **POST** /BatchGetView | 
[**createIndex**](DefaultApi.md#createIndex) | **POST** /CreateIndex | 
[**createView**](DefaultApi.md#createView) | **POST** /CreateView | 
[**deleteIndex**](DefaultApi.md#deleteIndex) | **POST** /DeleteIndex | 
[**deleteView**](DefaultApi.md#deleteView) | **POST** /DeleteView | 
[**disassociateDefaultView**](DefaultApi.md#disassociateDefaultView) | **POST** /DisassociateDefaultView | 
[**getDefaultView**](DefaultApi.md#getDefaultView) | **POST** /GetDefaultView | 
[**getIndex**](DefaultApi.md#getIndex) | **POST** /GetIndex | 
[**getView**](DefaultApi.md#getView) | **POST** /GetView | 
[**listIndexes**](DefaultApi.md#listIndexes) | **POST** /ListIndexes | 
[**listSupportedResourceTypes**](DefaultApi.md#listSupportedResourceTypes) | **POST** /ListSupportedResourceTypes | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**listViews**](DefaultApi.md#listViews) | **POST** /ListViews | 
[**search**](DefaultApi.md#search) | **POST** /Search | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateIndexType**](DefaultApi.md#updateIndexType) | **POST** /UpdateIndexType | 
[**updateView**](DefaultApi.md#updateView) | **POST** /UpdateView | 



## associateDefaultView

> AssociateDefaultViewOutput associateDefaultView(associateDefaultViewRequest, opts)



&lt;p&gt;Sets the specified view as the default for the Amazon Web Services Region in which you call this operation. When a user performs a &lt;a&gt;Search&lt;/a&gt; that doesn&#39;t explicitly specify which view to use, then Amazon Web Services Resource Explorer automatically chooses this default view for searches performed in this Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;If an Amazon Web Services Region doesn&#39;t have a default view configured, then users must explicitly specify a view with every &lt;code&gt;Search&lt;/code&gt; operation performed in that Region.&lt;/p&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let associateDefaultViewRequest = new AwsResourceExplorer.AssociateDefaultViewRequest(); // AssociateDefaultViewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateDefaultView(associateDefaultViewRequest, opts, (error, data, response) => {
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
 **associateDefaultViewRequest** | [**AssociateDefaultViewRequest**](AssociateDefaultViewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateDefaultViewOutput**](AssociateDefaultViewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGetView

> BatchGetViewOutput batchGetView(batchGetViewRequest, opts)



Retrieves details about a list of views.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let batchGetViewRequest = new AwsResourceExplorer.BatchGetViewRequest(); // BatchGetViewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetView(batchGetViewRequest, opts, (error, data, response) => {
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
 **batchGetViewRequest** | [**BatchGetViewRequest**](BatchGetViewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetViewOutput**](BatchGetViewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createIndex

> CreateIndexOutput createIndex(createIndexRequest, opts)



&lt;p&gt;Turns on Amazon Web Services Resource Explorer in the Amazon Web Services Region in which you called this operation by creating an index. Resource Explorer begins discovering the resources in this Region and stores the details about the resources in the index so that they can be queried by using the &lt;a&gt;Search&lt;/a&gt; operation. You can create only one index in a Region.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation creates only a &lt;i&gt;local&lt;/i&gt; index. To promote the local index in one Amazon Web Services Region into the aggregator index for the Amazon Web Services account, use the &lt;a&gt;UpdateIndexType&lt;/a&gt; operation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html\&quot;&gt;Turning on cross-Region search by creating an aggregator index&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Resource Explorer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more details about what happens when you turn on Resource Explorer in an Amazon Web Services Region, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-activate.html\&quot;&gt;Turn on Resource Explorer to index your resources in an Amazon Web Services Region&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Resource Explorer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If this is the first Amazon Web Services Region in which you&#39;ve created an index for Resource Explorer, then this operation also &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html\&quot;&gt;creates a service-linked role&lt;/a&gt; in your Amazon Web Services account that allows Resource Explorer to enumerate your resources to populate the index.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Action&lt;/b&gt;: &lt;code&gt;resource-explorer-2:CreateIndex&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Resource&lt;/b&gt;: The ARN of the index (as it will exist after the operation completes) in the Amazon Web Services Region and account in which you&#39;re trying to create the index. Use the wildcard character (&lt;code&gt;*&lt;/code&gt;) at the end of the string to match the eventual UUID. For example, the following &lt;code&gt;Resource&lt;/code&gt; element restricts the role or user to creating an index in only the &lt;code&gt;us-east-2&lt;/code&gt; Region of the specified account.&lt;/p&gt; &lt;p&gt; &lt;code&gt;\&quot;Resource\&quot;: \&quot;arn:aws:resource-explorer-2:us-west-2:&lt;i&gt;&amp;lt;account-id&amp;gt;&lt;/i&gt;:index/_*\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Alternatively, you can use &lt;code&gt;\&quot;Resource\&quot;: \&quot;*\&quot;&lt;/code&gt; to allow the role or user to create an index in any Region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Action&lt;/b&gt;: &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Resource&lt;/b&gt;: No specific resource (*). &lt;/p&gt; &lt;p&gt;This permission is required only the first time you create an index to turn on Resource Explorer in the account. Resource Explorer uses this to create the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html\&quot;&gt;service-linked role needed to index the resources in your account&lt;/a&gt;. Resource Explorer uses the same service-linked role for all additional indexes you create afterwards.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let createIndexRequest = new AwsResourceExplorer.CreateIndexRequest(); // CreateIndexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIndex(createIndexRequest, opts, (error, data, response) => {
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
 **createIndexRequest** | [**CreateIndexRequest**](CreateIndexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIndexOutput**](CreateIndexOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createView

> CreateViewOutput createView(createViewRequest, opts)



&lt;p&gt;Creates a view that users can query by using the &lt;a&gt;Search&lt;/a&gt; operation. Results from queries that you make using this view include only resources that match the view&#39;s &lt;code&gt;Filters&lt;/code&gt;. For more information about Amazon Web Services Resource Explorer views, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views.html\&quot;&gt;Managing views&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Resource Explorer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Only the principals with an IAM identity-based policy that grants &lt;code&gt;Allow&lt;/code&gt; to the &lt;code&gt;Search&lt;/code&gt; action on a &lt;code&gt;Resource&lt;/code&gt; with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon resource name (ARN)&lt;/a&gt; of this view can &lt;a&gt;Search&lt;/a&gt; using views you create with this operation.&lt;/p&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let createViewRequest = new AwsResourceExplorer.CreateViewRequest(); // CreateViewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createView(createViewRequest, opts, (error, data, response) => {
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
 **createViewRequest** | [**CreateViewRequest**](CreateViewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateViewOutput**](CreateViewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteIndex

> DeleteIndexOutput deleteIndex(deleteIndexRequest, opts)



&lt;p&gt;Deletes the specified index and turns off Amazon Web Services Resource Explorer in the specified Amazon Web Services Region. When you delete an index, Resource Explorer stops discovering and indexing resources in that Region. Resource Explorer also deletes all views in that Region. These actions occur as asynchronous background tasks. You can check to see when the actions are complete by using the &lt;a&gt;GetIndex&lt;/a&gt; operation and checking the &lt;code&gt;Status&lt;/code&gt; response value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the index you delete is the aggregator index for the Amazon Web Services account, you must wait 24 hours before you can promote another local index to be the aggregator index for the account. Users can&#39;t perform account-wide searches using Resource Explorer until another aggregator index is configured.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let deleteIndexRequest = new AwsResourceExplorer.DeleteIndexRequest(); // DeleteIndexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIndex(deleteIndexRequest, opts, (error, data, response) => {
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
 **deleteIndexRequest** | [**DeleteIndexRequest**](DeleteIndexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteIndexOutput**](DeleteIndexOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteView

> DeleteViewOutput deleteView(deleteViewRequest, opts)



&lt;p&gt;Deletes the specified view.&lt;/p&gt; &lt;p&gt;If the specified view is the default view for its Amazon Web Services Region, then all &lt;a&gt;Search&lt;/a&gt; operations in that Region must explicitly specify the view to use until you configure a new default by calling the &lt;a&gt;AssociateDefaultView&lt;/a&gt; operation.&lt;/p&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let deleteViewRequest = new AwsResourceExplorer.DeleteViewRequest(); // DeleteViewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteView(deleteViewRequest, opts, (error, data, response) => {
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
 **deleteViewRequest** | [**DeleteViewRequest**](DeleteViewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteViewOutput**](DeleteViewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateDefaultView

> disassociateDefaultView(opts)



&lt;p&gt;After you call this operation, the affected Amazon Web Services Region no longer has a default view. All &lt;a&gt;Search&lt;/a&gt; operations in that Region must explicitly specify a view or the operation fails. You can configure a new default by calling the &lt;a&gt;AssociateDefaultView&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;If an Amazon Web Services Region doesn&#39;t have a default view configured, then users must explicitly specify a view with every &lt;code&gt;Search&lt;/code&gt; operation performed in that Region.&lt;/p&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateDefaultView(opts, (error, data, response) => {
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


## getDefaultView

> GetDefaultViewOutput getDefaultView(opts)



Retrieves the Amazon Resource Name (ARN) of the view that is the default for the Amazon Web Services Region in which you call this operation. You can then call &lt;a&gt;GetView&lt;/a&gt; to retrieve the details of that view.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDefaultView(opts, (error, data, response) => {
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

### Return type

[**GetDefaultViewOutput**](GetDefaultViewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIndex

> GetIndexOutput getIndex(opts)



Retrieves details about the Amazon Web Services Resource Explorer index in the Amazon Web Services Region in which you invoked the operation.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIndex(opts, (error, data, response) => {
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

### Return type

[**GetIndexOutput**](GetIndexOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getView

> GetViewOutput getView(getViewRequest, opts)



Retrieves details of the specified view.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let getViewRequest = new AwsResourceExplorer.GetViewRequest(); // GetViewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getView(getViewRequest, opts, (error, data, response) => {
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
 **getViewRequest** | [**GetViewRequest**](GetViewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetViewOutput**](GetViewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIndexes

> ListIndexesOutput listIndexes(listIndexesRequest, opts)



Retrieves a list of all of the indexes in Amazon Web Services Regions that are currently collecting resource information for Amazon Web Services Resource Explorer.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let listIndexesRequest = new AwsResourceExplorer.ListIndexesRequest(); // ListIndexesRequest | 
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
apiInstance.listIndexes(listIndexesRequest, opts, (error, data, response) => {
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
 **listIndexesRequest** | [**ListIndexesRequest**](ListIndexesRequest.md)|  | 
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

[**ListIndexesOutput**](ListIndexesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSupportedResourceTypes

> ListSupportedResourceTypesOutput listSupportedResourceTypes(listSupportedResourceTypesRequest, opts)



Retrieves a list of all resource types currently supported by Amazon Web Services Resource Explorer.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let listSupportedResourceTypesRequest = new AwsResourceExplorer.ListSupportedResourceTypesRequest(); // ListSupportedResourceTypesRequest | 
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
apiInstance.listSupportedResourceTypes(listSupportedResourceTypesRequest, opts, (error, data, response) => {
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
 **listSupportedResourceTypesRequest** | [**ListSupportedResourceTypesRequest**](ListSupportedResourceTypesRequest.md)|  | 
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

[**ListSupportedResourceTypesOutput**](ListSupportedResourceTypesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(resourceArn, opts)



Lists the tags that are attached to the specified resource.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view or index that you want to attach tags to.
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
 **resourceArn** | **String**| The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon resource name (ARN)&lt;/a&gt; of the view or index that you want to attach tags to. | 
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


## listViews

> ListViewsOutput listViews(listViewsRequest, opts)



&lt;p&gt;Lists the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon resource names (ARNs)&lt;/a&gt; of the views available in the Amazon Web Services Region in which you call this operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let listViewsRequest = new AwsResourceExplorer.ListViewsRequest(); // ListViewsRequest | 
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
apiInstance.listViews(listViewsRequest, opts, (error, data, response) => {
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
 **listViewsRequest** | [**ListViewsRequest**](ListViewsRequest.md)|  | 
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

[**ListViewsOutput**](ListViewsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## search

> SearchOutput search(searchRequest, opts)



&lt;p&gt;Searches for resources and displays details about all resources that match the specified criteria. You must specify a query string.&lt;/p&gt; &lt;p&gt;All search queries must use a view. If you don&#39;t explicitly specify a view, then Amazon Web Services Resource Explorer uses the default view for the Amazon Web Services Region in which you call this operation. The results are the logical intersection of the results that match both the &lt;code&gt;QueryString&lt;/code&gt; parameter supplied to this operation and the &lt;code&gt;SearchFilter&lt;/code&gt; parameter attached to the view.&lt;/p&gt; &lt;p&gt;For the complete syntax supported by the &lt;code&gt;QueryString&lt;/code&gt; parameter, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/APIReference/about-query-syntax.html\&quot;&gt;Search query syntax reference for Resource Explorer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If your search results are empty, or are missing results that you think should be there, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html\&quot;&gt;Troubleshooting Resource Explorer search&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let searchRequest = new AwsResourceExplorer.SearchRequest(); // SearchRequest | 
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
apiInstance.search(searchRequest, opts, (error, data, response) => {
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
 **searchRequest** | [**SearchRequest**](SearchRequest.md)|  | 
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

[**SearchOutput**](SearchOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds one or more tag key and value pairs to an Amazon Web Services Resource Explorer view or index.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the view or index that you want to attach tags to.
let tagResourceRequest = new AwsResourceExplorer.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the view or index that you want to attach tags to. | 
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



Removes one or more tag key and value pairs from an Amazon Web Services Resource Explorer view or index.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the view or index that you want to remove tags from.
let tagKeys = ["null"]; // [String] | A list of the keys for the tags that you want to remove from the specified view or index.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the view or index that you want to remove tags from. | 
 **tagKeys** | [**[String]**](String.md)| A list of the keys for the tags that you want to remove from the specified view or index. | 
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


## updateIndexType

> UpdateIndexTypeOutput updateIndexType(updateIndexTypeRequest, opts)



&lt;p&gt;Changes the type of the index from one of the following types to the other. For more information about indexes and the role they perform in Amazon Web Services Resource Explorer, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html\&quot;&gt;Turning on cross-Region search by creating an aggregator index&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Resource Explorer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;AGGREGATOR&lt;/code&gt; index type&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The index contains information about resources from all Amazon Web Services Regions in the Amazon Web Services account in which you&#39;ve created a Resource Explorer index. Resource information from all other Regions is replicated to this Region&#39;s index.&lt;/p&gt; &lt;p&gt;When you change the index type to &lt;code&gt;AGGREGATOR&lt;/code&gt;, Resource Explorer turns on replication of all discovered resource information from the other Amazon Web Services Regions in your account to this index. You can then, from this Region only, perform resource search queries that span all Amazon Web Services Regions in the Amazon Web Services account. Turning on replication from all other Regions is performed by asynchronous background tasks. You can check the status of the asynchronous tasks by using the &lt;a&gt;GetIndex&lt;/a&gt; operation. When the asynchronous tasks complete, the &lt;code&gt;Status&lt;/code&gt; response of that operation changes from &lt;code&gt;UPDATING&lt;/code&gt; to &lt;code&gt;ACTIVE&lt;/code&gt;. After that, you can start to see results from other Amazon Web Services Regions in query results. However, it can take several hours for replication from all other Regions to complete.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can have only one aggregator index per Amazon Web Services account. Before you can promote a different index to be the aggregator index for the account, you must first demote the existing aggregator index to type &lt;code&gt;LOCAL&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;LOCAL&lt;/code&gt; index type&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The index contains information about resources in only the Amazon Web Services Region in which the index exists. If an aggregator index in another Region exists, then information in this local index is replicated to the aggregator index.&lt;/p&gt; &lt;p&gt;When you change the index type to &lt;code&gt;LOCAL&lt;/code&gt;, Resource Explorer turns off the replication of resource information from all other Amazon Web Services Regions in the Amazon Web Services account to this Region. The aggregator index remains in the &lt;code&gt;UPDATING&lt;/code&gt; state until all replication with other Regions successfully stops. You can check the status of the asynchronous task by using the &lt;a&gt;GetIndex&lt;/a&gt; operation. When Resource Explorer successfully stops all replication with other Regions, the &lt;code&gt;Status&lt;/code&gt; response of that operation changes from &lt;code&gt;UPDATING&lt;/code&gt; to &lt;code&gt;ACTIVE&lt;/code&gt;. Separately, the resource information from other Regions that was previously stored in the index is deleted within 30 days by another background task. Until that asynchronous task completes, some results from other Regions can continue to appear in search results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After you demote an aggregator index to a local index, you must wait 24 hours before you can promote another index to be the new aggregator index for the account.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let updateIndexTypeRequest = new AwsResourceExplorer.UpdateIndexTypeRequest(); // UpdateIndexTypeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIndexType(updateIndexTypeRequest, opts, (error, data, response) => {
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
 **updateIndexTypeRequest** | [**UpdateIndexTypeRequest**](UpdateIndexTypeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateIndexTypeOutput**](UpdateIndexTypeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateView

> UpdateViewOutput updateView(updateViewRequest, opts)



Modifies some of the details of a view. You can change the filter string and the list of included properties. You can&#39;t change the name of the view.

### Example

```javascript
import AwsResourceExplorer from 'aws_resource_explorer';
let defaultClient = AwsResourceExplorer.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceExplorer.DefaultApi();
let updateViewRequest = new AwsResourceExplorer.UpdateViewRequest(); // UpdateViewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateView(updateViewRequest, opts, (error, data, response) => {
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
 **updateViewRequest** | [**UpdateViewRequest**](UpdateViewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateViewOutput**](UpdateViewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

