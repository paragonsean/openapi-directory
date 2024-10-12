# AwsSupportApp.DefaultApi

All URIs are relative to *http://supportapp.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSlackChannelConfiguration**](DefaultApi.md#createSlackChannelConfiguration) | **POST** /control/create-slack-channel-configuration | 
[**deleteAccountAlias**](DefaultApi.md#deleteAccountAlias) | **POST** /control/delete-account-alias | 
[**deleteSlackChannelConfiguration**](DefaultApi.md#deleteSlackChannelConfiguration) | **POST** /control/delete-slack-channel-configuration | 
[**deleteSlackWorkspaceConfiguration**](DefaultApi.md#deleteSlackWorkspaceConfiguration) | **POST** /control/delete-slack-workspace-configuration | 
[**getAccountAlias**](DefaultApi.md#getAccountAlias) | **POST** /control/get-account-alias | 
[**listSlackChannelConfigurations**](DefaultApi.md#listSlackChannelConfigurations) | **POST** /control/list-slack-channel-configurations | 
[**listSlackWorkspaceConfigurations**](DefaultApi.md#listSlackWorkspaceConfigurations) | **POST** /control/list-slack-workspace-configurations | 
[**putAccountAlias**](DefaultApi.md#putAccountAlias) | **POST** /control/put-account-alias | 
[**registerSlackWorkspaceForOrganization**](DefaultApi.md#registerSlackWorkspaceForOrganization) | **POST** /control/register-slack-workspace-for-organization | 
[**updateSlackChannelConfiguration**](DefaultApi.md#updateSlackChannelConfiguration) | **POST** /control/update-slack-channel-configuration | 



## createSlackChannelConfiguration

> Object createSlackChannelConfiguration(createSlackChannelConfigurationRequest, opts)



&lt;p&gt;Creates a Slack channel configuration for your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can add up to 5 Slack workspaces for your account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can add up to 20 Slack channels for your account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;A Slack channel can have up to 100 Amazon Web Services accounts. This means that only 100 accounts can add the same Slack channel to the Amazon Web Services Support App. We recommend that you only add the accounts that you need to manage support cases for your organization. This can reduce the notifications about case updates that you receive in the Slack channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;We recommend that you choose a private Slack channel so that only members in that channel have read and write access to your support cases. Anyone in your Slack channel can create, update, or resolve support cases for your account. Users require an invitation to join private channels. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let createSlackChannelConfigurationRequest = new AwsSupportApp.CreateSlackChannelConfigurationRequest(); // CreateSlackChannelConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSlackChannelConfiguration(createSlackChannelConfigurationRequest, opts, (error, data, response) => {
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
 **createSlackChannelConfigurationRequest** | [**CreateSlackChannelConfigurationRequest**](CreateSlackChannelConfigurationRequest.md)|  | 
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


## deleteAccountAlias

> Object deleteAccountAlias(opts)



Deletes an alias for an Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccountAlias(opts, (error, data, response) => {
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

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSlackChannelConfiguration

> Object deleteSlackChannelConfiguration(deleteSlackChannelConfigurationRequest, opts)



Deletes a Slack channel configuration from your Amazon Web Services account. This operation doesn&#39;t delete your Slack channel.

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let deleteSlackChannelConfigurationRequest = new AwsSupportApp.DeleteSlackChannelConfigurationRequest(); // DeleteSlackChannelConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSlackChannelConfiguration(deleteSlackChannelConfigurationRequest, opts, (error, data, response) => {
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
 **deleteSlackChannelConfigurationRequest** | [**DeleteSlackChannelConfigurationRequest**](DeleteSlackChannelConfigurationRequest.md)|  | 
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


## deleteSlackWorkspaceConfiguration

> Object deleteSlackWorkspaceConfiguration(deleteSlackWorkspaceConfigurationRequest, opts)



Deletes a Slack workspace configuration from your Amazon Web Services account. This operation doesn&#39;t delete your Slack workspace.

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let deleteSlackWorkspaceConfigurationRequest = new AwsSupportApp.DeleteSlackWorkspaceConfigurationRequest(); // DeleteSlackWorkspaceConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSlackWorkspaceConfiguration(deleteSlackWorkspaceConfigurationRequest, opts, (error, data, response) => {
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
 **deleteSlackWorkspaceConfigurationRequest** | [**DeleteSlackWorkspaceConfigurationRequest**](DeleteSlackWorkspaceConfigurationRequest.md)|  | 
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


## getAccountAlias

> GetAccountAliasResult getAccountAlias(opts)



Retrieves the alias from an Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccountAlias(opts, (error, data, response) => {
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

[**GetAccountAliasResult**](GetAccountAliasResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSlackChannelConfigurations

> ListSlackChannelConfigurationsResult listSlackChannelConfigurations(listSlackChannelConfigurationsRequest, opts)



Lists the Slack channel configurations for an Amazon Web Services account.

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let listSlackChannelConfigurationsRequest = new AwsSupportApp.ListSlackChannelConfigurationsRequest(); // ListSlackChannelConfigurationsRequest | 
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
apiInstance.listSlackChannelConfigurations(listSlackChannelConfigurationsRequest, opts, (error, data, response) => {
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
 **listSlackChannelConfigurationsRequest** | [**ListSlackChannelConfigurationsRequest**](ListSlackChannelConfigurationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListSlackChannelConfigurationsResult**](ListSlackChannelConfigurationsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSlackWorkspaceConfigurations

> ListSlackWorkspaceConfigurationsResult listSlackWorkspaceConfigurations(listSlackChannelConfigurationsRequest, opts)



Lists the Slack workspace configurations for an Amazon Web Services account.

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let listSlackChannelConfigurationsRequest = new AwsSupportApp.ListSlackChannelConfigurationsRequest(); // ListSlackChannelConfigurationsRequest | 
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
apiInstance.listSlackWorkspaceConfigurations(listSlackChannelConfigurationsRequest, opts, (error, data, response) => {
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
 **listSlackChannelConfigurationsRequest** | [**ListSlackChannelConfigurationsRequest**](ListSlackChannelConfigurationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListSlackWorkspaceConfigurationsResult**](ListSlackWorkspaceConfigurationsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putAccountAlias

> Object putAccountAlias(putAccountAliasRequest, opts)



Creates or updates an individual alias for each Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let putAccountAliasRequest = new AwsSupportApp.PutAccountAliasRequest(); // PutAccountAliasRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccountAlias(putAccountAliasRequest, opts, (error, data, response) => {
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
 **putAccountAliasRequest** | [**PutAccountAliasRequest**](PutAccountAliasRequest.md)|  | 
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


## registerSlackWorkspaceForOrganization

> RegisterSlackWorkspaceForOrganizationResult registerSlackWorkspaceForOrganization(registerSlackWorkspaceForOrganizationRequest, opts)



&lt;p&gt;Registers a Slack workspace for your Amazon Web Services account. To call this API, your account must be part of an organization in Organizations.&lt;/p&gt; &lt;p&gt;If you&#39;re the &lt;i&gt;management account&lt;/i&gt; and you want to register Slack workspaces for your organization, you must complete the following tasks:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Sign in to the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/app\&quot;&gt;Amazon Web Services Support Center&lt;/a&gt; and authorize the Slack workspaces where you want your organization to have access to. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html\&quot;&gt;Authorize a Slack workspace&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call the &lt;code&gt;RegisterSlackWorkspaceForOrganization&lt;/code&gt; API to authorize each Slack workspace for the organization.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;After the management account authorizes the Slack workspace, member accounts can call this API to authorize the same Slack workspace for their individual accounts. Member accounts don&#39;t need to authorize the Slack workspace manually through the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/app\&quot;&gt;Amazon Web Services Support Center&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To use the Amazon Web Services Support App, each account must then complete the following tasks:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Create an Identity and Access Management (IAM) role with the required permission. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html\&quot;&gt;Managing access to the Amazon Web Services Support App&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Configure a Slack channel to use the Amazon Web Services Support App for support cases for that account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/add-your-slack-channel.html\&quot;&gt;Configuring a Slack channel&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let registerSlackWorkspaceForOrganizationRequest = new AwsSupportApp.RegisterSlackWorkspaceForOrganizationRequest(); // RegisterSlackWorkspaceForOrganizationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerSlackWorkspaceForOrganization(registerSlackWorkspaceForOrganizationRequest, opts, (error, data, response) => {
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
 **registerSlackWorkspaceForOrganizationRequest** | [**RegisterSlackWorkspaceForOrganizationRequest**](RegisterSlackWorkspaceForOrganizationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegisterSlackWorkspaceForOrganizationResult**](RegisterSlackWorkspaceForOrganizationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSlackChannelConfiguration

> UpdateSlackChannelConfigurationResult updateSlackChannelConfiguration(updateSlackChannelConfigurationRequest, opts)



Updates the configuration for a Slack channel, such as case update notifications.

### Example

```javascript
import AwsSupportApp from 'aws_support_app';
let defaultClient = AwsSupportApp.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSupportApp.DefaultApi();
let updateSlackChannelConfigurationRequest = new AwsSupportApp.UpdateSlackChannelConfigurationRequest(); // UpdateSlackChannelConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSlackChannelConfiguration(updateSlackChannelConfigurationRequest, opts, (error, data, response) => {
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
 **updateSlackChannelConfigurationRequest** | [**UpdateSlackChannelConfigurationRequest**](UpdateSlackChannelConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSlackChannelConfigurationResult**](UpdateSlackChannelConfigurationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

