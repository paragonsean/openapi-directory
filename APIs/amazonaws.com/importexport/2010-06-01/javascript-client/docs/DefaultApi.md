# AwsImportExport.DefaultApi

All URIs are relative to *http://importexport.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETCancelJob**](DefaultApi.md#gETCancelJob) | **GET** /#Operation&#x3D;CancelJob&amp;Action&#x3D;CancelJob | 
[**gETCreateJob**](DefaultApi.md#gETCreateJob) | **GET** /#Operation&#x3D;CreateJob&amp;Action&#x3D;CreateJob | 
[**gETGetShippingLabel**](DefaultApi.md#gETGetShippingLabel) | **GET** /#Operation&#x3D;GetShippingLabel&amp;Action&#x3D;GetShippingLabel | 
[**gETGetStatus**](DefaultApi.md#gETGetStatus) | **GET** /#Operation&#x3D;GetStatus&amp;Action&#x3D;GetStatus | 
[**gETListJobs**](DefaultApi.md#gETListJobs) | **GET** /#Operation&#x3D;ListJobs&amp;Action&#x3D;ListJobs | 
[**gETUpdateJob**](DefaultApi.md#gETUpdateJob) | **GET** /#Operation&#x3D;UpdateJob&amp;Action&#x3D;UpdateJob | 
[**pOSTCancelJob**](DefaultApi.md#pOSTCancelJob) | **POST** /#Operation&#x3D;CancelJob&amp;Action&#x3D;CancelJob | 
[**pOSTCreateJob**](DefaultApi.md#pOSTCreateJob) | **POST** /#Operation&#x3D;CreateJob&amp;Action&#x3D;CreateJob | 
[**pOSTGetShippingLabel**](DefaultApi.md#pOSTGetShippingLabel) | **POST** /#Operation&#x3D;GetShippingLabel&amp;Action&#x3D;GetShippingLabel | 
[**pOSTGetStatus**](DefaultApi.md#pOSTGetStatus) | **POST** /#Operation&#x3D;GetStatus&amp;Action&#x3D;GetStatus | 
[**pOSTListJobs**](DefaultApi.md#pOSTListJobs) | **POST** /#Operation&#x3D;ListJobs&amp;Action&#x3D;ListJobs | 
[**pOSTUpdateJob**](DefaultApi.md#pOSTUpdateJob) | **POST** /#Operation&#x3D;UpdateJob&amp;Action&#x3D;UpdateJob | 



## gETCancelJob

> CancelJobOutput gETCancelJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, operation, action, version, opts)



This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let jobId = "jobId_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'aPIVersion': "aPIVersion_example" // String | 
};
apiInstance.gETCancelJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **jobId** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **aPIVersion** | **String**|  | [optional] 

### Return type

[**CancelJobOutput**](CancelJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETCreateJob

> CreateJobOutput gETCreateJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobType, manifest, validateOnly, operation, action, version, opts)



This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let jobType = "jobType_example"; // String | 
let manifest = "manifest_example"; // String | 
let validateOnly = true; // Boolean | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'manifestAddendum': "manifestAddendum_example", // String | 
  'aPIVersion': "aPIVersion_example" // String | 
};
apiInstance.gETCreateJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobType, manifest, validateOnly, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **jobType** | **String**|  | 
 **manifest** | **String**|  | 
 **validateOnly** | **Boolean**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **manifestAddendum** | **String**|  | [optional] 
 **aPIVersion** | **String**|  | [optional] 

### Return type

[**CreateJobOutput**](CreateJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETGetShippingLabel

> GetShippingLabelOutput gETGetShippingLabel(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobIds, operation, action, version, opts)



This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let jobIds = ["null"]; // [String] | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'name': "name_example", // String | 
  'company': "company_example", // String | 
  'phoneNumber': "phoneNumber_example", // String | 
  'country': "country_example", // String | 
  'stateOrProvince': "stateOrProvince_example", // String | 
  'city': "city_example", // String | 
  'postalCode': "postalCode_example", // String | 
  'street1': "street1_example", // String | 
  'street2': "street2_example", // String | 
  'street3': "street3_example", // String | 
  'aPIVersion': "aPIVersion_example" // String | 
};
apiInstance.gETGetShippingLabel(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobIds, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **jobIds** | [**[String]**](String.md)|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **name** | **String**|  | [optional] 
 **company** | **String**|  | [optional] 
 **phoneNumber** | **String**|  | [optional] 
 **country** | **String**|  | [optional] 
 **stateOrProvince** | **String**|  | [optional] 
 **city** | **String**|  | [optional] 
 **postalCode** | **String**|  | [optional] 
 **street1** | **String**|  | [optional] 
 **street2** | **String**|  | [optional] 
 **street3** | **String**|  | [optional] 
 **aPIVersion** | **String**|  | [optional] 

### Return type

[**GetShippingLabelOutput**](GetShippingLabelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETGetStatus

> GetStatusOutput gETGetStatus(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, operation, action, version, opts)



This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let jobId = "jobId_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'aPIVersion': "aPIVersion_example" // String | 
};
apiInstance.gETGetStatus(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **jobId** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **aPIVersion** | **String**|  | [optional] 

### Return type

[**GetStatusOutput**](GetStatusOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETListJobs

> ListJobsOutput gETListJobs(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts)



This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'maxJobs': 56, // Number | 
  'marker': "marker_example", // String | 
  'aPIVersion': "aPIVersion_example" // String | 
};
apiInstance.gETListJobs(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **maxJobs** | **Number**|  | [optional] 
 **marker** | **String**|  | [optional] 
 **aPIVersion** | **String**|  | [optional] 

### Return type

[**ListJobsOutput**](ListJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETUpdateJob

> UpdateJobOutput gETUpdateJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, manifest, jobType, validateOnly, operation, action, version, opts)



You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let jobId = "jobId_example"; // String | 
let manifest = "manifest_example"; // String | 
let jobType = "jobType_example"; // String | 
let validateOnly = true; // Boolean | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'aPIVersion': "aPIVersion_example" // String | 
};
apiInstance.gETUpdateJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, manifest, jobType, validateOnly, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **jobId** | **String**|  | 
 **manifest** | **String**|  | 
 **jobType** | **String**|  | 
 **validateOnly** | **Boolean**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **aPIVersion** | **String**|  | [optional] 

### Return type

[**UpdateJobOutput**](UpdateJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## pOSTCancelJob

> CancelJobOutput pOSTCancelJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts)



This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'cancelJobInput': new AwsImportExport.CancelJobInput() // CancelJobInput | 
};
apiInstance.pOSTCancelJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **cancelJobInput** | [**CancelJobInput**](CancelJobInput.md)|  | [optional] 

### Return type

[**CancelJobOutput**](CancelJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTCreateJob

> CreateJobOutput pOSTCreateJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts)



This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'createJobInput': new AwsImportExport.CreateJobInput() // CreateJobInput | 
};
apiInstance.pOSTCreateJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **createJobInput** | [**CreateJobInput**](CreateJobInput.md)|  | [optional] 

### Return type

[**CreateJobOutput**](CreateJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTGetShippingLabel

> GetShippingLabelOutput pOSTGetShippingLabel(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts)



This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'getShippingLabelInput': new AwsImportExport.GetShippingLabelInput() // GetShippingLabelInput | 
};
apiInstance.pOSTGetShippingLabel(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **getShippingLabelInput** | [**GetShippingLabelInput**](GetShippingLabelInput.md)|  | [optional] 

### Return type

[**GetShippingLabelOutput**](GetShippingLabelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTGetStatus

> GetStatusOutput pOSTGetStatus(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts)



This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'getStatusInput': new AwsImportExport.GetStatusInput() // GetStatusInput | 
};
apiInstance.pOSTGetStatus(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **getStatusInput** | [**GetStatusInput**](GetStatusInput.md)|  | [optional] 

### Return type

[**GetStatusOutput**](GetStatusOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTListJobs

> ListJobsOutput pOSTListJobs(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts)



This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'maxJobs': "maxJobs_example", // String | Pagination limit
  'marker': "marker_example", // String | Pagination token
  'listJobsInput': new AwsImportExport.ListJobsInput() // ListJobsInput | 
};
apiInstance.pOSTListJobs(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **maxJobs** | **String**| Pagination limit | [optional] 
 **marker** | **String**| Pagination token | [optional] 
 **listJobsInput** | [**ListJobsInput**](ListJobsInput.md)|  | [optional] 

### Return type

[**ListJobsOutput**](ListJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTUpdateJob

> UpdateJobOutput pOSTUpdateJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts)



You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

### Example

```javascript
import AwsImportExport from 'aws_import_export';
let defaultClient = AwsImportExport.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsImportExport.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let operation = "operation_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'updateJobInput': new AwsImportExport.UpdateJobInput() // UpdateJobInput | 
};
apiInstance.pOSTUpdateJob(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **operation** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **updateJobInput** | [**UpdateJobInput**](UpdateJobInput.md)|  | [optional] 

### Return type

[**UpdateJobOutput**](UpdateJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml

