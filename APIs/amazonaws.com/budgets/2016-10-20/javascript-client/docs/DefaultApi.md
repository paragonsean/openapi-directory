# AwsBudgets.DefaultApi

All URIs are relative to *https://budgets.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBudget**](DefaultApi.md#createBudget) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.CreateBudget | 
[**createBudgetAction**](DefaultApi.md#createBudgetAction) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.CreateBudgetAction | 
[**createNotification**](DefaultApi.md#createNotification) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.CreateNotification | 
[**createSubscriber**](DefaultApi.md#createSubscriber) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.CreateSubscriber | 
[**deleteBudget**](DefaultApi.md#deleteBudget) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DeleteBudget | 
[**deleteBudgetAction**](DefaultApi.md#deleteBudgetAction) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DeleteBudgetAction | 
[**deleteNotification**](DefaultApi.md#deleteNotification) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DeleteNotification | 
[**deleteSubscriber**](DefaultApi.md#deleteSubscriber) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DeleteSubscriber | 
[**describeBudget**](DefaultApi.md#describeBudget) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeBudget | 
[**describeBudgetAction**](DefaultApi.md#describeBudgetAction) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeBudgetAction | 
[**describeBudgetActionHistories**](DefaultApi.md#describeBudgetActionHistories) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeBudgetActionHistories | 
[**describeBudgetActionsForAccount**](DefaultApi.md#describeBudgetActionsForAccount) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeBudgetActionsForAccount | 
[**describeBudgetActionsForBudget**](DefaultApi.md#describeBudgetActionsForBudget) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeBudgetActionsForBudget | 
[**describeBudgetNotificationsForAccount**](DefaultApi.md#describeBudgetNotificationsForAccount) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeBudgetNotificationsForAccount | 
[**describeBudgetPerformanceHistory**](DefaultApi.md#describeBudgetPerformanceHistory) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeBudgetPerformanceHistory | 
[**describeBudgets**](DefaultApi.md#describeBudgets) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeBudgets | 
[**describeNotificationsForBudget**](DefaultApi.md#describeNotificationsForBudget) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeNotificationsForBudget | 
[**describeSubscribersForNotification**](DefaultApi.md#describeSubscribersForNotification) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.DescribeSubscribersForNotification | 
[**executeBudgetAction**](DefaultApi.md#executeBudgetAction) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.ExecuteBudgetAction | 
[**updateBudget**](DefaultApi.md#updateBudget) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.UpdateBudget | 
[**updateBudgetAction**](DefaultApi.md#updateBudgetAction) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.UpdateBudgetAction | 
[**updateNotification**](DefaultApi.md#updateNotification) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.UpdateNotification | 
[**updateSubscriber**](DefaultApi.md#updateSubscriber) | **POST** /#X-Amz-Target&#x3D;AWSBudgetServiceGateway.UpdateSubscriber | 



## createBudget

> Object createBudget(xAmzTarget, createBudgetRequest, opts)



&lt;p&gt;Creates a budget and, if included, notifications and subscribers. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Only one of &lt;code&gt;BudgetLimit&lt;/code&gt; or &lt;code&gt;PlannedBudgetLimits&lt;/code&gt; can be present in the syntax at one time. Use the syntax that matches your case. The Request Syntax section shows the &lt;code&gt;BudgetLimit&lt;/code&gt; syntax. For &lt;code&gt;PlannedBudgetLimits&lt;/code&gt;, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudget.html#API_CreateBudget_Examples\&quot;&gt;Examples&lt;/a&gt; section. &lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createBudgetRequest = new AwsBudgets.CreateBudgetRequest(); // CreateBudgetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBudget(xAmzTarget, createBudgetRequest, opts, (error, data, response) => {
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
 **createBudgetRequest** | [**CreateBudgetRequest**](CreateBudgetRequest.md)|  | 
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


## createBudgetAction

> CreateBudgetActionResponse createBudgetAction(xAmzTarget, createBudgetActionRequest, opts)



 Creates a budget action. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createBudgetActionRequest = new AwsBudgets.CreateBudgetActionRequest(); // CreateBudgetActionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBudgetAction(xAmzTarget, createBudgetActionRequest, opts, (error, data, response) => {
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
 **createBudgetActionRequest** | [**CreateBudgetActionRequest**](CreateBudgetActionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBudgetActionResponse**](CreateBudgetActionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNotification

> Object createNotification(xAmzTarget, createNotificationRequest, opts)



Creates a notification. You must create the budget before you create the associated notification.

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createNotificationRequest = new AwsBudgets.CreateNotificationRequest(); // CreateNotificationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createNotification(xAmzTarget, createNotificationRequest, opts, (error, data, response) => {
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
 **createNotificationRequest** | [**CreateNotificationRequest**](CreateNotificationRequest.md)|  | 
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


## createSubscriber

> Object createSubscriber(xAmzTarget, createSubscriberRequest, opts)



Creates a subscriber. You must create the associated budget and notification before you create the subscriber.

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createSubscriberRequest = new AwsBudgets.CreateSubscriberRequest(); // CreateSubscriberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSubscriber(xAmzTarget, createSubscriberRequest, opts, (error, data, response) => {
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
 **createSubscriberRequest** | [**CreateSubscriberRequest**](CreateSubscriberRequest.md)|  | 
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


## deleteBudget

> Object deleteBudget(xAmzTarget, deleteBudgetRequest, opts)



&lt;p&gt;Deletes a budget. You can delete your budget at any time.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Deleting a budget also deletes the notifications and subscribers that are associated with that budget.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteBudgetRequest = new AwsBudgets.DeleteBudgetRequest(); // DeleteBudgetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBudget(xAmzTarget, deleteBudgetRequest, opts, (error, data, response) => {
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
 **deleteBudgetRequest** | [**DeleteBudgetRequest**](DeleteBudgetRequest.md)|  | 
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


## deleteBudgetAction

> DeleteBudgetActionResponse deleteBudgetAction(xAmzTarget, deleteBudgetActionRequest, opts)



 Deletes a budget action. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteBudgetActionRequest = new AwsBudgets.DeleteBudgetActionRequest(); // DeleteBudgetActionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBudgetAction(xAmzTarget, deleteBudgetActionRequest, opts, (error, data, response) => {
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
 **deleteBudgetActionRequest** | [**DeleteBudgetActionRequest**](DeleteBudgetActionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBudgetActionResponse**](DeleteBudgetActionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNotification

> Object deleteNotification(xAmzTarget, deleteNotificationRequest, opts)



&lt;p&gt;Deletes a notification.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Deleting a notification also deletes the subscribers that are associated with the notification.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteNotificationRequest = new AwsBudgets.DeleteNotificationRequest(); // DeleteNotificationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteNotification(xAmzTarget, deleteNotificationRequest, opts, (error, data, response) => {
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
 **deleteNotificationRequest** | [**DeleteNotificationRequest**](DeleteNotificationRequest.md)|  | 
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


## deleteSubscriber

> Object deleteSubscriber(xAmzTarget, deleteSubscriberRequest, opts)



&lt;p&gt;Deletes a subscriber.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Deleting the last subscriber to a notification also deletes the notification.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteSubscriberRequest = new AwsBudgets.DeleteSubscriberRequest(); // DeleteSubscriberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSubscriber(xAmzTarget, deleteSubscriberRequest, opts, (error, data, response) => {
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
 **deleteSubscriberRequest** | [**DeleteSubscriberRequest**](DeleteSubscriberRequest.md)|  | 
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


## describeBudget

> DescribeBudgetResponse describeBudget(xAmzTarget, describeBudgetRequest, opts)



&lt;p&gt;Describes a budget.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The Request Syntax section shows the &lt;code&gt;BudgetLimit&lt;/code&gt; syntax. For &lt;code&gt;PlannedBudgetLimits&lt;/code&gt;, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudget.html#API_DescribeBudget_Examples\&quot;&gt;Examples&lt;/a&gt; section. &lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBudgetRequest = new AwsBudgets.DescribeBudgetRequest(); // DescribeBudgetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBudget(xAmzTarget, describeBudgetRequest, opts, (error, data, response) => {
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
 **describeBudgetRequest** | [**DescribeBudgetRequest**](DescribeBudgetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBudgetResponse**](DescribeBudgetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBudgetAction

> DescribeBudgetActionResponse describeBudgetAction(xAmzTarget, describeBudgetActionRequest, opts)



 Describes a budget action detail. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBudgetActionRequest = new AwsBudgets.DescribeBudgetActionRequest(); // DescribeBudgetActionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBudgetAction(xAmzTarget, describeBudgetActionRequest, opts, (error, data, response) => {
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
 **describeBudgetActionRequest** | [**DescribeBudgetActionRequest**](DescribeBudgetActionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBudgetActionResponse**](DescribeBudgetActionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBudgetActionHistories

> DescribeBudgetActionHistoriesResponse describeBudgetActionHistories(xAmzTarget, describeBudgetActionHistoriesRequest, opts)



 Describes a budget action history detail. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBudgetActionHistoriesRequest = new AwsBudgets.DescribeBudgetActionHistoriesRequest(); // DescribeBudgetActionHistoriesRequest | 
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
apiInstance.describeBudgetActionHistories(xAmzTarget, describeBudgetActionHistoriesRequest, opts, (error, data, response) => {
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
 **describeBudgetActionHistoriesRequest** | [**DescribeBudgetActionHistoriesRequest**](DescribeBudgetActionHistoriesRequest.md)|  | 
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

[**DescribeBudgetActionHistoriesResponse**](DescribeBudgetActionHistoriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBudgetActionsForAccount

> DescribeBudgetActionsForAccountResponse describeBudgetActionsForAccount(xAmzTarget, describeBudgetActionsForAccountRequest, opts)



 Describes all of the budget actions for an account. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBudgetActionsForAccountRequest = new AwsBudgets.DescribeBudgetActionsForAccountRequest(); // DescribeBudgetActionsForAccountRequest | 
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
apiInstance.describeBudgetActionsForAccount(xAmzTarget, describeBudgetActionsForAccountRequest, opts, (error, data, response) => {
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
 **describeBudgetActionsForAccountRequest** | [**DescribeBudgetActionsForAccountRequest**](DescribeBudgetActionsForAccountRequest.md)|  | 
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

[**DescribeBudgetActionsForAccountResponse**](DescribeBudgetActionsForAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBudgetActionsForBudget

> DescribeBudgetActionsForBudgetResponse describeBudgetActionsForBudget(xAmzTarget, describeBudgetActionsForBudgetRequest, opts)



 Describes all of the budget actions for a budget. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBudgetActionsForBudgetRequest = new AwsBudgets.DescribeBudgetActionsForBudgetRequest(); // DescribeBudgetActionsForBudgetRequest | 
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
apiInstance.describeBudgetActionsForBudget(xAmzTarget, describeBudgetActionsForBudgetRequest, opts, (error, data, response) => {
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
 **describeBudgetActionsForBudgetRequest** | [**DescribeBudgetActionsForBudgetRequest**](DescribeBudgetActionsForBudgetRequest.md)|  | 
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

[**DescribeBudgetActionsForBudgetResponse**](DescribeBudgetActionsForBudgetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBudgetNotificationsForAccount

> DescribeBudgetNotificationsForAccountResponse describeBudgetNotificationsForAccount(xAmzTarget, describeBudgetNotificationsForAccountRequest, opts)



 Lists the budget names and notifications that are associated with an account. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBudgetNotificationsForAccountRequest = new AwsBudgets.DescribeBudgetNotificationsForAccountRequest(); // DescribeBudgetNotificationsForAccountRequest | 
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
apiInstance.describeBudgetNotificationsForAccount(xAmzTarget, describeBudgetNotificationsForAccountRequest, opts, (error, data, response) => {
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
 **describeBudgetNotificationsForAccountRequest** | [**DescribeBudgetNotificationsForAccountRequest**](DescribeBudgetNotificationsForAccountRequest.md)|  | 
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

[**DescribeBudgetNotificationsForAccountResponse**](DescribeBudgetNotificationsForAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBudgetPerformanceHistory

> DescribeBudgetPerformanceHistoryResponse describeBudgetPerformanceHistory(xAmzTarget, describeBudgetPerformanceHistoryRequest, opts)



Describes the history for &lt;code&gt;DAILY&lt;/code&gt;, &lt;code&gt;MONTHLY&lt;/code&gt;, and &lt;code&gt;QUARTERLY&lt;/code&gt; budgets. Budget history isn&#39;t available for &lt;code&gt;ANNUAL&lt;/code&gt; budgets.

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBudgetPerformanceHistoryRequest = new AwsBudgets.DescribeBudgetPerformanceHistoryRequest(); // DescribeBudgetPerformanceHistoryRequest | 
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
apiInstance.describeBudgetPerformanceHistory(xAmzTarget, describeBudgetPerformanceHistoryRequest, opts, (error, data, response) => {
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
 **describeBudgetPerformanceHistoryRequest** | [**DescribeBudgetPerformanceHistoryRequest**](DescribeBudgetPerformanceHistoryRequest.md)|  | 
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

[**DescribeBudgetPerformanceHistoryResponse**](DescribeBudgetPerformanceHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeBudgets

> DescribeBudgetsResponse describeBudgets(xAmzTarget, describeBudgetsRequest, opts)



&lt;p&gt;Lists the budgets that are associated with an account.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The Request Syntax section shows the &lt;code&gt;BudgetLimit&lt;/code&gt; syntax. For &lt;code&gt;PlannedBudgetLimits&lt;/code&gt;, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgets.html#API_DescribeBudgets_Examples\&quot;&gt;Examples&lt;/a&gt; section. &lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeBudgetsRequest = new AwsBudgets.DescribeBudgetsRequest(); // DescribeBudgetsRequest | 
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
apiInstance.describeBudgets(xAmzTarget, describeBudgetsRequest, opts, (error, data, response) => {
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
 **describeBudgetsRequest** | [**DescribeBudgetsRequest**](DescribeBudgetsRequest.md)|  | 
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

[**DescribeBudgetsResponse**](DescribeBudgetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeNotificationsForBudget

> DescribeNotificationsForBudgetResponse describeNotificationsForBudget(xAmzTarget, describeNotificationsForBudgetRequest, opts)



Lists the notifications that are associated with a budget.

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeNotificationsForBudgetRequest = new AwsBudgets.DescribeNotificationsForBudgetRequest(); // DescribeNotificationsForBudgetRequest | 
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
apiInstance.describeNotificationsForBudget(xAmzTarget, describeNotificationsForBudgetRequest, opts, (error, data, response) => {
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
 **describeNotificationsForBudgetRequest** | [**DescribeNotificationsForBudgetRequest**](DescribeNotificationsForBudgetRequest.md)|  | 
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

[**DescribeNotificationsForBudgetResponse**](DescribeNotificationsForBudgetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeSubscribersForNotification

> DescribeSubscribersForNotificationResponse describeSubscribersForNotification(xAmzTarget, describeSubscribersForNotificationRequest, opts)



Lists the subscribers that are associated with a notification.

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeSubscribersForNotificationRequest = new AwsBudgets.DescribeSubscribersForNotificationRequest(); // DescribeSubscribersForNotificationRequest | 
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
apiInstance.describeSubscribersForNotification(xAmzTarget, describeSubscribersForNotificationRequest, opts, (error, data, response) => {
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
 **describeSubscribersForNotificationRequest** | [**DescribeSubscribersForNotificationRequest**](DescribeSubscribersForNotificationRequest.md)|  | 
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

[**DescribeSubscribersForNotificationResponse**](DescribeSubscribersForNotificationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## executeBudgetAction

> ExecuteBudgetActionResponse executeBudgetAction(xAmzTarget, executeBudgetActionRequest, opts)



 Executes a budget action. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let executeBudgetActionRequest = new AwsBudgets.ExecuteBudgetActionRequest(); // ExecuteBudgetActionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.executeBudgetAction(xAmzTarget, executeBudgetActionRequest, opts, (error, data, response) => {
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
 **executeBudgetActionRequest** | [**ExecuteBudgetActionRequest**](ExecuteBudgetActionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExecuteBudgetActionResponse**](ExecuteBudgetActionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBudget

> Object updateBudget(xAmzTarget, updateBudgetRequest, opts)



&lt;p&gt;Updates a budget. You can change every part of a budget except for the &lt;code&gt;budgetName&lt;/code&gt; and the &lt;code&gt;calculatedSpend&lt;/code&gt;. When you modify a budget, the &lt;code&gt;calculatedSpend&lt;/code&gt; drops to zero until Amazon Web Services has new usage data to use for forecasting.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Only one of &lt;code&gt;BudgetLimit&lt;/code&gt; or &lt;code&gt;PlannedBudgetLimits&lt;/code&gt; can be present in the syntax at one time. Use the syntax that matches your case. The Request Syntax section shows the &lt;code&gt;BudgetLimit&lt;/code&gt; syntax. For &lt;code&gt;PlannedBudgetLimits&lt;/code&gt;, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudget.html#API_UpdateBudget_Examples\&quot;&gt;Examples&lt;/a&gt; section. &lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateBudgetRequest = new AwsBudgets.UpdateBudgetRequest(); // UpdateBudgetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBudget(xAmzTarget, updateBudgetRequest, opts, (error, data, response) => {
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
 **updateBudgetRequest** | [**UpdateBudgetRequest**](UpdateBudgetRequest.md)|  | 
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


## updateBudgetAction

> UpdateBudgetActionResponse updateBudgetAction(xAmzTarget, updateBudgetActionRequest, opts)



 Updates a budget action. 

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateBudgetActionRequest = new AwsBudgets.UpdateBudgetActionRequest(); // UpdateBudgetActionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBudgetAction(xAmzTarget, updateBudgetActionRequest, opts, (error, data, response) => {
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
 **updateBudgetActionRequest** | [**UpdateBudgetActionRequest**](UpdateBudgetActionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBudgetActionResponse**](UpdateBudgetActionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNotification

> Object updateNotification(xAmzTarget, updateNotificationRequest, opts)



Updates a notification.

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateNotificationRequest = new AwsBudgets.UpdateNotificationRequest(); // UpdateNotificationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateNotification(xAmzTarget, updateNotificationRequest, opts, (error, data, response) => {
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
 **updateNotificationRequest** | [**UpdateNotificationRequest**](UpdateNotificationRequest.md)|  | 
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


## updateSubscriber

> Object updateSubscriber(xAmzTarget, updateSubscriberRequest, opts)



Updates a subscriber.

### Example

```javascript
import AwsBudgets from 'aws_budgets';
let defaultClient = AwsBudgets.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBudgets.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateSubscriberRequest = new AwsBudgets.UpdateSubscriberRequest(); // UpdateSubscriberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSubscriber(xAmzTarget, updateSubscriberRequest, opts, (error, data, response) => {
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
 **updateSubscriberRequest** | [**UpdateSubscriberRequest**](UpdateSubscriberRequest.md)|  | 
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

