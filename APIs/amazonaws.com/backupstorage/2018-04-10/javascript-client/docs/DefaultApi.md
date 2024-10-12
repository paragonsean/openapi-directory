# AwsBackupStorage.DefaultApi

All URIs are relative to *http://backupstorage.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteObject**](DefaultApi.md#deleteObject) | **DELETE** /backup-jobs/{jobId}/object/{objectName} | 
[**getChunk**](DefaultApi.md#getChunk) | **GET** /restore-jobs/{jobId}/chunk/{chunkToken} | 
[**getObjectMetadata**](DefaultApi.md#getObjectMetadata) | **GET** /restore-jobs/{jobId}/object/{objectToken}/metadata | 
[**listChunks**](DefaultApi.md#listChunks) | **GET** /restore-jobs/{jobId}/chunks/{objectToken}/list | 
[**listObjects**](DefaultApi.md#listObjects) | **GET** /restore-jobs/{jobId}/objects/list | 
[**notifyObjectComplete**](DefaultApi.md#notifyObjectComplete) | **PUT** /backup-jobs/{jobId}/object/{uploadId}/complete#checksum&amp;checksum-algorithm | 
[**putChunk**](DefaultApi.md#putChunk) | **PUT** /backup-jobs/{jobId}/chunk/{uploadId}/{chunkIndex}#length&amp;checksum&amp;checksum-algorithm | 
[**putObject**](DefaultApi.md#putObject) | **PUT** /backup-jobs/{jobId}/object/{objectName}/put-object | 
[**startObject**](DefaultApi.md#startObject) | **PUT** /backup-jobs/{jobId}/object/{objectName} | 



## deleteObject

> deleteObject(jobId, objectName, opts)



Delete Object from the incremental base Backup.

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Backup job Id for the in-progress backup.
let objectName = "objectName_example"; // String | The name of the Object.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteObject(jobId, objectName, opts, (error, data, response) => {
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
 **jobId** | **String**| Backup job Id for the in-progress backup. | 
 **objectName** | **String**| The name of the Object. | 
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


## getChunk

> GetChunkOutput getChunk(jobId, chunkToken, opts)



Gets the specified object&#39;s chunk.

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Storage job id
let chunkToken = "chunkToken_example"; // String | Chunk token
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getChunk(jobId, chunkToken, opts, (error, data, response) => {
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
 **jobId** | **String**| Storage job id | 
 **chunkToken** | **String**| Chunk token | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetChunkOutput**](GetChunkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjectMetadata

> GetObjectMetadataOutput getObjectMetadata(jobId, objectToken, opts)



Get metadata associated with an Object.

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Backup job id for the in-progress backup.
let objectToken = "objectToken_example"; // String | Object token.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getObjectMetadata(jobId, objectToken, opts, (error, data, response) => {
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
 **jobId** | **String**| Backup job id for the in-progress backup. | 
 **objectToken** | **String**| Object token. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetObjectMetadataOutput**](GetObjectMetadataOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChunks

> ListChunksOutput listChunks(jobId, objectToken, opts)



List chunks in a given Object

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Storage job id
let objectToken = "objectToken_example"; // String | Object token
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Maximum number of chunks
  'nextToken': "nextToken_example", // String | Pagination token
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChunks(jobId, objectToken, opts, (error, data, response) => {
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
 **jobId** | **String**| Storage job id | 
 **objectToken** | **String**| Object token | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| Maximum number of chunks | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChunksOutput**](ListChunksOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listObjects

> ListObjectsOutput listObjects(jobId, opts)



List all Objects in a given Backup.

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Storage job id
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'startingObjectName': "startingObjectName_example", // String | Optional, specifies the starting Object name to list from. Ignored if NextToken is not NULL
  'startingObjectPrefix': "startingObjectPrefix_example", // String | Optional, specifies the starting Object prefix to list from. Ignored if NextToken is not NULL
  'maxResults': 56, // Number | Maximum objects count
  'nextToken': "nextToken_example", // String | Pagination token
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | (Optional) Created before filter
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | (Optional) Created after filter
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listObjects(jobId, opts, (error, data, response) => {
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
 **jobId** | **String**| Storage job id | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **startingObjectName** | **String**| Optional, specifies the starting Object name to list from. Ignored if NextToken is not NULL | [optional] 
 **startingObjectPrefix** | **String**| Optional, specifies the starting Object prefix to list from. Ignored if NextToken is not NULL | [optional] 
 **maxResults** | **Number**| Maximum objects count | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 
 **createdBefore** | **Date**| (Optional) Created before filter | [optional] 
 **createdAfter** | **Date**| (Optional) Created after filter | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListObjectsOutput**](ListObjectsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## notifyObjectComplete

> NotifyObjectCompleteOutput notifyObjectComplete(jobId, uploadId, checksum, checksumAlgorithm, notifyObjectCompleteRequest, opts)



Complete upload

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Backup job Id for the in-progress backup
let uploadId = "uploadId_example"; // String | Upload Id for the in-progress upload
let checksum = "checksum_example"; // String | Object checksum
let checksumAlgorithm = "checksumAlgorithm_example"; // String | Checksum algorithm
let notifyObjectCompleteRequest = new AwsBackupStorage.NotifyObjectCompleteRequest(); // NotifyObjectCompleteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'metadataString': "metadataString_example", // String | Optional metadata associated with an Object. Maximum string length is 256 bytes.
  'metadataBlobLength': 56, // Number | The size of MetadataBlob.
  'metadataChecksum': "metadataChecksum_example", // String | Checksum of MetadataBlob.
  'metadataChecksumAlgorithm': "metadataChecksumAlgorithm_example" // String | Checksum algorithm.
};
apiInstance.notifyObjectComplete(jobId, uploadId, checksum, checksumAlgorithm, notifyObjectCompleteRequest, opts, (error, data, response) => {
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
 **jobId** | **String**| Backup job Id for the in-progress backup | 
 **uploadId** | **String**| Upload Id for the in-progress upload | 
 **checksum** | **String**| Object checksum | 
 **checksumAlgorithm** | **String**| Checksum algorithm | 
 **notifyObjectCompleteRequest** | [**NotifyObjectCompleteRequest**](NotifyObjectCompleteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **metadataString** | **String**| Optional metadata associated with an Object. Maximum string length is 256 bytes. | [optional] 
 **metadataBlobLength** | **Number**| The size of MetadataBlob. | [optional] 
 **metadataChecksum** | **String**| Checksum of MetadataBlob. | [optional] 
 **metadataChecksumAlgorithm** | **String**| Checksum algorithm. | [optional] 

### Return type

[**NotifyObjectCompleteOutput**](NotifyObjectCompleteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putChunk

> PutChunkOutput putChunk(jobId, uploadId, chunkIndex, length, checksum, checksumAlgorithm, putChunkRequest, opts)



Upload chunk.

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Backup job Id for the in-progress backup.
let uploadId = "uploadId_example"; // String | Upload Id for the in-progress upload.
let chunkIndex = 56; // Number | Describes this chunk's position relative to the other chunks
let length = 56; // Number | Data length
let checksum = "checksum_example"; // String | Data checksum
let checksumAlgorithm = "checksumAlgorithm_example"; // String | Checksum algorithm
let putChunkRequest = new AwsBackupStorage.PutChunkRequest(); // PutChunkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putChunk(jobId, uploadId, chunkIndex, length, checksum, checksumAlgorithm, putChunkRequest, opts, (error, data, response) => {
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
 **jobId** | **String**| Backup job Id for the in-progress backup. | 
 **uploadId** | **String**| Upload Id for the in-progress upload. | 
 **chunkIndex** | **Number**| Describes this chunk&#39;s position relative to the other chunks | 
 **length** | **Number**| Data length | 
 **checksum** | **String**| Data checksum | 
 **checksumAlgorithm** | **String**| Checksum algorithm | 
 **putChunkRequest** | [**PutChunkRequest**](PutChunkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutChunkOutput**](PutChunkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putObject

> PutObjectOutput putObject(jobId, objectName, putObjectRequest, opts)



Upload object that can store object metadata String and data blob in single API call using inline chunk field.

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Backup job Id for the in-progress backup.
let objectName = "objectName_example"; // String | The name of the Object to be uploaded.
let putObjectRequest = new AwsBackupStorage.PutObjectRequest(); // PutObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'metadataString': "metadataString_example", // String | Store user defined metadata like backup checksum, disk ids, restore metadata etc.
  'length': 56, // Number | Length of the inline chunk data.
  'checksum': "checksum_example", // String | Inline chunk checksum
  'checksumAlgorithm': "checksumAlgorithm_example", // String | Inline chunk checksum algorithm
  'objectChecksum': "objectChecksum_example", // String | object checksum
  'objectChecksumAlgorithm': "objectChecksumAlgorithm_example", // String | object checksum algorithm
  'throwOnDuplicate': true // Boolean | Throw an exception if Object name is already exist.
};
apiInstance.putObject(jobId, objectName, putObjectRequest, opts, (error, data, response) => {
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
 **jobId** | **String**| Backup job Id for the in-progress backup. | 
 **objectName** | **String**| The name of the Object to be uploaded. | 
 **putObjectRequest** | [**PutObjectRequest**](PutObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **metadataString** | **String**| Store user defined metadata like backup checksum, disk ids, restore metadata etc. | [optional] 
 **length** | **Number**| Length of the inline chunk data. | [optional] 
 **checksum** | **String**| Inline chunk checksum | [optional] 
 **checksumAlgorithm** | **String**| Inline chunk checksum algorithm | [optional] 
 **objectChecksum** | **String**| object checksum | [optional] 
 **objectChecksumAlgorithm** | **String**| object checksum algorithm | [optional] 
 **throwOnDuplicate** | **Boolean**| Throw an exception if Object name is already exist. | [optional] 

### Return type

[**PutObjectOutput**](PutObjectOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startObject

> StartObjectOutput startObject(jobId, objectName, startObjectRequest, opts)



Start upload containing one or many chunks.

### Example

```javascript
import AwsBackupStorage from 'aws_backup_storage';
let defaultClient = AwsBackupStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackupStorage.DefaultApi();
let jobId = "jobId_example"; // String | Backup job Id for the in-progress backup
let objectName = "objectName_example"; // String | Name for the object.
let startObjectRequest = new AwsBackupStorage.StartObjectRequest(); // StartObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startObject(jobId, objectName, startObjectRequest, opts, (error, data, response) => {
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
 **jobId** | **String**| Backup job Id for the in-progress backup | 
 **objectName** | **String**| Name for the object. | 
 **startObjectRequest** | [**StartObjectRequest**](StartObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartObjectOutput**](StartObjectOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

