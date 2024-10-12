# AwsResilienceHub.DefaultApi

All URIs are relative to *http://resiliencehub.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addDraftAppVersionResourceMappings**](DefaultApi.md#addDraftAppVersionResourceMappings) | **POST** /add-draft-app-version-resource-mappings | 
[**batchUpdateRecommendationStatus**](DefaultApi.md#batchUpdateRecommendationStatus) | **POST** /batch-update-recommendation-status | 
[**createApp**](DefaultApi.md#createApp) | **POST** /create-app | 
[**createAppVersionAppComponent**](DefaultApi.md#createAppVersionAppComponent) | **POST** /create-app-version-app-component | 
[**createAppVersionResource**](DefaultApi.md#createAppVersionResource) | **POST** /create-app-version-resource | 
[**createRecommendationTemplate**](DefaultApi.md#createRecommendationTemplate) | **POST** /create-recommendation-template | 
[**createResiliencyPolicy**](DefaultApi.md#createResiliencyPolicy) | **POST** /create-resiliency-policy | 
[**deleteApp**](DefaultApi.md#deleteApp) | **POST** /delete-app | 
[**deleteAppAssessment**](DefaultApi.md#deleteAppAssessment) | **POST** /delete-app-assessment | 
[**deleteAppInputSource**](DefaultApi.md#deleteAppInputSource) | **POST** /delete-app-input-source | 
[**deleteAppVersionAppComponent**](DefaultApi.md#deleteAppVersionAppComponent) | **POST** /delete-app-version-app-component | 
[**deleteAppVersionResource**](DefaultApi.md#deleteAppVersionResource) | **POST** /delete-app-version-resource | 
[**deleteRecommendationTemplate**](DefaultApi.md#deleteRecommendationTemplate) | **POST** /delete-recommendation-template | 
[**deleteResiliencyPolicy**](DefaultApi.md#deleteResiliencyPolicy) | **POST** /delete-resiliency-policy | 
[**describeApp**](DefaultApi.md#describeApp) | **POST** /describe-app | 
[**describeAppAssessment**](DefaultApi.md#describeAppAssessment) | **POST** /describe-app-assessment | 
[**describeAppVersion**](DefaultApi.md#describeAppVersion) | **POST** /describe-app-version | 
[**describeAppVersionAppComponent**](DefaultApi.md#describeAppVersionAppComponent) | **POST** /describe-app-version-app-component | 
[**describeAppVersionResource**](DefaultApi.md#describeAppVersionResource) | **POST** /describe-app-version-resource | 
[**describeAppVersionResourcesResolutionStatus**](DefaultApi.md#describeAppVersionResourcesResolutionStatus) | **POST** /describe-app-version-resources-resolution-status | 
[**describeAppVersionTemplate**](DefaultApi.md#describeAppVersionTemplate) | **POST** /describe-app-version-template | 
[**describeDraftAppVersionResourcesImportStatus**](DefaultApi.md#describeDraftAppVersionResourcesImportStatus) | **POST** /describe-draft-app-version-resources-import-status | 
[**describeResiliencyPolicy**](DefaultApi.md#describeResiliencyPolicy) | **POST** /describe-resiliency-policy | 
[**importResourcesToDraftAppVersion**](DefaultApi.md#importResourcesToDraftAppVersion) | **POST** /import-resources-to-draft-app-version | 
[**listAlarmRecommendations**](DefaultApi.md#listAlarmRecommendations) | **POST** /list-alarm-recommendations | 
[**listAppAssessmentComplianceDrifts**](DefaultApi.md#listAppAssessmentComplianceDrifts) | **POST** /list-app-assessment-compliance-drifts | 
[**listAppAssessments**](DefaultApi.md#listAppAssessments) | **GET** /list-app-assessments | 
[**listAppComponentCompliances**](DefaultApi.md#listAppComponentCompliances) | **POST** /list-app-component-compliances | 
[**listAppComponentRecommendations**](DefaultApi.md#listAppComponentRecommendations) | **POST** /list-app-component-recommendations | 
[**listAppInputSources**](DefaultApi.md#listAppInputSources) | **POST** /list-app-input-sources | 
[**listAppVersionAppComponents**](DefaultApi.md#listAppVersionAppComponents) | **POST** /list-app-version-app-components | 
[**listAppVersionResourceMappings**](DefaultApi.md#listAppVersionResourceMappings) | **POST** /list-app-version-resource-mappings | 
[**listAppVersionResources**](DefaultApi.md#listAppVersionResources) | **POST** /list-app-version-resources | 
[**listAppVersions**](DefaultApi.md#listAppVersions) | **POST** /list-app-versions | 
[**listApps**](DefaultApi.md#listApps) | **GET** /list-apps | 
[**listRecommendationTemplates**](DefaultApi.md#listRecommendationTemplates) | **GET** /list-recommendation-templates#assessmentArn | 
[**listResiliencyPolicies**](DefaultApi.md#listResiliencyPolicies) | **GET** /list-resiliency-policies | 
[**listSopRecommendations**](DefaultApi.md#listSopRecommendations) | **POST** /list-sop-recommendations | 
[**listSuggestedResiliencyPolicies**](DefaultApi.md#listSuggestedResiliencyPolicies) | **GET** /list-suggested-resiliency-policies | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**listTestRecommendations**](DefaultApi.md#listTestRecommendations) | **POST** /list-test-recommendations | 
[**listUnsupportedAppVersionResources**](DefaultApi.md#listUnsupportedAppVersionResources) | **POST** /list-unsupported-app-version-resources | 
[**publishAppVersion**](DefaultApi.md#publishAppVersion) | **POST** /publish-app-version | 
[**putDraftAppVersionTemplate**](DefaultApi.md#putDraftAppVersionTemplate) | **POST** /put-draft-app-version-template | 
[**removeDraftAppVersionResourceMappings**](DefaultApi.md#removeDraftAppVersionResourceMappings) | **POST** /remove-draft-app-version-resource-mappings | 
[**resolveAppVersionResources**](DefaultApi.md#resolveAppVersionResources) | **POST** /resolve-app-version-resources | 
[**startAppAssessment**](DefaultApi.md#startAppAssessment) | **POST** /start-app-assessment | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateApp**](DefaultApi.md#updateApp) | **POST** /update-app | 
[**updateAppVersion**](DefaultApi.md#updateAppVersion) | **POST** /update-app-version | 
[**updateAppVersionAppComponent**](DefaultApi.md#updateAppVersionAppComponent) | **POST** /update-app-version-app-component | 
[**updateAppVersionResource**](DefaultApi.md#updateAppVersionResource) | **POST** /update-app-version-resource | 
[**updateResiliencyPolicy**](DefaultApi.md#updateResiliencyPolicy) | **POST** /update-resiliency-policy | 



## addDraftAppVersionResourceMappings

> AddDraftAppVersionResourceMappingsResponse addDraftAppVersionResourceMappings(addDraftAppVersionResourceMappingsRequest, opts)



Adds the resource mapping for the draft application version. You can also update an existing resource mapping to a new physical resource.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let addDraftAppVersionResourceMappingsRequest = new AwsResilienceHub.AddDraftAppVersionResourceMappingsRequest(); // AddDraftAppVersionResourceMappingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addDraftAppVersionResourceMappings(addDraftAppVersionResourceMappingsRequest, opts, (error, data, response) => {
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
 **addDraftAppVersionResourceMappingsRequest** | [**AddDraftAppVersionResourceMappingsRequest**](AddDraftAppVersionResourceMappingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddDraftAppVersionResourceMappingsResponse**](AddDraftAppVersionResourceMappingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUpdateRecommendationStatus

> BatchUpdateRecommendationStatusResponse batchUpdateRecommendationStatus(batchUpdateRecommendationStatusRequest, opts)



Enables you to include or exclude one or more operational recommendations.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let batchUpdateRecommendationStatusRequest = new AwsResilienceHub.BatchUpdateRecommendationStatusRequest(); // BatchUpdateRecommendationStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdateRecommendationStatus(batchUpdateRecommendationStatusRequest, opts, (error, data, response) => {
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
 **batchUpdateRecommendationStatusRequest** | [**BatchUpdateRecommendationStatusRequest**](BatchUpdateRecommendationStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdateRecommendationStatusResponse**](BatchUpdateRecommendationStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createApp

> CreateAppResponse createApp(createAppRequest, opts)



&lt;p&gt;Creates an Resilience Hub application. An Resilience Hub application is a collection of Amazon Web Services resources structured to prevent and recover Amazon Web Services application disruptions. To describe a Resilience Hub application, you provide an application name, resources from one or more CloudFormation stacks, Resource Groups, Terraform state files, AppRegistry applications, and an appropriate resiliency policy. In addition, you can also add resources that are located on Amazon Elastic Kubernetes Service (Amazon EKS) clusters as optional resources. For more information about the number of resources supported per application, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/resiliencehub.html#limits_resiliencehub\&quot;&gt;Service quotas&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After you create an Resilience Hub application, you publish it so that you can run a resiliency assessment on it. You can then use recommendations from the assessment to improve resiliency by running another assessment, comparing results, and then iterating the process until you achieve your goals for recovery time objective (RTO) and recovery point objective (RPO).&lt;/p&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let createAppRequest = new AwsResilienceHub.CreateAppRequest(); // CreateAppRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApp(createAppRequest, opts, (error, data, response) => {
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
 **createAppRequest** | [**CreateAppRequest**](CreateAppRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAppResponse**](CreateAppResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAppVersionAppComponent

> CreateAppVersionAppComponentResponse createAppVersionAppComponent(createAppVersionAppComponentRequest, opts)



&lt;p&gt;Creates a new Application Component in the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let createAppVersionAppComponentRequest = new AwsResilienceHub.CreateAppVersionAppComponentRequest(); // CreateAppVersionAppComponentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAppVersionAppComponent(createAppVersionAppComponentRequest, opts, (error, data, response) => {
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
 **createAppVersionAppComponentRequest** | [**CreateAppVersionAppComponentRequest**](CreateAppVersionAppComponentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAppVersionAppComponentResponse**](CreateAppVersionAppComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAppVersionResource

> CreateAppVersionResourceResponse createAppVersionResource(createAppVersionResourceRequest, opts)



&lt;p&gt;Adds a resource to the Resilience Hub application and assigns it to the specified Application Components. If you specify a new Application Component, Resilience Hub will automatically create the Application Component.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This action has no effect outside Resilience Hub.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To update application version with new &lt;code&gt;physicalResourceID&lt;/code&gt;, you must call &lt;code&gt;ResolveAppVersionResources&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let createAppVersionResourceRequest = new AwsResilienceHub.CreateAppVersionResourceRequest(); // CreateAppVersionResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAppVersionResource(createAppVersionResourceRequest, opts, (error, data, response) => {
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
 **createAppVersionResourceRequest** | [**CreateAppVersionResourceRequest**](CreateAppVersionResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAppVersionResourceResponse**](CreateAppVersionResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRecommendationTemplate

> CreateRecommendationTemplateResponse createRecommendationTemplate(createRecommendationTemplateRequest, opts)



Creates a new recommendation template for the Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let createRecommendationTemplateRequest = new AwsResilienceHub.CreateRecommendationTemplateRequest(); // CreateRecommendationTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRecommendationTemplate(createRecommendationTemplateRequest, opts, (error, data, response) => {
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
 **createRecommendationTemplateRequest** | [**CreateRecommendationTemplateRequest**](CreateRecommendationTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRecommendationTemplateResponse**](CreateRecommendationTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createResiliencyPolicy

> CreateResiliencyPolicyResponse createResiliencyPolicy(createResiliencyPolicyRequest, opts)



Creates a resiliency policy for an application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let createResiliencyPolicyRequest = new AwsResilienceHub.CreateResiliencyPolicyRequest(); // CreateResiliencyPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createResiliencyPolicy(createResiliencyPolicyRequest, opts, (error, data, response) => {
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
 **createResiliencyPolicyRequest** | [**CreateResiliencyPolicyRequest**](CreateResiliencyPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateResiliencyPolicyResponse**](CreateResiliencyPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApp

> DeleteAppResponse deleteApp(deleteAppRequest, opts)



Deletes an Resilience Hub application. This is a destructive action that can&#39;t be undone.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let deleteAppRequest = new AwsResilienceHub.DeleteAppRequest(); // DeleteAppRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApp(deleteAppRequest, opts, (error, data, response) => {
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
 **deleteAppRequest** | [**DeleteAppRequest**](DeleteAppRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAppResponse**](DeleteAppResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAppAssessment

> DeleteAppAssessmentResponse deleteAppAssessment(deleteAppAssessmentRequest, opts)



Deletes an Resilience Hub application assessment. This is a destructive action that can&#39;t be undone.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let deleteAppAssessmentRequest = new AwsResilienceHub.DeleteAppAssessmentRequest(); // DeleteAppAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppAssessment(deleteAppAssessmentRequest, opts, (error, data, response) => {
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
 **deleteAppAssessmentRequest** | [**DeleteAppAssessmentRequest**](DeleteAppAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAppAssessmentResponse**](DeleteAppAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAppInputSource

> DeleteAppInputSourceResponse deleteAppInputSource(deleteAppInputSourceRequest, opts)



Deletes the input source and all of its imported resources from the Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let deleteAppInputSourceRequest = new AwsResilienceHub.DeleteAppInputSourceRequest(); // DeleteAppInputSourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppInputSource(deleteAppInputSourceRequest, opts, (error, data, response) => {
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
 **deleteAppInputSourceRequest** | [**DeleteAppInputSourceRequest**](DeleteAppInputSourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAppInputSourceResponse**](DeleteAppInputSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAppVersionAppComponent

> DeleteAppVersionAppComponentResponse deleteAppVersionAppComponent(deleteAppVersionAppComponentRequest, opts)



&lt;p&gt;Deletes an Application Component from the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You will not be able to delete an Application Component if it has resources associated with it.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let deleteAppVersionAppComponentRequest = new AwsResilienceHub.DeleteAppVersionAppComponentRequest(); // DeleteAppVersionAppComponentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppVersionAppComponent(deleteAppVersionAppComponentRequest, opts, (error, data, response) => {
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
 **deleteAppVersionAppComponentRequest** | [**DeleteAppVersionAppComponentRequest**](DeleteAppVersionAppComponentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAppVersionAppComponentResponse**](DeleteAppVersionAppComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAppVersionResource

> DeleteAppVersionResourceResponse deleteAppVersionResource(deleteAppVersionResourceRequest, opts)



&lt;p&gt;Deletes a resource from the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can only delete a manually added resource. To exclude non-manually added resources, use the &lt;code&gt;UpdateAppVersionResource&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This action has no effect outside Resilience Hub.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let deleteAppVersionResourceRequest = new AwsResilienceHub.DeleteAppVersionResourceRequest(); // DeleteAppVersionResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppVersionResource(deleteAppVersionResourceRequest, opts, (error, data, response) => {
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
 **deleteAppVersionResourceRequest** | [**DeleteAppVersionResourceRequest**](DeleteAppVersionResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAppVersionResourceResponse**](DeleteAppVersionResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRecommendationTemplate

> DeleteRecommendationTemplateResponse deleteRecommendationTemplate(deleteRecommendationTemplateRequest, opts)



Deletes a recommendation template. This is a destructive action that can&#39;t be undone.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let deleteRecommendationTemplateRequest = new AwsResilienceHub.DeleteRecommendationTemplateRequest(); // DeleteRecommendationTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRecommendationTemplate(deleteRecommendationTemplateRequest, opts, (error, data, response) => {
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
 **deleteRecommendationTemplateRequest** | [**DeleteRecommendationTemplateRequest**](DeleteRecommendationTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteRecommendationTemplateResponse**](DeleteRecommendationTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteResiliencyPolicy

> DeleteResiliencyPolicyResponse deleteResiliencyPolicy(deleteResiliencyPolicyRequest, opts)



Deletes a resiliency policy. This is a destructive action that can&#39;t be undone.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let deleteResiliencyPolicyRequest = new AwsResilienceHub.DeleteResiliencyPolicyRequest(); // DeleteResiliencyPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteResiliencyPolicy(deleteResiliencyPolicyRequest, opts, (error, data, response) => {
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
 **deleteResiliencyPolicyRequest** | [**DeleteResiliencyPolicyRequest**](DeleteResiliencyPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteResiliencyPolicyResponse**](DeleteResiliencyPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeApp

> DescribeAppResponse describeApp(describeAppRequest, opts)



Describes an Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppRequest = new AwsResilienceHub.DescribeAppRequest(); // DescribeAppRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeApp(describeAppRequest, opts, (error, data, response) => {
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
 **describeAppRequest** | [**DescribeAppRequest**](DescribeAppRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppResponse**](DescribeAppResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAppAssessment

> DescribeAppAssessmentResponse describeAppAssessment(describeAppAssessmentRequest, opts)



Describes an assessment for an Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppAssessmentRequest = new AwsResilienceHub.DescribeAppAssessmentRequest(); // DescribeAppAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppAssessment(describeAppAssessmentRequest, opts, (error, data, response) => {
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
 **describeAppAssessmentRequest** | [**DescribeAppAssessmentRequest**](DescribeAppAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppAssessmentResponse**](DescribeAppAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAppVersion

> DescribeAppVersionResponse describeAppVersion(describeAppVersionRequest, opts)



Describes the Resilience Hub application version.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppVersionRequest = new AwsResilienceHub.DescribeAppVersionRequest(); // DescribeAppVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppVersion(describeAppVersionRequest, opts, (error, data, response) => {
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
 **describeAppVersionRequest** | [**DescribeAppVersionRequest**](DescribeAppVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppVersionResponse**](DescribeAppVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAppVersionAppComponent

> DescribeAppVersionAppComponentResponse describeAppVersionAppComponent(describeAppVersionAppComponentRequest, opts)



Describes an Application Component in the Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppVersionAppComponentRequest = new AwsResilienceHub.DescribeAppVersionAppComponentRequest(); // DescribeAppVersionAppComponentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppVersionAppComponent(describeAppVersionAppComponentRequest, opts, (error, data, response) => {
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
 **describeAppVersionAppComponentRequest** | [**DescribeAppVersionAppComponentRequest**](DescribeAppVersionAppComponentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppVersionAppComponentResponse**](DescribeAppVersionAppComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAppVersionResource

> DescribeAppVersionResourceResponse describeAppVersionResource(describeAppVersionResourceRequest, opts)



&lt;p&gt;Describes a resource of the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API accepts only one of the following parameters to descibe the resource:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resourceName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;logicalResourceId&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;physicalResourceId&lt;/code&gt; (Along with &lt;code&gt;physicalResourceId&lt;/code&gt;, you can also provide &lt;code&gt;awsAccountId&lt;/code&gt;, and &lt;code&gt;awsRegion&lt;/code&gt;)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppVersionResourceRequest = new AwsResilienceHub.DescribeAppVersionResourceRequest(); // DescribeAppVersionResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppVersionResource(describeAppVersionResourceRequest, opts, (error, data, response) => {
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
 **describeAppVersionResourceRequest** | [**DescribeAppVersionResourceRequest**](DescribeAppVersionResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppVersionResourceResponse**](DescribeAppVersionResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAppVersionResourcesResolutionStatus

> DescribeAppVersionResourcesResolutionStatusResponse describeAppVersionResourcesResolutionStatus(describeAppVersionResourcesResolutionStatusRequest, opts)



Returns the resolution status for the specified resolution identifier for an application version. If &lt;code&gt;resolutionId&lt;/code&gt; is not specified, the current resolution status is returned.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppVersionResourcesResolutionStatusRequest = new AwsResilienceHub.DescribeAppVersionResourcesResolutionStatusRequest(); // DescribeAppVersionResourcesResolutionStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppVersionResourcesResolutionStatus(describeAppVersionResourcesResolutionStatusRequest, opts, (error, data, response) => {
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
 **describeAppVersionResourcesResolutionStatusRequest** | [**DescribeAppVersionResourcesResolutionStatusRequest**](DescribeAppVersionResourcesResolutionStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppVersionResourcesResolutionStatusResponse**](DescribeAppVersionResourcesResolutionStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAppVersionTemplate

> DescribeAppVersionTemplateResponse describeAppVersionTemplate(describeAppVersionTemplateRequest, opts)



Describes details about an Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppVersionTemplateRequest = new AwsResilienceHub.DescribeAppVersionTemplateRequest(); // DescribeAppVersionTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppVersionTemplate(describeAppVersionTemplateRequest, opts, (error, data, response) => {
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
 **describeAppVersionTemplateRequest** | [**DescribeAppVersionTemplateRequest**](DescribeAppVersionTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppVersionTemplateResponse**](DescribeAppVersionTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeDraftAppVersionResourcesImportStatus

> DescribeDraftAppVersionResourcesImportStatusResponse describeDraftAppVersionResourcesImportStatus(describeAppRequest, opts)



&lt;p&gt;Describes the status of importing resources to an application version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you get a 404 error with &lt;code&gt;ResourceImportStatusNotFoundAppMetadataException&lt;/code&gt;, you must call &lt;code&gt;importResourcesToDraftAppVersion&lt;/code&gt; after creating the application and before calling &lt;code&gt;describeDraftAppVersionResourcesImportStatus&lt;/code&gt; to obtain the status.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppRequest = new AwsResilienceHub.DescribeAppRequest(); // DescribeAppRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDraftAppVersionResourcesImportStatus(describeAppRequest, opts, (error, data, response) => {
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
 **describeAppRequest** | [**DescribeAppRequest**](DescribeAppRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDraftAppVersionResourcesImportStatusResponse**](DescribeDraftAppVersionResourcesImportStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeResiliencyPolicy

> DescribeResiliencyPolicyResponse describeResiliencyPolicy(describeResiliencyPolicyRequest, opts)



Describes a specified resiliency policy for an Resilience Hub application. The returned policy object includes creation time, data location constraints, the Amazon Resource Name (ARN) for the policy, tags, tier, and more.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeResiliencyPolicyRequest = new AwsResilienceHub.DescribeResiliencyPolicyRequest(); // DescribeResiliencyPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeResiliencyPolicy(describeResiliencyPolicyRequest, opts, (error, data, response) => {
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
 **describeResiliencyPolicyRequest** | [**DescribeResiliencyPolicyRequest**](DescribeResiliencyPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeResiliencyPolicyResponse**](DescribeResiliencyPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importResourcesToDraftAppVersion

> ImportResourcesToDraftAppVersionResponse importResourcesToDraftAppVersion(importResourcesToDraftAppVersionRequest, opts)



Imports resources to Resilience Hub application draft version from different input sources. For more information about the input sources supported by Resilience Hub, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html\&quot;&gt;Discover the structure and describe your Resilience Hub application&lt;/a&gt;.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let importResourcesToDraftAppVersionRequest = new AwsResilienceHub.ImportResourcesToDraftAppVersionRequest(); // ImportResourcesToDraftAppVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.importResourcesToDraftAppVersion(importResourcesToDraftAppVersionRequest, opts, (error, data, response) => {
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
 **importResourcesToDraftAppVersionRequest** | [**ImportResourcesToDraftAppVersionRequest**](ImportResourcesToDraftAppVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ImportResourcesToDraftAppVersionResponse**](ImportResourcesToDraftAppVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAlarmRecommendations

> ListAlarmRecommendationsResponse listAlarmRecommendations(listAlarmRecommendationsRequest, opts)



Lists the alarm recommendations for an Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAlarmRecommendationsRequest = new AwsResilienceHub.ListAlarmRecommendationsRequest(); // ListAlarmRecommendationsRequest | 
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
apiInstance.listAlarmRecommendations(listAlarmRecommendationsRequest, opts, (error, data, response) => {
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
 **listAlarmRecommendationsRequest** | [**ListAlarmRecommendationsRequest**](ListAlarmRecommendationsRequest.md)|  | 
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

[**ListAlarmRecommendationsResponse**](ListAlarmRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppAssessmentComplianceDrifts

> ListAppAssessmentComplianceDriftsResponse listAppAssessmentComplianceDrifts(listAppAssessmentComplianceDriftsRequest, opts)



List of compliance drifts that were detected while running an assessment.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAppAssessmentComplianceDriftsRequest = new AwsResilienceHub.ListAppAssessmentComplianceDriftsRequest(); // ListAppAssessmentComplianceDriftsRequest | 
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
apiInstance.listAppAssessmentComplianceDrifts(listAppAssessmentComplianceDriftsRequest, opts, (error, data, response) => {
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
 **listAppAssessmentComplianceDriftsRequest** | [**ListAppAssessmentComplianceDriftsRequest**](ListAppAssessmentComplianceDriftsRequest.md)|  | 
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

[**ListAppAssessmentComplianceDriftsResponse**](ListAppAssessmentComplianceDriftsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppAssessments

> ListAppAssessmentsResponse listAppAssessments(opts)



Lists the assessments for an Resilience Hub application. You can use request parameters to refine the results for the response object.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'appArn': "appArn_example", // String | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i> guide.
  'assessmentName': "assessmentName_example", // String | The name for the assessment.
  'assessmentStatus': [new AwsResilienceHub.AssessmentStatus()], // [AssessmentStatus] | The current status of the assessment for the resiliency policy.
  'complianceStatus': "complianceStatus_example", // String | The current status of compliance for the resiliency policy.
  'invoker': "invoker_example", // String | Specifies the entity that invoked a specific assessment, either a <code>User</code> or the <code>System</code>.
  'maxResults': 56, // Number | Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.
  'nextToken': "nextToken_example", // String | Null, or the token from a previous call to get the next set of results.
  'reverseOrder': true // Boolean | The default is to sort by ascending <b>startTime</b>. To sort by descending <b>startTime</b>, set reverseOrder to <code>true</code>.
};
apiInstance.listAppAssessments(opts, (error, data, response) => {
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
 **appArn** | **String**| Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. | [optional] 
 **assessmentName** | **String**| The name for the assessment. | [optional] 
 **assessmentStatus** | [**[AssessmentStatus]**](AssessmentStatus.md)| The current status of the assessment for the resiliency policy. | [optional] 
 **complianceStatus** | **String**| The current status of compliance for the resiliency policy. | [optional] 
 **invoker** | **String**| Specifies the entity that invoked a specific assessment, either a &lt;code&gt;User&lt;/code&gt; or the &lt;code&gt;System&lt;/code&gt;. | [optional] 
 **maxResults** | **Number**| Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved. | [optional] 
 **nextToken** | **String**| Null, or the token from a previous call to get the next set of results. | [optional] 
 **reverseOrder** | **Boolean**| The default is to sort by ascending &lt;b&gt;startTime&lt;/b&gt;. To sort by descending &lt;b&gt;startTime&lt;/b&gt;, set reverseOrder to &lt;code&gt;true&lt;/code&gt;. | [optional] 

### Return type

[**ListAppAssessmentsResponse**](ListAppAssessmentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppComponentCompliances

> ListAppComponentCompliancesResponse listAppComponentCompliances(listAlarmRecommendationsRequest, opts)



Lists the compliances for an Resilience Hub Application Component.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAlarmRecommendationsRequest = new AwsResilienceHub.ListAlarmRecommendationsRequest(); // ListAlarmRecommendationsRequest | 
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
apiInstance.listAppComponentCompliances(listAlarmRecommendationsRequest, opts, (error, data, response) => {
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
 **listAlarmRecommendationsRequest** | [**ListAlarmRecommendationsRequest**](ListAlarmRecommendationsRequest.md)|  | 
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

[**ListAppComponentCompliancesResponse**](ListAppComponentCompliancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppComponentRecommendations

> ListAppComponentRecommendationsResponse listAppComponentRecommendations(listAlarmRecommendationsRequest, opts)



Lists the recommendations for an Resilience Hub Application Component.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAlarmRecommendationsRequest = new AwsResilienceHub.ListAlarmRecommendationsRequest(); // ListAlarmRecommendationsRequest | 
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
apiInstance.listAppComponentRecommendations(listAlarmRecommendationsRequest, opts, (error, data, response) => {
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
 **listAlarmRecommendationsRequest** | [**ListAlarmRecommendationsRequest**](ListAlarmRecommendationsRequest.md)|  | 
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

[**ListAppComponentRecommendationsResponse**](ListAppComponentRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppInputSources

> ListAppInputSourcesResponse listAppInputSources(listAppInputSourcesRequest, opts)



Lists all the input sources of the Resilience Hub application. For more information about the input sources supported by Resilience Hub, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html\&quot;&gt;Discover the structure and describe your Resilience Hub application&lt;/a&gt;.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAppInputSourcesRequest = new AwsResilienceHub.ListAppInputSourcesRequest(); // ListAppInputSourcesRequest | 
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
apiInstance.listAppInputSources(listAppInputSourcesRequest, opts, (error, data, response) => {
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
 **listAppInputSourcesRequest** | [**ListAppInputSourcesRequest**](ListAppInputSourcesRequest.md)|  | 
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

[**ListAppInputSourcesResponse**](ListAppInputSourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppVersionAppComponents

> ListAppVersionAppComponentsResponse listAppVersionAppComponents(listAppVersionAppComponentsRequest, opts)



Lists all the Application Components in the Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAppVersionAppComponentsRequest = new AwsResilienceHub.ListAppVersionAppComponentsRequest(); // ListAppVersionAppComponentsRequest | 
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
apiInstance.listAppVersionAppComponents(listAppVersionAppComponentsRequest, opts, (error, data, response) => {
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
 **listAppVersionAppComponentsRequest** | [**ListAppVersionAppComponentsRequest**](ListAppVersionAppComponentsRequest.md)|  | 
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

[**ListAppVersionAppComponentsResponse**](ListAppVersionAppComponentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppVersionResourceMappings

> ListAppVersionResourceMappingsResponse listAppVersionResourceMappings(listAppVersionResourceMappingsRequest, opts)



Lists how the resources in an application version are mapped/sourced from. Mappings can be physical resource identifiers, CloudFormation stacks, resource-groups, or an application registry app.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAppVersionResourceMappingsRequest = new AwsResilienceHub.ListAppVersionResourceMappingsRequest(); // ListAppVersionResourceMappingsRequest | 
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
apiInstance.listAppVersionResourceMappings(listAppVersionResourceMappingsRequest, opts, (error, data, response) => {
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
 **listAppVersionResourceMappingsRequest** | [**ListAppVersionResourceMappingsRequest**](ListAppVersionResourceMappingsRequest.md)|  | 
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

[**ListAppVersionResourceMappingsResponse**](ListAppVersionResourceMappingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppVersionResources

> ListAppVersionResourcesResponse listAppVersionResources(listAppVersionResourcesRequest, opts)



Lists all the resources in an Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAppVersionResourcesRequest = new AwsResilienceHub.ListAppVersionResourcesRequest(); // ListAppVersionResourcesRequest | 
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
apiInstance.listAppVersionResources(listAppVersionResourcesRequest, opts, (error, data, response) => {
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
 **listAppVersionResourcesRequest** | [**ListAppVersionResourcesRequest**](ListAppVersionResourcesRequest.md)|  | 
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

[**ListAppVersionResourcesResponse**](ListAppVersionResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppVersions

> ListAppVersionsResponse listAppVersions(listAppVersionsRequest, opts)



Lists the different versions for the Resilience Hub applications.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAppVersionsRequest = new AwsResilienceHub.ListAppVersionsRequest(); // ListAppVersionsRequest | 
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
apiInstance.listAppVersions(listAppVersionsRequest, opts, (error, data, response) => {
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
 **listAppVersionsRequest** | [**ListAppVersionsRequest**](ListAppVersionsRequest.md)|  | 
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

[**ListAppVersionsResponse**](ListAppVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listApps

> ListAppsResponse listApps(opts)



&lt;p&gt;Lists your Resilience Hub applications.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can filter applications using only one filter at a time or without using any filter. If you try to filter applications using multiple filters, you will get the following error:&lt;/p&gt; &lt;p&gt; &lt;code&gt;An error occurred (ValidationException) when calling the ListApps operation: Only one filter is supported for this operation.&lt;/code&gt; &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'appArn': "appArn_example", // String | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i> guide.
  'maxResults': 56, // Number | Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.
  'name': "name_example", // String | The name for the one of the listed applications.
  'nextToken': "nextToken_example" // String | Null, or the token from a previous call to get the next set of results.
};
apiInstance.listApps(opts, (error, data, response) => {
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
 **appArn** | **String**| Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. | [optional] 
 **maxResults** | **Number**| Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved. | [optional] 
 **name** | **String**| The name for the one of the listed applications. | [optional] 
 **nextToken** | **String**| Null, or the token from a previous call to get the next set of results. | [optional] 

### Return type

[**ListAppsResponse**](ListAppsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRecommendationTemplates

> ListRecommendationTemplatesResponse listRecommendationTemplates(assessmentArn, opts)



Lists the recommendation templates for the Resilience Hub applications.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let assessmentArn = "assessmentArn_example"; // String | Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i> guide.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.
  'name': "name_example", // String | The name for one of the listed recommendation templates.
  'nextToken': "nextToken_example", // String | Null, or the token from a previous call to get the next set of results.
  'recommendationTemplateArn': "recommendationTemplateArn_example", // String | The Amazon Resource Name (ARN) for a recommendation template.
  'reverseOrder': true, // Boolean | The default is to sort by ascending <b>startTime</b>. To sort by descending <b>startTime</b>, set reverseOrder to <code>true</code>.
  'status': [new AwsResilienceHub.RecommendationTemplateStatus()] // [RecommendationTemplateStatus] | Status of the action.
};
apiInstance.listRecommendationTemplates(assessmentArn, opts, (error, data, response) => {
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
 **assessmentArn** | **String**| Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app-assessment/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved. | [optional] 
 **name** | **String**| The name for one of the listed recommendation templates. | [optional] 
 **nextToken** | **String**| Null, or the token from a previous call to get the next set of results. | [optional] 
 **recommendationTemplateArn** | **String**| The Amazon Resource Name (ARN) for a recommendation template. | [optional] 
 **reverseOrder** | **Boolean**| The default is to sort by ascending &lt;b&gt;startTime&lt;/b&gt;. To sort by descending &lt;b&gt;startTime&lt;/b&gt;, set reverseOrder to &lt;code&gt;true&lt;/code&gt;. | [optional] 
 **status** | [**[RecommendationTemplateStatus]**](RecommendationTemplateStatus.md)| Status of the action. | [optional] 

### Return type

[**ListRecommendationTemplatesResponse**](ListRecommendationTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listResiliencyPolicies

> ListResiliencyPoliciesResponse listResiliencyPolicies(opts)



Lists the resiliency policies for the Resilience Hub applications.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.
  'nextToken': "nextToken_example", // String | Null, or the token from a previous call to get the next set of results.
  'policyName': "policyName_example" // String | The name of the policy
};
apiInstance.listResiliencyPolicies(opts, (error, data, response) => {
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
 **maxResults** | **Number**| Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved. | [optional] 
 **nextToken** | **String**| Null, or the token from a previous call to get the next set of results. | [optional] 
 **policyName** | **String**| The name of the policy | [optional] 

### Return type

[**ListResiliencyPoliciesResponse**](ListResiliencyPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSopRecommendations

> ListSopRecommendationsResponse listSopRecommendations(listAlarmRecommendationsRequest, opts)



Lists the standard operating procedure (SOP) recommendations for the Resilience Hub applications.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAlarmRecommendationsRequest = new AwsResilienceHub.ListAlarmRecommendationsRequest(); // ListAlarmRecommendationsRequest | 
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
apiInstance.listSopRecommendations(listAlarmRecommendationsRequest, opts, (error, data, response) => {
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
 **listAlarmRecommendationsRequest** | [**ListAlarmRecommendationsRequest**](ListAlarmRecommendationsRequest.md)|  | 
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

[**ListSopRecommendationsResponse**](ListSopRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSuggestedResiliencyPolicies

> ListSuggestedResiliencyPoliciesResponse listSuggestedResiliencyPolicies(opts)



Lists the suggested resiliency policies for the Resilience Hub applications.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.
  'nextToken': "nextToken_example" // String | Null, or the token from a previous call to get the next set of results.
};
apiInstance.listSuggestedResiliencyPolicies(opts, (error, data, response) => {
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
 **maxResults** | **Number**| Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved. | [optional] 
 **nextToken** | **String**| Null, or the token from a previous call to get the next set of results. | [optional] 

### Return type

[**ListSuggestedResiliencyPoliciesResponse**](ListSuggestedResiliencyPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags for your resources in your Resilience Hub applications.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) for a specific resource in your Resilience Hub application.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) for a specific resource in your Resilience Hub application. | 
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


## listTestRecommendations

> ListTestRecommendationsResponse listTestRecommendations(listAlarmRecommendationsRequest, opts)



Lists the test recommendations for the Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAlarmRecommendationsRequest = new AwsResilienceHub.ListAlarmRecommendationsRequest(); // ListAlarmRecommendationsRequest | 
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
apiInstance.listTestRecommendations(listAlarmRecommendationsRequest, opts, (error, data, response) => {
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
 **listAlarmRecommendationsRequest** | [**ListAlarmRecommendationsRequest**](ListAlarmRecommendationsRequest.md)|  | 
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

[**ListTestRecommendationsResponse**](ListTestRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listUnsupportedAppVersionResources

> ListUnsupportedAppVersionResourcesResponse listUnsupportedAppVersionResources(listAppVersionResourcesRequest, opts)



Lists the resources that are not currently supported in Resilience Hub. An unsupported resource is a resource that exists in the object that was used to create an app, but is not supported by Resilience Hub.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let listAppVersionResourcesRequest = new AwsResilienceHub.ListAppVersionResourcesRequest(); // ListAppVersionResourcesRequest | 
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
apiInstance.listUnsupportedAppVersionResources(listAppVersionResourcesRequest, opts, (error, data, response) => {
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
 **listAppVersionResourcesRequest** | [**ListAppVersionResourcesRequest**](ListAppVersionResourcesRequest.md)|  | 
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

[**ListUnsupportedAppVersionResourcesResponse**](ListUnsupportedAppVersionResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## publishAppVersion

> PublishAppVersionResponse publishAppVersion(publishAppVersionRequest, opts)



Publishes a new version of a specific Resilience Hub application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let publishAppVersionRequest = new AwsResilienceHub.PublishAppVersionRequest(); // PublishAppVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.publishAppVersion(publishAppVersionRequest, opts, (error, data, response) => {
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
 **publishAppVersionRequest** | [**PublishAppVersionRequest**](PublishAppVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PublishAppVersionResponse**](PublishAppVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDraftAppVersionTemplate

> PutDraftAppVersionTemplateResponse putDraftAppVersionTemplate(putDraftAppVersionTemplateRequest, opts)



Adds or updates the app template for an Resilience Hub application draft version.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let putDraftAppVersionTemplateRequest = new AwsResilienceHub.PutDraftAppVersionTemplateRequest(); // PutDraftAppVersionTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putDraftAppVersionTemplate(putDraftAppVersionTemplateRequest, opts, (error, data, response) => {
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
 **putDraftAppVersionTemplateRequest** | [**PutDraftAppVersionTemplateRequest**](PutDraftAppVersionTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutDraftAppVersionTemplateResponse**](PutDraftAppVersionTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeDraftAppVersionResourceMappings

> RemoveDraftAppVersionResourceMappingsResponse removeDraftAppVersionResourceMappings(removeDraftAppVersionResourceMappingsRequest, opts)



Removes resource mappings from a draft application version.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let removeDraftAppVersionResourceMappingsRequest = new AwsResilienceHub.RemoveDraftAppVersionResourceMappingsRequest(); // RemoveDraftAppVersionResourceMappingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeDraftAppVersionResourceMappings(removeDraftAppVersionResourceMappingsRequest, opts, (error, data, response) => {
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
 **removeDraftAppVersionResourceMappingsRequest** | [**RemoveDraftAppVersionResourceMappingsRequest**](RemoveDraftAppVersionResourceMappingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RemoveDraftAppVersionResourceMappingsResponse**](RemoveDraftAppVersionResourceMappingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resolveAppVersionResources

> ResolveAppVersionResourcesResponse resolveAppVersionResources(describeAppVersionTemplateRequest, opts)



Resolves the resources for an application version.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let describeAppVersionTemplateRequest = new AwsResilienceHub.DescribeAppVersionTemplateRequest(); // DescribeAppVersionTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resolveAppVersionResources(describeAppVersionTemplateRequest, opts, (error, data, response) => {
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
 **describeAppVersionTemplateRequest** | [**DescribeAppVersionTemplateRequest**](DescribeAppVersionTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ResolveAppVersionResourcesResponse**](ResolveAppVersionResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startAppAssessment

> StartAppAssessmentResponse startAppAssessment(startAppAssessmentRequest, opts)



Creates a new application assessment for an application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let startAppAssessmentRequest = new AwsResilienceHub.StartAppAssessmentRequest(); // StartAppAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startAppAssessment(startAppAssessmentRequest, opts, (error, data, response) => {
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
 **startAppAssessmentRequest** | [**StartAppAssessmentRequest**](StartAppAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartAppAssessmentResponse**](StartAppAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Applies one or more tags to a resource.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let resourceArn = "resourceArn_example"; // String | Amazon Resource Name (ARN) of the resource. 
let tagResourceRequest = new AwsResilienceHub.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| Amazon Resource Name (ARN) of the resource.  | 
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



Removes one or more tags from a resource.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let resourceArn = "resourceArn_example"; // String | Amazon Resource Name (ARN) of the resource. 
let tagKeys = ["null"]; // [String] | The keys of the tags you want to remove.
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
 **resourceArn** | **String**| Amazon Resource Name (ARN) of the resource.  | 
 **tagKeys** | [**[String]**](String.md)| The keys of the tags you want to remove. | 
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


## updateApp

> UpdateAppResponse updateApp(updateAppRequest, opts)



Updates an application.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let updateAppRequest = new AwsResilienceHub.UpdateAppRequest(); // UpdateAppRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApp(updateAppRequest, opts, (error, data, response) => {
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
 **updateAppRequest** | [**UpdateAppRequest**](UpdateAppRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAppResponse**](UpdateAppResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAppVersion

> UpdateAppVersionResponse updateAppVersion(updateAppVersionRequest, opts)



&lt;p&gt;Updates the Resilience Hub application version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this information for running resiliency assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let updateAppVersionRequest = new AwsResilienceHub.UpdateAppVersionRequest(); // UpdateAppVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAppVersion(updateAppVersionRequest, opts, (error, data, response) => {
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
 **updateAppVersionRequest** | [**UpdateAppVersionRequest**](UpdateAppVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAppVersionResponse**](UpdateAppVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAppVersionAppComponent

> UpdateAppVersionAppComponentResponse updateAppVersionAppComponent(updateAppVersionAppComponentRequest, opts)



&lt;p&gt;Updates an existing Application Component in the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let updateAppVersionAppComponentRequest = new AwsResilienceHub.UpdateAppVersionAppComponentRequest(); // UpdateAppVersionAppComponentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAppVersionAppComponent(updateAppVersionAppComponentRequest, opts, (error, data, response) => {
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
 **updateAppVersionAppComponentRequest** | [**UpdateAppVersionAppComponentRequest**](UpdateAppVersionAppComponentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAppVersionAppComponentResponse**](UpdateAppVersionAppComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAppVersionResource

> UpdateAppVersionResourceResponse updateAppVersionResource(updateAppVersionResourceRequest, opts)



&lt;p&gt;Updates the resource details in the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This action has no effect outside Resilience Hub.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To update application version with new &lt;code&gt;physicalResourceID&lt;/code&gt;, you must call &lt;code&gt;ResolveAppVersionResources&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let updateAppVersionResourceRequest = new AwsResilienceHub.UpdateAppVersionResourceRequest(); // UpdateAppVersionResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAppVersionResource(updateAppVersionResourceRequest, opts, (error, data, response) => {
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
 **updateAppVersionResourceRequest** | [**UpdateAppVersionResourceRequest**](UpdateAppVersionResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAppVersionResourceResponse**](UpdateAppVersionResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateResiliencyPolicy

> UpdateResiliencyPolicyResponse updateResiliencyPolicy(updateResiliencyPolicyRequest, opts)



Updates a resiliency policy.

### Example

```javascript
import AwsResilienceHub from 'aws_resilience_hub';
let defaultClient = AwsResilienceHub.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResilienceHub.DefaultApi();
let updateResiliencyPolicyRequest = new AwsResilienceHub.UpdateResiliencyPolicyRequest(); // UpdateResiliencyPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateResiliencyPolicy(updateResiliencyPolicyRequest, opts, (error, data, response) => {
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
 **updateResiliencyPolicyRequest** | [**UpdateResiliencyPolicyRequest**](UpdateResiliencyPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateResiliencyPolicyResponse**](UpdateResiliencyPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

