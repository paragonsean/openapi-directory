# AwsEntityResolution.DefaultApi

All URIs are relative to *http://entityresolution.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMatchingWorkflow**](DefaultApi.md#createMatchingWorkflow) | **POST** /matchingworkflows | 
[**createSchemaMapping**](DefaultApi.md#createSchemaMapping) | **POST** /schemas | 
[**deleteMatchingWorkflow**](DefaultApi.md#deleteMatchingWorkflow) | **DELETE** /matchingworkflows/{workflowName} | 
[**deleteSchemaMapping**](DefaultApi.md#deleteSchemaMapping) | **DELETE** /schemas/{schemaName} | 
[**getMatchId**](DefaultApi.md#getMatchId) | **POST** /matchingworkflows/{workflowName}/matches | 
[**getMatchingJob**](DefaultApi.md#getMatchingJob) | **GET** /matchingworkflows/{workflowName}/jobs/{jobId} | 
[**getMatchingWorkflow**](DefaultApi.md#getMatchingWorkflow) | **GET** /matchingworkflows/{workflowName} | 
[**getSchemaMapping**](DefaultApi.md#getSchemaMapping) | **GET** /schemas/{schemaName} | 
[**listMatchingJobs**](DefaultApi.md#listMatchingJobs) | **GET** /matchingworkflows/{workflowName}/jobs | 
[**listMatchingWorkflows**](DefaultApi.md#listMatchingWorkflows) | **GET** /matchingworkflows | 
[**listSchemaMappings**](DefaultApi.md#listSchemaMappings) | **GET** /schemas | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**startMatchingJob**](DefaultApi.md#startMatchingJob) | **POST** /matchingworkflows/{workflowName}/jobs | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateMatchingWorkflow**](DefaultApi.md#updateMatchingWorkflow) | **PUT** /matchingworkflows/{workflowName} | 



## createMatchingWorkflow

> CreateMatchingWorkflowOutput createMatchingWorkflow(createMatchingWorkflowRequest, opts)



Creates a &lt;code&gt;MatchingWorkflow&lt;/code&gt; object which stores the configuration of the data processing job to be run. It is important to note that there should not be a pre-existing &lt;code&gt;MatchingWorkflow&lt;/code&gt; with the same name. To modify an existing workflow, utilize the &lt;code&gt;UpdateMatchingWorkflow&lt;/code&gt; API.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let createMatchingWorkflowRequest = new AwsEntityResolution.CreateMatchingWorkflowRequest(); // CreateMatchingWorkflowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMatchingWorkflow(createMatchingWorkflowRequest, opts, (error, data, response) => {
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
 **createMatchingWorkflowRequest** | [**CreateMatchingWorkflowRequest**](CreateMatchingWorkflowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMatchingWorkflowOutput**](CreateMatchingWorkflowOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSchemaMapping

> CreateSchemaMappingOutput createSchemaMapping(createSchemaMappingRequest, opts)



Creates a schema mapping, which defines the schema of the input customer records table. The &lt;code&gt;SchemaMapping&lt;/code&gt; also provides Entity Resolution with some metadata about the table, such as the attribute types of the columns and which columns to match on.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let createSchemaMappingRequest = new AwsEntityResolution.CreateSchemaMappingRequest(); // CreateSchemaMappingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSchemaMapping(createSchemaMappingRequest, opts, (error, data, response) => {
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
 **createSchemaMappingRequest** | [**CreateSchemaMappingRequest**](CreateSchemaMappingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSchemaMappingOutput**](CreateSchemaMappingOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteMatchingWorkflow

> DeleteMatchingWorkflowOutput deleteMatchingWorkflow(workflowName, opts)



Deletes the &lt;code&gt;MatchingWorkflow&lt;/code&gt; with a given name. This operation will succeed even if a workflow with the given name does not exist.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let workflowName = "workflowName_example"; // String | The name of the workflow to be retrieved.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMatchingWorkflow(workflowName, opts, (error, data, response) => {
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
 **workflowName** | **String**| The name of the workflow to be retrieved. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteMatchingWorkflowOutput**](DeleteMatchingWorkflowOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSchemaMapping

> DeleteSchemaMappingOutput deleteSchemaMapping(schemaName, opts)



Deletes the &lt;code&gt;SchemaMapping&lt;/code&gt; with a given name. This operation will succeed even if a schema with the given name does not exist. This operation will fail if there is a &lt;code&gt;DataIntegrationWorkflow&lt;/code&gt; object that references the &lt;code&gt;SchemaMapping&lt;/code&gt; in the workflow&#39;s &lt;code&gt;InputSourceConfig&lt;/code&gt;.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let schemaName = "schemaName_example"; // String | The name of the schema to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSchemaMapping(schemaName, opts, (error, data, response) => {
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
 **schemaName** | **String**| The name of the schema to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteSchemaMappingOutput**](DeleteSchemaMappingOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMatchId

> GetMatchIdOutput getMatchId(workflowName, getMatchIdRequest, opts)



Returns the corresponding Match ID of a customer record if the record has been processed.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let workflowName = "workflowName_example"; // String | The name of the workflow.
let getMatchIdRequest = new AwsEntityResolution.GetMatchIdRequest(); // GetMatchIdRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMatchId(workflowName, getMatchIdRequest, opts, (error, data, response) => {
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
 **workflowName** | **String**| The name of the workflow. | 
 **getMatchIdRequest** | [**GetMatchIdRequest**](GetMatchIdRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMatchIdOutput**](GetMatchIdOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMatchingJob

> GetMatchingJobOutput getMatchingJob(jobId, workflowName, opts)



Gets the status, metrics, and errors (if there are any) that are associated with a job.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let jobId = "jobId_example"; // String | The ID of the job.
let workflowName = "workflowName_example"; // String | The name of the workflow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMatchingJob(jobId, workflowName, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job. | 
 **workflowName** | **String**| The name of the workflow. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMatchingJobOutput**](GetMatchingJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMatchingWorkflow

> GetMatchingWorkflowOutput getMatchingWorkflow(workflowName, opts)



Returns the &lt;code&gt;MatchingWorkflow&lt;/code&gt; with a given name, if it exists.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let workflowName = "workflowName_example"; // String | The name of the workflow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMatchingWorkflow(workflowName, opts, (error, data, response) => {
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
 **workflowName** | **String**| The name of the workflow. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMatchingWorkflowOutput**](GetMatchingWorkflowOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSchemaMapping

> GetSchemaMappingOutput getSchemaMapping(schemaName, opts)



Returns the SchemaMapping of a given name.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let schemaName = "schemaName_example"; // String | The name of the schema to be retrieved.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSchemaMapping(schemaName, opts, (error, data, response) => {
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
 **schemaName** | **String**| The name of the schema to be retrieved. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSchemaMappingOutput**](GetSchemaMappingOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMatchingJobs

> ListMatchingJobsOutput listMatchingJobs(workflowName, opts)



Lists all jobs for a given workflow.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let workflowName = "workflowName_example"; // String | The name of the workflow to be retrieved.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of objects returned per page.
  'nextToken': "nextToken_example" // String | The pagination token from the previous <code>ListSchemaMappings</code> API call.
};
apiInstance.listMatchingJobs(workflowName, opts, (error, data, response) => {
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
 **workflowName** | **String**| The name of the workflow to be retrieved. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 
 **nextToken** | **String**| The pagination token from the previous &lt;code&gt;ListSchemaMappings&lt;/code&gt; API call. | [optional] 

### Return type

[**ListMatchingJobsOutput**](ListMatchingJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMatchingWorkflows

> ListMatchingWorkflowsOutput listMatchingWorkflows(opts)



Returns a list of all the &lt;code&gt;MatchingWorkflows&lt;/code&gt; that have been created for an AWS account.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of objects returned per page.
  'nextToken': "nextToken_example" // String | The pagination token from the previous <code>ListSchemaMappings</code> API call.
};
apiInstance.listMatchingWorkflows(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 
 **nextToken** | **String**| The pagination token from the previous &lt;code&gt;ListSchemaMappings&lt;/code&gt; API call. | [optional] 

### Return type

[**ListMatchingWorkflowsOutput**](ListMatchingWorkflowsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSchemaMappings

> ListSchemaMappingsOutput listSchemaMappings(opts)



Returns a list of all the &lt;code&gt;SchemaMappings&lt;/code&gt; that have been created for an AWS account.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of objects returned per page.
  'nextToken': "nextToken_example" // String | The pagination token from the previous <code>ListSchemaMappings</code> API call.
};
apiInstance.listSchemaMappings(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 
 **nextToken** | **String**| The pagination token from the previous &lt;code&gt;ListSchemaMappings&lt;/code&gt; API call. | [optional] 

### Return type

[**ListSchemaMappingsOutput**](ListSchemaMappingsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(resourceArn, opts)



Displays the tags associated with an AWS Entity Resolution resource. In Entity Resolution, &lt;code&gt;SchemaMapping&lt;/code&gt;, and &lt;code&gt;MatchingWorkflow&lt;/code&gt; can be tagged.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource for which you want to view tags.
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
 **resourceArn** | **String**| The ARN of the resource for which you want to view tags. | 
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


## startMatchingJob

> StartMatchingJobOutput startMatchingJob(workflowName, opts)



Starts the &lt;code&gt;MatchingJob&lt;/code&gt; of a workflow. The workflow must have previously been created using the &lt;code&gt;CreateMatchingWorkflow&lt;/code&gt; endpoint.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let workflowName = "workflowName_example"; // String | The name of the matching job to be retrieved.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startMatchingJob(workflowName, opts, (error, data, response) => {
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
 **workflowName** | **String**| The name of the matching job to be retrieved. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartMatchingJobOutput**](StartMatchingJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Assigns one or more tags (key-value pairs) to the specified AWS Entity Resolution resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In Entity Resolution, &lt;code&gt;SchemaMapping&lt;/code&gt;, and &lt;code&gt;MatchingWorkflow&lt;/code&gt; can be tagged. Tags don&#39;t have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource for which you want to view tags.
let tagResourceRequest = new AwsEntityResolution.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The ARN of the resource for which you want to view tags. | 
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



Removes one or more tags from the specified AWS Entity Resolution resource. In Entity Resolution, &lt;code&gt;SchemaMapping&lt;/code&gt;, and &lt;code&gt;MatchingWorkflow&lt;/code&gt; can be tagged.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource for which you want to untag.
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
 **resourceArn** | **String**| The ARN of the resource for which you want to untag. | 
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


## updateMatchingWorkflow

> UpdateMatchingWorkflowOutput updateMatchingWorkflow(workflowName, updateMatchingWorkflowRequest, opts)



Updates an existing &lt;code&gt;MatchingWorkflow&lt;/code&gt;. This method is identical to &lt;code&gt;CreateMatchingWorkflow&lt;/code&gt;, except it uses an HTTP &lt;code&gt;PUT&lt;/code&gt; request instead of a &lt;code&gt;POST&lt;/code&gt; request, and the &lt;code&gt;MatchingWorkflow&lt;/code&gt; must already exist for the method to succeed.

### Example

```javascript
import AwsEntityResolution from 'aws_entity_resolution';
let defaultClient = AwsEntityResolution.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEntityResolution.DefaultApi();
let workflowName = "workflowName_example"; // String | The name of the workflow to be retrieved.
let updateMatchingWorkflowRequest = new AwsEntityResolution.UpdateMatchingWorkflowRequest(); // UpdateMatchingWorkflowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMatchingWorkflow(workflowName, updateMatchingWorkflowRequest, opts, (error, data, response) => {
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
 **workflowName** | **String**| The name of the workflow to be retrieved. | 
 **updateMatchingWorkflowRequest** | [**UpdateMatchingWorkflowRequest**](UpdateMatchingWorkflowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateMatchingWorkflowOutput**](UpdateMatchingWorkflowOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

