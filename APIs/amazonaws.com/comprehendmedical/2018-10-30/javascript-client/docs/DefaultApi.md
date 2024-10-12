# AwsComprehendMedical.DefaultApi

All URIs are relative to *http://comprehendmedical.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describeEntitiesDetectionV2Job**](DefaultApi.md#describeEntitiesDetectionV2Job) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribeEntitiesDetectionV2Job | 
[**describeICD10CMInferenceJob**](DefaultApi.md#describeICD10CMInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribeICD10CMInferenceJob | 
[**describePHIDetectionJob**](DefaultApi.md#describePHIDetectionJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribePHIDetectionJob | 
[**describeRxNormInferenceJob**](DefaultApi.md#describeRxNormInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribeRxNormInferenceJob | 
[**describeSNOMEDCTInferenceJob**](DefaultApi.md#describeSNOMEDCTInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribeSNOMEDCTInferenceJob | 
[**detectEntities**](DefaultApi.md#detectEntities) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DetectEntities | 
[**detectEntitiesV2**](DefaultApi.md#detectEntitiesV2) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DetectEntitiesV2 | 
[**detectPHI**](DefaultApi.md#detectPHI) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DetectPHI | 
[**inferICD10CM**](DefaultApi.md#inferICD10CM) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.InferICD10CM | 
[**inferRxNorm**](DefaultApi.md#inferRxNorm) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.InferRxNorm | 
[**inferSNOMEDCT**](DefaultApi.md#inferSNOMEDCT) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.InferSNOMEDCT | 
[**listEntitiesDetectionV2Jobs**](DefaultApi.md#listEntitiesDetectionV2Jobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListEntitiesDetectionV2Jobs | 
[**listICD10CMInferenceJobs**](DefaultApi.md#listICD10CMInferenceJobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListICD10CMInferenceJobs | 
[**listPHIDetectionJobs**](DefaultApi.md#listPHIDetectionJobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListPHIDetectionJobs | 
[**listRxNormInferenceJobs**](DefaultApi.md#listRxNormInferenceJobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListRxNormInferenceJobs | 
[**listSNOMEDCTInferenceJobs**](DefaultApi.md#listSNOMEDCTInferenceJobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListSNOMEDCTInferenceJobs | 
[**startEntitiesDetectionV2Job**](DefaultApi.md#startEntitiesDetectionV2Job) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartEntitiesDetectionV2Job | 
[**startICD10CMInferenceJob**](DefaultApi.md#startICD10CMInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartICD10CMInferenceJob | 
[**startPHIDetectionJob**](DefaultApi.md#startPHIDetectionJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartPHIDetectionJob | 
[**startRxNormInferenceJob**](DefaultApi.md#startRxNormInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartRxNormInferenceJob | 
[**startSNOMEDCTInferenceJob**](DefaultApi.md#startSNOMEDCTInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartSNOMEDCTInferenceJob | 
[**stopEntitiesDetectionV2Job**](DefaultApi.md#stopEntitiesDetectionV2Job) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopEntitiesDetectionV2Job | 
[**stopICD10CMInferenceJob**](DefaultApi.md#stopICD10CMInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopICD10CMInferenceJob | 
[**stopPHIDetectionJob**](DefaultApi.md#stopPHIDetectionJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopPHIDetectionJob | 
[**stopRxNormInferenceJob**](DefaultApi.md#stopRxNormInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopRxNormInferenceJob | 
[**stopSNOMEDCTInferenceJob**](DefaultApi.md#stopSNOMEDCTInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopSNOMEDCTInferenceJob | 



## describeEntitiesDetectionV2Job

> DescribeEntitiesDetectionV2JobResponse describeEntitiesDetectionV2Job(xAmzTarget, describeEntitiesDetectionV2JobRequest, opts)



Gets the properties associated with a medical entities detection job. Use this operation to get the status of a detection job.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEntitiesDetectionV2JobRequest = new AwsComprehendMedical.DescribeEntitiesDetectionV2JobRequest(); // DescribeEntitiesDetectionV2JobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeEntitiesDetectionV2Job(xAmzTarget, describeEntitiesDetectionV2JobRequest, opts, (error, data, response) => {
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
 **describeEntitiesDetectionV2JobRequest** | [**DescribeEntitiesDetectionV2JobRequest**](DescribeEntitiesDetectionV2JobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeEntitiesDetectionV2JobResponse**](DescribeEntitiesDetectionV2JobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeICD10CMInferenceJob

> DescribeICD10CMInferenceJobResponse describeICD10CMInferenceJob(xAmzTarget, describeICD10CMInferenceJobRequest, opts)



Gets the properties associated with an InferICD10CM job. Use this operation to get the status of an inference job.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeICD10CMInferenceJobRequest = new AwsComprehendMedical.DescribeICD10CMInferenceJobRequest(); // DescribeICD10CMInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeICD10CMInferenceJob(xAmzTarget, describeICD10CMInferenceJobRequest, opts, (error, data, response) => {
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
 **describeICD10CMInferenceJobRequest** | [**DescribeICD10CMInferenceJobRequest**](DescribeICD10CMInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeICD10CMInferenceJobResponse**](DescribeICD10CMInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describePHIDetectionJob

> DescribePHIDetectionJobResponse describePHIDetectionJob(xAmzTarget, describePHIDetectionJobRequest, opts)



Gets the properties associated with a protected health information (PHI) detection job. Use this operation to get the status of a detection job.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describePHIDetectionJobRequest = new AwsComprehendMedical.DescribePHIDetectionJobRequest(); // DescribePHIDetectionJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describePHIDetectionJob(xAmzTarget, describePHIDetectionJobRequest, opts, (error, data, response) => {
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
 **describePHIDetectionJobRequest** | [**DescribePHIDetectionJobRequest**](DescribePHIDetectionJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribePHIDetectionJobResponse**](DescribePHIDetectionJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeRxNormInferenceJob

> DescribeRxNormInferenceJobResponse describeRxNormInferenceJob(xAmzTarget, describeRxNormInferenceJobRequest, opts)



Gets the properties associated with an InferRxNorm job. Use this operation to get the status of an inference job.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeRxNormInferenceJobRequest = new AwsComprehendMedical.DescribeRxNormInferenceJobRequest(); // DescribeRxNormInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRxNormInferenceJob(xAmzTarget, describeRxNormInferenceJobRequest, opts, (error, data, response) => {
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
 **describeRxNormInferenceJobRequest** | [**DescribeRxNormInferenceJobRequest**](DescribeRxNormInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRxNormInferenceJobResponse**](DescribeRxNormInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeSNOMEDCTInferenceJob

> DescribeSNOMEDCTInferenceJobResponse describeSNOMEDCTInferenceJob(xAmzTarget, describeSNOMEDCTInferenceJobRequest, opts)



 Gets the properties associated with an InferSNOMEDCT job. Use this operation to get the status of an inference job. 

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeSNOMEDCTInferenceJobRequest = new AwsComprehendMedical.DescribeSNOMEDCTInferenceJobRequest(); // DescribeSNOMEDCTInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeSNOMEDCTInferenceJob(xAmzTarget, describeSNOMEDCTInferenceJobRequest, opts, (error, data, response) => {
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
 **describeSNOMEDCTInferenceJobRequest** | [**DescribeSNOMEDCTInferenceJobRequest**](DescribeSNOMEDCTInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeSNOMEDCTInferenceJobResponse**](DescribeSNOMEDCTInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## detectEntities

> DetectEntitiesResponse detectEntities(xAmzTarget, detectEntitiesRequest, opts)



&lt;p&gt;The &lt;code&gt;DetectEntities&lt;/code&gt; operation is deprecated. You should use the &lt;a&gt;DetectEntitiesV2&lt;/a&gt; operation instead.&lt;/p&gt; &lt;p&gt;Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information.&lt;/p&gt;

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let detectEntitiesRequest = new AwsComprehendMedical.DetectEntitiesRequest(); // DetectEntitiesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detectEntities(xAmzTarget, detectEntitiesRequest, opts, (error, data, response) => {
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
 **detectEntitiesRequest** | [**DetectEntitiesRequest**](DetectEntitiesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DetectEntitiesResponse**](DetectEntitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## detectEntitiesV2

> DetectEntitiesV2Response detectEntitiesV2(xAmzTarget, detectEntitiesV2Request, opts)



&lt;p&gt;Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information. Amazon Comprehend Medical only detects medical entities in English language texts.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation replaces the &lt;a&gt;DetectEntities&lt;/a&gt; operation. This new action uses a different model for determining the entities in your medical text and changes the way that some entities are returned in the output. You should use the &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation in all new applications.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation returns the &lt;code&gt;Acuity&lt;/code&gt; and &lt;code&gt;Direction&lt;/code&gt; entities as attributes instead of types. &lt;/p&gt;

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let detectEntitiesV2Request = new AwsComprehendMedical.DetectEntitiesV2Request(); // DetectEntitiesV2Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detectEntitiesV2(xAmzTarget, detectEntitiesV2Request, opts, (error, data, response) => {
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
 **detectEntitiesV2Request** | [**DetectEntitiesV2Request**](DetectEntitiesV2Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DetectEntitiesV2Response**](DetectEntitiesV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## detectPHI

> DetectPHIResponse detectPHI(xAmzTarget, detectPHIRequest, opts)



Inspects the clinical text for protected health information (PHI) entities and returns the entity category, location, and confidence score for each entity. Amazon Comprehend Medical only detects entities in English language texts.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let detectPHIRequest = new AwsComprehendMedical.DetectPHIRequest(); // DetectPHIRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detectPHI(xAmzTarget, detectPHIRequest, opts, (error, data, response) => {
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
 **detectPHIRequest** | [**DetectPHIRequest**](DetectPHIRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DetectPHIResponse**](DetectPHIResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## inferICD10CM

> InferICD10CMResponse inferICD10CM(xAmzTarget, inferICD10CMRequest, opts)



InferICD10CM detects medical conditions as entities listed in a patient record and links those entities to normalized concept identifiers in the ICD-10-CM knowledge base from the Centers for Disease Control. Amazon Comprehend Medical only detects medical entities in English language texts. 

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let inferICD10CMRequest = new AwsComprehendMedical.InferICD10CMRequest(); // InferICD10CMRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.inferICD10CM(xAmzTarget, inferICD10CMRequest, opts, (error, data, response) => {
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
 **inferICD10CMRequest** | [**InferICD10CMRequest**](InferICD10CMRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**InferICD10CMResponse**](InferICD10CMResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## inferRxNorm

> InferRxNormResponse inferRxNorm(xAmzTarget, inferRxNormRequest, opts)



InferRxNorm detects medications as entities listed in a patient record and links to the normalized concept identifiers in the RxNorm database from the National Library of Medicine. Amazon Comprehend Medical only detects medical entities in English language texts. 

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let inferRxNormRequest = new AwsComprehendMedical.InferRxNormRequest(); // InferRxNormRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.inferRxNorm(xAmzTarget, inferRxNormRequest, opts, (error, data, response) => {
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
 **inferRxNormRequest** | [**InferRxNormRequest**](InferRxNormRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**InferRxNormResponse**](InferRxNormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## inferSNOMEDCT

> InferSNOMEDCTResponse inferSNOMEDCT(xAmzTarget, inferSNOMEDCTRequest, opts)



 InferSNOMEDCT detects possible medical concepts as entities and links them to codes from the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED-CT) ontology

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let inferSNOMEDCTRequest = new AwsComprehendMedical.InferSNOMEDCTRequest(); // InferSNOMEDCTRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.inferSNOMEDCT(xAmzTarget, inferSNOMEDCTRequest, opts, (error, data, response) => {
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
 **inferSNOMEDCTRequest** | [**InferSNOMEDCTRequest**](InferSNOMEDCTRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**InferSNOMEDCTResponse**](InferSNOMEDCTResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEntitiesDetectionV2Jobs

> ListEntitiesDetectionV2JobsResponse listEntitiesDetectionV2Jobs(xAmzTarget, listEntitiesDetectionV2JobsRequest, opts)



Gets a list of medical entity detection jobs that you have submitted.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listEntitiesDetectionV2JobsRequest = new AwsComprehendMedical.ListEntitiesDetectionV2JobsRequest(); // ListEntitiesDetectionV2JobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listEntitiesDetectionV2Jobs(xAmzTarget, listEntitiesDetectionV2JobsRequest, opts, (error, data, response) => {
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
 **listEntitiesDetectionV2JobsRequest** | [**ListEntitiesDetectionV2JobsRequest**](ListEntitiesDetectionV2JobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListEntitiesDetectionV2JobsResponse**](ListEntitiesDetectionV2JobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listICD10CMInferenceJobs

> ListICD10CMInferenceJobsResponse listICD10CMInferenceJobs(xAmzTarget, listICD10CMInferenceJobsRequest, opts)



Gets a list of InferICD10CM jobs that you have submitted.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listICD10CMInferenceJobsRequest = new AwsComprehendMedical.ListICD10CMInferenceJobsRequest(); // ListICD10CMInferenceJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listICD10CMInferenceJobs(xAmzTarget, listICD10CMInferenceJobsRequest, opts, (error, data, response) => {
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
 **listICD10CMInferenceJobsRequest** | [**ListICD10CMInferenceJobsRequest**](ListICD10CMInferenceJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListICD10CMInferenceJobsResponse**](ListICD10CMInferenceJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPHIDetectionJobs

> ListPHIDetectionJobsResponse listPHIDetectionJobs(xAmzTarget, listPHIDetectionJobsRequest, opts)



Gets a list of protected health information (PHI) detection jobs you have submitted.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPHIDetectionJobsRequest = new AwsComprehendMedical.ListPHIDetectionJobsRequest(); // ListPHIDetectionJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listPHIDetectionJobs(xAmzTarget, listPHIDetectionJobsRequest, opts, (error, data, response) => {
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
 **listPHIDetectionJobsRequest** | [**ListPHIDetectionJobsRequest**](ListPHIDetectionJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListPHIDetectionJobsResponse**](ListPHIDetectionJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRxNormInferenceJobs

> ListRxNormInferenceJobsResponse listRxNormInferenceJobs(xAmzTarget, listRxNormInferenceJobsRequest, opts)



Gets a list of InferRxNorm jobs that you have submitted.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listRxNormInferenceJobsRequest = new AwsComprehendMedical.ListRxNormInferenceJobsRequest(); // ListRxNormInferenceJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listRxNormInferenceJobs(xAmzTarget, listRxNormInferenceJobsRequest, opts, (error, data, response) => {
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
 **listRxNormInferenceJobsRequest** | [**ListRxNormInferenceJobsRequest**](ListRxNormInferenceJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListRxNormInferenceJobsResponse**](ListRxNormInferenceJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSNOMEDCTInferenceJobs

> ListSNOMEDCTInferenceJobsResponse listSNOMEDCTInferenceJobs(xAmzTarget, listSNOMEDCTInferenceJobsRequest, opts)



 Gets a list of InferSNOMEDCT jobs a user has submitted. 

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listSNOMEDCTInferenceJobsRequest = new AwsComprehendMedical.ListSNOMEDCTInferenceJobsRequest(); // ListSNOMEDCTInferenceJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listSNOMEDCTInferenceJobs(xAmzTarget, listSNOMEDCTInferenceJobsRequest, opts, (error, data, response) => {
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
 **listSNOMEDCTInferenceJobsRequest** | [**ListSNOMEDCTInferenceJobsRequest**](ListSNOMEDCTInferenceJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListSNOMEDCTInferenceJobsResponse**](ListSNOMEDCTInferenceJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startEntitiesDetectionV2Job

> StartEntitiesDetectionV2JobResponse startEntitiesDetectionV2Job(xAmzTarget, startEntitiesDetectionV2JobRequest, opts)



Starts an asynchronous medical entity detection job for a collection of documents. Use the &lt;code&gt;DescribeEntitiesDetectionV2Job&lt;/code&gt; operation to track the status of a job.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startEntitiesDetectionV2JobRequest = new AwsComprehendMedical.StartEntitiesDetectionV2JobRequest(); // StartEntitiesDetectionV2JobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startEntitiesDetectionV2Job(xAmzTarget, startEntitiesDetectionV2JobRequest, opts, (error, data, response) => {
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
 **startEntitiesDetectionV2JobRequest** | [**StartEntitiesDetectionV2JobRequest**](StartEntitiesDetectionV2JobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartEntitiesDetectionV2JobResponse**](StartEntitiesDetectionV2JobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startICD10CMInferenceJob

> StartICD10CMInferenceJobResponse startICD10CMInferenceJob(xAmzTarget, startICD10CMInferenceJobRequest, opts)



Starts an asynchronous job to detect medical conditions and link them to the ICD-10-CM ontology. Use the &lt;code&gt;DescribeICD10CMInferenceJob&lt;/code&gt; operation to track the status of a job.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startICD10CMInferenceJobRequest = new AwsComprehendMedical.StartICD10CMInferenceJobRequest(); // StartICD10CMInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startICD10CMInferenceJob(xAmzTarget, startICD10CMInferenceJobRequest, opts, (error, data, response) => {
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
 **startICD10CMInferenceJobRequest** | [**StartICD10CMInferenceJobRequest**](StartICD10CMInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartICD10CMInferenceJobResponse**](StartICD10CMInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startPHIDetectionJob

> StartPHIDetectionJobResponse startPHIDetectionJob(xAmzTarget, startPHIDetectionJobRequest, opts)



Starts an asynchronous job to detect protected health information (PHI). Use the &lt;code&gt;DescribePHIDetectionJob&lt;/code&gt; operation to track the status of a job.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startPHIDetectionJobRequest = new AwsComprehendMedical.StartPHIDetectionJobRequest(); // StartPHIDetectionJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startPHIDetectionJob(xAmzTarget, startPHIDetectionJobRequest, opts, (error, data, response) => {
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
 **startPHIDetectionJobRequest** | [**StartPHIDetectionJobRequest**](StartPHIDetectionJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartPHIDetectionJobResponse**](StartPHIDetectionJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startRxNormInferenceJob

> StartRxNormInferenceJobResponse startRxNormInferenceJob(xAmzTarget, startRxNormInferenceJobRequest, opts)



Starts an asynchronous job to detect medication entities and link them to the RxNorm ontology. Use the &lt;code&gt;DescribeRxNormInferenceJob&lt;/code&gt; operation to track the status of a job.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startRxNormInferenceJobRequest = new AwsComprehendMedical.StartRxNormInferenceJobRequest(); // StartRxNormInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startRxNormInferenceJob(xAmzTarget, startRxNormInferenceJobRequest, opts, (error, data, response) => {
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
 **startRxNormInferenceJobRequest** | [**StartRxNormInferenceJobRequest**](StartRxNormInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartRxNormInferenceJobResponse**](StartRxNormInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startSNOMEDCTInferenceJob

> StartSNOMEDCTInferenceJobResponse startSNOMEDCTInferenceJob(xAmzTarget, startSNOMEDCTInferenceJobRequest, opts)



 Starts an asynchronous job to detect medical concepts and link them to the SNOMED-CT ontology. Use the DescribeSNOMEDCTInferenceJob operation to track the status of a job. 

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startSNOMEDCTInferenceJobRequest = new AwsComprehendMedical.StartSNOMEDCTInferenceJobRequest(); // StartSNOMEDCTInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startSNOMEDCTInferenceJob(xAmzTarget, startSNOMEDCTInferenceJobRequest, opts, (error, data, response) => {
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
 **startSNOMEDCTInferenceJobRequest** | [**StartSNOMEDCTInferenceJobRequest**](StartSNOMEDCTInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartSNOMEDCTInferenceJobResponse**](StartSNOMEDCTInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopEntitiesDetectionV2Job

> StopEntitiesDetectionV2JobResponse stopEntitiesDetectionV2Job(xAmzTarget, stopEntitiesDetectionV2JobRequest, opts)



Stops a medical entities detection job in progress.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopEntitiesDetectionV2JobRequest = new AwsComprehendMedical.StopEntitiesDetectionV2JobRequest(); // StopEntitiesDetectionV2JobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopEntitiesDetectionV2Job(xAmzTarget, stopEntitiesDetectionV2JobRequest, opts, (error, data, response) => {
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
 **stopEntitiesDetectionV2JobRequest** | [**StopEntitiesDetectionV2JobRequest**](StopEntitiesDetectionV2JobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopEntitiesDetectionV2JobResponse**](StopEntitiesDetectionV2JobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopICD10CMInferenceJob

> StopICD10CMInferenceJobResponse stopICD10CMInferenceJob(xAmzTarget, stopICD10CMInferenceJobRequest, opts)



Stops an InferICD10CM inference job in progress.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopICD10CMInferenceJobRequest = new AwsComprehendMedical.StopICD10CMInferenceJobRequest(); // StopICD10CMInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopICD10CMInferenceJob(xAmzTarget, stopICD10CMInferenceJobRequest, opts, (error, data, response) => {
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
 **stopICD10CMInferenceJobRequest** | [**StopICD10CMInferenceJobRequest**](StopICD10CMInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopICD10CMInferenceJobResponse**](StopICD10CMInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopPHIDetectionJob

> StopPHIDetectionJobResponse stopPHIDetectionJob(xAmzTarget, stopPHIDetectionJobRequest, opts)



Stops a protected health information (PHI) detection job in progress.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopPHIDetectionJobRequest = new AwsComprehendMedical.StopPHIDetectionJobRequest(); // StopPHIDetectionJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopPHIDetectionJob(xAmzTarget, stopPHIDetectionJobRequest, opts, (error, data, response) => {
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
 **stopPHIDetectionJobRequest** | [**StopPHIDetectionJobRequest**](StopPHIDetectionJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopPHIDetectionJobResponse**](StopPHIDetectionJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopRxNormInferenceJob

> StopRxNormInferenceJobResponse stopRxNormInferenceJob(xAmzTarget, stopRxNormInferenceJobRequest, opts)



Stops an InferRxNorm inference job in progress.

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopRxNormInferenceJobRequest = new AwsComprehendMedical.StopRxNormInferenceJobRequest(); // StopRxNormInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopRxNormInferenceJob(xAmzTarget, stopRxNormInferenceJobRequest, opts, (error, data, response) => {
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
 **stopRxNormInferenceJobRequest** | [**StopRxNormInferenceJobRequest**](StopRxNormInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopRxNormInferenceJobResponse**](StopRxNormInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopSNOMEDCTInferenceJob

> StopSNOMEDCTInferenceJobResponse stopSNOMEDCTInferenceJob(xAmzTarget, stopSNOMEDCTInferenceJobRequest, opts)



 Stops an InferSNOMEDCT inference job in progress. 

### Example

```javascript
import AwsComprehendMedical from 'aws_comprehend_medical';
let defaultClient = AwsComprehendMedical.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsComprehendMedical.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopSNOMEDCTInferenceJobRequest = new AwsComprehendMedical.StopSNOMEDCTInferenceJobRequest(); // StopSNOMEDCTInferenceJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopSNOMEDCTInferenceJob(xAmzTarget, stopSNOMEDCTInferenceJobRequest, opts, (error, data, response) => {
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
 **stopSNOMEDCTInferenceJobRequest** | [**StopSNOMEDCTInferenceJobRequest**](StopSNOMEDCTInferenceJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopSNOMEDCTInferenceJobResponse**](StopSNOMEDCTInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

