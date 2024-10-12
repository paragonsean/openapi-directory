# AmazonCloudWatchEvidently.DefaultApi

All URIs are relative to *http://evidently.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchEvaluateFeature**](DefaultApi.md#batchEvaluateFeature) | **POST** /projects/{project}/evaluations | 
[**createExperiment**](DefaultApi.md#createExperiment) | **POST** /projects/{project}/experiments | 
[**createFeature**](DefaultApi.md#createFeature) | **POST** /projects/{project}/features | 
[**createLaunch**](DefaultApi.md#createLaunch) | **POST** /projects/{project}/launches | 
[**createProject**](DefaultApi.md#createProject) | **POST** /projects | 
[**createSegment**](DefaultApi.md#createSegment) | **POST** /segments | 
[**deleteExperiment**](DefaultApi.md#deleteExperiment) | **DELETE** /projects/{project}/experiments/{experiment} | 
[**deleteFeature**](DefaultApi.md#deleteFeature) | **DELETE** /projects/{project}/features/{feature} | 
[**deleteLaunch**](DefaultApi.md#deleteLaunch) | **DELETE** /projects/{project}/launches/{launch} | 
[**deleteProject**](DefaultApi.md#deleteProject) | **DELETE** /projects/{project} | 
[**deleteSegment**](DefaultApi.md#deleteSegment) | **DELETE** /segments/{segment} | 
[**evaluateFeature**](DefaultApi.md#evaluateFeature) | **POST** /projects/{project}/evaluations/{feature} | 
[**getExperiment**](DefaultApi.md#getExperiment) | **GET** /projects/{project}/experiments/{experiment} | 
[**getExperimentResults**](DefaultApi.md#getExperimentResults) | **POST** /projects/{project}/experiments/{experiment}/results | 
[**getFeature**](DefaultApi.md#getFeature) | **GET** /projects/{project}/features/{feature} | 
[**getLaunch**](DefaultApi.md#getLaunch) | **GET** /projects/{project}/launches/{launch} | 
[**getProject**](DefaultApi.md#getProject) | **GET** /projects/{project} | 
[**getSegment**](DefaultApi.md#getSegment) | **GET** /segments/{segment} | 
[**listExperiments**](DefaultApi.md#listExperiments) | **GET** /projects/{project}/experiments | 
[**listFeatures**](DefaultApi.md#listFeatures) | **GET** /projects/{project}/features | 
[**listLaunches**](DefaultApi.md#listLaunches) | **GET** /projects/{project}/launches | 
[**listProjects**](DefaultApi.md#listProjects) | **GET** /projects | 
[**listSegmentReferences**](DefaultApi.md#listSegmentReferences) | **GET** /segments/{segment}/references#type | 
[**listSegments**](DefaultApi.md#listSegments) | **GET** /segments | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**putProjectEvents**](DefaultApi.md#putProjectEvents) | **POST** /events/projects/{project} | 
[**startExperiment**](DefaultApi.md#startExperiment) | **POST** /projects/{project}/experiments/{experiment}/start | 
[**startLaunch**](DefaultApi.md#startLaunch) | **POST** /projects/{project}/launches/{launch}/start | 
[**stopExperiment**](DefaultApi.md#stopExperiment) | **POST** /projects/{project}/experiments/{experiment}/cancel | 
[**stopLaunch**](DefaultApi.md#stopLaunch) | **POST** /projects/{project}/launches/{launch}/cancel | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**testSegmentPattern**](DefaultApi.md#testSegmentPattern) | **POST** /test-segment-pattern | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateExperiment**](DefaultApi.md#updateExperiment) | **PATCH** /projects/{project}/experiments/{experiment} | 
[**updateFeature**](DefaultApi.md#updateFeature) | **PATCH** /projects/{project}/features/{feature} | 
[**updateLaunch**](DefaultApi.md#updateLaunch) | **PATCH** /projects/{project}/launches/{launch} | 
[**updateProject**](DefaultApi.md#updateProject) | **PATCH** /projects/{project} | 
[**updateProjectDataDelivery**](DefaultApi.md#updateProjectDataDelivery) | **PATCH** /projects/{project}/data-delivery | 



## batchEvaluateFeature

> BatchEvaluateFeatureResponse batchEvaluateFeature(project, batchEvaluateFeatureRequest, opts)



&lt;p&gt;This operation assigns feature variation to user sessions. For each user session, you pass in an &lt;code&gt;entityID&lt;/code&gt; that represents the user. Evidently then checks the evaluation rules and assigns the variation.&lt;/p&gt; &lt;p&gt;The first rules that are evaluated are the override rules. If the user&#39;s &lt;code&gt;entityID&lt;/code&gt; matches an override rule, the user is served the variation specified by that rule.&lt;/p&gt; &lt;p&gt;Next, if there is a launch of the feature, the user might be assigned to a variation in the launch. The chance of this depends on the percentage of users that are allocated to that launch. If the user is enrolled in the launch, the variation they are served depends on the allocation of the various feature variations used for the launch.&lt;/p&gt; &lt;p&gt;If the user is not assigned to a launch, and there is an ongoing experiment for this feature, the user might be assigned to a variation in the experiment. The chance of this depends on the percentage of users that are allocated to that experiment. If the user is enrolled in the experiment, the variation they are served depends on the allocation of the various feature variations used for the experiment. &lt;/p&gt; &lt;p&gt;If the user is not assigned to a launch or experiment, they are served the default variation.&lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project that contains the feature being evaluated.
let batchEvaluateFeatureRequest = new AmazonCloudWatchEvidently.BatchEvaluateFeatureRequest(); // BatchEvaluateFeatureRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchEvaluateFeature(project, batchEvaluateFeatureRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project that contains the feature being evaluated. | 
 **batchEvaluateFeatureRequest** | [**BatchEvaluateFeatureRequest**](BatchEvaluateFeatureRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchEvaluateFeatureResponse**](BatchEvaluateFeatureResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExperiment

> CreateExperimentResponse createExperiment(project, createExperimentRequest, opts)



&lt;p&gt;Creates an Evidently &lt;i&gt;experiment&lt;/i&gt;. Before you create an experiment, you must create the feature to use for the experiment.&lt;/p&gt; &lt;p&gt;An experiment helps you make feature design decisions based on evidence and data. An experiment can test as many as five variations at once. Evidently collects experiment data and analyzes it by statistical methods, and provides clear recommendations about which variations perform better.&lt;/p&gt; &lt;p&gt;You can optionally specify a &lt;code&gt;segment&lt;/code&gt; to have the experiment consider only certain audience types in the experiment, such as using only user sessions from a certain location or who use a certain internet browser.&lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update an existing experiment. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateExperiment.html\&quot;&gt;UpdateExperiment&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project that you want to create the new experiment in.
let createExperimentRequest = new AmazonCloudWatchEvidently.CreateExperimentRequest(); // CreateExperimentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createExperiment(project, createExperimentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project that you want to create the new experiment in. | 
 **createExperimentRequest** | [**CreateExperimentRequest**](CreateExperimentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateExperimentResponse**](CreateExperimentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFeature

> CreateFeatureResponse createFeature(project, createFeatureRequest, opts)



&lt;p&gt;Creates an Evidently &lt;i&gt;feature&lt;/i&gt; that you want to launch or test. You can define up to five variations of a feature, and use these variations in your launches and experiments. A feature must be created in a project. For information about creating a project, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateProject.html\&quot;&gt;CreateProject&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update an existing feature. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateFeature.html\&quot;&gt;UpdateFeature&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project that is to contain the new feature.
let createFeatureRequest = new AmazonCloudWatchEvidently.CreateFeatureRequest(); // CreateFeatureRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFeature(project, createFeatureRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project that is to contain the new feature. | 
 **createFeatureRequest** | [**CreateFeatureRequest**](CreateFeatureRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateFeatureResponse**](CreateFeatureResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLaunch

> CreateLaunchResponse createLaunch(project, createLaunchRequest, opts)



&lt;p&gt;Creates a &lt;i&gt;launch&lt;/i&gt; of a given feature. Before you create a launch, you must create the feature to use for the launch.&lt;/p&gt; &lt;p&gt;You can use a launch to safely validate new features by serving them to a specified percentage of your users while you roll out the feature. You can monitor the performance of the new feature to help you decide when to ramp up traffic to more users. This helps you reduce risk and identify unintended consequences before you fully launch the feature.&lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update an existing launch. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateLaunch.html\&quot;&gt;UpdateLaunch&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project that you want to create the launch in.
let createLaunchRequest = new AmazonCloudWatchEvidently.CreateLaunchRequest(); // CreateLaunchRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLaunch(project, createLaunchRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project that you want to create the launch in. | 
 **createLaunchRequest** | [**CreateLaunchRequest**](CreateLaunchRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLaunchResponse**](CreateLaunchResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProject

> CreateProjectResponse createProject(createProjectRequest, opts)



&lt;p&gt;Creates a project, which is the logical object in Evidently that can contain features, launches, and experiments. Use projects to group similar features together.&lt;/p&gt; &lt;p&gt;To update an existing project, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProject.html\&quot;&gt;UpdateProject&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let createProjectRequest = new AmazonCloudWatchEvidently.CreateProjectRequest(); // CreateProjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createProject(createProjectRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createProjectRequest** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSegment

> CreateSegmentResponse createSegment(createSegmentRequest, opts)



&lt;p&gt;Use this operation to define a &lt;i&gt;segment&lt;/i&gt; of your audience. A segment is a portion of your audience that share one or more characteristics. Examples could be Chrome browser users, users in Europe, or Firefox browser users in Europe who also fit other criteria that your application collects, such as age.&lt;/p&gt; &lt;p&gt;Using a segment in an experiment limits that experiment to evaluate only the users who match the segment criteria. Using one or more segments in a launch allows you to define different traffic splits for the different audience segments.&lt;/p&gt; &lt;p&gt;For more information about segment pattern syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax.html\&quot;&gt; Segment rule pattern syntax&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The pattern that you define for a segment is matched against the value of &lt;code&gt;evaluationContext&lt;/code&gt;, which is passed into Evidently in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html\&quot;&gt;EvaluateFeature&lt;/a&gt; operation, when Evidently assigns a feature variation to a user.&lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let createSegmentRequest = new AmazonCloudWatchEvidently.CreateSegmentRequest(); // CreateSegmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSegment(createSegmentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createSegmentRequest** | [**CreateSegmentRequest**](CreateSegmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSegmentResponse**](CreateSegmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteExperiment

> Object deleteExperiment(experiment, project, opts)



&lt;p&gt;Deletes an Evidently experiment. The feature used for the experiment is not deleted.&lt;/p&gt; &lt;p&gt;To stop an experiment without deleting it, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_StopExperiment.html\&quot;&gt;StopExperiment&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let experiment = "experiment_example"; // String | The name of the experiment to delete.
let project = "project_example"; // String | The name or ARN of the project that contains the experiment to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteExperiment(experiment, project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **String**| The name of the experiment to delete. | 
 **project** | **String**| The name or ARN of the project that contains the experiment to delete. | 
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


## deleteFeature

> Object deleteFeature(feature, project, opts)



Deletes an Evidently feature.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let feature = "feature_example"; // String | The name of the feature to delete.
let project = "project_example"; // String | The name or ARN of the project that contains the feature to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteFeature(feature, project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **String**| The name of the feature to delete. | 
 **project** | **String**| The name or ARN of the project that contains the feature to delete. | 
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


## deleteLaunch

> Object deleteLaunch(launch, project, opts)



&lt;p&gt;Deletes an Evidently launch. The feature used for the launch is not deleted.&lt;/p&gt; &lt;p&gt;To stop a launch without deleting it, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_StopLaunch.html\&quot;&gt;StopLaunch&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let launch = "launch_example"; // String | The name of the launch to delete.
let project = "project_example"; // String | The name or ARN of the project that contains the launch to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLaunch(launch, project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch** | **String**| The name of the launch to delete. | 
 **project** | **String**| The name or ARN of the project that contains the launch to delete. | 
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


## deleteProject

> Object deleteProject(project, opts)



Deletes an Evidently project. Before you can delete a project, you must delete all the features that the project contains. To delete a feature, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteFeature.html\&quot;&gt;DeleteFeature&lt;/a&gt;.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProject(project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project to delete. | 
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


## deleteSegment

> Object deleteSegment(segment, opts)



Deletes a segment. You can&#39;t delete a segment that is being used in a launch or experiment, even if that launch or experiment is not currently running.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let segment = "segment_example"; // String | Specifies the segment to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSegment(segment, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **String**| Specifies the segment to delete. | 
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


## evaluateFeature

> EvaluateFeatureResponse evaluateFeature(feature, project, evaluateFeatureRequest, opts)



&lt;p&gt;This operation assigns a feature variation to one given user session. You pass in an &lt;code&gt;entityID&lt;/code&gt; that represents the user. Evidently then checks the evaluation rules and assigns the variation.&lt;/p&gt; &lt;p&gt;The first rules that are evaluated are the override rules. If the user&#39;s &lt;code&gt;entityID&lt;/code&gt; matches an override rule, the user is served the variation specified by that rule.&lt;/p&gt; &lt;p&gt;If there is a current launch with this feature that uses segment overrides, and if the user session&#39;s &lt;code&gt;evaluationContext&lt;/code&gt; matches a segment rule defined in a segment override, the configuration in the segment overrides is used. For more information about segments, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateSegment.html\&quot;&gt;CreateSegment&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html\&quot;&gt;Use segments to focus your audience&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If there is a launch with no segment overrides, the user might be assigned to a variation in the launch. The chance of this depends on the percentage of users that are allocated to that launch. If the user is enrolled in the launch, the variation they are served depends on the allocation of the various feature variations used for the launch.&lt;/p&gt; &lt;p&gt;If the user is not assigned to a launch, and there is an ongoing experiment for this feature, the user might be assigned to a variation in the experiment. The chance of this depends on the percentage of users that are allocated to that experiment.&lt;/p&gt; &lt;p&gt;If the experiment uses a segment, then only user sessions with &lt;code&gt;evaluationContext&lt;/code&gt; values that match the segment rule are used in the experiment.&lt;/p&gt; &lt;p&gt;If the user is enrolled in the experiment, the variation they are served depends on the allocation of the various feature variations used for the experiment. &lt;/p&gt; &lt;p&gt;If the user is not assigned to a launch or experiment, they are served the default variation.&lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let feature = "feature_example"; // String | The name of the feature being evaluated.
let project = "project_example"; // String | The name or ARN of the project that contains this feature.
let evaluateFeatureRequest = new AmazonCloudWatchEvidently.EvaluateFeatureRequest(); // EvaluateFeatureRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.evaluateFeature(feature, project, evaluateFeatureRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **String**| The name of the feature being evaluated. | 
 **project** | **String**| The name or ARN of the project that contains this feature. | 
 **evaluateFeatureRequest** | [**EvaluateFeatureRequest**](EvaluateFeatureRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**EvaluateFeatureResponse**](EvaluateFeatureResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getExperiment

> GetExperimentResponse getExperiment(experiment, project, opts)



Returns the details about one experiment. You must already know the experiment name. To retrieve a list of experiments in your account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListExperiments.html\&quot;&gt;ListExperiments&lt;/a&gt;.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let experiment = "experiment_example"; // String | The name of the experiment that you want to see the details of.
let project = "project_example"; // String | The name or ARN of the project that contains the experiment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExperiment(experiment, project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **String**| The name of the experiment that you want to see the details of. | 
 **project** | **String**| The name or ARN of the project that contains the experiment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetExperimentResponse**](GetExperimentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExperimentResults

> GetExperimentResultsResponse getExperimentResults(experiment, project, getExperimentResultsRequest, opts)



&lt;p&gt;Retrieves the results of a running or completed experiment. No results are available until there have been 100 events for each variation and at least 10 minutes have passed since the start of the experiment. To increase the statistical power, Evidently performs an additional offline p-value analysis at the end of the experiment. Offline p-value analysis can detect statistical significance in some cases where the anytime p-values used during the experiment do not find statistical significance.&lt;/p&gt; &lt;p&gt;Experiment results are available up to 63 days after the start of the experiment. They are not available after that because of CloudWatch data retention policies.&lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let experiment = "experiment_example"; // String | The name of the experiment to retrieve the results of.
let project = "project_example"; // String | The name or ARN of the project that contains the experiment that you want to see the results of.
let getExperimentResultsRequest = new AmazonCloudWatchEvidently.GetExperimentResultsRequest(); // GetExperimentResultsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExperimentResults(experiment, project, getExperimentResultsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **String**| The name of the experiment to retrieve the results of. | 
 **project** | **String**| The name or ARN of the project that contains the experiment that you want to see the results of. | 
 **getExperimentResultsRequest** | [**GetExperimentResultsRequest**](GetExperimentResultsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetExperimentResultsResponse**](GetExperimentResultsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getFeature

> GetFeatureResponse getFeature(feature, project, opts)



Returns the details about one feature. You must already know the feature name. To retrieve a list of features in your account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListFeatures.html\&quot;&gt;ListFeatures&lt;/a&gt;.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let feature = "feature_example"; // String | The name of the feature that you want to retrieve information for.
let project = "project_example"; // String | The name or ARN of the project that contains the feature.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFeature(feature, project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **String**| The name of the feature that you want to retrieve information for. | 
 **project** | **String**| The name or ARN of the project that contains the feature. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFeatureResponse**](GetFeatureResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLaunch

> GetLaunchResponse getLaunch(launch, project, opts)



Returns the details about one launch. You must already know the launch name. To retrieve a list of launches in your account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListLaunches.html\&quot;&gt;ListLaunches&lt;/a&gt;.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let launch = "launch_example"; // String | The name of the launch that you want to see the details of.
let project = "project_example"; // String | The name or ARN of the project that contains the launch.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLaunch(launch, project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch** | **String**| The name of the launch that you want to see the details of. | 
 **project** | **String**| The name or ARN of the project that contains the launch. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLaunchResponse**](GetLaunchResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProject

> GetProjectResponse getProject(project, opts)



Returns the details about one launch. You must already know the project name. To retrieve a list of projects in your account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListProjects.html\&quot;&gt;ListProjects&lt;/a&gt;.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project that you want to see the details of.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getProject(project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project that you want to see the details of. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetProjectResponse**](GetProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSegment

> GetSegmentResponse getSegment(segment, opts)



Returns information about the specified segment. Specify the segment you want to view by specifying its ARN.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let segment = "segment_example"; // String | The ARN of the segment to return information for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSegment(segment, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **String**| The ARN of the segment to return information for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSegmentResponse**](GetSegmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExperiments

> ListExperimentsResponse listExperiments(project, opts)



Returns configuration details about all the experiments in the specified project.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project to return the experiment list from.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextToken': "nextToken_example", // String | The token to use when requesting the next set of results. You received this token from a previous <code>ListExperiments</code> operation.
  'status': "status_example" // String | Use this optional parameter to limit the returned results to only the experiments with the status that you specify here.
};
apiInstance.listExperiments(project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project to return the experiment list from. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextToken** | **String**| The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListExperiments&lt;/code&gt; operation. | [optional] 
 **status** | **String**| Use this optional parameter to limit the returned results to only the experiments with the status that you specify here. | [optional] 

### Return type

[**ListExperimentsResponse**](ListExperimentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFeatures

> ListFeaturesResponse listFeatures(project, opts)



Returns configuration details about all the features in the specified project.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project to return the feature list from.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextToken': "nextToken_example" // String | The token to use when requesting the next set of results. You received this token from a previous <code>ListFeatures</code> operation.
};
apiInstance.listFeatures(project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project to return the feature list from. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextToken** | **String**| The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListFeatures&lt;/code&gt; operation. | [optional] 

### Return type

[**ListFeaturesResponse**](ListFeaturesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLaunches

> ListLaunchesResponse listLaunches(project, opts)



Returns configuration details about all the launches in the specified project.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project to return the launch list from.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextToken': "nextToken_example", // String | The token to use when requesting the next set of results. You received this token from a previous <code>ListLaunches</code> operation.
  'status': "status_example" // String | Use this optional parameter to limit the returned results to only the launches with the status that you specify here.
};
apiInstance.listLaunches(project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project to return the launch list from. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextToken** | **String**| The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListLaunches&lt;/code&gt; operation. | [optional] 
 **status** | **String**| Use this optional parameter to limit the returned results to only the launches with the status that you specify here. | [optional] 

### Return type

[**ListLaunchesResponse**](ListLaunchesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProjects

> ListProjectsResponse listProjects(opts)



Returns configuration details about all the projects in the current Region in your account.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextToken': "nextToken_example" // String | The token to use when requesting the next set of results. You received this token from a previous <code>ListProjects</code> operation.
};
apiInstance.listProjects(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextToken** | **String**| The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListProjects&lt;/code&gt; operation. | [optional] 

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSegmentReferences

> ListSegmentReferencesResponse listSegmentReferences(segment, type, opts)



Use this operation to find which experiments or launches are using a specified segment.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let segment = "segment_example"; // String | The ARN of the segment that you want to view information for.
let type = "type_example"; // String | Specifies whether to return information about launches or experiments that use this segment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response. If you omit this, the default of 50 is used.
  'nextToken': "nextToken_example" // String | The token to use when requesting the next set of results. You received this token from a previous <code>ListSegmentReferences</code> operation.
};
apiInstance.listSegmentReferences(segment, type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **String**| The ARN of the segment that you want to view information for. | 
 **type** | **String**| Specifies whether to return information about launches or experiments that use this segment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to include in the response. If you omit this, the default of 50 is used. | [optional] 
 **nextToken** | **String**| The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListSegmentReferences&lt;/code&gt; operation. | [optional] 

### Return type

[**ListSegmentReferencesResponse**](ListSegmentReferencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSegments

> ListSegmentsResponse listSegments(opts)



Returns a list of audience segments that you have created in your account in this Region.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response. If you omit this, the default of 50 is used.
  'nextToken': "nextToken_example" // String | The token to use when requesting the next set of results. You received this token from a previous <code>ListSegments</code> operation.
};
apiInstance.listSegments(opts, (error, data, response) => {
  if (error) {
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
 **maxResults** | **Number**| The maximum number of results to include in the response. If you omit this, the default of 50 is used. | [optional] 
 **nextToken** | **String**| The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListSegments&lt;/code&gt; operation. | [optional] 

### Return type

[**ListSegmentsResponse**](ListSegmentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Displays the tags associated with an Evidently resource.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource that you want to see the tags of.
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
 **resourceArn** | **String**| The ARN of the resource that you want to see the tags of. | 
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


## putProjectEvents

> PutProjectEventsResponse putProjectEvents(project, putProjectEventsRequest, opts)



Sends performance events to Evidently. These events can be used to evaluate a launch or an experiment.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project to write the events to.
let putProjectEventsRequest = new AmazonCloudWatchEvidently.PutProjectEventsRequest(); // PutProjectEventsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putProjectEvents(project, putProjectEventsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project to write the events to. | 
 **putProjectEventsRequest** | [**PutProjectEventsRequest**](PutProjectEventsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutProjectEventsResponse**](PutProjectEventsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startExperiment

> StartExperimentResponse startExperiment(experiment, project, startExperimentRequest, opts)



Starts an existing experiment. To create an experiment, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateExperiment.html\&quot;&gt;CreateExperiment&lt;/a&gt;.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let experiment = "experiment_example"; // String | The name of the experiment to start.
let project = "project_example"; // String | The name or ARN of the project that contains the experiment to start.
let startExperimentRequest = new AmazonCloudWatchEvidently.StartExperimentRequest(); // StartExperimentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startExperiment(experiment, project, startExperimentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **String**| The name of the experiment to start. | 
 **project** | **String**| The name or ARN of the project that contains the experiment to start. | 
 **startExperimentRequest** | [**StartExperimentRequest**](StartExperimentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartExperimentResponse**](StartExperimentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startLaunch

> StartLaunchResponse startLaunch(launch, project, opts)



Starts an existing launch. To create a launch, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateLaunch.html\&quot;&gt;CreateLaunch&lt;/a&gt;.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let launch = "launch_example"; // String | The name of the launch to start.
let project = "project_example"; // String | The name or ARN of the project that contains the launch to start.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startLaunch(launch, project, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch** | **String**| The name of the launch to start. | 
 **project** | **String**| The name or ARN of the project that contains the launch to start. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartLaunchResponse**](StartLaunchResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopExperiment

> StopExperimentResponse stopExperiment(experiment, project, stopExperimentRequest, opts)



Stops an experiment that is currently running. If you stop an experiment, you can&#39;t resume it or restart it.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let experiment = "experiment_example"; // String | The name of the experiment to stop.
let project = "project_example"; // String | The name or ARN of the project that contains the experiment to stop.
let stopExperimentRequest = new AmazonCloudWatchEvidently.StopExperimentRequest(); // StopExperimentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopExperiment(experiment, project, stopExperimentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **String**| The name of the experiment to stop. | 
 **project** | **String**| The name or ARN of the project that contains the experiment to stop. | 
 **stopExperimentRequest** | [**StopExperimentRequest**](StopExperimentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopExperimentResponse**](StopExperimentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopLaunch

> StopLaunchResponse stopLaunch(launch, project, stopLaunchRequest, opts)



Stops a launch that is currently running. After you stop a launch, you will not be able to resume it or restart it. Also, it will not be evaluated as a rule for traffic allocation, and the traffic that was allocated to the launch will instead be available to the feature&#39;s experiment, if there is one. Otherwise, all traffic will be served the default variation after the launch is stopped.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let launch = "launch_example"; // String | The name of the launch to stop.
let project = "project_example"; // String | The name or ARN of the project that contains the launch that you want to stop.
let stopLaunchRequest = new AmazonCloudWatchEvidently.StopLaunchRequest(); // StopLaunchRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopLaunch(launch, project, stopLaunchRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch** | **String**| The name of the launch to stop. | 
 **project** | **String**| The name or ARN of the project that contains the launch that you want to stop. | 
 **stopLaunchRequest** | [**StopLaunchRequest**](StopLaunchRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopLaunchResponse**](StopLaunchResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Assigns one or more tags (key-value pairs) to the specified CloudWatch Evidently resource. Projects, features, launches, and experiments can be tagged.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the CloudWatch Evidently resource that you're adding tags to.
let tagResourceRequest = new AmazonCloudWatchEvidently.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The ARN of the CloudWatch Evidently resource that you&#39;re adding tags to. | 
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


## testSegmentPattern

> TestSegmentPatternResponse testSegmentPattern(testSegmentPatternRequest, opts)



Use this operation to test a rules pattern that you plan to use to create an audience segment. For more information about segments, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateSegment.html\&quot;&gt;CreateSegment&lt;/a&gt;.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let testSegmentPatternRequest = new AmazonCloudWatchEvidently.TestSegmentPatternRequest(); // TestSegmentPatternRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.testSegmentPattern(testSegmentPatternRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testSegmentPatternRequest** | [**TestSegmentPatternRequest**](TestSegmentPatternRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TestSegmentPatternResponse**](TestSegmentPatternResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Removes one or more tags from the specified resource.

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the CloudWatch Evidently resource that you're removing tags from.
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
 **resourceArn** | **String**| The ARN of the CloudWatch Evidently resource that you&#39;re removing tags from. | 
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


## updateExperiment

> UpdateExperimentResponse updateExperiment(experiment, project, updateExperimentRequest, opts)



&lt;p&gt;Updates an Evidently experiment. &lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update an experiment&#39;s tag. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let experiment = "experiment_example"; // String | The name of the experiment to update.
let project = "project_example"; // String | The name or ARN of the project that contains the experiment that you want to update.
let updateExperimentRequest = new AmazonCloudWatchEvidently.UpdateExperimentRequest(); // UpdateExperimentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateExperiment(experiment, project, updateExperimentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **String**| The name of the experiment to update. | 
 **project** | **String**| The name or ARN of the project that contains the experiment that you want to update. | 
 **updateExperimentRequest** | [**UpdateExperimentRequest**](UpdateExperimentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateExperimentResponse**](UpdateExperimentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateFeature

> UpdateFeatureResponse updateFeature(feature, project, updateFeatureRequest, opts)



&lt;p&gt;Updates an existing feature.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation to update the tags of an existing feature. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let feature = "feature_example"; // String | The name of the feature to be updated.
let project = "project_example"; // String | The name or ARN of the project that contains the feature to be updated.
let updateFeatureRequest = new AmazonCloudWatchEvidently.UpdateFeatureRequest(); // UpdateFeatureRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateFeature(feature, project, updateFeatureRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **String**| The name of the feature to be updated. | 
 **project** | **String**| The name or ARN of the project that contains the feature to be updated. | 
 **updateFeatureRequest** | [**UpdateFeatureRequest**](UpdateFeatureRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateFeatureResponse**](UpdateFeatureResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLaunch

> UpdateLaunchResponse updateLaunch(launch, project, updateLaunchRequest, opts)



&lt;p&gt;Updates a launch of a given feature. &lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update the tags of an existing launch. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let launch = "launch_example"; // String | The name of the launch that is to be updated.
let project = "project_example"; // String | The name or ARN of the project that contains the launch that you want to update.
let updateLaunchRequest = new AmazonCloudWatchEvidently.UpdateLaunchRequest(); // UpdateLaunchRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLaunch(launch, project, updateLaunchRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch** | **String**| The name of the launch that is to be updated. | 
 **project** | **String**| The name or ARN of the project that contains the launch that you want to update. | 
 **updateLaunchRequest** | [**UpdateLaunchRequest**](UpdateLaunchRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateLaunchResponse**](UpdateLaunchResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProject

> UpdateProjectResponse updateProject(project, updateProjectRequest, opts)



&lt;p&gt;Updates the description of an existing project.&lt;/p&gt; &lt;p&gt;To create a new project, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateProject.html\&quot;&gt;CreateProject&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update the data storage options of a project. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProjectDataDelivery.html\&quot;&gt;UpdateProjectDataDelivery&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Don&#39;t use this operation to update the tags of a project. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project to update.
let updateProjectRequest = new AmazonCloudWatchEvidently.UpdateProjectRequest(); // UpdateProjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateProject(project, updateProjectRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project to update. | 
 **updateProjectRequest** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateProjectResponse**](UpdateProjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProjectDataDelivery

> UpdateProjectDataDeliveryResponse updateProjectDataDelivery(project, updateProjectDataDeliveryRequest, opts)



&lt;p&gt;Updates the data storage options for this project. If you store evaluation events, you an keep them and analyze them on your own. If you choose not to store evaluation events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.&lt;/p&gt; &lt;p&gt;You can&#39;t specify both &lt;code&gt;cloudWatchLogs&lt;/code&gt; and &lt;code&gt;s3Destination&lt;/code&gt; in the same operation.&lt;/p&gt;

### Example

```javascript
import AmazonCloudWatchEvidently from 'amazon_cloud_watch_evidently';
let defaultClient = AmazonCloudWatchEvidently.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudWatchEvidently.DefaultApi();
let project = "project_example"; // String | The name or ARN of the project that you want to modify the data storage options for.
let updateProjectDataDeliveryRequest = new AmazonCloudWatchEvidently.UpdateProjectDataDeliveryRequest(); // UpdateProjectDataDeliveryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateProjectDataDelivery(project, updateProjectDataDeliveryRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **String**| The name or ARN of the project that you want to modify the data storage options for. | 
 **updateProjectDataDeliveryRequest** | [**UpdateProjectDataDeliveryRequest**](UpdateProjectDataDeliveryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateProjectDataDeliveryResponse**](UpdateProjectDataDeliveryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

