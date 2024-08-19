# AwsResourceGroups.DefaultApi

All URIs are relative to *http://resource-groups.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGroup**](DefaultApi.md#createGroup) | **POST** /groups | 
[**deleteGroup**](DefaultApi.md#deleteGroup) | **POST** /delete-group | 
[**getAccountSettings**](DefaultApi.md#getAccountSettings) | **POST** /get-account-settings | 
[**getGroup**](DefaultApi.md#getGroup) | **POST** /get-group | 
[**getGroupConfiguration**](DefaultApi.md#getGroupConfiguration) | **POST** /get-group-configuration | 
[**getGroupQuery**](DefaultApi.md#getGroupQuery) | **POST** /get-group-query | 
[**getTags**](DefaultApi.md#getTags) | **GET** /resources/{Arn}/tags | 
[**groupResources**](DefaultApi.md#groupResources) | **POST** /group-resources | 
[**listGroupResources**](DefaultApi.md#listGroupResources) | **POST** /list-group-resources | 
[**listGroups**](DefaultApi.md#listGroups) | **POST** /groups-list | 
[**putGroupConfiguration**](DefaultApi.md#putGroupConfiguration) | **POST** /put-group-configuration | 
[**searchResources**](DefaultApi.md#searchResources) | **POST** /resources/search | 
[**tag**](DefaultApi.md#tag) | **PUT** /resources/{Arn}/tags | 
[**ungroupResources**](DefaultApi.md#ungroupResources) | **POST** /ungroup-resources | 
[**untag**](DefaultApi.md#untag) | **PATCH** /resources/{Arn}/tags | 
[**updateAccountSettings**](DefaultApi.md#updateAccountSettings) | **POST** /update-account-settings | 
[**updateGroup**](DefaultApi.md#updateGroup) | **POST** /update-group | 
[**updateGroupQuery**](DefaultApi.md#updateGroupQuery) | **POST** /update-group-query | 



## createGroup

> CreateGroupOutput createGroup(createGroupRequest, opts)



&lt;p&gt;Creates a resource group with the specified name and description. You can optionally include either a resource query or a service configuration. For more information about constructing a resource query, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/userguide/getting_started-query.html\&quot;&gt;Build queries and groups in Resource Groups&lt;/a&gt; in the &lt;i&gt;Resource Groups User Guide&lt;/i&gt;. For more information about service-linked groups and service configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html\&quot;&gt;Service configurations for Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:CreateGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let createGroupRequest = new AwsResourceGroups.CreateGroupRequest(); // CreateGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createGroup(createGroupRequest, opts, (error, data, response) => {
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
 **createGroupRequest** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateGroupOutput**](CreateGroupOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGroup

> DeleteGroupOutput deleteGroup(deleteGroupRequest, opts)



&lt;p&gt;Deletes the specified resource group. Deleting a resource group does not delete any resources that are members of the group; it only deletes the group structure.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:DeleteGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let deleteGroupRequest = new AwsResourceGroups.DeleteGroupRequest(); // DeleteGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteGroup(deleteGroupRequest, opts, (error, data, response) => {
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
 **deleteGroupRequest** | [**DeleteGroupRequest**](DeleteGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteGroupOutput**](DeleteGroupOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccountSettings

> GetAccountSettingsOutput getAccountSettings(opts)



Retrieves the current status of optional features in Resource Groups.

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccountSettings(opts, (error, data, response) => {
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

[**GetAccountSettingsOutput**](GetAccountSettingsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroup

> GetGroupOutput getGroup(getGroupRequest, opts)



&lt;p&gt;Returns information about a specified resource group.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GetGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let getGroupRequest = new AwsResourceGroups.GetGroupRequest(); // GetGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGroup(getGroupRequest, opts, (error, data, response) => {
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
 **getGroupRequest** | [**GetGroupRequest**](GetGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGroupOutput**](GetGroupOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getGroupConfiguration

> GetGroupConfigurationOutput getGroupConfiguration(getGroupConfigurationRequest, opts)



&lt;p&gt;Retrieves the service configuration associated with the specified resource group. For details about the service configuration syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html\&quot;&gt;Service configurations for Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GetGroupConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let getGroupConfigurationRequest = new AwsResourceGroups.GetGroupConfigurationRequest(); // GetGroupConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGroupConfiguration(getGroupConfigurationRequest, opts, (error, data, response) => {
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
 **getGroupConfigurationRequest** | [**GetGroupConfigurationRequest**](GetGroupConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGroupConfigurationOutput**](GetGroupConfigurationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getGroupQuery

> GetGroupQueryOutput getGroupQuery(getGroupQueryRequest, opts)



&lt;p&gt;Retrieves the resource query associated with the specified resource group. For more information about resource queries, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag\&quot;&gt;Create a tag-based group in Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GetGroupQuery&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let getGroupQueryRequest = new AwsResourceGroups.GetGroupQueryRequest(); // GetGroupQueryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGroupQuery(getGroupQueryRequest, opts, (error, data, response) => {
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
 **getGroupQueryRequest** | [**GetGroupQueryRequest**](GetGroupQueryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGroupQueryOutput**](GetGroupQueryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTags

> GetTagsOutput getTags(arn, opts)



&lt;p&gt;Returns a list of tags that are associated with a resource group, specified by an ARN.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GetTags&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let arn = "arn_example"; // String | The ARN of the resource group whose tags you want to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTags(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The ARN of the resource group whose tags you want to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTagsOutput**](GetTagsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupResources

> GroupResourcesOutput groupResources(groupResourcesRequest, opts)



&lt;p&gt;Adds the specified resources to the specified group.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can use this operation with only resource groups that are configured with the following types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS::EC2::HostManagement&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS::EC2::CapacityReservationPool&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Other resource group type and resource types aren&#39;t currently supported by this operation.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GroupResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let groupResourcesRequest = new AwsResourceGroups.GroupResourcesRequest(); // GroupResourcesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.groupResources(groupResourcesRequest, opts, (error, data, response) => {
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
 **groupResourcesRequest** | [**GroupResourcesRequest**](GroupResourcesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GroupResourcesOutput**](GroupResourcesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGroupResources

> ListGroupResourcesOutput listGroupResources(listGroupResourcesRequest, opts)



&lt;p&gt;Returns a list of ARNs of the resources that are members of a specified resource group.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:ListGroupResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudformation:DescribeStacks&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudformation:ListStackResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tag:GetResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let listGroupResourcesRequest = new AwsResourceGroups.ListGroupResourcesRequest(); // ListGroupResourcesRequest | 
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
apiInstance.listGroupResources(listGroupResourcesRequest, opts, (error, data, response) => {
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
 **listGroupResourcesRequest** | [**ListGroupResourcesRequest**](ListGroupResourcesRequest.md)|  | 
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

[**ListGroupResourcesOutput**](ListGroupResourcesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGroups

> ListGroupsOutput listGroups(listGroupsRequest, opts)



&lt;p&gt;Returns a list of existing Resource Groups in your account.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:ListGroups&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let listGroupsRequest = new AwsResourceGroups.ListGroupsRequest(); // ListGroupsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.
  'nextToken': "nextToken_example", // String | The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listGroups(listGroupsRequest, opts, (error, data, response) => {
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
 **listGroupsRequest** | [**ListGroupsRequest**](ListGroupsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is present and has a value (is not null). Include that value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. | [optional] 
 **nextToken** | **String**| The parameter for receiving additional results if you receive a &lt;code&gt;NextToken&lt;/code&gt; response in a previous request. A &lt;code&gt;NextToken&lt;/code&gt; response indicates that more output is available. Set this parameter to the value provided by a previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to indicate where the output should continue from. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListGroupsOutput**](ListGroupsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putGroupConfiguration

> Object putGroupConfiguration(putGroupConfigurationRequest, opts)



&lt;p&gt;Attaches a service configuration to the specified group. This occurs asynchronously, and can take time to complete. You can use &lt;a&gt;GetGroupConfiguration&lt;/a&gt; to check the status of the update.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:PutGroupConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let putGroupConfigurationRequest = new AwsResourceGroups.PutGroupConfigurationRequest(); // PutGroupConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putGroupConfiguration(putGroupConfigurationRequest, opts, (error, data, response) => {
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
 **putGroupConfigurationRequest** | [**PutGroupConfigurationRequest**](PutGroupConfigurationRequest.md)|  | 
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


## searchResources

> SearchResourcesOutput searchResources(searchResourcesRequest, opts)



&lt;p&gt;Returns a list of Amazon Web Services resource identifiers that matches the specified query. The query uses the same format as a resource query in a &lt;a&gt;CreateGroup&lt;/a&gt; or &lt;a&gt;UpdateGroupQuery&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:SearchResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudformation:DescribeStacks&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudformation:ListStackResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tag:GetResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let searchResourcesRequest = new AwsResourceGroups.SearchResourcesRequest(); // SearchResourcesRequest | 
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
apiInstance.searchResources(searchResourcesRequest, opts, (error, data, response) => {
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
 **searchResourcesRequest** | [**SearchResourcesRequest**](SearchResourcesRequest.md)|  | 
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

[**SearchResourcesOutput**](SearchResourcesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tag

> TagOutput tag(arn, tagRequest, opts)



&lt;p&gt;Adds tags to a resource group with the specified ARN. Existing tags on a resource group are not changed if they are not specified in the request parameters.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:Tag&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let arn = "arn_example"; // String | The ARN of the resource group to which to add tags.
let tagRequest = new AwsResourceGroups.TagRequest(); // TagRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tag(arn, tagRequest, opts, (error, data, response) => {
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
 **arn** | **String**| The ARN of the resource group to which to add tags. | 
 **tagRequest** | [**TagRequest**](TagRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TagOutput**](TagOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ungroupResources

> UngroupResourcesOutput ungroupResources(ungroupResourcesRequest, opts)



&lt;p&gt;Removes the specified resources from the specified group. This operation works only with static groups that you populated using the &lt;a&gt;GroupResources&lt;/a&gt; operation. It doesn&#39;t work with any resource groups that are automatically populated by tag-based or CloudFormation stack-based queries.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:UngroupResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let ungroupResourcesRequest = new AwsResourceGroups.UngroupResourcesRequest(); // UngroupResourcesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.ungroupResources(ungroupResourcesRequest, opts, (error, data, response) => {
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
 **ungroupResourcesRequest** | [**UngroupResourcesRequest**](UngroupResourcesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UngroupResourcesOutput**](UngroupResourcesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untag

> UntagOutput untag(arn, untagRequest, opts)



&lt;p&gt;Deletes tags from a specified resource group.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:Untag&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let arn = "arn_example"; // String | The ARN of the resource group from which to remove tags. The command removed both the specified keys and any values associated with those keys.
let untagRequest = new AwsResourceGroups.UntagRequest(); // UntagRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untag(arn, untagRequest, opts, (error, data, response) => {
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
 **arn** | **String**| The ARN of the resource group from which to remove tags. The command removed both the specified keys and any values associated with those keys. | 
 **untagRequest** | [**UntagRequest**](UntagRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UntagOutput**](UntagOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAccountSettings

> UpdateAccountSettingsOutput updateAccountSettings(updateAccountSettingsRequest, opts)



&lt;p&gt;Turns on or turns off optional features in Resource Groups.&lt;/p&gt; &lt;p&gt;The preceding example shows that the request to turn on group lifecycle events is &lt;code&gt;IN_PROGRESS&lt;/code&gt;. You can call the &lt;a&gt;GetAccountSettings&lt;/a&gt; operation to check for completion by looking for &lt;code&gt;GroupLifecycleEventsStatus&lt;/code&gt; to change to &lt;code&gt;ACTIVE&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let updateAccountSettingsRequest = new AwsResourceGroups.UpdateAccountSettingsRequest(); // UpdateAccountSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccountSettings(updateAccountSettingsRequest, opts, (error, data, response) => {
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
 **updateAccountSettingsRequest** | [**UpdateAccountSettingsRequest**](UpdateAccountSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAccountSettingsOutput**](UpdateAccountSettingsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGroup

> UpdateGroupOutput updateGroup(updateGroupRequest, opts)



&lt;p&gt;Updates the description for an existing group. You cannot update the name of a resource group.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:UpdateGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let updateGroupRequest = new AwsResourceGroups.UpdateGroupRequest(); // UpdateGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGroup(updateGroupRequest, opts, (error, data, response) => {
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
 **updateGroupRequest** | [**UpdateGroupRequest**](UpdateGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateGroupOutput**](UpdateGroupOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGroupQuery

> UpdateGroupQueryOutput updateGroupQuery(updateGroupQueryRequest, opts)



&lt;p&gt;Updates the resource query of a group. For more information about resource queries, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag\&quot;&gt;Create a tag-based group in Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:UpdateGroupQuery&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsResourceGroups from 'aws_resource_groups';
let defaultClient = AwsResourceGroups.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceGroups.DefaultApi();
let updateGroupQueryRequest = new AwsResourceGroups.UpdateGroupQueryRequest(); // UpdateGroupQueryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGroupQuery(updateGroupQueryRequest, opts, (error, data, response) => {
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
 **updateGroupQueryRequest** | [**UpdateGroupQueryRequest**](UpdateGroupQueryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateGroupQueryOutput**](UpdateGroupQueryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

