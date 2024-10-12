# AwsServerlessApplicationRepository.DefaultApi

All URIs are relative to *http://serverlessrepo.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApplication**](DefaultApi.md#createApplication) | **POST** /applications | 
[**createApplicationVersion**](DefaultApi.md#createApplicationVersion) | **PUT** /applications/{applicationId}/versions/{semanticVersion} | 
[**createCloudFormationChangeSet**](DefaultApi.md#createCloudFormationChangeSet) | **POST** /applications/{applicationId}/changesets | 
[**createCloudFormationTemplate**](DefaultApi.md#createCloudFormationTemplate) | **POST** /applications/{applicationId}/templates | 
[**deleteApplication**](DefaultApi.md#deleteApplication) | **DELETE** /applications/{applicationId} | 
[**getApplication**](DefaultApi.md#getApplication) | **GET** /applications/{applicationId} | 
[**getApplicationPolicy**](DefaultApi.md#getApplicationPolicy) | **GET** /applications/{applicationId}/policy | 
[**getCloudFormationTemplate**](DefaultApi.md#getCloudFormationTemplate) | **GET** /applications/{applicationId}/templates/{templateId} | 
[**listApplicationDependencies**](DefaultApi.md#listApplicationDependencies) | **GET** /applications/{applicationId}/dependencies | 
[**listApplicationVersions**](DefaultApi.md#listApplicationVersions) | **GET** /applications/{applicationId}/versions | 
[**listApplications**](DefaultApi.md#listApplications) | **GET** /applications | 
[**putApplicationPolicy**](DefaultApi.md#putApplicationPolicy) | **PUT** /applications/{applicationId}/policy | 
[**unshareApplication**](DefaultApi.md#unshareApplication) | **POST** /applications/{applicationId}/unshare | 
[**updateApplication**](DefaultApi.md#updateApplication) | **PATCH** /applications/{applicationId} | 



## createApplication

> CreateApplicationResponse createApplication(createApplicationRequest, opts)



Creates an application, optionally including an AWS SAM file to create the first application version in the same call.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let createApplicationRequest = new AwsServerlessApplicationRepository.CreateApplicationRequest(); // CreateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApplication(createApplicationRequest, opts, (error, data, response) => {
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
 **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createApplicationVersion

> CreateApplicationVersionResponse createApplicationVersion(applicationId, semanticVersion, createApplicationVersionRequest, opts)



Creates an application version.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let semanticVersion = "semanticVersion_example"; // String | The semantic version of the new version.
let createApplicationVersionRequest = new AwsServerlessApplicationRepository.CreateApplicationVersionRequest(); // CreateApplicationVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApplicationVersion(applicationId, semanticVersion, createApplicationVersionRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **semanticVersion** | **String**| The semantic version of the new version. | 
 **createApplicationVersionRequest** | [**CreateApplicationVersionRequest**](CreateApplicationVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateApplicationVersionResponse**](CreateApplicationVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCloudFormationChangeSet

> CreateCloudFormationChangeSetResponse createCloudFormationChangeSet(applicationId, createCloudFormationChangeSetRequest, opts)



Creates an AWS CloudFormation change set for the given application.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let createCloudFormationChangeSetRequest = new AwsServerlessApplicationRepository.CreateCloudFormationChangeSetRequest(); // CreateCloudFormationChangeSetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCloudFormationChangeSet(applicationId, createCloudFormationChangeSetRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **createCloudFormationChangeSetRequest** | [**CreateCloudFormationChangeSetRequest**](CreateCloudFormationChangeSetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCloudFormationChangeSetResponse**](CreateCloudFormationChangeSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCloudFormationTemplate

> CreateCloudFormationTemplateResponse createCloudFormationTemplate(applicationId, createCloudFormationTemplateRequest, opts)



Creates an AWS CloudFormation template.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let createCloudFormationTemplateRequest = new AwsServerlessApplicationRepository.CreateCloudFormationTemplateRequest(); // CreateCloudFormationTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCloudFormationTemplate(applicationId, createCloudFormationTemplateRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **createCloudFormationTemplateRequest** | [**CreateCloudFormationTemplateRequest**](CreateCloudFormationTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCloudFormationTemplateResponse**](CreateCloudFormationTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplication

> deleteApplication(applicationId, opts)



Deletes the specified application.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplication(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
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


## getApplication

> GetApplicationResponse getApplication(applicationId, opts)



Gets the specified application.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'semanticVersion': "semanticVersion_example" // String | The semantic version of the application to get.
};
apiInstance.getApplication(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **semanticVersion** | **String**| The semantic version of the application to get. | [optional] 

### Return type

[**GetApplicationResponse**](GetApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationPolicy

> GetApplicationPolicyResponse getApplicationPolicy(applicationId, opts)



Retrieves the policy for the application.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApplicationPolicy(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApplicationPolicyResponse**](GetApplicationPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCloudFormationTemplate

> GetCloudFormationTemplateResponse getCloudFormationTemplate(applicationId, templateId, opts)



Gets the specified AWS CloudFormation template.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let templateId = "templateId_example"; // String | <p>The UUID returned by CreateCloudFormationTemplate.</p><p>Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCloudFormationTemplate(applicationId, templateId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **templateId** | **String**| &lt;p&gt;The UUID returned by CreateCloudFormationTemplate.&lt;/p&gt;&lt;p&gt;Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCloudFormationTemplateResponse**](GetCloudFormationTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplicationDependencies

> ListApplicationDependenciesResponse listApplicationDependencies(applicationId, opts)



Retrieves the list of applications nested in the containing application.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxItems': 56, // Number | The total number of items to return.
  'nextToken': "nextToken_example", // String | A token to specify where to start paginating.
  'semanticVersion': "semanticVersion_example", // String | The semantic version of the application to get.
  'maxItems2': "maxItems_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listApplicationDependencies(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxItems** | **Number**| The total number of items to return. | [optional] 
 **nextToken** | **String**| A token to specify where to start paginating. | [optional] 
 **semanticVersion** | **String**| The semantic version of the application to get. | [optional] 
 **maxItems2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListApplicationDependenciesResponse**](ListApplicationDependenciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplicationVersions

> ListApplicationVersionsResponse listApplicationVersions(applicationId, opts)



Lists versions for the specified application.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxItems': 56, // Number | The total number of items to return.
  'nextToken': "nextToken_example", // String | A token to specify where to start paginating.
  'maxItems2': "maxItems_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listApplicationVersions(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxItems** | **Number**| The total number of items to return. | [optional] 
 **nextToken** | **String**| A token to specify where to start paginating. | [optional] 
 **maxItems2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListApplicationVersionsResponse**](ListApplicationVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplications

> ListApplicationsResponse listApplications(opts)



Lists applications owned by the requester.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxItems': 56, // Number | The total number of items to return.
  'nextToken': "nextToken_example", // String | A token to specify where to start paginating.
  'maxItems2': "maxItems_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listApplications(opts, (error, data, response) => {
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
 **maxItems** | **Number**| The total number of items to return. | [optional] 
 **nextToken** | **String**| A token to specify where to start paginating. | [optional] 
 **maxItems2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListApplicationsResponse**](ListApplicationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putApplicationPolicy

> PutApplicationPolicyResponse putApplicationPolicy(applicationId, putApplicationPolicyRequest, opts)



Sets the permission policy for an application. For the list of actions supported for this operation, see  &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions\&quot;&gt;Application   Permissions&lt;/a&gt;  .

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let putApplicationPolicyRequest = new AwsServerlessApplicationRepository.PutApplicationPolicyRequest(); // PutApplicationPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putApplicationPolicy(applicationId, putApplicationPolicyRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **putApplicationPolicyRequest** | [**PutApplicationPolicyRequest**](PutApplicationPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutApplicationPolicyResponse**](PutApplicationPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unshareApplication

> unshareApplication(applicationId, unshareApplicationRequest, opts)



&lt;p&gt;Unshares an application from an AWS Organization.&lt;/p&gt;&lt;p&gt;This operation can be called only from the organization&#39;s master account.&lt;/p&gt;

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let unshareApplicationRequest = new AwsServerlessApplicationRepository.UnshareApplicationRequest(); // UnshareApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.unshareApplication(applicationId, unshareApplicationRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **unshareApplicationRequest** | [**UnshareApplicationRequest**](UnshareApplicationRequest.md)|  | 
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


## updateApplication

> UpdateApplicationResponse updateApplication(applicationId, updateApplicationRequest, opts)



Updates the specified application.

### Example

```javascript
import AwsServerlessApplicationRepository from 'aws_serverless_application_repository';
let defaultClient = AwsServerlessApplicationRepository.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsServerlessApplicationRepository.DefaultApi();
let applicationId = "applicationId_example"; // String | The Amazon Resource Name (ARN) of the application.
let updateApplicationRequest = new AwsServerlessApplicationRepository.UpdateApplicationRequest(); // UpdateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApplication(applicationId, updateApplicationRequest, opts, (error, data, response) => {
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
 **applicationId** | **String**| The Amazon Resource Name (ARN) of the application. | 
 **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

