# CloudWatchRum.DefaultApi

All URIs are relative to *http://rum.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchCreateRumMetricDefinitions**](DefaultApi.md#batchCreateRumMetricDefinitions) | **POST** /rummetrics/{AppMonitorName}/metrics | 
[**batchDeleteRumMetricDefinitions**](DefaultApi.md#batchDeleteRumMetricDefinitions) | **DELETE** /rummetrics/{AppMonitorName}/metrics#destination&amp;metricDefinitionIds | 
[**batchGetRumMetricDefinitions**](DefaultApi.md#batchGetRumMetricDefinitions) | **GET** /rummetrics/{AppMonitorName}/metrics#destination | 
[**createAppMonitor**](DefaultApi.md#createAppMonitor) | **POST** /appmonitor | 
[**deleteAppMonitor**](DefaultApi.md#deleteAppMonitor) | **DELETE** /appmonitor/{Name} | 
[**deleteRumMetricsDestination**](DefaultApi.md#deleteRumMetricsDestination) | **DELETE** /rummetrics/{AppMonitorName}/metricsdestination#destination | 
[**getAppMonitor**](DefaultApi.md#getAppMonitor) | **GET** /appmonitor/{Name} | 
[**getAppMonitorData**](DefaultApi.md#getAppMonitorData) | **POST** /appmonitor/{Name}/data | 
[**listAppMonitors**](DefaultApi.md#listAppMonitors) | **POST** /appmonitors | 
[**listRumMetricsDestinations**](DefaultApi.md#listRumMetricsDestinations) | **GET** /rummetrics/{AppMonitorName}/metricsdestination | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**putRumEvents**](DefaultApi.md#putRumEvents) | **POST** /appmonitors/{Id}/ | 
[**putRumMetricsDestination**](DefaultApi.md#putRumMetricsDestination) | **POST** /rummetrics/{AppMonitorName}/metricsdestination | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateAppMonitor**](DefaultApi.md#updateAppMonitor) | **PATCH** /appmonitor/{Name} | 
[**updateRumMetricDefinition**](DefaultApi.md#updateRumMetricDefinition) | **PATCH** /rummetrics/{AppMonitorName}/metrics | 



## batchCreateRumMetricDefinitions

> BatchCreateRumMetricDefinitionsResponse batchCreateRumMetricDefinitions(appMonitorName, batchCreateRumMetricDefinitionsRequest, opts)



&lt;p&gt;Specifies the extended metrics and custom metrics that you want a CloudWatch RUM app monitor to send to a destination. Valid destinations include CloudWatch and Evidently.&lt;/p&gt; &lt;p&gt;By default, RUM app monitors send some metrics to CloudWatch. These default metrics are listed in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-metrics.html\&quot;&gt;CloudWatch metrics that you can collect with CloudWatch RUM&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;In addition to these default metrics, you can choose to send extended metrics or custom metrics or both.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Extended metrics enable you to send metrics with additional dimensions not included in the default metrics. You can also send extended metrics to Evidently as well as CloudWatch. The valid dimension names for the additional dimensions for extended metrics are &lt;code&gt;BrowserName&lt;/code&gt;, &lt;code&gt;CountryCode&lt;/code&gt;, &lt;code&gt;DeviceType&lt;/code&gt;, &lt;code&gt;FileType&lt;/code&gt;, &lt;code&gt;OSName&lt;/code&gt;, and &lt;code&gt;PageId&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-vended-metrics.html\&quot;&gt; Extended metrics that you can send to CloudWatch and CloudWatch Evidently&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Custom metrics are metrics that you define. You can send custom metrics to CloudWatch or to CloudWatch Evidently or to both. With custom metrics, you can use any metric name and namespace, and to derive the metrics you can use any custom events, built-in events, custom attributes, or default attributes. &lt;/p&gt; &lt;p&gt;You can&#39;t send custom metrics to the &lt;code&gt;AWS/RUM&lt;/code&gt; namespace. You must send custom metrics to a custom namespace that you define. The namespace that you use can&#39;t start with &lt;code&gt;AWS/&lt;/code&gt;. CloudWatch RUM prepends &lt;code&gt;RUM/CustomMetrics/&lt;/code&gt; to the custom namespace that you define, so the final namespace for your metrics in CloudWatch is &lt;code&gt;RUM/CustomMetrics/&lt;i&gt;your-custom-namespace&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The maximum number of metric definitions that you can specify in one &lt;code&gt;BatchCreateRumMetricDefinitions&lt;/code&gt; operation is 200.&lt;/p&gt; &lt;p&gt;The maximum number of metric definitions that one destination can contain is 2000.&lt;/p&gt; &lt;p&gt;Extended metrics sent to CloudWatch and RUM custom metrics are charged as CloudWatch custom metrics. Each combination of additional dimension name and dimension value counts as a custom metric. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You must have already created a destination for the metrics before you send them. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html\&quot;&gt;PutRumMetricsDestination&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If some metric definitions specified in a &lt;code&gt;BatchCreateRumMetricDefinitions&lt;/code&gt; operations are not valid, those metric definitions fail and return errors, but all valid metric definitions in the same operation still succeed.&lt;/p&gt;

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let appMonitorName = "appMonitorName_example"; // String | The name of the CloudWatch RUM app monitor that is to send the metrics.
let batchCreateRumMetricDefinitionsRequest = new CloudWatchRum.BatchCreateRumMetricDefinitionsRequest(); // BatchCreateRumMetricDefinitionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchCreateRumMetricDefinitions(appMonitorName, batchCreateRumMetricDefinitionsRequest, opts, (error, data, response) => {
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
 **appMonitorName** | **String**| The name of the CloudWatch RUM app monitor that is to send the metrics. | 
 **batchCreateRumMetricDefinitionsRequest** | [**BatchCreateRumMetricDefinitionsRequest**](BatchCreateRumMetricDefinitionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchCreateRumMetricDefinitionsResponse**](BatchCreateRumMetricDefinitionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDeleteRumMetricDefinitions

> BatchDeleteRumMetricDefinitionsResponse batchDeleteRumMetricDefinitions(appMonitorName, destination, metricDefinitionIds, opts)



&lt;p&gt;Removes the specified metrics from being sent to an extended metrics destination.&lt;/p&gt; &lt;p&gt;If some metric definition IDs specified in a &lt;code&gt;BatchDeleteRumMetricDefinitions&lt;/code&gt; operations are not valid, those metric definitions fail and return errors, but all valid metric definition IDs in the same operation are still deleted.&lt;/p&gt; &lt;p&gt;The maximum number of metric definitions that you can specify in one &lt;code&gt;BatchDeleteRumMetricDefinitions&lt;/code&gt; operation is 200.&lt;/p&gt;

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let appMonitorName = "appMonitorName_example"; // String | The name of the CloudWatch RUM app monitor that is sending these metrics.
let destination = "destination_example"; // String | Defines the destination where you want to stop sending the specified metrics. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.
let metricDefinitionIds = ["null"]; // [String] | An array of structures which define the metrics that you want to stop sending.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'destinationArn': "destinationArn_example" // String | <p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter. </p> <p>This parameter specifies the ARN of the Evidently experiment that was receiving the metrics that are being deleted.</p>
};
apiInstance.batchDeleteRumMetricDefinitions(appMonitorName, destination, metricDefinitionIds, opts, (error, data, response) => {
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
 **appMonitorName** | **String**| The name of the CloudWatch RUM app monitor that is sending these metrics. | 
 **destination** | **String**| Defines the destination where you want to stop sending the specified metrics. Valid values are &lt;code&gt;CloudWatch&lt;/code&gt; and &lt;code&gt;Evidently&lt;/code&gt;. If you specify &lt;code&gt;Evidently&lt;/code&gt;, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment. | 
 **metricDefinitionIds** | [**[String]**](String.md)| An array of structures which define the metrics that you want to stop sending. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **destinationArn** | **String**| &lt;p&gt;This parameter is required if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. If &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;CloudWatch&lt;/code&gt;, do not use this parameter. &lt;/p&gt; &lt;p&gt;This parameter specifies the ARN of the Evidently experiment that was receiving the metrics that are being deleted.&lt;/p&gt; | [optional] 

### Return type

[**BatchDeleteRumMetricDefinitionsResponse**](BatchDeleteRumMetricDefinitionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## batchGetRumMetricDefinitions

> BatchGetRumMetricDefinitionsResponse batchGetRumMetricDefinitions(appMonitorName, destination, opts)



Retrieves the list of metrics and dimensions that a RUM app monitor is sending to a single destination.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let appMonitorName = "appMonitorName_example"; // String | The name of the CloudWatch RUM app monitor that is sending the metrics.
let destination = "destination_example"; // String | The type of destination that you want to view metrics for. Valid values are <code>CloudWatch</code> and <code>Evidently</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'destinationArn': "destinationArn_example", // String | <p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter.</p> <p>This parameter specifies the ARN of the Evidently experiment that corresponds to the destination.</p>
  'maxResults': 56, // Number | <p>The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.</p> <p>To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. </p>
  'nextToken': "nextToken_example", // String | Use the token returned by the previous operation to request the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.batchGetRumMetricDefinitions(appMonitorName, destination, opts, (error, data, response) => {
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
 **appMonitorName** | **String**| The name of the CloudWatch RUM app monitor that is sending the metrics. | 
 **destination** | **String**| The type of destination that you want to view metrics for. Valid values are &lt;code&gt;CloudWatch&lt;/code&gt; and &lt;code&gt;Evidently&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **destinationArn** | **String**| &lt;p&gt;This parameter is required if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. If &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;CloudWatch&lt;/code&gt;, do not use this parameter.&lt;/p&gt; &lt;p&gt;This parameter specifies the ARN of the Evidently experiment that corresponds to the destination.&lt;/p&gt; | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.&lt;/p&gt; &lt;p&gt;To retrieve the remaining results, make another call with the returned &lt;code&gt;NextToken&lt;/code&gt; value. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| Use the token returned by the previous operation to request the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**BatchGetRumMetricDefinitionsResponse**](BatchGetRumMetricDefinitionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createAppMonitor

> CreateAppMonitorResponse createAppMonitor(createAppMonitorRequest, opts)



&lt;p&gt;Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from your application and sends that data to RUM. The data includes performance and reliability information such as page load time, client-side errors, and user behavior.&lt;/p&gt; &lt;p&gt;You use this operation only to create a new app monitor. To update an existing app monitor, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html\&quot;&gt;UpdateAppMonitor&lt;/a&gt; instead.&lt;/p&gt; &lt;p&gt;After you create an app monitor, sign in to the CloudWatch RUM console to get the JavaScript code snippet to add to your web application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html\&quot;&gt;How do I find a code snippet that I&#39;ve already generated?&lt;/a&gt; &lt;/p&gt;

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let createAppMonitorRequest = new CloudWatchRum.CreateAppMonitorRequest(); // CreateAppMonitorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAppMonitor(createAppMonitorRequest, opts, (error, data, response) => {
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
 **createAppMonitorRequest** | [**CreateAppMonitorRequest**](CreateAppMonitorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAppMonitorResponse**](CreateAppMonitorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAppMonitor

> Object deleteAppMonitor(name, opts)



Deletes an existing app monitor. This immediately stops the collection of data.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let name = "name_example"; // String | The name of the app monitor to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppMonitor(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the app monitor to delete. | 
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


## deleteRumMetricsDestination

> Object deleteRumMetricsDestination(appMonitorName, destination, opts)



Deletes a destination for CloudWatch RUM extended metrics, so that the specified app monitor stops sending extended metrics to that destination.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let appMonitorName = "appMonitorName_example"; // String | The name of the app monitor that is sending metrics to the destination that you want to delete.
let destination = "destination_example"; // String | The type of destination to delete. Valid values are <code>CloudWatch</code> and <code>Evidently</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'destinationArn': "destinationArn_example" // String | This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter. This parameter specifies the ARN of the Evidently experiment that corresponds to the destination to delete.
};
apiInstance.deleteRumMetricsDestination(appMonitorName, destination, opts, (error, data, response) => {
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
 **appMonitorName** | **String**| The name of the app monitor that is sending metrics to the destination that you want to delete. | 
 **destination** | **String**| The type of destination to delete. Valid values are &lt;code&gt;CloudWatch&lt;/code&gt; and &lt;code&gt;Evidently&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **destinationArn** | **String**| This parameter is required if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. If &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;CloudWatch&lt;/code&gt;, do not use this parameter. This parameter specifies the ARN of the Evidently experiment that corresponds to the destination to delete. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppMonitor

> GetAppMonitorResponse getAppMonitor(name, opts)



Retrieves the complete configuration information for one app monitor.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let name = "name_example"; // String | The app monitor to retrieve information for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAppMonitor(name, opts, (error, data, response) => {
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
 **name** | **String**| The app monitor to retrieve information for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAppMonitorResponse**](GetAppMonitorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppMonitorData

> GetAppMonitorDataResponse getAppMonitorData(name, getAppMonitorDataRequest, opts)



Retrieves the raw performance events that RUM has collected from your web application, so that you can do your own processing or analysis of this data.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let name = "name_example"; // String | The name of the app monitor that collected the data that you want to retrieve.
let getAppMonitorDataRequest = new CloudWatchRum.GetAppMonitorDataRequest(); // GetAppMonitorDataRequest | 
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
apiInstance.getAppMonitorData(name, getAppMonitorDataRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the app monitor that collected the data that you want to retrieve. | 
 **getAppMonitorDataRequest** | [**GetAppMonitorDataRequest**](GetAppMonitorDataRequest.md)|  | 
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

[**GetAppMonitorDataResponse**](GetAppMonitorDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppMonitors

> ListAppMonitorsResponse listAppMonitors(opts)



Returns a list of the Amazon CloudWatch RUM app monitors in the account.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.
  'nextToken': "nextToken_example", // String | Use the token returned by the previous operation to request the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAppMonitors(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100. | [optional] 
 **nextToken** | **String**| Use the token returned by the previous operation to request the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAppMonitorsResponse**](ListAppMonitorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRumMetricsDestinations

> ListRumMetricsDestinationsResponse listRumMetricsDestinations(appMonitorName, opts)



&lt;p&gt;Returns a list of destinations that you have created to receive RUM extended metrics, for the specified app monitor.&lt;/p&gt; &lt;p&gt;For more information about extended metrics, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AddRumMetrcs.html\&quot;&gt;AddRumMetrics&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let appMonitorName = "appMonitorName_example"; // String | The name of the app monitor associated with the destinations that you want to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | <p>The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.</p> <p>To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. </p>
  'nextToken': "nextToken_example", // String | Use the token returned by the previous operation to request the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRumMetricsDestinations(appMonitorName, opts, (error, data, response) => {
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
 **appMonitorName** | **String**| The name of the app monitor associated with the destinations that you want to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.&lt;/p&gt; &lt;p&gt;To retrieve the remaining results, make another call with the returned &lt;code&gt;NextToken&lt;/code&gt; value. &lt;/p&gt; | [optional] 
 **nextToken** | **String**| Use the token returned by the previous operation to request the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRumMetricsDestinationsResponse**](ListRumMetricsDestinationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Displays the tags associated with a CloudWatch RUM resource.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
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


## putRumEvents

> Object putRumEvents(id, putRumEventsRequest, opts)



&lt;p&gt;Sends telemetry events about your application performance and user behavior to CloudWatch RUM. The code snippet that RUM generates for you to add to your application includes &lt;code&gt;PutRumEvents&lt;/code&gt; operations to send this data to RUM.&lt;/p&gt; &lt;p&gt;Each &lt;code&gt;PutRumEvents&lt;/code&gt; operation can send a batch of events from one user session.&lt;/p&gt;

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let id = "id_example"; // String | The ID of the app monitor that is sending this data.
let putRumEventsRequest = new CloudWatchRum.PutRumEventsRequest(); // PutRumEventsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putRumEvents(id, putRumEventsRequest, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the app monitor that is sending this data. | 
 **putRumEventsRequest** | [**PutRumEventsRequest**](PutRumEventsRequest.md)|  | 
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


## putRumMetricsDestination

> Object putRumMetricsDestination(appMonitorName, putRumMetricsDestinationRequest, opts)



&lt;p&gt;Creates or updates a destination to receive extended metrics from CloudWatch RUM. You can send extended metrics to CloudWatch or to a CloudWatch Evidently experiment.&lt;/p&gt; &lt;p&gt;For more information about extended metrics, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html\&quot;&gt;BatchCreateRumMetricDefinitions&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let appMonitorName = "appMonitorName_example"; // String | The name of the CloudWatch RUM app monitor that will send the metrics.
let putRumMetricsDestinationRequest = new CloudWatchRum.PutRumMetricsDestinationRequest(); // PutRumMetricsDestinationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putRumMetricsDestination(appMonitorName, putRumMetricsDestinationRequest, opts, (error, data, response) => {
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
 **appMonitorName** | **String**| The name of the CloudWatch RUM app monitor that will send the metrics. | 
 **putRumMetricsDestinationRequest** | [**PutRumMetricsDestinationRequest**](PutRumMetricsDestinationRequest.md)|  | 
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


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM resource. Currently, the only resources that can be tagged app monitors.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the CloudWatch RUM resource that you're adding tags to.
let tagResourceRequest = new CloudWatchRum.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The ARN of the CloudWatch RUM resource that you&#39;re adding tags to. | 
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



Removes one or more tags from the specified resource.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the CloudWatch RUM resource that you're removing tags from.
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
 **resourceArn** | **String**| The ARN of the CloudWatch RUM resource that you&#39;re removing tags from. | 
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


## updateAppMonitor

> Object updateAppMonitor(name, updateAppMonitorRequest, opts)



&lt;p&gt;Updates the configuration of an existing app monitor. When you use this operation, only the parts of the app monitor configuration that you specify in this operation are changed. For any parameters that you omit, the existing values are kept.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation to change the tags of an existing app monitor. To change the tags of an existing app monitor, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To create a new app monitor, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html\&quot;&gt;CreateAppMonitor&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After you update an app monitor, sign in to the CloudWatch RUM console to get the updated JavaScript code snippet to add to your web application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html\&quot;&gt;How do I find a code snippet that I&#39;ve already generated?&lt;/a&gt; &lt;/p&gt;

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let name = "name_example"; // String | The name of the app monitor to update.
let updateAppMonitorRequest = new CloudWatchRum.UpdateAppMonitorRequest(); // UpdateAppMonitorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAppMonitor(name, updateAppMonitorRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the app monitor to update. | 
 **updateAppMonitorRequest** | [**UpdateAppMonitorRequest**](UpdateAppMonitorRequest.md)|  | 
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


## updateRumMetricDefinition

> Object updateRumMetricDefinition(appMonitorName, updateRumMetricDefinitionRequest, opts)



Modifies one existing metric definition for CloudWatch RUM extended metrics. For more information about extended metrics, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.html\&quot;&gt;BatchCreateRumMetricsDefinitions&lt;/a&gt;.

### Example

```javascript
import CloudWatchRum from 'cloud_watch_rum';
let defaultClient = CloudWatchRum.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new CloudWatchRum.DefaultApi();
let appMonitorName = "appMonitorName_example"; // String | The name of the CloudWatch RUM app monitor that sends these metrics.
let updateRumMetricDefinitionRequest = new CloudWatchRum.UpdateRumMetricDefinitionRequest(); // UpdateRumMetricDefinitionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRumMetricDefinition(appMonitorName, updateRumMetricDefinitionRequest, opts, (error, data, response) => {
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
 **appMonitorName** | **String**| The name of the CloudWatch RUM app monitor that sends these metrics. | 
 **updateRumMetricDefinitionRequest** | [**UpdateRumMetricDefinitionRequest**](UpdateRumMetricDefinitionRequest.md)|  | 
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

