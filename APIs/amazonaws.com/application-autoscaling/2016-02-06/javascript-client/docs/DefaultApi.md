# ApplicationAutoScaling.DefaultApi

All URIs are relative to *http://application-autoscaling.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteScalingPolicy**](DefaultApi.md#deleteScalingPolicy) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.DeleteScalingPolicy | 
[**deleteScheduledAction**](DefaultApi.md#deleteScheduledAction) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.DeleteScheduledAction | 
[**deregisterScalableTarget**](DefaultApi.md#deregisterScalableTarget) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.DeregisterScalableTarget | 
[**describeScalableTargets**](DefaultApi.md#describeScalableTargets) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.DescribeScalableTargets | 
[**describeScalingActivities**](DefaultApi.md#describeScalingActivities) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.DescribeScalingActivities | 
[**describeScalingPolicies**](DefaultApi.md#describeScalingPolicies) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.DescribeScalingPolicies | 
[**describeScheduledActions**](DefaultApi.md#describeScheduledActions) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.DescribeScheduledActions | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.ListTagsForResource | 
[**putScalingPolicy**](DefaultApi.md#putScalingPolicy) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.PutScalingPolicy | 
[**putScheduledAction**](DefaultApi.md#putScheduledAction) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.PutScheduledAction | 
[**registerScalableTarget**](DefaultApi.md#registerScalableTarget) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.RegisterScalableTarget | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AnyScaleFrontendService.UntagResource | 



## deleteScalingPolicy

> Object deleteScalingPolicy(xAmzTarget, deleteScalingPolicyRequest, opts)



&lt;p&gt;Deletes the specified scaling policy for an Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;Deleting a step scaling policy deletes the underlying alarm action, but does not delete the CloudWatch alarm associated with the scaling policy, even if it no longer has an associated action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html#delete-step-scaling-policy\&quot;&gt;Delete a step scaling policy&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html#delete-target-tracking-policy\&quot;&gt;Delete a target tracking scaling policy&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteScalingPolicyRequest = new ApplicationAutoScaling.DeleteScalingPolicyRequest(); // DeleteScalingPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteScalingPolicy(xAmzTarget, deleteScalingPolicyRequest, opts, (error, data, response) => {
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
 **deleteScalingPolicyRequest** | [**DeleteScalingPolicyRequest**](DeleteScalingPolicyRequest.md)|  | 
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


## deleteScheduledAction

> Object deleteScheduledAction(xAmzTarget, deleteScheduledActionRequest, opts)



&lt;p&gt;Deletes the specified scheduled action for an Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-additional-cli-commands.html#delete-scheduled-action\&quot;&gt;Delete a scheduled action&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteScheduledActionRequest = new ApplicationAutoScaling.DeleteScheduledActionRequest(); // DeleteScheduledActionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteScheduledAction(xAmzTarget, deleteScheduledActionRequest, opts, (error, data, response) => {
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
 **deleteScheduledActionRequest** | [**DeleteScheduledActionRequest**](DeleteScheduledActionRequest.md)|  | 
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


## deregisterScalableTarget

> Object deregisterScalableTarget(xAmzTarget, deregisterScalableTargetRequest, opts)



&lt;p&gt;Deregisters an Application Auto Scaling scalable target when you have finished using it. To see which resources have been registered, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html\&quot;&gt;DescribeScalableTargets&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Deregistering a scalable target deletes the scaling policies and the scheduled actions that are associated with it.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deregisterScalableTargetRequest = new ApplicationAutoScaling.DeregisterScalableTargetRequest(); // DeregisterScalableTargetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deregisterScalableTarget(xAmzTarget, deregisterScalableTargetRequest, opts, (error, data, response) => {
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
 **deregisterScalableTargetRequest** | [**DeregisterScalableTargetRequest**](DeregisterScalableTargetRequest.md)|  | 
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


## describeScalableTargets

> DescribeScalableTargetsResponse describeScalableTargets(xAmzTarget, describeScalableTargetsRequest, opts)



&lt;p&gt;Gets information about the scalable targets in the specified namespace.&lt;/p&gt; &lt;p&gt;You can filter the results using &lt;code&gt;ResourceIds&lt;/code&gt; and &lt;code&gt;ScalableDimension&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeScalableTargetsRequest = new ApplicationAutoScaling.DescribeScalableTargetsRequest(); // DescribeScalableTargetsRequest | 
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
apiInstance.describeScalableTargets(xAmzTarget, describeScalableTargetsRequest, opts, (error, data, response) => {
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
 **describeScalableTargetsRequest** | [**DescribeScalableTargetsRequest**](DescribeScalableTargetsRequest.md)|  | 
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

[**DescribeScalableTargetsResponse**](DescribeScalableTargetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeScalingActivities

> DescribeScalingActivitiesResponse describeScalingActivities(xAmzTarget, describeScalingActivitiesRequest, opts)



&lt;p&gt;Provides descriptive information about the scaling activities in the specified namespace from the previous six weeks.&lt;/p&gt; &lt;p&gt;You can filter the results using &lt;code&gt;ResourceId&lt;/code&gt; and &lt;code&gt;ScalableDimension&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For information about viewing scaling activities using the Amazon Web Services CLI, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html\&quot;&gt;Scaling activities for Application Auto Scaling&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeScalingActivitiesRequest = new ApplicationAutoScaling.DescribeScalingActivitiesRequest(); // DescribeScalingActivitiesRequest | 
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
apiInstance.describeScalingActivities(xAmzTarget, describeScalingActivitiesRequest, opts, (error, data, response) => {
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
 **describeScalingActivitiesRequest** | [**DescribeScalingActivitiesRequest**](DescribeScalingActivitiesRequest.md)|  | 
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

[**DescribeScalingActivitiesResponse**](DescribeScalingActivitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeScalingPolicies

> DescribeScalingPoliciesResponse describeScalingPolicies(xAmzTarget, describeScalingPoliciesRequest, opts)



&lt;p&gt;Describes the Application Auto Scaling scaling policies for the specified service namespace.&lt;/p&gt; &lt;p&gt;You can filter the results using &lt;code&gt;ResourceId&lt;/code&gt;, &lt;code&gt;ScalableDimension&lt;/code&gt;, and &lt;code&gt;PolicyNames&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html\&quot;&gt;Target tracking scaling policies&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html\&quot;&gt;Step scaling policies&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeScalingPoliciesRequest = new ApplicationAutoScaling.DescribeScalingPoliciesRequest(); // DescribeScalingPoliciesRequest | 
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
apiInstance.describeScalingPolicies(xAmzTarget, describeScalingPoliciesRequest, opts, (error, data, response) => {
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
 **describeScalingPoliciesRequest** | [**DescribeScalingPoliciesRequest**](DescribeScalingPoliciesRequest.md)|  | 
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

[**DescribeScalingPoliciesResponse**](DescribeScalingPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeScheduledActions

> DescribeScheduledActionsResponse describeScheduledActions(xAmzTarget, describeScheduledActionsRequest, opts)



&lt;p&gt;Describes the Application Auto Scaling scheduled actions for the specified service namespace.&lt;/p&gt; &lt;p&gt;You can filter the results using the &lt;code&gt;ResourceId&lt;/code&gt;, &lt;code&gt;ScalableDimension&lt;/code&gt;, and &lt;code&gt;ScheduledActionNames&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html\&quot;&gt;Scheduled scaling&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-additional-cli-commands.html\&quot;&gt;Managing scheduled scaling&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeScheduledActionsRequest = new ApplicationAutoScaling.DescribeScheduledActionsRequest(); // DescribeScheduledActionsRequest | 
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
apiInstance.describeScheduledActions(xAmzTarget, describeScheduledActionsRequest, opts, (error, data, response) => {
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
 **describeScheduledActionsRequest** | [**DescribeScheduledActionsRequest**](DescribeScheduledActionsRequest.md)|  | 
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

[**DescribeScheduledActionsResponse**](DescribeScheduledActionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



&lt;p&gt;Returns all the tags on the specified Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;For general information about tags, including the format and syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new ApplicationAutoScaling.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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


## putScalingPolicy

> PutScalingPolicyResponse putScalingPolicy(xAmzTarget, putScalingPolicyRequest, opts)



&lt;p&gt;Creates or updates a scaling policy for an Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scaling policy applies to the scalable target identified by those three attributes. You cannot create a scaling policy until you have registered the resource as a scalable target.&lt;/p&gt; &lt;p&gt;Multiple scaling policies can be in force at the same time for the same scalable target. You can have one or more target tracking scaling policies, one or more step scaling policies, or both. However, there is a chance that multiple policies could conflict, instructing the scalable target to scale out or in at the same time. Application Auto Scaling gives precedence to the policy that provides the largest capacity for both scale out and scale in. For example, if one policy increases capacity by 3, another policy increases capacity by 200 percent, and the current capacity is 10, Application Auto Scaling uses the policy with the highest calculated capacity (200% of 10 &#x3D; 20) and scales out to 30. &lt;/p&gt; &lt;p&gt;We recommend caution, however, when using target tracking scaling policies with step scaling policies because conflicts between these policies can cause undesirable behavior. For example, if the step scaling policy initiates a scale-in activity before the target tracking policy is ready to scale in, the scale-in activity will not be blocked. After the scale-in activity completes, the target tracking policy could instruct the scalable target to scale out again. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html\&quot;&gt;Target tracking scaling policies&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html\&quot;&gt;Step scaling policies&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a scalable target is deregistered, the scalable target is no longer available to use scaling policies. Any scaling policies that were specified for the scalable target are deleted.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putScalingPolicyRequest = new ApplicationAutoScaling.PutScalingPolicyRequest(); // PutScalingPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putScalingPolicy(xAmzTarget, putScalingPolicyRequest, opts, (error, data, response) => {
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
 **putScalingPolicyRequest** | [**PutScalingPolicyRequest**](PutScalingPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutScalingPolicyResponse**](PutScalingPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putScheduledAction

> Object putScheduledAction(xAmzTarget, putScheduledActionRequest, opts)



&lt;p&gt;Creates or updates a scheduled action for an Application Auto Scaling scalable target. &lt;/p&gt; &lt;p&gt;Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scheduled action applies to the scalable target identified by those three attributes. You cannot create a scheduled action until you have registered the resource as a scalable target.&lt;/p&gt; &lt;p&gt;When you specify start and end times with a recurring schedule using a cron expression or rates, they form the boundaries for when the recurring action starts and stops.&lt;/p&gt; &lt;p&gt;To update a scheduled action, specify the parameters that you want to change. If you don&#39;t specify start and end times, the old values are deleted.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html\&quot;&gt;Scheduled scaling&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a scalable target is deregistered, the scalable target is no longer available to run scheduled actions. Any scheduled actions that were specified for the scalable target are deleted.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putScheduledActionRequest = new ApplicationAutoScaling.PutScheduledActionRequest(); // PutScheduledActionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putScheduledAction(xAmzTarget, putScheduledActionRequest, opts, (error, data, response) => {
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
 **putScheduledActionRequest** | [**PutScheduledActionRequest**](PutScheduledActionRequest.md)|  | 
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


## registerScalableTarget

> RegisterScalableTargetResponse registerScalableTarget(xAmzTarget, registerScalableTargetRequest, opts)



&lt;p&gt;Registers or updates a scalable target, which is the resource that you want to scale.&lt;/p&gt; &lt;p&gt;Scalable targets are uniquely identified by the combination of resource ID, scalable dimension, and namespace, which represents some capacity dimension of the underlying service.&lt;/p&gt; &lt;p&gt;When you register a new scalable target, you must specify values for the minimum and maximum capacity. If the specified resource is not active in the target service, this operation does not change the resource&#39;s current capacity. Otherwise, it changes the resource&#39;s current capacity to a value that is inside of this range.&lt;/p&gt; &lt;p&gt;If you add a scaling policy, current capacity is adjustable within the specified range when scaling starts. Application Auto Scaling scaling policies will not scale capacity to values that are outside of the minimum and maximum range.&lt;/p&gt; &lt;p&gt;After you register a scalable target, you do not need to register it again to use other Application Auto Scaling operations. To see which resources have been registered, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html\&quot;&gt;DescribeScalableTargets&lt;/a&gt;. You can also view the scaling policies for a service namespace by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html\&quot;&gt;DescribeScalableTargets&lt;/a&gt;. If you no longer need a scalable target, you can deregister it by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeregisterScalableTarget.html\&quot;&gt;DeregisterScalableTarget&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To update a scalable target, specify the parameters that you want to change. Include the parameters that identify the scalable target: resource ID, scalable dimension, and namespace. Any parameters that you don&#39;t specify are not changed by this update request. &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you call the &lt;code&gt;RegisterScalableTarget&lt;/code&gt; API operation to create a scalable target, there might be a brief delay until the operation achieves &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Eventual_consistency\&quot;&gt;eventual consistency&lt;/a&gt;. You might become aware of this brief delay if you get unexpected errors when performing sequential operations. The typical strategy is to retry the request, and some Amazon Web Services SDKs include automatic backoff and retry logic.&lt;/p&gt; &lt;p&gt;If you call the &lt;code&gt;RegisterScalableTarget&lt;/code&gt; API operation to update an existing scalable target, Application Auto Scaling retrieves the current capacity of the resource. If it&#39;s below the minimum capacity or above the maximum capacity, Application Auto Scaling adjusts the capacity of the scalable target to place it within these bounds, even if you don&#39;t include the &lt;code&gt;MinCapacity&lt;/code&gt; or &lt;code&gt;MaxCapacity&lt;/code&gt; request parameters.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let registerScalableTargetRequest = new ApplicationAutoScaling.RegisterScalableTargetRequest(); // RegisterScalableTargetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerScalableTarget(xAmzTarget, registerScalableTargetRequest, opts, (error, data, response) => {
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
 **registerScalableTargetRequest** | [**RegisterScalableTargetRequest**](RegisterScalableTargetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegisterScalableTargetResponse**](RegisterScalableTargetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



&lt;p&gt;Adds or edits tags on an Application Auto Scaling scalable target.&lt;/p&gt; &lt;p&gt;Each tag consists of a tag key and a tag value, which are both case-sensitive strings. To add a tag, specify a new tag key and a tag value. To edit a tag, specify an existing tag key and a new tag value.&lt;/p&gt; &lt;p&gt;You can use this operation to tag an Application Auto Scaling scalable target, but you cannot tag a scaling policy or scheduled action.&lt;/p&gt; &lt;p&gt;You can also add tags to an Application Auto Scaling scalable target while creating it (&lt;code&gt;RegisterScalableTarget&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;For general information about tags, including the format and syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Use tags to control access to a scalable target. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/resource-tagging-support.html\&quot;&gt;Tagging support for Application Auto Scaling&lt;/a&gt; in the &lt;i&gt;Application Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new ApplicationAutoScaling.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceRequest, opts, (error, data, response) => {
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

> Object untagResource(xAmzTarget, untagResourceRequest, opts)



Deletes tags from an Application Auto Scaling scalable target. To delete a tag, specify the tag key and the Application Auto Scaling scalable target.

### Example

```javascript
import ApplicationAutoScaling from 'application_auto_scaling';
let defaultClient = ApplicationAutoScaling.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ApplicationAutoScaling.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new ApplicationAutoScaling.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceRequest, opts, (error, data, response) => {
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

