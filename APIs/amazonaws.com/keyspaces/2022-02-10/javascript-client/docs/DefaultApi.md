# AmazonKeyspaces.DefaultApi

All URIs are relative to *http://cassandra.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createKeyspace**](DefaultApi.md#createKeyspace) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.CreateKeyspace | 
[**createTable**](DefaultApi.md#createTable) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.CreateTable | 
[**deleteKeyspace**](DefaultApi.md#deleteKeyspace) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.DeleteKeyspace | 
[**deleteTable**](DefaultApi.md#deleteTable) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.DeleteTable | 
[**getKeyspace**](DefaultApi.md#getKeyspace) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.GetKeyspace | 
[**getTable**](DefaultApi.md#getTable) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.GetTable | 
[**listKeyspaces**](DefaultApi.md#listKeyspaces) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.ListKeyspaces | 
[**listTables**](DefaultApi.md#listTables) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.ListTables | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.ListTagsForResource | 
[**restoreTable**](DefaultApi.md#restoreTable) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.RestoreTable | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.UntagResource | 
[**updateTable**](DefaultApi.md#updateTable) | **POST** /#X-Amz-Target&#x3D;KeyspacesService.UpdateTable | 



## createKeyspace

> CreateKeyspaceResponse createKeyspace(xAmzTarget, createKeyspaceRequest, opts)



&lt;p&gt;The &lt;code&gt;CreateKeyspace&lt;/code&gt; operation adds a new keyspace to your account. In an Amazon Web Services account, keyspace names must be unique within each Region.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateKeyspace&lt;/code&gt; is an asynchronous operation. You can monitor the creation status of the new keyspace by using the &lt;code&gt;GetKeyspace&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-keyspaces.html#keyspaces-create\&quot;&gt;Creating keyspaces&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createKeyspaceRequest = new AmazonKeyspaces.CreateKeyspaceRequest(); // CreateKeyspaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createKeyspace(xAmzTarget, createKeyspaceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **createKeyspaceRequest** | [**CreateKeyspaceRequest**](CreateKeyspaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateKeyspaceResponse**](CreateKeyspaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTable

> CreateTableResponse createTable(xAmzTarget, createTableRequest, opts)



&lt;p&gt;The &lt;code&gt;CreateTable&lt;/code&gt; operation adds a new table to the specified keyspace. Within a keyspace, table names must be unique.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateTable&lt;/code&gt; is an asynchronous operation. When the request is received, the status of the table is set to &lt;code&gt;CREATING&lt;/code&gt;. You can monitor the creation status of the new table by using the &lt;code&gt;GetTable&lt;/code&gt; operation, which returns the current &lt;code&gt;status&lt;/code&gt; of the table. You can start using a table when the status is &lt;code&gt;ACTIVE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-tables.html#tables-create\&quot;&gt;Creating tables&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createTableRequest = new AmazonKeyspaces.CreateTableRequest(); // CreateTableRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTable(xAmzTarget, createTableRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **createTableRequest** | [**CreateTableRequest**](CreateTableRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateTableResponse**](CreateTableResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteKeyspace

> Object deleteKeyspace(xAmzTarget, deleteKeyspaceRequest, opts)



The &lt;code&gt;DeleteKeyspace&lt;/code&gt; operation deletes a keyspace and all of its tables. 

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteKeyspaceRequest = new AmazonKeyspaces.DeleteKeyspaceRequest(); // DeleteKeyspaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteKeyspace(xAmzTarget, deleteKeyspaceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteKeyspaceRequest** | [**DeleteKeyspaceRequest**](DeleteKeyspaceRequest.md)|  | 
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


## deleteTable

> Object deleteTable(xAmzTarget, deleteTableRequest, opts)



The &lt;code&gt;DeleteTable&lt;/code&gt; operation deletes a table and all of its data. After a &lt;code&gt;DeleteTable&lt;/code&gt; request is received, the specified table is in the &lt;code&gt;DELETING&lt;/code&gt; state until Amazon Keyspaces completes the deletion. If the table is in the &lt;code&gt;ACTIVE&lt;/code&gt; state, you can delete it. If a table is either in the &lt;code&gt;CREATING&lt;/code&gt; or &lt;code&gt;UPDATING&lt;/code&gt; states, then Amazon Keyspaces returns a &lt;code&gt;ResourceInUseException&lt;/code&gt;. If the specified table does not exist, Amazon Keyspaces returns a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;. If the table is already in the &lt;code&gt;DELETING&lt;/code&gt; state, no error is returned.

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteTableRequest = new AmazonKeyspaces.DeleteTableRequest(); // DeleteTableRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTable(xAmzTarget, deleteTableRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteTableRequest** | [**DeleteTableRequest**](DeleteTableRequest.md)|  | 
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


## getKeyspace

> GetKeyspaceResponse getKeyspace(xAmzTarget, getKeyspaceRequest, opts)



Returns the name and the Amazon Resource Name (ARN) of the specified table.

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getKeyspaceRequest = new AmazonKeyspaces.GetKeyspaceRequest(); // GetKeyspaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getKeyspace(xAmzTarget, getKeyspaceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getKeyspaceRequest** | [**GetKeyspaceRequest**](GetKeyspaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetKeyspaceResponse**](GetKeyspaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTable

> GetTableResponse getTable(xAmzTarget, getTableRequest, opts)



&lt;p&gt;Returns information about the table, including the table&#39;s name and current status, the keyspace name, configuration settings, and metadata.&lt;/p&gt; &lt;p&gt;To read table metadata using &lt;code&gt;GetTable&lt;/code&gt;, &lt;code&gt;Select&lt;/code&gt; action permissions for the table and system tables are required to complete the operation.&lt;/p&gt;

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getTableRequest = new AmazonKeyspaces.GetTableRequest(); // GetTableRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTable(xAmzTarget, getTableRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getTableRequest** | [**GetTableRequest**](GetTableRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTableResponse**](GetTableResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listKeyspaces

> ListKeyspacesResponse listKeyspaces(xAmzTarget, listKeyspacesRequest, opts)



Returns a list of keyspaces.

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listKeyspacesRequest = new AmazonKeyspaces.ListKeyspacesRequest(); // ListKeyspacesRequest | 
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
apiInstance.listKeyspaces(xAmzTarget, listKeyspacesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listKeyspacesRequest** | [**ListKeyspacesRequest**](ListKeyspacesRequest.md)|  | 
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

[**ListKeyspacesResponse**](ListKeyspacesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTables

> ListTablesResponse listTables(xAmzTarget, listTablesRequest, opts)



Returns a list of tables for a specified keyspace.

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTablesRequest = new AmazonKeyspaces.ListTablesRequest(); // ListTablesRequest | 
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
apiInstance.listTables(xAmzTarget, listTablesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listTablesRequest** | [**ListTablesRequest**](ListTablesRequest.md)|  | 
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

[**ListTablesResponse**](ListTablesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Returns a list of all tags associated with the specified Amazon Keyspaces resource.

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AmazonKeyspaces.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
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

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## restoreTable

> RestoreTableResponse restoreTable(xAmzTarget, restoreTableRequest, opts)



&lt;p&gt;Restores the specified table to the specified point in time within the &lt;code&gt;earliest_restorable_timestamp&lt;/code&gt; and the current time. For more information about restore points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_window\&quot;&gt; Time window for PITR continuous backups&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.&lt;/p&gt; &lt;p&gt;When you restore using point in time recovery, Amazon Keyspaces restores your source table&#39;s schema and data to the state based on the selected timestamp &lt;code&gt;(day:hour:minute:second)&lt;/code&gt; to a new table. The Time to Live (TTL) settings are also restored to the state based on the selected timestamp.&lt;/p&gt; &lt;p&gt;In addition to the table&#39;s schema, data, and TTL settings, &lt;code&gt;RestoreTable&lt;/code&gt; restores the capacity mode, encryption, and point-in-time recovery settings from the source table. Unlike the table&#39;s schema data and TTL settings, which are restored based on the selected timestamp, these settings are always restored based on the table&#39;s settings as of the current time or when the table was deleted.&lt;/p&gt; &lt;p&gt;You can also overwrite these settings during restore:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Read/write capacity mode&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Provisioned throughput capacity settings&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Point-in-time (PITR) settings&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tags&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_settings\&quot;&gt;PITR restore settings&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Note that the following settings are not restored, and you must configure them manually for the new table:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Automatic scaling policies (for tables that use provisioned capacity mode)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Identity and Access Management (IAM) policies&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon CloudWatch metrics and alarms&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let restoreTableRequest = new AmazonKeyspaces.RestoreTableRequest(); // RestoreTableRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.restoreTable(xAmzTarget, restoreTableRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **restoreTableRequest** | [**RestoreTableRequest**](RestoreTableRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RestoreTableResponse**](RestoreTableResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



&lt;p&gt;Associates a set of tags with a Amazon Keyspaces resource. You can then activate these user-defined tags so that they appear on the Cost Management Console for cost allocation tracking. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html\&quot;&gt;Adding tags and labels to Amazon Keyspaces resources&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For IAM policy examples that show how to control access to Amazon Keyspaces resources based on tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-tags\&quot;&gt;Amazon Keyspaces resource access based on tags&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AmazonKeyspaces.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
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

> Object untagResource(xAmzTarget, untagResourceRequest, opts)



Removes the association of tags from a Amazon Keyspaces resource.

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AmazonKeyspaces.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
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


## updateTable

> UpdateTableResponse updateTable(xAmzTarget, updateTableRequest, opts)



Adds new columns to the table or updates one of the table&#39;s settings, for example capacity mode, encryption, point-in-time recovery, or ttl settings. Note that you can only update one specific table setting per update operation.

### Example

```javascript
import AmazonKeyspaces from 'amazon_keyspaces';
let defaultClient = AmazonKeyspaces.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKeyspaces.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateTableRequest = new AmazonKeyspaces.UpdateTableRequest(); // UpdateTableRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTable(xAmzTarget, updateTableRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **updateTableRequest** | [**UpdateTableRequest**](UpdateTableRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateTableResponse**](UpdateTableResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

