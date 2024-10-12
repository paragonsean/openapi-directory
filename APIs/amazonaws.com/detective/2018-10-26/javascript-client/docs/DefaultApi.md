# AmazonDetective.DefaultApi

All URIs are relative to *http://api.detective.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptInvitation**](DefaultApi.md#acceptInvitation) | **PUT** /invitation | 
[**batchGetGraphMemberDatasources**](DefaultApi.md#batchGetGraphMemberDatasources) | **POST** /graph/datasources/get | 
[**batchGetMembershipDatasources**](DefaultApi.md#batchGetMembershipDatasources) | **POST** /membership/datasources/get | 
[**createGraph**](DefaultApi.md#createGraph) | **POST** /graph | 
[**createMembers**](DefaultApi.md#createMembers) | **POST** /graph/members | 
[**deleteGraph**](DefaultApi.md#deleteGraph) | **POST** /graph/removal | 
[**deleteMembers**](DefaultApi.md#deleteMembers) | **POST** /graph/members/removal | 
[**describeOrganizationConfiguration**](DefaultApi.md#describeOrganizationConfiguration) | **POST** /orgs/describeOrganizationConfiguration | 
[**disableOrganizationAdminAccount**](DefaultApi.md#disableOrganizationAdminAccount) | **POST** /orgs/disableAdminAccount | 
[**disassociateMembership**](DefaultApi.md#disassociateMembership) | **POST** /membership/removal | 
[**enableOrganizationAdminAccount**](DefaultApi.md#enableOrganizationAdminAccount) | **POST** /orgs/enableAdminAccount | 
[**getMembers**](DefaultApi.md#getMembers) | **POST** /graph/members/get | 
[**listDatasourcePackages**](DefaultApi.md#listDatasourcePackages) | **POST** /graph/datasources/list | 
[**listGraphs**](DefaultApi.md#listGraphs) | **POST** /graphs/list | 
[**listInvitations**](DefaultApi.md#listInvitations) | **POST** /invitations/list | 
[**listMembers**](DefaultApi.md#listMembers) | **POST** /graph/members/list | 
[**listOrganizationAdminAccounts**](DefaultApi.md#listOrganizationAdminAccounts) | **POST** /orgs/adminAccountslist | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**rejectInvitation**](DefaultApi.md#rejectInvitation) | **POST** /invitation/removal | 
[**startMonitoringMember**](DefaultApi.md#startMonitoringMember) | **POST** /graph/member/monitoringstate | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateDatasourcePackages**](DefaultApi.md#updateDatasourcePackages) | **POST** /graph/datasources/update | 
[**updateOrganizationConfiguration**](DefaultApi.md#updateOrganizationConfiguration) | **POST** /orgs/updateOrganizationConfiguration | 



## acceptInvitation

> acceptInvitation(acceptInvitationRequest, opts)



&lt;p&gt;Accepts an invitation for the member account to contribute data to a behavior graph. This operation can only be called by an invited member account. &lt;/p&gt; &lt;p&gt;The request provides the ARN of behavior graph.&lt;/p&gt; &lt;p&gt;The member account status in the graph must be &lt;code&gt;INVITED&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let acceptInvitationRequest = new AmazonDetective.AcceptInvitationRequest(); // AcceptInvitationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.acceptInvitation(acceptInvitationRequest, opts, (error, data, response) => {
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
 **acceptInvitationRequest** | [**AcceptInvitationRequest**](AcceptInvitationRequest.md)|  | 
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


## batchGetGraphMemberDatasources

> BatchGetGraphMemberDatasourcesResponse batchGetGraphMemberDatasources(batchGetGraphMemberDatasourcesRequest, opts)



Gets data source package information for the behavior graph.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let batchGetGraphMemberDatasourcesRequest = new AmazonDetective.BatchGetGraphMemberDatasourcesRequest(); // BatchGetGraphMemberDatasourcesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetGraphMemberDatasources(batchGetGraphMemberDatasourcesRequest, opts, (error, data, response) => {
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
 **batchGetGraphMemberDatasourcesRequest** | [**BatchGetGraphMemberDatasourcesRequest**](BatchGetGraphMemberDatasourcesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetGraphMemberDatasourcesResponse**](BatchGetGraphMemberDatasourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGetMembershipDatasources

> BatchGetMembershipDatasourcesResponse batchGetMembershipDatasources(batchGetMembershipDatasourcesRequest, opts)



Gets information on the data source package history for an account.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let batchGetMembershipDatasourcesRequest = new AmazonDetective.BatchGetMembershipDatasourcesRequest(); // BatchGetMembershipDatasourcesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetMembershipDatasources(batchGetMembershipDatasourcesRequest, opts, (error, data, response) => {
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
 **batchGetMembershipDatasourcesRequest** | [**BatchGetMembershipDatasourcesRequest**](BatchGetMembershipDatasourcesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetMembershipDatasourcesResponse**](BatchGetMembershipDatasourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGraph

> CreateGraphResponse createGraph(createGraphRequest, opts)



&lt;p&gt;Creates a new behavior graph for the calling account, and sets that account as the administrator account. This operation is called by the account that is enabling Detective.&lt;/p&gt; &lt;p&gt;Before you try to enable Detective, make sure that your account has been enrolled in Amazon GuardDuty for at least 48 hours. If you do not meet this requirement, you cannot enable Detective. If you do meet the GuardDuty prerequisite, then when you make the request to enable Detective, it checks whether your data volume is within the Detective quota. If it exceeds the quota, then you cannot enable Detective. &lt;/p&gt; &lt;p&gt;The operation also enables Detective for the calling account in the currently selected Region. It returns the ARN of the new behavior graph.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateGraph&lt;/code&gt; triggers a process to create the corresponding data tables for the new behavior graph.&lt;/p&gt; &lt;p&gt;An account can only be the administrator account for one behavior graph within a Region. If the same account calls &lt;code&gt;CreateGraph&lt;/code&gt; with the same administrator account, it always returns the same behavior graph ARN. It does not create a new behavior graph.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let createGraphRequest = new AmazonDetective.CreateGraphRequest(); // CreateGraphRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createGraph(createGraphRequest, opts, (error, data, response) => {
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
 **createGraphRequest** | [**CreateGraphRequest**](CreateGraphRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateGraphResponse**](CreateGraphResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMembers

> CreateMembersResponse createMembers(createMembersRequest, opts)



&lt;p&gt; &lt;code&gt;CreateMembers&lt;/code&gt; is used to send invitations to accounts. For the organization behavior graph, the Detective administrator account uses &lt;code&gt;CreateMembers&lt;/code&gt; to enable organization accounts as member accounts.&lt;/p&gt; &lt;p&gt;For invited accounts, &lt;code&gt;CreateMembers&lt;/code&gt; sends a request to invite the specified Amazon Web Services accounts to be member accounts in the behavior graph. This operation can only be called by the administrator account for a behavior graph. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateMembers&lt;/code&gt; verifies the accounts and then invites the verified accounts. The administrator can optionally specify to not send invitation emails to the member accounts. This would be used when the administrator manages their member accounts centrally.&lt;/p&gt; &lt;p&gt;For organization accounts in the organization behavior graph, &lt;code&gt;CreateMembers&lt;/code&gt; attempts to enable the accounts. The organization accounts do not receive invitations.&lt;/p&gt; &lt;p&gt;The request provides the behavior graph ARN and the list of accounts to invite or to enable.&lt;/p&gt; &lt;p&gt;The response separates the requested accounts into two lists:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The accounts that &lt;code&gt;CreateMembers&lt;/code&gt; was able to process. For invited accounts, includes member accounts that are being verified, that have passed verification and are to be invited, and that have failed verification. For organization accounts in the organization behavior graph, includes accounts that can be enabled and that cannot be enabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The accounts that &lt;code&gt;CreateMembers&lt;/code&gt; was unable to process. This list includes accounts that were already invited to be member accounts in the behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let createMembersRequest = new AmazonDetective.CreateMembersRequest(); // CreateMembersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMembers(createMembersRequest, opts, (error, data, response) => {
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
 **createMembersRequest** | [**CreateMembersRequest**](CreateMembersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMembersResponse**](CreateMembersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGraph

> deleteGraph(deleteGraphRequest, opts)



&lt;p&gt;Disables the specified behavior graph and queues it to be deleted. This operation removes the behavior graph from each member account&#39;s list of behavior graphs.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DeleteGraph&lt;/code&gt; can only be called by the administrator account for a behavior graph.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let deleteGraphRequest = new AmazonDetective.DeleteGraphRequest(); // DeleteGraphRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteGraph(deleteGraphRequest, opts, (error, data, response) => {
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
 **deleteGraphRequest** | [**DeleteGraphRequest**](DeleteGraphRequest.md)|  | 
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


## deleteMembers

> DeleteMembersResponse deleteMembers(deleteMembersRequest, opts)



&lt;p&gt;Removes the specified member accounts from the behavior graph. The removed accounts no longer contribute data to the behavior graph. This operation can only be called by the administrator account for the behavior graph.&lt;/p&gt; &lt;p&gt;For invited accounts, the removed accounts are deleted from the list of accounts in the behavior graph. To restore the account, the administrator account must send another invitation.&lt;/p&gt; &lt;p&gt;For organization accounts in the organization behavior graph, the Detective administrator account can always enable the organization account again. Organization accounts that are not enabled as member accounts are not included in the &lt;code&gt;ListMembers&lt;/code&gt; results for the organization behavior graph.&lt;/p&gt; &lt;p&gt;An administrator account cannot use &lt;code&gt;DeleteMembers&lt;/code&gt; to remove their own account from the behavior graph. To disable a behavior graph, the administrator account uses the &lt;code&gt;DeleteGraph&lt;/code&gt; API method.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let deleteMembersRequest = new AmazonDetective.DeleteMembersRequest(); // DeleteMembersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMembers(deleteMembersRequest, opts, (error, data, response) => {
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
 **deleteMembersRequest** | [**DeleteMembersRequest**](DeleteMembersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteMembersResponse**](DeleteMembersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeOrganizationConfiguration

> DescribeOrganizationConfigurationResponse describeOrganizationConfiguration(describeOrganizationConfigurationRequest, opts)



&lt;p&gt;Returns information about the configuration for the organization behavior graph. Currently indicates whether to automatically enable new organization accounts as member accounts.&lt;/p&gt; &lt;p&gt;Can only be called by the Detective administrator account for the organization. &lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let describeOrganizationConfigurationRequest = new AmazonDetective.DescribeOrganizationConfigurationRequest(); // DescribeOrganizationConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeOrganizationConfiguration(describeOrganizationConfigurationRequest, opts, (error, data, response) => {
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
 **describeOrganizationConfigurationRequest** | [**DescribeOrganizationConfigurationRequest**](DescribeOrganizationConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeOrganizationConfigurationResponse**](DescribeOrganizationConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disableOrganizationAdminAccount

> disableOrganizationAdminAccount(opts)



&lt;p&gt;Removes the Detective administrator account in the current Region. Deletes the organization behavior graph.&lt;/p&gt; &lt;p&gt;Can only be called by the organization management account.&lt;/p&gt; &lt;p&gt;Removing the Detective administrator account does not affect the delegated administrator account for Detective in Organizations.&lt;/p&gt; &lt;p&gt;To remove the delegated administrator account in Organizations, use the Organizations API. Removing the delegated administrator account also removes the Detective administrator account in all Regions, except for Regions where the Detective administrator account is the organization management account.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disableOrganizationAdminAccount(opts, (error, data, response) => {
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


## disassociateMembership

> disassociateMembership(disassociateMembershipRequest, opts)



&lt;p&gt;Removes the member account from the specified behavior graph. This operation can only be called by an invited member account that has the &lt;code&gt;ENABLED&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DisassociateMembership&lt;/code&gt; cannot be called by an organization account in the organization behavior graph. For the organization behavior graph, the Detective administrator account determines which organization accounts to enable or disable as member accounts.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let disassociateMembershipRequest = new AmazonDetective.DisassociateMembershipRequest(); // DisassociateMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateMembership(disassociateMembershipRequest, opts, (error, data, response) => {
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
 **disassociateMembershipRequest** | [**DisassociateMembershipRequest**](DisassociateMembershipRequest.md)|  | 
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


## enableOrganizationAdminAccount

> enableOrganizationAdminAccount(enableOrganizationAdminAccountRequest, opts)



&lt;p&gt;Designates the Detective administrator account for the organization in the current Region.&lt;/p&gt; &lt;p&gt;If the account does not have Detective enabled, then enables Detective for that account and creates a new behavior graph.&lt;/p&gt; &lt;p&gt;Can only be called by the organization management account.&lt;/p&gt; &lt;p&gt;If the organization has a delegated administrator account in Organizations, then the Detective administrator account must be either the delegated administrator account or the organization management account.&lt;/p&gt; &lt;p&gt;If the organization does not have a delegated administrator account in Organizations, then you can choose any account in the organization. If you choose an account other than the organization management account, Detective calls Organizations to make that account the delegated administrator account for Detective. The organization management account cannot be the delegated administrator account.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let enableOrganizationAdminAccountRequest = new AmazonDetective.EnableOrganizationAdminAccountRequest(); // EnableOrganizationAdminAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.enableOrganizationAdminAccount(enableOrganizationAdminAccountRequest, opts, (error, data, response) => {
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
 **enableOrganizationAdminAccountRequest** | [**EnableOrganizationAdminAccountRequest**](EnableOrganizationAdminAccountRequest.md)|  | 
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


## getMembers

> GetMembersResponse getMembers(getMembersRequest, opts)



Returns the membership details for specified member accounts for a behavior graph.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let getMembersRequest = new AmazonDetective.GetMembersRequest(); // GetMembersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMembers(getMembersRequest, opts, (error, data, response) => {
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
 **getMembersRequest** | [**GetMembersRequest**](GetMembersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMembersResponse**](GetMembersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listDatasourcePackages

> ListDatasourcePackagesResponse listDatasourcePackages(listDatasourcePackagesRequest, opts)



Lists data source packages in the behavior graph.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let listDatasourcePackagesRequest = new AmazonDetective.ListDatasourcePackagesRequest(); // ListDatasourcePackagesRequest | 
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
apiInstance.listDatasourcePackages(listDatasourcePackagesRequest, opts, (error, data, response) => {
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
 **listDatasourcePackagesRequest** | [**ListDatasourcePackagesRequest**](ListDatasourcePackagesRequest.md)|  | 
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

[**ListDatasourcePackagesResponse**](ListDatasourcePackagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGraphs

> ListGraphsResponse listGraphs(listGraphsRequest, opts)



&lt;p&gt;Returns the list of behavior graphs that the calling account is an administrator account of. This operation can only be called by an administrator account.&lt;/p&gt; &lt;p&gt;Because an account can currently only be the administrator of one behavior graph within a Region, the results always contain a single behavior graph.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let listGraphsRequest = new AmazonDetective.ListGraphsRequest(); // ListGraphsRequest | 
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
apiInstance.listGraphs(listGraphsRequest, opts, (error, data, response) => {
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
 **listGraphsRequest** | [**ListGraphsRequest**](ListGraphsRequest.md)|  | 
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

[**ListGraphsResponse**](ListGraphsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listInvitations

> ListInvitationsResponse listInvitations(listInvitationsRequest, opts)



&lt;p&gt;Retrieves the list of open and accepted behavior graph invitations for the member account. This operation can only be called by an invited member account.&lt;/p&gt; &lt;p&gt;Open invitations are invitations that the member account has not responded to.&lt;/p&gt; &lt;p&gt;The results do not include behavior graphs for which the member account declined the invitation. The results also do not include behavior graphs that the member account resigned from or was removed from.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let listInvitationsRequest = new AmazonDetective.ListInvitationsRequest(); // ListInvitationsRequest | 
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
apiInstance.listInvitations(listInvitationsRequest, opts, (error, data, response) => {
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
 **listInvitationsRequest** | [**ListInvitationsRequest**](ListInvitationsRequest.md)|  | 
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

[**ListInvitationsResponse**](ListInvitationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listMembers

> ListMembersResponse listMembers(listMembersRequest, opts)



&lt;p&gt;Retrieves the list of member accounts for a behavior graph.&lt;/p&gt; &lt;p&gt;For invited accounts, the results do not include member accounts that were removed from the behavior graph.&lt;/p&gt; &lt;p&gt;For the organization behavior graph, the results do not include organization accounts that the Detective administrator account has not enabled as member accounts.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let listMembersRequest = new AmazonDetective.ListMembersRequest(); // ListMembersRequest | 
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
apiInstance.listMembers(listMembersRequest, opts, (error, data, response) => {
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
 **listMembersRequest** | [**ListMembersRequest**](ListMembersRequest.md)|  | 
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

[**ListMembersResponse**](ListMembersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listOrganizationAdminAccounts

> ListOrganizationAdminAccountsResponse listOrganizationAdminAccounts(listOrganizationAdminAccountsRequest, opts)



Returns information about the Detective administrator account for an organization. Can only be called by the organization management account.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let listOrganizationAdminAccountsRequest = new AmazonDetective.ListOrganizationAdminAccountsRequest(); // ListOrganizationAdminAccountsRequest | 
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
apiInstance.listOrganizationAdminAccounts(listOrganizationAdminAccountsRequest, opts, (error, data, response) => {
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
 **listOrganizationAdminAccountsRequest** | [**ListOrganizationAdminAccountsRequest**](ListOrganizationAdminAccountsRequest.md)|  | 
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

[**ListOrganizationAdminAccountsResponse**](ListOrganizationAdminAccountsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Returns the tag values that are assigned to a behavior graph.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the behavior graph for which to retrieve the tag values.
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
 **resourceArn** | **String**| The ARN of the behavior graph for which to retrieve the tag values. | 
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


## rejectInvitation

> rejectInvitation(rejectInvitationRequest, opts)



&lt;p&gt;Rejects an invitation to contribute the account data to a behavior graph. This operation must be called by an invited member account that has the &lt;code&gt;INVITED&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt; &lt;code&gt;RejectInvitation&lt;/code&gt; cannot be called by an organization account in the organization behavior graph. In the organization behavior graph, organization accounts do not receive an invitation.&lt;/p&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let rejectInvitationRequest = new AmazonDetective.RejectInvitationRequest(); // RejectInvitationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rejectInvitation(rejectInvitationRequest, opts, (error, data, response) => {
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
 **rejectInvitationRequest** | [**RejectInvitationRequest**](RejectInvitationRequest.md)|  | 
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


## startMonitoringMember

> startMonitoringMember(startMonitoringMemberRequest, opts)



&lt;p&gt;Sends a request to enable data ingest for a member account that has a status of &lt;code&gt;ACCEPTED_BUT_DISABLED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For valid member accounts, the status is updated as follows.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If Detective enabled the member account, then the new status is &lt;code&gt;ENABLED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If Detective cannot enable the member account, the status remains &lt;code&gt;ACCEPTED_BUT_DISABLED&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let startMonitoringMemberRequest = new AmazonDetective.StartMonitoringMemberRequest(); // StartMonitoringMemberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startMonitoringMember(startMonitoringMemberRequest, opts, (error, data, response) => {
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
 **startMonitoringMemberRequest** | [**StartMonitoringMemberRequest**](StartMonitoringMemberRequest.md)|  | 
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


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Applies tag values to a behavior graph.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the behavior graph to assign the tags to.
let tagResourceRequest = new AmazonDetective.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The ARN of the behavior graph to assign the tags to. | 
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



Removes tags from a behavior graph.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the behavior graph to remove the tags from.
let tagKeys = ["null"]; // [String] | The tag keys of the tags to remove from the behavior graph. You can remove up to 50 tags at a time.
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
 **resourceArn** | **String**| The ARN of the behavior graph to remove the tags from. | 
 **tagKeys** | [**[String]**](String.md)| The tag keys of the tags to remove from the behavior graph. You can remove up to 50 tags at a time. | 
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


## updateDatasourcePackages

> updateDatasourcePackages(updateDatasourcePackagesRequest, opts)



Starts a data source packages for the behavior graph.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let updateDatasourcePackagesRequest = new AmazonDetective.UpdateDatasourcePackagesRequest(); // UpdateDatasourcePackagesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDatasourcePackages(updateDatasourcePackagesRequest, opts, (error, data, response) => {
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
 **updateDatasourcePackagesRequest** | [**UpdateDatasourcePackagesRequest**](UpdateDatasourcePackagesRequest.md)|  | 
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


## updateOrganizationConfiguration

> updateOrganizationConfiguration(updateOrganizationConfigurationRequest, opts)



Updates the configuration for the Organizations integration in the current Region. Can only be called by the Detective administrator account for the organization.

### Example

```javascript
import AmazonDetective from 'amazon_detective';
let defaultClient = AmazonDetective.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDetective.DefaultApi();
let updateOrganizationConfigurationRequest = new AmazonDetective.UpdateOrganizationConfigurationRequest(); // UpdateOrganizationConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateOrganizationConfiguration(updateOrganizationConfigurationRequest, opts, (error, data, response) => {
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
 **updateOrganizationConfigurationRequest** | [**UpdateOrganizationConfigurationRequest**](UpdateOrganizationConfigurationRequest.md)|  | 
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

