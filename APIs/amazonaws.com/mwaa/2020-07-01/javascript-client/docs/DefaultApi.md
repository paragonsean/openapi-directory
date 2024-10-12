# AmazonMwaa.DefaultApi

All URIs are relative to *http://airflow.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCliToken**](DefaultApi.md#createCliToken) | **POST** /clitoken/{Name} | 
[**createEnvironment**](DefaultApi.md#createEnvironment) | **PUT** /environments/{Name} | 
[**createWebLoginToken**](DefaultApi.md#createWebLoginToken) | **POST** /webtoken/{Name} | 
[**deleteEnvironment**](DefaultApi.md#deleteEnvironment) | **DELETE** /environments/{Name} | 
[**getEnvironment**](DefaultApi.md#getEnvironment) | **GET** /environments/{Name} | 
[**listEnvironments**](DefaultApi.md#listEnvironments) | **GET** /environments | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**publishMetrics**](DefaultApi.md#publishMetrics) | **POST** /metrics/environments/{EnvironmentName} | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateEnvironment**](DefaultApi.md#updateEnvironment) | **PATCH** /environments/{Name} | 



## createCliToken

> CreateCliTokenResponse createCliToken(name, opts)



Creates a CLI token for the Airflow CLI. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-cli.html\&quot;&gt;Creating an Apache Airflow CLI token&lt;/a&gt;.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let name = "name_example"; // String | The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCliToken(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCliTokenResponse**](CreateCliTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createEnvironment

> CreateEnvironmentOutput createEnvironment(name, createEnvironmentRequest, opts)



Creates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let name = "name_example"; // String | The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.
let createEnvironmentRequest = new AmazonMwaa.CreateEnvironmentRequest(); // CreateEnvironmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEnvironment(name, createEnvironmentRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;. | 
 **createEnvironmentRequest** | [**CreateEnvironmentRequest**](CreateEnvironmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateEnvironmentOutput**](CreateEnvironmentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWebLoginToken

> CreateWebLoginTokenResponse createWebLoginToken(name, opts)



Creates a web login token for the Airflow Web UI. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-web.html\&quot;&gt;Creating an Apache Airflow web login token&lt;/a&gt;.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let name = "name_example"; // String | The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWebLoginToken(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWebLoginTokenResponse**](CreateWebLoginTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEnvironment

> Object deleteEnvironment(name, opts)



Deletes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let name = "name_example"; // String | The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEnvironment(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;. | 
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


## getEnvironment

> GetEnvironmentOutput getEnvironment(name, opts)



Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let name = "name_example"; // String | The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEnvironment(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEnvironmentOutput**](GetEnvironmentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEnvironments

> ListEnvironmentsOutput listEnvironments(opts)



Lists the Amazon Managed Workflows for Apache Airflow (MWAA) environments.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to retrieve per page. For example, <code>5</code> environments per page.
  'nextToken': "nextToken_example" // String | Retrieves the next page of the results.
};
apiInstance.listEnvironments(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to retrieve per page. For example, &lt;code&gt;5&lt;/code&gt; environments per page. | [optional] 
 **nextToken** | **String**| Retrieves the next page of the results. | [optional] 

### Return type

[**ListEnvironmentsOutput**](ListEnvironmentsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(resourceArn, opts)



Lists the key-value tag pairs associated to the Amazon Managed Workflows for Apache Airflow (MWAA) environment. For example, &lt;code&gt;\&quot;Environment\&quot;: \&quot;Staging\&quot;&lt;/code&gt;. 

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, &lt;code&gt;arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishMetrics

> Object publishMetrics(environmentName, publishMetricsRequest, opts)



 &lt;b&gt;Internal only&lt;/b&gt;. Publishes environment health metrics to Amazon CloudWatch.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let environmentName = "environmentName_example"; // String |  <b>Internal only</b>. The name of the environment.
let publishMetricsRequest = new AmazonMwaa.PublishMetricsRequest(); // PublishMetricsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.publishMetrics(environmentName, publishMetricsRequest, opts, (error, data, response) => {
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
 **environmentName** | **String**|  &lt;b&gt;Internal only&lt;/b&gt;. The name of the environment. | 
 **publishMetricsRequest** | [**PublishMetricsRequest**](PublishMetricsRequest.md)|  | 
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



Associates key-value tag pairs to your Amazon Managed Workflows for Apache Airflow (MWAA) environment. 

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.
let tagResourceRequest = new AmazonMwaa.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, &lt;code&gt;arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment&lt;/code&gt;. | 
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



Removes key-value tag pairs associated to your Amazon Managed Workflows for Apache Airflow (MWAA) environment. For example, &lt;code&gt;\&quot;Environment\&quot;: \&quot;Staging\&quot;&lt;/code&gt;.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.
let tagKeys = ["null"]; // [String] | The key-value tag pair you want to remove. For example, <code>\"Environment\": \"Staging\"</code>. 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, &lt;code&gt;arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment&lt;/code&gt;. | 
 **tagKeys** | [**[String]**](String.md)| The key-value tag pair you want to remove. For example, &lt;code&gt;\&quot;Environment\&quot;: \&quot;Staging\&quot;&lt;/code&gt;.  | 
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


## updateEnvironment

> UpdateEnvironmentOutput updateEnvironment(name, updateEnvironmentRequest, opts)



Updates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

### Example

```javascript
import AmazonMwaa from 'amazon_mwaa';
let defaultClient = AmazonMwaa.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMwaa.DefaultApi();
let name = "name_example"; // String | The name of your Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.
let updateEnvironmentRequest = new AmazonMwaa.UpdateEnvironmentRequest(); // UpdateEnvironmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEnvironment(name, updateEnvironmentRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of your Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;. | 
 **updateEnvironmentRequest** | [**UpdateEnvironmentRequest**](UpdateEnvironmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateEnvironmentOutput**](UpdateEnvironmentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

