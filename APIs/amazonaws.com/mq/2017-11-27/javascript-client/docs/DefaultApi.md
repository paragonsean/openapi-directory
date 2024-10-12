# AmazonMq.DefaultApi

All URIs are relative to *http://mq.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBroker**](DefaultApi.md#createBroker) | **POST** /v1/brokers | 
[**createConfiguration**](DefaultApi.md#createConfiguration) | **POST** /v1/configurations | 
[**createTags**](DefaultApi.md#createTags) | **POST** /v1/tags/{resource-arn} | 
[**createUser**](DefaultApi.md#createUser) | **POST** /v1/brokers/{broker-id}/users/{username} | 
[**deleteBroker**](DefaultApi.md#deleteBroker) | **DELETE** /v1/brokers/{broker-id} | 
[**deleteTags**](DefaultApi.md#deleteTags) | **DELETE** /v1/tags/{resource-arn}#tagKeys | 
[**deleteUser**](DefaultApi.md#deleteUser) | **DELETE** /v1/brokers/{broker-id}/users/{username} | 
[**describeBroker**](DefaultApi.md#describeBroker) | **GET** /v1/brokers/{broker-id} | 
[**describeBrokerEngineTypes**](DefaultApi.md#describeBrokerEngineTypes) | **GET** /v1/broker-engine-types | 
[**describeBrokerInstanceOptions**](DefaultApi.md#describeBrokerInstanceOptions) | **GET** /v1/broker-instance-options | 
[**describeConfiguration**](DefaultApi.md#describeConfiguration) | **GET** /v1/configurations/{configuration-id} | 
[**describeConfigurationRevision**](DefaultApi.md#describeConfigurationRevision) | **GET** /v1/configurations/{configuration-id}/revisions/{configuration-revision} | 
[**describeUser**](DefaultApi.md#describeUser) | **GET** /v1/brokers/{broker-id}/users/{username} | 
[**listBrokers**](DefaultApi.md#listBrokers) | **GET** /v1/brokers | 
[**listConfigurationRevisions**](DefaultApi.md#listConfigurationRevisions) | **GET** /v1/configurations/{configuration-id}/revisions | 
[**listConfigurations**](DefaultApi.md#listConfigurations) | **GET** /v1/configurations | 
[**listTags**](DefaultApi.md#listTags) | **GET** /v1/tags/{resource-arn} | 
[**listUsers**](DefaultApi.md#listUsers) | **GET** /v1/brokers/{broker-id}/users | 
[**promote**](DefaultApi.md#promote) | **POST** /v1/brokers/{broker-id}/promote | 
[**rebootBroker**](DefaultApi.md#rebootBroker) | **POST** /v1/brokers/{broker-id}/reboot | 
[**updateBroker**](DefaultApi.md#updateBroker) | **PUT** /v1/brokers/{broker-id} | 
[**updateConfiguration**](DefaultApi.md#updateConfiguration) | **PUT** /v1/configurations/{configuration-id} | 
[**updateUser**](DefaultApi.md#updateUser) | **PUT** /v1/brokers/{broker-id}/users/{username} | 



## createBroker

> CreateBrokerResponse createBroker(createBrokerRequest, opts)



&lt;p&gt;Creates a broker. Note: This API is asynchronous.&lt;/p&gt; &lt;p&gt;To create a broker, you must either use the AmazonMQFullAccess IAM policy or include the following EC2 permissions in your IAM policy.&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;ec2:CreateNetworkInterface&lt;/p&gt; &lt;p&gt;This permission is required to allow Amazon MQ to create an elastic network interface (ENI) on behalf of your account.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:CreateNetworkInterfacePermission&lt;/p&gt; &lt;p&gt;This permission is required to attach the ENI to the broker instance.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DeleteNetworkInterface&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DeleteNetworkInterfacePermission&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DetachNetworkInterface&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeInternetGateways&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeNetworkInterfaces&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeNetworkInterfacePermissions&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeRouteTables&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeSecurityGroups&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeSubnets&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeVpcs&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/amazon-mq-setting-up.html#create-iam-user\&quot;&gt;Create an IAM User and Get Your Amazon Web Services Credentials&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/connecting-to-amazon-mq.html#never-modify-delete-elastic-network-interface\&quot;&gt;Never Modify or Delete the Amazon MQ Elastic Network Interface&lt;/a&gt; in the &lt;i&gt;Amazon MQ Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let createBrokerRequest = new AmazonMq.CreateBrokerRequest(); // CreateBrokerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBroker(createBrokerRequest, opts, (error, data, response) => {
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
 **createBrokerRequest** | [**CreateBrokerRequest**](CreateBrokerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBrokerResponse**](CreateBrokerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createConfiguration

> CreateConfigurationResponse createConfiguration(createConfigurationRequest, opts)



Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version).

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let createConfigurationRequest = new AmazonMq.CreateConfigurationRequest(); // CreateConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConfiguration(createConfigurationRequest, opts, (error, data, response) => {
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
 **createConfigurationRequest** | [**CreateConfigurationRequest**](CreateConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateConfigurationResponse**](CreateConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTags

> createTags(resourceArn, createTagsRequest, opts)



Add a tag to a resource.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource tag.
let createTagsRequest = new AmazonMq.CreateTagsRequest(); // CreateTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTags(resourceArn, createTagsRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource tag. | 
 **createTagsRequest** | [**CreateTagsRequest**](CreateTagsRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## createUser

> Object createUser(brokerId, username, createUserRequest, opts)



&lt;p&gt;Creates an ActiveMQ user.&lt;/p&gt; &lt;important&gt;&lt;p&gt;Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker usernames are not intended to be used for private or sensitive data.&lt;/p&gt;&lt;/important&gt;

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let username = "username_example"; // String | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
let createUserRequest = new AmazonMq.CreateUserRequest(); // CreateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUser(brokerId, username, createUserRequest, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **username** | **String**| The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. | 
 **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
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


## deleteBroker

> DeleteBrokerResponse deleteBroker(brokerId, opts)



Deletes a broker. Note: This API is asynchronous.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBroker(brokerId, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBrokerResponse**](DeleteBrokerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTags

> deleteTags(resourceArn, tagKeys, opts)



Removes a tag from a resource.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource tag.
let tagKeys = ["null"]; // [String] | An array of tag keys to delete
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTags(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource tag. | 
 **tagKeys** | [**[String]**](String.md)| An array of tag keys to delete | 
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


## deleteUser

> Object deleteUser(brokerId, username, opts)



Deletes an ActiveMQ user.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let username = "username_example"; // String | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUser(brokerId, username, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **username** | **String**| The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. | 
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


## describeBroker

> DescribeBrokerResponse describeBroker(brokerId, opts)



Returns information about the specified broker.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBroker(brokerId, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBrokerResponse**](DescribeBrokerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBrokerEngineTypes

> DescribeBrokerEngineTypesResponse describeBrokerEngineTypes(opts)



Describe available engine types and versions.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'engineType': "engineType_example", // String | Filter response by engine type.
  'maxResults': 56, // Number | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
  'nextToken': "nextToken_example" // String | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
};
apiInstance.describeBrokerEngineTypes(opts, (error, data, response) => {
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
 **engineType** | **String**| Filter response by engine type. | [optional] 
 **maxResults** | **Number**| The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. | [optional] 
 **nextToken** | **String**| The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. | [optional] 

### Return type

[**DescribeBrokerEngineTypesResponse**](DescribeBrokerEngineTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBrokerInstanceOptions

> DescribeBrokerInstanceOptionsResponse describeBrokerInstanceOptions(opts)



Describe available broker instance options.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'engineType': "engineType_example", // String | Filter response by engine type.
  'hostInstanceType': "hostInstanceType_example", // String | Filter response by host instance type.
  'maxResults': 56, // Number | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
  'nextToken': "nextToken_example", // String | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
  'storageType': "storageType_example" // String | Filter response by storage type.
};
apiInstance.describeBrokerInstanceOptions(opts, (error, data, response) => {
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
 **engineType** | **String**| Filter response by engine type. | [optional] 
 **hostInstanceType** | **String**| Filter response by host instance type. | [optional] 
 **maxResults** | **Number**| The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. | [optional] 
 **nextToken** | **String**| The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. | [optional] 
 **storageType** | **String**| Filter response by storage type. | [optional] 

### Return type

[**DescribeBrokerInstanceOptionsResponse**](DescribeBrokerInstanceOptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeConfiguration

> DescribeConfigurationResponse describeConfiguration(configurationId, opts)



Returns information about the specified configuration.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let configurationId = "configurationId_example"; // String | The unique ID that Amazon MQ generates for the configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeConfiguration(configurationId, opts, (error, data, response) => {
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
 **configurationId** | **String**| The unique ID that Amazon MQ generates for the configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeConfigurationResponse**](DescribeConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeConfigurationRevision

> DescribeConfigurationRevisionResponse describeConfigurationRevision(configurationId, configurationRevision, opts)



Returns the specified configuration revision for the specified configuration.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let configurationId = "configurationId_example"; // String | The unique ID that Amazon MQ generates for the configuration.
let configurationRevision = "configurationRevision_example"; // String | The revision of the configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeConfigurationRevision(configurationId, configurationRevision, opts, (error, data, response) => {
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
 **configurationId** | **String**| The unique ID that Amazon MQ generates for the configuration. | 
 **configurationRevision** | **String**| The revision of the configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeConfigurationRevisionResponse**](DescribeConfigurationRevisionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeUser

> DescribeUserResponse describeUser(brokerId, username, opts)



Returns information about an ActiveMQ user.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let username = "username_example"; // String | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeUser(brokerId, username, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **username** | **String**| The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeUserResponse**](DescribeUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBrokers

> ListBrokersResponse listBrokers(opts)



Returns a list of all brokers.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
  'nextToken': "nextToken_example", // String | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBrokers(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. | [optional] 
 **nextToken** | **String**| The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBrokersResponse**](ListBrokersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurationRevisions

> ListConfigurationRevisionsResponse listConfigurationRevisions(configurationId, opts)



Returns a list of all revisions for the specified configuration.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let configurationId = "configurationId_example"; // String | The unique ID that Amazon MQ generates for the configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
  'nextToken': "nextToken_example" // String | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
};
apiInstance.listConfigurationRevisions(configurationId, opts, (error, data, response) => {
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
 **configurationId** | **String**| The unique ID that Amazon MQ generates for the configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. | [optional] 
 **nextToken** | **String**| The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. | [optional] 

### Return type

[**ListConfigurationRevisionsResponse**](ListConfigurationRevisionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurations

> ListConfigurationsResponse listConfigurations(opts)



Returns a list of all configurations.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
  'nextToken': "nextToken_example" // String | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
};
apiInstance.listConfigurations(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. | [optional] 
 **nextToken** | **String**| The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. | [optional] 

### Return type

[**ListConfigurationsResponse**](ListConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTags

> ListTagsResponse listTags(resourceArn, opts)



Lists tags for a resource.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource tag.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTags(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource tag. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsers

> ListUsersResponse listUsers(brokerId, opts)



Returns a list of all ActiveMQ users.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
  'nextToken': "nextToken_example" // String | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
};
apiInstance.listUsers(brokerId, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. | [optional] 
 **nextToken** | **String**| The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## promote

> PromoteResponse promote(brokerId, promoteRequest, opts)



Promotes a data replication replica broker to the primary broker role.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let promoteRequest = new AmazonMq.PromoteRequest(); // PromoteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.promote(brokerId, promoteRequest, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **promoteRequest** | [**PromoteRequest**](PromoteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PromoteResponse**](PromoteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rebootBroker

> Object rebootBroker(brokerId, opts)



Reboots a broker. Note: This API is asynchronous.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rebootBroker(brokerId, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
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


## updateBroker

> UpdateBrokerResponse updateBroker(brokerId, updateBrokerRequest, opts)



Adds a pending configuration change to a broker.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let updateBrokerRequest = new AmazonMq.UpdateBrokerRequest(); // UpdateBrokerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBroker(brokerId, updateBrokerRequest, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **updateBrokerRequest** | [**UpdateBrokerRequest**](UpdateBrokerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBrokerResponse**](UpdateBrokerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConfiguration

> UpdateConfigurationResponse updateConfiguration(configurationId, updateConfigurationRequest, opts)



Updates the specified configuration.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let configurationId = "configurationId_example"; // String | The unique ID that Amazon MQ generates for the configuration.
let updateConfigurationRequest = new AmazonMq.UpdateConfigurationRequest(); // UpdateConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConfiguration(configurationId, updateConfigurationRequest, opts, (error, data, response) => {
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
 **configurationId** | **String**| The unique ID that Amazon MQ generates for the configuration. | 
 **updateConfigurationRequest** | [**UpdateConfigurationRequest**](UpdateConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateConfigurationResponse**](UpdateConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUser

> Object updateUser(brokerId, username, updateUserRequest, opts)



Updates the information for an ActiveMQ user.

### Example

```javascript
import AmazonMq from 'amazon_mq';
let defaultClient = AmazonMq.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMq.DefaultApi();
let brokerId = "brokerId_example"; // String | The unique ID that Amazon MQ generates for the broker.
let username = "username_example"; // String | The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
let updateUserRequest = new AmazonMq.UpdateUserRequest(); // UpdateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUser(brokerId, username, updateUserRequest, opts, (error, data, response) => {
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
 **brokerId** | **String**| The unique ID that Amazon MQ generates for the broker. | 
 **username** | **String**| The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. | 
 **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
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

