# AmazonKinesisAnalytics.DefaultApi

All URIs are relative to *http://kinesisanalytics.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addApplicationCloudWatchLoggingOption**](DefaultApi.md#addApplicationCloudWatchLoggingOption) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.AddApplicationCloudWatchLoggingOption | 
[**addApplicationInput**](DefaultApi.md#addApplicationInput) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.AddApplicationInput | 
[**addApplicationInputProcessingConfiguration**](DefaultApi.md#addApplicationInputProcessingConfiguration) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.AddApplicationInputProcessingConfiguration | 
[**addApplicationOutput**](DefaultApi.md#addApplicationOutput) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.AddApplicationOutput | 
[**addApplicationReferenceDataSource**](DefaultApi.md#addApplicationReferenceDataSource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.AddApplicationReferenceDataSource | 
[**addApplicationVpcConfiguration**](DefaultApi.md#addApplicationVpcConfiguration) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.AddApplicationVpcConfiguration | 
[**createApplication**](DefaultApi.md#createApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.CreateApplication | 
[**createApplicationPresignedUrl**](DefaultApi.md#createApplicationPresignedUrl) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.CreateApplicationPresignedUrl | 
[**createApplicationSnapshot**](DefaultApi.md#createApplicationSnapshot) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.CreateApplicationSnapshot | 
[**deleteApplication**](DefaultApi.md#deleteApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DeleteApplication | 
[**deleteApplicationCloudWatchLoggingOption**](DefaultApi.md#deleteApplicationCloudWatchLoggingOption) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DeleteApplicationCloudWatchLoggingOption | 
[**deleteApplicationInputProcessingConfiguration**](DefaultApi.md#deleteApplicationInputProcessingConfiguration) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DeleteApplicationInputProcessingConfiguration | 
[**deleteApplicationOutput**](DefaultApi.md#deleteApplicationOutput) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DeleteApplicationOutput | 
[**deleteApplicationReferenceDataSource**](DefaultApi.md#deleteApplicationReferenceDataSource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DeleteApplicationReferenceDataSource | 
[**deleteApplicationSnapshot**](DefaultApi.md#deleteApplicationSnapshot) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DeleteApplicationSnapshot | 
[**deleteApplicationVpcConfiguration**](DefaultApi.md#deleteApplicationVpcConfiguration) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DeleteApplicationVpcConfiguration | 
[**describeApplication**](DefaultApi.md#describeApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DescribeApplication | 
[**describeApplicationSnapshot**](DefaultApi.md#describeApplicationSnapshot) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DescribeApplicationSnapshot | 
[**describeApplicationVersion**](DefaultApi.md#describeApplicationVersion) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DescribeApplicationVersion | 
[**discoverInputSchema**](DefaultApi.md#discoverInputSchema) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.DiscoverInputSchema | 
[**listApplicationSnapshots**](DefaultApi.md#listApplicationSnapshots) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.ListApplicationSnapshots | 
[**listApplicationVersions**](DefaultApi.md#listApplicationVersions) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.ListApplicationVersions | 
[**listApplications**](DefaultApi.md#listApplications) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.ListApplications | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.ListTagsForResource | 
[**rollbackApplication**](DefaultApi.md#rollbackApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.RollbackApplication | 
[**startApplication**](DefaultApi.md#startApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.StartApplication | 
[**stopApplication**](DefaultApi.md#stopApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.StopApplication | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.UntagResource | 
[**updateApplication**](DefaultApi.md#updateApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.UpdateApplication | 
[**updateApplicationMaintenanceConfiguration**](DefaultApi.md#updateApplicationMaintenanceConfiguration) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20180523.UpdateApplicationMaintenanceConfiguration | 



## addApplicationCloudWatchLoggingOption

> AddApplicationCloudWatchLoggingOptionResponse addApplicationCloudWatchLoggingOption(xAmzTarget, addApplicationCloudWatchLoggingOptionRequest, opts)



Adds an Amazon CloudWatch log stream to monitor application configuration errors.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addApplicationCloudWatchLoggingOptionRequest = new AmazonKinesisAnalytics.AddApplicationCloudWatchLoggingOptionRequest(); // AddApplicationCloudWatchLoggingOptionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addApplicationCloudWatchLoggingOption(xAmzTarget, addApplicationCloudWatchLoggingOptionRequest, opts, (error, data, response) => {
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
 **addApplicationCloudWatchLoggingOptionRequest** | [**AddApplicationCloudWatchLoggingOptionRequest**](AddApplicationCloudWatchLoggingOptionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddApplicationCloudWatchLoggingOptionResponse**](AddApplicationCloudWatchLoggingOptionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addApplicationInput

> AddApplicationInputResponse addApplicationInput(xAmzTarget, addApplicationInputRequest, opts)



&lt;p&gt; Adds a streaming source to your SQL-based Kinesis Data Analytics application. &lt;/p&gt; &lt;p&gt;You can add a streaming source when you create an application, or you can use this operation to add a streaming source after you create an application. For more information, see &lt;a&gt;CreateApplication&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the &lt;a&gt;DescribeApplication&lt;/a&gt; operation to find the current application version. &lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addApplicationInputRequest = new AmazonKinesisAnalytics.AddApplicationInputRequest(); // AddApplicationInputRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addApplicationInput(xAmzTarget, addApplicationInputRequest, opts, (error, data, response) => {
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
 **addApplicationInputRequest** | [**AddApplicationInputRequest**](AddApplicationInputRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddApplicationInputResponse**](AddApplicationInputResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addApplicationInputProcessingConfiguration

> AddApplicationInputProcessingConfigurationResponse addApplicationInputProcessingConfiguration(xAmzTarget, addApplicationInputProcessingConfigurationRequest, opts)



Adds an &lt;a&gt;InputProcessingConfiguration&lt;/a&gt; to a SQL-based Kinesis Data Analytics application. An input processor pre-processes records on the input stream before the application&#39;s SQL code executes. Currently, the only input processor available is &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lambda/\&quot;&gt;Amazon Lambda&lt;/a&gt;.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addApplicationInputProcessingConfigurationRequest = new AmazonKinesisAnalytics.AddApplicationInputProcessingConfigurationRequest(); // AddApplicationInputProcessingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addApplicationInputProcessingConfiguration(xAmzTarget, addApplicationInputProcessingConfigurationRequest, opts, (error, data, response) => {
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
 **addApplicationInputProcessingConfigurationRequest** | [**AddApplicationInputProcessingConfigurationRequest**](AddApplicationInputProcessingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddApplicationInputProcessingConfigurationResponse**](AddApplicationInputProcessingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addApplicationOutput

> AddApplicationOutputResponse addApplicationOutput(xAmzTarget, addApplicationOutputRequest, opts)



&lt;p&gt;Adds an external destination to your SQL-based Kinesis Data Analytics application.&lt;/p&gt; &lt;p&gt;If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.&lt;/p&gt; &lt;p&gt; You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. &lt;/p&gt; &lt;p&gt; Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the &lt;a&gt;DescribeApplication&lt;/a&gt; operation to find the current application version.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addApplicationOutputRequest = new AmazonKinesisAnalytics.AddApplicationOutputRequest(); // AddApplicationOutputRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addApplicationOutput(xAmzTarget, addApplicationOutputRequest, opts, (error, data, response) => {
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
 **addApplicationOutputRequest** | [**AddApplicationOutputRequest**](AddApplicationOutputRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddApplicationOutputResponse**](AddApplicationOutputResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addApplicationReferenceDataSource

> AddApplicationReferenceDataSourceResponse addApplicationReferenceDataSource(xAmzTarget, addApplicationReferenceDataSourceRequest, opts)



&lt;p&gt;Adds a reference data source to an existing SQL-based Kinesis Data Analytics application.&lt;/p&gt; &lt;p&gt;Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addApplicationReferenceDataSourceRequest = new AmazonKinesisAnalytics.AddApplicationReferenceDataSourceRequest(); // AddApplicationReferenceDataSourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addApplicationReferenceDataSource(xAmzTarget, addApplicationReferenceDataSourceRequest, opts, (error, data, response) => {
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
 **addApplicationReferenceDataSourceRequest** | [**AddApplicationReferenceDataSourceRequest**](AddApplicationReferenceDataSourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddApplicationReferenceDataSourceResponse**](AddApplicationReferenceDataSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addApplicationVpcConfiguration

> AddApplicationVpcConfigurationResponse addApplicationVpcConfiguration(xAmzTarget, addApplicationVpcConfigurationRequest, opts)



&lt;p&gt;Adds a Virtual Private Cloud (VPC) configuration to the application. Applications can use VPCs to store and access resources securely.&lt;/p&gt; &lt;p&gt;Note the following about VPC configurations for Kinesis Data Analytics applications:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VPC configurations are not supported for SQL applications.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When a VPC is added to a Kinesis Data Analytics application, the application can no longer be accessed from the Internet directly. To enable Internet access to the application, add an Internet gateway to your VPC.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addApplicationVpcConfigurationRequest = new AmazonKinesisAnalytics.AddApplicationVpcConfigurationRequest(); // AddApplicationVpcConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addApplicationVpcConfiguration(xAmzTarget, addApplicationVpcConfigurationRequest, opts, (error, data, response) => {
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
 **addApplicationVpcConfigurationRequest** | [**AddApplicationVpcConfigurationRequest**](AddApplicationVpcConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddApplicationVpcConfigurationResponse**](AddApplicationVpcConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createApplication

> CreateApplicationResponse createApplication(xAmzTarget, createApplicationRequest, opts)



Creates a Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html\&quot;&gt;Creating an Application&lt;/a&gt;.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createApplicationRequest = new AmazonKinesisAnalytics.CreateApplicationRequest(); // CreateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApplication(xAmzTarget, createApplicationRequest, opts, (error, data, response) => {
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
 **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createApplicationPresignedUrl

> CreateApplicationPresignedUrlResponse createApplicationPresignedUrl(xAmzTarget, createApplicationPresignedUrlRequest, opts)



&lt;p&gt;Creates and returns a URL that you can use to connect to an application&#39;s extension.&lt;/p&gt; &lt;p&gt;The IAM role or user used to call this API defines the permissions to access the extension. After the presigned URL is created, no additional permission is required to access this URL. IAM authorization policies for this API are also enforced for every HTTP request that attempts to connect to the extension. &lt;/p&gt; &lt;p&gt;You control the amount of time that the URL will be valid using the &lt;code&gt;SessionExpirationDurationInSeconds&lt;/code&gt; parameter. If you do not provide this parameter, the returned URL is valid for twelve hours.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The URL that you get from a call to CreateApplicationPresignedUrl must be used within 3 minutes to be valid. If you first try to use the URL after the 3-minute limit expires, the service returns an HTTP 403 Forbidden error.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createApplicationPresignedUrlRequest = new AmazonKinesisAnalytics.CreateApplicationPresignedUrlRequest(); // CreateApplicationPresignedUrlRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApplicationPresignedUrl(xAmzTarget, createApplicationPresignedUrlRequest, opts, (error, data, response) => {
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
 **createApplicationPresignedUrlRequest** | [**CreateApplicationPresignedUrlRequest**](CreateApplicationPresignedUrlRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateApplicationPresignedUrlResponse**](CreateApplicationPresignedUrlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createApplicationSnapshot

> Object createApplicationSnapshot(xAmzTarget, createApplicationSnapshotRequest, opts)



Creates a snapshot of the application&#39;s state data.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createApplicationSnapshotRequest = new AmazonKinesisAnalytics.CreateApplicationSnapshotRequest(); // CreateApplicationSnapshotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApplicationSnapshot(xAmzTarget, createApplicationSnapshotRequest, opts, (error, data, response) => {
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
 **createApplicationSnapshotRequest** | [**CreateApplicationSnapshotRequest**](CreateApplicationSnapshotRequest.md)|  | 
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


## deleteApplication

> Object deleteApplication(xAmzTarget, deleteApplicationRequest, opts)



Deletes the specified application. Kinesis Data Analytics halts application execution and deletes the application.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteApplicationRequest = new AmazonKinesisAnalytics.DeleteApplicationRequest(); // DeleteApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplication(xAmzTarget, deleteApplicationRequest, opts, (error, data, response) => {
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
 **deleteApplicationRequest** | [**DeleteApplicationRequest**](DeleteApplicationRequest.md)|  | 
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


## deleteApplicationCloudWatchLoggingOption

> DeleteApplicationCloudWatchLoggingOptionResponse deleteApplicationCloudWatchLoggingOption(xAmzTarget, deleteApplicationCloudWatchLoggingOptionRequest, opts)



Deletes an Amazon CloudWatch log stream from an Kinesis Data Analytics application. 

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteApplicationCloudWatchLoggingOptionRequest = new AmazonKinesisAnalytics.DeleteApplicationCloudWatchLoggingOptionRequest(); // DeleteApplicationCloudWatchLoggingOptionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplicationCloudWatchLoggingOption(xAmzTarget, deleteApplicationCloudWatchLoggingOptionRequest, opts, (error, data, response) => {
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
 **deleteApplicationCloudWatchLoggingOptionRequest** | [**DeleteApplicationCloudWatchLoggingOptionRequest**](DeleteApplicationCloudWatchLoggingOptionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApplicationCloudWatchLoggingOptionResponse**](DeleteApplicationCloudWatchLoggingOptionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplicationInputProcessingConfiguration

> DeleteApplicationInputProcessingConfigurationResponse deleteApplicationInputProcessingConfiguration(xAmzTarget, deleteApplicationInputProcessingConfigurationRequest, opts)



Deletes an &lt;a&gt;InputProcessingConfiguration&lt;/a&gt; from an input.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteApplicationInputProcessingConfigurationRequest = new AmazonKinesisAnalytics.DeleteApplicationInputProcessingConfigurationRequest(); // DeleteApplicationInputProcessingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplicationInputProcessingConfiguration(xAmzTarget, deleteApplicationInputProcessingConfigurationRequest, opts, (error, data, response) => {
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
 **deleteApplicationInputProcessingConfigurationRequest** | [**DeleteApplicationInputProcessingConfigurationRequest**](DeleteApplicationInputProcessingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApplicationInputProcessingConfigurationResponse**](DeleteApplicationInputProcessingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplicationOutput

> DeleteApplicationOutputResponse deleteApplicationOutput(xAmzTarget, deleteApplicationOutputRequest, opts)



Deletes the output destination configuration from your SQL-based Kinesis Data Analytics application&#39;s configuration. Kinesis Data Analytics will no longer write data from the corresponding in-application stream to the external output destination.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteApplicationOutputRequest = new AmazonKinesisAnalytics.DeleteApplicationOutputRequest(); // DeleteApplicationOutputRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplicationOutput(xAmzTarget, deleteApplicationOutputRequest, opts, (error, data, response) => {
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
 **deleteApplicationOutputRequest** | [**DeleteApplicationOutputRequest**](DeleteApplicationOutputRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApplicationOutputResponse**](DeleteApplicationOutputResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplicationReferenceDataSource

> DeleteApplicationReferenceDataSourceResponse deleteApplicationReferenceDataSource(xAmzTarget, deleteApplicationReferenceDataSourceRequest, opts)



&lt;p&gt;Deletes a reference data source configuration from the specified SQL-based Kinesis Data Analytics application&#39;s configuration.&lt;/p&gt; &lt;p&gt;If the application is running, Kinesis Data Analytics immediately removes the in-application table that you created using the &lt;a&gt;AddApplicationReferenceDataSource&lt;/a&gt; operation. &lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteApplicationReferenceDataSourceRequest = new AmazonKinesisAnalytics.DeleteApplicationReferenceDataSourceRequest(); // DeleteApplicationReferenceDataSourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplicationReferenceDataSource(xAmzTarget, deleteApplicationReferenceDataSourceRequest, opts, (error, data, response) => {
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
 **deleteApplicationReferenceDataSourceRequest** | [**DeleteApplicationReferenceDataSourceRequest**](DeleteApplicationReferenceDataSourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApplicationReferenceDataSourceResponse**](DeleteApplicationReferenceDataSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplicationSnapshot

> Object deleteApplicationSnapshot(xAmzTarget, deleteApplicationSnapshotRequest, opts)



Deletes a snapshot of application state.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteApplicationSnapshotRequest = new AmazonKinesisAnalytics.DeleteApplicationSnapshotRequest(); // DeleteApplicationSnapshotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplicationSnapshot(xAmzTarget, deleteApplicationSnapshotRequest, opts, (error, data, response) => {
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
 **deleteApplicationSnapshotRequest** | [**DeleteApplicationSnapshotRequest**](DeleteApplicationSnapshotRequest.md)|  | 
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


## deleteApplicationVpcConfiguration

> DeleteApplicationVpcConfigurationResponse deleteApplicationVpcConfiguration(xAmzTarget, deleteApplicationVpcConfigurationRequest, opts)



Removes a VPC configuration from a Kinesis Data Analytics application.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteApplicationVpcConfigurationRequest = new AmazonKinesisAnalytics.DeleteApplicationVpcConfigurationRequest(); // DeleteApplicationVpcConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApplicationVpcConfiguration(xAmzTarget, deleteApplicationVpcConfigurationRequest, opts, (error, data, response) => {
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
 **deleteApplicationVpcConfigurationRequest** | [**DeleteApplicationVpcConfigurationRequest**](DeleteApplicationVpcConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApplicationVpcConfigurationResponse**](DeleteApplicationVpcConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeApplication

> DescribeApplicationResponse describeApplication(xAmzTarget, describeApplicationRequest, opts)



&lt;p&gt;Returns information about a specific Kinesis Data Analytics application.&lt;/p&gt; &lt;p&gt;If you want to retrieve a list of all applications in your account, use the &lt;a&gt;ListApplications&lt;/a&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeApplicationRequest = new AmazonKinesisAnalytics.DescribeApplicationRequest(); // DescribeApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeApplication(xAmzTarget, describeApplicationRequest, opts, (error, data, response) => {
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
 **describeApplicationRequest** | [**DescribeApplicationRequest**](DescribeApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeApplicationResponse**](DescribeApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeApplicationSnapshot

> DescribeApplicationSnapshotResponse describeApplicationSnapshot(xAmzTarget, describeApplicationSnapshotRequest, opts)



Returns information about a snapshot of application state data.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeApplicationSnapshotRequest = new AmazonKinesisAnalytics.DescribeApplicationSnapshotRequest(); // DescribeApplicationSnapshotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeApplicationSnapshot(xAmzTarget, describeApplicationSnapshotRequest, opts, (error, data, response) => {
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
 **describeApplicationSnapshotRequest** | [**DescribeApplicationSnapshotRequest**](DescribeApplicationSnapshotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeApplicationSnapshotResponse**](DescribeApplicationSnapshotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeApplicationVersion

> DescribeApplicationVersionResponse describeApplicationVersion(xAmzTarget, describeApplicationVersionRequest, opts)



&lt;p&gt;Provides a detailed description of a specified version of the application. To see a list of all the versions of an application, invoke the &lt;a&gt;ListApplicationVersions&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is supported only for Amazon Kinesis Data Analytics for Apache Flink.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeApplicationVersionRequest = new AmazonKinesisAnalytics.DescribeApplicationVersionRequest(); // DescribeApplicationVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeApplicationVersion(xAmzTarget, describeApplicationVersionRequest, opts, (error, data, response) => {
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
 **describeApplicationVersionRequest** | [**DescribeApplicationVersionRequest**](DescribeApplicationVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeApplicationVersionResponse**](DescribeApplicationVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## discoverInputSchema

> DiscoverInputSchemaResponse discoverInputSchema(xAmzTarget, discoverInputSchemaRequest, opts)



&lt;p&gt;Infers a schema for a SQL-based Kinesis Data Analytics application by evaluating sample records on the specified streaming source (Kinesis data stream or Kinesis Data Firehose delivery stream) or Amazon S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.&lt;/p&gt; &lt;p&gt; You can use the inferred schema when configuring a streaming source for your application. When you create an application using the Kinesis Data Analytics console, the console uses this operation to infer a schema and show it in the console user interface. &lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let discoverInputSchemaRequest = new AmazonKinesisAnalytics.DiscoverInputSchemaRequest(); // DiscoverInputSchemaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.discoverInputSchema(xAmzTarget, discoverInputSchemaRequest, opts, (error, data, response) => {
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
 **discoverInputSchemaRequest** | [**DiscoverInputSchemaRequest**](DiscoverInputSchemaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DiscoverInputSchemaResponse**](DiscoverInputSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listApplicationSnapshots

> ListApplicationSnapshotsResponse listApplicationSnapshots(xAmzTarget, listApplicationSnapshotsRequest, opts)



Lists information about the current application snapshots.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listApplicationSnapshotsRequest = new AmazonKinesisAnalytics.ListApplicationSnapshotsRequest(); // ListApplicationSnapshotsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listApplicationSnapshots(xAmzTarget, listApplicationSnapshotsRequest, opts, (error, data, response) => {
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
 **listApplicationSnapshotsRequest** | [**ListApplicationSnapshotsRequest**](ListApplicationSnapshotsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListApplicationSnapshotsResponse**](ListApplicationSnapshotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listApplicationVersions

> ListApplicationVersionsResponse listApplicationVersions(xAmzTarget, listApplicationVersionsRequest, opts)



&lt;p&gt;Lists all the versions for the specified application, including versions that were rolled back. The response also includes a summary of the configuration associated with each version.&lt;/p&gt; &lt;p&gt;To get the complete description of a specific application version, invoke the &lt;a&gt;DescribeApplicationVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is supported only for Amazon Kinesis Data Analytics for Apache Flink.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listApplicationVersionsRequest = new AmazonKinesisAnalytics.ListApplicationVersionsRequest(); // ListApplicationVersionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listApplicationVersions(xAmzTarget, listApplicationVersionsRequest, opts, (error, data, response) => {
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
 **listApplicationVersionsRequest** | [**ListApplicationVersionsRequest**](ListApplicationVersionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListApplicationVersionsResponse**](ListApplicationVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listApplications

> ListApplicationsResponse listApplications(xAmzTarget, listApplicationsRequest, opts)



&lt;p&gt;Returns a list of Kinesis Data Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. &lt;/p&gt; &lt;p&gt;If you want detailed information about a specific application, use &lt;a&gt;DescribeApplication&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listApplicationsRequest = new AmazonKinesisAnalytics.ListApplicationsRequest(); // ListApplicationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listApplications(xAmzTarget, listApplicationsRequest, opts, (error, data, response) => {
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
 **listApplicationsRequest** | [**ListApplicationsRequest**](ListApplicationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListApplicationsResponse**](ListApplicationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Retrieves the list of key-value tags assigned to the application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AmazonKinesisAnalytics.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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


## rollbackApplication

> RollbackApplicationResponse rollbackApplication(xAmzTarget, rollbackApplicationRequest, opts)



&lt;p&gt;Reverts the application to the previous running version. You can roll back an application if you suspect it is stuck in a transient status. &lt;/p&gt; &lt;p&gt;You can roll back an application only if it is in the &lt;code&gt;UPDATING&lt;/code&gt; or &lt;code&gt;AUTOSCALING&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt;When you rollback an application, it loads state data from the last successful snapshot. If the application has no snapshots, Kinesis Data Analytics rejects the rollback request.&lt;/p&gt; &lt;p&gt;This action is not supported for Kinesis Data Analytics for SQL applications.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let rollbackApplicationRequest = new AmazonKinesisAnalytics.RollbackApplicationRequest(); // RollbackApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rollbackApplication(xAmzTarget, rollbackApplicationRequest, opts, (error, data, response) => {
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
 **rollbackApplicationRequest** | [**RollbackApplicationRequest**](RollbackApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RollbackApplicationResponse**](RollbackApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startApplication

> Object startApplication(xAmzTarget, startApplicationRequest, opts)



Starts the specified Kinesis Data Analytics application. After creating an application, you must exclusively call this operation to start your application.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startApplicationRequest = new AmazonKinesisAnalytics.StartApplicationRequest(); // StartApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startApplication(xAmzTarget, startApplicationRequest, opts, (error, data, response) => {
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
 **startApplicationRequest** | [**StartApplicationRequest**](StartApplicationRequest.md)|  | 
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


## stopApplication

> Object stopApplication(xAmzTarget, stopApplicationRequest, opts)



&lt;p&gt;Stops the application from processing data. You can stop an application only if it is in the running status, unless you set the &lt;code&gt;Force&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;a&gt;DescribeApplication&lt;/a&gt; operation to find the application status. &lt;/p&gt; &lt;p&gt;Kinesis Data Analytics takes a snapshot when the application is stopped, unless &lt;code&gt;Force&lt;/code&gt; is set to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopApplicationRequest = new AmazonKinesisAnalytics.StopApplicationRequest(); // StopApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopApplication(xAmzTarget, stopApplicationRequest, opts, (error, data, response) => {
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
 **stopApplicationRequest** | [**StopApplicationRequest**](StopApplicationRequest.md)|  | 
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

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Adds one or more key-value tags to a Kinesis Data Analytics application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AmazonKinesisAnalytics.TagResourceRequest(); // TagResourceRequest | 
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



Removes one or more tags from a Kinesis Data Analytics application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AmazonKinesisAnalytics.UntagResourceRequest(); // UntagResourceRequest | 
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


## updateApplication

> UpdateApplicationResponse updateApplication(xAmzTarget, updateApplicationRequest, opts)



&lt;p&gt;Updates an existing Kinesis Data Analytics application. Using this operation, you can update application code, input configuration, and output configuration. &lt;/p&gt; &lt;p&gt;Kinesis Data Analytics updates the &lt;code&gt;ApplicationVersionId&lt;/code&gt; each time you update your application. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot update the &lt;code&gt;RuntimeEnvironment&lt;/code&gt; of an existing application. If you need to update an application&#39;s &lt;code&gt;RuntimeEnvironment&lt;/code&gt;, you must delete the application and create it again.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateApplicationRequest = new AmazonKinesisAnalytics.UpdateApplicationRequest(); // UpdateApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApplication(xAmzTarget, updateApplicationRequest, opts, (error, data, response) => {
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
 **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApplicationMaintenanceConfiguration

> UpdateApplicationMaintenanceConfigurationResponse updateApplicationMaintenanceConfiguration(xAmzTarget, updateApplicationMaintenanceConfigurationRequest, opts)



&lt;p&gt;Updates the maintenance configuration of the Kinesis Data Analytics application. &lt;/p&gt; &lt;p&gt;You can invoke this operation on an application that is in one of the two following states: &lt;code&gt;READY&lt;/code&gt; or &lt;code&gt;RUNNING&lt;/code&gt;. If you invoke it when the application is in a state other than these two states, it throws a &lt;code&gt;ResourceInUseException&lt;/code&gt;. The service makes use of the updated configuration the next time it schedules maintenance for the application. If you invoke this operation after the service schedules maintenance, the service will apply the configuration update the next time it schedules maintenance for the application. This means that you might not see the maintenance configuration update applied to the maintenance process that follows a successful invocation of this operation, but to the following maintenance process instead.&lt;/p&gt; &lt;p&gt;To see the current maintenance configuration of your application, invoke the &lt;a&gt;DescribeApplication&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;For information about application maintenance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/maintenance.html\&quot;&gt;Kinesis Data Analytics for Apache Flink Maintenance&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is supported only for Amazon Kinesis Data Analytics for Apache Flink.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonKinesisAnalytics from 'amazon_kinesis_analytics';
let defaultClient = AmazonKinesisAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisAnalytics.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateApplicationMaintenanceConfigurationRequest = new AmazonKinesisAnalytics.UpdateApplicationMaintenanceConfigurationRequest(); // UpdateApplicationMaintenanceConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApplicationMaintenanceConfiguration(xAmzTarget, updateApplicationMaintenanceConfigurationRequest, opts, (error, data, response) => {
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
 **updateApplicationMaintenanceConfigurationRequest** | [**UpdateApplicationMaintenanceConfigurationRequest**](UpdateApplicationMaintenanceConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApplicationMaintenanceConfigurationResponse**](UpdateApplicationMaintenanceConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

