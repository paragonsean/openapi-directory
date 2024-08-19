# AmazonInspector.DefaultApi

All URIs are relative to *http://inspector.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addAttributesToFindings**](DefaultApi.md#addAttributesToFindings) | **POST** /#X-Amz-Target&#x3D;InspectorService.AddAttributesToFindings | 
[**createAssessmentTarget**](DefaultApi.md#createAssessmentTarget) | **POST** /#X-Amz-Target&#x3D;InspectorService.CreateAssessmentTarget | 
[**createAssessmentTemplate**](DefaultApi.md#createAssessmentTemplate) | **POST** /#X-Amz-Target&#x3D;InspectorService.CreateAssessmentTemplate | 
[**createExclusionsPreview**](DefaultApi.md#createExclusionsPreview) | **POST** /#X-Amz-Target&#x3D;InspectorService.CreateExclusionsPreview | 
[**createResourceGroup**](DefaultApi.md#createResourceGroup) | **POST** /#X-Amz-Target&#x3D;InspectorService.CreateResourceGroup | 
[**deleteAssessmentRun**](DefaultApi.md#deleteAssessmentRun) | **POST** /#X-Amz-Target&#x3D;InspectorService.DeleteAssessmentRun | 
[**deleteAssessmentTarget**](DefaultApi.md#deleteAssessmentTarget) | **POST** /#X-Amz-Target&#x3D;InspectorService.DeleteAssessmentTarget | 
[**deleteAssessmentTemplate**](DefaultApi.md#deleteAssessmentTemplate) | **POST** /#X-Amz-Target&#x3D;InspectorService.DeleteAssessmentTemplate | 
[**describeAssessmentRuns**](DefaultApi.md#describeAssessmentRuns) | **POST** /#X-Amz-Target&#x3D;InspectorService.DescribeAssessmentRuns | 
[**describeAssessmentTargets**](DefaultApi.md#describeAssessmentTargets) | **POST** /#X-Amz-Target&#x3D;InspectorService.DescribeAssessmentTargets | 
[**describeAssessmentTemplates**](DefaultApi.md#describeAssessmentTemplates) | **POST** /#X-Amz-Target&#x3D;InspectorService.DescribeAssessmentTemplates | 
[**describeCrossAccountAccessRole**](DefaultApi.md#describeCrossAccountAccessRole) | **POST** /#X-Amz-Target&#x3D;InspectorService.DescribeCrossAccountAccessRole | 
[**describeExclusions**](DefaultApi.md#describeExclusions) | **POST** /#X-Amz-Target&#x3D;InspectorService.DescribeExclusions | 
[**describeFindings**](DefaultApi.md#describeFindings) | **POST** /#X-Amz-Target&#x3D;InspectorService.DescribeFindings | 
[**describeResourceGroups**](DefaultApi.md#describeResourceGroups) | **POST** /#X-Amz-Target&#x3D;InspectorService.DescribeResourceGroups | 
[**describeRulesPackages**](DefaultApi.md#describeRulesPackages) | **POST** /#X-Amz-Target&#x3D;InspectorService.DescribeRulesPackages | 
[**getAssessmentReport**](DefaultApi.md#getAssessmentReport) | **POST** /#X-Amz-Target&#x3D;InspectorService.GetAssessmentReport | 
[**getExclusionsPreview**](DefaultApi.md#getExclusionsPreview) | **POST** /#X-Amz-Target&#x3D;InspectorService.GetExclusionsPreview | 
[**getTelemetryMetadata**](DefaultApi.md#getTelemetryMetadata) | **POST** /#X-Amz-Target&#x3D;InspectorService.GetTelemetryMetadata | 
[**listAssessmentRunAgents**](DefaultApi.md#listAssessmentRunAgents) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListAssessmentRunAgents | 
[**listAssessmentRuns**](DefaultApi.md#listAssessmentRuns) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListAssessmentRuns | 
[**listAssessmentTargets**](DefaultApi.md#listAssessmentTargets) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListAssessmentTargets | 
[**listAssessmentTemplates**](DefaultApi.md#listAssessmentTemplates) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListAssessmentTemplates | 
[**listEventSubscriptions**](DefaultApi.md#listEventSubscriptions) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListEventSubscriptions | 
[**listExclusions**](DefaultApi.md#listExclusions) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListExclusions | 
[**listFindings**](DefaultApi.md#listFindings) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListFindings | 
[**listRulesPackages**](DefaultApi.md#listRulesPackages) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListRulesPackages | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;InspectorService.ListTagsForResource | 
[**previewAgents**](DefaultApi.md#previewAgents) | **POST** /#X-Amz-Target&#x3D;InspectorService.PreviewAgents | 
[**registerCrossAccountAccessRole**](DefaultApi.md#registerCrossAccountAccessRole) | **POST** /#X-Amz-Target&#x3D;InspectorService.RegisterCrossAccountAccessRole | 
[**removeAttributesFromFindings**](DefaultApi.md#removeAttributesFromFindings) | **POST** /#X-Amz-Target&#x3D;InspectorService.RemoveAttributesFromFindings | 
[**setTagsForResource**](DefaultApi.md#setTagsForResource) | **POST** /#X-Amz-Target&#x3D;InspectorService.SetTagsForResource | 
[**startAssessmentRun**](DefaultApi.md#startAssessmentRun) | **POST** /#X-Amz-Target&#x3D;InspectorService.StartAssessmentRun | 
[**stopAssessmentRun**](DefaultApi.md#stopAssessmentRun) | **POST** /#X-Amz-Target&#x3D;InspectorService.StopAssessmentRun | 
[**subscribeToEvent**](DefaultApi.md#subscribeToEvent) | **POST** /#X-Amz-Target&#x3D;InspectorService.SubscribeToEvent | 
[**unsubscribeFromEvent**](DefaultApi.md#unsubscribeFromEvent) | **POST** /#X-Amz-Target&#x3D;InspectorService.UnsubscribeFromEvent | 
[**updateAssessmentTarget**](DefaultApi.md#updateAssessmentTarget) | **POST** /#X-Amz-Target&#x3D;InspectorService.UpdateAssessmentTarget | 



## addAttributesToFindings

> AddAttributesToFindingsResponse addAttributesToFindings(xAmzTarget, addAttributesToFindingsRequest, opts)



Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addAttributesToFindingsRequest = new AmazonInspector.AddAttributesToFindingsRequest(); // AddAttributesToFindingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addAttributesToFindings(xAmzTarget, addAttributesToFindingsRequest, opts, (error, data, response) => {
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
 **addAttributesToFindingsRequest** | [**AddAttributesToFindingsRequest**](AddAttributesToFindingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddAttributesToFindingsResponse**](AddAttributesToFindingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssessmentTarget

> CreateAssessmentTargetResponse createAssessmentTarget(xAmzTarget, createAssessmentTargetRequest, opts)



Creates a new assessment target using the ARN of the resource group that is generated by &lt;a&gt;CreateResourceGroup&lt;/a&gt;. If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target. If the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/inspector/latest/userguide/inspector_slr.html\&quot;&gt;service-linked role&lt;/a&gt; isn’t already registered, this action also creates and registers a service-linked role to grant Amazon Inspector access to AWS Services needed to perform security assessments. You can create up to 50 assessment targets per AWS account. You can run up to 500 concurrent agents per AWS account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/inspector/latest/userguide/inspector_applications.html\&quot;&gt; Amazon Inspector Assessment Targets&lt;/a&gt;.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createAssessmentTargetRequest = new AmazonInspector.CreateAssessmentTargetRequest(); // CreateAssessmentTargetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAssessmentTarget(xAmzTarget, createAssessmentTargetRequest, opts, (error, data, response) => {
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
 **createAssessmentTargetRequest** | [**CreateAssessmentTargetRequest**](CreateAssessmentTargetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssessmentTargetResponse**](CreateAssessmentTargetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssessmentTemplate

> CreateAssessmentTemplateResponse createAssessmentTemplate(xAmzTarget, createAssessmentTemplateRequest, opts)



Creates an assessment template for the assessment target that is specified by the ARN of the assessment target. If the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/inspector/latest/userguide/inspector_slr.html\&quot;&gt;service-linked role&lt;/a&gt; isn’t already registered, this action also creates and registers a service-linked role to grant Amazon Inspector access to AWS Services needed to perform security assessments.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createAssessmentTemplateRequest = new AmazonInspector.CreateAssessmentTemplateRequest(); // CreateAssessmentTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAssessmentTemplate(xAmzTarget, createAssessmentTemplateRequest, opts, (error, data, response) => {
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
 **createAssessmentTemplateRequest** | [**CreateAssessmentTemplateRequest**](CreateAssessmentTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssessmentTemplateResponse**](CreateAssessmentTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExclusionsPreview

> CreateExclusionsPreviewResponse createExclusionsPreview(xAmzTarget, createExclusionsPreviewRequest, opts)



Starts the generation of an exclusions preview for the specified assessment template. The exclusions preview lists the potential exclusions (ExclusionPreview) that Inspector can detect before it runs the assessment. 

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createExclusionsPreviewRequest = new AmazonInspector.CreateExclusionsPreviewRequest(); // CreateExclusionsPreviewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createExclusionsPreview(xAmzTarget, createExclusionsPreviewRequest, opts, (error, data, response) => {
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
 **createExclusionsPreviewRequest** | [**CreateExclusionsPreviewRequest**](CreateExclusionsPreviewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateExclusionsPreviewResponse**](CreateExclusionsPreviewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createResourceGroup

> CreateResourceGroupResponse createResourceGroup(xAmzTarget, createResourceGroupRequest, opts)



Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target. The created resource group is then used to create an Amazon Inspector assessment target. For more information, see &lt;a&gt;CreateAssessmentTarget&lt;/a&gt;.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createResourceGroupRequest = new AmazonInspector.CreateResourceGroupRequest(); // CreateResourceGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createResourceGroup(xAmzTarget, createResourceGroupRequest, opts, (error, data, response) => {
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
 **createResourceGroupRequest** | [**CreateResourceGroupRequest**](CreateResourceGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateResourceGroupResponse**](CreateResourceGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAssessmentRun

> deleteAssessmentRun(xAmzTarget, deleteAssessmentRunRequest, opts)



Deletes the assessment run that is specified by the ARN of the assessment run.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteAssessmentRunRequest = new AmazonInspector.DeleteAssessmentRunRequest(); // DeleteAssessmentRunRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssessmentRun(xAmzTarget, deleteAssessmentRunRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteAssessmentRunRequest** | [**DeleteAssessmentRunRequest**](DeleteAssessmentRunRequest.md)|  | 
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


## deleteAssessmentTarget

> deleteAssessmentTarget(xAmzTarget, deleteAssessmentTargetRequest, opts)



Deletes the assessment target that is specified by the ARN of the assessment target.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteAssessmentTargetRequest = new AmazonInspector.DeleteAssessmentTargetRequest(); // DeleteAssessmentTargetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssessmentTarget(xAmzTarget, deleteAssessmentTargetRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteAssessmentTargetRequest** | [**DeleteAssessmentTargetRequest**](DeleteAssessmentTargetRequest.md)|  | 
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


## deleteAssessmentTemplate

> deleteAssessmentTemplate(xAmzTarget, deleteAssessmentTemplateRequest, opts)



Deletes the assessment template that is specified by the ARN of the assessment template.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteAssessmentTemplateRequest = new AmazonInspector.DeleteAssessmentTemplateRequest(); // DeleteAssessmentTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssessmentTemplate(xAmzTarget, deleteAssessmentTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteAssessmentTemplateRequest** | [**DeleteAssessmentTemplateRequest**](DeleteAssessmentTemplateRequest.md)|  | 
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


## describeAssessmentRuns

> DescribeAssessmentRunsResponse describeAssessmentRuns(xAmzTarget, describeAssessmentRunsRequest, opts)



Describes the assessment runs that are specified by the ARNs of the assessment runs.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAssessmentRunsRequest = new AmazonInspector.DescribeAssessmentRunsRequest(); // DescribeAssessmentRunsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAssessmentRuns(xAmzTarget, describeAssessmentRunsRequest, opts, (error, data, response) => {
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
 **describeAssessmentRunsRequest** | [**DescribeAssessmentRunsRequest**](DescribeAssessmentRunsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAssessmentRunsResponse**](DescribeAssessmentRunsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAssessmentTargets

> DescribeAssessmentTargetsResponse describeAssessmentTargets(xAmzTarget, describeAssessmentTargetsRequest, opts)



Describes the assessment targets that are specified by the ARNs of the assessment targets.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAssessmentTargetsRequest = new AmazonInspector.DescribeAssessmentTargetsRequest(); // DescribeAssessmentTargetsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAssessmentTargets(xAmzTarget, describeAssessmentTargetsRequest, opts, (error, data, response) => {
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
 **describeAssessmentTargetsRequest** | [**DescribeAssessmentTargetsRequest**](DescribeAssessmentTargetsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAssessmentTargetsResponse**](DescribeAssessmentTargetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAssessmentTemplates

> DescribeAssessmentTemplatesResponse describeAssessmentTemplates(xAmzTarget, describeAssessmentTemplatesRequest, opts)



Describes the assessment templates that are specified by the ARNs of the assessment templates.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAssessmentTemplatesRequest = new AmazonInspector.DescribeAssessmentTemplatesRequest(); // DescribeAssessmentTemplatesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAssessmentTemplates(xAmzTarget, describeAssessmentTemplatesRequest, opts, (error, data, response) => {
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
 **describeAssessmentTemplatesRequest** | [**DescribeAssessmentTemplatesRequest**](DescribeAssessmentTemplatesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAssessmentTemplatesResponse**](DescribeAssessmentTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeCrossAccountAccessRole

> DescribeCrossAccountAccessRoleResponse describeCrossAccountAccessRole(xAmzTarget, opts)



Describes the IAM role that enables Amazon Inspector to access your AWS account.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeCrossAccountAccessRole(xAmzTarget, opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeCrossAccountAccessRoleResponse**](DescribeCrossAccountAccessRoleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeExclusions

> DescribeExclusionsResponse describeExclusions(xAmzTarget, describeExclusionsRequest, opts)



Describes the exclusions that are specified by the exclusions&#39; ARNs.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeExclusionsRequest = new AmazonInspector.DescribeExclusionsRequest(); // DescribeExclusionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeExclusions(xAmzTarget, describeExclusionsRequest, opts, (error, data, response) => {
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
 **describeExclusionsRequest** | [**DescribeExclusionsRequest**](DescribeExclusionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeExclusionsResponse**](DescribeExclusionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeFindings

> DescribeFindingsResponse describeFindings(xAmzTarget, describeFindingsRequest, opts)



Describes the findings that are specified by the ARNs of the findings.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeFindingsRequest = new AmazonInspector.DescribeFindingsRequest(); // DescribeFindingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeFindings(xAmzTarget, describeFindingsRequest, opts, (error, data, response) => {
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
 **describeFindingsRequest** | [**DescribeFindingsRequest**](DescribeFindingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeFindingsResponse**](DescribeFindingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeResourceGroups

> DescribeResourceGroupsResponse describeResourceGroups(xAmzTarget, describeResourceGroupsRequest, opts)



Describes the resource groups that are specified by the ARNs of the resource groups.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeResourceGroupsRequest = new AmazonInspector.DescribeResourceGroupsRequest(); // DescribeResourceGroupsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeResourceGroups(xAmzTarget, describeResourceGroupsRequest, opts, (error, data, response) => {
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
 **describeResourceGroupsRequest** | [**DescribeResourceGroupsRequest**](DescribeResourceGroupsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeResourceGroupsResponse**](DescribeResourceGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeRulesPackages

> DescribeRulesPackagesResponse describeRulesPackages(xAmzTarget, describeRulesPackagesRequest, opts)



Describes the rules packages that are specified by the ARNs of the rules packages.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeRulesPackagesRequest = new AmazonInspector.DescribeRulesPackagesRequest(); // DescribeRulesPackagesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRulesPackages(xAmzTarget, describeRulesPackagesRequest, opts, (error, data, response) => {
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
 **describeRulesPackagesRequest** | [**DescribeRulesPackagesRequest**](DescribeRulesPackagesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRulesPackagesResponse**](DescribeRulesPackagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAssessmentReport

> GetAssessmentReportResponse getAssessmentReport(xAmzTarget, getAssessmentReportRequest, opts)



Produces an assessment report that includes detailed and comprehensive results of a specified assessment run. 

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getAssessmentReportRequest = new AmazonInspector.GetAssessmentReportRequest(); // GetAssessmentReportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssessmentReport(xAmzTarget, getAssessmentReportRequest, opts, (error, data, response) => {
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
 **getAssessmentReportRequest** | [**GetAssessmentReportRequest**](GetAssessmentReportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssessmentReportResponse**](GetAssessmentReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getExclusionsPreview

> GetExclusionsPreviewResponse getExclusionsPreview(xAmzTarget, getExclusionsPreviewRequest, opts)



Retrieves the exclusions preview (a list of ExclusionPreview objects) specified by the preview token. You can obtain the preview token by running the CreateExclusionsPreview API.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getExclusionsPreviewRequest = new AmazonInspector.GetExclusionsPreviewRequest(); // GetExclusionsPreviewRequest | 
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
apiInstance.getExclusionsPreview(xAmzTarget, getExclusionsPreviewRequest, opts, (error, data, response) => {
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
 **getExclusionsPreviewRequest** | [**GetExclusionsPreviewRequest**](GetExclusionsPreviewRequest.md)|  | 
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

[**GetExclusionsPreviewResponse**](GetExclusionsPreviewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTelemetryMetadata

> GetTelemetryMetadataResponse getTelemetryMetadata(xAmzTarget, getTelemetryMetadataRequest, opts)



Information about the data that is collected for the specified assessment run.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getTelemetryMetadataRequest = new AmazonInspector.GetTelemetryMetadataRequest(); // GetTelemetryMetadataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTelemetryMetadata(xAmzTarget, getTelemetryMetadataRequest, opts, (error, data, response) => {
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
 **getTelemetryMetadataRequest** | [**GetTelemetryMetadataRequest**](GetTelemetryMetadataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTelemetryMetadataResponse**](GetTelemetryMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAssessmentRunAgents

> ListAssessmentRunAgentsResponse listAssessmentRunAgents(xAmzTarget, listAssessmentRunAgentsRequest, opts)



Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAssessmentRunAgentsRequest = new AmazonInspector.ListAssessmentRunAgentsRequest(); // ListAssessmentRunAgentsRequest | 
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
apiInstance.listAssessmentRunAgents(xAmzTarget, listAssessmentRunAgentsRequest, opts, (error, data, response) => {
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
 **listAssessmentRunAgentsRequest** | [**ListAssessmentRunAgentsRequest**](ListAssessmentRunAgentsRequest.md)|  | 
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

[**ListAssessmentRunAgentsResponse**](ListAssessmentRunAgentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAssessmentRuns

> ListAssessmentRunsResponse listAssessmentRuns(xAmzTarget, listAssessmentRunsRequest, opts)



Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAssessmentRunsRequest = new AmazonInspector.ListAssessmentRunsRequest(); // ListAssessmentRunsRequest | 
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
apiInstance.listAssessmentRuns(xAmzTarget, listAssessmentRunsRequest, opts, (error, data, response) => {
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
 **listAssessmentRunsRequest** | [**ListAssessmentRunsRequest**](ListAssessmentRunsRequest.md)|  | 
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

[**ListAssessmentRunsResponse**](ListAssessmentRunsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAssessmentTargets

> ListAssessmentTargetsResponse listAssessmentTargets(xAmzTarget, listAssessmentTargetsRequest, opts)



Lists the ARNs of the assessment targets within this AWS account. For more information about assessment targets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/inspector/latest/userguide/inspector_applications.html\&quot;&gt;Amazon Inspector Assessment Targets&lt;/a&gt;.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAssessmentTargetsRequest = new AmazonInspector.ListAssessmentTargetsRequest(); // ListAssessmentTargetsRequest | 
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
apiInstance.listAssessmentTargets(xAmzTarget, listAssessmentTargetsRequest, opts, (error, data, response) => {
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
 **listAssessmentTargetsRequest** | [**ListAssessmentTargetsRequest**](ListAssessmentTargetsRequest.md)|  | 
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

[**ListAssessmentTargetsResponse**](ListAssessmentTargetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAssessmentTemplates

> ListAssessmentTemplatesResponse listAssessmentTemplates(xAmzTarget, listAssessmentTemplatesRequest, opts)



Lists the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAssessmentTemplatesRequest = new AmazonInspector.ListAssessmentTemplatesRequest(); // ListAssessmentTemplatesRequest | 
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
apiInstance.listAssessmentTemplates(xAmzTarget, listAssessmentTemplatesRequest, opts, (error, data, response) => {
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
 **listAssessmentTemplatesRequest** | [**ListAssessmentTemplatesRequest**](ListAssessmentTemplatesRequest.md)|  | 
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

[**ListAssessmentTemplatesResponse**](ListAssessmentTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEventSubscriptions

> ListEventSubscriptionsResponse listEventSubscriptions(xAmzTarget, listEventSubscriptionsRequest, opts)



Lists all the event subscriptions for the assessment template that is specified by the ARN of the assessment template. For more information, see &lt;a&gt;SubscribeToEvent&lt;/a&gt; and &lt;a&gt;UnsubscribeFromEvent&lt;/a&gt;.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listEventSubscriptionsRequest = new AmazonInspector.ListEventSubscriptionsRequest(); // ListEventSubscriptionsRequest | 
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
apiInstance.listEventSubscriptions(xAmzTarget, listEventSubscriptionsRequest, opts, (error, data, response) => {
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
 **listEventSubscriptionsRequest** | [**ListEventSubscriptionsRequest**](ListEventSubscriptionsRequest.md)|  | 
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

[**ListEventSubscriptionsResponse**](ListEventSubscriptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listExclusions

> ListExclusionsResponse listExclusions(xAmzTarget, listExclusionsRequest, opts)



List exclusions that are generated by the assessment run.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listExclusionsRequest = new AmazonInspector.ListExclusionsRequest(); // ListExclusionsRequest | 
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
apiInstance.listExclusions(xAmzTarget, listExclusionsRequest, opts, (error, data, response) => {
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
 **listExclusionsRequest** | [**ListExclusionsRequest**](ListExclusionsRequest.md)|  | 
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

[**ListExclusionsResponse**](ListExclusionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listFindings

> ListFindingsResponse listFindings(xAmzTarget, listFindingsRequest, opts)



Lists findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listFindingsRequest = new AmazonInspector.ListFindingsRequest(); // ListFindingsRequest | 
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
apiInstance.listFindings(xAmzTarget, listFindingsRequest, opts, (error, data, response) => {
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
 **listFindingsRequest** | [**ListFindingsRequest**](ListFindingsRequest.md)|  | 
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

[**ListFindingsResponse**](ListFindingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRulesPackages

> ListRulesPackagesResponse listRulesPackages(xAmzTarget, listRulesPackagesRequest, opts)



Lists all available Amazon Inspector rules packages.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listRulesPackagesRequest = new AmazonInspector.ListRulesPackagesRequest(); // ListRulesPackagesRequest | 
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
apiInstance.listRulesPackages(xAmzTarget, listRulesPackagesRequest, opts, (error, data, response) => {
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
 **listRulesPackagesRequest** | [**ListRulesPackagesRequest**](ListRulesPackagesRequest.md)|  | 
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

[**ListRulesPackagesResponse**](ListRulesPackagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Lists all tags associated with an assessment template.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AmazonInspector.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts, (error, data, response) => {
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
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## previewAgents

> PreviewAgentsResponse previewAgents(xAmzTarget, previewAgentsRequest, opts)



Previews the agents installed on the EC2 instances that are part of the specified assessment target.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let previewAgentsRequest = new AmazonInspector.PreviewAgentsRequest(); // PreviewAgentsRequest | 
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
apiInstance.previewAgents(xAmzTarget, previewAgentsRequest, opts, (error, data, response) => {
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
 **previewAgentsRequest** | [**PreviewAgentsRequest**](PreviewAgentsRequest.md)|  | 
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

[**PreviewAgentsResponse**](PreviewAgentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registerCrossAccountAccessRole

> registerCrossAccountAccessRole(xAmzTarget, registerCrossAccountAccessRoleRequest, opts)



Registers the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let registerCrossAccountAccessRoleRequest = new AmazonInspector.RegisterCrossAccountAccessRoleRequest(); // RegisterCrossAccountAccessRoleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerCrossAccountAccessRole(xAmzTarget, registerCrossAccountAccessRoleRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **registerCrossAccountAccessRoleRequest** | [**RegisterCrossAccountAccessRoleRequest**](RegisterCrossAccountAccessRoleRequest.md)|  | 
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


## removeAttributesFromFindings

> RemoveAttributesFromFindingsResponse removeAttributesFromFindings(xAmzTarget, removeAttributesFromFindingsRequest, opts)



Removes entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let removeAttributesFromFindingsRequest = new AmazonInspector.RemoveAttributesFromFindingsRequest(); // RemoveAttributesFromFindingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeAttributesFromFindings(xAmzTarget, removeAttributesFromFindingsRequest, opts, (error, data, response) => {
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
 **removeAttributesFromFindingsRequest** | [**RemoveAttributesFromFindingsRequest**](RemoveAttributesFromFindingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RemoveAttributesFromFindingsResponse**](RemoveAttributesFromFindingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setTagsForResource

> setTagsForResource(xAmzTarget, setTagsForResourceRequest, opts)



Sets tags (key and value pairs) to the assessment template that is specified by the ARN of the assessment template.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let setTagsForResourceRequest = new AmazonInspector.SetTagsForResourceRequest(); // SetTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setTagsForResource(xAmzTarget, setTagsForResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **setTagsForResourceRequest** | [**SetTagsForResourceRequest**](SetTagsForResourceRequest.md)|  | 
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


## startAssessmentRun

> StartAssessmentRunResponse startAssessmentRun(xAmzTarget, startAssessmentRunRequest, opts)



Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startAssessmentRunRequest = new AmazonInspector.StartAssessmentRunRequest(); // StartAssessmentRunRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startAssessmentRun(xAmzTarget, startAssessmentRunRequest, opts, (error, data, response) => {
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
 **startAssessmentRunRequest** | [**StartAssessmentRunRequest**](StartAssessmentRunRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartAssessmentRunResponse**](StartAssessmentRunResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopAssessmentRun

> stopAssessmentRun(xAmzTarget, stopAssessmentRunRequest, opts)



Stops the assessment run that is specified by the ARN of the assessment run.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopAssessmentRunRequest = new AmazonInspector.StopAssessmentRunRequest(); // StopAssessmentRunRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopAssessmentRun(xAmzTarget, stopAssessmentRunRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **stopAssessmentRunRequest** | [**StopAssessmentRunRequest**](StopAssessmentRunRequest.md)|  | 
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


## subscribeToEvent

> subscribeToEvent(xAmzTarget, subscribeToEventRequest, opts)



Enables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let subscribeToEventRequest = new AmazonInspector.SubscribeToEventRequest(); // SubscribeToEventRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.subscribeToEvent(xAmzTarget, subscribeToEventRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **subscribeToEventRequest** | [**SubscribeToEventRequest**](SubscribeToEventRequest.md)|  | 
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


## unsubscribeFromEvent

> unsubscribeFromEvent(xAmzTarget, unsubscribeFromEventRequest, opts)



Disables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let unsubscribeFromEventRequest = new AmazonInspector.UnsubscribeFromEventRequest(); // UnsubscribeFromEventRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.unsubscribeFromEvent(xAmzTarget, unsubscribeFromEventRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **unsubscribeFromEventRequest** | [**UnsubscribeFromEventRequest**](UnsubscribeFromEventRequest.md)|  | 
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


## updateAssessmentTarget

> updateAssessmentTarget(xAmzTarget, updateAssessmentTargetRequest, opts)



&lt;p&gt;Updates the assessment target that is specified by the ARN of the assessment target.&lt;/p&gt; &lt;p&gt;If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.&lt;/p&gt;

### Example

```javascript
import AmazonInspector from 'amazon_inspector';
let defaultClient = AmazonInspector.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonInspector.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateAssessmentTargetRequest = new AmazonInspector.UpdateAssessmentTargetRequest(); // UpdateAssessmentTargetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssessmentTarget(xAmzTarget, updateAssessmentTargetRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **updateAssessmentTargetRequest** | [**UpdateAssessmentTargetRequest**](UpdateAssessmentTargetRequest.md)|  | 
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

