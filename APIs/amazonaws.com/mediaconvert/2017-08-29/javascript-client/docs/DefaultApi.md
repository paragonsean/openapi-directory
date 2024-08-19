# AwsElementalMediaConvert.DefaultApi

All URIs are relative to *http://mediaconvert.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateCertificate**](DefaultApi.md#associateCertificate) | **POST** /2017-08-29/certificates | 
[**cancelJob**](DefaultApi.md#cancelJob) | **DELETE** /2017-08-29/jobs/{id} | 
[**createJob**](DefaultApi.md#createJob) | **POST** /2017-08-29/jobs | 
[**createJobTemplate**](DefaultApi.md#createJobTemplate) | **POST** /2017-08-29/jobTemplates | 
[**createPreset**](DefaultApi.md#createPreset) | **POST** /2017-08-29/presets | 
[**createQueue**](DefaultApi.md#createQueue) | **POST** /2017-08-29/queues | 
[**deleteJobTemplate**](DefaultApi.md#deleteJobTemplate) | **DELETE** /2017-08-29/jobTemplates/{name} | 
[**deletePolicy**](DefaultApi.md#deletePolicy) | **DELETE** /2017-08-29/policy | 
[**deletePreset**](DefaultApi.md#deletePreset) | **DELETE** /2017-08-29/presets/{name} | 
[**deleteQueue**](DefaultApi.md#deleteQueue) | **DELETE** /2017-08-29/queues/{name} | 
[**describeEndpoints**](DefaultApi.md#describeEndpoints) | **POST** /2017-08-29/endpoints | 
[**disassociateCertificate**](DefaultApi.md#disassociateCertificate) | **DELETE** /2017-08-29/certificates/{arn} | 
[**getJob**](DefaultApi.md#getJob) | **GET** /2017-08-29/jobs/{id} | 
[**getJobTemplate**](DefaultApi.md#getJobTemplate) | **GET** /2017-08-29/jobTemplates/{name} | 
[**getPolicy**](DefaultApi.md#getPolicy) | **GET** /2017-08-29/policy | 
[**getPreset**](DefaultApi.md#getPreset) | **GET** /2017-08-29/presets/{name} | 
[**getQueue**](DefaultApi.md#getQueue) | **GET** /2017-08-29/queues/{name} | 
[**listJobTemplates**](DefaultApi.md#listJobTemplates) | **GET** /2017-08-29/jobTemplates | 
[**listJobs**](DefaultApi.md#listJobs) | **GET** /2017-08-29/jobs | 
[**listPresets**](DefaultApi.md#listPresets) | **GET** /2017-08-29/presets | 
[**listQueues**](DefaultApi.md#listQueues) | **GET** /2017-08-29/queues | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /2017-08-29/tags/{arn} | 
[**putPolicy**](DefaultApi.md#putPolicy) | **PUT** /2017-08-29/policy | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /2017-08-29/tags | 
[**untagResource**](DefaultApi.md#untagResource) | **PUT** /2017-08-29/tags/{arn} | 
[**updateJobTemplate**](DefaultApi.md#updateJobTemplate) | **PUT** /2017-08-29/jobTemplates/{name} | 
[**updatePreset**](DefaultApi.md#updatePreset) | **PUT** /2017-08-29/presets/{name} | 
[**updateQueue**](DefaultApi.md#updateQueue) | **PUT** /2017-08-29/queues/{name} | 



## associateCertificate

> Object associateCertificate(associateCertificateRequest, opts)



Associates an AWS Certificate Manager (ACM) Amazon Resource Name (ARN) with AWS Elemental MediaConvert.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let associateCertificateRequest = new AwsElementalMediaConvert.AssociateCertificateRequest(); // AssociateCertificateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateCertificate(associateCertificateRequest, opts, (error, data, response) => {
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
 **associateCertificateRequest** | [**AssociateCertificateRequest**](AssociateCertificateRequest.md)|  | 
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


## cancelJob

> Object cancelJob(id, opts)



Permanently cancel a job. Once you have canceled a job, you can&#39;t start it again.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let id = "id_example"; // String | The Job ID of the job to be cancelled.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelJob(id, opts, (error, data, response) => {
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
 **id** | **String**| The Job ID of the job to be cancelled. | 
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


## createJob

> CreateJobResponse createJob(createJobRequest, opts)



Create a new transcoding job. For information about jobs and job settings, see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let createJobRequest = new AwsElementalMediaConvert.CreateJobRequest(); // CreateJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createJob(createJobRequest, opts, (error, data, response) => {
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
 **createJobRequest** | [**CreateJobRequest**](CreateJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateJobResponse**](CreateJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createJobTemplate

> CreateJobTemplateResponse createJobTemplate(createJobTemplateRequest, opts)



Create a new job template. For information about job templates see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let createJobTemplateRequest = new AwsElementalMediaConvert.CreateJobTemplateRequest(); // CreateJobTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createJobTemplate(createJobTemplateRequest, opts, (error, data, response) => {
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
 **createJobTemplateRequest** | [**CreateJobTemplateRequest**](CreateJobTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateJobTemplateResponse**](CreateJobTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPreset

> CreatePresetResponse createPreset(createPresetRequest, opts)



Create a new preset. For information about job templates see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let createPresetRequest = new AwsElementalMediaConvert.CreatePresetRequest(); // CreatePresetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPreset(createPresetRequest, opts, (error, data, response) => {
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
 **createPresetRequest** | [**CreatePresetRequest**](CreatePresetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePresetResponse**](CreatePresetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createQueue

> CreateQueueResponse createQueue(createQueueRequest, opts)



Create a new transcoding queue. For information about queues, see Working With Queues in the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let createQueueRequest = new AwsElementalMediaConvert.CreateQueueRequest(); // CreateQueueRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createQueue(createQueueRequest, opts, (error, data, response) => {
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
 **createQueueRequest** | [**CreateQueueRequest**](CreateQueueRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateQueueResponse**](CreateQueueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteJobTemplate

> Object deleteJobTemplate(name, opts)



Permanently delete a job template you have created.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the job template to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteJobTemplate(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the job template to be deleted. | 
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


## deletePolicy

> Object deletePolicy(opts)



Permanently delete a policy that you created.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePolicy(opts, (error, data, response) => {
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

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePreset

> Object deletePreset(name, opts)



Permanently delete a preset you have created.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the preset to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePreset(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the preset to be deleted. | 
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


## deleteQueue

> Object deleteQueue(name, opts)



Permanently delete a queue you have created.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the queue that you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteQueue(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the queue that you want to delete. | 
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


## describeEndpoints

> DescribeEndpointsResponse describeEndpoints(describeEndpointsRequest, opts)



Send an request with an empty body to the regional API endpoint to get your account API endpoint.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let describeEndpointsRequest = new AwsElementalMediaConvert.DescribeEndpointsRequest(); // DescribeEndpointsRequest | 
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
apiInstance.describeEndpoints(describeEndpointsRequest, opts, (error, data, response) => {
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
 **describeEndpointsRequest** | [**DescribeEndpointsRequest**](DescribeEndpointsRequest.md)|  | 
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

[**DescribeEndpointsResponse**](DescribeEndpointsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateCertificate

> Object disassociateCertificate(arn, opts)



Removes an association between the Amazon Resource Name (ARN) of an AWS Certificate Manager (ACM) certificate and an AWS Elemental MediaConvert resource.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let arn = "arn_example"; // String | The ARN of the ACM certificate that you want to disassociate from your MediaConvert resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateCertificate(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The ARN of the ACM certificate that you want to disassociate from your MediaConvert resource. | 
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


## getJob

> GetJobResponse getJob(id, opts)



Retrieve the JSON for a specific completed transcoding job.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let id = "id_example"; // String | the job ID of the job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getJob(id, opts, (error, data, response) => {
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
 **id** | **String**| the job ID of the job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetJobResponse**](GetJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJobTemplate

> GetJobTemplateResponse getJobTemplate(name, opts)



Retrieve the JSON for a specific job template.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the job template.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getJobTemplate(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the job template. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetJobTemplateResponse**](GetJobTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPolicy

> GetPolicyResponse getPolicy(opts)



Retrieve the JSON for your policy.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPolicy(opts, (error, data, response) => {
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

[**GetPolicyResponse**](GetPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPreset

> GetPresetResponse getPreset(name, opts)



Retrieve the JSON for a specific preset.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the preset.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPreset(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the preset. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPresetResponse**](GetPresetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQueue

> GetQueueResponse getQueue(name, opts)



Retrieve the JSON for a specific queue.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the queue that you want information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getQueue(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the queue that you want information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetQueueResponse**](GetQueueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listJobTemplates

> ListJobTemplatesResponse listJobTemplates(opts)



Retrieve a JSON array of up to twenty of your job templates. This will return the templates themselves, not just a list of them. To retrieve the next twenty templates, use the nextToken string returned with the array

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'category': "category_example", // String | Optionally, specify a job template category to limit responses to only job templates from that category.
  'listBy': "listBy_example", // String | Optional. When you request a list of job templates, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name.
  'maxResults': 56, // Number | Optional. Number of job templates, up to twenty, that will be returned at one time.
  'nextToken': "nextToken_example", // String | Use this string, provided with the response to a previous request, to request the next batch of job templates.
  'order': "order_example", // String | Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listJobTemplates(opts, (error, data, response) => {
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
 **category** | **String**| Optionally, specify a job template category to limit responses to only job templates from that category. | [optional] 
 **listBy** | **String**| Optional. When you request a list of job templates, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don&#39;t specify, the service will list them by name. | [optional] 
 **maxResults** | **Number**| Optional. Number of job templates, up to twenty, that will be returned at one time. | [optional] 
 **nextToken** | **String**| Use this string, provided with the response to a previous request, to request the next batch of job templates. | [optional] 
 **order** | **String**| Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListJobTemplatesResponse**](ListJobTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listJobs

> ListJobsResponse listJobs(opts)



Retrieve a JSON array of up to twenty of your most recently created jobs. This array includes in-process, completed, and errored jobs. This will return the jobs themselves, not just a list of the jobs. To retrieve the twenty next most recent jobs, use the nextToken string returned with the array.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Optional. Number of jobs, up to twenty, that will be returned at one time.
  'nextToken': "nextToken_example", // String | Optional. Use this string, provided with the response to a previous request, to request the next batch of jobs.
  'order': "order_example", // String | Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
  'queue': "queue_example", // String | Optional. Provide a queue name to get back only jobs from that queue.
  'status': "status_example", // String | Optional. A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listJobs(opts, (error, data, response) => {
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
 **maxResults** | **Number**| Optional. Number of jobs, up to twenty, that will be returned at one time. | [optional] 
 **nextToken** | **String**| Optional. Use this string, provided with the response to a previous request, to request the next batch of jobs. | [optional] 
 **order** | **String**| Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource. | [optional] 
 **queue** | **String**| Optional. Provide a queue name to get back only jobs from that queue. | [optional] 
 **status** | **String**| Optional. A job&#39;s status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListJobsResponse**](ListJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPresets

> ListPresetsResponse listPresets(opts)



Retrieve a JSON array of up to twenty of your presets. This will return the presets themselves, not just a list of them. To retrieve the next twenty presets, use the nextToken string returned with the array.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'category': "category_example", // String | Optionally, specify a preset category to limit responses to only presets from that category.
  'listBy': "listBy_example", // String | Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name.
  'maxResults': 56, // Number | Optional. Number of presets, up to twenty, that will be returned at one time
  'nextToken': "nextToken_example", // String | Use this string, provided with the response to a previous request, to request the next batch of presets.
  'order': "order_example", // String | Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listPresets(opts, (error, data, response) => {
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
 **category** | **String**| Optionally, specify a preset category to limit responses to only presets from that category. | [optional] 
 **listBy** | **String**| Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don&#39;t specify, the service will list them by name. | [optional] 
 **maxResults** | **Number**| Optional. Number of presets, up to twenty, that will be returned at one time | [optional] 
 **nextToken** | **String**| Use this string, provided with the response to a previous request, to request the next batch of presets. | [optional] 
 **order** | **String**| Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListPresetsResponse**](ListPresetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listQueues

> ListQueuesResponse listQueues(opts)



Retrieve a JSON array of up to twenty of your queues. This will return the queues themselves, not just a list of them. To retrieve the next twenty queues, use the nextToken string returned with the array.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'listBy': "listBy_example", // String | Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by creation date.
  'maxResults': 56, // Number | Optional. Number of queues, up to twenty, that will be returned at one time.
  'nextToken': "nextToken_example", // String | Use this string, provided with the response to a previous request, to request the next batch of queues.
  'order': "order_example", // String | Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listQueues(opts, (error, data, response) => {
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
 **listBy** | **String**| Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don&#39;t specify, the service will list them by creation date. | [optional] 
 **maxResults** | **Number**| Optional. Number of queues, up to twenty, that will be returned at one time. | [optional] 
 **nextToken** | **String**| Use this string, provided with the response to a previous request, to request the next batch of queues. | [optional] 
 **order** | **String**| Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListQueuesResponse**](ListQueuesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(arn, opts)



Retrieve the tags for a MediaConvert resource.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let arn = "arn_example"; // String | The Amazon Resource Name (ARN) of the resource that you want to list tags for. To get the ARN, send a GET request with the resource name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The Amazon Resource Name (ARN) of the resource that you want to list tags for. To get the ARN, send a GET request with the resource name. | 
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


## putPolicy

> PutPolicyResponse putPolicy(putPolicyRequest, opts)



Create or change your policy. For more information about policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let putPolicyRequest = new AwsElementalMediaConvert.PutPolicyRequest(); // PutPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putPolicy(putPolicyRequest, opts, (error, data, response) => {
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
 **putPolicyRequest** | [**PutPolicyRequest**](PutPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutPolicyResponse**](PutPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(tagResourceRequest, opts)



Add tags to a MediaConvert queue, preset, or job template. For information about tagging, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-resources.html

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let tagResourceRequest = new AwsElementalMediaConvert.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(tagResourceRequest, opts, (error, data, response) => {
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

> Object untagResource(arn, untagResourceRequest, opts)



Remove tags from a MediaConvert queue, preset, or job template. For information about tagging, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-resources.html

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let arn = "arn_example"; // String | The Amazon Resource Name (ARN) of the resource that you want to remove tags from. To get the ARN, send a GET request with the resource name.
let untagResourceRequest = new AwsElementalMediaConvert.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(arn, untagResourceRequest, opts, (error, data, response) => {
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
 **arn** | **String**| The Amazon Resource Name (ARN) of the resource that you want to remove tags from. To get the ARN, send a GET request with the resource name. | 
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


## updateJobTemplate

> UpdateJobTemplateResponse updateJobTemplate(name, updateJobTemplateRequest, opts)



Modify one of your existing job templates.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the job template you are modifying
let updateJobTemplateRequest = new AwsElementalMediaConvert.UpdateJobTemplateRequest(); // UpdateJobTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateJobTemplate(name, updateJobTemplateRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the job template you are modifying | 
 **updateJobTemplateRequest** | [**UpdateJobTemplateRequest**](UpdateJobTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateJobTemplateResponse**](UpdateJobTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePreset

> UpdatePresetResponse updatePreset(name, updatePresetRequest, opts)



Modify one of your existing presets.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the preset you are modifying.
let updatePresetRequest = new AwsElementalMediaConvert.UpdatePresetRequest(); // UpdatePresetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePreset(name, updatePresetRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the preset you are modifying. | 
 **updatePresetRequest** | [**UpdatePresetRequest**](UpdatePresetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePresetResponse**](UpdatePresetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQueue

> UpdateQueueResponse updateQueue(name, updateQueueRequest, opts)



Modify one of your existing queues.

### Example

```javascript
import AwsElementalMediaConvert from 'aws_elemental_media_convert';
let defaultClient = AwsElementalMediaConvert.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaConvert.DefaultApi();
let name = "name_example"; // String | The name of the queue that you are modifying.
let updateQueueRequest = new AwsElementalMediaConvert.UpdateQueueRequest(); // UpdateQueueRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateQueue(name, updateQueueRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the queue that you are modifying. | 
 **updateQueueRequest** | [**UpdateQueueRequest**](UpdateQueueRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateQueueResponse**](UpdateQueueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

