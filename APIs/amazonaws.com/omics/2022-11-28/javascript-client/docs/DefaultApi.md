# AmazonOmics.DefaultApi

All URIs are relative to *http://omics.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abortMultipartReadSetUpload**](DefaultApi.md#abortMultipartReadSetUpload) | **DELETE** /sequencestore/{sequenceStoreId}/upload/{uploadId}/abort | 
[**batchDeleteReadSet**](DefaultApi.md#batchDeleteReadSet) | **POST** /sequencestore/{sequenceStoreId}/readset/batch/delete | 
[**cancelAnnotationImportJob**](DefaultApi.md#cancelAnnotationImportJob) | **DELETE** /import/annotation/{jobId} | 
[**cancelRun**](DefaultApi.md#cancelRun) | **POST** /run/{id}/cancel | 
[**cancelVariantImportJob**](DefaultApi.md#cancelVariantImportJob) | **DELETE** /import/variant/{jobId} | 
[**completeMultipartReadSetUpload**](DefaultApi.md#completeMultipartReadSetUpload) | **POST** /sequencestore/{sequenceStoreId}/upload/{uploadId}/complete | 
[**createAnnotationStore**](DefaultApi.md#createAnnotationStore) | **POST** /annotationStore | 
[**createMultipartReadSetUpload**](DefaultApi.md#createMultipartReadSetUpload) | **POST** /sequencestore/{sequenceStoreId}/upload | 
[**createReferenceStore**](DefaultApi.md#createReferenceStore) | **POST** /referencestore | 
[**createRunGroup**](DefaultApi.md#createRunGroup) | **POST** /runGroup | 
[**createSequenceStore**](DefaultApi.md#createSequenceStore) | **POST** /sequencestore | 
[**createVariantStore**](DefaultApi.md#createVariantStore) | **POST** /variantStore | 
[**createWorkflow**](DefaultApi.md#createWorkflow) | **POST** /workflow | 
[**deleteAnnotationStore**](DefaultApi.md#deleteAnnotationStore) | **DELETE** /annotationStore/{name} | 
[**deleteReference**](DefaultApi.md#deleteReference) | **DELETE** /referencestore/{referenceStoreId}/reference/{id} | 
[**deleteReferenceStore**](DefaultApi.md#deleteReferenceStore) | **DELETE** /referencestore/{id} | 
[**deleteRun**](DefaultApi.md#deleteRun) | **DELETE** /run/{id} | 
[**deleteRunGroup**](DefaultApi.md#deleteRunGroup) | **DELETE** /runGroup/{id} | 
[**deleteSequenceStore**](DefaultApi.md#deleteSequenceStore) | **DELETE** /sequencestore/{id} | 
[**deleteVariantStore**](DefaultApi.md#deleteVariantStore) | **DELETE** /variantStore/{name} | 
[**deleteWorkflow**](DefaultApi.md#deleteWorkflow) | **DELETE** /workflow/{id} | 
[**getAnnotationImportJob**](DefaultApi.md#getAnnotationImportJob) | **GET** /import/annotation/{jobId} | 
[**getAnnotationStore**](DefaultApi.md#getAnnotationStore) | **GET** /annotationStore/{name} | 
[**getReadSet**](DefaultApi.md#getReadSet) | **GET** /sequencestore/{sequenceStoreId}/readset/{id}#partNumber | 
[**getReadSetActivationJob**](DefaultApi.md#getReadSetActivationJob) | **GET** /sequencestore/{sequenceStoreId}/activationjob/{id} | 
[**getReadSetExportJob**](DefaultApi.md#getReadSetExportJob) | **GET** /sequencestore/{sequenceStoreId}/exportjob/{id} | 
[**getReadSetImportJob**](DefaultApi.md#getReadSetImportJob) | **GET** /sequencestore/{sequenceStoreId}/importjob/{id} | 
[**getReadSetMetadata**](DefaultApi.md#getReadSetMetadata) | **GET** /sequencestore/{sequenceStoreId}/readset/{id}/metadata | 
[**getReference**](DefaultApi.md#getReference) | **GET** /referencestore/{referenceStoreId}/reference/{id}#partNumber | 
[**getReferenceImportJob**](DefaultApi.md#getReferenceImportJob) | **GET** /referencestore/{referenceStoreId}/importjob/{id} | 
[**getReferenceMetadata**](DefaultApi.md#getReferenceMetadata) | **GET** /referencestore/{referenceStoreId}/reference/{id}/metadata | 
[**getReferenceStore**](DefaultApi.md#getReferenceStore) | **GET** /referencestore/{id} | 
[**getRun**](DefaultApi.md#getRun) | **GET** /run/{id} | 
[**getRunGroup**](DefaultApi.md#getRunGroup) | **GET** /runGroup/{id} | 
[**getRunTask**](DefaultApi.md#getRunTask) | **GET** /run/{id}/task/{taskId} | 
[**getSequenceStore**](DefaultApi.md#getSequenceStore) | **GET** /sequencestore/{id} | 
[**getVariantImportJob**](DefaultApi.md#getVariantImportJob) | **GET** /import/variant/{jobId} | 
[**getVariantStore**](DefaultApi.md#getVariantStore) | **GET** /variantStore/{name} | 
[**getWorkflow**](DefaultApi.md#getWorkflow) | **GET** /workflow/{id} | 
[**listAnnotationImportJobs**](DefaultApi.md#listAnnotationImportJobs) | **POST** /import/annotations | 
[**listAnnotationStores**](DefaultApi.md#listAnnotationStores) | **POST** /annotationStores | 
[**listMultipartReadSetUploads**](DefaultApi.md#listMultipartReadSetUploads) | **POST** /sequencestore/{sequenceStoreId}/uploads | 
[**listReadSetActivationJobs**](DefaultApi.md#listReadSetActivationJobs) | **POST** /sequencestore/{sequenceStoreId}/activationjobs | 
[**listReadSetExportJobs**](DefaultApi.md#listReadSetExportJobs) | **POST** /sequencestore/{sequenceStoreId}/exportjobs | 
[**listReadSetImportJobs**](DefaultApi.md#listReadSetImportJobs) | **POST** /sequencestore/{sequenceStoreId}/importjobs | 
[**listReadSetUploadParts**](DefaultApi.md#listReadSetUploadParts) | **POST** /sequencestore/{sequenceStoreId}/upload/{uploadId}/parts | 
[**listReadSets**](DefaultApi.md#listReadSets) | **POST** /sequencestore/{sequenceStoreId}/readsets | 
[**listReferenceImportJobs**](DefaultApi.md#listReferenceImportJobs) | **POST** /referencestore/{referenceStoreId}/importjobs | 
[**listReferenceStores**](DefaultApi.md#listReferenceStores) | **POST** /referencestores | 
[**listReferences**](DefaultApi.md#listReferences) | **POST** /referencestore/{referenceStoreId}/references | 
[**listRunGroups**](DefaultApi.md#listRunGroups) | **GET** /runGroup | 
[**listRunTasks**](DefaultApi.md#listRunTasks) | **GET** /run/{id}/task | 
[**listRuns**](DefaultApi.md#listRuns) | **GET** /run | 
[**listSequenceStores**](DefaultApi.md#listSequenceStores) | **POST** /sequencestores | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**listVariantImportJobs**](DefaultApi.md#listVariantImportJobs) | **POST** /import/variants | 
[**listVariantStores**](DefaultApi.md#listVariantStores) | **POST** /variantStores | 
[**listWorkflows**](DefaultApi.md#listWorkflows) | **GET** /workflow | 
[**startAnnotationImportJob**](DefaultApi.md#startAnnotationImportJob) | **POST** /import/annotation | 
[**startReadSetActivationJob**](DefaultApi.md#startReadSetActivationJob) | **POST** /sequencestore/{sequenceStoreId}/activationjob | 
[**startReadSetExportJob**](DefaultApi.md#startReadSetExportJob) | **POST** /sequencestore/{sequenceStoreId}/exportjob | 
[**startReadSetImportJob**](DefaultApi.md#startReadSetImportJob) | **POST** /sequencestore/{sequenceStoreId}/importjob | 
[**startReferenceImportJob**](DefaultApi.md#startReferenceImportJob) | **POST** /referencestore/{referenceStoreId}/importjob | 
[**startRun**](DefaultApi.md#startRun) | **POST** /run | 
[**startVariantImportJob**](DefaultApi.md#startVariantImportJob) | **POST** /import/variant | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateAnnotationStore**](DefaultApi.md#updateAnnotationStore) | **POST** /annotationStore/{name} | 
[**updateRunGroup**](DefaultApi.md#updateRunGroup) | **POST** /runGroup/{id} | 
[**updateVariantStore**](DefaultApi.md#updateVariantStore) | **POST** /variantStore/{name} | 
[**updateWorkflow**](DefaultApi.md#updateWorkflow) | **POST** /workflow/{id} | 
[**uploadReadSetPart**](DefaultApi.md#uploadReadSetPart) | **PUT** /sequencestore/{sequenceStoreId}/upload/{uploadId}/part#partSource&amp;partNumber | 



## abortMultipartReadSetUpload

> Object abortMultipartReadSetUpload(sequenceStoreId, uploadId, opts)



 Stops a multipart upload. 

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String |  The sequence store ID for the store involved in the multipart upload. 
let uploadId = "uploadId_example"; // String |  The ID for the multipart upload. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.abortMultipartReadSetUpload(sequenceStoreId, uploadId, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**|  The sequence store ID for the store involved in the multipart upload.  | 
 **uploadId** | **String**|  The ID for the multipart upload.  | 
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


## batchDeleteReadSet

> BatchDeleteReadSetResponse batchDeleteReadSet(sequenceStoreId, batchDeleteReadSetRequest, opts)



Deletes one or more read sets.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The read sets' sequence store ID.
let batchDeleteReadSetRequest = new AmazonOmics.BatchDeleteReadSetRequest(); // BatchDeleteReadSetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeleteReadSet(sequenceStoreId, batchDeleteReadSetRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The read sets&#39; sequence store ID. | 
 **batchDeleteReadSetRequest** | [**BatchDeleteReadSetRequest**](BatchDeleteReadSetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteReadSetResponse**](BatchDeleteReadSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelAnnotationImportJob

> Object cancelAnnotationImportJob(jobId, opts)



Cancels an annotation import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let jobId = "jobId_example"; // String | The job's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelAnnotationImportJob(jobId, opts, (error, data, response) => {
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
 **jobId** | **String**| The job&#39;s ID. | 
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


## cancelRun

> cancelRun(id, opts)



Cancels a run.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The run's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelRun(id, opts, (error, data, response) => {
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
 **id** | **String**| The run&#39;s ID. | 
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


## cancelVariantImportJob

> Object cancelVariantImportJob(jobId, opts)



Cancels a variant import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let jobId = "jobId_example"; // String | The job's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelVariantImportJob(jobId, opts, (error, data, response) => {
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
 **jobId** | **String**| The job&#39;s ID. | 
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


## completeMultipartReadSetUpload

> CompleteMultipartReadSetUploadResponse completeMultipartReadSetUpload(sequenceStoreId, uploadId, completeMultipartReadSetUploadRequest, opts)



 Concludes a multipart upload once you have uploaded all the components. 

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String |  The sequence store ID for the store involved in the multipart upload. 
let uploadId = "uploadId_example"; // String |  The ID for the multipart upload. 
let completeMultipartReadSetUploadRequest = new AmazonOmics.CompleteMultipartReadSetUploadRequest(); // CompleteMultipartReadSetUploadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.completeMultipartReadSetUpload(sequenceStoreId, uploadId, completeMultipartReadSetUploadRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**|  The sequence store ID for the store involved in the multipart upload.  | 
 **uploadId** | **String**|  The ID for the multipart upload.  | 
 **completeMultipartReadSetUploadRequest** | [**CompleteMultipartReadSetUploadRequest**](CompleteMultipartReadSetUploadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CompleteMultipartReadSetUploadResponse**](CompleteMultipartReadSetUploadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnnotationStore

> CreateAnnotationStoreResponse createAnnotationStore(createAnnotationStoreRequest, opts)



Creates an annotation store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let createAnnotationStoreRequest = new AmazonOmics.CreateAnnotationStoreRequest(); // CreateAnnotationStoreRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAnnotationStore(createAnnotationStoreRequest, opts, (error, data, response) => {
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
 **createAnnotationStoreRequest** | [**CreateAnnotationStoreRequest**](CreateAnnotationStoreRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAnnotationStoreResponse**](CreateAnnotationStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMultipartReadSetUpload

> CreateMultipartReadSetUploadResponse createMultipartReadSetUpload(sequenceStoreId, createMultipartReadSetUploadRequest, opts)



 Begins a multipart read set upload. 

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String |  The sequence store ID for the store that is the destination of the multipart uploads. 
let createMultipartReadSetUploadRequest = new AmazonOmics.CreateMultipartReadSetUploadRequest(); // CreateMultipartReadSetUploadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMultipartReadSetUpload(sequenceStoreId, createMultipartReadSetUploadRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**|  The sequence store ID for the store that is the destination of the multipart uploads.  | 
 **createMultipartReadSetUploadRequest** | [**CreateMultipartReadSetUploadRequest**](CreateMultipartReadSetUploadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMultipartReadSetUploadResponse**](CreateMultipartReadSetUploadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createReferenceStore

> CreateReferenceStoreResponse createReferenceStore(createReferenceStoreRequest, opts)



Creates a reference store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let createReferenceStoreRequest = new AmazonOmics.CreateReferenceStoreRequest(); // CreateReferenceStoreRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createReferenceStore(createReferenceStoreRequest, opts, (error, data, response) => {
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
 **createReferenceStoreRequest** | [**CreateReferenceStoreRequest**](CreateReferenceStoreRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateReferenceStoreResponse**](CreateReferenceStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRunGroup

> CreateRunGroupResponse createRunGroup(createRunGroupRequest, opts)



Creates a run group.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let createRunGroupRequest = new AmazonOmics.CreateRunGroupRequest(); // CreateRunGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRunGroup(createRunGroupRequest, opts, (error, data, response) => {
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
 **createRunGroupRequest** | [**CreateRunGroupRequest**](CreateRunGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRunGroupResponse**](CreateRunGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSequenceStore

> CreateSequenceStoreResponse createSequenceStore(createSequenceStoreRequest, opts)



Creates a sequence store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let createSequenceStoreRequest = new AmazonOmics.CreateSequenceStoreRequest(); // CreateSequenceStoreRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSequenceStore(createSequenceStoreRequest, opts, (error, data, response) => {
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
 **createSequenceStoreRequest** | [**CreateSequenceStoreRequest**](CreateSequenceStoreRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSequenceStoreResponse**](CreateSequenceStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVariantStore

> CreateVariantStoreResponse createVariantStore(createVariantStoreRequest, opts)



Creates a variant store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let createVariantStoreRequest = new AmazonOmics.CreateVariantStoreRequest(); // CreateVariantStoreRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVariantStore(createVariantStoreRequest, opts, (error, data, response) => {
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
 **createVariantStoreRequest** | [**CreateVariantStoreRequest**](CreateVariantStoreRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVariantStoreResponse**](CreateVariantStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWorkflow

> CreateWorkflowResponse createWorkflow(createWorkflowRequest, opts)



Creates a workflow.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let createWorkflowRequest = new AmazonOmics.CreateWorkflowRequest(); // CreateWorkflowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWorkflow(createWorkflowRequest, opts, (error, data, response) => {
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
 **createWorkflowRequest** | [**CreateWorkflowRequest**](CreateWorkflowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWorkflowResponse**](CreateWorkflowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAnnotationStore

> DeleteAnnotationStoreResponse deleteAnnotationStore(name, opts)



Deletes an annotation store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let name = "name_example"; // String | The store's name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'force': true // Boolean | Whether to force deletion.
};
apiInstance.deleteAnnotationStore(name, opts, (error, data, response) => {
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
 **name** | **String**| The store&#39;s name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **force** | **Boolean**| Whether to force deletion. | [optional] 

### Return type

[**DeleteAnnotationStoreResponse**](DeleteAnnotationStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteReference

> Object deleteReference(id, referenceStoreId, opts)



Deletes a genome reference.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The reference's ID.
let referenceStoreId = "referenceStoreId_example"; // String | The reference's store ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteReference(id, referenceStoreId, opts, (error, data, response) => {
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
 **id** | **String**| The reference&#39;s ID. | 
 **referenceStoreId** | **String**| The reference&#39;s store ID. | 
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


## deleteReferenceStore

> Object deleteReferenceStore(id, opts)



Deletes a genome reference store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The store's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteReferenceStore(id, opts, (error, data, response) => {
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
 **id** | **String**| The store&#39;s ID. | 
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


## deleteRun

> deleteRun(id, opts)



Deletes a workflow run.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The run's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRun(id, opts, (error, data, response) => {
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
 **id** | **String**| The run&#39;s ID. | 
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


## deleteRunGroup

> deleteRunGroup(id, opts)



Deletes a workflow run group.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The run group's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRunGroup(id, opts, (error, data, response) => {
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
 **id** | **String**| The run group&#39;s ID. | 
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


## deleteSequenceStore

> Object deleteSequenceStore(id, opts)



Deletes a sequence store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The sequence store's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSequenceStore(id, opts, (error, data, response) => {
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
 **id** | **String**| The sequence store&#39;s ID. | 
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


## deleteVariantStore

> DeleteVariantStoreResponse deleteVariantStore(name, opts)



Deletes a variant store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let name = "name_example"; // String | The store's name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'force': true // Boolean | Whether to force deletion.
};
apiInstance.deleteVariantStore(name, opts, (error, data, response) => {
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
 **name** | **String**| The store&#39;s name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **force** | **Boolean**| Whether to force deletion. | [optional] 

### Return type

[**DeleteVariantStoreResponse**](DeleteVariantStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWorkflow

> deleteWorkflow(id, opts)



Deletes a workflow.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The workflow's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWorkflow(id, opts, (error, data, response) => {
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
 **id** | **String**| The workflow&#39;s ID. | 
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


## getAnnotationImportJob

> GetAnnotationImportResponse getAnnotationImportJob(jobId, opts)



Gets information about an annotation import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let jobId = "jobId_example"; // String | The job's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAnnotationImportJob(jobId, opts, (error, data, response) => {
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
 **jobId** | **String**| The job&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAnnotationImportResponse**](GetAnnotationImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnnotationStore

> GetAnnotationStoreResponse getAnnotationStore(name, opts)



Gets information about an annotation store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let name = "name_example"; // String | The store's name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAnnotationStore(name, opts, (error, data, response) => {
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
 **name** | **String**| The store&#39;s name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAnnotationStoreResponse**](GetAnnotationStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReadSet

> GetReadSetResponse getReadSet(id, sequenceStoreId, partNumber, opts)



Gets a file from a read set.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The read set's ID.
let sequenceStoreId = "sequenceStoreId_example"; // String | The read set's sequence store ID.
let partNumber = 56; // Number | The part number to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'file': "file_example" // String | The file to retrieve.
};
apiInstance.getReadSet(id, sequenceStoreId, partNumber, opts, (error, data, response) => {
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
 **id** | **String**| The read set&#39;s ID. | 
 **sequenceStoreId** | **String**| The read set&#39;s sequence store ID. | 
 **partNumber** | **Number**| The part number to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **file** | **String**| The file to retrieve. | [optional] 

### Return type

[**GetReadSetResponse**](GetReadSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReadSetActivationJob

> GetReadSetActivationJobResponse getReadSetActivationJob(id, sequenceStoreId, opts)



Gets information about a read set activation job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The job's ID.
let sequenceStoreId = "sequenceStoreId_example"; // String | The job's sequence store ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getReadSetActivationJob(id, sequenceStoreId, opts, (error, data, response) => {
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
 **id** | **String**| The job&#39;s ID. | 
 **sequenceStoreId** | **String**| The job&#39;s sequence store ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetReadSetActivationJobResponse**](GetReadSetActivationJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReadSetExportJob

> GetReadSetExportJobResponse getReadSetExportJob(sequenceStoreId, id, opts)



Gets information about a read set export job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The job's sequence store ID.
let id = "id_example"; // String | The job's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getReadSetExportJob(sequenceStoreId, id, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The job&#39;s sequence store ID. | 
 **id** | **String**| The job&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetReadSetExportJobResponse**](GetReadSetExportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReadSetImportJob

> GetReadSetImportJobResponse getReadSetImportJob(id, sequenceStoreId, opts)



Gets information about a read set import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The job's ID.
let sequenceStoreId = "sequenceStoreId_example"; // String | The job's sequence store ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getReadSetImportJob(id, sequenceStoreId, opts, (error, data, response) => {
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
 **id** | **String**| The job&#39;s ID. | 
 **sequenceStoreId** | **String**| The job&#39;s sequence store ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetReadSetImportJobResponse**](GetReadSetImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReadSetMetadata

> GetReadSetMetadataResponse getReadSetMetadata(id, sequenceStoreId, opts)



Gets details about a read set.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The read set's ID.
let sequenceStoreId = "sequenceStoreId_example"; // String | The read set's sequence store ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getReadSetMetadata(id, sequenceStoreId, opts, (error, data, response) => {
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
 **id** | **String**| The read set&#39;s ID. | 
 **sequenceStoreId** | **String**| The read set&#39;s sequence store ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetReadSetMetadataResponse**](GetReadSetMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReference

> GetReferenceResponse getReference(id, referenceStoreId, partNumber, opts)



Gets a reference file.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The reference's ID.
let referenceStoreId = "referenceStoreId_example"; // String | The reference's store ID.
let partNumber = 56; // Number | The part number to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'range': "range_example", // String | The range to retrieve.
  'file': "file_example" // String | The file to retrieve.
};
apiInstance.getReference(id, referenceStoreId, partNumber, opts, (error, data, response) => {
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
 **id** | **String**| The reference&#39;s ID. | 
 **referenceStoreId** | **String**| The reference&#39;s store ID. | 
 **partNumber** | **Number**| The part number to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **range** | **String**| The range to retrieve. | [optional] 
 **file** | **String**| The file to retrieve. | [optional] 

### Return type

[**GetReferenceResponse**](GetReferenceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReferenceImportJob

> GetReferenceImportJobResponse getReferenceImportJob(id, referenceStoreId, opts)



Gets information about a reference import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The job's ID.
let referenceStoreId = "referenceStoreId_example"; // String | The job's reference store ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getReferenceImportJob(id, referenceStoreId, opts, (error, data, response) => {
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
 **id** | **String**| The job&#39;s ID. | 
 **referenceStoreId** | **String**| The job&#39;s reference store ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetReferenceImportJobResponse**](GetReferenceImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReferenceMetadata

> GetReferenceMetadataResponse getReferenceMetadata(id, referenceStoreId, opts)



Gets information about a genome reference&#39;s metadata.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The reference's ID.
let referenceStoreId = "referenceStoreId_example"; // String | The reference's reference store ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getReferenceMetadata(id, referenceStoreId, opts, (error, data, response) => {
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
 **id** | **String**| The reference&#39;s ID. | 
 **referenceStoreId** | **String**| The reference&#39;s reference store ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetReferenceMetadataResponse**](GetReferenceMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReferenceStore

> GetReferenceStoreResponse getReferenceStore(id, opts)



Gets information about a reference store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The store's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getReferenceStore(id, opts, (error, data, response) => {
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
 **id** | **String**| The store&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetReferenceStoreResponse**](GetReferenceStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRun

> GetRunResponse getRun(id, opts)



Gets information about a workflow run.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The run's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  '_export': [new AmazonOmics.RunExport()] // [RunExport] | The run's export format.
};
apiInstance.getRun(id, opts, (error, data, response) => {
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
 **id** | **String**| The run&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **_export** | [**[RunExport]**](RunExport.md)| The run&#39;s export format. | [optional] 

### Return type

[**GetRunResponse**](GetRunResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRunGroup

> GetRunGroupResponse getRunGroup(id, opts)



Gets information about a workflow run group.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The group's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRunGroup(id, opts, (error, data, response) => {
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
 **id** | **String**| The group&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRunGroupResponse**](GetRunGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRunTask

> GetRunTaskResponse getRunTask(id, taskId, opts)



Gets information about a workflow run task.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The task's ID.
let taskId = "taskId_example"; // String | The task's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRunTask(id, taskId, opts, (error, data, response) => {
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
 **id** | **String**| The task&#39;s ID. | 
 **taskId** | **String**| The task&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRunTaskResponse**](GetRunTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSequenceStore

> GetSequenceStoreResponse getSequenceStore(id, opts)



Gets information about a sequence store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The store's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSequenceStore(id, opts, (error, data, response) => {
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
 **id** | **String**| The store&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSequenceStoreResponse**](GetSequenceStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantImportJob

> GetVariantImportResponse getVariantImportJob(jobId, opts)



Gets information about a variant import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let jobId = "jobId_example"; // String | The job's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVariantImportJob(jobId, opts, (error, data, response) => {
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
 **jobId** | **String**| The job&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVariantImportResponse**](GetVariantImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantStore

> GetVariantStoreResponse getVariantStore(name, opts)



Gets information about a variant store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let name = "name_example"; // String | The store's name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVariantStore(name, opts, (error, data, response) => {
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
 **name** | **String**| The store&#39;s name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVariantStoreResponse**](GetVariantStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWorkflow

> GetWorkflowResponse getWorkflow(id, opts)



Gets information about a workflow.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The workflow's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'type': "type_example", // String | The workflow's type.
  '_export': [new AmazonOmics.WorkflowExport()] // [WorkflowExport] | The export format for the workflow.
};
apiInstance.getWorkflow(id, opts, (error, data, response) => {
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
 **id** | **String**| The workflow&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **type** | **String**| The workflow&#39;s type. | [optional] 
 **_export** | [**[WorkflowExport]**](WorkflowExport.md)| The export format for the workflow. | [optional] 

### Return type

[**GetWorkflowResponse**](GetWorkflowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAnnotationImportJobs

> ListAnnotationImportJobsResponse listAnnotationImportJobs(listAnnotationImportJobsRequest, opts)



Retrieves a list of annotation import jobs.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let listAnnotationImportJobsRequest = new AmazonOmics.ListAnnotationImportJobsRequest(); // ListAnnotationImportJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of jobs to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listAnnotationImportJobs(listAnnotationImportJobsRequest, opts, (error, data, response) => {
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
 **listAnnotationImportJobsRequest** | [**ListAnnotationImportJobsRequest**](ListAnnotationImportJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of jobs to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListAnnotationImportJobsResponse**](ListAnnotationImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAnnotationStores

> ListAnnotationStoresResponse listAnnotationStores(listAnnotationStoresRequest, opts)



Retrieves a list of annotation stores.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let listAnnotationStoresRequest = new AmazonOmics.ListAnnotationStoresRequest(); // ListAnnotationStoresRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of stores to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listAnnotationStores(listAnnotationStoresRequest, opts, (error, data, response) => {
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
 **listAnnotationStoresRequest** | [**ListAnnotationStoresRequest**](ListAnnotationStoresRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of stores to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListAnnotationStoresResponse**](ListAnnotationStoresResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listMultipartReadSetUploads

> ListMultipartReadSetUploadsResponse listMultipartReadSetUploads(sequenceStoreId, opts)



 Lists all multipart read set uploads and their statuses. 

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String |  The Sequence Store ID used for the multipart uploads. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |  The maximum number of multipart uploads returned in a page. 
  'nextToken': "nextToken_example" // String |  Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results. 
};
apiInstance.listMultipartReadSetUploads(sequenceStoreId, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**|  The Sequence Store ID used for the multipart uploads.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  The maximum number of multipart uploads returned in a page.  | [optional] 
 **nextToken** | **String**|  Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results.  | [optional] 

### Return type

[**ListMultipartReadSetUploadsResponse**](ListMultipartReadSetUploadsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listReadSetActivationJobs

> ListReadSetActivationJobsResponse listReadSetActivationJobs(sequenceStoreId, listReadSetActivationJobsRequest, opts)



Retrieves a list of read set activation jobs.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The read set's sequence store ID.
let listReadSetActivationJobsRequest = new AmazonOmics.ListReadSetActivationJobsRequest(); // ListReadSetActivationJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of read set activation jobs to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listReadSetActivationJobs(sequenceStoreId, listReadSetActivationJobsRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The read set&#39;s sequence store ID. | 
 **listReadSetActivationJobsRequest** | [**ListReadSetActivationJobsRequest**](ListReadSetActivationJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of read set activation jobs to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListReadSetActivationJobsResponse**](ListReadSetActivationJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listReadSetExportJobs

> ListReadSetExportJobsResponse listReadSetExportJobs(sequenceStoreId, listReadSetExportJobsRequest, opts)



Retrieves a list of read set export jobs.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The jobs' sequence store ID.
let listReadSetExportJobsRequest = new AmazonOmics.ListReadSetExportJobsRequest(); // ListReadSetExportJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of jobs to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listReadSetExportJobs(sequenceStoreId, listReadSetExportJobsRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The jobs&#39; sequence store ID. | 
 **listReadSetExportJobsRequest** | [**ListReadSetExportJobsRequest**](ListReadSetExportJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of jobs to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListReadSetExportJobsResponse**](ListReadSetExportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listReadSetImportJobs

> ListReadSetImportJobsResponse listReadSetImportJobs(sequenceStoreId, listReadSetImportJobsRequest, opts)



Retrieves a list of read set import jobs.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The jobs' sequence store ID.
let listReadSetImportJobsRequest = new AmazonOmics.ListReadSetImportJobsRequest(); // ListReadSetImportJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of jobs to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listReadSetImportJobs(sequenceStoreId, listReadSetImportJobsRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The jobs&#39; sequence store ID. | 
 **listReadSetImportJobsRequest** | [**ListReadSetImportJobsRequest**](ListReadSetImportJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of jobs to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListReadSetImportJobsResponse**](ListReadSetImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listReadSetUploadParts

> ListReadSetUploadPartsResponse listReadSetUploadParts(sequenceStoreId, uploadId, listReadSetUploadPartsRequest, opts)



 This operation will list all parts in a requested multipart upload for a sequence store. 

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String |  The Sequence Store ID used for the multipart uploads. 
let uploadId = "uploadId_example"; // String |  The ID for the initiated multipart upload. 
let listReadSetUploadPartsRequest = new AmazonOmics.ListReadSetUploadPartsRequest(); // ListReadSetUploadPartsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |  The maximum number of read set upload parts returned in a page. 
  'nextToken': "nextToken_example" // String |  Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results. 
};
apiInstance.listReadSetUploadParts(sequenceStoreId, uploadId, listReadSetUploadPartsRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**|  The Sequence Store ID used for the multipart uploads.  | 
 **uploadId** | **String**|  The ID for the initiated multipart upload.  | 
 **listReadSetUploadPartsRequest** | [**ListReadSetUploadPartsRequest**](ListReadSetUploadPartsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  The maximum number of read set upload parts returned in a page.  | [optional] 
 **nextToken** | **String**|  Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.  | [optional] 

### Return type

[**ListReadSetUploadPartsResponse**](ListReadSetUploadPartsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listReadSets

> ListReadSetsResponse listReadSets(sequenceStoreId, listReadSetsRequest, opts)



Retrieves a list of read sets.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The jobs' sequence store ID.
let listReadSetsRequest = new AmazonOmics.ListReadSetsRequest(); // ListReadSetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of read sets to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listReadSets(sequenceStoreId, listReadSetsRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The jobs&#39; sequence store ID. | 
 **listReadSetsRequest** | [**ListReadSetsRequest**](ListReadSetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of read sets to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListReadSetsResponse**](ListReadSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listReferenceImportJobs

> ListReferenceImportJobsResponse listReferenceImportJobs(referenceStoreId, listReferenceImportJobsRequest, opts)



Retrieves a list of reference import jobs.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let referenceStoreId = "referenceStoreId_example"; // String | The job's reference store ID.
let listReferenceImportJobsRequest = new AmazonOmics.ListReferenceImportJobsRequest(); // ListReferenceImportJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of jobs to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listReferenceImportJobs(referenceStoreId, listReferenceImportJobsRequest, opts, (error, data, response) => {
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
 **referenceStoreId** | **String**| The job&#39;s reference store ID. | 
 **listReferenceImportJobsRequest** | [**ListReferenceImportJobsRequest**](ListReferenceImportJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of jobs to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListReferenceImportJobsResponse**](ListReferenceImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listReferenceStores

> ListReferenceStoresResponse listReferenceStores(listReferenceStoresRequest, opts)



Retrieves a list of reference stores.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let listReferenceStoresRequest = new AmazonOmics.ListReferenceStoresRequest(); // ListReferenceStoresRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of stores to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listReferenceStores(listReferenceStoresRequest, opts, (error, data, response) => {
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
 **listReferenceStoresRequest** | [**ListReferenceStoresRequest**](ListReferenceStoresRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of stores to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListReferenceStoresResponse**](ListReferenceStoresResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listReferences

> ListReferencesResponse listReferences(referenceStoreId, listReferencesRequest, opts)



Retrieves a list of references.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let referenceStoreId = "referenceStoreId_example"; // String | The references' reference store ID.
let listReferencesRequest = new AmazonOmics.ListReferencesRequest(); // ListReferencesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of references to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listReferences(referenceStoreId, listReferencesRequest, opts, (error, data, response) => {
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
 **referenceStoreId** | **String**| The references&#39; reference store ID. | 
 **listReferencesRequest** | [**ListReferencesRequest**](ListReferencesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of references to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListReferencesResponse**](ListReferencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRunGroups

> ListRunGroupsResponse listRunGroups(opts)



Retrieves a list of run groups.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'name': "name_example", // String | The run groups' name.
  'startingToken': "startingToken_example", // String | Specify the pagination token from a previous request to retrieve the next page of results.
  'maxResults': 56 // Number | The maximum number of run groups to return in one page of results.
};
apiInstance.listRunGroups(opts, (error, data, response) => {
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
 **name** | **String**| The run groups&#39; name. | [optional] 
 **startingToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of run groups to return in one page of results. | [optional] 

### Return type

[**ListRunGroupsResponse**](ListRunGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRunTasks

> ListRunTasksResponse listRunTasks(id, opts)



Retrieves a list of tasks for a run.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The run's ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'status': "status_example", // String | Filter the list by status.
  'startingToken': "startingToken_example", // String | Specify the pagination token from a previous request to retrieve the next page of results.
  'maxResults': 56 // Number | The maximum number of run tasks to return in one page of results.
};
apiInstance.listRunTasks(id, opts, (error, data, response) => {
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
 **id** | **String**| The run&#39;s ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **status** | **String**| Filter the list by status. | [optional] 
 **startingToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of run tasks to return in one page of results. | [optional] 

### Return type

[**ListRunTasksResponse**](ListRunTasksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRuns

> ListRunsResponse listRuns(opts)



Retrieves a list of runs.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'name': "name_example", // String | Filter the list by run name.
  'runGroupId': "runGroupId_example", // String | Filter the list by run group ID.
  'startingToken': "startingToken_example", // String | Specify the pagination token from a previous request to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of runs to return in one page of results.
  'status': "status_example" // String |  The status of a run. 
};
apiInstance.listRuns(opts, (error, data, response) => {
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
 **name** | **String**| Filter the list by run name. | [optional] 
 **runGroupId** | **String**| Filter the list by run group ID. | [optional] 
 **startingToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of runs to return in one page of results. | [optional] 
 **status** | **String**|  The status of a run.  | [optional] 

### Return type

[**ListRunsResponse**](ListRunsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSequenceStores

> ListSequenceStoresResponse listSequenceStores(listSequenceStoresRequest, opts)



Retrieves a list of sequence stores.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let listSequenceStoresRequest = new AmazonOmics.ListSequenceStoresRequest(); // ListSequenceStoresRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of stores to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listSequenceStores(listSequenceStoresRequest, opts, (error, data, response) => {
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
 **listSequenceStoresRequest** | [**ListSequenceStoresRequest**](ListSequenceStoresRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of stores to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListSequenceStoresResponse**](ListSequenceStoresResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Retrieves a list of tags for a resource.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource's ARN.
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
 **resourceArn** | **String**| The resource&#39;s ARN. | 
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


## listVariantImportJobs

> ListVariantImportJobsResponse listVariantImportJobs(listVariantImportJobsRequest, opts)



Retrieves a list of variant import jobs.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let listVariantImportJobsRequest = new AmazonOmics.ListVariantImportJobsRequest(); // ListVariantImportJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of import jobs to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listVariantImportJobs(listVariantImportJobsRequest, opts, (error, data, response) => {
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
 **listVariantImportJobsRequest** | [**ListVariantImportJobsRequest**](ListVariantImportJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of import jobs to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListVariantImportJobsResponse**](ListVariantImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listVariantStores

> ListVariantStoresResponse listVariantStores(listVariantStoresRequest, opts)



Retrieves a list of variant stores.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let listVariantStoresRequest = new AmazonOmics.ListVariantStoresRequest(); // ListVariantStoresRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of stores to return in one page of results.
  'nextToken': "nextToken_example" // String | Specify the pagination token from a previous request to retrieve the next page of results.
};
apiInstance.listVariantStores(listVariantStoresRequest, opts, (error, data, response) => {
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
 **listVariantStoresRequest** | [**ListVariantStoresRequest**](ListVariantStoresRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of stores to return in one page of results. | [optional] 
 **nextToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 

### Return type

[**ListVariantStoresResponse**](ListVariantStoresResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listWorkflows

> ListWorkflowsResponse listWorkflows(opts)



Retrieves a list of workflows.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'type': "type_example", // String | The workflows' type.
  'name': "name_example", // String | The workflows' name.
  'startingToken': "startingToken_example", // String | Specify the pagination token from a previous request to retrieve the next page of results.
  'maxResults': 56 // Number | The maximum number of workflows to return in one page of results.
};
apiInstance.listWorkflows(opts, (error, data, response) => {
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
 **type** | **String**| The workflows&#39; type. | [optional] 
 **name** | **String**| The workflows&#39; name. | [optional] 
 **startingToken** | **String**| Specify the pagination token from a previous request to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of workflows to return in one page of results. | [optional] 

### Return type

[**ListWorkflowsResponse**](ListWorkflowsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startAnnotationImportJob

> StartAnnotationImportResponse startAnnotationImportJob(startAnnotationImportJobRequest, opts)



Starts an annotation import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let startAnnotationImportJobRequest = new AmazonOmics.StartAnnotationImportJobRequest(); // StartAnnotationImportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startAnnotationImportJob(startAnnotationImportJobRequest, opts, (error, data, response) => {
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
 **startAnnotationImportJobRequest** | [**StartAnnotationImportJobRequest**](StartAnnotationImportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartAnnotationImportResponse**](StartAnnotationImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startReadSetActivationJob

> StartReadSetActivationJobResponse startReadSetActivationJob(sequenceStoreId, startReadSetActivationJobRequest, opts)



Activates an archived read set. To reduce storage charges, Amazon Omics archives unused read sets after 30 days.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The read set's sequence store ID.
let startReadSetActivationJobRequest = new AmazonOmics.StartReadSetActivationJobRequest(); // StartReadSetActivationJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startReadSetActivationJob(sequenceStoreId, startReadSetActivationJobRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The read set&#39;s sequence store ID. | 
 **startReadSetActivationJobRequest** | [**StartReadSetActivationJobRequest**](StartReadSetActivationJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartReadSetActivationJobResponse**](StartReadSetActivationJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startReadSetExportJob

> StartReadSetExportJobResponse startReadSetExportJob(sequenceStoreId, startReadSetExportJobRequest, opts)



Exports a read set to Amazon S3.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The read set's sequence store ID.
let startReadSetExportJobRequest = new AmazonOmics.StartReadSetExportJobRequest(); // StartReadSetExportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startReadSetExportJob(sequenceStoreId, startReadSetExportJobRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The read set&#39;s sequence store ID. | 
 **startReadSetExportJobRequest** | [**StartReadSetExportJobRequest**](StartReadSetExportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartReadSetExportJobResponse**](StartReadSetExportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startReadSetImportJob

> StartReadSetImportJobResponse startReadSetImportJob(sequenceStoreId, startReadSetImportJobRequest, opts)



Starts a read set import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String | The read set's sequence store ID.
let startReadSetImportJobRequest = new AmazonOmics.StartReadSetImportJobRequest(); // StartReadSetImportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startReadSetImportJob(sequenceStoreId, startReadSetImportJobRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**| The read set&#39;s sequence store ID. | 
 **startReadSetImportJobRequest** | [**StartReadSetImportJobRequest**](StartReadSetImportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartReadSetImportJobResponse**](StartReadSetImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startReferenceImportJob

> StartReferenceImportJobResponse startReferenceImportJob(referenceStoreId, startReferenceImportJobRequest, opts)



Starts a reference import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let referenceStoreId = "referenceStoreId_example"; // String | The job's reference store ID.
let startReferenceImportJobRequest = new AmazonOmics.StartReferenceImportJobRequest(); // StartReferenceImportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startReferenceImportJob(referenceStoreId, startReferenceImportJobRequest, opts, (error, data, response) => {
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
 **referenceStoreId** | **String**| The job&#39;s reference store ID. | 
 **startReferenceImportJobRequest** | [**StartReferenceImportJobRequest**](StartReferenceImportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartReferenceImportJobResponse**](StartReferenceImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startRun

> StartRunResponse startRun(startRunRequest, opts)



Starts a run.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let startRunRequest = new AmazonOmics.StartRunRequest(); // StartRunRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startRun(startRunRequest, opts, (error, data, response) => {
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
 **startRunRequest** | [**StartRunRequest**](StartRunRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartRunResponse**](StartRunResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startVariantImportJob

> StartVariantImportResponse startVariantImportJob(startVariantImportJobRequest, opts)



Starts a variant import job.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let startVariantImportJobRequest = new AmazonOmics.StartVariantImportJobRequest(); // StartVariantImportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startVariantImportJob(startVariantImportJobRequest, opts, (error, data, response) => {
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
 **startVariantImportJobRequest** | [**StartVariantImportJobRequest**](StartVariantImportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartVariantImportResponse**](StartVariantImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Tags a resource.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource's ARN.
let tagResourceRequest = new AmazonOmics.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The resource&#39;s ARN. | 
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



Removes tags from a resource.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource's ARN.
let tagKeys = ["null"]; // [String] | Keys of tags to remove.
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
 **resourceArn** | **String**| The resource&#39;s ARN. | 
 **tagKeys** | [**[String]**](String.md)| Keys of tags to remove. | 
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


## updateAnnotationStore

> UpdateAnnotationStoreResponse updateAnnotationStore(name, updateAnnotationStoreRequest, opts)



Updates an annotation store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let name = "name_example"; // String | A name for the store.
let updateAnnotationStoreRequest = new AmazonOmics.UpdateAnnotationStoreRequest(); // UpdateAnnotationStoreRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAnnotationStore(name, updateAnnotationStoreRequest, opts, (error, data, response) => {
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
 **name** | **String**| A name for the store. | 
 **updateAnnotationStoreRequest** | [**UpdateAnnotationStoreRequest**](UpdateAnnotationStoreRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAnnotationStoreResponse**](UpdateAnnotationStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRunGroup

> updateRunGroup(id, updateRunGroupRequest, opts)



Updates a run group.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The group's ID.
let updateRunGroupRequest = new AmazonOmics.UpdateRunGroupRequest(); // UpdateRunGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRunGroup(id, updateRunGroupRequest, opts, (error, data, response) => {
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
 **id** | **String**| The group&#39;s ID. | 
 **updateRunGroupRequest** | [**UpdateRunGroupRequest**](UpdateRunGroupRequest.md)|  | 
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


## updateVariantStore

> UpdateVariantStoreResponse updateVariantStore(name, updateAnnotationStoreRequest, opts)



Updates a variant store.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let name = "name_example"; // String | A name for the store.
let updateAnnotationStoreRequest = new AmazonOmics.UpdateAnnotationStoreRequest(); // UpdateAnnotationStoreRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVariantStore(name, updateAnnotationStoreRequest, opts, (error, data, response) => {
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
 **name** | **String**| A name for the store. | 
 **updateAnnotationStoreRequest** | [**UpdateAnnotationStoreRequest**](UpdateAnnotationStoreRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVariantStoreResponse**](UpdateVariantStoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkflow

> updateWorkflow(id, updateWorkflowRequest, opts)



Updates a workflow.

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let id = "id_example"; // String | The workflow's ID.
let updateWorkflowRequest = new AmazonOmics.UpdateWorkflowRequest(); // UpdateWorkflowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWorkflow(id, updateWorkflowRequest, opts, (error, data, response) => {
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
 **id** | **String**| The workflow&#39;s ID. | 
 **updateWorkflowRequest** | [**UpdateWorkflowRequest**](UpdateWorkflowRequest.md)|  | 
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


## uploadReadSetPart

> UploadReadSetPartResponse uploadReadSetPart(sequenceStoreId, uploadId, partSource, partNumber, uploadReadSetPartRequest, opts)



 This operation uploads a specific part of a read set. If you upload a new part using a previously used part number, the previously uploaded part will be overwritten. 

### Example

```javascript
import AmazonOmics from 'amazon_omics';
let defaultClient = AmazonOmics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonOmics.DefaultApi();
let sequenceStoreId = "sequenceStoreId_example"; // String |  The Sequence Store ID used for the multipart upload. 
let uploadId = "uploadId_example"; // String |  The ID for the initiated multipart upload. 
let partSource = "partSource_example"; // String |  The source file for an upload part. 
let partNumber = 56; // Number |  The number of the part being uploaded. 
let uploadReadSetPartRequest = new AmazonOmics.UploadReadSetPartRequest(); // UploadReadSetPartRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.uploadReadSetPart(sequenceStoreId, uploadId, partSource, partNumber, uploadReadSetPartRequest, opts, (error, data, response) => {
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
 **sequenceStoreId** | **String**|  The Sequence Store ID used for the multipart upload.  | 
 **uploadId** | **String**|  The ID for the initiated multipart upload.  | 
 **partSource** | **String**|  The source file for an upload part.  | 
 **partNumber** | **Number**|  The number of the part being uploaded.  | 
 **uploadReadSetPartRequest** | [**UploadReadSetPartRequest**](UploadReadSetPartRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UploadReadSetPartResponse**](UploadReadSetPartResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

