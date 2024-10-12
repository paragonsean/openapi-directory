# AwsHealthImaging.DefaultApi

All URIs are relative to *http://medical-imaging.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copyImageSet**](DefaultApi.md#copyImageSet) | **POST** /datastore/{datastoreId}/imageSet/{sourceImageSetId}/copyImageSet | 
[**createDatastore**](DefaultApi.md#createDatastore) | **POST** /datastore | 
[**deleteDatastore**](DefaultApi.md#deleteDatastore) | **DELETE** /datastore/{datastoreId} | 
[**deleteImageSet**](DefaultApi.md#deleteImageSet) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/deleteImageSet | 
[**getDICOMImportJob**](DefaultApi.md#getDICOMImportJob) | **GET** /getDICOMImportJob/datastore/{datastoreId}/job/{jobId} | 
[**getDatastore**](DefaultApi.md#getDatastore) | **GET** /datastore/{datastoreId} | 
[**getImageFrame**](DefaultApi.md#getImageFrame) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageFrame | 
[**getImageSet**](DefaultApi.md#getImageSet) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageSet | 
[**getImageSetMetadata**](DefaultApi.md#getImageSetMetadata) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageSetMetadata | 
[**listDICOMImportJobs**](DefaultApi.md#listDICOMImportJobs) | **GET** /listDICOMImportJobs/datastore/{datastoreId} | 
[**listDatastores**](DefaultApi.md#listDatastores) | **GET** /datastore | 
[**listImageSetVersions**](DefaultApi.md#listImageSetVersions) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/listImageSetVersions | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**searchImageSets**](DefaultApi.md#searchImageSets) | **POST** /datastore/{datastoreId}/searchImageSets | 
[**startDICOMImportJob**](DefaultApi.md#startDICOMImportJob) | **POST** /startDICOMImportJob/datastore/{datastoreId} | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateImageSetMetadata**](DefaultApi.md#updateImageSetMetadata) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/updateImageSetMetadata#latestVersion | 



## copyImageSet

> CopyImageSetResponse copyImageSet(datastoreId, sourceImageSetId, copyImageSetRequest, opts)



Copy an image set.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let sourceImageSetId = "sourceImageSetId_example"; // String | The source image set identifier.
let copyImageSetRequest = new AwsHealthImaging.CopyImageSetRequest(); // CopyImageSetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.copyImageSet(datastoreId, sourceImageSetId, copyImageSetRequest, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **sourceImageSetId** | **String**| The source image set identifier. | 
 **copyImageSetRequest** | [**CopyImageSetRequest**](CopyImageSetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CopyImageSetResponse**](CopyImageSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDatastore

> CreateDatastoreResponse createDatastore(createDatastoreRequest, opts)



Create a data store.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let createDatastoreRequest = new AwsHealthImaging.CreateDatastoreRequest(); // CreateDatastoreRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDatastore(createDatastoreRequest, opts, (error, data, response) => {
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
 **createDatastoreRequest** | [**CreateDatastoreRequest**](CreateDatastoreRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDatastoreResponse**](CreateDatastoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDatastore

> DeleteDatastoreResponse deleteDatastore(datastoreId, opts)



&lt;p&gt;Delete a data store.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before a data store can be deleted, you must first delete all image sets within it.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDatastore(datastoreId, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteDatastoreResponse**](DeleteDatastoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteImageSet

> DeleteImageSetResponse deleteImageSet(datastoreId, imageSetId, opts)



Delete an image set.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let imageSetId = "imageSetId_example"; // String | The image set identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteImageSet(datastoreId, imageSetId, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **imageSetId** | **String**| The image set identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteImageSetResponse**](DeleteImageSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDICOMImportJob

> GetDICOMImportJobResponse getDICOMImportJob(datastoreId, jobId, opts)



Get the import job properties to learn more about the job or job progress.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let jobId = "jobId_example"; // String | The import job identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDICOMImportJob(datastoreId, jobId, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **jobId** | **String**| The import job identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDICOMImportJobResponse**](GetDICOMImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatastore

> GetDatastoreResponse getDatastore(datastoreId, opts)



Get data store properties.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDatastore(datastoreId, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDatastoreResponse**](GetDatastoreResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageFrame

> GetImageFrameResponse getImageFrame(datastoreId, imageSetId, getImageFrameRequest, opts)



Get an image frame (pixel data) for an image set.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let imageSetId = "imageSetId_example"; // String | The image set identifier.
let getImageFrameRequest = new AwsHealthImaging.GetImageFrameRequest(); // GetImageFrameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getImageFrame(datastoreId, imageSetId, getImageFrameRequest, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **imageSetId** | **String**| The image set identifier. | 
 **getImageFrameRequest** | [**GetImageFrameRequest**](GetImageFrameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetImageFrameResponse**](GetImageFrameResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getImageSet

> GetImageSetResponse getImageSet(datastoreId, imageSetId, opts)



Get image set properties.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let imageSetId = "imageSetId_example"; // String | The image set identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | The image set version identifier.
};
apiInstance.getImageSet(datastoreId, imageSetId, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **imageSetId** | **String**| The image set identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| The image set version identifier. | [optional] 

### Return type

[**GetImageSetResponse**](GetImageSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageSetMetadata

> GetImageSetMetadataResponse getImageSetMetadata(datastoreId, imageSetId, opts)



Get metadata attributes for an image set.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let imageSetId = "imageSetId_example"; // String | The image set identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | The image set version identifier.
};
apiInstance.getImageSetMetadata(datastoreId, imageSetId, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **imageSetId** | **String**| The image set identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| The image set version identifier. | [optional] 

### Return type

[**GetImageSetMetadataResponse**](GetImageSetMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDICOMImportJobs

> ListDICOMImportJobsResponse listDICOMImportJobs(datastoreId, opts)



List import jobs created by this AWS account for a specific data store.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'jobStatus': "jobStatus_example", // String | The filters for listing import jobs based on status.
  'nextToken': "nextToken_example", // String | The pagination token used to request the list of import jobs on the next page.
  'maxResults': 56 // Number | The max results count. The upper bound is determined by load testing.
};
apiInstance.listDICOMImportJobs(datastoreId, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **jobStatus** | **String**| The filters for listing import jobs based on status. | [optional] 
 **nextToken** | **String**| The pagination token used to request the list of import jobs on the next page. | [optional] 
 **maxResults** | **Number**| The max results count. The upper bound is determined by load testing. | [optional] 

### Return type

[**ListDICOMImportJobsResponse**](ListDICOMImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDatastores

> ListDatastoresResponse listDatastores(opts)



List data stores created by this AWS account.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'datastoreStatus': "datastoreStatus_example", // String | The data store status.
  'nextToken': "nextToken_example", // String | The pagination token used to request the list of data stores on the next page.
  'maxResults': 56 // Number | Valid Range: Minimum value of 1. Maximum value of 50.
};
apiInstance.listDatastores(opts, (error, data, response) => {
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
 **datastoreStatus** | **String**| The data store status. | [optional] 
 **nextToken** | **String**| The pagination token used to request the list of data stores on the next page. | [optional] 
 **maxResults** | **Number**| Valid Range: Minimum value of 1. Maximum value of 50. | [optional] 

### Return type

[**ListDatastoresResponse**](ListDatastoresResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImageSetVersions

> ListImageSetVersionsResponse listImageSetVersions(datastoreId, imageSetId, opts)



List image set versions.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let imageSetId = "imageSetId_example"; // String | The image set identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token used to request the list of image set versions on the next page.
  'maxResults': 56 // Number | The max results count.
};
apiInstance.listImageSetVersions(datastoreId, imageSetId, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **imageSetId** | **String**| The image set identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token used to request the list of image set versions on the next page. | [optional] 
 **maxResults** | **Number**| The max results count. | [optional] 

### Return type

[**ListImageSetVersionsResponse**](ListImageSetVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists all tags associated with a medical imaging resource.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the medical imaging resource to list tags for.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the medical imaging resource to list tags for. | 
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


## searchImageSets

> SearchImageSetsResponse searchImageSets(datastoreId, searchImageSetsRequest, opts)



Search image sets based on defined input attributes.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The identifier of the data store where the image sets reside.
let searchImageSetsRequest = new AwsHealthImaging.SearchImageSetsRequest(); // SearchImageSetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results that can be returned in a search.
  'nextToken': "nextToken_example" // String | The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended.
};
apiInstance.searchImageSets(datastoreId, searchImageSetsRequest, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The identifier of the data store where the image sets reside. | 
 **searchImageSetsRequest** | [**SearchImageSetsRequest**](SearchImageSetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results that can be returned in a search. | [optional] 
 **nextToken** | **String**| The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended. | [optional] 

### Return type

[**SearchImageSetsResponse**](SearchImageSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startDICOMImportJob

> StartDICOMImportJobResponse startDICOMImportJob(datastoreId, startDICOMImportJobRequest, opts)



Start importing bulk data into an &lt;code&gt;ACTIVE&lt;/code&gt; data store. The import job imports DICOM P10 files found in the S3 prefix specified by the &lt;code&gt;inputS3Uri&lt;/code&gt; parameter. The import job stores processing results in the file specified by the &lt;code&gt;outputS3Uri&lt;/code&gt; parameter.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let startDICOMImportJobRequest = new AwsHealthImaging.StartDICOMImportJobRequest(); // StartDICOMImportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startDICOMImportJob(datastoreId, startDICOMImportJobRequest, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **startDICOMImportJobRequest** | [**StartDICOMImportJobRequest**](StartDICOMImportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartDICOMImportJobResponse**](StartDICOMImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds a user-specifed key and value tag to a medical imaging resource.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to.
let tagResourceRequest = new AwsHealthImaging.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to. | 
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



Removes tags from a medical imaging resource.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from.
let tagKeys = ["null"]; // [String] | The keys for the tags to be removed from the medical imaging resource.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from. | 
 **tagKeys** | [**[String]**](String.md)| The keys for the tags to be removed from the medical imaging resource. | 
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


## updateImageSetMetadata

> UpdateImageSetMetadataResponse updateImageSetMetadata(datastoreId, imageSetId, latestVersion, updateImageSetMetadataRequest, opts)



Update image set metadata attributes.

### Example

```javascript
import AwsHealthImaging from 'aws_health_imaging';
let defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthImaging.DefaultApi();
let datastoreId = "datastoreId_example"; // String | The data store identifier.
let imageSetId = "imageSetId_example"; // String | The image set identifier.
let latestVersion = "latestVersion_example"; // String | The latest image set version identifier.
let updateImageSetMetadataRequest = new AwsHealthImaging.UpdateImageSetMetadataRequest(); // UpdateImageSetMetadataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateImageSetMetadata(datastoreId, imageSetId, latestVersion, updateImageSetMetadataRequest, opts, (error, data, response) => {
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
 **datastoreId** | **String**| The data store identifier. | 
 **imageSetId** | **String**| The image set identifier. | 
 **latestVersion** | **String**| The latest image set version identifier. | 
 **updateImageSetMetadataRequest** | [**UpdateImageSetMetadataRequest**](UpdateImageSetMetadataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateImageSetMetadataResponse**](UpdateImageSetMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

