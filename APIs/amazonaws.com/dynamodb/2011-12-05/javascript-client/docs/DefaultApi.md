# AmazonDynamoDb.DefaultApi

All URIs are relative to *http://dynamodb.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchGetItem**](DefaultApi.md#batchGetItem) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.BatchGetItem | 
[**batchWriteItem**](DefaultApi.md#batchWriteItem) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.BatchWriteItem | 
[**createTable**](DefaultApi.md#createTable) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.CreateTable | 
[**deleteItem**](DefaultApi.md#deleteItem) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.DeleteItem | 
[**deleteTable**](DefaultApi.md#deleteTable) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.DeleteTable | 
[**describeTable**](DefaultApi.md#describeTable) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.DescribeTable | 
[**getItem**](DefaultApi.md#getItem) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.GetItem | 
[**listTables**](DefaultApi.md#listTables) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.ListTables | 
[**putItem**](DefaultApi.md#putItem) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.PutItem | 
[**query**](DefaultApi.md#query) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.Query | 
[**scan**](DefaultApi.md#scan) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.Scan | 
[**updateItem**](DefaultApi.md#updateItem) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.UpdateItem | 
[**updateTable**](DefaultApi.md#updateTable) | **POST** /#X-Amz-Target&#x3D;DynamoDB_20111205.UpdateTable | 



## batchGetItem

> BatchGetItemOutput batchGetItem(xAmzTarget, batchGetItemInput, opts)



&lt;p&gt;Retrieves the attributes for multiple items from multiple tables using their primary keys.&lt;/p&gt; &lt;p&gt;The maximum number of item attributes that can be retrieved for a single operation is 100. Also, the number of items retrieved is constrained by a 1 MB the size limit. If the response size limit is exceeded or a partial result is returned due to an internal processing failure, Amazon DynamoDB returns an &lt;code&gt;UnprocessedKeys&lt;/code&gt; value so you can retry the operation starting with the next item to get.&lt;/p&gt; &lt;p&gt;Amazon DynamoDB automatically adjusts the number of items returned per page to enforce this limit. For example, even if you ask to retrieve 100 items, but each individual item is 50k in size, the system returns 20 items and an appropriate &lt;code&gt;UnprocessedKeys&lt;/code&gt; value so you can get the next page of results. If necessary, your application needs its own logic to assemble the pages of results into one set.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let batchGetItemInput = new AmazonDynamoDb.BatchGetItemInput(); // BatchGetItemInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'requestItems': "requestItems_example" // String | Pagination token
};
apiInstance.batchGetItem(xAmzTarget, batchGetItemInput, opts, (error, data, response) => {
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
 **batchGetItemInput** | [**BatchGetItemInput**](BatchGetItemInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **requestItems** | **String**| Pagination token | [optional] 

### Return type

[**BatchGetItemOutput**](BatchGetItemOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchWriteItem

> BatchWriteItemOutput batchWriteItem(xAmzTarget, batchWriteItemInput, opts)



&lt;p&gt;Allows to execute a batch of Put and/or Delete Requests for many tables in a single call. A total of 25 requests are allowed.&lt;/p&gt; &lt;p&gt;There are no transaction guarantees provided by this API. It does not allow conditional puts nor does it support return values.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let batchWriteItemInput = new AmazonDynamoDb.BatchWriteItemInput(); // BatchWriteItemInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchWriteItem(xAmzTarget, batchWriteItemInput, opts, (error, data, response) => {
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
 **batchWriteItemInput** | [**BatchWriteItemInput**](BatchWriteItemInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchWriteItemOutput**](BatchWriteItemOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTable

> CreateTableOutput createTable(xAmzTarget, createTableInput, opts)



&lt;p&gt;Adds a new table to your account.&lt;/p&gt; &lt;p&gt;The table name must be unique among those associated with the AWS Account issuing the request, and the AWS Region that receives the request (e.g. &lt;code&gt;us-east-1&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;The &lt;code&gt;CreateTable&lt;/code&gt; operation triggers an asynchronous workflow to begin creating the table. Amazon DynamoDB immediately returns the state of the table (&lt;code&gt;CREATING&lt;/code&gt;) until the table is in the &lt;code&gt;ACTIVE&lt;/code&gt; state. Once the table is in the &lt;code&gt;ACTIVE&lt;/code&gt; state, you can perform data plane operations.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createTableInput = new AmazonDynamoDb.CreateTableInput(); // CreateTableInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTable(xAmzTarget, createTableInput, opts, (error, data, response) => {
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
 **createTableInput** | [**CreateTableInput**](CreateTableInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateTableOutput**](CreateTableOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteItem

> DeleteItemOutput deleteItem(xAmzTarget, deleteItemInput, opts)



&lt;p&gt;Deletes a single item in a table by primary key.&lt;/p&gt; &lt;p&gt;You can perform a conditional delete operation that deletes the item if it exists, or if it has an expected attribute value.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteItemInput = new AmazonDynamoDb.DeleteItemInput(); // DeleteItemInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteItem(xAmzTarget, deleteItemInput, opts, (error, data, response) => {
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
 **deleteItemInput** | [**DeleteItemInput**](DeleteItemInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteItemOutput**](DeleteItemOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTable

> DeleteTableOutput deleteTable(xAmzTarget, deleteTableInput, opts)



&lt;p&gt;Deletes a table and all of its items.&lt;/p&gt; &lt;p&gt;If the table is in the &lt;code&gt;ACTIVE&lt;/code&gt; state, you can delete it. If a table is in &lt;code&gt;CREATING&lt;/code&gt; or &lt;code&gt;UPDATING&lt;/code&gt; states then Amazon DynamoDB returns a &lt;code&gt;ResourceInUseException&lt;/code&gt;. If the specified table does not exist, Amazon DynamoDB returns a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteTableInput = new AmazonDynamoDb.DeleteTableInput(); // DeleteTableInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTable(xAmzTarget, deleteTableInput, opts, (error, data, response) => {
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
 **deleteTableInput** | [**DeleteTableInput**](DeleteTableInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteTableOutput**](DeleteTableOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeTable

> DescribeTableOutput describeTable(xAmzTarget, describeTableInput, opts)



&lt;p&gt;Retrieves information about the table, including the current status of the table, the primary key schema and when the table was created.&lt;/p&gt; &lt;p&gt;If the table does not exist, Amazon DynamoDB returns a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeTableInput = new AmazonDynamoDb.DescribeTableInput(); // DescribeTableInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTable(xAmzTarget, describeTableInput, opts, (error, data, response) => {
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
 **describeTableInput** | [**DescribeTableInput**](DescribeTableInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTableOutput**](DescribeTableOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getItem

> GetItemOutput getItem(xAmzTarget, getItemInput, opts)



&lt;p&gt;Retrieves a set of Attributes for an item that matches the primary key.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetItem&lt;/code&gt; operation provides an eventually-consistent read by default. If eventually-consistent reads are not acceptable for your application, use &lt;code&gt;ConsistentRead&lt;/code&gt;. Although this operation might take longer than a standard read, it always returns the last updated value.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getItemInput = new AmazonDynamoDb.GetItemInput(); // GetItemInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getItem(xAmzTarget, getItemInput, opts, (error, data, response) => {
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
 **getItemInput** | [**GetItemInput**](GetItemInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetItemOutput**](GetItemOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTables

> ListTablesOutput listTables(xAmzTarget, listTablesInput, opts)



Retrieves a paginated list of table names created by the AWS Account of the caller in the AWS Region (e.g. &lt;code&gt;us-east-1&lt;/code&gt;).

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTablesInput = new AmazonDynamoDb.ListTablesInput(); // ListTablesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': "limit_example", // String | Pagination limit
  'exclusiveStartTableName': "exclusiveStartTableName_example" // String | Pagination token
};
apiInstance.listTables(xAmzTarget, listTablesInput, opts, (error, data, response) => {
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
 **listTablesInput** | [**ListTablesInput**](ListTablesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **String**| Pagination limit | [optional] 
 **exclusiveStartTableName** | **String**| Pagination token | [optional] 

### Return type

[**ListTablesOutput**](ListTablesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putItem

> PutItemOutput putItem(xAmzTarget, putItemInput, opts)



&lt;p&gt;Creates a new item, or replaces an old item with a new item (including all the attributes).&lt;/p&gt; &lt;p&gt;If an item already exists in the specified table with the same primary key, the new item completely replaces the existing item. You can perform a conditional put (insert a new item if one with the specified primary key doesn&#39;t exist), or replace an existing item if it has certain attribute values.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putItemInput = new AmazonDynamoDb.PutItemInput(); // PutItemInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putItem(xAmzTarget, putItemInput, opts, (error, data, response) => {
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
 **putItemInput** | [**PutItemInput**](PutItemInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutItemOutput**](PutItemOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## query

> QueryOutput query(xAmzTarget, queryInput, opts)



&lt;p&gt;Gets the values of one or more items and its attributes by primary key (composite primary key, only).&lt;/p&gt; &lt;p&gt;Narrow the scope of the query using comparison operators on the &lt;code&gt;RangeKeyValue&lt;/code&gt; of the composite key. Use the &lt;code&gt;ScanIndexForward&lt;/code&gt; parameter to get results in forward or reverse order by range key.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let queryInput = new AmazonDynamoDb.QueryInput(); // QueryInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': "limit_example", // String | Pagination limit
  'exclusiveStartKey': "exclusiveStartKey_example" // String | Pagination token
};
apiInstance.query(xAmzTarget, queryInput, opts, (error, data, response) => {
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
 **queryInput** | [**QueryInput**](QueryInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **String**| Pagination limit | [optional] 
 **exclusiveStartKey** | **String**| Pagination token | [optional] 

### Return type

[**QueryOutput**](QueryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## scan

> ScanOutput scan(xAmzTarget, scanInput, opts)



&lt;p&gt;Retrieves one or more items and its attributes by performing a full scan of a table.&lt;/p&gt; &lt;p&gt;Provide a &lt;code&gt;ScanFilter&lt;/code&gt; to get more specific results.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let scanInput = new AmazonDynamoDb.ScanInput(); // ScanInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': "limit_example", // String | Pagination limit
  'exclusiveStartKey': "exclusiveStartKey_example" // String | Pagination token
};
apiInstance.scan(xAmzTarget, scanInput, opts, (error, data, response) => {
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
 **scanInput** | [**ScanInput**](ScanInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **String**| Pagination limit | [optional] 
 **exclusiveStartKey** | **String**| Pagination token | [optional] 

### Return type

[**ScanOutput**](ScanOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateItem

> UpdateItemOutput updateItem(xAmzTarget, updateItemInput, opts)



&lt;p&gt;Edits an existing item&#39;s attributes.&lt;/p&gt; &lt;p&gt;You can perform a conditional update (insert a new attribute name-value pair if it doesn&#39;t exist, or replace an existing name-value pair if it has certain expected attribute values).&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateItemInput = new AmazonDynamoDb.UpdateItemInput(); // UpdateItemInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateItem(xAmzTarget, updateItemInput, opts, (error, data, response) => {
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
 **updateItemInput** | [**UpdateItemInput**](UpdateItemInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateItemOutput**](UpdateItemOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTable

> UpdateTableOutput updateTable(xAmzTarget, updateTableInput, opts)



&lt;p&gt;Updates the provisioned throughput for the given table.&lt;/p&gt; &lt;p&gt;Setting the throughput for a table helps you manage performance and is part of the Provisioned Throughput feature of Amazon DynamoDB.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDb from 'amazon_dynamo_db';
let defaultClient = AmazonDynamoDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDb.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateTableInput = new AmazonDynamoDb.UpdateTableInput(); // UpdateTableInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTable(xAmzTarget, updateTableInput, opts, (error, data, response) => {
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
 **updateTableInput** | [**UpdateTableInput**](UpdateTableInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateTableOutput**](UpdateTableOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

