# AwsLakeFormation.DefaultApi

All URIs are relative to *http://lakeformation.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLFTagsToResource**](DefaultApi.md#addLFTagsToResource) | **POST** /AddLFTagsToResource | 
[**assumeDecoratedRoleWithSAML**](DefaultApi.md#assumeDecoratedRoleWithSAML) | **POST** /AssumeDecoratedRoleWithSAML | 
[**batchGrantPermissions**](DefaultApi.md#batchGrantPermissions) | **POST** /BatchGrantPermissions | 
[**batchRevokePermissions**](DefaultApi.md#batchRevokePermissions) | **POST** /BatchRevokePermissions | 
[**cancelTransaction**](DefaultApi.md#cancelTransaction) | **POST** /CancelTransaction | 
[**commitTransaction**](DefaultApi.md#commitTransaction) | **POST** /CommitTransaction | 
[**createDataCellsFilter**](DefaultApi.md#createDataCellsFilter) | **POST** /CreateDataCellsFilter | 
[**createLFTag**](DefaultApi.md#createLFTag) | **POST** /CreateLFTag | 
[**deleteDataCellsFilter**](DefaultApi.md#deleteDataCellsFilter) | **POST** /DeleteDataCellsFilter | 
[**deleteLFTag**](DefaultApi.md#deleteLFTag) | **POST** /DeleteLFTag | 
[**deleteObjectsOnCancel**](DefaultApi.md#deleteObjectsOnCancel) | **POST** /DeleteObjectsOnCancel | 
[**deregisterResource**](DefaultApi.md#deregisterResource) | **POST** /DeregisterResource | 
[**describeResource**](DefaultApi.md#describeResource) | **POST** /DescribeResource | 
[**describeTransaction**](DefaultApi.md#describeTransaction) | **POST** /DescribeTransaction | 
[**extendTransaction**](DefaultApi.md#extendTransaction) | **POST** /ExtendTransaction | 
[**getDataCellsFilter**](DefaultApi.md#getDataCellsFilter) | **POST** /GetDataCellsFilter | 
[**getDataLakeSettings**](DefaultApi.md#getDataLakeSettings) | **POST** /GetDataLakeSettings | 
[**getEffectivePermissionsForPath**](DefaultApi.md#getEffectivePermissionsForPath) | **POST** /GetEffectivePermissionsForPath | 
[**getLFTag**](DefaultApi.md#getLFTag) | **POST** /GetLFTag | 
[**getQueryState**](DefaultApi.md#getQueryState) | **POST** /GetQueryState | 
[**getQueryStatistics**](DefaultApi.md#getQueryStatistics) | **POST** /GetQueryStatistics | 
[**getResourceLFTags**](DefaultApi.md#getResourceLFTags) | **POST** /GetResourceLFTags | 
[**getTableObjects**](DefaultApi.md#getTableObjects) | **POST** /GetTableObjects | 
[**getTemporaryGluePartitionCredentials**](DefaultApi.md#getTemporaryGluePartitionCredentials) | **POST** /GetTemporaryGluePartitionCredentials | 
[**getTemporaryGlueTableCredentials**](DefaultApi.md#getTemporaryGlueTableCredentials) | **POST** /GetTemporaryGlueTableCredentials | 
[**getWorkUnitResults**](DefaultApi.md#getWorkUnitResults) | **POST** /GetWorkUnitResults | 
[**getWorkUnits**](DefaultApi.md#getWorkUnits) | **POST** /GetWorkUnits | 
[**grantPermissions**](DefaultApi.md#grantPermissions) | **POST** /GrantPermissions | 
[**listDataCellsFilter**](DefaultApi.md#listDataCellsFilter) | **POST** /ListDataCellsFilter | 
[**listLFTags**](DefaultApi.md#listLFTags) | **POST** /ListLFTags | 
[**listPermissions**](DefaultApi.md#listPermissions) | **POST** /ListPermissions | 
[**listResources**](DefaultApi.md#listResources) | **POST** /ListResources | 
[**listTableStorageOptimizers**](DefaultApi.md#listTableStorageOptimizers) | **POST** /ListTableStorageOptimizers | 
[**listTransactions**](DefaultApi.md#listTransactions) | **POST** /ListTransactions | 
[**putDataLakeSettings**](DefaultApi.md#putDataLakeSettings) | **POST** /PutDataLakeSettings | 
[**registerResource**](DefaultApi.md#registerResource) | **POST** /RegisterResource | 
[**removeLFTagsFromResource**](DefaultApi.md#removeLFTagsFromResource) | **POST** /RemoveLFTagsFromResource | 
[**revokePermissions**](DefaultApi.md#revokePermissions) | **POST** /RevokePermissions | 
[**searchDatabasesByLFTags**](DefaultApi.md#searchDatabasesByLFTags) | **POST** /SearchDatabasesByLFTags | 
[**searchTablesByLFTags**](DefaultApi.md#searchTablesByLFTags) | **POST** /SearchTablesByLFTags | 
[**startQueryPlanning**](DefaultApi.md#startQueryPlanning) | **POST** /StartQueryPlanning | 
[**startTransaction**](DefaultApi.md#startTransaction) | **POST** /StartTransaction | 
[**updateDataCellsFilter**](DefaultApi.md#updateDataCellsFilter) | **POST** /UpdateDataCellsFilter | 
[**updateLFTag**](DefaultApi.md#updateLFTag) | **POST** /UpdateLFTag | 
[**updateResource**](DefaultApi.md#updateResource) | **POST** /UpdateResource | 
[**updateTableObjects**](DefaultApi.md#updateTableObjects) | **POST** /UpdateTableObjects | 
[**updateTableStorageOptimizer**](DefaultApi.md#updateTableStorageOptimizer) | **POST** /UpdateTableStorageOptimizer | 



## addLFTagsToResource

> AddLFTagsToResourceResponse addLFTagsToResource(addLFTagsToResourceRequest, opts)



Attaches one or more LF-tags to an existing resource.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let addLFTagsToResourceRequest = new AwsLakeFormation.AddLFTagsToResourceRequest(); // AddLFTagsToResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addLFTagsToResource(addLFTagsToResourceRequest, opts, (error, data, response) => {
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
 **addLFTagsToResourceRequest** | [**AddLFTagsToResourceRequest**](AddLFTagsToResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddLFTagsToResourceResponse**](AddLFTagsToResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assumeDecoratedRoleWithSAML

> AssumeDecoratedRoleWithSAMLResponse assumeDecoratedRoleWithSAML(assumeDecoratedRoleWithSAMLRequest, opts)



&lt;p&gt;Allows a caller to assume an IAM role decorated as the SAML user specified in the SAML assertion included in the request. This decoration allows Lake Formation to enforce access policies against the SAML users and groups. This API operation requires SAML federation setup in the caller’s account as it can only be called with valid SAML assertions. Lake Formation does not scope down the permission of the assumed role. All permissions attached to the role via the SAML federation setup will be included in the role session. &lt;/p&gt; &lt;p&gt; This decorated role is expected to access data in Amazon S3 by getting temporary access from Lake Formation which is authorized via the virtual API &lt;code&gt;GetDataAccess&lt;/code&gt;. Therefore, all SAML roles that can be assumed via &lt;code&gt;AssumeDecoratedRoleWithSAML&lt;/code&gt; must at a minimum include &lt;code&gt;lakeformation:GetDataAccess&lt;/code&gt; in their role policies. A typical IAM policy attached to such a role would look as follows: &lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let assumeDecoratedRoleWithSAMLRequest = new AwsLakeFormation.AssumeDecoratedRoleWithSAMLRequest(); // AssumeDecoratedRoleWithSAMLRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.assumeDecoratedRoleWithSAML(assumeDecoratedRoleWithSAMLRequest, opts, (error, data, response) => {
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
 **assumeDecoratedRoleWithSAMLRequest** | [**AssumeDecoratedRoleWithSAMLRequest**](AssumeDecoratedRoleWithSAMLRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssumeDecoratedRoleWithSAMLResponse**](AssumeDecoratedRoleWithSAMLResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGrantPermissions

> BatchGrantPermissionsResponse batchGrantPermissions(batchGrantPermissionsRequest, opts)



Batch operation to grant permissions to the principal.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let batchGrantPermissionsRequest = new AwsLakeFormation.BatchGrantPermissionsRequest(); // BatchGrantPermissionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGrantPermissions(batchGrantPermissionsRequest, opts, (error, data, response) => {
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
 **batchGrantPermissionsRequest** | [**BatchGrantPermissionsRequest**](BatchGrantPermissionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGrantPermissionsResponse**](BatchGrantPermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchRevokePermissions

> BatchRevokePermissionsResponse batchRevokePermissions(batchRevokePermissionsRequest, opts)



Batch operation to revoke permissions from the principal.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let batchRevokePermissionsRequest = new AwsLakeFormation.BatchRevokePermissionsRequest(); // BatchRevokePermissionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchRevokePermissions(batchRevokePermissionsRequest, opts, (error, data, response) => {
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
 **batchRevokePermissionsRequest** | [**BatchRevokePermissionsRequest**](BatchRevokePermissionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchRevokePermissionsResponse**](BatchRevokePermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelTransaction

> Object cancelTransaction(cancelTransactionRequest, opts)



Attempts to cancel the specified transaction. Returns an exception if the transaction was previously committed.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let cancelTransactionRequest = new AwsLakeFormation.CancelTransactionRequest(); // CancelTransactionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelTransaction(cancelTransactionRequest, opts, (error, data, response) => {
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
 **cancelTransactionRequest** | [**CancelTransactionRequest**](CancelTransactionRequest.md)|  | 
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


## commitTransaction

> CommitTransactionResponse commitTransaction(commitTransactionRequest, opts)



Attempts to commit the specified transaction. Returns an exception if the transaction was previously aborted. This API action is idempotent if called multiple times for the same transaction.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let commitTransactionRequest = new AwsLakeFormation.CommitTransactionRequest(); // CommitTransactionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.commitTransaction(commitTransactionRequest, opts, (error, data, response) => {
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
 **commitTransactionRequest** | [**CommitTransactionRequest**](CommitTransactionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CommitTransactionResponse**](CommitTransactionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDataCellsFilter

> Object createDataCellsFilter(createDataCellsFilterRequest, opts)



Creates a data cell filter to allow one to grant access to certain columns on certain rows.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let createDataCellsFilterRequest = new AwsLakeFormation.CreateDataCellsFilterRequest(); // CreateDataCellsFilterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDataCellsFilter(createDataCellsFilterRequest, opts, (error, data, response) => {
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
 **createDataCellsFilterRequest** | [**CreateDataCellsFilterRequest**](CreateDataCellsFilterRequest.md)|  | 
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


## createLFTag

> Object createLFTag(createLFTagRequest, opts)



Creates an LF-tag with the specified name and values.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let createLFTagRequest = new AwsLakeFormation.CreateLFTagRequest(); // CreateLFTagRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLFTag(createLFTagRequest, opts, (error, data, response) => {
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
 **createLFTagRequest** | [**CreateLFTagRequest**](CreateLFTagRequest.md)|  | 
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


## deleteDataCellsFilter

> Object deleteDataCellsFilter(deleteDataCellsFilterRequest, opts)



Deletes a data cell filter.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let deleteDataCellsFilterRequest = new AwsLakeFormation.DeleteDataCellsFilterRequest(); // DeleteDataCellsFilterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDataCellsFilter(deleteDataCellsFilterRequest, opts, (error, data, response) => {
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
 **deleteDataCellsFilterRequest** | [**DeleteDataCellsFilterRequest**](DeleteDataCellsFilterRequest.md)|  | 
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


## deleteLFTag

> Object deleteLFTag(deleteLFTagRequest, opts)



Deletes the specified LF-tag given a key name. If the input parameter tag key was not found, then the operation will throw an exception. When you delete an LF-tag, the &lt;code&gt;LFTagPolicy&lt;/code&gt; attached to the LF-tag becomes invalid. If the deleted LF-tag was still assigned to any resource, the tag policy attach to the deleted LF-tag will no longer be applied to the resource.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let deleteLFTagRequest = new AwsLakeFormation.DeleteLFTagRequest(); // DeleteLFTagRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLFTag(deleteLFTagRequest, opts, (error, data, response) => {
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
 **deleteLFTagRequest** | [**DeleteLFTagRequest**](DeleteLFTagRequest.md)|  | 
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


## deleteObjectsOnCancel

> Object deleteObjectsOnCancel(deleteObjectsOnCancelRequest, opts)



&lt;p&gt;For a specific governed table, provides a list of Amazon S3 objects that will be written during the current transaction and that can be automatically deleted if the transaction is canceled. Without this call, no Amazon S3 objects are automatically deleted when a transaction cancels. &lt;/p&gt; &lt;p&gt; The Glue ETL library function &lt;code&gt;write_dynamic_frame.from_catalog()&lt;/code&gt; includes an option to automatically call &lt;code&gt;DeleteObjectsOnCancel&lt;/code&gt; before writes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/transactions-data-operations.html#rolling-back-writes\&quot;&gt;Rolling Back Amazon S3 Writes&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let deleteObjectsOnCancelRequest = new AwsLakeFormation.DeleteObjectsOnCancelRequest(); // DeleteObjectsOnCancelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteObjectsOnCancel(deleteObjectsOnCancelRequest, opts, (error, data, response) => {
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
 **deleteObjectsOnCancelRequest** | [**DeleteObjectsOnCancelRequest**](DeleteObjectsOnCancelRequest.md)|  | 
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


## deregisterResource

> Object deregisterResource(deregisterResourceRequest, opts)



&lt;p&gt;Deregisters the resource as managed by the Data Catalog.&lt;/p&gt; &lt;p&gt;When you deregister a path, Lake Formation removes the path from the inline policy attached to your service-linked role.&lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let deregisterResourceRequest = new AwsLakeFormation.DeregisterResourceRequest(); // DeregisterResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deregisterResource(deregisterResourceRequest, opts, (error, data, response) => {
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
 **deregisterResourceRequest** | [**DeregisterResourceRequest**](DeregisterResourceRequest.md)|  | 
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


## describeResource

> DescribeResourceResponse describeResource(describeResourceRequest, opts)



Retrieves the current data access role for the given resource registered in Lake Formation.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let describeResourceRequest = new AwsLakeFormation.DescribeResourceRequest(); // DescribeResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeResource(describeResourceRequest, opts, (error, data, response) => {
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
 **describeResourceRequest** | [**DescribeResourceRequest**](DescribeResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeResourceResponse**](DescribeResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeTransaction

> DescribeTransactionResponse describeTransaction(describeTransactionRequest, opts)



Returns the details of a single transaction.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let describeTransactionRequest = new AwsLakeFormation.DescribeTransactionRequest(); // DescribeTransactionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTransaction(describeTransactionRequest, opts, (error, data, response) => {
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
 **describeTransactionRequest** | [**DescribeTransactionRequest**](DescribeTransactionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTransactionResponse**](DescribeTransactionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extendTransaction

> Object extendTransaction(extendTransactionRequest, opts)



&lt;p&gt;Indicates to the service that the specified transaction is still active and should not be treated as idle and aborted.&lt;/p&gt; &lt;p&gt;Write transactions that remain idle for a long period are automatically aborted unless explicitly extended.&lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let extendTransactionRequest = new AwsLakeFormation.ExtendTransactionRequest(); // ExtendTransactionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.extendTransaction(extendTransactionRequest, opts, (error, data, response) => {
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
 **extendTransactionRequest** | [**ExtendTransactionRequest**](ExtendTransactionRequest.md)|  | 
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


## getDataCellsFilter

> GetDataCellsFilterResponse getDataCellsFilter(getDataCellsFilterRequest, opts)



Returns a data cells filter.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getDataCellsFilterRequest = new AwsLakeFormation.GetDataCellsFilterRequest(); // GetDataCellsFilterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDataCellsFilter(getDataCellsFilterRequest, opts, (error, data, response) => {
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
 **getDataCellsFilterRequest** | [**GetDataCellsFilterRequest**](GetDataCellsFilterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDataCellsFilterResponse**](GetDataCellsFilterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDataLakeSettings

> GetDataLakeSettingsResponse getDataLakeSettings(getDataLakeSettingsRequest, opts)



Retrieves the list of the data lake administrators of a Lake Formation-managed data lake. 

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getDataLakeSettingsRequest = new AwsLakeFormation.GetDataLakeSettingsRequest(); // GetDataLakeSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDataLakeSettings(getDataLakeSettingsRequest, opts, (error, data, response) => {
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
 **getDataLakeSettingsRequest** | [**GetDataLakeSettingsRequest**](GetDataLakeSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDataLakeSettingsResponse**](GetDataLakeSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getEffectivePermissionsForPath

> GetEffectivePermissionsForPathResponse getEffectivePermissionsForPath(getEffectivePermissionsForPathRequest, opts)



Returns the Lake Formation permissions for a specified table or database resource located at a path in Amazon S3. &lt;code&gt;GetEffectivePermissionsForPath&lt;/code&gt; will not return databases and tables if the catalog is encrypted.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getEffectivePermissionsForPathRequest = new AwsLakeFormation.GetEffectivePermissionsForPathRequest(); // GetEffectivePermissionsForPathRequest | 
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
apiInstance.getEffectivePermissionsForPath(getEffectivePermissionsForPathRequest, opts, (error, data, response) => {
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
 **getEffectivePermissionsForPathRequest** | [**GetEffectivePermissionsForPathRequest**](GetEffectivePermissionsForPathRequest.md)|  | 
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

[**GetEffectivePermissionsForPathResponse**](GetEffectivePermissionsForPathResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLFTag

> GetLFTagResponse getLFTag(getLFTagRequest, opts)



Returns an LF-tag definition.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getLFTagRequest = new AwsLakeFormation.GetLFTagRequest(); // GetLFTagRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLFTag(getLFTagRequest, opts, (error, data, response) => {
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
 **getLFTagRequest** | [**GetLFTagRequest**](GetLFTagRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLFTagResponse**](GetLFTagResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getQueryState

> GetQueryStateResponse getQueryState(getQueryStateRequest, opts)



Returns the state of a query previously submitted. Clients are expected to poll &lt;code&gt;GetQueryState&lt;/code&gt; to monitor the current state of the planning before retrieving the work units. A query state is only visible to the principal that made the initial call to &lt;code&gt;StartQueryPlanning&lt;/code&gt;.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getQueryStateRequest = new AwsLakeFormation.GetQueryStateRequest(); // GetQueryStateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getQueryState(getQueryStateRequest, opts, (error, data, response) => {
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
 **getQueryStateRequest** | [**GetQueryStateRequest**](GetQueryStateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetQueryStateResponse**](GetQueryStateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getQueryStatistics

> GetQueryStatisticsResponse getQueryStatistics(getQueryStateRequest, opts)



Retrieves statistics on the planning and execution of a query.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getQueryStateRequest = new AwsLakeFormation.GetQueryStateRequest(); // GetQueryStateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getQueryStatistics(getQueryStateRequest, opts, (error, data, response) => {
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
 **getQueryStateRequest** | [**GetQueryStateRequest**](GetQueryStateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetQueryStatisticsResponse**](GetQueryStatisticsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getResourceLFTags

> GetResourceLFTagsResponse getResourceLFTags(getResourceLFTagsRequest, opts)



Returns the LF-tags applied to a resource.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getResourceLFTagsRequest = new AwsLakeFormation.GetResourceLFTagsRequest(); // GetResourceLFTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getResourceLFTags(getResourceLFTagsRequest, opts, (error, data, response) => {
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
 **getResourceLFTagsRequest** | [**GetResourceLFTagsRequest**](GetResourceLFTagsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetResourceLFTagsResponse**](GetResourceLFTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTableObjects

> GetTableObjectsResponse getTableObjects(getTableObjectsRequest, opts)



Returns the set of Amazon S3 objects that make up the specified governed table. A transaction ID or timestamp can be specified for time-travel queries.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getTableObjectsRequest = new AwsLakeFormation.GetTableObjectsRequest(); // GetTableObjectsRequest | 
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
apiInstance.getTableObjects(getTableObjectsRequest, opts, (error, data, response) => {
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
 **getTableObjectsRequest** | [**GetTableObjectsRequest**](GetTableObjectsRequest.md)|  | 
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

[**GetTableObjectsResponse**](GetTableObjectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTemporaryGluePartitionCredentials

> GetTemporaryGluePartitionCredentialsResponse getTemporaryGluePartitionCredentials(getTemporaryGluePartitionCredentialsRequest, opts)



This API is identical to &lt;code&gt;GetTemporaryTableCredentials&lt;/code&gt; except that this is used when the target Data Catalog resource is of type Partition. Lake Formation restricts the permission of the vended credentials with the same scope down policy which restricts access to a single Amazon S3 prefix.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getTemporaryGluePartitionCredentialsRequest = new AwsLakeFormation.GetTemporaryGluePartitionCredentialsRequest(); // GetTemporaryGluePartitionCredentialsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTemporaryGluePartitionCredentials(getTemporaryGluePartitionCredentialsRequest, opts, (error, data, response) => {
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
 **getTemporaryGluePartitionCredentialsRequest** | [**GetTemporaryGluePartitionCredentialsRequest**](GetTemporaryGluePartitionCredentialsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTemporaryGluePartitionCredentialsResponse**](GetTemporaryGluePartitionCredentialsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTemporaryGlueTableCredentials

> GetTemporaryGlueTableCredentialsResponse getTemporaryGlueTableCredentials(getTemporaryGlueTableCredentialsRequest, opts)



Allows a caller in a secure environment to assume a role with permission to access Amazon S3. In order to vend such credentials, Lake Formation assumes the role associated with a registered location, for example an Amazon S3 bucket, with a scope down policy which restricts the access to a single prefix.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getTemporaryGlueTableCredentialsRequest = new AwsLakeFormation.GetTemporaryGlueTableCredentialsRequest(); // GetTemporaryGlueTableCredentialsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTemporaryGlueTableCredentials(getTemporaryGlueTableCredentialsRequest, opts, (error, data, response) => {
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
 **getTemporaryGlueTableCredentialsRequest** | [**GetTemporaryGlueTableCredentialsRequest**](GetTemporaryGlueTableCredentialsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTemporaryGlueTableCredentialsResponse**](GetTemporaryGlueTableCredentialsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getWorkUnitResults

> GetWorkUnitResultsResponse getWorkUnitResults(getWorkUnitResultsRequest, opts)



Returns the work units resulting from the query. Work units can be executed in any order and in parallel. 

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getWorkUnitResultsRequest = new AwsLakeFormation.GetWorkUnitResultsRequest(); // GetWorkUnitResultsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWorkUnitResults(getWorkUnitResultsRequest, opts, (error, data, response) => {
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
 **getWorkUnitResultsRequest** | [**GetWorkUnitResultsRequest**](GetWorkUnitResultsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWorkUnitResultsResponse**](GetWorkUnitResultsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getWorkUnits

> GetWorkUnitsResponse getWorkUnits(getWorkUnitsRequest, opts)



Retrieves the work units generated by the &lt;code&gt;StartQueryPlanning&lt;/code&gt; operation.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let getWorkUnitsRequest = new AwsLakeFormation.GetWorkUnitsRequest(); // GetWorkUnitsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getWorkUnits(getWorkUnitsRequest, opts, (error, data, response) => {
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
 **getWorkUnitsRequest** | [**GetWorkUnitsRequest**](GetWorkUnitsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetWorkUnitsResponse**](GetWorkUnitsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## grantPermissions

> Object grantPermissions(grantPermissionsRequest, opts)



&lt;p&gt;Grants permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3.&lt;/p&gt; &lt;p&gt;For information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html\&quot;&gt;Security and Access Control to Metadata and Data&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let grantPermissionsRequest = new AwsLakeFormation.GrantPermissionsRequest(); // GrantPermissionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.grantPermissions(grantPermissionsRequest, opts, (error, data, response) => {
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
 **grantPermissionsRequest** | [**GrantPermissionsRequest**](GrantPermissionsRequest.md)|  | 
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


## listDataCellsFilter

> ListDataCellsFilterResponse listDataCellsFilter(listDataCellsFilterRequest, opts)



Lists all the data cell filters on a table.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let listDataCellsFilterRequest = new AwsLakeFormation.ListDataCellsFilterRequest(); // ListDataCellsFilterRequest | 
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
apiInstance.listDataCellsFilter(listDataCellsFilterRequest, opts, (error, data, response) => {
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
 **listDataCellsFilterRequest** | [**ListDataCellsFilterRequest**](ListDataCellsFilterRequest.md)|  | 
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

[**ListDataCellsFilterResponse**](ListDataCellsFilterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLFTags

> ListLFTagsResponse listLFTags(listLFTagsRequest, opts)



Lists LF-tags that the requester has permission to view. 

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let listLFTagsRequest = new AwsLakeFormation.ListLFTagsRequest(); // ListLFTagsRequest | 
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
apiInstance.listLFTags(listLFTagsRequest, opts, (error, data, response) => {
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
 **listLFTagsRequest** | [**ListLFTagsRequest**](ListLFTagsRequest.md)|  | 
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

[**ListLFTagsResponse**](ListLFTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPermissions

> ListPermissionsResponse listPermissions(listPermissionsRequest, opts)



&lt;p&gt;Returns a list of the principal permissions on the resource, filtered by the permissions of the caller. For example, if you are granted an ALTER permission, you are able to see only the principal permissions for ALTER.&lt;/p&gt; &lt;p&gt;This operation returns only those permissions that have been explicitly granted.&lt;/p&gt; &lt;p&gt;For information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html\&quot;&gt;Security and Access Control to Metadata and Data&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let listPermissionsRequest = new AwsLakeFormation.ListPermissionsRequest(); // ListPermissionsRequest | 
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
apiInstance.listPermissions(listPermissionsRequest, opts, (error, data, response) => {
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
 **listPermissionsRequest** | [**ListPermissionsRequest**](ListPermissionsRequest.md)|  | 
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

[**ListPermissionsResponse**](ListPermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listResources

> ListResourcesResponse listResources(listResourcesRequest, opts)



Lists the resources registered to be managed by the Data Catalog.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let listResourcesRequest = new AwsLakeFormation.ListResourcesRequest(); // ListResourcesRequest | 
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
apiInstance.listResources(listResourcesRequest, opts, (error, data, response) => {
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
 **listResourcesRequest** | [**ListResourcesRequest**](ListResourcesRequest.md)|  | 
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

[**ListResourcesResponse**](ListResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTableStorageOptimizers

> ListTableStorageOptimizersResponse listTableStorageOptimizers(listTableStorageOptimizersRequest, opts)



Returns the configuration of all storage optimizers associated with a specified table.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let listTableStorageOptimizersRequest = new AwsLakeFormation.ListTableStorageOptimizersRequest(); // ListTableStorageOptimizersRequest | 
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
apiInstance.listTableStorageOptimizers(listTableStorageOptimizersRequest, opts, (error, data, response) => {
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
 **listTableStorageOptimizersRequest** | [**ListTableStorageOptimizersRequest**](ListTableStorageOptimizersRequest.md)|  | 
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

[**ListTableStorageOptimizersResponse**](ListTableStorageOptimizersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTransactions

> ListTransactionsResponse listTransactions(listTransactionsRequest, opts)



&lt;p&gt;Returns metadata about transactions and their status. To prevent the response from growing indefinitely, only uncommitted transactions and those available for time-travel queries are returned.&lt;/p&gt; &lt;p&gt;This operation can help you identify uncommitted transactions or to get information about transactions.&lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let listTransactionsRequest = new AwsLakeFormation.ListTransactionsRequest(); // ListTransactionsRequest | 
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
apiInstance.listTransactions(listTransactionsRequest, opts, (error, data, response) => {
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
 **listTransactionsRequest** | [**ListTransactionsRequest**](ListTransactionsRequest.md)|  | 
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

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDataLakeSettings

> Object putDataLakeSettings(putDataLakeSettingsRequest, opts)



&lt;p&gt;Sets the list of data lake administrators who have admin privileges on all resources managed by Lake Formation. For more information on admin privileges, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html\&quot;&gt;Granting Lake Formation Permissions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This API replaces the current list of data lake admins with the new list being passed. To add an admin, fetch the current list and add the new admin to that list and pass that list in this API.&lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let putDataLakeSettingsRequest = new AwsLakeFormation.PutDataLakeSettingsRequest(); // PutDataLakeSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putDataLakeSettings(putDataLakeSettingsRequest, opts, (error, data, response) => {
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
 **putDataLakeSettingsRequest** | [**PutDataLakeSettingsRequest**](PutDataLakeSettingsRequest.md)|  | 
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


## registerResource

> Object registerResource(registerResourceRequest, opts)



&lt;p&gt;Registers the resource as managed by the Data Catalog.&lt;/p&gt; &lt;p&gt;To add or update data, Lake Formation needs read/write access to the chosen Amazon S3 path. Choose a role that you know has permission to do this, or choose the AWSServiceRoleForLakeFormationDataAccess service-linked role. When you register the first Amazon S3 path, the service-linked role and a new inline policy are created on your behalf. Lake Formation adds the first path to the inline policy and attaches it to the service-linked role. When you register subsequent paths, Lake Formation adds the path to the existing policy.&lt;/p&gt; &lt;p&gt;The following request registers a new location and gives Lake Formation permission to use the service-linked role to access that location.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ResourceArn &#x3D; arn:aws:s3:::my-bucket UseServiceLinkedRole &#x3D; true&lt;/code&gt; &lt;/p&gt; &lt;p&gt;If &lt;code&gt;UseServiceLinkedRole&lt;/code&gt; is not set to true, you must provide or set the &lt;code&gt;RoleArn&lt;/code&gt;:&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:aws:iam::12345:role/my-data-access-role&lt;/code&gt; &lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let registerResourceRequest = new AwsLakeFormation.RegisterResourceRequest(); // RegisterResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerResource(registerResourceRequest, opts, (error, data, response) => {
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
 **registerResourceRequest** | [**RegisterResourceRequest**](RegisterResourceRequest.md)|  | 
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


## removeLFTagsFromResource

> RemoveLFTagsFromResourceResponse removeLFTagsFromResource(removeLFTagsFromResourceRequest, opts)



Removes an LF-tag from the resource. Only database, table, or tableWithColumns resource are allowed. To tag columns, use the column inclusion list in &lt;code&gt;tableWithColumns&lt;/code&gt; to specify column input.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let removeLFTagsFromResourceRequest = new AwsLakeFormation.RemoveLFTagsFromResourceRequest(); // RemoveLFTagsFromResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeLFTagsFromResource(removeLFTagsFromResourceRequest, opts, (error, data, response) => {
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
 **removeLFTagsFromResourceRequest** | [**RemoveLFTagsFromResourceRequest**](RemoveLFTagsFromResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RemoveLFTagsFromResourceResponse**](RemoveLFTagsFromResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokePermissions

> Object revokePermissions(revokePermissionsRequest, opts)



Revokes permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let revokePermissionsRequest = new AwsLakeFormation.RevokePermissionsRequest(); // RevokePermissionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.revokePermissions(revokePermissionsRequest, opts, (error, data, response) => {
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
 **revokePermissionsRequest** | [**RevokePermissionsRequest**](RevokePermissionsRequest.md)|  | 
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


## searchDatabasesByLFTags

> SearchDatabasesByLFTagsResponse searchDatabasesByLFTags(searchDatabasesByLFTagsRequest, opts)



This operation allows a search on &lt;code&gt;DATABASE&lt;/code&gt; resources by &lt;code&gt;TagCondition&lt;/code&gt;. This operation is used by admins who want to grant user permissions on certain &lt;code&gt;TagConditions&lt;/code&gt;. Before making a grant, the admin can use &lt;code&gt;SearchDatabasesByTags&lt;/code&gt; to find all resources where the given &lt;code&gt;TagConditions&lt;/code&gt; are valid to verify whether the returned resources can be shared.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let searchDatabasesByLFTagsRequest = new AwsLakeFormation.SearchDatabasesByLFTagsRequest(); // SearchDatabasesByLFTagsRequest | 
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
apiInstance.searchDatabasesByLFTags(searchDatabasesByLFTagsRequest, opts, (error, data, response) => {
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
 **searchDatabasesByLFTagsRequest** | [**SearchDatabasesByLFTagsRequest**](SearchDatabasesByLFTagsRequest.md)|  | 
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

[**SearchDatabasesByLFTagsResponse**](SearchDatabasesByLFTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchTablesByLFTags

> SearchTablesByLFTagsResponse searchTablesByLFTags(searchTablesByLFTagsRequest, opts)



This operation allows a search on &lt;code&gt;TABLE&lt;/code&gt; resources by &lt;code&gt;LFTag&lt;/code&gt;s. This will be used by admins who want to grant user permissions on certain LF-tags. Before making a grant, the admin can use &lt;code&gt;SearchTablesByLFTags&lt;/code&gt; to find all resources where the given &lt;code&gt;LFTag&lt;/code&gt;s are valid to verify whether the returned resources can be shared.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let searchTablesByLFTagsRequest = new AwsLakeFormation.SearchTablesByLFTagsRequest(); // SearchTablesByLFTagsRequest | 
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
apiInstance.searchTablesByLFTags(searchTablesByLFTagsRequest, opts, (error, data, response) => {
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
 **searchTablesByLFTagsRequest** | [**SearchTablesByLFTagsRequest**](SearchTablesByLFTagsRequest.md)|  | 
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

[**SearchTablesByLFTagsResponse**](SearchTablesByLFTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startQueryPlanning

> StartQueryPlanningResponse startQueryPlanning(startQueryPlanningRequest, opts)



&lt;p&gt;Submits a request to process a query statement.&lt;/p&gt; &lt;p&gt;This operation generates work units that can be retrieved with the &lt;code&gt;GetWorkUnits&lt;/code&gt; operation as soon as the query state is WORKUNITS_AVAILABLE or FINISHED.&lt;/p&gt;

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let startQueryPlanningRequest = new AwsLakeFormation.StartQueryPlanningRequest(); // StartQueryPlanningRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startQueryPlanning(startQueryPlanningRequest, opts, (error, data, response) => {
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
 **startQueryPlanningRequest** | [**StartQueryPlanningRequest**](StartQueryPlanningRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartQueryPlanningResponse**](StartQueryPlanningResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startTransaction

> StartTransactionResponse startTransaction(startTransactionRequest, opts)



Starts a new transaction and returns its transaction ID. Transaction IDs are opaque objects that you can use to identify a transaction.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let startTransactionRequest = new AwsLakeFormation.StartTransactionRequest(); // StartTransactionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startTransaction(startTransactionRequest, opts, (error, data, response) => {
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
 **startTransactionRequest** | [**StartTransactionRequest**](StartTransactionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartTransactionResponse**](StartTransactionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDataCellsFilter

> Object updateDataCellsFilter(createDataCellsFilterRequest, opts)



Updates a data cell filter.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let createDataCellsFilterRequest = new AwsLakeFormation.CreateDataCellsFilterRequest(); // CreateDataCellsFilterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDataCellsFilter(createDataCellsFilterRequest, opts, (error, data, response) => {
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
 **createDataCellsFilterRequest** | [**CreateDataCellsFilterRequest**](CreateDataCellsFilterRequest.md)|  | 
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


## updateLFTag

> Object updateLFTag(updateLFTagRequest, opts)



Updates the list of possible values for the specified LF-tag key. If the LF-tag does not exist, the operation throws an EntityNotFoundException. The values in the delete key values will be deleted from list of possible values. If any value in the delete key values is attached to a resource, then API errors out with a 400 Exception - \&quot;Update not allowed\&quot;. Untag the attribute before deleting the LF-tag key&#39;s value. 

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let updateLFTagRequest = new AwsLakeFormation.UpdateLFTagRequest(); // UpdateLFTagRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLFTag(updateLFTagRequest, opts, (error, data, response) => {
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
 **updateLFTagRequest** | [**UpdateLFTagRequest**](UpdateLFTagRequest.md)|  | 
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


## updateResource

> Object updateResource(updateResourceRequest, opts)



Updates the data access role used for vending access to the given (registered) resource in Lake Formation. 

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let updateResourceRequest = new AwsLakeFormation.UpdateResourceRequest(); // UpdateResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateResource(updateResourceRequest, opts, (error, data, response) => {
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
 **updateResourceRequest** | [**UpdateResourceRequest**](UpdateResourceRequest.md)|  | 
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


## updateTableObjects

> Object updateTableObjects(updateTableObjectsRequest, opts)



Updates the manifest of Amazon S3 objects that make up the specified governed table.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let updateTableObjectsRequest = new AwsLakeFormation.UpdateTableObjectsRequest(); // UpdateTableObjectsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTableObjects(updateTableObjectsRequest, opts, (error, data, response) => {
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
 **updateTableObjectsRequest** | [**UpdateTableObjectsRequest**](UpdateTableObjectsRequest.md)|  | 
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


## updateTableStorageOptimizer

> UpdateTableStorageOptimizerResponse updateTableStorageOptimizer(updateTableStorageOptimizerRequest, opts)



Updates the configuration of the storage optimizers for a table.

### Example

```javascript
import AwsLakeFormation from 'aws_lake_formation';
let defaultClient = AwsLakeFormation.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLakeFormation.DefaultApi();
let updateTableStorageOptimizerRequest = new AwsLakeFormation.UpdateTableStorageOptimizerRequest(); // UpdateTableStorageOptimizerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTableStorageOptimizer(updateTableStorageOptimizerRequest, opts, (error, data, response) => {
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
 **updateTableStorageOptimizerRequest** | [**UpdateTableStorageOptimizerRequest**](UpdateTableStorageOptimizerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateTableStorageOptimizerResponse**](UpdateTableStorageOptimizerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

