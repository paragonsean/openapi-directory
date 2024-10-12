# AwsMarketplaceCommerceAnalytics.DefaultApi

All URIs are relative to *http://marketplacecommerceanalytics.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateDataSet**](DefaultApi.md#generateDataSet) | **POST** /#X-Amz-Target&#x3D;MarketplaceCommerceAnalytics20150701.GenerateDataSet | 
[**startSupportDataExport**](DefaultApi.md#startSupportDataExport) | **POST** /#X-Amz-Target&#x3D;MarketplaceCommerceAnalytics20150701.StartSupportDataExport | 



## generateDataSet

> GenerateDataSetResult generateDataSet(xAmzTarget, generateDataSetRequest, opts)



Given a data set type and data set publication date, asynchronously publishes the requested data set to the specified S3 bucket and notifies the specified SNS topic once the data is available. Returns a unique request identifier that can be used to correlate requests with notifications from the SNS topic. Data sets will be published in comma-separated values (CSV) format with the file name {data_set_type}_YYYY-MM-DD.csv. If a file with the same name already exists (e.g. if the same data set is requested twice), the original file will be overwritten by the new file. Requires a Role with an attached permissions policy providing Allow permissions for the following actions: s3:PutObject, s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish, iam:GetRolePolicy.

### Example

```javascript
import AwsMarketplaceCommerceAnalytics from 'aws_marketplace_commerce_analytics';
let defaultClient = AwsMarketplaceCommerceAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCommerceAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let generateDataSetRequest = new AwsMarketplaceCommerceAnalytics.GenerateDataSetRequest(); // GenerateDataSetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.generateDataSet(xAmzTarget, generateDataSetRequest, opts, (error, data, response) => {
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
 **generateDataSetRequest** | [**GenerateDataSetRequest**](GenerateDataSetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GenerateDataSetResult**](GenerateDataSetResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startSupportDataExport

> StartSupportDataExportResult startSupportDataExport(xAmzTarget, startSupportDataExportRequest, opts)



Given a data set type and a from date, asynchronously publishes the requested customer support data to the specified S3 bucket and notifies the specified SNS topic once the data is available. Returns a unique request identifier that can be used to correlate requests with notifications from the SNS topic. Data sets will be published in comma-separated values (CSV) format with the file name {data_set_type}_YYYY-MM-DD&#39;T&#39;HH-mm-ss&#39;Z&#39;.csv. If a file with the same name already exists (e.g. if the same data set is requested twice), the original file will be overwritten by the new file. Requires a Role with an attached permissions policy providing Allow permissions for the following actions: s3:PutObject, s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish, iam:GetRolePolicy.

### Example

```javascript
import AwsMarketplaceCommerceAnalytics from 'aws_marketplace_commerce_analytics';
let defaultClient = AwsMarketplaceCommerceAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceCommerceAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startSupportDataExportRequest = new AwsMarketplaceCommerceAnalytics.StartSupportDataExportRequest(); // StartSupportDataExportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startSupportDataExport(xAmzTarget, startSupportDataExportRequest, opts, (error, data, response) => {
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
 **startSupportDataExportRequest** | [**StartSupportDataExportRequest**](StartSupportDataExportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartSupportDataExportResult**](StartSupportDataExportResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

