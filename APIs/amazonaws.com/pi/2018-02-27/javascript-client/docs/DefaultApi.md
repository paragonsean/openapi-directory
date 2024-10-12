# AwsPerformanceInsights.DefaultApi

All URIs are relative to *http://pi.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describeDimensionKeys**](DefaultApi.md#describeDimensionKeys) | **POST** /#X-Amz-Target&#x3D;PerformanceInsightsv20180227.DescribeDimensionKeys | 
[**getDimensionKeyDetails**](DefaultApi.md#getDimensionKeyDetails) | **POST** /#X-Amz-Target&#x3D;PerformanceInsightsv20180227.GetDimensionKeyDetails | 
[**getResourceMetadata**](DefaultApi.md#getResourceMetadata) | **POST** /#X-Amz-Target&#x3D;PerformanceInsightsv20180227.GetResourceMetadata | 
[**getResourceMetrics**](DefaultApi.md#getResourceMetrics) | **POST** /#X-Amz-Target&#x3D;PerformanceInsightsv20180227.GetResourceMetrics | 
[**listAvailableResourceDimensions**](DefaultApi.md#listAvailableResourceDimensions) | **POST** /#X-Amz-Target&#x3D;PerformanceInsightsv20180227.ListAvailableResourceDimensions | 
[**listAvailableResourceMetrics**](DefaultApi.md#listAvailableResourceMetrics) | **POST** /#X-Amz-Target&#x3D;PerformanceInsightsv20180227.ListAvailableResourceMetrics | 



## describeDimensionKeys

> DescribeDimensionKeysResponse describeDimensionKeys(xAmzTarget, describeDimensionKeysRequest, opts)



&lt;p&gt;For a specific time period, retrieve the top &lt;code&gt;N&lt;/code&gt; dimension keys for a metric. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsPerformanceInsights from 'aws_performance_insights';
let defaultClient = AwsPerformanceInsights.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPerformanceInsights.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeDimensionKeysRequest = new AwsPerformanceInsights.DescribeDimensionKeysRequest(); // DescribeDimensionKeysRequest | 
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
apiInstance.describeDimensionKeys(xAmzTarget, describeDimensionKeysRequest, opts, (error, data, response) => {
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
 **describeDimensionKeysRequest** | [**DescribeDimensionKeysRequest**](DescribeDimensionKeysRequest.md)|  | 
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

[**DescribeDimensionKeysResponse**](DescribeDimensionKeysResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDimensionKeyDetails

> GetDimensionKeyDetailsResponse getDimensionKeyDetails(xAmzTarget, getDimensionKeyDetailsRequest, opts)



Get the attributes of the specified dimension group for a DB instance or data source. For example, if you specify a SQL ID, &lt;code&gt;GetDimensionKeyDetails&lt;/code&gt; retrieves the full text of the dimension &lt;code&gt;db.sql.statement&lt;/code&gt; associated with this ID. This operation is useful because &lt;code&gt;GetResourceMetrics&lt;/code&gt; and &lt;code&gt;DescribeDimensionKeys&lt;/code&gt; don&#39;t support retrieval of large SQL statement text.

### Example

```javascript
import AwsPerformanceInsights from 'aws_performance_insights';
let defaultClient = AwsPerformanceInsights.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPerformanceInsights.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getDimensionKeyDetailsRequest = new AwsPerformanceInsights.GetDimensionKeyDetailsRequest(); // GetDimensionKeyDetailsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDimensionKeyDetails(xAmzTarget, getDimensionKeyDetailsRequest, opts, (error, data, response) => {
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
 **getDimensionKeyDetailsRequest** | [**GetDimensionKeyDetailsRequest**](GetDimensionKeyDetailsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDimensionKeyDetailsResponse**](GetDimensionKeyDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getResourceMetadata

> GetResourceMetadataResponse getResourceMetadata(xAmzTarget, getResourceMetadataRequest, opts)



Retrieve the metadata for different features. For example, the metadata might indicate that a feature is turned on or off on a specific DB instance. 

### Example

```javascript
import AwsPerformanceInsights from 'aws_performance_insights';
let defaultClient = AwsPerformanceInsights.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPerformanceInsights.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getResourceMetadataRequest = new AwsPerformanceInsights.GetResourceMetadataRequest(); // GetResourceMetadataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getResourceMetadata(xAmzTarget, getResourceMetadataRequest, opts, (error, data, response) => {
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
 **getResourceMetadataRequest** | [**GetResourceMetadataRequest**](GetResourceMetadataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetResourceMetadataResponse**](GetResourceMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getResourceMetrics

> GetResourceMetricsResponse getResourceMetrics(xAmzTarget, getResourceMetricsRequest, opts)



&lt;p&gt;Retrieve Performance Insights metrics for a set of data sources over a time period. You can provide specific dimension groups and dimensions, and provide aggregation and filtering criteria for each group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsPerformanceInsights from 'aws_performance_insights';
let defaultClient = AwsPerformanceInsights.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPerformanceInsights.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getResourceMetricsRequest = new AwsPerformanceInsights.GetResourceMetricsRequest(); // GetResourceMetricsRequest | 
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
apiInstance.getResourceMetrics(xAmzTarget, getResourceMetricsRequest, opts, (error, data, response) => {
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
 **getResourceMetricsRequest** | [**GetResourceMetricsRequest**](GetResourceMetricsRequest.md)|  | 
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

[**GetResourceMetricsResponse**](GetResourceMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAvailableResourceDimensions

> ListAvailableResourceDimensionsResponse listAvailableResourceDimensions(xAmzTarget, listAvailableResourceDimensionsRequest, opts)



Retrieve the dimensions that can be queried for each specified metric type on a specified DB instance.

### Example

```javascript
import AwsPerformanceInsights from 'aws_performance_insights';
let defaultClient = AwsPerformanceInsights.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPerformanceInsights.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAvailableResourceDimensionsRequest = new AwsPerformanceInsights.ListAvailableResourceDimensionsRequest(); // ListAvailableResourceDimensionsRequest | 
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
apiInstance.listAvailableResourceDimensions(xAmzTarget, listAvailableResourceDimensionsRequest, opts, (error, data, response) => {
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
 **listAvailableResourceDimensionsRequest** | [**ListAvailableResourceDimensionsRequest**](ListAvailableResourceDimensionsRequest.md)|  | 
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

[**ListAvailableResourceDimensionsResponse**](ListAvailableResourceDimensionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAvailableResourceMetrics

> ListAvailableResourceMetricsResponse listAvailableResourceMetrics(xAmzTarget, listAvailableResourceMetricsRequest, opts)



Retrieve metrics of the specified types that can be queried for a specified DB instance. 

### Example

```javascript
import AwsPerformanceInsights from 'aws_performance_insights';
let defaultClient = AwsPerformanceInsights.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsPerformanceInsights.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAvailableResourceMetricsRequest = new AwsPerformanceInsights.ListAvailableResourceMetricsRequest(); // ListAvailableResourceMetricsRequest | 
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
apiInstance.listAvailableResourceMetrics(xAmzTarget, listAvailableResourceMetricsRequest, opts, (error, data, response) => {
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
 **listAvailableResourceMetricsRequest** | [**ListAvailableResourceMetricsRequest**](ListAvailableResourceMetricsRequest.md)|  | 
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

[**ListAvailableResourceMetricsResponse**](ListAvailableResourceMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

