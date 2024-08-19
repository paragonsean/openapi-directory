# AmazonCodeGuruSecurity.DefaultApi

All URIs are relative to *http://codeguru-security.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchGetFindings**](DefaultApi.md#batchGetFindings) | **POST** /batchGetFindings | 
[**createScan**](DefaultApi.md#createScan) | **POST** /scans | 
[**createUploadUrl**](DefaultApi.md#createUploadUrl) | **POST** /uploadUrl | 
[**getAccountConfiguration**](DefaultApi.md#getAccountConfiguration) | **GET** /accountConfiguration/get | 
[**getFindings**](DefaultApi.md#getFindings) | **GET** /findings/{scanName} | 
[**getMetricsSummary**](DefaultApi.md#getMetricsSummary) | **GET** /metrics/summary#date | 
[**getScan**](DefaultApi.md#getScan) | **GET** /scans/{scanName} | 
[**listFindingsMetrics**](DefaultApi.md#listFindingsMetrics) | **GET** /metrics/findings#endDate&amp;startDate | 
[**listScans**](DefaultApi.md#listScans) | **GET** /scans | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateAccountConfiguration**](DefaultApi.md#updateAccountConfiguration) | **PUT** /updateAccountConfiguration | 



## batchGetFindings

> BatchGetFindingsResponse batchGetFindings(batchGetFindingsRequest, opts)



Returns a list of all requested findings.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let batchGetFindingsRequest = new AmazonCodeGuruSecurity.BatchGetFindingsRequest(); // BatchGetFindingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetFindings(batchGetFindingsRequest, opts, (error, data, response) => {
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
 **batchGetFindingsRequest** | [**BatchGetFindingsRequest**](BatchGetFindingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetFindingsResponse**](BatchGetFindingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createScan

> CreateScanResponse createScan(createScanRequest, opts)



Use to create a scan using code uploaded to an S3 bucket.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let createScanRequest = new AmazonCodeGuruSecurity.CreateScanRequest(); // CreateScanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createScan(createScanRequest, opts, (error, data, response) => {
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
 **createScanRequest** | [**CreateScanRequest**](CreateScanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateScanResponse**](CreateScanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUploadUrl

> CreateUploadUrlResponse createUploadUrl(createUploadUrlRequest, opts)



&lt;p&gt;Generates a pre-signed URL and request headers used to upload a code resource.&lt;/p&gt; &lt;p&gt;You can upload your code resource to the URL and add the request headers using any HTTP client.&lt;/p&gt;

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let createUploadUrlRequest = new AmazonCodeGuruSecurity.CreateUploadUrlRequest(); // CreateUploadUrlRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUploadUrl(createUploadUrlRequest, opts, (error, data, response) => {
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
 **createUploadUrlRequest** | [**CreateUploadUrlRequest**](CreateUploadUrlRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateUploadUrlResponse**](CreateUploadUrlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccountConfiguration

> GetAccountConfigurationResponse getAccountConfiguration(opts)



Use to get account level configuration.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccountConfiguration(opts, (error, data, response) => {
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

[**GetAccountConfigurationResponse**](GetAccountConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFindings

> GetFindingsResponse getFindings(scanName, opts)



Returns a list of all findings generated by a particular scan.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let scanName = "scanName_example"; // String | The name of the scan you want to retrieve findings from.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the <code>nextToken</code> element is returned in the response. Use <code>nextToken</code> in a subsequent request to retrieve additional results.
  'nextToken': "nextToken_example", // String | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.
  'status': "status_example" // String | The status of the findings you want to get. Pass either <code>Open</code>, <code>Closed</code>, or <code>All</code>.
};
apiInstance.getFindings(scanName, opts, (error, data, response) => {
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
 **scanName** | **String**| The name of the scan you want to retrieve findings from. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the &lt;code&gt;nextToken&lt;/code&gt; element is returned in the response. Use &lt;code&gt;nextToken&lt;/code&gt; in a subsequent request to retrieve additional results. | [optional] 
 **nextToken** | **String**| A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the &lt;code&gt;nextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. | [optional] 
 **status** | **String**| The status of the findings you want to get. Pass either &lt;code&gt;Open&lt;/code&gt;, &lt;code&gt;Closed&lt;/code&gt;, or &lt;code&gt;All&lt;/code&gt;. | [optional] 

### Return type

[**GetFindingsResponse**](GetFindingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetricsSummary

> GetMetricsSummaryResponse getMetricsSummary(date, opts)



Returns top level metrics about an account from a specified date, including number of open findings, the categories with most findings, the scans with most open findings, and scans with most open critical findings. 

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let date = new Date("2013-10-20T19:20:30+01:00"); // Date | The date you want to retrieve summary metrics from, rounded to the nearest day. The date must be within the past two years since metrics data is only stored for two years. If a date outside of this range is passed, the response will be empty.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMetricsSummary(date, opts, (error, data, response) => {
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
 **date** | **Date**| The date you want to retrieve summary metrics from, rounded to the nearest day. The date must be within the past two years since metrics data is only stored for two years. If a date outside of this range is passed, the response will be empty. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMetricsSummaryResponse**](GetMetricsSummaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScan

> GetScanResponse getScan(scanName, opts)



Returns details about a scan, including whether or not a scan has completed.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let scanName = "scanName_example"; // String | The name of the scan you want to view details about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'runId': "runId_example" // String | UUID that identifies the individual scan run you want to view details about. You retrieve this when you call the <code>CreateScan</code> operation. Defaults to the latest scan run if missing.
};
apiInstance.getScan(scanName, opts, (error, data, response) => {
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
 **scanName** | **String**| The name of the scan you want to view details about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **runId** | **String**| UUID that identifies the individual scan run you want to view details about. You retrieve this when you call the &lt;code&gt;CreateScan&lt;/code&gt; operation. Defaults to the latest scan run if missing. | [optional] 

### Return type

[**GetScanResponse**](GetScanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFindingsMetrics

> ListFindingsMetricsResponse listFindingsMetrics(endDate, startDate, opts)



Returns metrics about all findings in an account within a specified time range.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The end date of the interval which you want to retrieve metrics from.
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The start date of the interval which you want to retrieve metrics from.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the <code>nextToken</code> element is returned in the response. Use <code>nextToken</code> in a subsequent request to retrieve additional results.
  'nextToken': "nextToken_example" // String | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.
};
apiInstance.listFindingsMetrics(endDate, startDate, opts, (error, data, response) => {
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
 **endDate** | **Date**| The end date of the interval which you want to retrieve metrics from. | 
 **startDate** | **Date**| The start date of the interval which you want to retrieve metrics from. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the &lt;code&gt;nextToken&lt;/code&gt; element is returned in the response. Use &lt;code&gt;nextToken&lt;/code&gt; in a subsequent request to retrieve additional results. | [optional] 
 **nextToken** | **String**| A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the &lt;code&gt;nextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. | [optional] 

### Return type

[**ListFindingsMetricsResponse**](ListFindingsMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listScans

> ListScansResponse listScans(opts)



Returns a list of all the standard scans in an account. Does not return express scans.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the <code>nextToken</code> element is returned in the response. Use <code>nextToken</code> in a subsequent request to retrieve additional results.
  'nextToken': "nextToken_example" // String | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.
};
apiInstance.listScans(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the &lt;code&gt;nextToken&lt;/code&gt; element is returned in the response. Use &lt;code&gt;nextToken&lt;/code&gt; in a subsequent request to retrieve additional results. | [optional] 
 **nextToken** | **String**| A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the &lt;code&gt;nextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. | [optional] 

### Return type

[**ListScansResponse**](ListScansResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Returns a list of all tags associated with a scan.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>ListScans</code> or <code>GetScan</code>.
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
 **resourceArn** | **String**| The ARN of the &lt;code&gt;ScanName&lt;/code&gt; object. You can retrieve this ARN by calling &lt;code&gt;ListScans&lt;/code&gt; or &lt;code&gt;GetScan&lt;/code&gt;. | 
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


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Use to add one or more tags to an existing scan.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>ListScans</code> or <code>GetScan</code>.
let tagResourceRequest = new AmazonCodeGuruSecurity.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The ARN of the &lt;code&gt;ScanName&lt;/code&gt; object. You can retrieve this ARN by calling &lt;code&gt;ListScans&lt;/code&gt; or &lt;code&gt;GetScan&lt;/code&gt;. | 
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



Use to remove one or more tags from an existing scan.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>ListScans</code> or <code>GetScan</code>.
let tagKeys = ["null"]; // [String] | A list of keys for each tag you want to remove from a scan.
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
 **resourceArn** | **String**| The ARN of the &lt;code&gt;ScanName&lt;/code&gt; object. You can retrieve this ARN by calling &lt;code&gt;ListScans&lt;/code&gt; or &lt;code&gt;GetScan&lt;/code&gt;. | 
 **tagKeys** | [**[String]**](String.md)| A list of keys for each tag you want to remove from a scan. | 
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


## updateAccountConfiguration

> UpdateAccountConfigurationResponse updateAccountConfiguration(updateAccountConfigurationRequest, opts)



Use to update account-level configuration with an encryption key.

### Example

```javascript
import AmazonCodeGuruSecurity from 'amazon_code_guru_security';
let defaultClient = AmazonCodeGuruSecurity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCodeGuruSecurity.DefaultApi();
let updateAccountConfigurationRequest = new AmazonCodeGuruSecurity.UpdateAccountConfigurationRequest(); // UpdateAccountConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccountConfiguration(updateAccountConfigurationRequest, opts, (error, data, response) => {
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
 **updateAccountConfigurationRequest** | [**UpdateAccountConfigurationRequest**](UpdateAccountConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAccountConfigurationResponse**](UpdateAccountConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

