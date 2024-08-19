# AmazonDevOpsGuru.DefaultApi

All URIs are relative to *http://devops-guru.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addNotificationChannel**](DefaultApi.md#addNotificationChannel) | **PUT** /channels | 
[**deleteInsight**](DefaultApi.md#deleteInsight) | **DELETE** /insights/{Id} | 
[**describeAccountHealth**](DefaultApi.md#describeAccountHealth) | **GET** /accounts/health | 
[**describeAccountOverview**](DefaultApi.md#describeAccountOverview) | **POST** /accounts/overview | 
[**describeAnomaly**](DefaultApi.md#describeAnomaly) | **GET** /anomalies/{Id} | 
[**describeEventSourcesConfig**](DefaultApi.md#describeEventSourcesConfig) | **POST** /event-sources | 
[**describeFeedback**](DefaultApi.md#describeFeedback) | **POST** /feedback | 
[**describeInsight**](DefaultApi.md#describeInsight) | **GET** /insights/{Id} | 
[**describeOrganizationHealth**](DefaultApi.md#describeOrganizationHealth) | **POST** /organization/health | 
[**describeOrganizationOverview**](DefaultApi.md#describeOrganizationOverview) | **POST** /organization/overview | 
[**describeOrganizationResourceCollectionHealth**](DefaultApi.md#describeOrganizationResourceCollectionHealth) | **POST** /organization/health/resource-collection | 
[**describeResourceCollectionHealth**](DefaultApi.md#describeResourceCollectionHealth) | **GET** /accounts/health/resource-collection/{ResourceCollectionType} | 
[**describeServiceIntegration**](DefaultApi.md#describeServiceIntegration) | **GET** /service-integrations | 
[**getCostEstimation**](DefaultApi.md#getCostEstimation) | **GET** /cost-estimation | 
[**getResourceCollection**](DefaultApi.md#getResourceCollection) | **GET** /resource-collections/{ResourceCollectionType} | 
[**listAnomaliesForInsight**](DefaultApi.md#listAnomaliesForInsight) | **POST** /anomalies/insight/{InsightId} | 
[**listAnomalousLogGroups**](DefaultApi.md#listAnomalousLogGroups) | **POST** /list-log-anomalies | 
[**listEvents**](DefaultApi.md#listEvents) | **POST** /events | 
[**listInsights**](DefaultApi.md#listInsights) | **POST** /insights | 
[**listMonitoredResources**](DefaultApi.md#listMonitoredResources) | **POST** /monitoredResources | 
[**listNotificationChannels**](DefaultApi.md#listNotificationChannels) | **POST** /channels | 
[**listOrganizationInsights**](DefaultApi.md#listOrganizationInsights) | **POST** /organization/insights | 
[**listRecommendations**](DefaultApi.md#listRecommendations) | **POST** /recommendations | 
[**putFeedback**](DefaultApi.md#putFeedback) | **PUT** /feedback | 
[**removeNotificationChannel**](DefaultApi.md#removeNotificationChannel) | **DELETE** /channels/{Id} | 
[**searchInsights**](DefaultApi.md#searchInsights) | **POST** /insights/search | 
[**searchOrganizationInsights**](DefaultApi.md#searchOrganizationInsights) | **POST** /organization/insights/search | 
[**startCostEstimation**](DefaultApi.md#startCostEstimation) | **PUT** /cost-estimation | 
[**updateEventSourcesConfig**](DefaultApi.md#updateEventSourcesConfig) | **PUT** /event-sources | 
[**updateResourceCollection**](DefaultApi.md#updateResourceCollection) | **PUT** /resource-collections | 
[**updateServiceIntegration**](DefaultApi.md#updateServiceIntegration) | **PUT** /service-integrations | 



## addNotificationChannel

> AddNotificationChannelResponse addNotificationChannel(addNotificationChannelRequest, opts)



&lt;p&gt; Adds a notification channel to DevOps Guru. A notification channel is used to notify you about important DevOps Guru events, such as when an insight is generated. &lt;/p&gt; &lt;p&gt;If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html\&quot;&gt;Permissions for Amazon SNS topics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you use an Amazon SNS topic that is encrypted by an Amazon Web Services Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html\&quot;&gt;Permissions for Amazon Web Services KMS–encrypted Amazon SNS topics&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let addNotificationChannelRequest = new AmazonDevOpsGuru.AddNotificationChannelRequest(); // AddNotificationChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addNotificationChannel(addNotificationChannelRequest, opts, (error, data, response) => {
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
 **addNotificationChannelRequest** | [**AddNotificationChannelRequest**](AddNotificationChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddNotificationChannelResponse**](AddNotificationChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteInsight

> Object deleteInsight(id, opts)



Deletes the insight along with the associated anomalies, events and recommendations.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let id = "id_example"; // String | The ID of the insight.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteInsight(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the insight. | 
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


## describeAccountHealth

> DescribeAccountHealthResponse describeAccountHealth(opts)



 Returns the number of open reactive insights, the number of open proactive insights, and the number of metrics analyzed in your Amazon Web Services account. Use these numbers to gauge the health of operations in your Amazon Web Services account. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAccountHealth(opts, (error, data, response) => {
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

### Return type

[**DescribeAccountHealthResponse**](DescribeAccountHealthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAccountOverview

> DescribeAccountOverviewResponse describeAccountOverview(describeAccountOverviewRequest, opts)



 For the time range passed in, returns the number of open reactive insight that were created, the number of open proactive insights that were created, and the Mean Time to Recover (MTTR) for all closed reactive insights. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let describeAccountOverviewRequest = new AmazonDevOpsGuru.DescribeAccountOverviewRequest(); // DescribeAccountOverviewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAccountOverview(describeAccountOverviewRequest, opts, (error, data, response) => {
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
 **describeAccountOverviewRequest** | [**DescribeAccountOverviewRequest**](DescribeAccountOverviewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAccountOverviewResponse**](DescribeAccountOverviewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAnomaly

> DescribeAnomalyResponse describeAnomaly(id, opts)



 Returns details about an anomaly that you specify using its ID. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let id = "id_example"; // String |  The ID of the anomaly. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'accountId': "accountId_example" // String | The ID of the member account.
};
apiInstance.describeAnomaly(id, opts, (error, data, response) => {
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
 **id** | **String**|  The ID of the anomaly.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **accountId** | **String**| The ID of the member account. | [optional] 

### Return type

[**DescribeAnomalyResponse**](DescribeAnomalyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeEventSourcesConfig

> DescribeEventSourcesConfigResponse describeEventSourcesConfig(opts)



Returns the integration status of services that are integrated with DevOps Guru as Consumer via EventBridge. The one service that can be integrated with DevOps Guru is Amazon CodeGuru Profiler, which can produce proactive recommendations which can be stored and viewed in DevOps Guru.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeEventSourcesConfig(opts, (error, data, response) => {
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

### Return type

[**DescribeEventSourcesConfigResponse**](DescribeEventSourcesConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeFeedback

> DescribeFeedbackResponse describeFeedback(describeFeedbackRequest, opts)



 Returns the most recent feedback submitted in the current Amazon Web Services account and Region. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let describeFeedbackRequest = new AmazonDevOpsGuru.DescribeFeedbackRequest(); // DescribeFeedbackRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeFeedback(describeFeedbackRequest, opts, (error, data, response) => {
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
 **describeFeedbackRequest** | [**DescribeFeedbackRequest**](DescribeFeedbackRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeFeedbackResponse**](DescribeFeedbackResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeInsight

> DescribeInsightResponse describeInsight(id, opts)



 Returns details about an insight that you specify using its ID. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let id = "id_example"; // String |  The ID of the insight. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'accountId': "accountId_example" // String | The ID of the member account in the organization.
};
apiInstance.describeInsight(id, opts, (error, data, response) => {
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
 **id** | **String**|  The ID of the insight.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **accountId** | **String**| The ID of the member account in the organization. | [optional] 

### Return type

[**DescribeInsightResponse**](DescribeInsightResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeOrganizationHealth

> DescribeOrganizationHealthResponse describeOrganizationHealth(describeOrganizationHealthRequest, opts)



Returns active insights, predictive insights, and resource hours analyzed in last hour.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let describeOrganizationHealthRequest = new AmazonDevOpsGuru.DescribeOrganizationHealthRequest(); // DescribeOrganizationHealthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeOrganizationHealth(describeOrganizationHealthRequest, opts, (error, data, response) => {
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
 **describeOrganizationHealthRequest** | [**DescribeOrganizationHealthRequest**](DescribeOrganizationHealthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeOrganizationHealthResponse**](DescribeOrganizationHealthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeOrganizationOverview

> DescribeOrganizationOverviewResponse describeOrganizationOverview(describeOrganizationOverviewRequest, opts)



Returns an overview of your organization&#39;s history based on the specified time range. The overview includes the total reactive and proactive insights.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let describeOrganizationOverviewRequest = new AmazonDevOpsGuru.DescribeOrganizationOverviewRequest(); // DescribeOrganizationOverviewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeOrganizationOverview(describeOrganizationOverviewRequest, opts, (error, data, response) => {
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
 **describeOrganizationOverviewRequest** | [**DescribeOrganizationOverviewRequest**](DescribeOrganizationOverviewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeOrganizationOverviewResponse**](DescribeOrganizationOverviewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeOrganizationResourceCollectionHealth

> DescribeOrganizationResourceCollectionHealthResponse describeOrganizationResourceCollectionHealth(describeOrganizationResourceCollectionHealthRequest, opts)



Provides an overview of your system&#39;s health. If additional member accounts are part of your organization, you can filter those accounts using the &lt;code&gt;AccountIds&lt;/code&gt; field.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let describeOrganizationResourceCollectionHealthRequest = new AmazonDevOpsGuru.DescribeOrganizationResourceCollectionHealthRequest(); // DescribeOrganizationResourceCollectionHealthRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.describeOrganizationResourceCollectionHealth(describeOrganizationResourceCollectionHealthRequest, opts, (error, data, response) => {
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
 **describeOrganizationResourceCollectionHealthRequest** | [**DescribeOrganizationResourceCollectionHealthRequest**](DescribeOrganizationResourceCollectionHealthRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**DescribeOrganizationResourceCollectionHealthResponse**](DescribeOrganizationResourceCollectionHealthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeResourceCollectionHealth

> DescribeResourceCollectionHealthResponse describeResourceCollectionHealth(resourceCollectionType, opts)



 Returns the number of open proactive insights, open reactive insights, and the Mean Time to Recover (MTTR) for all closed insights in resource collections in your account. You specify the type of Amazon Web Services resources collection. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let resourceCollectionType = "resourceCollectionType_example"; // String |  An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
};
apiInstance.describeResourceCollectionHealth(resourceCollectionType, opts, (error, data, response) => {
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
 **resourceCollectionType** | **String**|  An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page. | [optional] 

### Return type

[**DescribeResourceCollectionHealthResponse**](DescribeResourceCollectionHealthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeServiceIntegration

> DescribeServiceIntegrationResponse describeServiceIntegration(opts)



 Returns the integration status of services that are integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon Web Services Systems Manager, which can be used to create an OpsItem for each generated insight. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeServiceIntegration(opts, (error, data, response) => {
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

### Return type

[**DescribeServiceIntegrationResponse**](DescribeServiceIntegrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCostEstimation

> GetCostEstimationResponse getCostEstimation(opts)



Returns an estimate of the monthly cost for DevOps Guru to analyze your Amazon Web Services resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html\&quot;&gt;Estimate your Amazon DevOps Guru costs&lt;/a&gt; and &lt;a href&#x3D;\&quot;http://aws.amazon.com/devops-guru/pricing/\&quot;&gt;Amazon DevOps Guru pricing&lt;/a&gt;.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
};
apiInstance.getCostEstimation(opts, (error, data, response) => {
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
 **nextToken** | **String**| The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page. | [optional] 

### Return type

[**GetCostEstimationResponse**](GetCostEstimationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourceCollection

> GetResourceCollectionResponse getResourceCollection(resourceCollectionType, opts)



 Returns lists Amazon Web Services resources that are of the specified resource collection type. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let resourceCollectionType = "resourceCollectionType_example"; // String |  The type of Amazon Web Services resource collections to return. The one valid value is <code>CLOUD_FORMATION</code> for Amazon Web Services CloudFormation stacks. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
};
apiInstance.getResourceCollection(resourceCollectionType, opts, (error, data, response) => {
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
 **resourceCollectionType** | **String**|  The type of Amazon Web Services resource collections to return. The one valid value is &lt;code&gt;CLOUD_FORMATION&lt;/code&gt; for Amazon Web Services CloudFormation stacks.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page. | [optional] 

### Return type

[**GetResourceCollectionResponse**](GetResourceCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAnomaliesForInsight

> ListAnomaliesForInsightResponse listAnomaliesForInsight(insightId, listAnomaliesForInsightRequest, opts)



 Returns a list of the anomalies that belong to an insight that you specify using its ID. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let insightId = "insightId_example"; // String |  The ID of the insight. The returned anomalies belong to this insight. 
let listAnomaliesForInsightRequest = new AmazonDevOpsGuru.ListAnomaliesForInsightRequest(); // ListAnomaliesForInsightRequest | 
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
apiInstance.listAnomaliesForInsight(insightId, listAnomaliesForInsightRequest, opts, (error, data, response) => {
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
 **insightId** | **String**|  The ID of the insight. The returned anomalies belong to this insight.  | 
 **listAnomaliesForInsightRequest** | [**ListAnomaliesForInsightRequest**](ListAnomaliesForInsightRequest.md)|  | 
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

[**ListAnomaliesForInsightResponse**](ListAnomaliesForInsightResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAnomalousLogGroups

> ListAnomalousLogGroupsResponse listAnomalousLogGroups(listAnomalousLogGroupsRequest, opts)



 Returns the list of log groups that contain log anomalies. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let listAnomalousLogGroupsRequest = new AmazonDevOpsGuru.ListAnomalousLogGroupsRequest(); // ListAnomalousLogGroupsRequest | 
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
apiInstance.listAnomalousLogGroups(listAnomalousLogGroupsRequest, opts, (error, data, response) => {
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
 **listAnomalousLogGroupsRequest** | [**ListAnomalousLogGroupsRequest**](ListAnomalousLogGroupsRequest.md)|  | 
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

[**ListAnomalousLogGroupsResponse**](ListAnomalousLogGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEvents

> ListEventsResponse listEvents(listEventsRequest, opts)



 Returns a list of the events emitted by the resources that are evaluated by DevOps Guru. You can use filters to specify which events are returned. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let listEventsRequest = new AmazonDevOpsGuru.ListEventsRequest(); // ListEventsRequest | 
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
apiInstance.listEvents(listEventsRequest, opts, (error, data, response) => {
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
 **listEventsRequest** | [**ListEventsRequest**](ListEventsRequest.md)|  | 
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

[**ListEventsResponse**](ListEventsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listInsights

> ListInsightsResponse listInsights(listInsightsRequest, opts)



 Returns a list of insights in your Amazon Web Services account. You can specify which insights are returned by their start time and status (&lt;code&gt;ONGOING&lt;/code&gt;, &lt;code&gt;CLOSED&lt;/code&gt;, or &lt;code&gt;ANY&lt;/code&gt;). 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let listInsightsRequest = new AmazonDevOpsGuru.ListInsightsRequest(); // ListInsightsRequest | 
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
apiInstance.listInsights(listInsightsRequest, opts, (error, data, response) => {
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
 **listInsightsRequest** | [**ListInsightsRequest**](ListInsightsRequest.md)|  | 
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

[**ListInsightsResponse**](ListInsightsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listMonitoredResources

> ListMonitoredResourcesResponse listMonitoredResources(listMonitoredResourcesRequest, opts)



 Returns the list of all log groups that are being monitored and tagged by DevOps Guru. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let listMonitoredResourcesRequest = new AmazonDevOpsGuru.ListMonitoredResourcesRequest(); // ListMonitoredResourcesRequest | 
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
apiInstance.listMonitoredResources(listMonitoredResourcesRequest, opts, (error, data, response) => {
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
 **listMonitoredResourcesRequest** | [**ListMonitoredResourcesRequest**](ListMonitoredResourcesRequest.md)|  | 
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

[**ListMonitoredResourcesResponse**](ListMonitoredResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listNotificationChannels

> ListNotificationChannelsResponse listNotificationChannels(listNotificationChannelsRequest, opts)



 Returns a list of notification channels configured for DevOps Guru. Each notification channel is used to notify you when DevOps Guru generates an insight that contains information about how to improve your operations. The one supported notification channel is Amazon Simple Notification Service (Amazon SNS). 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let listNotificationChannelsRequest = new AmazonDevOpsGuru.ListNotificationChannelsRequest(); // ListNotificationChannelsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listNotificationChannels(listNotificationChannelsRequest, opts, (error, data, response) => {
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
 **listNotificationChannelsRequest** | [**ListNotificationChannelsRequest**](ListNotificationChannelsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListNotificationChannelsResponse**](ListNotificationChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listOrganizationInsights

> ListOrganizationInsightsResponse listOrganizationInsights(listOrganizationInsightsRequest, opts)



Returns a list of insights associated with the account or OU Id.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let listOrganizationInsightsRequest = new AmazonDevOpsGuru.ListOrganizationInsightsRequest(); // ListOrganizationInsightsRequest | 
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
apiInstance.listOrganizationInsights(listOrganizationInsightsRequest, opts, (error, data, response) => {
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
 **listOrganizationInsightsRequest** | [**ListOrganizationInsightsRequest**](ListOrganizationInsightsRequest.md)|  | 
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

[**ListOrganizationInsightsResponse**](ListOrganizationInsightsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRecommendations

> ListRecommendationsResponse listRecommendations(listRecommendationsRequest, opts)



 Returns a list of a specified insight&#39;s recommendations. Each recommendation includes a list of related metrics and a list of related events. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let listRecommendationsRequest = new AmazonDevOpsGuru.ListRecommendationsRequest(); // ListRecommendationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listRecommendations(listRecommendationsRequest, opts, (error, data, response) => {
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
 **listRecommendationsRequest** | [**ListRecommendationsRequest**](ListRecommendationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListRecommendationsResponse**](ListRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putFeedback

> Object putFeedback(putFeedbackRequest, opts)



 Collects customer feedback about the specified insight. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let putFeedbackRequest = new AmazonDevOpsGuru.PutFeedbackRequest(); // PutFeedbackRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putFeedback(putFeedbackRequest, opts, (error, data, response) => {
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
 **putFeedbackRequest** | [**PutFeedbackRequest**](PutFeedbackRequest.md)|  | 
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


## removeNotificationChannel

> Object removeNotificationChannel(id, opts)



 Removes a notification channel from DevOps Guru. A notification channel is used to notify you when DevOps Guru generates an insight that contains information about how to improve your operations. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let id = "id_example"; // String |  The ID of the notification channel to be removed. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeNotificationChannel(id, opts, (error, data, response) => {
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
 **id** | **String**|  The ID of the notification channel to be removed.  | 
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


## searchInsights

> SearchInsightsResponse searchInsights(searchInsightsRequest, opts)



&lt;p&gt; Returns a list of insights in your Amazon Web Services account. You can specify which insights are returned by their start time, one or more statuses (&lt;code&gt;ONGOING&lt;/code&gt; or &lt;code&gt;CLOSED&lt;/code&gt;), one or more severities (&lt;code&gt;LOW&lt;/code&gt;, &lt;code&gt;MEDIUM&lt;/code&gt;, and &lt;code&gt;HIGH&lt;/code&gt;), and type (&lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt;). &lt;/p&gt; &lt;p&gt; Use the &lt;code&gt;Filters&lt;/code&gt; parameter to specify status and severity search parameters. Use the &lt;code&gt;Type&lt;/code&gt; parameter to specify &lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt; in your search. &lt;/p&gt;

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let searchInsightsRequest = new AmazonDevOpsGuru.SearchInsightsRequest(); // SearchInsightsRequest | 
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
apiInstance.searchInsights(searchInsightsRequest, opts, (error, data, response) => {
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
 **searchInsightsRequest** | [**SearchInsightsRequest**](SearchInsightsRequest.md)|  | 
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

[**SearchInsightsResponse**](SearchInsightsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchOrganizationInsights

> SearchOrganizationInsightsResponse searchOrganizationInsights(searchOrganizationInsightsRequest, opts)



&lt;p&gt; Returns a list of insights in your organization. You can specify which insights are returned by their start time, one or more statuses (&lt;code&gt;ONGOING&lt;/code&gt;, &lt;code&gt;CLOSED&lt;/code&gt;, and &lt;code&gt;CLOSED&lt;/code&gt;), one or more severities (&lt;code&gt;LOW&lt;/code&gt;, &lt;code&gt;MEDIUM&lt;/code&gt;, and &lt;code&gt;HIGH&lt;/code&gt;), and type (&lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt;). &lt;/p&gt; &lt;p&gt; Use the &lt;code&gt;Filters&lt;/code&gt; parameter to specify status and severity search parameters. Use the &lt;code&gt;Type&lt;/code&gt; parameter to specify &lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt; in your search. &lt;/p&gt;

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let searchOrganizationInsightsRequest = new AmazonDevOpsGuru.SearchOrganizationInsightsRequest(); // SearchOrganizationInsightsRequest | 
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
apiInstance.searchOrganizationInsights(searchOrganizationInsightsRequest, opts, (error, data, response) => {
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
 **searchOrganizationInsightsRequest** | [**SearchOrganizationInsightsRequest**](SearchOrganizationInsightsRequest.md)|  | 
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

[**SearchOrganizationInsightsResponse**](SearchOrganizationInsightsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startCostEstimation

> Object startCostEstimation(startCostEstimationRequest, opts)



Starts the creation of an estimate of the monthly cost to analyze your Amazon Web Services resources.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let startCostEstimationRequest = new AmazonDevOpsGuru.StartCostEstimationRequest(); // StartCostEstimationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startCostEstimation(startCostEstimationRequest, opts, (error, data, response) => {
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
 **startCostEstimationRequest** | [**StartCostEstimationRequest**](StartCostEstimationRequest.md)|  | 
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


## updateEventSourcesConfig

> Object updateEventSourcesConfig(updateEventSourcesConfigRequest, opts)



Enables or disables integration with a service that can be integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon CodeGuru Profiler, which can produce proactive recommendations which can be stored and viewed in DevOps Guru.

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let updateEventSourcesConfigRequest = new AmazonDevOpsGuru.UpdateEventSourcesConfigRequest(); // UpdateEventSourcesConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEventSourcesConfig(updateEventSourcesConfigRequest, opts, (error, data, response) => {
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
 **updateEventSourcesConfigRequest** | [**UpdateEventSourcesConfigRequest**](UpdateEventSourcesConfigRequest.md)|  | 
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


## updateResourceCollection

> Object updateResourceCollection(updateResourceCollectionRequest, opts)



 Updates the collection of resources that DevOps Guru analyzes. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks. This method also creates the IAM role required for you to use DevOps Guru. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let updateResourceCollectionRequest = new AmazonDevOpsGuru.UpdateResourceCollectionRequest(); // UpdateResourceCollectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateResourceCollection(updateResourceCollectionRequest, opts, (error, data, response) => {
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
 **updateResourceCollectionRequest** | [**UpdateResourceCollectionRequest**](UpdateResourceCollectionRequest.md)|  | 
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


## updateServiceIntegration

> Object updateServiceIntegration(updateServiceIntegrationRequest, opts)



 Enables or disables integration with a service that can be integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon Web Services Systems Manager, which can be used to create an OpsItem for each generated insight. 

### Example

```javascript
import AmazonDevOpsGuru from 'amazon_dev_ops_guru';
let defaultClient = AmazonDevOpsGuru.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDevOpsGuru.DefaultApi();
let updateServiceIntegrationRequest = new AmazonDevOpsGuru.UpdateServiceIntegrationRequest(); // UpdateServiceIntegrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateServiceIntegration(updateServiceIntegrationRequest, opts, (error, data, response) => {
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
 **updateServiceIntegrationRequest** | [**UpdateServiceIntegrationRequest**](UpdateServiceIntegrationRequest.md)|  | 
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

