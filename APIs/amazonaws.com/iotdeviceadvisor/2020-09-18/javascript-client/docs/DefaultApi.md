# AwsIoTCoreDeviceAdvisor.DefaultApi

All URIs are relative to *http://api.iotdeviceadvisor.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSuiteDefinition**](DefaultApi.md#createSuiteDefinition) | **POST** /suiteDefinitions | 
[**deleteSuiteDefinition**](DefaultApi.md#deleteSuiteDefinition) | **DELETE** /suiteDefinitions/{suiteDefinitionId} | 
[**getEndpoint**](DefaultApi.md#getEndpoint) | **GET** /endpoint | 
[**getSuiteDefinition**](DefaultApi.md#getSuiteDefinition) | **GET** /suiteDefinitions/{suiteDefinitionId} | 
[**getSuiteRun**](DefaultApi.md#getSuiteRun) | **GET** /suiteDefinitions/{suiteDefinitionId}/suiteRuns/{suiteRunId} | 
[**getSuiteRunReport**](DefaultApi.md#getSuiteRunReport) | **GET** /suiteDefinitions/{suiteDefinitionId}/suiteRuns/{suiteRunId}/report | 
[**listSuiteDefinitions**](DefaultApi.md#listSuiteDefinitions) | **GET** /suiteDefinitions | 
[**listSuiteRuns**](DefaultApi.md#listSuiteRuns) | **GET** /suiteRuns | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**startSuiteRun**](DefaultApi.md#startSuiteRun) | **POST** /suiteDefinitions/{suiteDefinitionId}/suiteRuns | 
[**stopSuiteRun**](DefaultApi.md#stopSuiteRun) | **POST** /suiteDefinitions/{suiteDefinitionId}/suiteRuns/{suiteRunId}/stop | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateSuiteDefinition**](DefaultApi.md#updateSuiteDefinition) | **PATCH** /suiteDefinitions/{suiteDefinitionId} | 



## createSuiteDefinition

> CreateSuiteDefinitionResponse createSuiteDefinition(createSuiteDefinitionRequest, opts)



&lt;p&gt;Creates a Device Advisor test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;CreateSuiteDefinition&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let createSuiteDefinitionRequest = new AwsIoTCoreDeviceAdvisor.CreateSuiteDefinitionRequest(); // CreateSuiteDefinitionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSuiteDefinition(createSuiteDefinitionRequest, opts, (error, data, response) => {
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
 **createSuiteDefinitionRequest** | [**CreateSuiteDefinitionRequest**](CreateSuiteDefinitionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSuiteDefinitionResponse**](CreateSuiteDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSuiteDefinition

> Object deleteSuiteDefinition(suiteDefinitionId, opts)



&lt;p&gt;Deletes a Device Advisor test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;DeleteSuiteDefinition&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let suiteDefinitionId = "suiteDefinitionId_example"; // String | Suite definition ID of the test suite to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSuiteDefinition(suiteDefinitionId, opts, (error, data, response) => {
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
 **suiteDefinitionId** | **String**| Suite definition ID of the test suite to be deleted. | 
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


## getEndpoint

> GetEndpointResponse getEndpoint(opts)



Gets information about an Device Advisor endpoint.

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'thingArn': "thingArn_example", // String | The thing ARN of the device. This is an optional parameter.
  'certificateArn': "certificateArn_example", // String | The certificate ARN of the device. This is an optional parameter.
  'deviceRoleArn': "deviceRoleArn_example", // String | The device role ARN of the device. This is an optional parameter.
  'authenticationMethod': "authenticationMethod_example" // String | The authentication method used during the device connection.
};
apiInstance.getEndpoint(opts, (error, data, response) => {
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
 **thingArn** | **String**| The thing ARN of the device. This is an optional parameter. | [optional] 
 **certificateArn** | **String**| The certificate ARN of the device. This is an optional parameter. | [optional] 
 **deviceRoleArn** | **String**| The device role ARN of the device. This is an optional parameter. | [optional] 
 **authenticationMethod** | **String**| The authentication method used during the device connection. | [optional] 

### Return type

[**GetEndpointResponse**](GetEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSuiteDefinition

> GetSuiteDefinitionResponse getSuiteDefinition(suiteDefinitionId, opts)



&lt;p&gt;Gets information about a Device Advisor test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetSuiteDefinition&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let suiteDefinitionId = "suiteDefinitionId_example"; // String | Suite definition ID of the test suite to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'suiteDefinitionVersion': "suiteDefinitionVersion_example" // String | Suite definition version of the test suite to get.
};
apiInstance.getSuiteDefinition(suiteDefinitionId, opts, (error, data, response) => {
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
 **suiteDefinitionId** | **String**| Suite definition ID of the test suite to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **suiteDefinitionVersion** | **String**| Suite definition version of the test suite to get. | [optional] 

### Return type

[**GetSuiteDefinitionResponse**](GetSuiteDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSuiteRun

> GetSuiteRunResponse getSuiteRun(suiteDefinitionId, suiteRunId, opts)



&lt;p&gt;Gets information about a Device Advisor test suite run.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetSuiteRun&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let suiteDefinitionId = "suiteDefinitionId_example"; // String | Suite definition ID for the test suite run.
let suiteRunId = "suiteRunId_example"; // String | Suite run ID for the test suite run.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSuiteRun(suiteDefinitionId, suiteRunId, opts, (error, data, response) => {
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
 **suiteDefinitionId** | **String**| Suite definition ID for the test suite run. | 
 **suiteRunId** | **String**| Suite run ID for the test suite run. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSuiteRunResponse**](GetSuiteRunResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSuiteRunReport

> GetSuiteRunReportResponse getSuiteRunReport(suiteDefinitionId, suiteRunId, opts)



&lt;p&gt;Gets a report download link for a successful Device Advisor qualifying test suite run.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetSuiteRunReport&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let suiteDefinitionId = "suiteDefinitionId_example"; // String | Suite definition ID of the test suite.
let suiteRunId = "suiteRunId_example"; // String | Suite run ID of the test suite run.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSuiteRunReport(suiteDefinitionId, suiteRunId, opts, (error, data, response) => {
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
 **suiteDefinitionId** | **String**| Suite definition ID of the test suite. | 
 **suiteRunId** | **String**| Suite run ID of the test suite run. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSuiteRunReportResponse**](GetSuiteRunReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSuiteDefinitions

> ListSuiteDefinitionsResponse listSuiteDefinitions(opts)



&lt;p&gt;Lists the Device Advisor test suites you have created.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListSuiteDefinitions&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return at once.
  'nextToken': "nextToken_example" // String | A token used to get the next set of results.
};
apiInstance.listSuiteDefinitions(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to return at once. | [optional] 
 **nextToken** | **String**| A token used to get the next set of results. | [optional] 

### Return type

[**ListSuiteDefinitionsResponse**](ListSuiteDefinitionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSuiteRuns

> ListSuiteRunsResponse listSuiteRuns(opts)



&lt;p&gt;Lists runs of the specified Device Advisor test suite. You can list all runs of the test suite, or the runs of a specific version of the test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListSuiteRuns&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'suiteDefinitionId': "suiteDefinitionId_example", // String | Lists the test suite runs of the specified test suite based on suite definition ID.
  'suiteDefinitionVersion': "suiteDefinitionVersion_example", // String | Must be passed along with <code>suiteDefinitionId</code>. Lists the test suite runs of the specified test suite based on suite definition version.
  'maxResults': 56, // Number | The maximum number of results to return at once.
  'nextToken': "nextToken_example" // String | A token to retrieve the next set of results.
};
apiInstance.listSuiteRuns(opts, (error, data, response) => {
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
 **suiteDefinitionId** | **String**| Lists the test suite runs of the specified test suite based on suite definition ID. | [optional] 
 **suiteDefinitionVersion** | **String**| Must be passed along with &lt;code&gt;suiteDefinitionId&lt;/code&gt;. Lists the test suite runs of the specified test suite based on suite definition version. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return at once. | [optional] 
 **nextToken** | **String**| A token to retrieve the next set of results. | [optional] 

### Return type

[**ListSuiteRunsResponse**](ListSuiteRunsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



&lt;p&gt;Lists the tags attached to an IoT Device Advisor resource.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListTagsForResource&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource ARN of the IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.
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
 **resourceArn** | **String**| The resource ARN of the IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN. | 
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


## startSuiteRun

> StartSuiteRunResponse startSuiteRun(suiteDefinitionId, startSuiteRunRequest, opts)



&lt;p&gt;Starts a Device Advisor test suite run.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;StartSuiteRun&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let suiteDefinitionId = "suiteDefinitionId_example"; // String | Suite definition ID of the test suite.
let startSuiteRunRequest = new AwsIoTCoreDeviceAdvisor.StartSuiteRunRequest(); // StartSuiteRunRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startSuiteRun(suiteDefinitionId, startSuiteRunRequest, opts, (error, data, response) => {
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
 **suiteDefinitionId** | **String**| Suite definition ID of the test suite. | 
 **startSuiteRunRequest** | [**StartSuiteRunRequest**](StartSuiteRunRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartSuiteRunResponse**](StartSuiteRunResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopSuiteRun

> Object stopSuiteRun(suiteDefinitionId, suiteRunId, opts)



&lt;p&gt;Stops a Device Advisor test suite run that is currently running.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;StopSuiteRun&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let suiteDefinitionId = "suiteDefinitionId_example"; // String | Suite definition ID of the test suite run to be stopped.
let suiteRunId = "suiteRunId_example"; // String | Suite run ID of the test suite run to be stopped.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopSuiteRun(suiteDefinitionId, suiteRunId, opts, (error, data, response) => {
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
 **suiteDefinitionId** | **String**| Suite definition ID of the test suite run to be stopped. | 
 **suiteRunId** | **String**| Suite run ID of the test suite run to be stopped. | 
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


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Adds to and modifies existing tags of an IoT Device Advisor resource.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;TagResource&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.
let tagResourceRequest = new AwsIoTCoreDeviceAdvisor.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN. | 
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



&lt;p&gt;Removes tags from an IoT Device Advisor resource.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;UntagResource&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.
let tagKeys = ["null"]; // [String] | List of tag keys to remove from the IoT Device Advisor resource.
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
 **resourceArn** | **String**| The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN. | 
 **tagKeys** | [**[String]**](String.md)| List of tag keys to remove from the IoT Device Advisor resource. | 
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


## updateSuiteDefinition

> UpdateSuiteDefinitionResponse updateSuiteDefinition(suiteDefinitionId, updateSuiteDefinitionRequest, opts)



&lt;p&gt;Updates a Device Advisor test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;UpdateSuiteDefinition&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTCoreDeviceAdvisor from 'aws_io_t_core_device_advisor';
let defaultClient = AwsIoTCoreDeviceAdvisor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTCoreDeviceAdvisor.DefaultApi();
let suiteDefinitionId = "suiteDefinitionId_example"; // String | Suite definition ID of the test suite to be updated.
let updateSuiteDefinitionRequest = new AwsIoTCoreDeviceAdvisor.UpdateSuiteDefinitionRequest(); // UpdateSuiteDefinitionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSuiteDefinition(suiteDefinitionId, updateSuiteDefinitionRequest, opts, (error, data, response) => {
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
 **suiteDefinitionId** | **String**| Suite definition ID of the test suite to be updated. | 
 **updateSuiteDefinitionRequest** | [**UpdateSuiteDefinitionRequest**](UpdateSuiteDefinitionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSuiteDefinitionResponse**](UpdateSuiteDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

