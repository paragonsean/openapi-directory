# AwsHealthApisAndNotifications.DefaultApi

All URIs are relative to *https://health.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describeAffectedAccountsForOrganization**](DefaultApi.md#describeAffectedAccountsForOrganization) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeAffectedAccountsForOrganization | 
[**describeAffectedEntities**](DefaultApi.md#describeAffectedEntities) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeAffectedEntities | 
[**describeAffectedEntitiesForOrganization**](DefaultApi.md#describeAffectedEntitiesForOrganization) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeAffectedEntitiesForOrganization | 
[**describeEntityAggregates**](DefaultApi.md#describeEntityAggregates) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeEntityAggregates | 
[**describeEventAggregates**](DefaultApi.md#describeEventAggregates) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeEventAggregates | 
[**describeEventDetails**](DefaultApi.md#describeEventDetails) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeEventDetails | 
[**describeEventDetailsForOrganization**](DefaultApi.md#describeEventDetailsForOrganization) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeEventDetailsForOrganization | 
[**describeEventTypes**](DefaultApi.md#describeEventTypes) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeEventTypes | 
[**describeEvents**](DefaultApi.md#describeEvents) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeEvents | 
[**describeEventsForOrganization**](DefaultApi.md#describeEventsForOrganization) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeEventsForOrganization | 
[**describeHealthServiceStatusForOrganization**](DefaultApi.md#describeHealthServiceStatusForOrganization) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DescribeHealthServiceStatusForOrganization | 
[**disableHealthServiceAccessForOrganization**](DefaultApi.md#disableHealthServiceAccessForOrganization) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.DisableHealthServiceAccessForOrganization | 
[**enableHealthServiceAccessForOrganization**](DefaultApi.md#enableHealthServiceAccessForOrganization) | **POST** /#X-Amz-Target&#x3D;AWSHealth_20160804.EnableHealthServiceAccessForOrganization | 



## describeAffectedAccountsForOrganization

> DescribeAffectedAccountsForOrganizationResponse describeAffectedAccountsForOrganization(xAmzTarget, describeAffectedAccountsForOrganizationRequest, opts)



&lt;p&gt;Returns a list of accounts in the organization from Organizations that are affected by the provided event. For more information about the different types of Health events, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html\&quot;&gt;Event&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html\&quot;&gt;EnableHealthServiceAccessForOrganization&lt;/a&gt; operation from your organization&#39;s management account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API operation uses pagination. Specify the &lt;code&gt;nextToken&lt;/code&gt; parameter in the next request to return more results.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAffectedAccountsForOrganizationRequest = new AwsHealthApisAndNotifications.DescribeAffectedAccountsForOrganizationRequest(); // DescribeAffectedAccountsForOrganizationRequest | 
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
apiInstance.describeAffectedAccountsForOrganization(xAmzTarget, describeAffectedAccountsForOrganizationRequest, opts, (error, data, response) => {
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
 **describeAffectedAccountsForOrganizationRequest** | [**DescribeAffectedAccountsForOrganizationRequest**](DescribeAffectedAccountsForOrganizationRequest.md)|  | 
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

[**DescribeAffectedAccountsForOrganizationResponse**](DescribeAffectedAccountsForOrganizationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAffectedEntities

> DescribeAffectedEntitiesResponse describeAffectedEntities(xAmzTarget, describeAffectedEntitiesRequest, opts)



&lt;p&gt;Returns a list of entities that have been affected by the specified events, based on the specified filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the Amazon Web Service. Events that have impact beyond that of the affected entities, or where the extent of impact is unknown, include at least one entity indicating this.&lt;/p&gt; &lt;p&gt;At least one event ARN is required.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API operation uses pagination. Specify the &lt;code&gt;nextToken&lt;/code&gt; parameter in the next request to return more results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This operation supports resource-level permissions. You can use this operation to allow or deny access to specific Health events. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions\&quot;&gt;Resource- and action-based conditions&lt;/a&gt; in the &lt;i&gt;Health User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAffectedEntitiesRequest = new AwsHealthApisAndNotifications.DescribeAffectedEntitiesRequest(); // DescribeAffectedEntitiesRequest | 
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
apiInstance.describeAffectedEntities(xAmzTarget, describeAffectedEntitiesRequest, opts, (error, data, response) => {
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
 **describeAffectedEntitiesRequest** | [**DescribeAffectedEntitiesRequest**](DescribeAffectedEntitiesRequest.md)|  | 
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

[**DescribeAffectedEntitiesResponse**](DescribeAffectedEntitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAffectedEntitiesForOrganization

> DescribeAffectedEntitiesForOrganizationResponse describeAffectedEntitiesForOrganization(xAmzTarget, describeAffectedEntitiesForOrganizationRequest, opts)



&lt;p&gt;Returns a list of entities that have been affected by one or more events for one or more accounts in your organization in Organizations, based on the filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the Amazon Web Service.&lt;/p&gt; &lt;p&gt;At least one event Amazon Resource Name (ARN) and account ID are required.&lt;/p&gt; &lt;p&gt;Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html\&quot;&gt;EnableHealthServiceAccessForOrganization&lt;/a&gt; operation from your organization&#39;s management account.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API operation uses pagination. Specify the &lt;code&gt;nextToken&lt;/code&gt; parameter in the next request to return more results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This operation doesn&#39;t support resource-level permissions. You can&#39;t use this operation to allow or deny access to specific Health events. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions\&quot;&gt;Resource- and action-based conditions&lt;/a&gt; in the &lt;i&gt;Health User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAffectedEntitiesForOrganizationRequest = new AwsHealthApisAndNotifications.DescribeAffectedEntitiesForOrganizationRequest(); // DescribeAffectedEntitiesForOrganizationRequest | 
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
apiInstance.describeAffectedEntitiesForOrganization(xAmzTarget, describeAffectedEntitiesForOrganizationRequest, opts, (error, data, response) => {
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
 **describeAffectedEntitiesForOrganizationRequest** | [**DescribeAffectedEntitiesForOrganizationRequest**](DescribeAffectedEntitiesForOrganizationRequest.md)|  | 
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

[**DescribeAffectedEntitiesForOrganizationResponse**](DescribeAffectedEntitiesForOrganizationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEntityAggregates

> DescribeEntityAggregatesResponse describeEntityAggregates(xAmzTarget, describeEntityAggregatesRequest, opts)



Returns the number of entities that are affected by each of the specified events.

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEntityAggregatesRequest = new AwsHealthApisAndNotifications.DescribeEntityAggregatesRequest(); // DescribeEntityAggregatesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeEntityAggregates(xAmzTarget, describeEntityAggregatesRequest, opts, (error, data, response) => {
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
 **describeEntityAggregatesRequest** | [**DescribeEntityAggregatesRequest**](DescribeEntityAggregatesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeEntityAggregatesResponse**](DescribeEntityAggregatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEventAggregates

> DescribeEventAggregatesResponse describeEventAggregates(xAmzTarget, describeEventAggregatesRequest, opts)



&lt;p&gt;Returns the number of events of each event type (issue, scheduled change, and account notification). If no filter is specified, the counts of all events in each category are returned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API operation uses pagination. Specify the &lt;code&gt;nextToken&lt;/code&gt; parameter in the next request to return more results.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEventAggregatesRequest = new AwsHealthApisAndNotifications.DescribeEventAggregatesRequest(); // DescribeEventAggregatesRequest | 
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
apiInstance.describeEventAggregates(xAmzTarget, describeEventAggregatesRequest, opts, (error, data, response) => {
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
 **describeEventAggregatesRequest** | [**DescribeEventAggregatesRequest**](DescribeEventAggregatesRequest.md)|  | 
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

[**DescribeEventAggregatesResponse**](DescribeEventAggregatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEventDetails

> DescribeEventDetailsResponse describeEventDetails(xAmzTarget, describeEventDetailsRequest, opts)



&lt;p&gt;Returns detailed information about one or more specified events. Information includes standard event data (Amazon Web Services Region, service, and so on, as returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html\&quot;&gt;DescribeEvents&lt;/a&gt;), a detailed event description, and possible additional metadata that depends upon the nature of the event. Affected entities are not included. To retrieve the entities, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html\&quot;&gt;DescribeAffectedEntities&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;If a specified event can&#39;t be retrieved, an error message is returned for that event.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation supports resource-level permissions. You can use this operation to allow or deny access to specific Health events. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions\&quot;&gt;Resource- and action-based conditions&lt;/a&gt; in the &lt;i&gt;Health User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEventDetailsRequest = new AwsHealthApisAndNotifications.DescribeEventDetailsRequest(); // DescribeEventDetailsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeEventDetails(xAmzTarget, describeEventDetailsRequest, opts, (error, data, response) => {
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
 **describeEventDetailsRequest** | [**DescribeEventDetailsRequest**](DescribeEventDetailsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeEventDetailsResponse**](DescribeEventDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEventDetailsForOrganization

> DescribeEventDetailsForOrganizationResponse describeEventDetailsForOrganization(xAmzTarget, describeEventDetailsForOrganizationRequest, opts)



&lt;p&gt;Returns detailed information about one or more specified events for one or more Amazon Web Services accounts in your organization. This information includes standard event data (such as the Amazon Web Services Region and service), an event description, and (depending on the event) possible metadata. This operation doesn&#39;t return affected entities, such as the resources related to the event. To return affected entities, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html\&quot;&gt;DescribeAffectedEntitiesForOrganization&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html\&quot;&gt;EnableHealthServiceAccessForOrganization&lt;/a&gt; operation from your organization&#39;s management account.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;When you call the &lt;code&gt;DescribeEventDetailsForOrganization&lt;/code&gt; operation, specify the &lt;code&gt;organizationEventDetailFilters&lt;/code&gt; object in the request. Depending on the Health event type, note the following differences:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To return event details for a public event, you must specify a null value for the &lt;code&gt;awsAccountId&lt;/code&gt; parameter. If you specify an account ID for a public event, Health returns an error message because public events aren&#39;t specific to an account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To return event details for an event that is specific to an account in your organization, you must specify the &lt;code&gt;awsAccountId&lt;/code&gt; parameter in the request. If you don&#39;t specify an account ID, Health returns an error message because the event is specific to an account in your organization. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html\&quot;&gt;Event&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation doesn&#39;t support resource-level permissions. You can&#39;t use this operation to allow or deny access to specific Health events. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions\&quot;&gt;Resource- and action-based conditions&lt;/a&gt; in the &lt;i&gt;Health User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEventDetailsForOrganizationRequest = new AwsHealthApisAndNotifications.DescribeEventDetailsForOrganizationRequest(); // DescribeEventDetailsForOrganizationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeEventDetailsForOrganization(xAmzTarget, describeEventDetailsForOrganizationRequest, opts, (error, data, response) => {
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
 **describeEventDetailsForOrganizationRequest** | [**DescribeEventDetailsForOrganizationRequest**](DescribeEventDetailsForOrganizationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeEventDetailsForOrganizationResponse**](DescribeEventDetailsForOrganizationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEventTypes

> DescribeEventTypesResponse describeEventTypes(xAmzTarget, describeEventTypesRequest, opts)



&lt;p&gt;Returns the event types that meet the specified filter criteria. You can use this API operation to find information about the Health event, such as the category, Amazon Web Service, and event code. The metadata for each event appears in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_EventType.html\&quot;&gt;EventType&lt;/a&gt; object. &lt;/p&gt; &lt;p&gt;If you don&#39;t specify a filter criteria, the API operation returns all event types, in no particular order. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This API operation uses pagination. Specify the &lt;code&gt;nextToken&lt;/code&gt; parameter in the next request to return more results.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEventTypesRequest = new AwsHealthApisAndNotifications.DescribeEventTypesRequest(); // DescribeEventTypesRequest | 
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
apiInstance.describeEventTypes(xAmzTarget, describeEventTypesRequest, opts, (error, data, response) => {
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
 **describeEventTypesRequest** | [**DescribeEventTypesRequest**](DescribeEventTypesRequest.md)|  | 
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

[**DescribeEventTypesResponse**](DescribeEventTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEvents

> DescribeEventsResponse describeEvents(xAmzTarget, describeEventsRequest, opts)



&lt;p&gt; Returns information about events that meet the specified filter criteria. Events are returned in a summary form and do not include the detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html\&quot;&gt;DescribeEventDetails&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html\&quot;&gt;DescribeAffectedEntities&lt;/a&gt; operations.&lt;/p&gt; &lt;p&gt;If no filter criteria are specified, all events are returned. Results are sorted by &lt;code&gt;lastModifiedTime&lt;/code&gt;, starting with the most recent event.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When you call the &lt;code&gt;DescribeEvents&lt;/code&gt; operation and specify an entity for the &lt;code&gt;entityValues&lt;/code&gt; parameter, Health might return public events that aren&#39;t specific to that resource. For example, if you call &lt;code&gt;DescribeEvents&lt;/code&gt; and specify an ID for an Amazon Elastic Compute Cloud (Amazon EC2) instance, Health might return events that aren&#39;t specific to that resource or service. To get events that are specific to a service, use the &lt;code&gt;services&lt;/code&gt; parameter in the &lt;code&gt;filter&lt;/code&gt; object. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html\&quot;&gt;Event&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This API operation uses pagination. Specify the &lt;code&gt;nextToken&lt;/code&gt; parameter in the next request to return more results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEventsRequest = new AwsHealthApisAndNotifications.DescribeEventsRequest(); // DescribeEventsRequest | 
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
apiInstance.describeEvents(xAmzTarget, describeEventsRequest, opts, (error, data, response) => {
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
 **describeEventsRequest** | [**DescribeEventsRequest**](DescribeEventsRequest.md)|  | 
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

[**DescribeEventsResponse**](DescribeEventsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEventsForOrganization

> DescribeEventsForOrganizationResponse describeEventsForOrganization(xAmzTarget, describeEventsForOrganizationRequest, opts)



&lt;p&gt;Returns information about events across your organization in Organizations. You can use the&lt;code&gt;filters&lt;/code&gt; parameter to specify the events that you want to return. Events are returned in a summary form and don&#39;t include the affected accounts, detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the following operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedAccountsForOrganization.html\&quot;&gt;DescribeAffectedAccountsForOrganization&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html\&quot;&gt;DescribeEventDetailsForOrganization&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html\&quot;&gt;DescribeAffectedEntitiesForOrganization&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you don&#39;t specify a &lt;code&gt;filter&lt;/code&gt;, the &lt;code&gt;DescribeEventsForOrganizations&lt;/code&gt; returns all events across your organization. Results are sorted by &lt;code&gt;lastModifiedTime&lt;/code&gt;, starting with the most recent event. &lt;/p&gt; &lt;p&gt;For more information about the different types of Health events, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html\&quot;&gt;Event&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html\&quot;&gt;EnableHealthServiceAccessForOrganization&lt;/a&gt; operation from your organization&#39;s management account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API operation uses pagination. Specify the &lt;code&gt;nextToken&lt;/code&gt; parameter in the next request to return more results.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEventsForOrganizationRequest = new AwsHealthApisAndNotifications.DescribeEventsForOrganizationRequest(); // DescribeEventsForOrganizationRequest | 
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
apiInstance.describeEventsForOrganization(xAmzTarget, describeEventsForOrganizationRequest, opts, (error, data, response) => {
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
 **describeEventsForOrganizationRequest** | [**DescribeEventsForOrganizationRequest**](DescribeEventsForOrganizationRequest.md)|  | 
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

[**DescribeEventsForOrganizationResponse**](DescribeEventsForOrganizationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeHealthServiceStatusForOrganization

> DescribeHealthServiceStatusForOrganizationResponse describeHealthServiceStatusForOrganization(xAmzTarget, opts)



This operation provides status information on enabling or disabling Health to work with your organization. To call this operation, you must use the organization&#39;s management account.

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
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
apiInstance.describeHealthServiceStatusForOrganization(xAmzTarget, opts, (error, data, response) => {
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

[**DescribeHealthServiceStatusForOrganizationResponse**](DescribeHealthServiceStatusForOrganizationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableHealthServiceAccessForOrganization

> disableHealthServiceAccessForOrganization(xAmzTarget, opts)



&lt;p&gt;Disables Health from working with Organizations. To call this operation, you must sign in to the organization&#39;s management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html\&quot;&gt;Aggregating Health events&lt;/a&gt; in the &lt;i&gt;Health User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation doesn&#39;t remove the service-linked role from the management account in your organization. You must use the IAM console, API, or Command Line Interface (CLI) to remove the service-linked role. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role\&quot;&gt;Deleting a Service-Linked Role&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can also disable the organizational feature by using the Organizations &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html\&quot;&gt;DisableAWSServiceAccess&lt;/a&gt; API operation. After you call this operation, Health stops aggregating events for all other Amazon Web Services accounts in your organization. If you call the Health API operations for organizational view, Health returns an error. Health continues to aggregate health events for your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
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
apiInstance.disableHealthServiceAccessForOrganization(xAmzTarget, opts, (error, data, response) => {
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


## enableHealthServiceAccessForOrganization

> enableHealthServiceAccessForOrganization(xAmzTarget, opts)



&lt;p&gt;Enables Health to work with Organizations. You can use the organizational view feature to aggregate events from all Amazon Web Services accounts in your organization in a centralized location. &lt;/p&gt; &lt;p&gt;This operation also creates a service-linked role for the management account in the organization. &lt;/p&gt; &lt;note&gt; &lt;p&gt;To call this operation, you must meet the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan from &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt; to use the Health API. If you call the Health API from an Amazon Web Services account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, you receive a &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must have permission to call this operation from the organization&#39;s management account. For example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html\&quot;&gt;Health identity-based policy examples&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;If you don&#39;t have the required support plan, you can instead use the Health console to enable the organizational view feature. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html\&quot;&gt;Aggregating Health events&lt;/a&gt; in the &lt;i&gt;Health User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsHealthApisAndNotifications from 'aws_health_apis_and_notifications';
let defaultClient = AwsHealthApisAndNotifications.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsHealthApisAndNotifications.DefaultApi();
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
apiInstance.enableHealthServiceAccessForOrganization(xAmzTarget, opts, (error, data, response) => {
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

